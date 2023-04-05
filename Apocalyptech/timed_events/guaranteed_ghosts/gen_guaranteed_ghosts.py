#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2022 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF

mod = Mod('guaranteed_ghosts.bl3hotfix',
        'Guaranteed Ghosts',
        'Apocalyptech',
        [
            "Guaranteed ghosts everywhere, so long as the Bloody Harvest",
            "event is on.  Just an extracted version of at hotfix deployed",
            "by GBX on Oct 31, 2019, with a few additions to the same",
            "DataTable object.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.1',
        cats='event, enemy',
        )

table = '/Game/PatchDLC/BloodyHarvest/GameData/Balance/BloodyHarvest/DataTable_Season_Halloween'

mod.comment('Default: 0.45')
mod.table_hotfix(Mod.PATCH, '',
        table,
        'ChanceToSpawnAsHaunted',
        'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
        1)
mod.newline()

mod.comment('Also guarantee badasses?  No idea on the default here, may already be 1.')
mod.table_hotfix(Mod.PATCH, '',
        table,
        'ChanceToSpawnAsHaunted_Badass',
        'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
        1)
mod.newline()

mod.comment('Also guarantee ghosts on Urn break')
mod.table_hotfix(Mod.PATCH, '',
        table,
        'Lootable_Urn_GhostSpawnChance',
        'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
        1)
mod.newline()

mod.comment('Also on ammo boxes')
mod.table_hotfix(Mod.PATCH, '',
        table,
        'Lootable_Box_GhostSpawnChance',
        'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
        1)
mod.newline()

mod.close()
