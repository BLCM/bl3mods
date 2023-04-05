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

# Timing / Event Parameters
target_time = 15
event_triggers = [1, 5, 8, 10]

mod = Mod('life_of_the_party_short_rakk_shootout.bl3hotfix',
        'Life of the Party: Short Rakk Shootout',
        'Apocalyptech',
        [
            "Shortens the Rakk-shooting contest during Life of the Party from 90",
            f"seconds to {target_time} seconds, for Vault Hunters who are content to let",
            "Grace's record stand but don't feel like waiting around.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='quest-changes',
        videos='https://www.youtube.com/watch?v=OvfddAOP_FA',
        )

obj_base = '/Game/Maps/Zone_3/Desert/Desert_M_BirthdaySurprise.Desert_M_BirthdaySurprise:PersistentLevel.Desert_M_BirthdaySurprise_C_1.Timeline_0'
mod.reg_hotfix(Mod.LEVEL, 'Desert_P',
        obj_base,
        'TheTimeline.Length',
        target_time)
for idx, secs in enumerate(event_triggers):
    mod.reg_hotfix(Mod.LEVEL, 'Desert_P',
            obj_base,
            f'TheTimeline.Events.Events[{idx}].Time',
            secs)
mod.reg_hotfix(Mod.LEVEL, 'Desert_P',
        '/Game/Maps/Zone_3/Desert/Desert_M_BirthdaySurprise.Desert_M_BirthdaySurprise_C:CurveFloat_0',
        'FloatCurve.Keys.Keys[1].Time',
        target_time)
mod.reg_hotfix(Mod.LEVEL, 'Desert_P',
        '/Game/Maps/Zone_3/Desert/Desert_M_BirthdaySurprise.Desert_M_BirthdaySurprise_C:CurveFloat_0',
        'FloatCurve.Keys.Keys[1].Value',
        target_time)

if False:
    # Just some shenanigans!  Can we turn Mordecai into a jerk?  This statement does
    # prevent him from stopping once he hits 20:
    mod.bytecode_hotfix(Mod.LEVEL, 'Desert_P',
            '/Game/Missions/Side/Zone_3/Desert/Mission_BirthdaySurprise',
            'ExecuteUbergraph_Mission_BirthdaySurprise',
            39532,
            20,
            999)

    # ... then these *might* improve his combat ability during that sequence, though
    # I honestly haven't compared it closely to vanilla.  His AI's actually not very
    # good at the contest anyway -- he spends a lot of time repositioning and lining
    # up shots.  I think to *really* get the Jerk Effect I was after, I'd have to
    # start tweaking his AITree object, which is pretty gigantic and a lot more work
    # than I care to do, just for a laff.  Anyway, these hotfixes *do* at least
    # update the attrs they're meant to update, so there's that, at least.
    obj_name = '/Game/NonPlayerCharacters/Mordecai/_Design/Character/BPChar_Mordecai.BPChar_Mordecai_C:OakAIWeaponUser_GEN_VARIABLE'
    mod.reg_hotfix(Mod.CHAR, 'BPChar_Mordecai',
            obj_name,
            'bOverrideBurstCount',
            'True')
    mod.reg_hotfix(Mod.CHAR, 'BPChar_Mordecai',
            obj_name,
            'BurstCountOverride',
            '(Range=(Value=10,Variance=1))')
    mod.reg_hotfix(Mod.CHAR, 'BPChar_Mordecai',
            obj_name,
            'bOverrideBurstDelay',
            'True')
    mod.reg_hotfix(Mod.CHAR, 'BPChar_Mordecai',
            obj_name,
            'BurstDelayOverride',
            '(Range=(Value=0.5,Variance=0.3))')

mod.close()

