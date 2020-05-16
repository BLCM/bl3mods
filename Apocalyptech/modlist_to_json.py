#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
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
import json
import argparse

parser = argparse.ArgumentParser(
        description='Converts modlist.txt style BL3 modsets to JSON compatible with c0dycode\'s injector',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )

parser.add_argument('-m', '--modlist',
        type=str,
        default='modlist.txt',
        help='File to read mod sets from',
        )

parser.add_argument('-o', '--output',
        type=str,
        default='modlist.json',
        help='JSON file to output',
        )

parser.add_argument('-f', '--force',
        action='store_true',
        help='Overwrite output file without prompting',
        )

parser.add_argument('-v', '--verbose',
        action='store_true',
        help='Verbose output (show modfile contents as it goes)',
        )

args = parser.parse_args()

if os.path.exists(args.output) and not args.force:
    sys.stdout.write('WARNING: {} already exists.  Overwrite [y/N]? '.format(args.output))
    sys.stdout.flush()
    response = sys.stdin.readline().strip().lower()
    if len(response) == 0 or response[0] != 'y':
        print('Aborting!')
        sys.exit(1)
    print('')

if not os.path.exists(args.modlist):
    print('ERROR: {} does not exist'.format(args.modlist))
    sys.exit(1)

def process_modfile(modpath, prefix, verbose=False):

    to_ret = []
    with open(modpath, encoding='utf-8') as mod_df:
        hf_counter = 0
        for linenum, modline in enumerate(mod_df):
            modline = modline.strip()
            if verbose:
                print('{} line {}: {}'.format(modpath, linenum+1, modline))
            if modline == '' or modline.startswith('#'):
                continue

            # Check for prefix
            hf_counter += 1
            hftype, hf = modline.split(',', 1)
            key = '{}-Apoc{}-{}'.format(hftype, prefix, hf_counter)
            to_ret.append((key, hf))

    if verbose:
        print('')
    return to_ret

# Start constructing
json_out = {
        'service_name': 'Micropatch',
        'configuration_group': 'OakDefault',
        'configuration_version': '1.0',
        'parameters': [],
        }
mod_count = 0
with open(args.modlist, encoding='utf-8') as modlist_df:
    for line in modlist_df:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue

        modpath = '{}.txt'.format(line)
        if not os.path.exists(modpath):
            print('WARNING: {} was not found, skipping...'.format(modpath))
            continue

        print('Processing: {}'.format(modpath))
        for (key, value) in process_modfile(modpath, '{:X}'.format(mod_count), verbose=args.verbose):
            json_out['parameters'].append({'key': key, 'value': value})
        mod_count += 1

# Write out
with open(args.output, 'w') as json_df:
    json.dump(json_out, json_df, indent='  ')

# Report!
print('Done!  Wrote {} mods (with {} total hotfixes) to {}'.format(
    mod_count,
    len(json_out['parameters']),
    args.output,
    ))
