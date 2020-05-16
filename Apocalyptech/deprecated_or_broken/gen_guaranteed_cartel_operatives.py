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

mod = Mod('guaranteed_cartel_operatives.txt',
        'Revenge of the Cartels: Guaranteed Operatives',
        'Apocalyptech',
        [
            "All spawns which can generate operatives should do so.  This is",
            "actually a bit much, I stopped using it after a couple of tests.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

mod.table_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Event2/GameData/Balance/DataTable_Event02_Cartels',
        'OperativeSpawnChance',
        'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
        1)

mod.close()
