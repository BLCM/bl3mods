#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Boss Race Generator
# Copyright (C) 2021 abram/skruntksrunt, altef-4, Christopher J. Kucera
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import json
import sys
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod
import random
sys.path.append('../boss-rush-slaughter')
import boss
import ixorabosses
import argparse

OUTPUT='bossrace.bl3hotfix'
BPCHAR=1
IXORA_MAP = 'FrostSite_P'
SEED=None#42
CHUBBY=True # include the Chubby mod for Arm's Race
our_seed = SEED

def parse_args():
    parser = argparse.ArgumentParser(description='Boss Race Generator')
    parser.add_argument('--seed', type=int, default=SEED, help='Seed of random number generator.')
    parser.add_argument('--output', type=str, default=OUTPUT, help='Hotfix output file')
    parser.add_argument('--nochubby',action='store_true', default=False, help='Disable Chubby Mod')
    return parser.parse_args()

args = parse_args()
our_seed = args.seed
chubby_mod = not args.nochubby

if our_seed is None:
    our_seed = random.randint(0,2**32-1)
else:
    our_seed = int(our_seed)

random.seed(our_seed)

DFL_LEVEL=Mod.EARLYLEVEL
output_filename = args.output
mod = Mod(output_filename,
          'Boss Race',
          'skruntskrunt',
          ["Turns Arm's Race into a weird boss rush"],
          lic=Mod.CC_BY_SA_40,
          v='0.1.2',
          cats='gameplay',
)

mod.comment(f"Seed {our_seed}")
EASY="easy"
MEDIUM="medium"
HARD="hard"

difficulty_pools = {
    EASY:ixorabosses.easy_bosses,
    MEDIUM:ixorabosses.medium_bosses,
    HARD:ixorabosses.hard_bosses,
    "heavy":ixorabosses.heavy_bosses,
    "all":ixorabosses.safe_bosses,
}

