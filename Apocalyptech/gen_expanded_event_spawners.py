#!/usr/bin/env python
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

import collections
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

# Mod to expand the limited-time event enemy spawn modifications so that they
# apply to every location that's been used in an event thus far.  Each one
# has at least a slightly different set of locations, it seems.  Cartel
# operatives don't show up in Voracious Canopy, for instance, and neither
# Bloody Harvest nor Broken Hearts will be active in DLC2.
#
# Note that our processing here sort of depends on the "Description" field
# of the objects in question being the same between events, though I think
# that things would probably still work fine even if they weren't (you'd
# just have duplicate definitions in the objects).  It looks like they've
# been copy+pasting them, so far, though, so we're good for now.
#
# These generate huge hotfixes -- Broken Hearts and Bloody Harvest are
# composed of a single 200KB hotfix each, whereas Cartels is the same size
# but split over three statements.
#
# This is, as so many of my things tend to be, rather overcomplicated, no
# doubt.

data = BL3Data()
expansion_objs = [
        ('Bloody Harvest', 'bloody_harvest', '/Game/PatchDLC/BloodyHarvest/GameData/SpawnDLCScripts/SpawnDLC_BloodyHarvest'),
        ('Broken Hearts', 'broken_hearts', '/Game/PatchDLC/EventVDay/GameData/SpawnDLCScripts/SpawnDLC_VDay'),
        ('Revenge of the Cartels', 'cartels', '/Game/PatchDLC/Event2/GameData/SpawnDLCSCripts/SpawnDLC_Cartels'),
        ]

SoftPath = collections.namedtuple('SoftPath', ['SpawnerPathName', 'SpawnerSubPathString'])

class ScriptedSpawner(object):

    def __init__(self, description):

        self.description = description
        self.soft_paths = []

    def add_soft_path(self, path_name, sub_path):

        self.soft_paths.append(SoftPath(path_name, sub_path))

    @staticmethod
    def from_data(obj_data):

        # Just checking to see if I have to worry about any of this.
        msspgo = obj_data['MaximumScriptedSpawnersPerGroupOverride']
        assert(msspgo['ValueType'] == 'EGbxParamValueType::Float')
        assert(msspgo['DisabledValueModes'] == 64)
        assert(msspgo['ValueFlags'] == 0)
        assert(msspgo['ValueMode'] == 'EGbxParamValueMode::Value')
        assert(msspgo['Range']['Value'] == 0)
        assert(msspgo['Range']['Variance'] == 0)
        assert('export' in msspgo['AttributeInitializer'])
        assert(msspgo['AttributeInitializer']['export'] == 0)
        assert('export' in msspgo['AttributeData'])
        assert(msspgo['AttributeData']['export'] == 0)
        aid = msspgo['AttributeInitializationData']
        assert(aid['BaseValueConstant'] == 0)
        assert('export' in aid['DataTableValue']['DataTable'])
        assert(aid['DataTableValue']['DataTable']['export'] == 0)
        assert('export' in aid['BaseValueAttribute'])
        assert(aid['BaseValueAttribute']['export'] == 0)
        assert('export' in aid['AttributeInitializer'])
        assert(aid['AttributeInitializer']['export'] == 0)
        assert(aid['BaseValueScale'] == 1)
        assert(msspgo['BlackboardKey']['KeyName'] == 'None')
        assert(not msspgo['BlackboardKey']['bRuntimeKey'])
        assert('export' in msspgo['Condition'])
        assert(msspgo['Condition']['export'] == 0)
        assert('export' in msspgo['Actor'])
        assert(msspgo['Actor']['export'] == 0)
        assert(not obj_data['bAlwaysEnabledDuringEvent'])

        spawner = ScriptedSpawner(obj_data['Description'])
        for path in obj_data['SpawnerSoftPaths']:
            spawner.add_soft_path(path['SpawnerPathName'], path['SpawnerSubPathString'])
        return spawner

    def to_hotfix(self):
        # Looks like all the other values are just defaults, so we can get away with this.
        return """(
                Description="{description}",
                SpawnerSoftPaths=({softpaths})
            )""".format(
                    description=self.description,
                    softpaths=','.join([
                        '(SpawnerPathName="{}",SpawnerSubPathString="{}")'.format(
                            p.SpawnerPathName,
                            p.SpawnerSubPathString,
                            ) for p in self.soft_paths
                        ])
                    )

