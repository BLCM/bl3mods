#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
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

import re
import os
import sys
import lzma
import glob
import sqlite3

# Constants
sqldb = 'map_objects.sqlite3'
datadir = '/games/bl3_decrypt/extracted'
dumpsdir = '/games/bl3_steam/games/steamapps/common/Borderlands 3/OakGame/Binaries/Win64/data'
mapglobs = [
        '/*/Maps/*',
        '/Game/Maps/ProvingGrounds/*',
        '/Game/Maps/Slaughters/*',
        '/Game/Maps/Zone_?/*',
        '/Game/PatchDLC/BloodyHarvest/Maps/Seasons/BloodyHarvest',
        '/Game/PatchDLC/Event2/Maps',
        '/Game/PatchDLC/Raid1/Maps/Raid',
        '/Game/PatchDLC/Takedown2/Maps',
        '/Ixora2/Maps/Mystery/*',
        ]
blocklist = set([
    # These will get skipped anyway, but this way we won't print anything about 'em
    '/Alisma/Maps/Gyms',
    '/Dandelion/Maps/Vignettes',
    '/Engine/Maps/Templates',
    '/Game/Maps/ProvingGrounds',
    '/Game/Maps/ProvingGrounds/Trial0',
    '/Game/Maps/ProvingGrounds/Trial2',
    '/Game/Maps/Slaughters',
    '/Game/Maps/Zone_0',
    '/Game/Maps/Zone_1',
    '/Game/Maps/Zone_2',
    '/Game/Maps/Zone_3',
    '/Game/Maps/Zone_3/Grotto',
    '/Game/Maps/Zone_4',
    '/Game/Maps/Zone_4/FinalVault',
    '/Geranium/Maps/TestMaps',
    '/Hibiscus/Maps/Vignettes',
    '/Ixora2/Maps/Mystery',
    ])
dumpdir_blocklist = set([
    # Likewise
    'cyclone_blade_sonic',
    'cyclone_hover_mg_light_digi',
    'cyclone_mono_saw_heavy_fire',
    'cyclone_wide_needle_heavyboost',
    'outrunner_dune_blaze',
    'outrunner_hover_mg_shotgun_light_boost',
    'outrunner_twitchy_tesla_swarmer_heavy_energy',
    'outrunner_zip_flame_heavymissile_laser',
    'technical_allterrain_fuel',
    'technical_barbed_mg_sticky_lt_jet',
    'technical_hover_flak_tire_heavy_passenger',
    'technical_monster_barrel_meat_toxic',
    ])


# Classes
class Map():

    def __init__(self, name, path, idnum):
        self.name = name
        self.path = path
        self.idnum = idnum
        self.submaps = []

    def __repr__(self):
        return f'Map<{self.name},{self.idnum}>'

class SubMap():

    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum

    def __repr__(self):
        return f'SubMap<{self.name},{self.idnum}>'

# Connect to the DB and truncate it
db = sqlite3.connect(sqldb)
curs = db.cursor()
curs.execute('PRAGMA foreign_keys = ON')
curs.execute('delete from object')
curs.execute('delete from datatype')
curs.execute('delete from submap')
curs.execute('delete from map')
curs.execute('delete from sqlite_sequence')
db.commit()

# Get a list of maps that we'll be processing
map_objs = {}
submap_objs = {}
for mapglob in mapglobs:
    for filename in glob.glob(f'{datadir}{mapglob}'):
        if os.path.isdir(filename):
            base_path = filename[len(datadir):]
            if base_path in blocklist:
                continue
            underscore_p = list(glob.glob(f'{datadir}{base_path}/*_[Pp].umap'))
            if len(underscore_p) == 0:
                print(f'Skipping {base_path}, does not contain LevelName_P.umap')
                continue
            elif len(underscore_p) > 1:
                print(f'ERROR: {base_path} has more than one *_P.umap')
                sys.exit(1)

            # First store the main map object
            print(f'Finding sub-maps for {base_path}...')
            base_name = underscore_p[0].split('/')[-1].rsplit('.', 1)[0]
            curs.execute('insert into map (name, base_path) values (?, ?)', (base_name, base_path))
            map_obj = Map(base_name, base_path, curs.lastrowid)
            assert(base_name.lower() not in map_objs)
            map_objs[base_name.lower()] = map_obj

            # Now find all the sub-maps
            for newfile in glob.glob(f'{datadir}{base_path}/*.umap'):
                sub_base_name = newfile.split('/')[-1].rsplit('.', 1)[0]
                curs.execute('insert into submap (mapid, name) values (?, ?)', (map_obj.idnum, sub_base_name))
                submap_obj = SubMap(sub_base_name, curs.lastrowid)
                map_obj.submaps.append(submap_obj)
                assert(sub_base_name not in submap_objs)
                submap_objs[sub_base_name] = submap_obj
db.commit()

# Okay, now it's time to loop through our objects lists
datatypes = {}
digit_re = re.compile(r'^(?P<main>.*)_(?P<digit>\d+)$')
for dumpdir in glob.glob(f'{dumpsdir}/*/*'):

    if os.path.isdir(dumpdir):

        last_path = dumpdir.split('/')[-1]
        if last_path in dumpdir_blocklist:
            continue
        if last_path.lower() not in map_objs:
            print(f'WARNING: {last_path} not found, skipping...')
            continue
        print(f'Finding map objects for {last_path}')

        regex_str = r'^\[\d+\] [0-9A-F]+ (?P<datatype>[a-zA-Z0-9_]+) (?P<submap>({})+)\.(?P=submap)\.(?P<obj_path>\S+)\s*$'.format(
                '|'.join([s.name for s in map_objs[last_path.lower()].submaps]),
                )
        #print(regex_str)

        obj_re = re.compile(regex_str)
        with lzma.open(f'{dumpdir}/UE4Tools_ObjectsDump.txt.xz', 'rt', encoding='utf-8') as df:
            for line in df:
                if match := obj_re.match(line):

                    # Grab info about the object
                    datatype = match.group('datatype')
                    submap = match.group('submap')
                    obj_path = match.group('obj_path')

                    # If we've got a digit suffix, we probably have to subtract one.
                    if digitmatch := digit_re.match(obj_path):
                        digit = int(digitmatch.group('digit'))
                        if digit == 0:
                            print(f'ERROR: No clue what to do with: {submap} {obj_path}')
                            sys.exit(1)
                        obj_path = '{}_{}'.format(
                                digitmatch.group('main'),
                                digit-1,
                                )

                    # Check to make sure we've got this datatype in our DB
                    if datatype not in datatypes:
                        curs.execute('insert into datatype (name) values (?)', (datatype,))
                        datatypes[datatype] = curs.lastrowid

                    # Now input
                    curs.execute('insert into object (submapid, typeid, name) values (?, ?, ?)', (
                        submap_objs[submap].idnum,
                        datatypes[datatype],
                        obj_path,
                        ))

        db.commit()