# @piggy:~/projects/bl3data/extracted_new/frost-site/pp$ for file in `cat SpawnOptions`; do echo; bash json-of.sh $file | fgrep jwp_object_name | sed -e "s#^#'$file',#"; done | fgrep Factory | sed -e 's/"_jwp_object_name" : //'
raw_ixora_spawn_list = [
    #('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "Factory_SpawnFactory_OakAI",0),
    #('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "SpawnFactory_OakAI_1",1),
    #('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "SpawnFactory_OakAI_2",2),
    #('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "SpawnFactory_OakAI_3",3),
    #('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/CotV/Tink/SpawnOptions_MaliTinkSuicide_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY]),
    ('/Ixora/Enemies/_Spawning/CotV/Psycho/SpawnOptions_PsychoBadass_GearUp',      "SpawnFactory_OakAI_0",0,[EASY]),
    ('/Ixora/Enemies/_Spawning/CotV/Psycho/SpawnOptions_MaliPsychoBasic_GearUp',      "SpawnFactory_OakAI_0",0,[EASY]),
    ('/Ixora/Enemies/_Spawning/CotV/Punk/SpawnOptions_PunkBasic_GearUp',      "SpawnFactory_OakAI_0",0,[EASY,MEDIUM]),
    ('/Ixora/Enemies/_Spawning/CotV/Punk/SpawnOptions_PunkBadass_GearUp',      "SpawnFactory_OakAI_0",0,[MEDIUM,HARD]),
    ('/Ixora/Enemies/_Spawning/CotV/Punk/SpawnOptions_PunkSniper_GearUp',      "SpawnFactory_OakAI_0",0,[EASY,MEDIUM]),
    ('/Ixora/Enemies/_Spawning/CotV/Punk/SpawnOptions_PunkShotgunner_GearUp',      "SpawnFactory_OakAI_0",0,[MEDIUM]),
    ('/Ixora/Enemies/_Spawning/CotV/Punk/SpawnOptions_PunkAssaulter_GearUp',      "SpawnFactory_OakAI_0",0,[MEDIUM]),
    ('/Ixora/Enemies/_Spawning/CotV/Enforcer/SpawnOptions_MaliEnforcerGun_GearUp',      "Factory_SpawnFactory_OakAI",0,[MEDIUM,HARD]),
    # ('/Ixora/Enemies/_Spawning/CotV/Enforcer/SpawnOptions_Enforcer_Reaper',      "Factory_SpawnFactory_OakAI"), # disable replacement of revenants
    ('/Ixora/Enemies/_Spawning/Maliwan/Frontrunner/SpawnOptions_Frontrunner_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY,MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Frontrunner/SpawnOptions_Nullhound_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY,MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Frontrunner/SpawnOptions_Gunwolf_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Frontrunner/SpawnOptions_CoVFrontrunner_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY,MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperJetpack_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperShotgun_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY,MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperFlash_GearUp',      "Factory_SpawnFactory_OakAI",0,[MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperMelee_Random_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY,MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperBasic_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY,MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_CoVTrooper_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY,MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperMedic_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperBadass_GearUp',      "Factory_SpawnFactory_OakAI",0,[MEDIUM,HARD]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Nog/SpawnOptions_NogNinja_GearUp',      "SpawnFactory_OakAI_0",0,[EASY]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Nog/SpawnOptions_NogBasic_GearUp',      "SpawnFactory_OakAI_0",0,[EASY]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Oversphere/SpawnOptions_CoVOversphere_GearUp',      "Factory_SpawnFactory_OakAI",0,[EASY]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyBasic_GearUp',      "Factory_SpawnFactory_OakAI",0,[MEDIUM,HARD]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyAcidrain_GearUp',      "Factory_SpawnFactory_OakAI",0,[MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyGunner_GearUp',      "Factory_SpawnFactory_OakAI",0,[MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyPowerhouse_GearUp',      "Factory_SpawnFactory_OakAI",0,[MEDIUM,HARD]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyBadass_Random_GearUp',      "Factory_SpawnFactory_OakAI",0,[MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyBadass_Random_GearUp',      "SpawnFactory_OakAI_0",1,[MEDIUM]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyBadass_Random_GearUp',      "SpawnFactory_OakAI_1",2,[MEDIUM,HARD]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyBadass_Random_GearUp',      "SpawnFactory_OakAI_2",3,[HARD]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_CoVHeavy_GearUp',      "Factory_SpawnFactory_OakAI",0,[MEDIUM,HARD]),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyIcebreaker_GearUp',      "Factory_SpawnFactory_OakAI",0,[MEDIUM,HARD]),
    #('/Ixora/Enemies/_Spawning/Skags/SpawnOptions_SkagBadass',      "SpawnFactory_OakAI_0"),
    #('/Ixora/Enemies/_Spawning/Skags/SpawnOptions_SkagAdultsAndBarfers',      "SpawnFactory_OakAI_0"),
    #('/Ixora/Enemies/_Spawning/Skags/SpawnOptions_SkagAdultsAndBarfers',      "SpawnFactory_OakAI_2"),
    #('/Ixora/Enemies/GearUpBoss/Pet/_Design/Character/SpawnOptions_FrontRider_Pet',      "Factory_SpawnFactory_OakAI"),
    #('/Ixora/Enemies/GearUpBoss/Rider/_Design/Character/SpawnOptions_FrontRider_Rider',      "Factory_SpawnFactory_OakAI"),
    #('/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/SpawnOptions_FrontRider_Mount',      "Factory_SpawnFactory_OakAI"),
]
ixora_spawnoptions = dict()
for entry in  raw_ixora_spawn_list:
    row,factory = entry[0:2]
    l = ixora_spawnoptions.get(row,list())
    l.append(factory)
    ixora_spawnoptions[row]=l

def get_bpchar(s):
    return s.split('/')[-1]

## Doesn't work on heavies in pit
# params = {
#     "extend":(70,70,119),
#     "collision":'AlwaysSpawn',
#     "UseActorProperties":"True",
#     'bosses':ixorabosses.heavy_bosses,
# }
## Doesn't spawn heavies in pit after first round
# params = {
#     "extend":(70,70,119),
#     # "collision":'AlwaysSpawn',
#     "collision":'AdjustIfPossibleButDontSpawnIfColliding',
#     "UseActorProperties":"True",
#     'bosses':ixorabosses.heavy_bosses,
# }
# 
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"True",# maybe coop doesn't see it
#     'bosses':ixorabosses.safe_bosses,
# }
# # no movement of pit spawns
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",# maybe coop doesn't see it
#     'bosses':ixorabosses.heavy_bosses,
#     'SpawnOrigin':f'(X={1500},Y={0},Z={100})',
# }
# # no bugs but no big baddies
#params = {
#    "extend":(119,119,119),
#    'collision':'AdjustIfPossibleButAlwaysSpawn',
#    "UseActorProperties":"False",# maybe coop doesn't see it
#    'bosses':ixorabosses.safe_bosses,
#    'SpawnOrigin':f'(X={1500},Y={0},Z={100})',
#}
# 1. crash?
# 2. still the lock problem :(
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",# maybe coop doesn't see it
#     'SpawnOrigin':f'(X={1500},Y={0},Z={100})',
#     'heavy':True,
# }
# # someone didn't spawn??
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",# maybe coop doesn't see it
#     'SpawnOrigin':f'(X={1500},Y={0},Z={100})',
#     'heavy':False,
#     'modify_spawnpoints':True,
# }
# # spawn issues?
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",# maybe coop doesn't see it
#     'SpawnOrigin':f'(X={1500},Y={0},Z={100})',
#     'heavy':False,
#     'modify_spawnpoints':False,
# }
#
# # some failed spawns?
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",# maybe coop doesn't see it
#     'SpawnOrigin':f'(X={1500},Y={0},Z={100})',
#     'heavy':False,
#     'modify_spawnpoints':False,
# }
# # sane
#params = {
#    "extend":(119,119,119),
#    'collision':'AdjustIfPossibleButAlwaysSpawn',
#    "UseActorProperties":"False",# maybe coop doesn't see it
#    'SpawnOrigin':f'(X={1500},Y={0},Z={100})',
#    'heavy':False,
#    'modify_spawnpoints':True,
#}
# # still didn't work on heavies
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",# maybe coop doesn't see it
#     'SpawnOrigin':f'(X={1500},Y={0},Z={100})',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
# # 
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",# maybe coop doesn't see it
#     'SpawnOrigin':f'(X={1500},Y={0},Z={100})',
#     'heavy':False,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
# Play with spawn origin
# # DID NOT SPAWN WELL
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"True",
#     'SpawnOrigin':f'(X={0},Y={0},Z={0})',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
# COOP ISSUES
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"True",
#     'SpawnOrigin':f'(X={1000},Y={100},Z={100})',
#     'heavy':False,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }

# 
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':f'(X={1000},Y={100},Z={100})',
#     'heavy':False,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
# # a little weird
# params = {
#     "extend":(119,119,119),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':f'(X={1500},Y={100},Z={100})',
#     'heavy':False,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
#
# # Traunt moved but sigdriftia did not.?
# params = {
#     "extend":(160,160,160),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':f'(X={1500},Y={100},Z={100})',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
# # Sigdriftia spawns but doesn't move
# params = {
#     "extend":(180,180,180),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':f'(X={1500},Y={100},Z={100})',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
# # They fall through the map, traunt doesn't though
# params = {
#     "extend":(180,180,180),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':f'(X={1500},Y={1500},Z={1500})',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
#
# Nothing spawns
# params = {
#     "extend":(180,180,180),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':f'(X=0,Y=0,Z=-100)',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
# # Some spawning issues
# params = {
#     "extend":(180,180,180),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':f'(X=1500,Y=0,Z=-100)',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
# # Trying none? No spawn
# params = {
#     "extend":(180,180,180),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':'None',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
# # # No spawn
# params = {
#     "extend":(180,180,180),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':f'(X=1500,Y=0,Z=100)',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":False,
#     'modify_spawnpoints':False,
# }
# # # mod spawn but no special?
# params = {
#     "extend":(180,180,180),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':f'(X=1500,Y=0,Z=100)',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":False,
#     'modify_spawnpoints':True,
# }
# # All true? & Z=200 it didn't spawn
# params = {
#     "extend":(180,180,180),
#     'collision':'AdjustIfPossibleButAlwaysSpawn',
#     "UseActorProperties":"False",
#     'SpawnOrigin':f'(X=1500,Y=0,Z=200)',
#     'heavy':True,
#     "SpawnDetails":True,
#     "SpecialEffects":True,
#     'modify_spawnpoints':True,
# }
# # ?? well the heavies do spawn :/ but sigdrifia just rotates :(
# params = {
#      "extend":(99,99,180),
#      'collision':'AdjustIfPossibleButAlwaysSpawn',
#      "UseActorProperties":"False",
#      'SpawnOrigin':f'(X={1000},Y={100},Z={100})',
#      'heavy':True,
#      "SpawnDetails":True,
#      "SpecialEffects":True,
#      'modify_spawnpoints':True,
# }
# # Works OK v0.1.2 was this
params = {
     "extend":(99,99,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1000},Y={100},Z={100})',
     'heavy':False,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
}
# billy the annointed got stuck
params = {
     "extend":(99,99,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1000},Y={100},Z={100})',
     'heavy':False,
     "SpawnDetails":True,
     "SpecialEffects":False,
     'modify_spawnpoints':False,
}
# billy worked? No. Not in the pit
params = {
     "extend":(99,99,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1000},Y={0},Z={180})',
     'heavy':False,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
}
# Disabled Billy
params = {
     "extend":(99,99,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1000},Y={0},Z={180})',
     'heavy':False,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
}
# added navcollisionsize
# removed lowercase SpawnExtent
# didn't spawn in pit?
params = {
     "extend":(99,99,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1000},Y={0},Z={180})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# Y to 180
