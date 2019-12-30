#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

# Trying to figure out how to modify vehicle part (or any gun part, really) weights, with the
# eventual intention of making all vehicle parts equally likely to spawn.
#
# The efforts below are just specifically trying to make the Bubblegum Outrunner skin the
# only one spawnable in the early levels (like the Droughts).  No luck yet, alas.  Giving
# up for now; I've yet to successfully construct one of these "complex" object references
# myself.  :(

mod = Mod('vehicle_unlocks_test.txt',
        'Vehicle Unlocks Test',
        [
        ],
        'VUnlocksTest',
        )

# I think this one's used when the SpawnOptions doesn't explicitly override/set anything
for idx in [0, 1, 2, 4, 5]:
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Vehicles/Outrunner/Design/PartSets/COTV/Outrunner_VehiclePartSet_Enemy_COTV.Outrunner_VehiclePartSet_Enemy_COTV',
            f'ActorPartLists.ActorPartLists[0].Parts[{idx}].Weight.BaseValueConstant',
            0)

# ... whereas this is the SpawnOptions being precise about things.  No idea wtf I'm doing here.
#for suffix in ['', '_0', '_1', '_2']:
#    for idx in [0, 1, 2, 4, 5]:
#        #mod.reg_hotfix(Mod.LEVEL, 'Prologue_P',
#        mod.reg_hotfix(Mod.PATCH, '',
#                #f'/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner.SpawnOptions_CotV_Outrunner:CustomVehicleInventoryBalanceData{suffix}',
#                f'/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner.SpawnOptions_CotV_Outrunner:InventoryBalanceData{suffix}',
#                f'RuntimePartList.AllParts[{idx}].Weight.BaseValueConstant',
#                0)

#for opt_idx in [0, 1]:
#    for idx in [0, 1, 2, 4, 5]:
#        mod.reg_hotfix(Mod.PATCH, '',
#                f'/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner.SpawnOptions_CotV_Outrunner',
#                f'Options.Options[{opt_idx}].Factory.Object..CustomVehicleInventoryBalanceData.Object..RuntimePartList.AllParts[{idx}].Weight.BaseValueConstant',
#                0)

#for suffix in ['', '_0', '_1', '_2']:
#    for idx in [0, 1, 2, 4, 5]:
#        mod.reg_hotfix(Mod.PATCH, '',
#                f'/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner.SpawnOptions_CotV_Outrunner:Factory_SpawnFactory_OakVehicleBuilder{suffix}',
#                #f'CustomVehicleInventoryBalanceData.Object..RuntimePartList.AllParts[{idx}].Weight.BaseValueConstant',
#                f'CustomVehicleInventoryBalanceData.RuntimePartList.AllParts[{idx}].Weight.BaseValueConstant',
#                0)

for suffix in ['', '_0', '_1', '_2']:
    for idx in [0, 1, 2, 4, 5]:
        mod.reg_hotfix(Mod.PATCH, '',
                #f'/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner.SpawnOptions_CotV_Outrunner:Factory_SpawnFactory_OakVehicleBuilder{suffix}.CustomVehicleInventoryBalanceData',
                f'/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner.SpawnOptions_CotV_Outrunner:Factory_SpawnFactory_OakVehicleBuilder{suffix}.InventoryBalanceData',
                f'RuntimePartList.AllParts[{idx}].Weight.BaseValueConstant',
                0)

mod.close()
