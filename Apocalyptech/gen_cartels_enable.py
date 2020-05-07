#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('cartels_enable.txt',
        'Enable "Revenge of the Cartels" Event',
        [
            "Enables the Revenge of the Cartels event.  Will interfere with any",
            "other event which happens to be running.  (Only one can be fully",
            "active at a time.)",
        ])

mod.comment('Global activation switches')

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/GameplayGlobals',
        'LeagueInstance',
        1)

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/GameplayGlobals',
        'ActiveLeague',
        'OL_TheCartels')

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Spawning/GlobalSpawnDLCData',
        'DLCs',
        """(
            (
                Data=/Game/PatchDLC/Event2/GameData/SpawnDLCSCripts/SpawnDLC_Cartels.SpawnDLC_Cartels,
                IsEnabled=(BaseValueConstant=1.000000)
            )
        )""")

# The default here is apparently:
#   SpawnOptionData'/Game/PatchDLC/BloodyHarvest/NonPlayerCharacters/LeagueNPC/_Design/Spawning/SpawnOptions_LeagueNPC_Season01.SpawnOptions_LeagueNPC_Season01'
# Should maybe add that into our Bloody Harvest enabling thing
mod.reg_hotfix(Mod.EARLYLEVEL, 'Sanctuary3_P',
        '/Game/Maps/Sanctuary3/Sanctuary3_Season.Sanctuary3_Season:PersistentLevel.OakMissionSpawner_1.SpawnerComponent.SpawnerStyle_SpawnerStyle_Single',
        'SpawnOptions',
        "SpawnOptionData'/Game/PatchDLC/Event2/NonPlayerCharacters/LeagueNPC/_Design/Spawning/SpawnOptions_LeagueNPC_Season02.SpawnOptions_LeagueNPC_Season02'")

mod.newline()

mod.comment('Main Menu')
mod.table_hotfix(Mod.PATCH, '',
        '/Game/Common/_Design/Table_MicropatchSwitches',
        'MainMenuAltBackground',
        'Value',
        BVC(bvc=5))
mod.newline()

# Bugfixes included with the rollout; stuff that was fixed after the data was
# cooked, presumably
mod.comment('Bugfixes')
mod.reg_hotfix(Mod.LEVEL, 'Cartels_P',
        '/Game/PatchDLC/Event2/Maps/Cartels_Mission.Cartels_Mission:PersistentLevel.OakMissionWaypointBox_ACtivateStairSlide.CollisionComp',
        'RelativeScale3D',
        '(X=1.000000,Y=1.000000,Z=1.600000)')
mod.newline()

mod.close()


