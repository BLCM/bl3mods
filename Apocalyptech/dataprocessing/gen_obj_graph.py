#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2020 Christopher J. Kucera
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

import argparse
import subprocess
from bl3data.bl3data import BL3Data

parser = argparse.ArgumentParser(
        description='Generate a graphviz representation of an object',
        epilog="""
        Given an object name, and a "base" output filename, generates a graphviz dotfile
        representing the relationships between the various exports in there.  Will use
        the `output` arg in the files `output.dot`, `output.png`, and `output.svg`.  Will
        generate both PNG and SVG exports, in addition to the raw dotfile.
        """
        )
parser.add_argument('-o', '--output',
        type=str,
        required=True,
        help='Base output filename for .dot and .png',
        )
parser.add_argument('object',
        nargs=1,
        help='Object name to generate',
        )
args = parser.parse_args()
obj_name = args.object[0]
obj_short = obj_name.split('/')[-1]

class Link:
    
    def __init__(self, attr, target):
        self.attr = attr
        self.target = target

class Export:

    def __init__(self, data):
        self.data = data
        self.export_type = data['export_type']
        self.idx = data['_jwp_export_idx']
        self.asset = data['_jwp_is_asset']
        self.name = data['_jwp_object_name']
        self.links = []
        self.has_incoming = False

def loop_obj(export, struct, cur_path=''):
    global exports
    struct_type = type(struct)
    if struct_type == dict:
        if 'export' in struct:
            if struct['export'] != 0:
                export.links.append(Link(cur_path, exports[struct['export']]))
                exports[struct['export']].has_incoming = True
            return
        for key, val in struct.items():
            if cur_path == '':
                new_path = key
            else:
                new_path = '{}.{}'.format(cur_path, key)
            loop_obj(export, val, new_path)
    elif struct_type == list:
        for idx, val in enumerate(struct):
            loop_obj(export, val, '{}[{}]'.format(cur_path, idx))
    elif struct_type == str or struct_type == int or struct_type == float or struct_type == bool:
        return
    else:
        raise RuntimeError('Unknown datatype: {}'.format(struct_type))

# Grab the data
data = BL3Data()
obj = data.get_data(obj_name)
exports = {}
for export_data in obj:
    export = Export(export_data)
    exports[export.idx] = export

# Process the links
for export in exports.values():
    loop_obj(export, export.data)

# Generate the graphviz .dot file
filename_dot = '{}.dot'.format(args.output)
filename_svg = '{}.svg'.format(args.output)
filename_png = '{}.png'.format(args.output)
with open(filename_dot, 'w') as df:

    # Open the file
    print('digraph {} {{'.format(obj_short), file=df)
    print('', file=df)

    # First enumerate all the exports
    print('    // Exports', file=df)
    for idx, export in sorted(exports.items()):
        if export.has_incoming or export.links:
            if export.asset:
                extra = ',style=filled,fillcolor=green'
            else:
                extra = ''
            print('    e{} [label=<{}<br/><i>type: {}</i><br/>{}>{}];'.format(
                export.idx,
                export.name,
                export.export_type,
                export.idx,
                extra,
                ), file=df)
    print('', file=df)

    # Now the links
    print('    // Links', file=df)
    for export in exports.values():
        for link in export.links:
            print('    e{} -> e{} [label=<{}>];'.format(
                export.idx,
                link.target.idx,
                link.attr,
                ), file=df)

    # Close it out
    print('}', file=df)

print('Wrote graphviz dotfile to {}'.format(filename_dot))

# Convert to .png
subprocess.call(['dot', '-Tpng', filename_dot, '-o', filename_png])
print('Converted to {}'.format(filename_png))

# Convert to .svg
subprocess.call(['dot', '-Tsvg', filename_dot, '-o', filename_svg])
print('Converted to {}'.format(filename_svg))

