#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('better_rare_spawn_hunt_stripped.txt',
        'Pared-down alteration of Week 2 Event',
        [
            'Mostly just ensures that the rare spawns will appear at 100%.  Other',
            'functionality has been moved, as appropriate, into Better Loot.',
            '',
            'https://borderlands.com/en-US/news/2019-10-07-borderlands-3-rare-spawn-hunt/',
            'https://github.com/BLCM/bl3hotfixes/blob/master/gbx_info_archive/2019-10-07-anniversary_2.md',
        ],
        'Week2Stripped',
        )

# Make all rare spawns 100%
mod.comment('General level-based spawn rates (unchanged from stock GBX hotfixes, but for all levels)')
mod.comment("I'm not actually sure if the extra levels make any difference (it definitely shouldn't")
mod.comment('for stuff like the trials/slaughters, for instance), but eh.')
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
                '/Game/GameData/Balance/RareSpawns/Table_Async_RareSpawnRarities.Table_Async_RareSpawnRarities',
                row_name,
                'Value',
                """(
                    BaseValueConstant=100.000000,
                    DataTableValue=(DataTable=None,RowName="",ValueName=""),
                    BaseValueAttribute=None,
                    AttributeInitializer=None,
                    BaseValueScale=1.000000
                )""")
mod.newline()

# Some individual spawn rates which apparently don't use those values above
# TODO: I think Brood Mother (Pyre of Stars) needs something similar
mod.comment('Individual Spawn rates')
mod.reg_hotfix(Mod.LEVEL, 'Towers_P',
        '/Game/Maps/Zone_1/Towers/Towers_Combat.Towers_Combat:PersistentLevel.OakMissionRareSpawner_VicAndWarty',
        'PercentChanceToSpawn',
        """(
            BaseValueConstant=100.000000,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1.000000
        )""")
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
