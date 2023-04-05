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

import sys
sys.path.append('../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF

mod = Mod('trivial_vc.txt',
        'Trivial Vault Cards',
        'Apocalyptech',
        [
            "Reduces the quantity required for all VC1 challenges down to 1.",
            "Doesn't affect the 'Kill This Boss' style challenges, since",
            "those are already at 1.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

data = BL3Data()
for obj_name, obj_data in sorted(data.glob_data('/Game/PatchDLC/VaultCard/Challenges/*/VC*/VC*Challenge_*')):
    last_bit = obj_name.split('/')[-1]
    for export in obj_data:
        if export['export_type'] == f'{last_bit}_C':
            if ('StatChallengeTests' in export and
                    len(export['StatChallengeTests']) > 0 and
                    'GoalInfo' in export['StatChallengeTests'][0]):

                # Err?
                assert(len(export['StatChallengeTests']) == 1)

                # What's our current goal?
                cur_goal = 0
                for goal in export['StatChallengeTests'][0]['GoalInfo']:
                    cur_goal = max(cur_goal, goal['GoalValue'])

                # If it's >1, mod it.
                if cur_goal > 1:
                    mod.comment(last_bit)

                    full_obj_name = '{}.{}'.format(obj_name, export['_jwp_object_name'])
                    for idx in range(len(export['StatChallengeTests'][0]['GoalInfo'])):

                        # Attempting to override the *entire* GoalInfo array (while
                        # at the same time shrinking it to a single entry) causes
                        # crashes.  Maybe we could get away with setting it all at
                        # once if we kept the number of elements the same, but eh.
                        # May as well just do this, instead.
                        mod.reg_hotfix(Mod.PATCH, '',
                                full_obj_name,
                                f'StatChallengeTests.StatChallengeTests[0].GoalInfo.GoalInfo[{idx}].GoalValue',
                                1)

                        mod.reg_hotfix(Mod.PATCH, '',
                                full_obj_name,
                                f'StatChallengeTests.StatChallengeTests[0].GoalInfo.GoalInfo[{idx}].NotificationThreshold',
                                1)

                    cur_goal_str = str(cur_goal)
                    for desc_field in ['Description', 'CompletedDescription']:
                        if desc_field in export and 'string' in export[desc_field]:
                            desc_str = export[desc_field]['string']
                            orig_desc_str = desc_str
                            if cur_goal_str in desc_str:
                                desc_str = '1'.join(desc_str.split(cur_goal_str))

                            # Buncha pluralization nonsense follows
                            desc_str = desc_str.replace(' the ', ' a ')
                            desc_str = desc_str.replace(' and ', ' and/or ')
                            desc_str = desc_str.replace(' & ', ' or ')
                            desc_str = desc_str.replace('ies', 'y')
                            desc_str = desc_str.replace('sses', 'ss')
                            desc_str = desc_str.replace('s Killed', ' Killed')
                            desc_str = desc_str.replace('Valkyry', 'Valkyrie')
                            if desc_str.endswith('s') and not desc_str.endswith('Boss'):
                                desc_str = desc_str[:-1]

                            if desc_str != orig_desc_str:
                                mod.reg_hotfix(Mod.PATCH, '',
                                        full_obj_name,
                                        desc_field,
                                        desc_str)

                    mod.newline()

mod.close()
