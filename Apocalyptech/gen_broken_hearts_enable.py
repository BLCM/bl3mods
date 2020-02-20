#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod


mod = Mod('broken_hearts_enable.txt',
        'Enable "Broken Hearts" Event',
        [
            "Theoretically enables the Broken Hearts event even after it's been closed down.",
            "This is currently untested, given that it was written when the event was still",
            "ongoing.",
            "",
            "This will presumably interfere with any other event which happens to be running",
            "at the time.",
        ],
        'BrokenHeartsEnable',
        )

mod.comment('Global activation switches')

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/GameplayGlobals',
        'LeagueInstance',
        1)

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/GameplayGlobals',
        'ActiveLeague',
        'OL_ValentinesDay')

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Spawning/GlobalSpawnDLCData',
        'DLCs',
        """(
            (
                Data=/Game/PatchDLC/EventVDay/GameData/SpawnDLCScripts/SpawnDLC_VDay.SpawnDLC_VDay,
                IsEnabled=(BaseValueConstant=1.000000)
            )
        )""")

# The default here is apparently:
#   SpawnOptionData'/Game/PatchDLC/BloodyHarvest/NonPlayerCharacters/LeagueNPC/_Design/Spawning/SpawnOptions_LeagueNPC_Season01.SpawnOptions_LeagueNPC_Season01'
# Should maybe add that into our Bloody Harvest enabling thing
mod.reg_hotfix(Mod.EARLYLEVEL, 'Sanctuary3_P',
        '/Game/Maps/Sanctuary3/Sanctuary3_Season.Sanctuary3_Season:PersistentLevel.OakMissionSpawner_1.SpawnerComponent.SpawnerStyle_SpawnerStyle_Single',
        'SpawnOptions',
        "SpawnOptionData'/Game/PatchDLC/EventVDay/NonPlayerCharacters/LeagueNPC/_Design/Spawning/SpawnOptions_LeagueNPC_VDay.SpawnOptions_LeagueNPC_VDay'")

mod.newline()

# Balance changes - default here is 8500, apparently
mod.comment('Balance Changes')
for char_name in [
        'BPChar_PunkBasic',
        'BPChar_RakkBasic',
        'BPChar_GuardianWraith',
        'BPChar_ApeBasic',
        'BPChar_LoaderBasic',
        'BPChar_NogBasic',
        'BPChar_Ratch',
        ]:
    mod.table_hotfix(Mod.CHAR, char_name,
            '/Game/PatchDLC/EventVDay/Enemies/Hearts/_Shared/Balance/Table_VDay_LootRarityBalance',
            'LootHeart',
            'LegendaryWeightModifier_18_B98DE11946C28DF64D94E197F7FED9BE',
            6500)
mod.newline()

# Reward scaling
mod.comment('Force Terminal Polyaimorous and Wedding Invitation to Level 53')
for row in [
        'PolyAim',
        'WeddingInvitation',
        ]:
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/EventVDay/Gear/Weapon/DataTable_WeaponBalance_EventVDay',
            row,
            'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
            53)
mod.newline()

mod.close()


