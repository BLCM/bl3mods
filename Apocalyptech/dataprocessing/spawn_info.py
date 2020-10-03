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

import sys
import argparse
import collections
from bl3data.bl3data import BL3Data

# Little util to get info about SpawnOptions objects easily

Report = collections.namedtuple('Report', [
    'actor',
    'probability',
    'weight',
    ])

# Args
parser = argparse.ArgumentParser(description='Spawn Info')
parser.add_argument('spawn_name',
        nargs='+',
        help='SpawnOptions objects to look up',
        )
args = parser.parse_args()

# Now process
data = BL3Data()
for obj_name in args.spawn_name:

    all_exports = data.get_data(obj_name)
    optiondata = data.get_exports(obj_name, 'SpawnOptionData')[0]

    to_report = []
    for idx, option in enumerate(optiondata['Options']):
        export_idx = option['Factory']['export']
        factory = all_exports[export_idx-1]
        if 'AIActorClass' in factory:
            actor = factory['AIActorClass']['asset_path_name']
        elif 'Options' in factory:
            actor = factory['Options'][1]
        else:
            raise Exception('{}: Unknown data in Factory export {} (option {})'.format(
                obj_name,
                export_idx,
                idx,
                ))
        advertised_prob = option['Probability']

        # Figure out the actual weights used.  This either isn't always entirely accurate,
        # or else the advertised percentage isn't always right.  For instance, in
        # /Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_TowersBadasses
        # indicies 6-9 claim to be using EGbxParamValueMode::Value, which by this logic
        # would end up being weighted at 0.6.  The advertised percentage is 0%, though.
        weightparam = option['WeightParam']
        if weightparam['ValueMode'] == 'EGbxParamValueMode::Value':
            weight = weightparam['Range']['Value']
            variance = weightparam['Range']['Variance']
            if variance == 0:
                weight = str(weight)
            else:
                weight = f'{weight} ~{variance}'
        elif weightparam['ValueMode'] == 'EGbxParamValueMode::AttributeInitializationData':
            weight = str(data.process_bvc_struct(weightparam['AttributeInitializationData']))
        else:
            raise Exception('{}: Option {}: unknown ValueMode: {}'.format(
                obj_name,
                idx,
                weightparam['ValueMode'],
                ))

        # Add to report list
        to_report.append(Report(actor, advertised_prob, weight))

    # Now report
    print('Object: {}'.format(obj_name))
    max_prob_len = max([len(r.probability) for r in to_report])
    max_weight_len = max([len(r.weight) for r in to_report])
    format_str = ' {}: {:>' + str(max_prob_len) + '} ({:>' + str(max_weight_len) + '}) {}'
    for idx, report in enumerate(to_report):
        print(format_str.format(idx, report.probability, report.weight, report.actor))
    print('')