class SpawnDLC(object):

    def __init__(self, data, spawn_name):

        self.obj_name = spawn_name
        self.short_name = spawn_name.split('/')[-1]

        spawn_obj = data.get_data(spawn_name)[0]

        self.spawners = []
        self.spawners_by_desc = {}
        for spawner_obj in spawn_obj['ScriptedSpawners']:
            spawner = ScriptedSpawner.from_data(spawner_obj)
            self.spawners.append(spawner)
            assert(spawner.description not in self.spawners_by_desc)
            self.spawners_by_desc[spawner.description] = spawner

        self.expansions = []
        if 'ExpansionScriptedSpawners' in spawn_obj:
            for exp_obj in spawn_obj['ExpansionScriptedSpawners']:
                exp = SpawnDLC(data, exp_obj[1])
                for desc in exp.spawners_by_desc.keys():
                    assert(desc not in self.spawners_by_desc)
                self.expansions.append(exp)

    def get_descriptions(self):
        descriptions = list(self.spawners_by_desc.keys())
        for exp in self.expansions:
            descriptions.extend(exp.get_descriptions())
        return descriptions

    def has_description(self, desc):
        return desc in set(self.get_descriptions())

    def get_desc_count(self, desc):
        if desc in self.spawners_by_desc:
            return len(self.spawners_by_desc[desc].soft_paths)
        for exp in self.expansions:
            length = exp.get_desc_count(desc)
            if length is not None:
                return length
        return None

    def get_spawner(self, desc):
        if desc in self.spawners_by_desc:
            return self.spawners_by_desc[desc]
        for exp in self.expansions:
            if exp.has_description(desc):
                return exp.get_spawner(desc)
        return None

    def get_softpaths(self, desc):
        if desc in self.spawners_by_desc:
            return self.spawners_by_desc[desc].soft_paths
        for exp in self.expansions:
            paths = exp.get_softpaths(desc)
            if paths is not None:
                return paths
        return None

    def add_spawner(self, description):
        assert(not self.has_description(description))
        new_spawner = ScriptedSpawner(description)
        self.spawners.append(new_spawner)
        self.spawners_by_desc[description] = new_spawner
        return new_spawner

    def to_hotfix(self):
        return '({})'.format(','.join([s.to_hotfix() for s in self.spawners]))

    def generate_hotfixes(self, mod):
        # This does have to be EARLYLEVEL for it to take effect on the first
        # level you join.
        mod.reg_hotfix(Mod.EARLYLEVEL, 'MatchAll',
                self.obj_name,
                'ScriptedSpawners',
                self.to_hotfix())
        for exp in self.expansions:
            exp.generate_hotfixes(mod)

# Load in all the data from each of our SpawnDLC objects
spawndlcs = []
all_descs = set()
for _, _, exp_obj in expansion_objs:
    spawndlc = SpawnDLC(data, exp_obj)
    all_descs |= set(spawndlc.get_descriptions())
    spawndlcs.append(spawndlc)

# Go through and process by description now.
for desc in sorted(all_descs):

    # Get a list of all paths which are in use for this description
    all_paths = set()
    for spawndlc in spawndlcs:
        paths = spawndlc.get_softpaths(desc)
        if paths is not None:
            all_paths |= set(paths)

    # Now loop through each spawndlc and add in anything missing
    for spawndlc in spawndlcs:

        # If we don't have the spawner *at all*, add it.
        if not spawndlc.has_description(desc):
            print('{}: Adding spawner in {}'.format(desc, spawndlc.short_name))
            spawndlc.add_spawner(desc)

        # Get the spawner
        spawner = spawndlc.get_spawner(desc)

        # Find what softpaths to add
        to_add = all_paths - set(spawner.soft_paths)
        if len(to_add) > 0:
            print('{}: Adding {} softpaths in {}'.format(desc, len(to_add), spawndlc.short_name))
        for path in to_add:
            spawner.add_soft_path(path.SpawnerPathName, path.SpawnerSubPathString)

# Now generate hotfixes
print('')
print('Writing mod files:')
print('')
for (label, filename, _), spawndlc in zip(expansion_objs, spawndlcs):

    full_filename = 'expanded_event_spawners_{}.txt'.format(filename)

    mod = Mod(full_filename,
            'Expanded Event Spawners: {}'.format(label),
            'Apocalyptech',
            [
                "Updates the {}-specific enemy spawn modifications so that".format(label),
                "it occurs in every location which has been used in limited-time events",
                "so far.  Bloody Harvest, Broken Hearts, and Revenge of the Cartels have",
                "all had at least slightly differing activation locations, so this evens",
                "it out to apply for anything that's been touched.",
                "",
                "Note that this does not yet equate to Literally Everywhere - Droughts",
                "and Covenant Pass won't have any, for instance.",
            ],
            lic=Mod.CC_BY_SA_40,
            )

    spawndlc.generate_hotfixes(mod)

    mod.close()
    print('Wrote to {}'.format(full_filename))

