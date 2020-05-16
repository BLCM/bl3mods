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

mod = Mod('fix_dlc2_shield_drops.txt',
        'Fix DLC2 Shield Drops',
        [
            "Most enemies in DLC2 (Guns, Love, and Tentacles) don't actually drop",
            "shields.  For standard enemies, they're in the pool list but with a",
            "zero weight.  For badasses, they're absent entirely from the pool",
            "list.  We're fixing the Standard ones, but not bothering with Badasses",
            "for now.",
        ])

mod.reg_hotfix(Mod.CHAR, 'MatchAll',
        '/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Hibiscus',
        'ItemPools.ItemPools[6].PoolProbability.BaseValueAttribute',
        Mod.get_full_cond('/Game/GameData/Loot/ItemPools/Attributes/Att_Shields_DropOdds', 'GbxAttributeData'))
mod.close()
