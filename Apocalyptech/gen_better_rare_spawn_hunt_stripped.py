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

mod.close()
