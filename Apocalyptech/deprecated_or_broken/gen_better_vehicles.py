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
