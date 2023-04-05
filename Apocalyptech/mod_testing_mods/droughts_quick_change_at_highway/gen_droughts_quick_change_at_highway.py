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
import math
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('droughts_quick_change_at_highway.bl3hotfix',
        "Droughts Quick Change at Highway Fast Travel",
        'Apocalyptech',
        [
            "Moves the Quick Change machine in The Droughts to near the",
            "Highway Fast Travel, instead of at the Crimson Raiders'",
            "temporary base at the beginning.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='maps',
        )

base_obj = '/Game/Maps/Zone_0/Prologue/Prologue_P.Prologue_P:PersistentLevel.BP_QuickChange_2'
mod.reg_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
        f'{base_obj}.RootComponent',
        'RelativeLocation',
        '(X=47497,Y=21135,Z=-3849)',
        notify=True)
mod.reg_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
        f'{base_obj}.RootComponent',
        'RelativeRotation',
        '(Pitch=0,Yaw=95,Roll=5)',
        notify=True)

mod.close()
