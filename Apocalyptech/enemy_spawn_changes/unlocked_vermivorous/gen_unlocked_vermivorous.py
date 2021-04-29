#!/usr/bin/env python
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

mod = Mod('unlocked_vermivorous.bl3hotfix',
        'Unlocked Vermivorous',
        'Apocalyptech',
        [
            "Ordinarily, Vermivorous only spawns during the Hemovorous fight when you're",
            "in Mayhem 6 or higher.  This mod will make Vermivorous spawn during that",
            "battle regardless of Mayhem level."
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='spawns',
        )

# For some reason, using `BPChar_VarkidSuperBadass_Raid` here for the char
# target does *not* work.  Things must be a little weird during the Varkid
# evolutions.
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
        '/Ixora2/Enemies/Varkid/_Unique/RaidBoss/_Design/Evolutions/BPChar_VarkidSuperBadass_Raid.Default__BPChar_VarkidSuperBadass_Raid_C',
        'SecondBossSpawnMayhemThreshold',
        1)

mod.close()
