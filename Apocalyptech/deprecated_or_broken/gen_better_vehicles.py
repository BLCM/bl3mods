#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('better_vehicles.txt',
        'Better Vehicles',
        [
        ])

# Mostly I just want to make the hovering more speedy so I can have, effectively,
# sandskiffs across all vehicle types.  I've tried a few variations of the
# statements below, to no avail.  Boo.
#
# getall vehiclehovercomponent dampingforce
# getall vehiclehovercomponent brakingdampingforce

# In terms of what I *think* should work, the _GEN_VARIABLE var itself is almost
# certainly the one to use.  It's just a matter of finding a hotfix syntax which
# fires at the right time, because that object doesn't exist until the vehicle's
# actually loaded in.

# Just gonna go ahead and try out every combination I can think of, here.
# If something starts working I can start excluding.
for trigger_method, trigger_names in [
        (Mod.PACKAGE, [
            'WT_Outrunner_HoverWheels',
            '/Game/Vehicles/Outrunner/Design/WT_Outrunner_HoverWheels',
            'Balance_Outrunner_HoverWheels',
            '/Game/Vehicles/Outrunner/Design/BalanceStates/Balance_Outrunner_HoverWheels',
            'Vehicle_Outrunner_HoverWheels',
            '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner_HoverWheels',
            # Longshots here, referenced by the Vehicle_Outrunner_HoverWheels uasset...
            'Vehicle_Outrunner',
            '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner',
            'AspectData_Outrunner_Hover',
            '/Game/Vehicles/_Shared/Effects/Data/AspectData_Outrunner_Hover',
            # Something new to try?
            'MatchAll',
            ]),
        (Mod.CHAR, [
            'WT_Outrunner_HoverWheels',
            'Balance_Outrunner_HoverWheels',
            'Vehicle_Outrunner_HoverWheels',
            'Vehicle_Outrunner',
            'AspectData_Outrunner_Hover',
            # Something new to try?
            'MatchAll',
            ]),
        (Mod.POST, [
            # These are *all* longshots, no idea what this hotfix type would even be
            # intended for.
            'WT_Outrunner_HoverWheels',
            '/Game/Vehicles/Outrunner/Design/WT_Outrunner_HoverWheels',
            'Balance_Outrunner_HoverWheels',
            '/Game/Vehicles/Outrunner/Design/BalanceStates/Balance_Outrunner_HoverWheels',
            'Vehicle_Outrunner_HoverWheels',
            '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner_HoverWheels',
            'Vehicle_Outrunner',
            '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner',
            'AspectData_Outrunner_Hover',
            '/Game/Vehicles/_Shared/Effects/Data/AspectData_Outrunner_Hover',
            '',
            ]),
        ]:
    for trigger_name in trigger_names:
        for obj_name in [
                '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner_HoverWheels.Vehicle_Outrunner_HoverWheels_C:VehicleHover',
                '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner_HoverWheels.Vehicle_Outrunner_HoverWheels_C:VehicleHover_GEN_VARIABLE',
                ]:
            for var, new_val in [
                    ('DampingForce', 0.5),
                    ('BrakingDampingForce', 0.5),
                    ]:
                for notify in [True, False]:
                    mod.reg_hotfix(trigger_method, trigger_name,
                            obj_name,
                            var,
                            new_val,
                            notify=notify)

mod.close()
