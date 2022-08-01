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

mod = Mod('equal_character_gear_chance.bl3hotfix',
        'Equal Character Gear Chance',
        'Apocalyptech',
        [
            "Adjusts the character-specific weighting so that character-specific",
            "gear (such as COMs, customizations, and anointments) should drop at",
            "about equal rates, instead of being weighted towards the currently-",
            "active characters.  This is basically the opposite of my No Wasted",
            "Equipment mod.",
            "",
            "This is really only intended for my own mod-testing purposes, and",
            "might have some unintended consequences when used in ordinary",
            "gameplay, so beware!  COMs, customizations, and character-specific",
            "anointments are likely to start overpowering all other loot.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.1',
        cats='loot-system',
        )

mod.comment("This could be done more gracefully, but I'm just setting the \"base\"")
mod.comment("character-specific weight to 200.  Each character class in-game")
mod.comment("adds 0.85 to this value, which is negligible compared to the 200.")
mod.table_hotfix(Mod.PATCH, '',
        '/Game/GameData/Economy/Economy_Miscellaneous',
        'CharacterWeights_Base',
        'Value',
        BVCF(bvc=200))

mod.close()
