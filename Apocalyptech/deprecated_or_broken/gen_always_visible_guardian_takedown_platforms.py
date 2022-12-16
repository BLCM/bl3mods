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
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('always_visible_guardian_takedown_platforms.txt',
        'Always Visible Guardian Takedown Platforms',
        'Apocalyptech',
        [
            "An attempt to make the visibility-cycling platforms in Guardian Takedown",
            "visible *all* the time.  The attrs here *do* get updated but they still go",
            "invisible.  Might just be looking at the wrong thing; I'd expected to find",
            "a ParticleSystem in there but didn't see any.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol, maps, takedowns',
        )

for hf_type in [
        Mod.LEVEL,
        Mod.EARLYLEVEL,
        ]:
    for notify in [
            True,
            False,
            ]:
        for num in [
                2,
                3,
                4,
                5,
                7,
                12,
                13,
                14,
                ]:
            for sub_obj in [
                    'ElevatorMeshComp',
                    'Floor1Mesh',
                    'Floor2Mesh',
                    ]:
                mod.reg_hotfix(hf_type, 'GuardianTakedown_P',
                    f'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.Elevator_GuardianTakedown_Lift_{num}.{sub_obj}',
                    'BodyInstance.PhysMaterialOverride',
                    'None',
                    notify=notify,
                    )
            for sub_obj in [
                    'Floor1Mesh',
                    'Floor2Mesh',
                    ]:
                mod.reg_hotfix(hf_type, 'GuardianTakedown_P',
                    f'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.Elevator_GuardianTakedown_Lift_{num}.{sub_obj}',
                    'OverrideMaterials',
                    '',
                    notify=notify,
                    )

        mod.reg_hotfix(hf_type, 'GuardianTakedown_P',
                '/Game/PatchDLC/Takedown2/Maps/MapSpecificAssets/EridianBlock/MI_Eridian_Block',
                'PhysMaterial',
                'None',
                notify=notify,
                )

mod.close()
