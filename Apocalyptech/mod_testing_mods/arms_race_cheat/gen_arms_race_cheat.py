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
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('arms_race_cheat.bl3hotfix',
        'Arms Race Cheat',
        'Apocalyptech',
        [
            "Various cheats for Arms Race, primarily intended for mod testing.",
            "Specifically, makes the player basically invulnerable, the enemies",
            "one-shottable by practically anything, and increases the first",
            "Murdercane timer to six hours.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='armsrace, cheat',
        )

def change(row, value):
    global mod
    mod.table_hotfix(Mod.LEVEL, 'FrostSite_P',
            '/Game/PatchDLC/Ixora/GameData/Balance/Table_GearUp_Combat_Balance',
            row,
            'Value_138_7567CFEB4E1077623BE84EBC11D10EB8',
            value)

mod.comment('Player basically takes no damage')
change('PlayerDamageTakenScale', 0.001)
mod.newline()

mod.comment('Enemies are super-lame')
change('EnemyAccuracyScale', 0.001)
change('EnemyHealthScale', 0.001)
change('EnemyHealthPerHumanPlayerScale', 0)
change('EnemyHealthScalePerDeathCircle', 0)
mod.newline()

mod.comment('Six-hour time window')
mod.reg_hotfix(Mod.LEVEL, 'FrostSite_P',
        '/Game/PatchDLC/Ixora/GameData/Mode/FrostSiteGearUpData',
        'DeathCircleStages.DeathCircleStages[0].StableSeconds.BaseValueConstant',
        60*60*6)
mod.newline()

mod.close()
