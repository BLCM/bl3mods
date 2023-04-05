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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('transaction_packed_abridged.bl3hotfix',
        'Transaction-Packed: Abridged',
        'Apocalyptech',
        [
            "Skips basically all of the Desolation's Edge side mission 'Transaction-Packed'",
            "and removes all quest dialogue.  The only objective will be to destroy the",
            "final portal!",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='quest-changes',
        videos='https://www.youtube.com/watch?v=NAOGOA1Ufr4',
        )

# Get rid of all dialogue (not that there's much left after the huge skip, but eh)
mod.header('Disable all mission dialogue')
mod.reg_hotfix(Mod.LEVEL, 'Desolate_P',
        '/Game/Dialog/Scripts/Sidequests/DialogScript_SQ_Debug_Destroyer_of_Worlds',
        'TimeSlots',
        '')
mod.newline()

# Objective skip
mod.header('Skip the majority of the mission')
mission_base = '/Game/Missions/Side/Zone_4/Desolate/Mission_DestroyerOfWorlds'
objset = f'{mission_base}.SET_FindCartridge_ObjectiveSet'

mod.reg_hotfix(Mod.LEVEL, 'Desolate_P',
        objset,
        'Objectives',
        '({})'.format(','.join([
            Mod.get_full_cond(f'{mission_base}.{o}', 'MissionObjective') for o in [
                'OBJ_Desetroy_Portal5_Objective',
                ]
            ])),
        )

mod.reg_hotfix(Mod.LEVEL, 'Desolate_P',
        objset,
        'NextSet',
        Mod.get_full_cond(f'{mission_base}.SET_TalkToCreativeDirector4_ObjectiveSet', 'MissionObjectiveSet'),
        )

mod.reg_hotfix(Mod.LEVEL, 'Desolate_P',
        objset,
        'ObjectiveSetGuid',
        'c92f6e4b42e37ad50d8e0fb057e1ad02',
        )

mod.reg_hotfix(Mod.LEVEL, 'Desolate_P',
        objset,
        'ObjOrderPos',
        '(31360)',
        )

mod.newline()

# Without this, the portal is still destroyable but it won't be visible.
mod.header('Make sure the end portal is visible')
mod.reg_hotfix(Mod.LEVEL, 'Desolate_P',
        '/Game/Maps/Zone_4/Desolate/Desolate_M_DestroyerOfWorlds.Desolate_M_DestroyerOfWorlds:PersistentLevel.IO_DOW_Portal__12.Cond_Visibility_NewEnumerator1_MissionEnableConditionObjective',
        'ObjectiveRef',
        """
        (
            Mission={},
            ObjectiveName="{}",
            ObjectiveGuid={}
        )
        """.format(
            Mod.get_full_cond('/Game/Missions/Side/Zone_4/Desolate/Mission_DestroyerOfWorlds.Mission_DestroyerOfWorlds_C', 'BlueprintGeneratedClass'),
            'OBJ_Desetroy_Portal5_Objective',
            '2cd3c49942f4ccb7998a8b895d86c238',
            ),
        )

mod.reg_hotfix(Mod.LEVEL, 'Desolate_P',
        '/Game/Maps/Zone_4/Desolate/Desolate_M_DestroyerOfWorlds.Desolate_M_DestroyerOfWorlds:PersistentLevel.IO_DOW_Portal__12.Cond_Visibility_NewEnumerator1_MissionEnableConditionObjective',
        'ObjectiveStatus',
        'MOS_Active',
        )

mod.newline()

mod.close()
