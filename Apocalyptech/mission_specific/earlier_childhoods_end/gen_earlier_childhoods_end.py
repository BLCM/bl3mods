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
import collections
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('earlier_childhoods_end.bl3hotfix',
        "Earlier Childhood's End",
        'Apocalyptech',
        [
            "Allows the mission \"Childhood's End\" to be picked up prior to entering",
            "Konrad's hold, and unlocks the full mission-intro dialogue if picked up",
            "from the water purifier in Devil's Razor.  The mission-pickup point in",
            "Konrad's Hold remains valid, and will still skip to the appropriate quest",
            "objective.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='quest-changes',
        videos='https://www.youtube.com/watch?v=OD_PCND7eBw',
        )

# So this one's a bit weird.  The default objective dependency is against Mission_Ep19_MinerDetails,
# with the objective Obj_EnterLab_Objective / 6d2befeb4209fde65635bab71336818a.  Really what I
# *want* to set here is to leave it at that mission, but change it to objective
# Obj_OpenGateToMines_INVS_Objective / d01ef7824fc3d6b519925d8bc372c2f1, which is when Vaughn
# kicks open the door to Konrad's Hold.  However, it seems that this statement only actually
# *works* when you give it a completely different mission.  I've tried five different objectives
# within Mission_Ep19_MinerDetails, and even though the attr updates just fine, it would never
# result in any changes in-game -- the mission would remain hidden until you get to Tannis'
# lab.
#
# I did try various shenanigans to get around that.  Level hotfixes don't help, early or not
# (they don't apply quickly enough to affect the instantiated objects, so the "real" mission
# object in the level is one step behind).  I thought maybe what I had to do was *first* set
# it to a different mission, and *then* re-update it with Mission_Ep19_MinerDetails again, but
# that didn't work either.
#
# In the end, I just resigned myself to doing a dependency on the last objective in
# Mission_Ep17_BigChase.  It opens up the mission a bit earlier than I'd like, but whatever,
# it's fine.  Note that this mission already technically has a dependency on Mission_Ep17_BigChase
# as a whole, so we could, instead, just clear out this `ObjectiveDependency` attr altogether
# to achieve the same goal.  But, I'll leave it in place regardless.
mod.comment('Update mission objective dependency')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Missions/Side/Zone_3/Mine/Mission_GrowingPains.Default__Mission_GrowingPains_C',
        'ObjectiveDependency',
        """
        (
            ObjectiveRef=(
                Mission={},
                ObjectiveName="{}",
                ObjectiveGuid={}
            ),
            ObjectiveStatus=MODS_Complete
        )
        """.format(
            Mod.get_full_cond('/Game/Missions/Plot/Mission_Ep17_BigChase.Mission_Ep17_BigChase_C', 'BlueprintGeneratedClass'),
            'Obj_TalkWithTannis_Objective',
            'f0cb41c24811087dfe37c6ab08556702',
            ),
        )
mod.newline()

# Also, weirdly, *both* pickup points for this mission (the purifier in Devil's Razor and
# the door button in Konrad's Hold) don't start at the beginning of the mission.  The
# Konrad's Hold skip makes some sense, since they clearly don't want to force you to
# backtrack all the way back to Devil's Razor, but the Devil's Razor pickup point one is
# weird.  It means that regardless of where you pick up the mission, you miss the mission
# intro spiel from Vaughn, which leaves the mission bereft of any actual context.
# Bizarre.
#
# Anyway, this clears it up so the Devil's Razor pickup point starts the mission right at
# the beginning.  I expect basically nobody but GBX has ever heard this dialogue!  The
# Konrad's Hold pickup point is left as-is, to avoid that backtracking stuff.
mod.comment('Start mission at the actual beginning')
director_obj = '/Game/Maps/Zone_3/Desert/Desert_Dynamic.Desert_Dynamic:PersistentLevel.IO_MissionGiver_Single_InvisibleBox_4.OakMissionDirector'
mod.reg_hotfix(Mod.LEVEL, 'Desert_P',
        director_obj,
        'MissionEntryPoints',
        '',
        )
mod.reg_hotfix(Mod.LEVEL, 'Desert_P',
        director_obj,
        'Missions',
        '({})'.format(
            Mod.get_full_cond('/Game/Missions/Side/Zone_3/Mine/Mission_GrowingPains.Mission_GrowingPains_C', 'BlueprintGeneratedClass'),
            ),
        )
mod.newline()

mod.close()

