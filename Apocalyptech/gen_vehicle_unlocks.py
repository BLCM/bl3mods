#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('vehicle_unlocks.txt',
        'Vehicle Unlocks',
        [
            "Unlocks most vehicle parts/skins from the beginning of the game.  Wheel",
            "types, unfortunately, can't be unlocked early, but the others should be",
            "available as soon as the associated vehicles are.",
        ],
        'VUnlocks',
        )

mod.header('Remove level restrictions for parts')

for (label, table, col_name, rows) in [
        ('Vehicle Parts (table 1)',
            '/Game/Vehicles/_Shared/Design/Balance/Data/DataTable_VehiclePartsData',
            'MinGameStage_15_D986BDE142AA94D9995403BC41D5DA70',
            [
                'Technical_StickyBombs',
                'Technical_FlakCannon',
                'Technical_ToxicBooster',
                'Technical_FuelBarrels',
                'Outrunner_TwitchyWheels',
                'Outrunner_HoverWheels',
                'Outrunner_TeslaCoil',
                'Outrunner_FlameThrower',
                'Outrunner_ShotgunMissile',
                'Outrunner_SwarmerMissile',
                'Outrunner_BlazeBooster',
                'Revolver_DualWheel',
                'Revolver_HoverWheels',
                'Revolver_HeavyArmor',
                'Revolver_FireStarter',
                'Revolver_SpikeLauncher',
                'Revolver_SawBladeLauncher',
                ]),
        ('Vehicle Parts (table 2)',
            '/Game/Vehicles/_Shared/Design/Balance/Data/DataTable_VehiclePartsSchedule',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            [
                'Technical_Mod_ToxicBoost',
                'Technical_Mod_FuelBarrels',
                'Technical_Armor_Heavy',
                'Technical_Wep_FlakCannon',
                'Outrunner_Wheels_Twitchy',
                'Outrunner_Wheels_Hover',
                'Outrunner_Mod_BlazeBoost',
                'Outrunner_Wep_Flamethrower',
                'Outrunner_Wep_TeslaCoil',
                'Outrunner_Wep_SwarmerMissile',
                'Outrunner_Wep_ShotgunMissile',
                'Revolver_Wheel_Dual',
                'Revolver_Wheel_Hover',
                'Revolver_Mod_FireStarter',
                'Revolver_Armor_Heavy',
                'Revolver_Wep_SpikeLauncher',
                'Revolver_Wep_Sawblades',
                ]),
        ('Vehicle Skins',
            '/Game/Vehicles/_Shared/Design/Balance/Data/DataTable_VehicleSkinSchedule',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            [
                'Outrunner_PsychoMobile',
                'Outrunner_Houndstooth',
                'Outrunner_Forest',
                'Outrunner_GoldenHog',
                'Outrunner_Borderlandstton',
                'Outrunner_HistoricRacing',
                'Outrunner_Bubblegum',
                'Outrunner_RageCage',
                'Outrunner_Pirate',
                'Outrunner_RedMachine',
                'Technical_Bubblegum',
                'Technical_Desert',
                'Technical_Blueangels',
                'Technical_Halftone',
                'Technical_Forest',
                'Technical_Leather',
                'Technical_Stealth',
                'Technical_Thunderbird',
                'Revolver_Chopper',
                'Revolver_Lollipop',
                'Revolver_Dark',
                'Revolver_Forest',
                'Revolver_Bubblegum',
                'Revolver_Golden',
                'Revolver_Lifeline',
                'Revolver_Maliwan',
                'Revolver_Stealth',
                ]),
        ]:
    full_table = Mod.get_full(table)
    mod.comment(label)
    for row in rows:
        mod.table_hotfix(Mod.PATCH, '',
                full_table,
                row,
                col_name,
                0)
    mod.newline()

# Fix any skin errors
mod.header('Skin fixes')

