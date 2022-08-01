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

mod = Mod('no_wasted_equipment.bl3hotfix',
        'No Wasted Equipment',
        'Apocalyptech',
        [
            "Adjusts the character-specific weighting so that you won't get COMs,",
            "customizations, or anointments for any character other than the one",
            "you're currently playing.  Theoretically this should work just fine",
            "in multiplayer, though I haven't tested it at all in that mode.",
            "",
            "This does *not* affect specific gear drops from named enemies/bosses!",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.1',
        cats='loot-system, qol',
        )

mod.comment("Yep, this single statement should do it!  Rather nicer than the BL2/TPS versions.")
mod.comment("Default weighting: 0.15 (the character Atts add 0.85 when the char is present)")
mod.table_hotfix(Mod.PATCH, '',
        '/Game/GameData/Economy/Economy_Miscellaneous',
        'CharacterWeights_Base',
        'Value',
        BVCF(bvc=0))

mod.close()