# Switch to 80,80,80 NavCollision
# sigdriftia spawns but doesn't move
params = {
     "extend":(99,99,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1500},Y={180},Z={180})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=80,Y=80,Z=80)',
}
# added NavBox.BoxExtent
# Rota stands still
params = {
     "extend":(99,99,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1500},Y={180},Z={180})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=80,Y=80,Z=80)',
}
# 180 NavCollisionSize
# spawn no move :(
params = {
     "extend":(99,99,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1500},Y={180},Z={180})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# 180 extend
params = {
     "extend":(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1500},Y={180},Z={180})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# just always spawn
# rota doesn't move in WTF
params = {
     "extend":(180,180,180),
     'collision':'AlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1500},Y={180},Z={180})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# Just overdo it
# nope still no movement
params = {
     "extend":(1800,1800,1800),
     'collision':'AlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1800},Y={1800},Z={1800})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=1800,Y=1800,Z=1800)',
}
# Nuke it?
# Rota doesn't move
params = {
     "extend":'None',#(180,180,180),
     'collision':'AlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':'None',#f'(X={1800},Y={1800},Z={1800})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'None',#(X=1800,Y=1800,Z=1800)',
}
# ok add Adjust
# no still no movement spawns
params = {
     "extend":'None',#(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':'None',#f'(X={1800},Y={1800},Z={1800})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'None',#(X=1800,Y=1800,Z=1800)',
}
# 200 extend
# sigdrifia doesn't move
params = {
     "extend":(200,200,200),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':'None',#f'(X={1800},Y={1800},Z={1800})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'None',#(X=1800,Y=1800,Z=1800)',
}
# tesitng this now

# navbox fix?
# some sunk into the ground
params = {
     "extend":(150,150,150),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1500},Y={0},Z={180})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# Nothing spawns
