#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('beef_plissken_loot_pattern_fix.bl3hotfix',
        'Beef Plissken Loot Pattern Fix',
        'Apocalyptech',
        [
            "Beef Plissken has a loot drop pattern which is custom-built for his in-story",
            "death sequence, which shoots the loot up onto the platform he just jumped from.",
            "When returning to the area later, though, you just kill Beef as usual, and that",
            "loot pattern has a tendency to shoot the loot off the edge of the map, making",
            "the loot unobtainable. This replaces Beef's drop pattern with the usual enemy",
            "drop pattern.  This ends up dropping his loot on top of the masher gears when",
            "going through the DLC6 story, but you can hop onto them without getting killed",
            "so the loot is still retrievable during the plot mission, too.",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol, enemy, bugfix',
        )

mod.reg_hotfix(Mod.CHAR, 'BPChar_Punk_BanditChief',
        '/Ixora2/Enemies/CotV/Punk/BanditChief/_Design/Character/BPChar_Punk_BanditChief.BPChar_Punk_BanditChief_C:AIBalanceState_GEN_VARIABLE',
        'DropLootPattern',
        Mod.get_full_cond('/Game/GameData/Loot/SpawnPatterns/LootSpawnPattern_Enemy', 'LootSpawnPatternData'))

mod.close()
