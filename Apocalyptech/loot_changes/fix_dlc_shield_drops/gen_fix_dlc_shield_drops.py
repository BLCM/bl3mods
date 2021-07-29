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
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('fix_dlc_shield_drops.bl3hotfix',
        'Fix DLC Shield Drops',
        'Apocalyptech',
        [
            "Most enemies in DLC2 (Guns, Love, and Tentacles) don't actually drop",
            "shields, and some enemies in DLC4 (Psycho Krieg) have a very odd shield",
            "drop configuration as well.  For DLC2 standard enemies, they're in the",
            "pool list but with a zero weight.  For DCL2 badasses, they're absent",
            "entirely from the pool list.  We're fixing the DLC2 Standard ones, but",
            "not bothering with Badasses for now.",
            "",
            "For DLC4 standard enemies, they won't drop non-DLC-specific shields, though",
            "I don't know how widespread that issue is.  Regardless, this should fix",
            "it up for the ones that have the problem.  This DLC4 fix is also included",
            "in my DLC Loot De-Emphasizer mod.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.1.0',
        cats='bugfix',
        )

# DLC2 Fix
mod.comment('DLC2')
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
        '/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Hibiscus',
        'ItemPools.ItemPools[6].PoolProbability.BaseValueAttribute',
        Mod.get_full_cond('/Game/GameData/Loot/ItemPools/Attributes/Att_Shields_DropOdds', 'GbxAttributeData'))
mod.newline()

# DLC4 Fix
mod.comment('DLC4')
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
        '/Game/PatchDLC/Alisma/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Alisma',
        'ItemPools.ItemPools[5]',
        """(
            ItemPool={},
            PoolProbability={},
            NumberOfTimesToSelectFromThisPool={}
        )""".format(
            Mod.get_full_cond('/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All', 'ItemPoolData'),
            BVCF(bva='/Game/GameData/Loot/ItemPools/Attributes/Att_Shields_DropOddsWithMayhem_Total'),
            BVCF(bvc=1),
            ))
mod.newline()

# And done.
mod.close()

