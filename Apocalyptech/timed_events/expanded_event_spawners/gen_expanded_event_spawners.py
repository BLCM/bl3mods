#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2021 Christopher J. Kucera
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

import os
import re
import sys
import lzma
import collections
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF, LVL_TO_ENG

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

    map_re = re.compile(r'^(?P<obj_path>/.+/Maps/(Zone_\d+/|Mystery/)?[^/]+)/(?P<obj_base>[^/\.]+)\.(?P=obj_base)$')
    spawner_re = re.compile(r' Oak(Mission(Rare)?)?Spawner (?P<level_base_obj>.*?)\.(?P=level_base_obj)\.(?P<attribute>.*?)(_(?P<num_suffix>\d+))?$')

    def __init__(self, description, soft_paths=None):

        self.description = description
        if soft_paths:
            self.soft_paths = soft_paths
        else:
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

    @staticmethod
    def from_object_name_dumps(names_filename, objects_filename, description, excluders=set()):
        """
        This method gleans a set of SoftPaths from an object-name dump file, of the sort
        generated by the Universal Unreal Engine 4 Unlocker app, and various other UE4
        introspection tools.  Specifically, `names_filename` should be `UE4Tools_NamesDump.txt.xz`
        or the like, and `objects_filename` should be `UE4Tools_ObjectsDump.txt.xz` or the
        like -- they should be LZMA-compressed (hence the `.xz` extension).  `description`
        will be the description field in the object (presumably almost entirely unimportant,
        though perhaps it's supposed to be unique -- this app will force uniqueness).
        `excluders` is a set of SubPathString names to *not* add in, even if they're found.
        (Used by me to omit various NPCs, etc.)
        """

        # First create a map of objects found in the level (which we'll need to construct
        # the full object reference).  This'll actually find much more than just level-name
        # mappings, but whatever.
        level_obj_mapping = {}
        with lzma.open(names_filename, 'rt', encoding='utf8') as df:
            for line in df:
                _, obj_full = line.split(' ', 1)
                match = ScriptedSpawner.map_re.search(obj_full.strip())
                if match:
                    level_obj_mapping[match.group('obj_base')] = match.group('obj_path')
                    if match.group('obj_base').endswith('_BuiltData'):
                        level_obj_mapping[match.group('obj_base')[:-10]] = match.group('obj_path')

        # Now loop through the object names
        spawners = []
        with lzma.open(objects_filename, 'rt', encoding='utf8') as df:
            for line in df:
                match = ScriptedSpawner.spawner_re.search(line)
                if match:
                    base_obj = match.group('level_base_obj')
                    #assert(match.group('level_base_obj') in level_obj_mapping)
                    if match.group('num_suffix'):
                        subpath = '{}_{}'.format(match.group('attribute'), int(match.group('num_suffix'))-1)
                    else:
                        subpath = match.group('attribute')
                    if '{}.{}'.format(base_obj, subpath) not in excluders:
                        spawners.append(SoftPath(
                            '{}/{}.{}'.format(level_obj_mapping[base_obj], base_obj, base_obj),
                            subpath,
                            ))

        # Debugging (and figuring out excluders)
        #for s in spawners:
        #    first, last = s.SpawnerPathName.rsplit('.', 1)
        #    print('{} -> {}.{}'.format(first, last, s.SpawnerSubPathString))

        # Lastly, create and return the object
        return ScriptedSpawner(description, spawners)

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

    def add_scriptedspawner(self, scriptedspawner):
        assert(scriptedspawner.description not in self.spawners_by_desc)
        self.spawners.append(scriptedspawner)
        self.spawners_by_desc[scriptedspawner.description] = scriptedspawner

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

        # Testing vars here -- looking at differences between my own data-driven DLC3+DLC4 adds
        # and the GBX ones added in Bloody Harvest 2020
        #with open('output.txt', 'a') as df:
        #    print(self.obj_name, file=df)
        #    print('-'*len(self.obj_name), file=df)
        #    print('', file=df)
        #    for s in self.spawners:
        #        print('Spawner: {}'.format(s.description), file=df)
        #        print('', file=df)
        #        for path in sorted(s.soft_paths):
        #            print("            '{}.{}',".format(path.SpawnerPathName.split('.')[-1], path.SpawnerSubPathString), file=df)
        #        print('', file=df)

        for exp in self.expansions:
            exp.generate_hotfixes(mod)

