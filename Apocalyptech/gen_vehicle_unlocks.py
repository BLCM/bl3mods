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

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('vehicle_unlocks.txt',
        'Vehicle Unlocks',
        'Apocalyptech',
        [
            "Unlocks most vehicle parts/skins from the beginning of the game.  Wheel",
            "types, unfortunately, can't be unlocked early, but the others should be",
            "available as soon as the associated vehicles are.  Vehicles will always",
            "pull from the entire available part/skin pools, so there will be a much",
            "greater variety of vehicles from the beginning of the game (at the cost",
            "of having more strongly-themed vehicles per area).",
            "",
            "Also converts Clever Girl, Festive Flesh-Eater, Skagzilla, and all",
            "Technicals in Sandblast Scar to the Monster Wheels variety, so that",
            "there's ingame sources for the Monster Wheels."
        ],
        lic=Mod.CC_BY_SA_40,
        )

# A list of all levels where vehicles can show up
# (We don't have to worry about this for Jetbeasts, there aren't level restrictions on those)
outrunner_levels = {
        'Prologue_P',
        'Sacrifice_P',
        'Outskirts_P',
        'Desert_P',
        'MotorcadeFestival_P',
        'Convoy_P',
        'City_P',
        'Desolate_P',
        }
technical_levels = {
        'Outskirts_P',
        'CityVault_P',
        'Wetlands_P',
        'Convoy_P',
        'Motorcade_P',
        'MotorcadeFestival_P',
        'Lake_P',
        }
cyclone_levels = {
        'Convoy_P',
        'Wetlands_P',
        'MotorcadeFestival_P',
        'Desert_P',
        'Motorcade_P',
        'CityVault_P',
        'Desolate_P',
        'City_P',
        }
all_levels = outrunner_levels|technical_levels|cyclone_levels

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
        for level in sorted(all_levels):
            if ((level in outrunner_levels and row.startswith('Outrunner_'))
                    or (level in technical_levels and row.startswith('Technical_'))
                    or (level in cyclone_levels and row.startswith('Revolver_'))):
                mod.table_hotfix(Mod.LEVEL, level,
                        full_table,
                        row,
                        col_name,
                        0)
    mod.newline()

# Fix any skin errors
mod.header('Fixes/Tweaks')

mod.comment('Fix Outrunner Red Machine Skin MaxGameStage')
for level in sorted(outrunner_levels):
    mod.reg_hotfix(Mod.LEVEL, level,
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_RedMachine.VehiclePart_Mat_VehiclePart_Outrunner_RedMachine',
            'MaxGameStage.DataTableValue.ValueName',
            'MaxGameStage_18_5DDD0AF343807440C74B37A083027F1C')
mod.newline()

