#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('guaranteed_rare_spawns.txt',
        'Guarantee all rare spawns',
        [
            "Ensures that all BL3 rare spawns will appear at 100%.  This is actually",
            "mostly unnecessary now, as GBX has decided to permanently buff them to",
            "100% after their Farming Frenzy event, but I'll keep them in here anyway.",
            "",
            "This *does* also buff most rare vehicle spawns, too, which GBX does not",
            "do yet.  Rare Vehicle spawns should be maybe about 10% per vehicle spawn.",
        ])

# Make all rare spawns 100%.  We specify a lot more levels than GBX does, and I don't
# think that the extra levels actually do any good, but whatever.
mod.comment('General level-based spawn rates')
for level_name in [
        'AtlasHQ_P',
        'Beach_P',
        'BloodyHarvest_P',
        'COVSlaughter_P',
        'CityBoss_P',
        'CityVault_P',
        'City_P',
        'Convoy_P',
        'CreatureSlaughter_P',
        'Crypt_P',
        'DesertBoss_P',
        'Desert_P',
        'Desertvault_P',
        'Desolate_P',
        'FinalBoss_P',
        'Mansion_P',
        'MarshFields_P',
        'Mine_P',
        'Monastery_P',
        'MotorcadeFestival_P',
        'MotorcadeInterior_P',
        'Motorcade_P',
        'OrbitalPlatform_P',
        'Outskirts_P',
        'Prison_P',
        'Prologue_P',
        'ProvingGrounds_Trial1_P',
        'ProvingGrounds_Trial4_P',
        'ProvingGrounds_Trial5_P',
        'ProvingGrounds_Trial6_P',
        'ProvingGrounds_Trial7_P',
        'ProvingGrounds_Trial8_P',
        'Raid_P',
        'Recruitment_P',
        'Sacrifice_P',
        'Sanctuary3_P',
        'TechSlaughter_P',
        'Towers_P',
        'Watership_P',
        'WetlandsBoss_P',
        'WetlandsVault_P',
        'Wetlands_P',
        ]:
    for row_name in [
            'Rare',
            'VeryRare',
            'SuperRare',
            ]:
        mod.table_hotfix(Mod.LEVEL, level_name,
                '/Game/GameData/Balance/RareSpawns/Table_Async_RareSpawnRarities',
                row_name,
                'Value',
                BVCF(bvc=100))
mod.newline()

# Some individual spawn rates which apparently don't use those values above
# TODO: I think Brood Mother (Pyre of Stars) needs something similar.  GBX
# has said that Brood Mother's spawn actually depends on killing mobs outside
# her lair, so I should look into that...
mod.header('Individual Spawn rates')

mod.comment('Wick and Warty')
mod.reg_hotfix(Mod.LEVEL, 'Towers_P',
        '/Game/Maps/Zone_1/Towers/Towers_Combat.Towers_Combat:PersistentLevel.OakMissionRareSpawner_VicAndWarty',
        'PercentChanceToSpawn',
        BVCF(bvc=100))
mod.newline()

mod.comment('Amach')
mod.reg_hotfix(Mod.LEVEL, 'Village_P',
        '/Hibiscus/Maps/Village/Village_Combat.Village_Combat:PersistentLevel.OakMissionRareSpawner_1',
        'PercentChanceToSpawn',
        BVCF(bvc=100))
mod.newline()

mod.comment('Fungal Gorger')
mod.reg_hotfix(Mod.LEVEL, 'Woods_P',
        '/Hibiscus/Maps/Woods/Woods_Combat.Woods_Combat:PersistentLevel.OakMissionRareSpawner_1',
        'PercentChanceToSpawn',
        BVCF(bvc=100))
mod.newline()

mod.comment('Shiverous the Unscathed and Voltborn (not sure which is which)')
mod.reg_hotfix(Mod.LEVEL, 'Camp_P',
        '/Hibiscus/Maps/Camp/Camp_Combat.Camp_Combat:PersistentLevel.OakMissionRareSpawner_0',
        'PercentChanceToSpawn',
        BVCF(bvc=100))
mod.reg_hotfix(Mod.LEVEL, 'Camp_P',
        '/Hibiscus/Maps/Camp/Camp_Combat.Camp_Combat:PersistentLevel.OakMissionRareSpawner_1',
        'PercentChanceToSpawn',
        BVCF(bvc=100))
mod.newline()

# Rare Vehicle Spawns
mod.header_lines([
    "Rare Vehicle Spawns",
    "",
    "Due to how these work, these won't be *guaranteed* spawns, but",
    "they'll be much more likely, at least.  Aiming for about a 10%",
    "unique-vehicle spawn rate, in the levels which have them.  Note",
    "that Skagzilla's spawn is defined very differently than the",
    "others, and isn't touched in here at all.",
    ])

for (label, levels, spawnoptions, weights) in [
        ('Clever Girl / Bayou Watch (in Floodmoor Basin)',
            ['Wetlands_P'],
            '/Game/Enemies/_Spawning/CotV/Vehicles/Zone_2/SpawnOptions_Vehicle_CotV_WetlandsMix',
            # Defaults: 1 (technicals), 0.6 (cyclones), 0.01 (clever girl), 0.01 (bayou watch)
            [1, 0.6, 0.1, 0.1]),
        ("Houndstooth (in Devil's Razor)",
            ['Desert_P'],
            '/Game/Enemies/_Spawning/CotV/Vehicles/Zone_3/Desert/SpawnOptions_Vehicle_CotV_DesertMix',
            # Defaults: 1 (outrunners), 1 (cyclones), 0.01 (houndstooth)
            [1, 1, 0.25]),
        ("Candy (in Desolation's Edge)",
            ['Desolate_P'],
            '/Game/Enemies/_Spawning/Maliwan/Vehicles/Zone4/Desolate_P/SpawnOptions_Vehicle_DarkMaliwan_DesolateMix',
            # Defaults: 0.6 (outrunners), 1 (cyclones), 0.01 (candy)
            [0.6, 1, 0.2]),
        ('Festive Flesh-Eater (in Splinterlands and Carnivora)',
            ['Motorcade_P', 'MotorcadeFestival_P'],
            '/Game/Enemies/_Spawning/CotV/Vehicles/Zone_3/Motorcade_P/SpawnOptions_Vehicle_CotV_Motorcade_FullMix',
            # Defaults: 1 (technicals), 0.6 (cyclones), 0.01 (festive flesh-eater)
            [1, 0.6, 0.2]),
        ]:

    # Process the data a bit.
    spawnoptions_full = Mod.get_full(spawnoptions)
    total_weight = sum(weights)

    # Go!
    mod.comment(label)
    for idx, weight in enumerate(weights):
        pct_weight = weight/total_weight*100
        for level in levels:
            mod.reg_hotfix(Mod.LEVEL, level,
                    spawnoptions_full,
                    'Options.Options[{}].WeightParam.Range.Value'.format(idx),
                    weight)
            mod.reg_hotfix(Mod.LEVEL, level,
                    spawnoptions_full,
                    'Options.Options[{}].Probability'.format(idx),
                    '{:.02f}%'.format(pct_weight))
    mod.newline()

mod.close()
