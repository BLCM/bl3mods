#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2023 Christopher J. Kucera
# <cj@apocalyptech.com>
# <https://apocalyptech.com/contact.php>
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

mod = Mod('digbys_smooth_tube_audio_fix.bl3pakinfo',
        "Digby's Smooth Tube Audio Fix",
        'Apocalyptech',
        [
            "Fixes the broken audio for Digby's Smooth Tube by reverting its custom",
            "soundbank back to its original state, after it had gotten broken by the",
            "2020-06-11 Guardian Takedown patch.  Note that there is *no* hotfix",
            "component to this mod!  You don't actually have to import this file into",
            "either OHL or B3HM.  The actual fix is contained in the associated",
            "pakfile.  Get that installed along with your existing pakfiles, and",
            "you'll be good to go.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic='The pakfile contents included here are owned by Gearbox/2K/whoever-technically-owns-that-stuff',
        v='1.0.0',
        cats='bugfix',
        pakfile='Digbys_Smooth_Tube_Audio_Fix_999999_P.pak',
        )

mod.close()
