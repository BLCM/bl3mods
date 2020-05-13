#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('all_event_spawns.txt',
        'All (Limited-Time) Event Spawns',
        [
            "Enables Bloody Harvest, Broken Hearts, and Revenge of the Cartels spawn",
            "modifications at the same time.  Shouldn't require the events to be",
            "actually active in order to work.  Enemies *can* be both Haunted and",
            "Cartel, fwiw!",
            "",
            "This should appear in your modlist *after* any mod which enables an event,",
            "otherwise this statement will get overwritten.",
        ])

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
