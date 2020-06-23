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

mod = Mod('achievement_shenanigans.txt',
        "Achievement Shenanigans",
        'Apocalyptech',
        [
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Win a duel
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/GameData/Challenges/System/BP_Challenge_Console_8.Default__BP_Challenge_Console_8_C',
#        'StatChallengeTests.StatChallengeTests[0]',
#        """(
#            StatId={},
#            GoalInfo=(
#                (
#                    GoalValue=6849,
#                    NotificationThreshold=6849
#                )
#            )
#        )""".format(Mod.get_full_cond('/Game/PlayerCharacters/_Shared/_Design/Stats/Combat/Weapon/Stat_Weapon_SMGKills', 'GameStatData')))

# Revive a co-op partner
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Challenges/System/BP_Challenge_Console_9.Default__BP_Challenge_Console_9_C',
        'StatChallengeTests.StatChallengeTests[0]',
        """(
            StatId={},
            GoalInfo=(
                (
                    GoalValue=6850,
                    NotificationThreshold=6850
                )
            )
        )""".format(Mod.get_full_cond('/Game/PlayerCharacters/_Shared/_Design/Stats/Combat/Weapon/Stat_Weapon_SMGKills', 'GameStatData')))

mod.close()
