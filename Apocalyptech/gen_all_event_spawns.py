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

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('all_event_spawns.txt',
        'All (Limited-Time) Event Spawns',
        'Apocalyptech',
        [
            "Enables Bloody Harvest, Broken Hearts, and Revenge of the Cartels spawn",
            "modifications at the same time.  Shouldn't require the events to be",
            "actually active in order to work.  Enemies *can* be both Haunted and",
            "Cartel, fwiw!",
            "",
            "This should appear in your modlist *after* any mod which enables an event,",
            "otherwise this statement will get overwritten.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

mod.reg_hotfix(Mod.PATCH, '',
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
