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

mod = Mod('fewer_cartel_operatives.txt',
        'Revenge of the Cartels: Fewer Operatives',
        'Apocalyptech',
        [
            "I enjoy having Cartel operatives pop up all over the place and",
            "provide a bit more chaos, but at their stock spawn rates, nearly",
            "every enemy encounter ends up as a total scrum.  When I'm not",
            "actively hunting them down for a Cartels mission, I'd like to",
            "ease off a bit without getting rid of them entirely.  So this",
            "just cuts their spawn probability in half.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Default value: 0.3
mod.table_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Event2/GameData/Balance/DataTable_Event02_Cartels',
        'OperativeSpawnChance',
        'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
        0.15)

mod.close()
