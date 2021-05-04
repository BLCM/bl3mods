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

import sys
import argparse
from mapobjlib.mapobjlib import MapObjects

# Args
parser = argparse.ArgumentParser(description='Find some stuff')

parser.add_argument('-c', '--classname',
        type=str,
        required=True,
        help='Class Name to look up',
        )

parser.add_argument('-m', '--mapname',
        type=str,
        required=False,
        help='Map name to look in',
        )

args = parser.parse_args()

mo = MapObjects()

# First make sure we have a valid datatype, for the purposes of friendly
# error messages
if not mo.is_datatype(args.classname):
    print('Classname "{}" is unknown'.format(args.classname))
    sys.exit(1)

# May as well do the same for the level, if we've been given it.
if args.mapname:
    if not mo.is_level(args.mapname):
        print('Map name "{}" is unknown'.format(args.mapname))
        sys.exit(1)

# Now do the main lookup
for level, obj_name in mo.get_by_type(args.classname, level=args.mapname):
    print(obj_name)

