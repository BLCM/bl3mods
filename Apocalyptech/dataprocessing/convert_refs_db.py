#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2022 Christopher J. Kucera
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
import sys
import appdirs
import subprocess
import configparser

# The stanza we expect to see (including vars used by populate_refs_db.py):
#
#    [mysql]
#    host = localhost
#    port = 3306
#    user = bl3refs
#    passwd = password
#    db = bl3refs
#    mysql2sqlite = /usr/local/dv/virtualenv/mysql2sqlite/bin/mysql2sqlite
#    notice2 = Not used by bl3data anymore, but IS used by populate_refs_db.py
#
# (The "notice2" isn't actually important, just a note to myself.)

# Load the config (~/.config/bl3data/bl3data.ini on Linux, if using defaults)
config_dir = appdirs.user_config_dir('bl3data')
config_file = os.path.join(config_dir, 'bl3data.ini')
config = configparser.ConfigParser()
config.read(config_file)

host = config['mysql']['host']
port = config['mysql']['port']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
db = config['mysql']['db']
mysql2sqlite = config['mysql']['mysql2sqlite']

# Construct filenames
file_sql = f'{db}.sql'
file_sql_zip = f'{db}.zip'
file_sqlite = f'{db}.sqlite3'
file_sqlite_zip = f'{db}.sqlite3.zip'

# Now a raw SQL dump
print('')
print('Dumping SQL first...')
print('')
if os.path.exists(file_sql_zip):
    os.unlink(file_sql_zip)
with open(file_sql, 'w') as odf:
    subprocess.run(['mysqldump',
        '-u', user,
        f'-p{passwd}',
        '-h', host,
        f'-P{port}',
        db,
        ], stdout=odf)
subprocess.run(['zip', file_sql_zip, file_sql])
os.unlink(file_sql)

# Now a sqlite conversion
print('')
print('Now doing SQLite dump/conversion...')
print('')
if os.path.exists(file_sqlite):
    os.unlink(file_sqlite)
if os.path.exists(file_sqlite_zip):
    os.unlink(file_sqlite_zip)
cp = subprocess.run([mysql2sqlite,
    '-f', file_sqlite,
    '-d', db,
    '-u', user,
    '-h', host,
    '-P', port,
    '-V',
    '-p', passwd,
    ])
if cp.returncode == 0:
    subprocess.run(['zip', file_sqlite_zip, file_sqlite])

# Report
print('')
subprocess.run(['ls', '-lh', file_sql_zip, file_sqlite, file_sqlite_zip])
print('')

