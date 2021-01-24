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

import sys
import argparse
import subprocess
sys.path.append('../../python_mod_helpers')
from bl3data.bl3data import BL3Data

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

def loop_obj(export_map, export, struct, cur_path=''):
    struct_type = type(struct)
    if struct_type == dict:
        if 'export' in struct:
            if struct['export'] != 0:
                export.links.append(Link(cur_path, export_map[struct['export']]))
                export_map[struct['export']].has_incoming = True
            return
        for key, val in struct.items():
            if cur_path == '':
                new_path = key
            else:
                new_path = '{}.{}'.format(cur_path, key)
            loop_obj(export_map, export, val, new_path)
    elif struct_type == list:
        for idx, val in enumerate(struct):
            loop_obj(export_map, export, val, '{}[{}]'.format(cur_path, idx))
    elif struct_type == str or struct_type == int or struct_type == float or struct_type == bool:
        return
    else:
        raise RuntimeError('Unknown datatype: {}'.format(struct_type))

def process_dotfile(data, obj_name, base_name=None, do_png=False, do_svg=False, verbose=True):

    # Figure out our base_name if needed
    obj_short = obj_name.split('/')[-1]
    if not base_name:
        base_name = obj_short

    # Grab the data
    obj = data.get_data(obj_name)
    exports = {}
    for export_data in obj:
        export = Export(export_data)
        exports[export.idx] = export

    # Process the links
    for export in exports.values():
        loop_obj(exports, export, export.data)

    # Generate the graphviz .dot file
    filename_dot = '{}.dot'.format(base_name)
    filename_svg = '{}.svg'.format(base_name)
    filename_png = '{}.png'.format(base_name)
    with open(filename_dot, 'w') as df:

        # Open the file
        print('digraph {} {{'.format(obj_short), file=df)
        print('', file=df)

        # Put a header in there
        print('    // Header', file=df)
        print('    labelloc = "t";', file=df)
        print('    fontsize = 24;', file=df)
        print('    label = <{}>;'.format(obj_name), file=df)
        print('', file=df)

        # First enumerate all the exports
        print('    // Exports', file=df)
        for _, export in sorted(exports.items()):
            if export.has_incoming or export.links:
                if export.asset:
                    extratitle = ' (asset)'
                    extra = ',style=filled,fillcolor=green'
                else:
                    extratitle = ''
                    extra = ''
                print('    e{} [label=<{}{}<br/><i>type: {}</i><br/>{}>{}];'.format(
                    export.idx,
                    export.name,
                    extratitle,
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

    if verbose:
        print('Wrote graphviz dotfile to {}'.format(filename_dot))

    # Convert to .png
    if do_png:
        subprocess.call(['dot', '-Tpng', filename_dot, '-o', filename_png])
        if verbose:
            print('Converted to {}'.format(filename_png))

    # Convert to .svg
    if do_svg:
        subprocess.call(['dot', '-Tsvg', filename_dot, '-o', filename_svg])
        if verbose:
            print('Converted to {}'.format(filename_svg))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description='Generate a graphviz representation of an object',
            epilog="""
            Given an object name, generates a graphviz dotfile representing the relationships
            between the various exports in there.  The `--output` argument will be used as the
            base filename for the files `output.dot`, `output.png`, and `output.svg`, and will
            default to the "short" name of the object if not given (ie: the last path component
            in the object name).  Will generate both PNG and SVG exports by default, in addition
            to the raw dotfile.  To generate *only* PNG or SVG, specify `--png` or `--svg`.
            """
            )
    parser.add_argument('-o', '--output',
            type=str,
            required=False,
            help="""Base output filename for .dot and .png (will default to the "short" name
            of the object, if not specified)""",
            )
    parser.add_argument('-p', '--png',
            action='store_true',
            help='Write only to PNG',
            )
    parser.add_argument('-s', '--svg',
            action='store_true',
            help='Write only to SVG',
            )
    parser.add_argument('object',
            nargs=1,
            help='Object name to generate',
            )

    args = parser.parse_args()
    obj_name = args.object[0]
    do_png = args.png
    do_svg = args.svg
    if not do_png and not do_svg:
        do_png = True
        do_svg = True

    data = BL3Data()
    process_dotfile(data, obj_name,
            base_name=args.output,
            do_png=do_png,
            do_svg=do_svg,
            )