mod.comment('Fix Outrunner Red Machine MaxGameStage')
for level in [
        'Prologue_P',
        'Outskirts_P',
        'Desert_P',
        'MotorcadeFestival_P',
        'Convoy_P',
        'City_P',
        'Desolate_P',
        ]:
    mod.reg_hotfix(Mod.LEVEL, level,
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_RedMachine.VehiclePart_Mat_VehiclePart_Outrunner_RedMachine',
            'MaxGameStage.DataTableValue.ValueName',
            'MaxGameStage_18_5DDD0AF343807440C74B37A083027F1C')
mod.newline()

mod.header('Spawn as many parts as possible')

def make_partlist(parts):
    """
    I'm honestly not sure if BPVehiclePart_C is the correct object name prefix to use on
    the PartData attribute, but it seems to work, so eh?
    """
    construct = []
    for part in parts:
        last_bit = part.split('/')[-1]
        full_part = '{}.{}'.format(part, last_bit)
        construct.append("""(
            PartData=BPVehiclePart_C'"{}"',
            Weight=(BaseValueConstant=1)
        )""".format(full_part))
    return '({})'.format(','.join(construct))

vehicle_parts = [
        ('Outrunner',
            {
                ('COV',
                    '/Game/Vehicles/Outrunner/Design/PartSets/COTV/Outrunner_VehiclePartSet_Enemy_COTV',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner',
                    (0, 1)): [
                        'Prologue_P',
                        'Outskirts_P',
                        # The Badass PartSet references this, so adding the badass maps here, too, just in case.
                        'Desert_P',
                        'MotorcadeFestival_P',
                        'Convoy_P',
                        ],
                ('COV Badass',
                    '/Game/Vehicles/Outrunner/Design/PartSets/COTV/Outrunner_VehiclePartSet_Enemy_COTV_Badass',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner_Badass',
                    (0, 1)): [
                        'Desert_P',
                        'MotorcadeFestival_P',
                        'Convoy_P',
                        ],
                ('COV @ Sandblast Scar',
                    '/Game/Vehicles/Outrunner/Design/PartSets/COTV/Outrunner_VehiclePartSet_Enemy_COTV_Convoy',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Convoy/SpawnOptions_Outrunner_CotV_Convoy',
                    (0, 1)): [
                        'Convoy_P',
                        ],
                ('COV @ Carnivora',
                    '/Game/Vehicles/Outrunner/Design/PartSets/COTV/Outrunner_VehiclePartSet_Enemy_COTV_CarnivoraChase',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Carnivora/SpawnOptions_Outrunner_CotV_Carnivora',
                    (0, 1)): [
                        'MotorcadeFestival_P',
                        ],
                ('COV @ Devil\'s Razor',
                    '/Game/Vehicles/Outrunner/Design/PartSets/COTV/Outrunner_VehiclePartSet_Enemy_COTV_Desert',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Desert/SpawnOptions_Outrunner_CotV_Desert',
                    (0, 1)): [
                        'Desert_P',
                        ],
                ('Maliwan',
                    '/Game/Vehicles/Outrunner/Design/PartSets/Outrunner_VehiclePartSet_Enemy_Maliwan',
                    '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Outrunner',
                    (0, 1)): [
                        'City_P',
                        # The PartSet is *referenced* by DarkMaliwan; putting this in here just in case.
                        'Desolate_P',
                        ],
                ('Maliwan Badass',
                    '/Game/Vehicles/Outrunner/Design/PartSets/Outrunner_VehiclePartSet_Enemy_Maliwan_Badass',
                    '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Outrunner_Badass',
                    (0, 1)): [
                        'City_P',
                        # The PartSet is *referenced* by DarkMaliwan; putting this in here just in case.
                        'Desolate_P',
                        ],
                ('Dark Maliwan',
                    '/Game/Vehicles/Outrunner/Design/PartSets/Outrunner_VehiclePartSet_Enemy_DarkMaliwan',
                    '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Outrunner',
                    (0, 1)): [
                        'Desolate_P',
                        ],
                ('Dark Maliwan Badass',
                    '/Game/Vehicles/Outrunner/Design/PartSets/Outrunner_VehiclePartSet_Enemy_DarkMaliwan_Badass',
                    '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Outrunner_Badass',
                    (0, 1)): [
                        'Desolate_P',
                        ],
                },
            [
                # Skins
                [
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Atlas',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Batmobile',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_COV',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Dahl',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Default',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Ellie1',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_FF',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Fire',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Forest',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_GBX',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Gold',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Grog',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Gulf',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Herbie',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Hexagon',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Houndstooth',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_HubbaBubba',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Hyp',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Hyp2',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Infection',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Jakobs',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Maliwan',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Maya',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Pirate',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Prisa',
                    # Note that Red Machine will only spawn *exactly* at its MinGameStage unless the fix above is in place
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_RedMachine',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_SDCC',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Stealth',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Torgue',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Tri',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Vladof',
                    '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Wrap',
                    ],
                # Armor
                [
                    '/Game/Vehicles/Outrunner/Design/Parts/Armor/VehiclePart_Outrunner_Armor_BasicArmor',
                    '/Game/Vehicles/Outrunner/Design/Parts/Armor/VehiclePart_Outrunner_Armor_HeavyArmor',
                    ],
                # Gunner Weapons
                [
                    '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_MissileLauncher/HeavyMissile/VehiclePart_Weapon_HeavyMissile_Native',
                    '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_MissileLauncher/SwarmerMissile/VehiclePart_Weapon_SwarmerMissile_Native',
                    '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_MissileLauncher/ShotgunMissile/VehiclePart_Weapon_ShotgunMissile_Native',
                    ],
                # Driver Weapons
                [
                    '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MachineGun/OutrunnerMachineGun/VehiclePart_WeaponDriver_OutrunnerMachineGun_Native',
                    '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_FlameThrower/FlameThrower/VehiclePart_WeaponDriver_FlameThrower_Native',
                    '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_FlameThrower/TeslaCoil/VehiclePart_WeaponDriver_TeslaCoil_Native',
                    ],
                # Boosts
                [
                    '/Game/Vehicles/Outrunner/Design/Parts/CoreMod/BoostCanisters/VehiclePart_CoreMod_BoostCanisters',
                    '/Game/Vehicles/Outrunner/Design/Parts/CoreMod/BlazeBooster/VehiclePart_CoreMod_BlazeBooster',
                    '/Game/Vehicles/Outrunner/Design/Parts/CoreMod/EnergyCells/VehiclePart_CoreMod_EnergyCells',
                    '/Game/Vehicles/Outrunner/Design/Parts/CoreMod/RazerWings/VehiclePart_CoreMod_RazerWings',
                    ],
            ]),

        ('Technical',
            {
                ('COV',
                    '/Game/Vehicles/Technical/Design/PartSets/VehiclePartSet_Technical_COTV',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Technical',
                    (0,)): [
                        'Outskirts_P',
                        'CityVault_P',
                        ],
                ('COV Badass',
                    '/Game/Vehicles/Technical/Design/PartSets/VehiclePartSet_Technical_COTV_Badass',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Technical_Badass',
                    (0,)): [
                        'Outskirts_P',
                        'Wetlands_P',
                        'Convoy_P',
                        'Motorcade_P',
                        'MotorcadeFestival_P',
                        ],
                ('COV @ Sandblast Scar',
                    '/Game/Vehicles/Technical/Design/PartSets/COTV/VehiclePartSet_Technical_COTV_Convoy',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Convoy/SpawnOptions_Technical_CotV_Convoy',
                    (0,)): [
                        'Convoy_P',
                        ],
                ('COV @ Splinterlands',
                    '/Game/Vehicles/Technical/Design/PartSets/COTV/VehiclePartSet_Technical_COTV_Motorcade',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Motorcade/SpawnOptions_Technical_CotV_Motorcade',
                    (0,)): [
                        'Motorcade_P',
                        # Looks like this can probably get called from Carnivora, too
                        'MotorcadeFestival_P',
                        ],
                ('COV @ Neon Arterial',
                    '/Game/Vehicles/Technical/Design/PartSets/COTV/VehiclePartSet_Technical_COTV_CityVault',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_1/CityVault/SpawnOptions_Technical_CotV_CityVault',
                    (0,)): [
                        'CityVault_P',
                        ],
                ('COV @ Floodmoor Basin',
                    '/Game/Vehicles/Technical/Design/PartSets/COTV/VehiclePartSet_Technical_COTV_Wetlands',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_2/Wetlands/SpawnOptions_Technical_CotV_Wetlands',
                    (0,)): [
                        'Wetlands_P',
                        ],
                ('Meridian Outskirts Hover Technical (mission-specific but continues to spawn)',
                    # Note the exact same object for both!
                    '/Game/Enemies/_Spawning/Vehicles/Technical/SpawnOptions_Vehicle_EP05_HoverTechnical',
                    '/Game/Enemies/_Spawning/Vehicles/Technical/SpawnOptions_Vehicle_EP05_HoverTechnical',
                    (0,)): [
                        'Outskirts_P',
                        ],
                },
            [
                # Skins
                [
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Atlas',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Bling',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_BlueAngel',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Bubblegum',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Camo',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Checker',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Cov',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Dahl',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Default',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Dino',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_E3',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Ellie1',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Festi',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Forest',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_GBX',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_GoldenTicket',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Halftone',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_HYP',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_JAK',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_MAL',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Maya',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Plaid',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Roadkill',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Sand',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Skag',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Stealth',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Thunderbird',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Torgue',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Vaughn',
                    '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Vladof',
                    ],
                # Armor
                [
                    '/Game/Vehicles/Technical/Design/Parts/Armor/VehiclePart_Techincal_Armor_BasicArmor',
                    '/Game/Vehicles/Technical/Design/Parts/Armor/VehiclePart_Technical_Armor_HeavyArmor',
                    '/Game/Vehicles/Technical/Design/Parts/Armor/VehiclePart_Technical_Armor_MeatGrinder',
                    ],
                # Gunner Weapons
                [
                    '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_Catapult/BarrelLauncher/VehiclePart_Weapon_BarrelLauncher_Native',
                    '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_Catapult/PropelledBombsLauncher/VehiclePart_Weapon_PropelledBombsLauncher_Native',
                    '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_Catapult/StickyBombLauncher/VehiclePart_Weapon_StickyBombs_Native',
                    ],
                # Driver Weapons
                [
                    '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MachineGun/MachineGun/VehiclePart_WeaponDriver_MachineGun_Native',
                    '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MachineGun/FlakCannon/VehiclePart_WeaponDriver_FlakCannon_Native',
                    ],
                # Boosters
                [
                    '/Game/Vehicles/Technical/Design/Parts/Accessory/ToxicBooster/VehiclePart_CoreMod_ToxicBooster',
                    '/Game/Vehicles/Technical/Design/Parts/Accessory/FuelBarrels/VehiclePart_CoreMod_FuelBarrels',
                    '/Game/Vehicles/Technical/Design/Parts/Accessory/FlatBed/VehiclePart_CoreMod_Flatbed',
                    '/Game/Vehicles/Technical/Design/Parts/Accessory/JetBooster/VehiclePart_CoreMod_JetBooster',
                    ],
            ]),

        ('Cyclone',
            {
                ('COV',
                    '/Game/Vehicles/Revolver/Design/PartSets/Revolver_VehiclePartSet_Enemy_COTV',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Revolver',
                    (0, 1)): [
                        'Convoy_P',
                        ],
                ('COV Badass',
                    '/Game/Vehicles/Revolver/Design/PartSets/Revolver_VehiclePartSet_Enemy_COTV_Badass',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Revolver_Badass',
                    (0, 1)): [
                        'Wetlands_P',
                        'MotorcadeFestival_P',
                        'Convoy_P',
                        'Desert_P',
                        'Motorcade_P',
                        ],
                ('COV @ Sandblast Scar',
                    '/Game/Vehicles/Revolver/Design/PartSets/COTV/VehiclePartSet_Revolver_CotV_Convoy',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Convoy/SpawnOptions_Revolver_CotV_Convoy',
                    (0, 1)): [
                        'Convoy_P',
                        ],
                ('COV @ Carnivora',
                    '/Game/Vehicles/Revolver/Design/PartSets/COTV/VehiclePartSet_Revolver_CotV_Carnivora',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Carnivora/SpawnOptions_Revolver_CotV_Carnivora',
                    (0, 1)): [
                        'MotorcadeFestival_P',
                        ],
                ('COV @ Devil\'s Razor',
                    '/Game/Vehicles/Revolver/Design/PartSets/COTV/VehiclePartSet_Revolver_CotV_Desert',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Desert/SpawnOptions_Revolver_CotV_Desert',
                    (0, 1)): [
                        'Desert_P',
                        ],
                ('COV @ Splinterlands',
                    '/Game/Vehicles/Revolver/Design/PartSets/COTV/VehiclePartSet_Revolver_CotV_Motorcade',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Motorcade/SpawnOptions_Revolver_CotV_Motorcade',
                    (0, 1)): [
                        'Motorcade_P',
                        # Looks like this can probably get called from Canivora as well.
                        'MotorcadeFestival_P',
                        ],
                ('COV @ Floodmoor Basin',
                    '/Game/Vehicles/Revolver/Design/PartSets/COTV/VehiclePartSet_Revolver_CotV_Wetlands',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_2/Wetlands/SpawnOptions_Revolver_CotV_Wetlands',
                    (0, 1)): [
                        'Wetlands_P',
                        ],
                ('COV @ Neon Arterial',
                    '/Game/Vehicles/Revolver/Design/PartSets/COTV/VehiclePartSet_Revolver_CotV_CityVault',
                    '/Game/Enemies/_Spawning/CotV/Vehicles/Zone_1/CityVault/SpawnOptions_Revolver_CotV_CityVault',
                    (0, 1)): [
                        'CityVault_P',
                        ],
                ('Maliwan',
                    '/Game/Vehicles/Revolver/Design/PartSets/Revolver_VehiclePartSet_Enemy_Maliwan',
                    '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Revolver',
                    (0, 1)): [
                        'City_P',
                        # Dark Maliwan (and Dark Maliwan Badass) references this partset, so I'm putting
                        # their levels here, too
                        'Desolate_P',
                        ],
                ('Maliwan Badass',
                    '/Game/Vehicles/Revolver/Design/PartSets/Revolver_VehiclePartSet_Enemy_Maliwan_Badass',
                    '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Revolver_Badass',
                    (0, 1)): [
                        'City_P',
                        ],
                ('Dark Maliwan',
                    '/Game/Vehicles/Revolver/Design/PartSets/Revolver_VehiclePartSet_Enemy_DarkMaliwan',
                    '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Revolver',
                    (0, 1)): [
                        'Desolate_P',
                        ],
                ('Dark Maliwan Badass',
                    '/Game/Vehicles/Revolver/Design/PartSets/Revolver_VehiclePartSet_Enemy_DarkMaliwan_Badass',
                    '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Revolver_Badass',
                    (0, 1)): [
                        'Desolate_P',
                        ],
                },
            [
                # Materials
                [
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Atlas',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Chopper',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Chups',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_COV',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Dahl',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Dark',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Default',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Ellie1',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Forest',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_GBX',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_GC',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_HubbaBubba',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Hyp',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Hyp2',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Jakobs',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_LifeSaver',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Maliwan',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Mask',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Maya',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Ninja',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Pepto',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Police',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Stealth',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Torgue',
                    '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Vladof',
                    ],
                # Armor
                [
                    '/Game/Vehicles/Revolver/Design/Parts/Armor/VehiclePart_Revolver_Armor_BasicArmor',
                    '/Game/Vehicles/Revolver/Design/Parts/Armor/VehiclePart_Revolver_Armor_HeavyArmor',
                    ],
                # Gunner Weapon
                [
                    ],
                # Driver Weapon
                [
                    '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MechanicalLauncher/SawBladeLancer/VehiclePart_WeaponDriver_SawBladeLauncher_Native',
                    '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MechanicalLauncher/RevolverMachineGun/VehiclePart_WeaponDriver_RevolverMachineGun_Native',
                    '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MechanicalLauncher/BlazeRodLancer/VehiclePart_WeaponDriver_BlazeRodLauncher_Native',
                    ],
                # Booster
                [
                    '/Game/Vehicles/Revolver/Design/Parts/CoreMod/HeavyBooster/VehiclePart_HeavyBooster',
                    '/Game/Vehicles/Revolver/Design/Parts/CoreMod/Firestarter/VehiclePart_FireStarter',
                    '/Game/Vehicles/Revolver/Design/Parts/CoreMod/DigiThruster/VehiclePart_DigiThruster',
                    '/Game/Vehicles/Revolver/Design/Parts/CoreMod/CryoBooster/VehiclePart_CryoBooster',
                    ],
            ]),
    ]