params = {
     "extend":(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1500},Y={1500},Z={1500})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# Don't touch y Z is still 1500
params = {
     "extend":(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1500},Y={0},Z={1500})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# make spawn og X bigger
# they all fell down in WTF
params = {
     "extend":(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={2500},Y={0},Z={500})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# interesting...
# spawn don't move but fall down
params = {
     "extend":(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={2500},Y={0},Z={-500})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# 0 out X
# spawn no move
params = {
     "extend":(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={0},Y={0},Z={-500})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# try -500 X
# spawn no move fall
params = {
     "extend":(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={-500},Y={0},Z={-500})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# OK try use actor properties
# spawn no move fall :(
params = {
     "extend":(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"True",
     'SpawnOrigin':f'(X={-500},Y={-500},Z={-500})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
}
# Hmmm last successful play
params = {
     "extend":(99,99,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1000},Y={0},Z={180})',
     'heavy':False,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':True,
}
# heavy test with IrrelevantAction
# didn't move
params = {
     "extend":(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1000},Y={0},Z={-500})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
     'IrrelevantAction':True,     
}
# Now with critical
# Respawn
params = {
     "extend":(180,180,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1000},Y={0},Z={-500})',
     'heavy':True,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':'(X=180,Y=180,Z=180)',
     'IrrelevantAction':True,
     'Critical':'Critical',
     'RespawnStyle':True,
}
# works
params = {
     "extend":(99,99,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1000},Y={0},Z={180})',
     'heavy':False,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':True,
}





def make_ixora_spawns():
    done_so = set()
    for entry in raw_ixora_spawn_list:
        row,factory,idx,pools = entry
        so = row
        # 'Options.Options[{}].Factory.Object..AIActorClass'.format(rev(c,idx))
        pool = "all"
        if params["heavy"]:
            pool = "heavy"
        elif len(pools) > 0:
            pool = random.choice(pools)
        mod.comment(f"From Pool: {pool}")
        mob = random.choice(difficulty_pools[pool])
        bpchar = mob[BPCHAR]
        mod.comment(f"so:{row} factory:{factory} bpchar:{bpchar}")
        mod.reg_hotfix(Mod.EARLYLEVEL,
                       IXORA_MAP,
                       row,
                       f'Options.Options[{idx}].Factory.Object..AIActorClass',
                       f"BlueprintGeneratedClass'{bpchar}.{get_bpchar(bpchar)}_C'",
        )
        extend = params["extend"]
        scale = 1.0
        if not so in done_so:
            if not extend == 'None':
                mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
                               'Options.Options[{}].Factory.Object..SpawnExtent'.format(idx),
                               f'(X={scale * float(extend[0])},Y={scale * float(extend[1])},Z={scale * float(extend[2])})')
            else:
                mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
                               'Options.Options[{}].Factory.Object..SpawnExtent'.format(idx),
                               'None')

            #mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
            #           'Options.Options[{}].Factory.Object..SpawnExtent'.format(idx),
            #           f'(x={scale * float(extend[0])},y={scale * float(extend[1])},z={scale * float(extend[2])})')
            mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..UINameOverride'.format(idx),
                       'None')
            mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..SpawnOrigin'.format(idx),
                        params["SpawnOrigin"])
            # We used AlwaysSpawn and it didn't necessarily work
            mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..CollisionHandling'.format(idx),
                       params["collision"])
            mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..bOverrideCollisionHandling'.format(idx),
                       'True')
            mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..ItemPoolToDropOnDeathAdditive'.format(idx),
                       'True')
            mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..bUseActorProperties'.format(idx),
                           params["UseActorProperties"])
            # respawn_style=""
            # if params.get("RespawnStyle"
            # respawn_style=",{params.get("Critical","AlwaysSpawn")}
            if params.get("IrrelevantAction",False):
                action = params.get("IrrelevantAction")
                if action == True:
                    action = "Nothing"
                mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..SpawnDetails'.format(idx),
                       f'(Critical={params.get("Critical","AlwaysSpawn")},bOverrideCritical=True,IrrelevantAction={action},bOverrideIrrelevantAction=True)')
            else:
                mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..SpawnDetails'.format(idx),
                       '(Critical=AlwaysSpawn,bOverrideCritical=True)') # added this
            mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, '{}:{}'.format(Mod.get_full(so),bpchar), 'TeamOverride', Mod.get_full_cond('/Game/Common/_Design/Teams/Team_Maliwan', 'Team'))
    
        done_so.add(so)