# Pull in extra spawners to apply events to
extra_spawners = []
base_dump_dir = '/home/pez/bl3_steam_root/OakGame/Binaries/Win64/data'
for cat_name, subdir, level_names in [
        # Eh, I couldn't get these to work.  The DLC3 ones seem to work fine, and the generated
        # structures seem right, but nothing gets ghostified (or whatever).  Just leaving them
        # out for now...
        #('Base Game', 'basegame', [
        #    ('Recruitment_P', set([
        #        'Recruitment_M_Ep01_ChildrenOfTheVault.PersistentLevel.OakMissionSpawner_Gatekeeper',
        #        'Recruitment_M_Ep01_ChildrenOfTheVault.PersistentLevel.OakMissionSpawner_Claptrap',
        #        'Recruitment_M_Ep02_Sacrifice.PersistentLevel.OakMissionSpawner_Lilith',
        #        ])),
        #    # Prologue_P *does* have some spawns set, but not many of 'em
        #    ('Prologue_P', set([
        #        'Prologue_M_Ep02_Sacrifice.PersistentLevel.OakMissionSpawner_Lilith',
        #        'Prologue_M_Ep02_Sacrifice.PersistentLevel.OakMissionSpawner_Vaughn',
        #        'Prologue_Dynamic.PersistentLevel.OakMissionSpawner_ClaptrapDynamic',
        #        'Prologue_Dynamic.PersistentLevel.OakMissionSpawner_Ellie',
        #        'Prologue_Dynamic.PersistentLevel.OakMissionSpawner_Tannis',
        #        ])),
        #    ]),

        # The majority of enemies in Negul Neshai don't seem to pick up Hearts or Cartels spawners,
        # though Ghosts work fine without.  Had tried adding in our own processing here, but it
        # didn't end up helping out at all (even though this code adds quite a few more spawners).
        #('DLC2', 'dlc2', [
        #    ('Camp_P', set([
        #        # Deathtrap
        #        'Camp_BossFight.PersistentLevel.OakMissionSpawner_DeathTrapPostMission',
        #        'Camp_Plot_M.PersistentLevel.OakMissionSpawner_Deathtrap',
        #        # Mancubus statue
        #        'Camp_Bunkers.PersistentLevel.OakMissionSpawner_Crew_Mancubus_Statue',
        #        # Chests / Crystals / Other Objects
        #        'Camp_Loot.PersistentLevel.EridianChests',
        #        'Camp_Loot.PersistentLevel.EridianCrystals',
        #        'Camp_Loot.PersistentLevel.OakMissionSpawner_PortalChest',
        #        'Camp_Side_M_ResearchCamp.PersistentLevel.OakMissionSpawner_IntoTheDeep_EchoLog',
        #        'Camp_Side_M_ResearchCamp.PersistentLevel.OakMissionSpawner_IntoTheDeep_FrozenEchoHolder',
        #        # Turret
        #        'Camp_Plot_M.PersistentLevel.SpawnOptions_Hib_DahlTurret_2',
        #        ])),
        #    ]),

        # Omitting DLC3 entirely since Bloody Harvest 2020 added them legitimately.  My code
        # here technically adds *more* spawners than BH2020 did, but probably the omissions
        # make sense.  Anyway, don't want to double up, so getting rid of it.
        #('DLC3', 'dlc3', [
        #    # Omitting CraterBoss_P
        #    ('Facility_P', set([
        #        # The husband+wife in The Dandy and Damsel
        #        'Facility_M_LoveBarNone.PersistentLevel.LoveBars_Husbando',
        #        'Facility_M_LoveBarNone.PersistentLevel.LoveBars_BossKeem',
        #        ])),
        #    ('Forest_P', set([
        #        # Oletta, probably
        #        'Forest_M_Ep03_Forest.PersistentLevel.OakMissionSpawner_Granny',
        #        # From Of Blood and Beans
        #        'Forest_M_BloodAndBeans.PersistentLevel.OakMissionSpawner_CowboyB',
        #        'Forest_M_BloodAndBeans.PersistentLevel.OakMissionSpawner_CowboyA',
        #        ])),
        #    ('Frontier_P', set([
        #        # Husband+wife in Miracle Elixir Fixer
        #        'Frontier_M_SnakeOil.PersistentLevel.OakMissionSpawner_Hina',
        #        'Frontier_M_SnakeOil.PersistentLevel.OakMissionSpawner_Eli',
        #        # Posse on way to final boss fight (I suspect the vehicles can't
        #        # get it anyway, but whatever)
        #        'Frontier_M_Ep05_CraterBoss.PersistentLevel.CraterBoss_TitusVehicle_1',
        #        'Frontier_M_Ep05_CraterBoss.PersistentLevel.CraterBoss_TitusVehicle',
        #        'Frontier_M_Ep05_CraterBoss.PersistentLevel.CraterBoss_Titus',
        #        'Frontier_M_Ep05_CraterBoss.PersistentLevel.CraterBoss_PosseMember_3',
        #        'Frontier_M_Ep05_CraterBoss.PersistentLevel.CraterBoss_DakotaVehicle_3',
        #        'Frontier_M_Ep05_CraterBoss.PersistentLevel.CraterBoss_DakotaVehicle_2',
        #        'Frontier_M_Ep05_CraterBoss.PersistentLevel.CraterBoss_DakotaVehicle',
        #        'Frontier_M_Ep05_CraterBoss.PersistentLevel.CraterBoss_Dakota',
        #        # Saurdew Valley NPCS (not sure about pygmies+predators)
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawnerCagedGrogs',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawnerCagedGrog_5',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawnerCagedGrog_4',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawnerCagedGrog_3',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawnerCagedGrog_1',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawner_RanchPet_1',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawner_RanchPet',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawner_RancherJan',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawner_Pygmies_1',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawner_Pygmies',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawner_Predators',
        #        'Frontier_M_SaurdewValley.PersistentLevel.OakMissionSpawner_Daisy',
        #        ])),
        #    ('Lodge_P', set([
        #        # Titus, maybe?
        #        'Lodge_M_Ep02_Bathhouse.PersistentLevel.OakMissionSpawner_Clay_2',
        #        'Lodge_M_Ep02_Bathhouse.PersistentLevel.OakMissionSpawner_Clay_1',
        #        # McSmugger
        #        'Lodge_M_TheLegendOfMcSmugger.PersistentLevel.McSmuggerSpawner',
        #        # Captive from Dirty Deeds, maybe?
        #        'Lodge_M_DirtyDeeds.OakMissionSpawner_SoapMaker',
        #        ])),
        #    ('Town_P', set([
        #        # Various NPCs
        #        'Town_M_WestLandIntro.PersistentLevel.OakMissionSpawner_Toge',
        #        'Town_M_WestLandIntro.PersistentLevel.OakMissionSpawner_Rose',
        #        'Town_M_NPC.PersistentLevel.OakMissionSpawner_Tanner',
        #        'Town_M_NPC.PersistentLevel.OakMissionSpawner_Mission1_FilmMaker',
        #        'Town_M_NPC.PersistentLevel.OakMissionSpawner_GenericTownsfolk__10',
        #        'Town_M_NPC.PersistentLevel.OakMissionSpawner_GenericTownsfolk__8',
        #        'Town_M_NPC.PersistentLevel.OakMissionSpawner_GenericTownsfolk__7',
        #        'Town_M_NPC.PersistentLevel.OakMissionSpawner_GenericTownsfolk__11',
        #        'Town_M_NPC.PersistentLevel.OakMissionSpawner_GenericTownsfolk_',
        #        'Town_M_NPC.PersistentLevel.BathhouseEp02_Wanderer',
        #        'Town_M_Dueling.OakMissionSpawner_4',
        #        'Town_M_Dueling.OakMissionSpawner_3',
        #        'Town_M_Dueling.OakMissionSpawner_1',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Yuko',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Yosuke',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Tarou',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Ori',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Micah',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Maiko',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Ko',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Josey',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Jinson',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Jerica',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Herb',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Gus',
        #        'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_Felice',
        #        # I've pruned some "obvious" attackers, but I suspect these might be, too
        #        #'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_Mission1_EggAttack',
        #        #'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_MarketGyros',
        #        #'Town_M_WestlandWelcome.PersistentLevel.OakMissionSpawner_2',
        #        'Town_M_WestlandWelcome.PersistentLevel.Mission1_YoungJed',
        #        'Town_M_WestlandWelcome.PersistentLevel.Mission1_Titus',
        #        'Town_M_WestlandWelcome.PersistentLevel.Mission1_Sheriff',
        #        'Town_M_WestlandWelcome.PersistentLevel.Mission1_OldPete',
        #        'Town_M_WestlandWelcome.PersistentLevel.Mission1_BulliedGuy_1',
        #        'Town_M_WestlandWelcome.PersistentLevel.Mission1_BulliedGuy',
        #        'Town_M_WestlandWelcome.PersistentLevel.Mission1_Bartender',
        #        'Town_M_WestlandWelcome.PersistentLevel.Mission1_BackTalker',
        #        'Town_Missions.PersistentLevel.Missions_Titus',
        #        'Town_Missions.PersistentLevel.Missions_Dakota',
        #        'Town_Missions.PersistentLevel.Mission_DirtyDeeds_Soapmaker',
        #        'Town_Missions.PersistentLevel.Mission_AnimalCTRL_BiobeastBetsyShock',
        #        'Town_Missions.PersistentLevel.Mission_AnimalCTRL_BiobeastBetsyRad',
        #        'Town_Missions.PersistentLevel.LoveBars_Husband',
        #        'Town_Missions.PersistentLevel.LoveBars_GrogReward',
        #        'Town_Missions.PersistentLevel.LoveBars_GrievingHusband',
        #        'Town_Missions.PersistentLevel.GhostStories_Preacher',
        #        'Town_Missions.PersistentLevel.GhostStories_CrazedMan',
        #        'Town_M_Ep05CraterBoss.PersistentLevel.Ep05Crater_PosseMember',
        #        'Town_M_Ep05CraterBoss.PersistentLevel.CraterBoss_RetreatingNPCs',
        #        'Town_M_Ep02_Bathhouse.PersistentLevel.Ep02Baths_FerrisTownsfolk',
        #        ])),
        #    ]),

        # Likewise, paring down DLC4 considerably, though in this case I'm keeping my own
        # Psychoscape and Vaulthalla additions, so that enemies in those areas can get
        # statuses.
        ('DLC4', 'dlc4', [
            ('Sanctum_P', set([
                # Friendly NPCs
                'Sanctum_MissionNPCs.PersistentLevel.OakMissionSpawner_ShadowMordecai',
                'Sanctum_MissionNPCs.PersistentLevel.OakMissionSpawner_ShadowBrick',
                'Sanctum_MissionNPCs.PersistentLevel.OakMissionSpawner_SaneKrieg',
                'Sanctum_MissionNPCs.PersistentLevel.OakMissionSpawner_Mordecai',
                'Sanctum_MissionNPCs.PersistentLevel.OakMissionSpawner_Maya',
                'Sanctum_MissionNPCs.PersistentLevel.OakMissionSpawner_MadKrieg',
                'Sanctum_MissionNPCs.PersistentLevel.OakMissionSpawner_Lilith',
                'Sanctum_MissionNPCs.PersistentLevel.OakMissionSpawner_Brick',
                ])),
            #('Anger_P', set([
            #    # P.A.T. and offspring
            #    'Anger_SM_AllShapesAndCalibers.PersistentLevel.OakMissionSpawner_PAT',
            #    'Anger_SM_AllShapesAndCalibers.PersistentLevel.OakMissionSpawner_BabyGun_5',
            #    # Krieg
            #    'Anger_BSM_GoodbyeOldFriend.PersistentLevel.OakMissionSpawner_SaneKrieg_GoodbyeOldFriend',
            #    'Anger_BSM_GoodbyeOldFriend.PersistentLevel.OakMissionSpawner_MadKrieg_GoodbyeOldFriend',
            #    'Anger_M_Plot.PersistentLevel.OakMissionSpawner_SaneKrieg',
            #    'Anger_M_Plot.PersistentLevel.OakMissionSpawner_MadKrieg',
            #    # Hot and Bothered NPCs
            #    'Anger_BSM_HotNBothered.PersistentLevel.OakMissionSpawner_HotNBothered_MissionGiver',
            #    'Anger_BSM_HotNBothered.PersistentLevel.OakMissionSpawner_HotNBothered',
            #    # Post-boss white dreamy zone
            #    'Anger_M_Plot.PersistentLevel.OakMissionSpawner_WhiteRoom_GhostMord',
            #    'Anger_M_Plot.PersistentLevel.OakMissionSpawner_WhiteRoom_GhostLilith',
            #    'Anger_M_Plot.PersistentLevel.OakMissionSpawner_WhiteRoom_GhostKrieg',
            #    'Anger_M_Plot.PersistentLevel.OakMissionSpawner_WhiteRoom_GhostBrick',
            #    # Containers
            #    'Anger_IO.PersistentLevel.OakSpawner_EridianCrystalSmall',
            #    'Anger_IO.PersistentLevel.OakSpawner_EridianCrystalChest',
            #    ])),
            #('Chase_P', set([
            #    # Interstitial Trains
            #    'Chase_Combat.PersistentLevel.OakMissionSpawner_TrainStation01_Train',
            #    'Chase_Combat.PersistentLevel.OakMissionSpawner_Station02_Trains',
            #    'Chase_Combat.PersistentLevel.OakMissionSpawner_Station01_Trains',
            #    'Chase_Combat.PersistentLevel.OakMissionSpawner_Mines02_Train_3',
            #    'Chase_Combat.PersistentLevel.OakMissionSpawner_Mines02_Train',
            #    'Chase_Combat.PersistentLevel.OakMissionSpawner_HangarTrains',
            #    'Chase_Combat.PersistentLevel.OakMissionSpawner_BridgeTrains',
            #    'Chase_M_Plot.PersistentLevel.Spawner_BridgeEnd_Trains',
            #    'Chase_M_Plot.PersistentLevel.Spawner_BridgeEnd_CrashingTrain',
            #    'Chase_Env_Station_01.PersistentLevel.OakMissionSpawner_StationJumps_Trains_0',
            #    'Chase_Env_Station_01.PersistentLevel.OakMissionSpawner_StationJumps_Trains',
            #    'Chase_Interactives.PersistentLevel.Spawner_Intro_Train_NoMission',
            #    # Caboose?  No idea.
            #    'Chase_M_Plot.PersistentLevel.OakMissionSpawner_Caboose',
            #    # NPCs/Krieg
            #    'Chase_M_Plot.PersistentLevel.OakMissionSpawner_Maya',
            #    'Chase_M_Plot.PersistentLevel.OakMissionSpawner_KriegSane',
            #    'Chase_M_Plot.PersistentLevel.OakMissionSpawner_KriegMad',
            #    'Chase_M_Plot.PersistentLevel.OakMissionSpawner_GhostMaya',
            #    'Chase_M_Plot.PersistentLevel.OakMissionSpawner_GhostKrieg_4',
            #    'Chase_SM_ChecksAndBalances.PersistentLevel.OakMissionSpawner_Thadeus',
            #    'Chase_SM_ChecksAndBalances.PersistentLevel.OakMissionSpawner_Maya_ChecksAndBalances_3',
            #    'Chase_SM_ChecksAndBalances.PersistentLevel.OakMissionSpawner_MK_ChecksAndBalances',
            #    'Chase_SM_ParadeHarpoon.PersistentLevel.OakMissionSpawner_SaneKriegHarpoon',
            #    'Chase_SM_ParadeHarpoon.PersistentLevel.OakMissionSpawner_Parade_Mad',
            #    'Chase_SM_WhenItRains.PersistentLevel.OakMissionSpawner_Rains_Mad',
            #    'Chase_SM_ThatRingsABell.PersistentLevel.OakMissionSpawner_RingABell_Sane',
            #    'Chase_SM_ThatRingsABell.PersistentLevel.OakMissionSpawner_RingABell_Mad',
            #    'Chase_SM_SpineTingler.PersistentLevel.OakMissionSpawner_SpineTingler_Sane',
            #    'Chase_SM_SpineTingler.PersistentLevel.OakMissionSpawner_SpineTingler_Mad',
            #    # Containers, etc
            #    'Chase_Interactives.PersistentLevel.OakSpawner_EridiumCrystals_Small',
            #    'Chase_Interactives.PersistentLevel.OakSpawner_EridiumCrystals_Medium',
            #    ])),
            #('Experiment_P', set([
            #    # Krieg
            #    'Experiment_SM_ExposureTherapy.PersistentLevel.OakMissionSpawner_SaneKrieg_Exposure',
            #    'Experiment_SM_ExposureTherapy.PersistentLevel.OakMissionSpawner_MadKrieg_Exposure',
            #    'Experiment_M_Plot.PersistentLevel.OakMissionSpawnerSaneKrieg',
            #    'Experiment_M_Plot.PersistentLevel.OakMissionSpawner_MadKrieg',
            #    # Containers
            #    'Experiment_Lootable.PersistentLevel.EridianCrystals_SecretCave',
            #    'Experiment_Lootable.PersistentLevel.EridianCrystals',
            #    'Experiment_Lootable.PersistentLevel.EridianChests',
            #    'Experiment_Lootable.PersistentLevel.EridianChest_SecretCave',
            #    ])),
            ('Eldorado_P', set([
                # Krieg
                'Eldorado_BossFight.PersistentLevel.SpawnOption_Ali_Krieg_Sane_BigAss',
                'Eldorado_BossFight.PersistentLevel.SpawnOption_Ali_Krieg_Sane_6',
                'Eldorado_BossFight.PersistentLevel.SpawnOption_Ali_Krieg_Mad_BigAss_6',
                'Eldorado_BossFight.PersistentLevel.SpawnOption_Ali_Krieg_Mad_2',
                'Eldorado_Plot_M.PersistentLevel.OakMissionSpawner_SaneKrieg',
                'Eldorado_Plot_M.PersistentLevel.OakMissionSpawner_MadKrieg',
                # Dreamy white room afterwards
                'Eldorado_Env_LootRoom.PersistentLevel.SpawnerWhiteSecondRoom',
                'Eldorado_Env_LootRoom.PersistentLevel.SpawnerWhiteFirstRoom',
                'Eldorado_Env_LootRoom.PersistentLevel.SpawnerRedSecondRoom',
                'Eldorado_Env_LootRoom.PersistentLevel.SpawnerRedFirstRoom',
                'Eldorado_Env_LootRoom.PersistentLevel.SpawnerWhiteChest',
                'Eldorado_Env_LootRoom.PersistentLevel.SpawnerRedChest',
                # Psychoreaver exclusions
                'Eldorado_BossFight.PersistentLevel.OakMissionSpawnerDummy',
                'Eldorado_BossFight.PersistentLevel.SpawnOptions_PsychodinP_2',
                ])),
            ]),
        ('DLC5', 'dlc5', [
            ('FrostSite_P', set([
                # Chests+stuff
                'FrostSite_Combat.PersistentLevel.TRASHPILES-LOOTDEN',
                'FrostSite_Combat.PersistentLevel.POIREDCHESTWATERWORKS',
                'FrostSite_Combat.PersistentLevel.POIREDCHESTTHUNDERDOME',
                'FrostSite_Combat.PersistentLevel.POIREDCHESTSPACEPORT',
                'FrostSite_Combat.PersistentLevel.POIREDCHESTSILO',
                'FrostSite_Combat.PersistentLevel.POIREDCHESTINDUSTRY',
                'FrostSite_Combat.PersistentLevel.POIREDCHESTHQ',
                'FrostSite_Combat.PersistentLevel.POIREDCHESTDAM',
                'FrostSite_Combat.PersistentLevel.POIREDCHESTCREATURESEWER',
                'FrostSite_Combat.PersistentLevel.OFFERINGBOX-LOOTDEN',
                'FrostSite_Combat.PersistentLevel.LOCKERS-LOOTDEN',
                'FrostSite_Combat.PersistentLevel.GLOBALWhiteChestDen-LOOTDEN',
                'FrostSite_Combat.PersistentLevel.GlobalWeaponVendingMachine',
                'FrostSite_Combat.PersistentLevel.GLOBALRedChestDen-LOOTDEN',
                'FrostSite_Combat.PersistentLevel.GlobalHealthVendingMachine',
                'FrostSite_Combat.PersistentLevel.GLOBALBARRELS-LootDen',
                'FrostSite_Combat.PersistentLevel.GlobalAmmoVendingMachine',
                'FrostSite_Combat.PersistentLevel.DAHLAMMOBOXES-LOOTDEN',
                'FrostSite_Combat.PersistentLevel.BONEPILES-LOOTDEN',
                'FrostSite_Mission.PersistentLevel.OakSpawner_StarterChest__5',
                'FrostSite_Mission.PersistentLevel.OakSpawner_StarterChest__4',
                'FrostSite_Mission.PersistentLevel.OakSpawner_StarterChest__3',
                'FrostSite_Mission.PersistentLevel.OakSpawner_StarterChest__2',
                'FrostSite_Mission.PersistentLevel.OakSpawner_StarterChest_',
                ])),
            ]),
        ('DLC6', 'dlc6', [
            ('SacrificeBoss_p', set([
                # Ammo Crates
                'SacrificeBoss_Combat.PersistentLevel.OakSpawner_AmmoCrates',
                # Maybe don't have Hemovorous itself be haunted or cartel...
                'SacrificeBoss_Combat.PersistentLevel.OakSpawner_RaidBoss',
                ])),
            ('Cabin_P', set([
                # Clay
                'Cabin_Mission.PersistentLevel.OakMissionSpawner_Clay',
                ])),
            ('Noir_P', set([
                # Friendly NPCs
                'Noir_Mission.PersistentLevel.OakMissionSpawner_Witness_2',
                'Noir_Mission.PersistentLevel.OakMissionSpawner_Witness',
                'Noir_Mission.PersistentLevel.OakMissionSpawner_Lorelai',
                'Noir_Mission.PersistentLevel.OakMissionSpawner_EntranceSoldierC',
                'Noir_Mission.PersistentLevel.OakMissionSpawner_EntranceSoldierB',
                'Noir_Mission.PersistentLevel.OakMissionSpawner_EntranceSoldierA',
                'Noir_Mission.PersistentLevel.OakMissionSpawner_BloodySoldier',
                'Noir_Mission.PersistentLevel.OakMissionSpawner_ApartmentSoldiers',
                # Chests
                'Noir_Combat.PersistentLevel.OakSpawner_EridiumCrystalsCHEST',
                'Noir_Combat.PersistentLevel.OakSpawner_EridiumCrystals',
                ])),
            ('PandoraMystery_p', set([
                # Body parts
                'PandoraMystery_Combat.PersistentLevel.OakMissionSpawner_SkagBodyPartsC_Loot',
                'PandoraMystery_Combat.PersistentLevel.OakMissionSpawner_SkagBodyPartsC',
                'PandoraMystery_Combat.PersistentLevel.OakMissionSpawner_SkagBodyPartsB_Loot',
                'PandoraMystery_Combat.PersistentLevel.OakMissionSpawner_SkagBodyPartsB',
                'PandoraMystery_Combat.PersistentLevel.OakMissionSpawner_SkagBodyPartA_Loot',
                'PandoraMystery_Combat.PersistentLevel.OakMissionSpawner_SkagBodyPartA',
                # Beef Plissken and related; I think the haunt/cartel thing would end up being weird
                # during the plotline.
                'PandoraMystery_Mission.PersistentLevel.OakMissionSpawner_Warchief',
                'PandoraMystery_Mission.PersistentLevel.OakMissionSpawner_RedeemerSpirit',
                # Claptrap
                'PandoraMystery_Mission.PersistentLevel.OakMissionSpawner_Claptrap',
                # Crystals + Chests
                'PandoraMystery_IO.PersistentLevel.EridianCrystals',
                'PandoraMystery_IO.PersistentLevel.EridianChests',
                ])),
            ('NekroMystery_p', set([
                # The Seer; might be a bit much
                'NekroMystery_Boss.PersistentLevel.OakMissionSpawner_Redeemer',
                # Crystals + Chests
                'NekroMystery_Gameplay.PersistentLevel.EridianCrystals',
                'NekroMystery_Gameplay.PersistentLevel.EridianChests',
                # Ava
                'NekroMystery_Mission.PersistentLevel.OakMissionSpawner_Ava',
                ])),
            ]),
        ]:
    for level_name, excluders in level_names:
        print('Processing extra spawns from {} {} ({})'.format(cat_name, LVL_TO_ENG[level_name], level_name))
        names_filename = os.path.join(base_dump_dir, subdir, level_name, 'UE4Tools_NamesDump.txt.xz')
        objects_filename = os.path.join(base_dump_dir, subdir, level_name, 'UE4Tools_ObjectsDump.txt.xz')
        extra_spawners.append(ScriptedSpawner.from_object_name_dumps(
            names_filename,
            objects_filename,
            'Apoc Addition - {} - {}'.format(
                cat_name,
                LVL_TO_ENG[level_name],
                ),
            excluders,
            ))

# Load in all the data from each of our SpawnDLC objects
spawndlcs = []
all_descs = set()
for _, _, exp_obj in expansion_objs:
    spawndlc = SpawnDLC(data, exp_obj)
    for spawner in extra_spawners:
        spawndlc.add_scriptedspawner(spawner)
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

    full_filename = 'expanded_event_spawners_{}.bl3hotfix'.format(filename)

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
                "and Covenant Pass won't have any, for instance.  This is up to date",
                "through DLC4 (Psycho Krieg), though.",
            ],
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.3.1',
            cats='event, enemy, maps',
            )

    spawndlc.generate_hotfixes(mod)

    mod.close()

