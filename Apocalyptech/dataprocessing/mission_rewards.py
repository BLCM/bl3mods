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

from bl3data.bl3data import BL3Data

# Used to generate data for gen_mission_reward_randomizer.py

bl3data = BL3Data()

AR='AR'
HW='HW'
PS='PS'
SG='SG'
SM='SM'
SR='SR'
SH='SH'
GM='GM'
CM='CM'
AF='AF'
SK='SK'
HD='HD'
TK='TK'
RD='RD'

mission_data = list(bl3data.find_data('/Game/Missions', 'Mission_'))
mission_data += list(bl3data.find_data('/Game/PatchDLC/Dandelion/Missions', 'Mission_'))
mission_data += list(bl3data.find_data('/Game/PatchDLC/Hibiscus/Missions', 'EP0'))
mission_data += list(bl3data.find_data('/Game/PatchDLC/Hibiscus/Missions', 'Mission_'))
mission_data += list(bl3data.find_data('/Game/PatchDLC/Hibiscus/Missions', 'SideMission_'))
mission_data += list(bl3data.find_data('/Game/PatchDLC/CitizenScience/Missions', 'Mission_'))
mission_data += list(bl3data.find_data('/Game/PatchDLC/Geranium/Missions', 'Mission_'))

# Missions not not alert on, when we would otherwise have output.  Just so's I
# don't keep getting messages for missions that I've looked at and don't care about.
mission_no_alert = {
        # More than one reward
        '/Game/Missions/Side/Zone_1/City/Mission_WizardOfNogs',
        '/Game/Missions/Side/Zone_2/Prison/Mission_FreeHugs',

        # Multiple reward types
        '/Game/Missions/Side/Zone_0/Prologue/Mission_UnderwearTink',

        # No standard reward types
        '/Game/Missions/Side/Zone_2/Wetlands/Mission_DriveAwayThePain',
        '/Game/Missions/Plot/Mission_Ep21_Beachhead',
        '/Game/PatchDLC/Hibiscus/Missions/Plot/EP05_DLC2',
        }

written = 0
out_file = 'mission_rewards_output.txt'
with open(out_file, 'w') as df:

    for (obj_name, obj) in mission_data:
        if obj is None:
            pass
            #print('{} could not be serialized'.format(obj_name))
        else:
            multiple_reward_tracker = []
            for part in obj:
                if part['export_type'] == 'OakMissionRewardData':
                    if 'ItemPoolReward' in part:
                        reward_pool_full = part['ItemPoolReward']['asset_path_name']
                        reward_pool = reward_pool_full.split('.')[0]

                        pool_data = bl3data.get_data(reward_pool)
                        pool_contents = []
                        for pool_part in pool_data:
                            if pool_part['export_type'] == 'ItemPoolData':
                                for item_idx, item in enumerate(pool_part['BalancedItems']):
                                    item_name = None
                                    if 'export' in item['ItemPoolData']:
                                        if 'export' in item['ResolvedInventoryBalanceData']:
                                            if obj_name not in mission_no_alert:
                                                print('WARNING: no pool or balance found in idx {} of {}'.format(item_idx, reward_pool))
                                                print('')
                                            continue
                                        else:
                                            item_name = item['ResolvedInventoryBalanceData'][1]
                                    else:
                                        item_name = item['ItemPoolData'][1]
                                    pool_contents.append(item_name)

                        # Debugging stuff
                        if False:
                            if len(pool_contents) > 0:
                                print('{}:'.format(obj_name))
                                for reward in pool_contents:
                                    print(' * {}'.format(reward))
                                print('')

                        reward_types = set()
                        for reward in pool_contents:
                            if '_AR_' in reward or '_AssaultRifles_' in reward:
                                reward_types.add(AR)
                            elif '_HW_' in reward:
                                reward_types.add(HW)
                            elif '_PS_' in reward:
                                reward_types.add(PS)
                            elif '_SG_' in reward or '_Shotguns_' in reward:
                                reward_types.add(SG)
                            elif '_SM_' in reward or '_SMGs_' in reward:
                                reward_types.add(SM)
                            elif '_SR_' in reward:
                                reward_types.add(SR)
                            elif '_Shield_' in reward or '_SH_' in reward:
                                reward_types.add(SH)
                            elif '_GrenadeMod_' in reward or '_GM_' in reward:
                                reward_types.add(GM)
                            elif '_Artifact_' in reward:
                                reward_types.add(AF)
                            elif '/Skins/' in reward or '/PlayerSkin/' in reward:
                                reward_types.add(SK)
                            elif '/Heads/' in reward:
                                reward_types.add(HD)
                            elif 'WeaponTrinket' in reward:
                                reward_types.add(TK)
                            elif 'RoomDecoration' in reward:
                                reward_types.add(RD)
                            else:
                                if obj_name not in mission_no_alert:
                                    print('{} -> {}'.format(obj_name, reward))

                        # Figure out what the rest of the object name that we're going to set will
                        # look like
                        last_bit = obj_name.split('/')[-1]
                        obj_extra = 'Default__{}_C:RewardData_OakMissionRewardData'.format(last_bit)

                        # Handle some special cases.  Object names taken from UUU ObjectName dumps
                        if 'Mission_WizardOfNogs' in obj_name and reward_types == set([HD]):
                            # Technical NOGout; there's an optional objective reward in there which is
                            # supposed to do the NOG head thing, which doesn't work.  Whatever.
                            obj_extra = 'OBJ_MissionRewardSkin_Objective:OakMissionRewardData_5'
                        elif 'Mission_FreeHugs' in obj_name:
                            # On the Blood Path
                            if reward_types == set([SH]):
                                obj_extra = 'OBJ_TalkwithHugs_Objective:OakMissionRewardData_8'
                            elif reward_types == set([SG]):
                                obj_extra = 'OBJ_SideWithGangLeader_Objective:OakMissionRewardData_8'
                            else:
                                raise Exception('Unknown reward_types for Blood Path: {}'.format(reward_types))

                        # Write out STUFF
                        if len(reward_types) == 0:
                            if obj_name not in mission_no_alert:
                                print('No standard reward types found for {} ({})'.format(obj_name, reward_pool))
                                print('')
                        elif len(reward_types) > 1:
                            if obj_name not in mission_no_alert:
                                print('Multiple reward types for {} ({}): {}'.format(obj_name, reward_pool, reward_types))
                                print('')
                        else:
                            print("('{}.{}', {}),".format(
                                obj_name,
                                obj_extra,
                                list(reward_types)[0],
                                ), file=df)
                            written += 1
                            multiple_reward_tracker.append(reward_types)

            if len(multiple_reward_tracker) > 1:
                # Going to omit reporting on instances I've already looked at and don't care about
                if obj_name not in mission_no_alert:
                    print('{}: more than one reward (info only, lines were written)'.format(obj_name))
                    for reward in multiple_reward_tracker:
                        print(' * {}'.format(reward))
                    print('')

print('Wrote {} lines to {}'.format(written, out_file))
print('')
