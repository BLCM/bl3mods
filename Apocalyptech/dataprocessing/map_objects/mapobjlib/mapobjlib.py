#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

import os
import sys
import sqlite3

class MapObjects:
    """
    Class to let us get info about map-based objects.  This is a pretty
    stupidly-written class; if I ever make this stuff more formal, it could
    use a full rewrite.
    """

    def __init__(self):

        self.sqldb = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'map_objects.sqlite3'))
        if not os.path.exists(self.sqldb):
            print('This mod-generation script requires some pretty weird data setup to')
            print('happen first, in my dataprocessing/map_objects dir.  Browse around')
            print('in there (and in this script\'s code) if you\'re feeling brave!')
            print('')
            print(f'DB Location: {self.sqldb}')
            sys.exit(1)

        self.db = sqlite3.connect(self.sqldb)
        self.db.row_factory = sqlite3.Row
        self.curs = self.db.cursor()

    def is_datatype(self, classname):
        """
        Checks to see if the given classname is a valid data type
        """
        self.curs.execute('select id from datatype where name=?', (classname,))
        if self.curs.fetchone() is None:
            return False
        else:
            return True

    def is_level(self, level):
        """
        Checks to see if the given level name is a valid level
        """
        self.curs.execute('select id from map where name=?', (level,))
        if self.curs.fetchone() is None:
            return False
        else:
            return True

    def get_by_type(self, classname, level=None):
        """
        Given a `classname`, yield tuples describing the map objects
        found of that type.  tuple[0] is the map name (suitable for
        a level-based hotfix), tuple[1] is the full object path.
        Optionally pass in `level` to restrict results to a specific
        level.
        """

        # SQL Parameters
        selects = [
                'm.name map_name',
                'm.base_path base_path',
                's.name submap_name',
                'o.name obj_name',
                ]
        froms = [
                'map m',
                'submap s',
                'object o',
                'datatype t',
                ]
        wheres = [
                # Just assuming these will all be ANDs
                't.name=?',
                't.id=o.typeid',
                'o.submapid=s.id',
                's.mapid=m.id',
                ]
        orders = [
                'map_name',
                'submap_name',
                'obj_name',
                ]

        # Doing slightly different query if a level is specified
        if level is None:
            query_tuple = (classname,)
        else:
            wheres.append('m.name=?')
            query_tuple = (classname, level)

        # Construct the SQL
        sql = 'SELECT {} FROM {} WHERE {} ORDER BY {}'.format(
                ', '.join(selects),
                ', '.join(froms),
                ' AND '.join(wheres),
                ', '.join(orders),
                )

        # Run the query
        self.curs.execute(sql, query_tuple)
        for row in self.curs:
            yield (
                    row['map_name'], 
                    '{}/{}.{}:{}'.format(
                        row['base_path'],
                        row['submap_name'],
                        row['submap_name'],
                        row['obj_name'],
                        ),
                    )

