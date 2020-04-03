#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('always_visible_challenge_icons.txt',
        'Sets all the challenge icons to be visible on the map at all times',
        [
            "Note that this mod will cause to to miss dialogue -- when entering",
            "a new map for the first time, you'll basically just get one random",
            "voiceover from the pool of challenges that just got 'found'.",
            "",
            "Eridian Writings are included in here, though those aren't really",
            "challenges per se.",
            "",
            "NOTE: This is currently not well-tested.  Only a handful of early",
            "maps have been validated.",
        ],
        'ChallengeIcons',
        )

# I should look at actual data, but it looks to me from some *real* simple
# scaling on the map screen that The Droughts is probably 65k "wide".
# Double that and round up to the next "nicest" number will get you 200k,
# so I'm thinking that's what we should go for.
radius = 200000

# This value wouldn't be awful to simply have a pretty wide radius which
# would reveal things as you go sort of generally in their direction.  In
# the end I don't think I like it as much, even though having everything
# out means missing dialogue
#radius = 30000

# As for height, I still don't really know what this controls exactly,
# though obviously it's related to how close you have to be in the y axis.
# Gonna set it to half the radius, I guess?
height = 100000

# The radius around the newly-discovered icon which will show up as "visited"
# on the map.  A lot of these icons have this set to 0 which prevents
# functionality for this mod, so we'll set 'em all.
unfog_radius = 2000

# For the last part of the extended object name:
#
# BP_CrewChallengeComponent_Collection - Typhon Logs
# BP_CrewChallengeComponent_CollectionDeadDrop - Typhon Dead Drop
# BP_CrewChallengeComponent_Hijack_Spawner - Ellie Vehicle Theft
# BP_CrewChallengeComponent_Hunt_Spawner - Hammerlock Hunt
# BP_CrewChallengeComponent_Sabotage - Radios
# BP_CrewChallengeComponent_Salvage - Claptraps

# getall BP_CrewChallengeComponent_Salvage_C DetectionRadius

