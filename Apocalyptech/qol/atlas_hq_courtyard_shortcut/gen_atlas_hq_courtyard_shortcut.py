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

mod = Mod('atlas_hq_courtyard_shortcut.bl3hotfix',
        'Atlas HQ Courtyard Shortcut',
        'Apocalyptech',
        [
            "Adds a food cart with an umbrella just to the right when leaving the",
            "Bank area in Atlas HQ and heading to the promenade/courtyard, which",
            "allows you to climb up to the promenade level without having to walk",
            "all the way around.",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.1',
        cats='qol, maps',
        ss=['https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/qol/atlas_hq_courtyard_shortcut/screenshot.jpg'],
        )

mod.mesh_hotfix('/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_P',
        '/Game/LevelArt/Environments/Promethea/AtlasHQ/Props/Food_Cart/Model/Mesh/SM_Food_Cart',
        location=(9641, 7275, -1150),
        rotation=(0, 45, 0),
        )
mod.newline()

mod.close()
