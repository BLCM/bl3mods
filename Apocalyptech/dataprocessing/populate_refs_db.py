#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import io
import sys
import time
import struct
import MySQLdb
import subprocess

from bl3data.bl3data import BL3Data

# create table bl3object
# (
#     id int not null auto_increment,
#     name varchar(512) character set latin1 not null,
#     primary key (id),
#     unique index idx_name (name)
# ) engine=innodb;
# 
# create table bl3refs
# (
#     from_obj int not null,
#     to_obj int not null,
#     unique index idx_from (from_obj, to_obj),
#     index idx_to (to_obj, from_obj)
# ) engine=innodb;

# Objects which generate a *ton* of refs.  I have hand-pruned them from the DB
# for now, but they should probably be blacklisted or something here.
#
#   /Game/Common/_Design/BPLevelAssetLists - 13485 entries in the "from" field
#
# (actually, turned out to be just the one.  Next biggest in "from" was in
# the 400s, which I'm fine with, and the biggest in "to" was less than 2k,
# which is a lot but it seems fine.)
#
# select from_obj, count(from_obj) from bl3refs group by from_obj having count(from_obj) > N
# select to_obj, count(to_obj) from bl3refs group by to_obj having count(to_obj) > N

blacklist_from = {
        '/game/common/_design/bplevelassetlists',
        }
blacklist_to = {
        }

# Abusing our bl3data class to connect to the DB, here.
data = BL3Data()
data._connect_db()
db = data.db
curs = data.curs

# Let's time this.  Obviously the ETA comparison will vary if you're not
# on my machine.
estimated_secs = 826
start_time = time.time()

# Go ahead and auto-truncate first
print('Truncating database...')
curs.execute('truncate bl3refs')
curs.execute('truncate bl3object')
db.commit()

def insert(db, curs, objname):
    curs.execute('insert into bl3object (name) values (%s)', (objname,))
    new_id = curs.lastrowid
    return new_id

def insert_ref(db, curs, from_num, to_num):
    curs.execute('insert into bl3refs (from_obj, to_obj) values (%s, %s)', (from_num, to_num))

def read_int(df):
    return struct.unpack('<i', df.read(4))[0]

def read_str(df):
    strlen = read_int(df)
    if strlen < 0:
        strlen = abs(strlen)
        return df.read(strlen*2)[:-2].decode('utf_16_le')
    else:
        return df.read(strlen)[:-1].decode('latin1')

objects = {}
toplevels = set()
obj_count = 0

for (dirpath, dirnames, filenames) in os.walk('extracted'):
    for filename in filenames:
        if filename.endswith('.uasset') or filename.endswith('.umap'):

            refs = set()
            full_filename = os.path.join(dirpath, filename)

            # Get our object name
            if filename.endswith('.uasset'):
                cur_obj_name = full_filename[9:-7]
            else:
                cur_obj_name = full_filename[9:-5]
            cur_obj_name_lower = cur_obj_name.lower()
            if cur_obj_name_lower in toplevels:
                print('WARNING: Found duplicate name {} in {}'.format(cur_obj_name, full_filename))
            else:
                toplevels.add(cur_obj_name_lower)

            # Add the object name to the DB if it's not already there
            if cur_obj_name_lower not in objects:
                objects[cur_obj_name_lower] = insert(db, curs, cur_obj_name)

            # Process the file.  I'm assuming (perhaps wrongly?) that this'll be faster than
            # parsing 'strings', though of course it depends on me parsin the file correctly.
            syms = []
            with open(full_filename, 'rb') as df:
                # There's a string 28 bytes in, so we can't use entirely absolute positioning.
                # Could be that there's some other strings in here we're unaware of, of course.
                df.seek(28)
                read_str(df)
                # Then there's a bunch of ints we skip (again, maybe some of these are actually
                # zero-length strings?)
                df.seek(80, io.SEEK_CUR)
                num_symbols = read_int(df)
                # Then a bunch more possibly-zero-strengh-length ints
                df.seek(72, io.SEEK_CUR)
                # Now we're ready to actually read our symbols
                for _ in range(num_symbols):
                    syms.append(read_str(df))
                    read_int(df)
            for sym in syms:
                # We're allowing non-/Game objects now, but don't allow /Script/.
                if sym.startswith('/') and not sym.startswith('/Script/'):
                    obj_name_lower = sym.lower()
                    if obj_name_lower != cur_obj_name_lower and obj_name_lower not in refs:
                        refs.add(obj_name_lower)
                        # Insert into the DB
                        if obj_name_lower not in objects:
                            objects[obj_name_lower] = insert(db, curs, sym)
                        insert_ref(db, curs, objects[cur_obj_name_lower], objects[obj_name_lower])

            #for line in subprocess.run(['/usr/bin/strings', full_filename],
            #            capture_output=True,
            #            text=True,
            #            ).stdout.split():
            #    if line.startswith('/Game/'):
            #        obj_name_lower = line.lower()
            #        if obj_name_lower != cur_obj_name_lower and obj_name_lower not in refs:
            #            refs.add(obj_name_lower)
            #            # Insert into the DB
            #            if obj_name_lower not in objects:
            #                objects[obj_name_lower] = insert(db, curs, line)
            #            insert_ref(db, curs, objects[cur_obj_name_lower], objects[obj_name_lower])

            # Commit any changes and report, if need be
            obj_count += 1
            if obj_count % 100 == 0:
                cur_time = time.time()
                elapsed = int(cur_time-start_time)
                remaining = estimated_secs - elapsed
                if remaining >= 0:
                    mins = int(remaining/60)
                    secs = remaining % 60
                    eta = '{}m{}s remaining'.format(mins, secs)
                else:
                    eta = '---- remaining'
                print('Processed {} objects (of ~169500, post-DLC4 patch (200967 in DB)) | {}...'.format(obj_count, eta))
                db.commit()

# Ensure that we've committed
db.commit()

# Cleanup at the end -- automatically get rid of /Game/Common/_Design/BPLevelAssetLists "from" refs
# Untested!
for obj_name in sorted(blacklist_from):
    if obj_name in objects:
        print('Clearing "from" refs from {}'.format(obj_name))
        curs.execute('delete from bl3refs where from_obj=%s', (objects[obj_name],))
    else:
        print('WARNING: could not find blacklisted {}'.format(obj_name))
for obj_name in sorted(blacklist_to):
    if obj_name in objects:
        print('Clearing "to" refs from {}'.format(obj_name))
        curs.execute('delete from bl3refs where to_obj=%s', (objects[obj_name],))
    else:
        print('WARNING: could not find blacklisted {}'.format(obj_name))
db.commit()

# Report on the number of records in the DB
curs.execute('select count(name) as name_count from bl3object')
row = curs.fetchone()
print('New records in DB: {}'.format(row[0]))

# And close
db.close()
end_time = time.time()
elapsed = int(end_time-start_time)
mins = int(elapsed/60)
secs = elapsed % 60
print('Finished in {}m{}s ({} seconds)'.format(mins, secs, elapsed))

