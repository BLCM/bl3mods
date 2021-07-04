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

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('all_event_spawns_active.bl3hotfix',
        'All (Limited-Time) Event Spawns Active',
        'Apocalyptech',
        [
            "Enables Bloody Harvest, Broken Hearts, and Revenge of the Cartels spawn",
            "modifications at the same time.  This does *not* enable the full event;",
            "you'll still have to enable a single event of your choice from the main",
            "menu for that.  Enemies *can* be both Haunted and Cartel, fwiw!",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.1.0',
        cats='event, enemy',
        )

# Prior to the June 24, 2021 patch (which added "endless" seasonal events which you
# can toggle from the main menu), a regular PATCH hotfix worked fine for this.  After
# that patch, though, the engine ends up overwriting this attribute after hotfixes
# have run, and it seems to do so after level loads, as well (or at least after
# LEVEL hotfixes have run).  Fortunately, switching this over to a CHAR-based hotfix
# works just fune, so that's what we're doing now.
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
        '/Game/GameData/Spawning/GlobalSpawnDLCData',
        'DLCs',
        """(
            (
                Data=/Game/PatchDLC/BloodyHarvest/GameData/SpawnDLCScripts/SpawnDLC_BloodyHarvest.SpawnDLC_BloodyHarvest,
                IsEnabled=(BaseValueConstant=1.000000)
            ),
            (
                Data=/Game/PatchDLC/EventVDay/GameData/SpawnDLCScripts/SpawnDLC_VDay.SpawnDLC_VDay,
                IsEnabled=(BaseValueConstant=1.000000)
            ),
            (
                Data=/Game/PatchDLC/Event2/GameData/SpawnDLCSCripts/SpawnDLC_Cartels.SpawnDLC_Cartels,
                IsEnabled=(BaseValueConstant=1.000000)
            )
        )""")

mod.close()
