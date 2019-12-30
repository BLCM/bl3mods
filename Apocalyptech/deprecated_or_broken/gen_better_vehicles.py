#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('better_vehicles.txt',
        'Better Vehicles',
        [
        ],
        'BetterVehicles',
        )

# Mostly I just want to make the hovering more speedy so I can have, effectively,
# sandskiffs across all vehicle types.  I've tried a few variations of the
# statements below, to no avail.  Boo.

mod.reg_hotfix(Mod.LEVEL, 'Prologue_P',
        '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner_HoverWheels.Vehicle_Outrunner_HoverWheels_C:VehicleHover_GEN_VARIABLE',
        'DampingForce',
        0)

mod.reg_hotfix(Mod.LEVEL, 'Prologue_P',
        '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner_HoverWheels.Vehicle_Outrunner_HoverWheels_C:VehicleHover_GEN_VARIABLE',
        'BrakingDampingForce',
        0)

mod.close()
