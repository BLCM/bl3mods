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

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('disable_email_loyalty_rewards.txt',
        'Disable Email Loyalty Rewards',
        'Apocalyptech',
        [
            "Disables the email rewards given out for 100 kills for each manufacturer type.",
            "This does NOT interfere with the 'Rewards Card' achievement, though you don't",
            "get any notification from the game that you've met the requirements for the",
            "individual manufacturer types.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

for manufacturer in [
        'Atlas',
        'CoV',
        'Dahl',
        'Hyperion',
        'Jakobs',
        'Maliwan',
        'Tediore',
        'Torgue',
        'Vladof',
        ]:
    mod.reg_hotfix(Mod.PATCH, '',
            f'/Game/GameData/Challenges/Manufacturer/ManufacturerRewards/Challenge_ManufacturerRewardReward_{manufacturer}.Default__Challenge_ManufacturerRewardReward_{manufacturer}_C',
            'NPCMailDataRowHandles',
            '()')

    # This statement could be used to alter the point at which you get the rewards, but
    # it's finnicky -- if you "miss" the number (due to mod-application shenanigans or
    # whatever) the reward will never actually fire, so I figured I wouldn't mess with
    # that, in the end.  Setting to -1 makes 'em reward on *every* kill, FWIW.
    #mod.reg_hotfix(Mod.PATCH, '',
    #        f'/Game/GameData/Challenges/Manufacturer/ManufacturerRewards/Challenge_ManufacturerRewardReward_{manufacturer}.Default__Challenge_ManufacturerRewardReward_{manufacturer}_C',
    #        'StatChallengeTests.StatChallengeTests[0].GoalInfo.GoalInfo[0]',
    #        f'(GoalValue=100,NotificationThreshold=100)')

mod.close()