for (vehicle, object_mapping, master_partlist) in vehicle_parts:

    # Set up our PartList parts and Balance TOC (and also flatten the array
    # in prep for the Balance)
    partlist_parts = []
    flattened_parts = []
    balance_toc_parts = []
    for parts in master_partlist:
        partlist_parts.append(make_partlist(parts))
        if len(parts) > 0:
            balance_toc_parts.append((len(flattened_parts), len(parts)))
        else:
            balance_toc_parts.append((-1, 0))
        flattened_parts.extend(parts)

    # Set up our Balance parts and toc
    balance_parts = make_partlist(flattened_parts)
    toc_construct = []
    for (start_idx, part_len) in balance_toc_parts:
        toc_construct.append('(StartIndex={},NumParts={})'.format(start_idx, part_len))
    balance_toc = '({})'.format(','.join(toc_construct))

    # Now loop through and do the statements
    for (part_label, partset_obj, balance_obj, balance_nums), levels in object_mapping.items():
        partset_obj_full = Mod.get_full(partset_obj)
        balance_obj_full = Mod.get_full(balance_obj)
        option_probability = '{:.02f}%'.format(1/len(balance_nums)*100)
        for level in levels:

            mod.comment('{} - {} (in {})'.format(vehicle, part_label, level))

            # It looks like these have to be EARLYLEVEL in order to fully preload properly
            for (part_idx, parts) in enumerate(partlist_parts):
                mod.reg_hotfix(Mod.EARLYLEVEL, level,
                        partset_obj_full,
                        'ActorPartLists.ActorPartLists[{}].Parts'.format(part_idx),
                        parts)

            # Now set the Balance parts and TOC (can be regular LEVEL)
            for balance_num in balance_nums:
                mod.reg_hotfix(Mod.LEVEL, level,
                        balance_obj_full,
                        'Options.Options[{}].Factory.Object..CustomVehicleInventoryBalanceData.Object..RuntimePartList.AllParts'.format(balance_num),
                        balance_parts)
                mod.reg_hotfix(Mod.LEVEL, level,
                        balance_obj_full,
                        'Options.Options[{}].Factory.Object..CustomVehicleInventoryBalanceData.Object..RuntimePartList.PartTypeTOC'.format(balance_num),
                        balance_toc)

                # Also set each option to be equally-likely.  Not really sure how these two vars
                # interact with each other.
                if len(balance_nums) > 1:
                    mod.reg_hotfix(Mod.LEVEL, level,
                            balance_obj_full,
                            'Options.Options[{}].WeightParam.Range.Value'.format(balance_num),
                            1)
                    mod.reg_hotfix(Mod.LEVEL, level,
                            balance_obj_full,
                            'Options.Options[{}].Probability'.format(balance_num),
                            option_probability)

            mod.newline()

mod.close()
