#!/usr/bin/env python3
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

import csv
import json
import lzma

# Generating a mapping of "short" balance name to english label, for use
# in bl3-cli-saveedit.  I basically already did this for my Balance
# spreadsheets, so I may as well just reuse that data.

output_file = 'short_name_balance_mapping.json.xz'
files = [
        'artifact_balances.csv',
        'com_balances.csv',
        'grenade_balances.csv',
        'gun_balances.csv',
        'shield_balances.csv',
        ]

rarity_map = {
        '01/common': 'White',
        '01/common (starting gear)': 'White',
        '02/uncommon': 'Green',
        '03/rare': 'Blue',
        '03/rare e-tech': 'Blue E-Tech',
        '04/very rare': 'Purple',
        '04/very rare e-tech': 'Purple E-Tech',
        '05/legendary': 'Legendary',
        }

# Main Mapping object.  Filling in some hardcodes here, first.
mapping = {
        'balance_atl_ar_portals': 'Portals and Shite',
        'balance_eridian_fabricator': 'Eridian Fabricator',
        'balance_ps_tediore_babymaker_salvage': 'Baby Maker (fixed part)',
        'balance_ps_jak_lovedrill': 'Love Drill (mission version)',
        'balance_sm_hyp_shortstick': 'Short Stick',
        'balance_ps_jak_theseventhsense_missionweapon': 'Seventh Sense (mission version)',
        'balance_ps_jak_ss_l': 'Seventh Sense (ghost Burton version)',
        'balance_ps_jak_seventhsense': 'Seventh Sense (unknown version)',
        }

# Now loop through our CSVs and pull out the info.
for filename in files:
    with open(filename) as df:
        reader = csv.DictReader(df)
        for row in reader:
            balance = row['Balance'].lower()
            rarity = row['Rarity'].lower()
            if 'Gun Type' in row:
                if rarity == 'named weapon':
                    label = row['Manufacturer/Name']
                else:
                    guntype = row['Gun Type'][:-1]
                    label = '{} {} {}'.format(
                            rarity_map[rarity],
                            row['Manufacturer/Name'],
                            guntype,
                            )
            elif 'Character/Name' in row:
                # Our balance sheet takes pains to point out some COM balances which only
                # come from the Trials bosses, but for these purposes we don't care, so
                # I'm stripping that out.
                if 'trials boss' in row['Character/Name'].lower():
                    com_name = row['Character/Name'].split(' (', 1)[0]
                else:
                    com_name = row['Character/Name']
                label = '{} {} COM'.format(
                        com_name.replace(' - ', ' '),
                        rarity_map[rarity],
                        )
            elif 'Type/Name' in row:
                if rarity_map[rarity] == 'Legendary' and row['Type/Name'] != 'Legendary':
                    label = '{} {} Artifact'.format(
                            row['Type/Name'],
                            rarity_map[rarity],
                            )
                else:
                    label = '{} Artifact'.format(rarity_map[rarity])
            else:
                if 'grenade' in filename:
                    type_name = 'Grenade'
                else:
                    type_name = 'Shield'
                if rarity.startswith('named'):
                    label = '{}'.format(
                            row['Manufacturer/Name'],
                            )
                else:
                    label = '{} {} {}'.format(
                            row['Manufacturer/Name'],
                            rarity_map[rarity],
                            type_name,
                            )

            mapping[balance] = label

# Write out
with lzma.open(output_file, 'wt') as df:
    json.dump(mapping, df, separators=(',', ':'))
print('Written to {}'.format(output_file))

