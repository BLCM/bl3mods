#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2022 Christopher J. Kucera
# <cj@apocalyptech.com>
# <https://apocalyptech.com/contact.php>
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

import os
import sys
import argparse
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import LVL_TO_ENG_LOWER

# Written while doing Mega TimeSaver XL -- wanted to pre-generate Elevator
# snippets.  Note that this serializes every map object in the game!  See
# Fragile Containers' generation script for a quick way to clean that up.
# (Also, Fragile Containers uses mulitprocessing to parallelize the
# serialization, which is quite a bit faster -- honestly you might want to
# do the serializations by running that generation script and then come
# back here to run.)

data = BL3Data()

class Elevator:

    def __init__(self, path, speed=None, travel=None):
        self.path = path
        self.speed = speed
        self.travel = travel

# Find base Elevator objects
elevators = {}
for obj_name in data.find('', 'Elevator'):
    obj_last = obj_name.rsplit('/', 1)[-1]
    if obj_last in elevators:
        print('WARNING: Duplicate elevator name {obj_last} found')
        continue
    obj_data = data.get_data(obj_name)
    for export in obj_data:
        if export['_jwp_object_name'].startswith('Default__'):
            speed = None
            travel = None
            if 'ElevatorSpeed' in export:
                speed = export['ElevatorSpeed']
            if 'ElevatorTravelTime' in export:
                travel = export['ElevatorTravelTime']
            elevators[obj_last] = Elevator(obj_name, speed, travel)
            break