# Maybe we should on SpawnerComponent
#      "SpawnDetails" : {
#         "Critical" : "ESpawnerCritical::AlwaysSpawn",
#         "bOverrideCritical" : true
#      },

#              "SpawnDetails" : {
#         "RespawnStyle" : "ERespawnStyle::Never",
#         "Critical" : "ESpawnerCritical::Critical",
#         "bOverrideRespawnStyle" : true,
#         "bOverrideCritical" : true
#      },

def modify_spawnpoints():
    spawnpoints = json.load(open('spawnpoints.json'))
    pp_ixora_path = f"/Ixora/Maps/FrostSite/FrostSite_Combat.FrostSite_Combat:PersistentLevel"
    objvals =  [('SpawnAction','None'),
                ('bFilterByTag','False'), # was None
                ('FilterMatchType','None'),
                ('Tags','None')]
    if params["SpecialEffects"]:
        objvals.append(('SpecialEffect','None'))
    if params.get("NavCollisionSize",False):
        v = params["NavCollisionSize"]
        if v == True:
            v = '(X=80.0,Y=80.0,Z=80.0)'
        objvals.append(('NavCollisionSize',v))
        objvals.append(('NavBox.Object..BoxExtent',v))
    for sp in spawnpoints:
        for (obj,val) in objvals:
            mod.reg_hotfix(
                Mod.EARLYLEVEL, IXORA_MAP,
                f"{pp_ixora_path}.{sp}.SpawnPointComponent",
                obj,
                val,'',True)
        # danger!!!
        if params.get("SpawnDetails",False):
            details = {'Critical':params.get("Critical","AlwaysSpawn"),
                       'bOverrideCritical':'True'}
            if params.get("IrrelevantAction",False):
                details["IrrelevantAction"] = 'Nothing'
                details["bOverrideIrrelevantAction"] = 'True'
            spdetails = ",".join([f'{x}={details[x]}' for x in details])
            for (obj,val) in [('SpawnDetails',spdetails)]:
                mod.reg_hotfix(
                    Mod.EARLYLEVEL, IXORA_MAP,
                    f"{pp_ixora_path}.{sp}.SpawnerComponent",
                    obj,
                    val,'',True)


            
make_ixora_spawns()
if params.get("modify_spawnpoints",False):
    modify_spawnpoints()

if chubby_mod:
    mod.raw_line(open("ixorachubby.bl3hotfix.txt").read())

mod.close()

# TODOS
# - Current test is the pit to see if the trial boss spawns
# - [ ] Starting Chest Better?
# - [ ] Big Mobs not moving in the pit
# - [ ] Tiers of Big Guys
# Thoughts:
# - Pit is called ThunderDome, the spawn points are not detailed
# Maybe we need to address SpawnerComponent and deal with style?
# Big bosses have problems spawning
# Even gigamind?
# Flyers have problems spawning there's some aspect of spawn points
# Traunt would spawn and attack but staying in the same spot and not doing damage
