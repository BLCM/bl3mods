#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2022 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod

for label, filename_label, rate_initial, rate_combat, desc in [
        ('Regular', 'regular', 26, 13, [
            "The initial two (only used during the initial run) have been shortened",
            "to about 2-4 seconds, and the other ones have been shortened to about",
            "6-10 (depending on how long they've had to decay, etc).",
            ]),
        ('Instant', 'instant', 200, 200, [
            "This variant causes the platforms to basically instantly complete as",
            "soon as the player steps on the.",
            ]),
        ]:

    mod = Mod(f'short_guardian_takedown_crystal_charge_{filename_label}.bl3hotfix',
            f'Short Guardian Takedown Crystal Charge: {label}',
            'Apocalyptech',
            [
                "Drastically shortens the time required to charge the crystal pads during",
                "Takedown at the Guardian Breach, on Minos Prime.",
                "",
                *desc,
                "",
                "This also removes the scaling which ordinarily occurs when multiple players",
                "are running the Takedown, and removes the initial charge delay.  When the",
                "pads aren't being occupied, they will decay at their usual rate.",
            ],
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.0.0',
            cats='cheat, takedowns, maps',
            )

    for label, charge_per_sec, pads in [
            # These go from 47 -> 100, default is 3.  Stock time is ~18sec (at initial values)
            ("Initial Set", rate_initial, [
                'IO_Takedown2_GuardianPad_0',
                'IO_Takedown2_GuardianPad_3',
                ]),
            # These go from 47/50 -> 130, default is 2.75.  Stock time is ~30sec (at initial values)
            ("During-combat sets", rate_combat, [
                # This is the first set, w/ a start value of 47
                'IO_Takedown2_GuardianPad',
                'IO_Takedown2_GuardianPad_1',
                'IO_Takedown2_GuardianPad_2',
                # This is the second set, w/ a start value of 50
                'IO_Takedown2_GuardianPad_6',
                'IO_Takedown2_GuardianPad_7',
                'IO_Takedown2_GuardianPad_8',
                ]),
            ]:

        mod.header(label)

        for pad in pads:
            mod.comment(pad)
            obj_name = f'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Mission.GuardianTakedown_Mission:PersistentLevel.{pad}'

            mod.reg_hotfix(Mod.LEVEL, 'GuardianTakedown_P',
                    obj_name,
                    'ChargeIncreasePerSecond',
                    charge_per_sec)
            mod.reg_hotfix(Mod.LEVEL, 'GuardianTakedown_P',
                    obj_name,
                    'ChargeDelayTime',
                    0)
            mod.reg_hotfix(Mod.LEVEL, 'GuardianTakedown_P',
                    obj_name,
                    'AddMaxChargePerPlayer',
                    0)
            mod.newline()

    mod.close()

