#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021-2022 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod, LVL_TO_ENG

mod = Mod('easy_entry_to_fort_sunshine.bl3hotfix',
        'Easy Entry to Fort Sunshine',
        'Apocalyptech',
        [
            "Adds a door-opening lever to the outside of Fort Sunshine, in Floodmoor Basin.",
            "During the game plot, you'll still need to ride the lumber conveyors into the",
            "fort in order to make progress, but the interior will be much easier to access",
            "outside of that mission.",
            "",
            "This mod requires either OpenHotfixLoader or B3HM v1.0.2 (or higher)",
            "to work properly.  Note that at time of release, B3HM v1.0.2 has not yet",
            "been released.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='maps, qol',
        quiet_streaming=True,
        ss='https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/qol/easy_entry_to_fort_sunshine/switch.png',
        )

mod.comment('Create the new switch')
new_obj = mod.streaming_hotfix('/Game/Maps/Zone_2/Wetlands/Wetlands_P',
        '/Game/InteractiveObjects/Switches/Lever/Design/IO_Switch_Industrial_Prison',
        location=(34927, 10709, 3139),
        rotation=(0, 67.71637, 0),
        )
mod.newline()

mod.comment('Hook it up to the door')

mod.reg_hotfix(Mod.LEVEL, 'Wetlands_P',
        new_obj,
        'On_SwitchUsed',
        '(Wetlands_M_EP12JakobsRebellion_C_11.BndEvt__IO_Switch_Circuit_Breaker_V_2_K2Node_ActorBoundEvent_0_On_SwitchUsed__DelegateSignature)')

mod.reg_hotfix(Mod.LEVEL, 'Wetlands_P',
        new_obj,
        'SingleActivation',
        'False')

mod.newline()

mod.close()