for (label, levels, spawn_obj) in [
        ('Technicals in Sandblast Scar',
            ['Convoy_P'],
            '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Convoy/SpawnOptions_Technical_CotV_Convoy.SpawnOptions_Technical_CotV_Convoy'),
        ('Clever Girl (in Floodmoor Basin)',
            ['Wetlands_P'],
            '/Game/Enemies/_Spawning/Vehicles/RareSpawns/SpawnOptions_RareVehicle_Technical_CleverGirl.SpawnOptions_RareVehicle_Technical_CleverGirl'),
        ('Festive Flesh-Eater (in Splinterlands and Carnivora)',
            ['Motorcade_P', 'MotorcadeFestival_P'],
            '/Game/Enemies/_Spawning/Vehicles/RareSpawns/SpawnOptions_RareVehicle_Technical_Princess.SpawnOptions_RareVehicle_Technical_Princess'),
        ('Skagzilla (in The Droughts)',
            ['Prologue_P'],
            '/Game/Enemies/_Spawning/Vehicles/RareSpawns/SpawnOptions_RareVehicle_Technical_Skagzilla.SpawnOptions_RareVehicle_Technical_Skagzilla'),
        ]:
    mod.comment('Make {} use Monster Wheels'.format(label))
    for level in levels:
        mod.reg_hotfix(Mod.LEVEL, level,
                spawn_obj,
                'Options[0].Factory.Object..VehicleClass',
                'Vehicle_Technical_BigWheels_C\'"/Game/Vehicles/Technical/Vehicle/Vehicle_Technical_BigWheels.Vehicle_Technical_BigWheels"\'')
        mod.reg_hotfix(Mod.LEVEL, level,
                spawn_obj,
                'Options[0].Factory.Object..CustomInventoryData.Object..InventoryActorClass',
                'Vehicle_Technical_BigWheels_C\'"/Game/Vehicles/Technical/Vehicle/Vehicle_Technical_BigWheels.Vehicle_Technical_BigWheels"\'')
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
                # This one works different than all the rest; the parts used are directly on
                # `Balance_Outrunner_BuggyWheels_Basic`, and it doesn't use the "Builder" objects that
                # basically every other spawn uses.
                #('COV @ Ascension Bluff',
                #    '/Game/Vehicles/Outrunner/Design/PartSets/Outrunner_VehiclePartSet_All',
                #    '/Game/Missions/Plot/Ep02_Sacrifice/SpawnOptions_CotV_Outrunner_Basic',
                #    (0,)): [
                #        'Sacrifice_P',
                #        ],
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

                    # DLC2 skins
                    '/Game/PatchDLC/Hibiscus/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Fish',
                    '/Game/PatchDLC/Hibiscus/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Tentacle',
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
                ('Frostbiters in Skittermaw Basin',
                    '/Hibiscus/Enemies/_Spawning/Vehicles/VehiclePartSet_Technical_Hibiscus',
                    '/Hibiscus/Enemies/_Spawning/Vehicles/SpawnOptions_Vehicle_Frostbiter_Lake_FullMix',
                    (0,)): [
                        'Lake_P',
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

                    # DLC2 Skins
                    '/Game/PatchDLC/Hibiscus/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Tentacle',
                    '/Game/PatchDLC/Hibiscus/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Fish',
                    '/Game/PatchDLC/Hibiscus/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Frost',
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

                    # DLC2 skins
                    '/Game/PatchDLC/Hibiscus/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Fish',
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

        ('Jetbeast',
            {
                ('Devil Riders',
                    '/Geranium/Vehicles/Horse/PartSets/Horse_VehiclePartSet_All',
                    '/Geranium/Enemies/_Spawning/Vehicles/Horse/SpawnOptions_Vehicle_Horse_ALL',
                    (0, 1, 2)): [
                        'Frontier_P',
                        ],
                },
            [
                # Materials
                [
                    '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Default',
                    '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Skin1',
                    '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Skin2',
                    '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Skin3',
                    '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Skin4',
                    '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Skin5',
                    ],
                # Armor
                [
                    '/Geranium/Vehicles/Horse/Design/Parts/Armor/VehiclePart_Horse_Armor_HardSaddleBags',
                    '/Geranium/Vehicles/Horse/Design/Parts/Armor/VehiclePart_Horse_Armor_SoftSaddleBags',
                    ],
                # Gunner Weapon
                [
                    ],
                # Driver Weapon
                [
                    '/Geranium/Vehicles/VehicleWeapons/Type_DualMachineGun/VehiclePart_WeaponDriver_Horse_DualMachineGun',
                    '/Geranium/Vehicles/VehicleWeapons/Type_Cannon/VehiclePart_WeaponDriver_Horse_Cannon',
                    '/Geranium/Vehicles/VehicleWeapons/Type_Mortar/VehiclePart_Weapon_Horse_Mortar',
                    ],
                # Booster
                [
                    '/Geranium/Vehicles/Horse/Design/Parts/CoreMod/TwinEngine/VehiclePart_TwinEngine_Horse',
                    '/Geranium/Vehicles/Horse/Design/Parts/CoreMod/SingleEngine/VehiclePart_SingleBooster_Horse',
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

# Now we need to do one weird little custom thing for the Outrunners in
# Ascension Bluff.  Note that these aren't *fully* unlocked like the other
# maps, but it's pretty close; I think it's only missing a couple of skins.
mod.comment('Nonstandard Fixes for Outrunnners in Ascension Bluff')
for num in range(42):
    mod.reg_hotfix(Mod.LEVEL, 'Sacrifice_P',
            '/Game/Missions/Plot/Ep02_Sacrifice/Balance_Outrunner_BuggyWheels_Basic',
            'RuntimePartList.AllParts.AllParts[{}].Weight.BaseValueConstant'.format(num),
            1)
mod.newline()

mod.close()