# Now loop through all levels and process the objects we care about.
for level_orig in [
        '/Alisma/Maps/Anger/Anger_P',
        '/Alisma/Maps/Chase/Chase_P',
        '/Alisma/Maps/Eldorado/Eldorado_P',
        '/Alisma/Maps/Experiment/Experiment_P',
        '/Alisma/Maps/Sanctum/Sanctum_P',
        '/Dandelion/Maps/CasinoIntro/CasinoIntro_P',
        '/Dandelion/Maps/Core/Core_P',
        '/Dandelion/Maps/Impound/Impound_P',
        '/Dandelion/Maps/Strip/Strip_P',
        '/Dandelion/Maps/TowerLair/TowerLair_P',
        '/Dandelion/Maps/Trashtown/Trashtown_P',
        '/Game/Maps/ProvingGrounds/Trial1/ProvingGrounds_Trial1_P',
        '/Game/Maps/ProvingGrounds/Trial4/ProvingGrounds_Trial4_P',
        '/Game/Maps/ProvingGrounds/Trial5/ProvingGrounds_Trial5_P',
        '/Game/Maps/ProvingGrounds/Trial6/ProvingGrounds_Trial6_P',
        '/Game/Maps/ProvingGrounds/Trial7/ProvingGrounds_Trial7_P',
        '/Game/Maps/ProvingGrounds/Trial8/ProvingGrounds_Trial8_P',
        '/Game/Maps/Sanctuary3/Sanctuary3_P',
        '/Game/Maps/Slaughters/COVSlaughter/COVSlaughter_P',
        '/Game/Maps/Slaughters/CreatureSlaughter/CreatureSlaughter_P',
        '/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_P',
        '/Game/Maps/Zone_0/FinalBoss/FinalBoss_P',
        '/Game/Maps/Zone_0/Prologue/Prologue_P',
        '/Game/Maps/Zone_0/Recruitment/Recruitment_P',
        '/Game/Maps/Zone_0/Sacrifice/Sacrifice_P',
        '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_P',
        '/Game/Maps/Zone_1/City/City_P',
        '/Game/Maps/Zone_1/CityBoss/CityBoss_P',
        '/Game/Maps/Zone_1/CityVault/CityVault_P',
        '/Game/Maps/Zone_1/Monastery/Monastery_P',
        '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_P',
        '/Game/Maps/Zone_1/Outskirts/Outskirts_P',
        '/Game/Maps/Zone_1/Towers/Towers_P',
        '/Game/Maps/Zone_2/Mansion/Mansion_P',
        '/Game/Maps/Zone_2/MarshFields/MarshFields_P',
        '/Game/Maps/Zone_2/Prison/Prison_P',
        '/Game/Maps/Zone_2/Watership/Watership_P',
        '/Game/Maps/Zone_2/Wetlands/Wetlands_P',
        '/Game/Maps/Zone_2/WetlandsBoss/WetlandsBoss_P',
        '/Game/Maps/Zone_2/WetlandsVault/WetlandsVault_P',
        '/Game/Maps/Zone_3/Convoy/Convoy_P',
        '/Game/Maps/Zone_3/Desert/Desert_P',
        '/Game/Maps/Zone_3/DesertBoss/DesertBoss_P',
        '/Game/Maps/Zone_3/DesertVault/Desertvault_P',
        '/Game/Maps/Zone_3/Mine/Mine_P',
        '/Game/Maps/Zone_3/Motorcade/Motorcade_P',
        '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_P',
        '/Game/Maps/Zone_3/MotorcadeInterior/MotorcadeInterior_P',
        '/Game/Maps/Zone_4/Beach/Beach_P',
        '/Game/Maps/Zone_4/Crypt/Crypt_P',
        '/Game/Maps/Zone_4/Desolate/Desolate_P',
        '/Game/PatchDLC/BloodyHarvest/Maps/Seasons/BloodyHarvest/BloodyHarvest_P',
        '/Game/PatchDLC/Event2/Maps/Cartels_P',
        '/Game/PatchDLC/Raid1/Maps/Raid/Raid_P',
        '/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_P',
        '/Geranium/Maps/CraterBoss/CraterBoss_P',
        '/Geranium/Maps/Facility/Facility_P',
        '/Geranium/Maps/Forest/Forest_P',
        '/Geranium/Maps/Frontier/Frontier_P',
        '/Geranium/Maps/Lodge/Lodge_P',
        '/Geranium/Maps/Town/Town_P',
        '/Hibiscus/Maps/Archive/Archive_P',
        '/Hibiscus/Maps/Bar/Bar_P',
        '/Hibiscus/Maps/Camp/Camp_P',
        '/Hibiscus/Maps/Lake/Lake_P',
        '/Hibiscus/Maps/Venue/Venue_P',
        '/Hibiscus/Maps/Village/Village_P',
        '/Hibiscus/Maps/Woods/Woods_P',
        '/Ixora/Maps/FrostSite/FrostSite_P',
        '/Ixora2/Maps/Boss/SacrificeBoss_p',
        '/Ixora2/Maps/Cabin/Cabin_P',
        '/Ixora2/Maps/Mystery/Nekro/NekroMystery_p',
        '/Ixora2/Maps/Mystery/Pandora/PandoraMystery_p',
        '/Ixora2/Maps/Noir/Noir_P',
        ]:
    level_base, level_short = level_orig.rsplit('/', 1)
    level_eng = LVL_TO_ENG_LOWER[level_short.lower()]
    for map_name in sorted(data.find(level_base, ''), key=str.casefold):
        map_data = data.get_data(map_name)
        map_last = map_name.rsplit('/', 1)[-1]
        if map_data:
            for export in map_data:
                if export['export_type'].startswith('Elevator') and not export['_jwp_object_name'].startswith('Default__'):
                    full_name = '{}/{}.{}:PersistentLevel.{}'.format(
                            level_base,
                            map_last,
                            map_last,
                            export['_jwp_object_name'],
                            )

                    # These have been experimentally verified to be the defaults when there's
                    # literally no info in the serializations anywhere.
                    speed = 200
                    travel = 10

                    class_name = export['export_type'][:-2]
                    if class_name in elevators:
                        el = elevators[class_name]
                        if el.speed is not None:
                            speed = el.speed
                        if el.travel is not None:
                            travel = el.travel

                    if 'ElevatorSpeed' in export:
                        speed = export['ElevatorSpeed']
                    if 'ElevatorTravelTime' in export:
                        travel = export['ElevatorTravelTime']

                    level_eng = LVL_TO_ENG_LOWER[level_short.lower()]

                    print('        # {}'.format(class_name))
                    print('        ("{}", \'{}\','.format(level_eng, level_short))
                    print('            \'{}\','.format(full_name))
                    print('            {}, {}),'.format(speed, travel))
                    print('')

