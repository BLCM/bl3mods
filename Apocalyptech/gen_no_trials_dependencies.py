#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
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

import collections
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('no_trials_dependencies.txt',
        'No Trials Dependencies',
        [
            "Allows you to pick up (and enter) Proving Grounds Trials as soon as",
            "you get to the levels which unlock them.  The missions (both the",
            "'Discovery' mission and the Trials mission itself) will claim to be",
            "a minimum level of 29 when they're picked up, but the enemies in those",
            "zones can scale all the way to level 1, so the actual combat should",
            "always match your level.",
            "",
            "NOTE: In order for this to *actually* take effect, you will have to",
            "enter the game once, and then quit back to the main menu.  No idea",
            "why this doesn't apply cleanly until then, but them's the breaks.",
        ])

mission_dep = Mod.get_full_cond('/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Mission_Ep01_ChildrenOfTheVault_C', 'Mission')

# Trying to set this to an empty list seems to result in a single-element list with
# `None` as the element, which isn't exactly what I'd want.  That would probably work
# fine anyway, honestly, but we'll just set it to the first plot mission, which'll
# be good enough.
#
# TODO: Would love to figure out how to NOT have to do the main menu dance with this.
# I've tried both LEVEL and EARLYLEVEL (and even tried doing *both*), but you've still
# got to exit out to the main menu in order for it to apply.  Unsurprisingly, PATCH
# doesn't do the trick.  You *can* also just do a hotfix on the pseudo-object of
# `Default__{name_base}_C`, rather than having the full path, but that doesn't affect
# that main-menu behavior at all, so I'm just leaving it like it is.
for num in [1, 4, 5, 6, 7, 8]:
    for name_base in [
            f'Mission_ProvingGroundsDiscovery_Mission{num:02d}',
            f'Mission_ProvingGrounds_Mission{num:02d}',
            ]:
        obj_name = f'/Game/Missions/Side/ProvingGrounds/ProvingGrounds{num}/{name_base}.Default__{name_base}_C'
        mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                obj_name,
                'MissionDependencies',
                f'({mission_dep})')

mod.close()
