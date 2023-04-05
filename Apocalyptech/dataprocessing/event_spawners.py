#!/usr/bin/env python3
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

import csv
import sys
import enum
from bl3data.bl3data import BL3Data

data = BL3Data()

class SpawnDLCData:

    def __init__(self, label, obj_name):
        global data
        self.label = label
        self.obj_name = obj_name
        self.spawners = set()

        obj = data.get_data(self.obj_name)[0]
        for ss in obj['ScriptedSpawners']:
            for ssp in ss['SpawnerSoftPaths']:
                self.spawners.add('{}:{}'.format(
                    ssp['SpawnerPathName'],
                    ssp['SpawnerSubPathString'],
                    ))
        print('Loaded from {}: {}'.format(self.label, len(self.spawners)))

        if 'ExpansionScriptedSpawners' in obj:
            for ess in obj['ExpansionScriptedSpawners']:
                other_data = SpawnDLCData('dummy', ess[1])
                self.spawners |= other_data.spawners

events = [SpawnDLCData(l, n) for l, n in [
    ('Bloody Harvest', '/Game/PatchDLC/BloodyHarvest/GameData/SpawnDLCScripts/SpawnDLC_BloodyHarvest'),
    ('Broken Hearts', '/Game/PatchDLC/EventVDay/GameData/SpawnDLCScripts/SpawnDLC_VDay'),
    ('Cartels', '/Game/PatchDLC/Event2/GameData/SpawnDLCSCripts/SpawnDLC_Cartels'),
    ]]

in_all = set(events[0].spawners)
for event in events[1:]:
    in_all &= event.spawners

print('In all: {}'.format(len(in_all)))
for event in events:
    print('Extras in {}: {}'.format(
        event.label,
        len(event.spawners) - len(in_all),
        ))

