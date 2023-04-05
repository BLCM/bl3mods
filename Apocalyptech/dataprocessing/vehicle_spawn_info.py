#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from bl3data.bl3data import BL3Data

# Used when building out Vehicle Unlocks v2.0.0.  Just data gathering to
# make sure I knew how all the vanilla spawn stuff looked.

data = BL3Data()

spawnoptions = [
        '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner',
        '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner_Badass',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Convoy/SpawnOptions_Outrunner_CotV_Convoy',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Carnivora/SpawnOptions_Outrunner_CotV_Carnivora',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Desert/SpawnOptions_Outrunner_CotV_Desert',
        '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Outrunner',
        '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Outrunner_Badass',
        '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Outrunner',
        '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Outrunner_Badass',

        '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Technical',
        '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Technical_Badass',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Convoy/SpawnOptions_Technical_CotV_Convoy',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Motorcade/SpawnOptions_Technical_CotV_Motorcade',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_1/CityVault/SpawnOptions_Technical_CotV_CityVault',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_2/Wetlands/SpawnOptions_Technical_CotV_Wetlands',
        '/Game/Enemies/_Spawning/Vehicles/Technical/SpawnOptions_Vehicle_EP05_HoverTechnical',
        '/Hibiscus/Enemies/_Spawning/Vehicles/SpawnOptions_Vehicle_Frostbiter_Lake_FullMix',

        '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Revolver',
        '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Revolver_Badass',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Convoy/SpawnOptions_Revolver_CotV_Convoy',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Carnivora/SpawnOptions_Revolver_CotV_Carnivora',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Desert/SpawnOptions_Revolver_CotV_Desert',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Motorcade/SpawnOptions_Revolver_CotV_Motorcade',
        '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_2/Wetlands/SpawnOptions_Revolver_CotV_Wetlands',
        '/Game/Enemies/_Spawning/CotV/Vehicles/Zone_1/CityVault/SpawnOptions_Revolver_CotV_CityVault',
        '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Revolver',
        '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Revolver_Badass',
        '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Revolver',
        '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Revolver_Badass',

        '/Geranium/Enemies/_Spawning/Vehicles/Horse/SpawnOptions_Vehicle_Horse_ALL',

        ]

class InventoryData:

    def __init__(self, invdata, obj):
        self.invdata = invdata
        self.obj = obj
        self.name = invdata['_jwp_object_name']
        assert(len(invdata['TitlePartList']) == 1)
        self.title = invdata['TitlePartList'][0][1]

class PWeight:

    def __init__(self, count, weight):
        self.count = count
        self.weight = weight
        self.total = None

    @staticmethod
    def from_data(data):
        return PWeight(data['PassengerCount'], data['Weight'])

    def set_total(self, total):
        self.total = total
        self.pct = self.weight/total*100

    def __str__(self):
        if round(self.pct, 6) == int(self.pct):
            report_val = int(self.pct)
        else:
            report_val = '{:0.1f}'.format(self.pct)
        return '{} @ {}% ({})'.format(self.count, report_val, self.weight)

class Factory:

    def __init__(self, factory, obj):
        self.factory = factory
        self.obj = obj
        self.name = factory['_jwp_object_name']
        self.invdata = InventoryData(obj[factory['CustomInventoryData']['export']-1], obj)
        self.uiname = factory['UINameOverride'][1]
        self.vehicle_class = factory['VehicleClass'][1]
        if 'DefaultSpawnOptions' in factory:
            self.default_rider = factory['DefaultSpawnOptions'][1]
        else:
            self.default_rider = None
        self.riders = set()
        self.riders_l = []
        for seat in factory['SeatList']:
            self.riders.add(seat['SpawnOptions'][1])
            self.riders_l.append(seat['SpawnOptions'][1])
        self.num_seats = len(factory['SeatList'])

        self.passenger_weights = [PWeight(1, 1)]
        if 'WeightedPassengersNum' in factory:
            if factory['bWeightedPassengersNum']:
                self.passenger_weights = []
                for thing in factory['WeightedPassengersNum']:
                    self.passenger_weights.append(PWeight.from_data(thing))

        self.total_passenger_weight = sum([p.weight for p in self.passenger_weights])
        for p in self.passenger_weights:
            p.set_total(self.total_passenger_weight)

        self.origin = (factory['SpawnOrigin']['x'], factory['SpawnOrigin']['y'], factory['SpawnOrigin']['z'])
        self.extent = (factory['SpawnExtent']['x'], factory['SpawnExtent']['y'], factory['SpawnExtent']['z'])
        self.team = factory['CachedTeam'][1]

class Option:

    def __init__(self, option, obj):
        self.option = option
        self.obj = obj
        self.factory = Factory(obj[option['Factory']['export']-1], obj)
        self.prob_text = option['Probability']
        assert(option['WeightParam']['DisabledValueModes'] == 110)
        assert(option['AliveLimitParam']['DisabledValueModes'] == 110)
        assert(option['AliveLimitParam']['ValueType'] == 'EGbxParamValueType::Int')

for spawnoption in spawnoptions:

    print(spawnoption)
    print('='*len(spawnoption))
    print('')

    obj = data.get_data(spawnoption)

    options = []
    for export in obj:
        if export['export_type'] == 'SpawnOptionData':
            for option in export['Options']:
                options.append(Option(option, obj))

    for idx, option in enumerate(options):
        print('{}: {}'.format(
            idx,
            option.factory.name,
            ))
        print('   - Vehicle: {}'.format(option.factory.vehicle_class))
        print('   - UIName: {}'.format(option.factory.uiname))
        print('   - Origin: {}'.format(option.factory.origin))
        print('   - Extent: {}'.format(option.factory.extent))
        #print('   - Invdata Title: {}'.format(option.factory.invdata.title))
        print('   - Team: {}'.format(option.factory.team))
        print('   - Num Passengers: {}'.format(', '.join([str(p) for p in option.factory.passenger_weights])))
        if len(option.factory.riders) == 1 and option.factory.default_rider == list(option.factory.riders)[0]:
            print('   - Single rider type defined: {}'.format(option.factory.default_rider))
        else:
            print('   - Default Rider: {}'.format(option.factory.default_rider))
            print('   - Riders: {}'.format(', '.join(sorted(option.factory.riders))))
        if 'Outrunner' in spawnoption:
            if option.factory.num_seats != 2:
                print('   - *** {} rider(s) found... ***'.format(option.factory.num_seats))
        elif 'Technical' in spawnoption or 'Frostbiter' in spawnoption:
            if option.factory.num_seats != 4:
                print('   - *** {} rider(s) found... ***'.format(option.factory.num_seats))
            if option.factory.riders_l[0] != option.factory.riders_l[1] or option.factory.riders_l[2] != option.factory.riders_l[3]:
                print('   - *** mismatch in drivers/passengers ***')
        elif 'Revolver' in spawnoption:
            if option.factory.num_seats != 1:
                print('   - *** {} rider(s) found... ***'.format(option.factory.num_seats))
        elif 'Horse' in spawnoption:
            if option.factory.num_seats != 1:
                print('   - *** {} rider(s) found... ***'.format(option.factory.num_seats))
        else:
            raise RuntimeError('unknown spawnoption...')
        print('')