for (label, level_name, object_names) in sorted([
        ("Atlas HQ", 'AtlasHQ_P', [
            '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_Office.AtlasHQ_Office:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_Office.AtlasHQ_Office:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_Courtyard_Dynamic.AtlasHQ_Courtyard_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_6.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_Courtyard_Dynamic.AtlasHQ_Courtyard_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_10.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_Courtyard_Dynamic.AtlasHQ_Courtyard_Dynamic:PersistentLevel.BP_IO_BroadcastControlBox_2.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_FoyerLobby.AtlasHQ_FoyerLobby:PersistentLevel.BP_IO_Salvage_ClapTrapPart_Firewall.BP_CrewChallengeComponent_Salvage',
            ]),
        ("Tazendeer Ruins", 'Beach_P', [
            '/Game/Maps/Zone_4/Beach/Beach_Encounters.Beach_Encounters:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_4/Beach/Beach_Encounters.Beach_Encounters:PersistentLevel.BP_IO_KillTargetCrewChallenge_2.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_4/Beach/Beach_Encounters.Beach_Encounters:PersistentLevel.BP_IO_Collection_EchoJournal_822.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_4/Beach/Beach_Encounters.Beach_Encounters:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_4/Beach/Beach_Encounters.Beach_Encounters:PersistentLevel.BP_IO_Collection_EchoJournal_0.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_4/Beach/Beach_Encounters.Beach_Encounters:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_4/Beach/Beach_Encounters.Beach_Encounters:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_HeatVents.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_4/Beach/Beach_Encounters.Beach_Encounters:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_RotatorCuffModule_0.BP_CrewChallengeComponent_Salvage',
            ]),
        ("Forgotten Basilica", 'CityBoss_P', [
            ]),
        ("Meridian Metroplex", 'City_P', [
            '/Game/Maps/Zone_1/City/City_Combat.City_Combat:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_1/City/City_Mission.City_Mission:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_StairClimbingUpdate.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_1/City/City_Mission.City_Mission:PersistentLevel.BP_IO_KillTargetCrewChallenge_2.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_1/City/City_Mission.City_Mission:PersistentLevel.BP_IO_HijackCrewChallenge_2.BP_CrewChallengeComponent_Hijack_Spawner',
            '/Game/Maps/Zone_1/City/City_Mission.City_Mission:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage_0.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_1/City/City_Combat.City_Combat:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/City/City_Combat.City_Combat:PersistentLevel.BP_IO_Collection_EchoJournal3-AtlasTower.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/City/City_Combat.City_Combat:PersistentLevel.BP_IO_Collection_EchoJournal2-RandomParkthing.BP_CrewChallengeComponent_Collection',
            ]),
        ("Neon Arterial", 'CityVault_P', [
            '/Game/Maps/Zone_1/CityVault/CityVault_P.CityVault_P:PersistentLevel.BP_IO_Collection_EchoJournal_6.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/CityVault/CityVault_P.CityVault_P:PersistentLevel.BP_IO_Collection_EchoJournal_3.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/CityVault/CityVault_P.CityVault_P:PersistentLevel.BP_IO_Collection_EchoJournal_1.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/CityVault/CityVault_P.CityVault_P:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_1/CityVault/CityVault_P.CityVault_P:PersistentLevel.BP_IO_Salvage_ClapTrapPart_AntennaAccessory_0.BP_CrewChallengeComponent_Salvage',
            ]),
        ("Sandblast Scar", 'Convoy_P', [
            ]),
        ("Pyre of Stars", 'Crypt_P', [
            '/Game/Maps/Zone_4/Crypt/Crypt_Dynamic.Crypt_Dynamic:PersistentLevel.BP_IO_HuntCrewChallenge_2.BP_CrewChallengeComponent_Hunt_Spawner',
            '/Game/Maps/Zone_4/Crypt/Crypt_Dynamic.Crypt_Dynamic:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_4/Crypt/Crypt_Dynamic.Crypt_Dynamic:PersistentLevel.BP_IO_Salvage_ClapTrapPart_HumorSarcasmModule_1.BP_CrewChallengeComponent_Salvage',
            ]),
        ("Great Vault", 'DesertBoss_P', [
            ]),
        ("Devil's Razor", 'Desert_P', [
            '/Game/Maps/Zone_3/Desert/Desert_Combat.Desert_Combat:PersistentLevel.BP_IO_HuntCrewChallenge_2.BP_CrewChallengeComponent_Hunt_Spawner',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.EridianWritingSpawner__4.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.BP_IO_Salvage_ClapTrapPart_AllTerrainMotor.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.BP_IO_KillTargetCrewChallenge_2.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.BP_IO_HijackCrewChallenge_6.BP_CrewChallengeComponent_Hijack_Spawner',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.BP_IO_HijackCrewChallenge_2.BP_CrewChallengeComponent_Hijack_Spawner',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.BP_IO_Collection_EchoJournal_236.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.BP_IO_Collection_EchoJournal_1809.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.BP_IO_Collection_EchoJournal_1807.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_3/Desert/Desert_M_CrewMissions.Desert_M_CrewMissions:PersistentLevel.BP_IO_BroadcastControlBox2_Sabotage.BP_CrewChallengeComponent_Sabotage',
            ]),
        ("Cathedral of the Twin Gods", 'Desertvault_P', [
            '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.BP_IO_KillTargetCrewChallenge_2.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_4.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_3.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.BP_IO_Salvage_ClapTrapPart_AntennaAccessory.BP_CrewChallengeComponent_Salvage',
            ]),
        ("Desolation's Edge", 'Desolate_P', [
            '/Game/Maps/Zone_4/Desolate/Desolate_Encounters.Desolate_Encounters:PersistentLevel.BP_IO_HuntCrewChallenge_2.BP_CrewChallengeComponent_Hunt_Spawner',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.EridianWritingSpawner__4.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_VoiceVolume.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_FigurativeSpeechAdapter.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_IO_HijackCrewChallenge__0.BP_CrewChallengeComponent_Hijack_Spawner',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_IO_HijackCrewChallenge_.BP_CrewChallengeComponent_Hijack_Spawner',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_IO_Collection_EchoJournal_6.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_IO_Collection_EchoJournal_10.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_IO_BroadcastControlBox_6.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_IO_BroadcastControlBox_2.BP_CrewChallengeComponent_Sabotage',
            ]),
        ("Destroyer's Rift", 'FinalBoss_P', [
            '/Game/Maps/Zone_0/FinalBoss/FinalBoss_P.FinalBoss_P:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            ]),
        ("Jakobs Estate", 'Mansion_P', [
            '/Game/Maps/Zone_2/Mansion/Mansion_Dynamic.Mansion_Dynamic:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_DoorOpeningModule.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_2/Mansion/Mansion_Dynamic.Mansion_Dynamic:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_MultiTaskingRAM.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_2/Mansion/Mansion_Dynamic.Mansion_Dynamic:PersistentLevel.BP_IO_KillTargetCrewChallenge_2.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_2/Mansion/Mansion_Dynamic.Mansion_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_7086.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Mansion/Mansion_Dynamic.Mansion_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_297.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Mansion/Mansion_Dynamic.Mansion_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Mansion/Mansion_Dynamic.Mansion_Dynamic:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_2/Mansion/Mansion_Mission.Mansion_Mission:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            ]),
        ("Ambermire", 'MarshFields_P', [
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.EridianWritingSpawner__36.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_LongTermMemory.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_HardDiskSlot.BP_CrewChallengeComponent_Salvage',
            # hm, there's supposed to be only the Billies in here, yeah?  Not sure what the second killtarget is doing.
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.BP_IO_KillTargetCrewChallenge_3.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.BP_IO_KillTargetCrewChallenge_2.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.BP_IO_Collection_EchoJournal_4.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.BP_IO_Collection_EchoJournal_3.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.BP_IO_BroadcastControlBox2_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_2/MarshFields/MarshFields_Combat.MarshFields_Combat:PersistentLevel.BP_IO_BroadcastControlBox1_Sabotage.BP_CrewChallengeComponent_Sabotage',
            ]),
        ("Konrad's Hold", 'Mine_P', [
            '/Game/Maps/Zone_3/Mine/Mine_Mission.Mine_Mission:PersistentLevel.BP_IO_HuntCrewChallenge_2.BP_CrewChallengeComponent_Hunt_Spawner',
            '/Game/Maps/Zone_3/Mine/Mine_Combat.Mine_Combat:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_3/Mine/Mine_Mission.Mine_Mission:PersistentLevel.BP_IO_Collection_EchoJournal_470.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/Mine/Mine_Mission.Mine_Mission:PersistentLevel.BP_IO_Collection_EchoJournal3.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/Mine/Mine_Mission.Mine_Mission:PersistentLevel.BP_IO_Collection_EchoJournal.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/Mine/Mine_Mission.Mine_Mission:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_3/Mine/Mine_Mission.Mine_Mission:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_HandClamps.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_3/Mine/Mine_Mission.Mine_Mission:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_Arms.BP_CrewChallengeComponent_Salvage',
            ]),
        ("Athenas", 'Monastery_P', [
            '/Game/Maps/Zone_1/Monastery/Monastery_Challenges.Monastery_Challenges:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_PoetryModule.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_1/Monastery/Monastery_Challenges.Monastery_Challenges:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_SingingModule.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_1/Monastery/Monastery_Challenges.Monastery_Challenges:PersistentLevel.BP_IO_HuntCrewChallenge_2.BP_CrewChallengeComponent_Hunt_Spawner',
            '/Game/Maps/Zone_1/Monastery/Monastery_Challenges.Monastery_Challenges:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_1/Monastery/Monastery_Challenges.Monastery_Challenges:PersistentLevel.BP_IO_Collection_EchoJournal_4.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/Monastery/Monastery_Challenges.Monastery_Challenges:PersistentLevel.BP_IO_Collection_EchoJournal_3.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/Monastery/Monastery_Challenges.Monastery_Challenges:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/Monastery/Monastery_Challenges.Monastery_Challenges:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            ]),
        ("Carnivora", 'MotorcadeFestival_P', [
            '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Encounters.MotorcadeFestival_Encounters:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Encounters.MotorcadeFestival_Encounters:PersistentLevel.BP_IO_Salvage_ClapTrapPart_LEDs.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Encounters.MotorcadeFestival_Encounters:PersistentLevel.BP_IO_Collection_EchoJournal_6.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Encounters.MotorcadeFestival_Encounters:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Encounters.MotorcadeFestival_Encounters:PersistentLevel.BP_IO_Collection_EchoJournal_10.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Encounters.MotorcadeFestival_Encounters:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            ]),
        ("Guts of Carnivora", 'MotorcadeInterior_P', [
            '/Game/Maps/Zone_3/MotorcadeInterior/MotorcadeInterior_Encounter.MotorcadeInterior_Encounter:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_3/MotorcadeInterior/MotorcadeInterior_Encounter.MotorcadeInterior_Encounter:PersistentLevel.BP_IO_Salvage_ClapTrapPart_SpeechProcessor.BP_CrewChallengeComponent_Salvage',
            ]),
        ("Splinterlands", 'Motorcade_P', [
            '/Game/Maps/Zone_3/Motorcade/Motorcade_CrewChallenges.Motorcade_CrewChallenges:PersistentLevel.BP_IO_HuntCrewChallenge_2.BP_CrewChallengeComponent_Hunt_Spawner',
            '/Game/Maps/Zone_3/Motorcade/Motorcade_CrewChallenges.Motorcade_CrewChallenges:PersistentLevel.BP_IO_KillTargetCrewChallenge_2.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_3/Motorcade/Motorcade_CrewChallenges.Motorcade_CrewChallenges:PersistentLevel.BP_IO_HijackCrewChallenge_0.BP_CrewChallengeComponent_Hijack_Spawner',
            '/Game/Maps/Zone_3/Motorcade/Motorcade_CrewChallenges.Motorcade_CrewChallenges:PersistentLevel.BP_IO_Collection_EchoJournal_762.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/Motorcade/Motorcade_CrewChallenges.Motorcade_CrewChallenges:PersistentLevel.BP_IO_Collection_EchoJournal_206.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/Motorcade/Motorcade_CrewChallenges.Motorcade_CrewChallenges:PersistentLevel.BP_IO_Collection_EchoJournal_2014.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_3/Motorcade/Motorcade_CrewChallenges.Motorcade_CrewChallenges:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_3/Motorcade/Motorcade_CrewChallenges.Motorcade_CrewChallenges:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_3/Motorcade/Motorcade_CrewChallenges.Motorcade_CrewChallenges:PersistentLevel.BP_IO_Salvage_ClapTrapPart_Wheel.BP_CrewChallengeComponent_Salvage',
            ]),
        ("Skywell-27", 'OrbitalPlatform_P', [
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_Cinema.OrbitalPlatform_Cinema:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_DubstepLibrary.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_Cinema.OrbitalPlatform_Cinema:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_Antenna_0.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_Cinema.OrbitalPlatform_Cinema:PersistentLevel.BP_IO_KillTargetCrewChallenge_2.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_Cinema.OrbitalPlatform_Cinema:PersistentLevel.BP_IO_Collection_EchoJournal_752.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_Cinema.OrbitalPlatform_Cinema:PersistentLevel.BP_IO_Collection_EchoJournal_37.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_Cinema.OrbitalPlatform_Cinema:PersistentLevel.BP_IO_Collection_EchoJournal_36.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_Mission.OrbitalPlatform_Mission:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            ]),
        ("Meridian Outskirts", 'Outskirts_P', [
            '/Game/Maps/Zone_1/Outskirts/Outskirts_Dynamic.Outskirts_Dynamic:PersistentLevel.BP_IO_HijackCrewChallenge_2.BP_CrewChallengeComponent_Hijack_Spawner',
            # One of these journals doesn't like showing up, it seems
            '/Game/Maps/Zone_1/Outskirts/Outskirts_Dynamic.Outskirts_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_6.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/Outskirts/Outskirts_Dynamic.Outskirts_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/Outskirts/Outskirts_Dynamic.Outskirts_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal3-OutskirtsofCity.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/Outskirts/Outskirts_Dynamic.Outskirts_Dynamic:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_1/Outskirts/Outskirts_Mission.Outskirts_Mission:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_UniversalTranslator.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_1/Outskirts/Outskirts_Combat.Outskirts_Combat:PersistentLevel.EridianWritingSpawner.BP_ChallengeComponent_IconEridian',
            ]),
        ("Anvil", 'Prison_P', [
            '/Game/Maps/Zone_2/Prison/Prison_Mission.Prison_Mission:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_2/Prison/Prison_Mission.Prison_Mission:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_PaintJob.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_2/Prison/Prison_Mission.Prison_Mission:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_Hair.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_2/Prison/Prison_Mission.Prison_Mission:PersistentLevel.BP_IO_KillTargetCrewChallenge_0.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_2/Prison/Prison_Mission.Prison_Mission:PersistentLevel.BP_IO_Collection_EchoJournal_422.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Prison/Prison_Mission.Prison_Mission:PersistentLevel.BP_IO_Collection_EchoJournal_1.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Prison/Prison_Mission.Prison_Mission:PersistentLevel.BP_IO_Collection_EchoJournal.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Prison/Prison_Mission.Prison_Mission:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_2/Prison/Prison_Mission.Prison_Mission:PersistentLevel.BP_IO_BroadcastControlBox2_Sabotage.BP_CrewChallengeComponent_Sabotage',
            ]),
        ("Droughts", 'Prologue_P', [
            '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_5.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_6.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_IO_HuntCrewChallenge_2.BP_CrewChallengeComponent_Hunt_Spawner',
            '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_GyroscopicRotor.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.EridianWritingSpawner__4.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_0/Prologue/Prologue_Terrain.Prologue_Terrain:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_Motor.BP_CrewChallengeComponent_Salvage',
            ]),
        ("Covenant Pass", 'Recruitment_P', [
            ]),
        ("Ascension Bluff", 'Sacrifice_P', [
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_HuntCrewChallenge-Skrakk.BP_CrewChallengeComponent_Hunt_Spawner',
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_HijackCrewChallenge_2.BP_CrewChallengeComponent_Hijack_Spawner',
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_4.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_3.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_Salvage_ClapTrapPart_GasTank.BP_CrewChallengeComponent_Salvage',
            ]),
        ("Sanctuary", 'Sanctuary3_P', [
            '/Game/Maps/Sanctuary3/Sanctuary3_P.Sanctuary3_P:PersistentLevel.IO_WantedPosterRareSpawns_C_1.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Sanctuary3/Sanctuary3_P.Sanctuary3_P:PersistentLevel.IO_WantedPosterRareSpawns_C_0.BP_CrewChallengeComponent_KillTarget_Spawner',
            ]),
        ("Lectra City", 'Towers_P', [
            '/Game/Maps/Zone_1/Towers/Towers_Mission.Towers_Mission:PersistentLevel.BP_IO_Salvage_ClapTrapPart_Eye.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_1/Towers/Towers_Mission.Towers_Mission:PersistentLevel.BP_IO_Salvage_ClapTrapPart_2.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_1/Towers/Towers_Mission.Towers_Mission:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_1/Towers/Towers_Combat.Towers_Combat:PersistentLevel.BP_IO_KillTargetCrewChallenge_2.BP_CrewChallengeComponent_KillTarget_Spawner',
            '/Game/Maps/Zone_1/Towers/Towers_Combat.Towers_Combat:PersistentLevel.BP_IO_Collection_EchoJournal_2.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/Towers/Towers_Combat.Towers_Combat:PersistentLevel.BP_IO_Collection_EchoJournal_1.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/Towers/Towers_Combat.Towers_Combat:PersistentLevel.BP_IO_Collection_EchoJournal_0.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_1/Towers/Towers_Combat.Towers_Combat:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            ]),
        ("Voracious Canopy", 'Watership_P', [
            '/Game/Maps/Zone_2/Watership/Watership_Sidemission.Watership_Sidemission:PersistentLevel.BP_IO_HuntCrewChallenge_2.BP_CrewChallengeComponent_Hunt_Spawner',
            '/Game/Maps/Zone_2/Watership/Watership_Sidemission.Watership_Sidemission:PersistentLevel.BP_IO_Salvage_ClapTrapPart_DanceProtocol.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_2/Watership/Watership_Sidemission.Watership_Sidemission:PersistentLevel.BP_IO_Collection_EchoJournal_3258.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Watership/Watership_Sidemission.Watership_Sidemission:PersistentLevel.BP_IO_Collection_EchoJournal_1232.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Watership/Watership_Sidemission.Watership_Sidemission:PersistentLevel.BP_IO_Collection_EchoJournal_0.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Watership/Watership_P.Watership_P:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            ]),
        ("Floating Tomb", 'WetlandsBoss_P', [
            ]),
        ("Floodmoor Basin", 'Wetlands_P', [
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Combat.Wetlands_Combat:PersistentLevel.BP_IO_HijackCrewChallenge_2.BP_CrewChallengeComponent_Hijack_Spawner',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Challenges.Wetlands_Challenges:PersistentLevel.BP_IO_HijackCrewChallenge_5.BP_CrewChallengeComponent_Hijack_Spawner',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Challenges.Wetlands_Challenges:PersistentLevel.BP_IO_Collection_EchoJournal_502.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Challenges.Wetlands_Challenges:PersistentLevel.BP_IO_Collection_EchoJournal_0.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Challenges.Wetlands_Challenges:PersistentLevel.BP_IO_Collection_EchoJournal.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Challenges.Wetlands_Challenges:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Challenges.Wetlands_Challenges:PersistentLevel.BP_IO_BroadcastControlBox2_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Challenges.Wetlands_Challenges:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_LoveModule.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Challenges.Wetlands_Challenges:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_ReinforcedRearPaneling.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Challenges.Wetlands_Challenges:PersistentLevel.BP_IO_HuntCrewChallenge_2.BP_CrewChallengeComponent_Hunt_Spawner',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Combat.Wetlands_Combat:PersistentLevel.EridianWritingSpawner__39.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Combat.Wetlands_Combat:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            # Found by my script but I don't think they're actually what we want
            #'/Game/Maps/Zone_2/Wetlands/Wetlands_Challenges.Wetlands_Challenges:PersistentLevel.OakVehicleSpawner_HijackChallenge2_Wheel.BP_CrewChallengeComponent_Hijack_Spawner',
            #'/Game/Maps/Zone_2/Wetlands/Wetlands_Combat.Wetlands_Combat:PersistentLevel.OakVehicleSpawner_HijackChallenge_Outrunner.BP_CrewChallengeComponent_Hijack_Spawner',
            #'/Game/Maps/Zone_2/Wetlands/Wetlands_Combat.Wetlands_Combat:PersistentLevel.OakMissionSpawner_Vehicle_1.BP_CrewChallengeComponent_Hijack_Spawner',
            ]),
        ("Blackbarrel Cellars", 'WetlandsVault_P', [
            '/Game/Maps/Zone_2/WetlandsVault/WetlandsVault_Combat.WetlandsVault_Combat:PersistentLevel.BP_IO_Collection_EchoJournal_182.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/WetlandsVault/WetlandsVault_Combat.WetlandsVault_Combat:PersistentLevel.BP_IO_Collection_EchoJournal_161.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/WetlandsVault/WetlandsVault_Combat.WetlandsVault_Combat:PersistentLevel.BP_IO_Collection_EchoJournal_120.BP_CrewChallengeComponent_Collection',
            '/Game/Maps/Zone_2/WetlandsVault/WetlandsVault_P.WetlandsVault_P:PersistentLevel.EridianWritingSpawner_.BP_ChallengeComponent_IconEridian',
            '/Game/Maps/Zone_2/WetlandsVault/WetlandsVault_P.WetlandsVault_P:PersistentLevel.BP_IO_Salvage_ClapTrapPart_AntennaAccessory.BP_CrewChallengeComponent_Salvage',
            ]),

        ###
        ### DLC1
        ###

        # These mostly don't work yet, and have several downsides:
        #
        #   1) They activate the Torgue dialogues, but it turns out that those are always visible on the map anyway
        #   2) They actively *prevent* the other sorts from ever showing up.  You can still *do* the challenges if
        #      you go there, but the dialogue never starts and you never get credit for it.
        #   3) They seem to prevent the loader spawns right outside Timothy's hideout.  (Perhaps that's all the
        #      `Strip_Central_TimLair_CrewIOStatus` stuff, actually?)
        #
        # So anyway, just commenting for now.  Will try to piece that together later.

        #("Grand Opening", 'CasinoIntro_P', [
        #    ]),
        #("Jack's Secret", 'Core_P', [
        #    '/Dandelion/Maps/Core/Core_Gameplay.Core_Gameplay:PersistentLevel.IO_CrewChallenge_Sabotage_DLC_7.BP_CrewChallengeComp_Sabotage_DLC1',
        #    '/Dandelion/Maps/Core/Core_Gameplay.Core_Gameplay:PersistentLevel.IO_CrewChallenge_Collect_DLC_5.BP_CrewChallengeComponent_Collection',
        #    ]),
        #("Impound Deluxe", 'Impound_P', [
        #    '/Dandelion/Maps/Impound/Impound_Gameplay.Impound_Gameplay:PersistentLevel.IO_CrewChallenge_Kill_DLC_2.BP_CrewChallengeComp_KillTarget_DLC1',
        #    '/Dandelion/Maps/Impound/Impound_Gameplay.Impound_Gameplay:PersistentLevel.IO_CrewChallenge_Sabotage_DLC_2.BP_CrewChallengeComp_Sabotage_DLC1',
        #    ]),
        #("Spendopticon", 'Strip_P', [
        #    '/Dandelion/Maps/Strip/Strip_Interactives.Strip_Interactives:PersistentLevel.IO_CrewChallenge_Collect_DLC_4.BP_CrewChallengeComponent_Collection',
        #    '/Dandelion/Maps/Strip/Strip_PM_MeetCrad.Strip_PM_MeetCrad:PersistentLevel.IO_CrewChallenge_Sabotage_DLC_2.BP_CrewChallengeComp_Sabotage_DLC1',
        #    '/Dandelion/Maps/Strip/Strip_Central_TimLair_CrewIOStatus.Strip_Central_TimLair_CrewIOStatus:PersistentLevel.IO_CrewChallenge_Sabotage_DLC1_Strip__0.BP_CrewChallengeComp_Sabotage_DLC1',
        #    '/Dandelion/Maps/Strip/Strip_Central_TimLair_CrewIOStatus.Strip_Central_TimLair_CrewIOStatus:PersistentLevel.IO_CrewChallenge_Sabotage_DLC1_Strip_.BP_CrewChallengeComp_Sabotage_DLC1',
        #    '/Dandelion/Maps/Strip/Strip_Central_TimLair_CrewIOStatus.Strip_Central_TimLair_CrewIOStatus:PersistentLevel.IO_CrewChallenge_Kill_DLC1__0.BP_CrewChallengeComp_KillTarget_DLC1',
        #    '/Dandelion/Maps/Strip/Strip_Central_TimLair_CrewIOStatus.Strip_Central_TimLair_CrewIOStatus:PersistentLevel.IO_CrewChallenge_Kill_DLC1_.BP_CrewChallengeComp_KillTarget_DLC1',
        #    '/Dandelion/Maps/Strip/Strip_Central_TimLair_CrewIOStatus.Strip_Central_TimLair_CrewIOStatus:PersistentLevel.IO_CrewChallenge_Collect_DLC_2.BP_CrewChallengeComponent_Collection',
        #    ]),
        #("VIP Tower", 'TowerLair_P', [
        #    '/Dandelion/Maps/TowerLair/TowerLair_Interactives.TowerLair_Interactives:PersistentLevel.IO_CrewChallenge_Kill_DLC_2.BP_CrewChallengeComp_KillTarget_DLC1',
        #    '/Dandelion/Maps/TowerLair/TowerLair_Interactives.TowerLair_Interactives:PersistentLevel.IO_CrewChallenge_Sabotage_DLC_2.BP_CrewChallengeComp_Sabotage_DLC1',
        #    '/Dandelion/Maps/TowerLair/TowerLair_Interactives.TowerLair_Interactives:PersistentLevel.IO_CrewChallenge_Collect_DLC_2.BP_CrewChallengeComponent_Collection',
        #    ]),
        #("Compactor", 'Trashtown_P', [
        #    '/Dandelion/Maps/Trashtown/Trashtown_Gameplay.Trashtown_Gameplay:PersistentLevel.IO_CrewChallenge_Kill_DLC_5.BP_CrewChallengeComp_KillTarget_DLC1',
        #    '/Dandelion/Maps/Trashtown/Trashtown_Gameplay.Trashtown_Gameplay:PersistentLevel.IO_CrewChallenge_Collect_DLC_2.BP_CrewChallengeComponent_Collection',
        #    ]),

        ###
        ### DLC2
        ###

        # So the Occult Hunts seem to work fine, but Gaige's Gifts don't, and having these in here
        # prevents her dialog from playing, so I'm taking those out for now.  (Or rather: the gifts
        # themselves work just fine, minus the missing dialog, but these statements don't make them
        # show up ahead of time.)  Jury's still out on the statues; those don't activate until after
        # Wainwright's taken over, and the one I'd checked out previously in Cursehaven showed up
        # when I went back there, but the one in Dustbound Archive didn't.  So: hrm.

        ("Dustbound Archives", 'Archive_P', [
            '/Hibiscus/Maps/Archive/Archive_CrewChallenges.Archive_CrewChallenges:PersistentLevel.IO_DLC2_Crew_Mancubus_Brain_2.BP_CrewChallengeComp_Mancubus_DLC2',
            #'/Hibiscus/Maps/Archive/Archive_CrewChallenges.Archive_CrewChallenges:PersistentLevel.IO_DLC2_Crew_Gifts_2.BP_CrewChallengeComp_Gifts_DLC2',
            ]),
        ("Lodge", 'Bar_P', [
            ]),
        ("Negul Neshai", 'Camp_P', [
            '/Hibiscus/Maps/Camp/Camp_Combat.Camp_Combat:PersistentLevel.IO_DLC2_Crew_Hunt_2.BP_CrewChallengeComp_Hunt_DLC2',
            '/Hibiscus/Maps/Camp/Camp_Bunkers.Camp_Bunkers:PersistentLevel.IO_DLC2_Crew_Mancubus_Brain_2.BP_CrewChallengeComp_Mancubus_DLC2',
            #'/Hibiscus/Maps/Camp/Camp_DigSite.Camp_DigSite:PersistentLevel.IO_DLC2_Crew_Gifts_2.BP_CrewChallengeComp_Gifts_DLC2',
            ]),
        ("Skittermaw Basin", 'Lake_P', [
            #'/Hibiscus/Maps/Lake/Lake_Docks.Lake_Docks:PersistentLevel.IO_DLC2_Crew_Gifts_2.BP_CrewChallengeComp_Gifts_DLC2',
            '/Hibiscus/Maps/Lake/Lake_CrewHunt.Lake_CrewHunt:PersistentLevel.IO_DLC2_Crew_Hunt_2.BP_CrewChallengeComp_Hunt_DLC2',
            ]),
        ("Heart's Desire", 'Venue_P', [
            '/Hibiscus/Maps/Venue/Venue_Combat.Venue_Combat:PersistentLevel.IO_DLC2_Crew_Hunt_2.BP_CrewChallengeComp_Hunt_DLC2',
            '/Hibiscus/Maps/Venue/Venue_P.Venue_P:PersistentLevel.IO_DLC2_Crew_Mancubus_Brain_2.BP_CrewChallengeComp_Mancubus_DLC2',
            ]),
        ("Cursehaven", 'Village_P', [
            '/Hibiscus/Maps/Village/Village_CrewChallenges.Village_CrewChallenges:PersistentLevel.IO_DLC2_Crew_Mancubus_Brain_2.BP_CrewChallengeComp_Mancubus_DLC2',
            '/Hibiscus/Maps/Village/Village_CrewChallenges.Village_CrewChallenges:PersistentLevel.IO_DLC2_Crew_Hunt_2.BP_CrewChallengeComp_Hunt_DLC2',
            #'/Hibiscus/Maps/Village/Village_CrewChallenges.Village_CrewChallenges:PersistentLevel.IO_DLC2_Crew_Gifts_2.BP_CrewChallengeComp_Gifts_DLC2',
            ]),
        ("Cankerwood", 'Woods_P', [
            '/Hibiscus/Maps/Woods/Woods_Combat.Woods_Combat:PersistentLevel.IO_DLC2_Crew_Mancubus_Brain_2.BP_CrewChallengeComp_Mancubus_DLC2',
            '/Hibiscus/Maps/Woods/Woods_Combat.Woods_Combat:PersistentLevel.IO_DLC2_Crew_Hunt_2.BP_CrewChallengeComp_Hunt_DLC2',
            #'/Hibiscus/Maps/Woods/Woods_IO.Woods_IO:PersistentLevel.IO_DLC2_Crew_Gifts_2.BP_CrewChallengeComp_Gifts_DLC2',
            ]),

        ]):

    mod.comment(label)
    for object_name in object_names:
        mod.reg_hotfix(Mod.LEVEL, level_name,
                object_name,
                'DetectionRadius',
                radius,
                notify=True)
        mod.reg_hotfix(Mod.LEVEL, level_name,
                object_name,
                'DetectionHalfHeight',
                height,
                notify=True)
        mod.reg_hotfix(Mod.LEVEL, level_name,
                object_name,
                'UnfogRadiusWhenChallengeActive',
                unfog_radius,
                notify=True)
    mod.newline()

mod.close()
