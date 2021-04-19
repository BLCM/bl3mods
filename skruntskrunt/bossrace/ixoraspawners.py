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
OUTPUT='bossrace.bl3hotfix'
BPCHAR=1
IXORA_MAP = 'FrostSite_P'
SEED=None#42
our_seed = SEED
if our_seed is None:
    our_seed = random.randint(0,2**32-1)
random.seed(our_seed)

mod = Mod(OUTPUT,
          'Boss Race',
          'skruntskrunt',
          ["Turns Arm's Race into a weird boss rush"],
          lic=Mod.CC_BY_SA_40,
          v='0.1.0',
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
params = {
    "extend":(119,119,119),
    'collision':'AdjustIfPossibleButAlwaysSpawn',
    "UseActorProperties":"False",# maybe coop doesn't see it
    'SpawnOrigin':f'(X={1500},Y={0},Z={100})',
    'heavy':False,
    'modify_spawnpoints':True,
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
                       #f'{row}.{factory}',
                       #f'{factory}.AIActorClass',
                       #'AIActorClass',
                       f'Options.Options[{idx}].Factory.Object..AIActorClass',
                       f"BlueprintGeneratedClass'{bpchar}.{get_bpchar(bpchar)}_C'",
        )
        # extend = (70,70,119)
        # extend = (250,250,250)
        extend = params["extend"]
        scale = 1.0
        if not so in done_so:
            mod.reg_hotfix(Mod.LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..SpawnExtent'.format(idx),
                       f'(X={scale * float(extend[0])},Y={scale * float(extend[1])},Z={scale * float(extend[2])})')
            mod.reg_hotfix(Mod.LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..SpawnExtent'.format(idx),
                       f'(x={scale * float(extend[0])},y={scale * float(extend[1])},z={scale * float(extend[2])})')
            mod.reg_hotfix(Mod.LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..UINameOverride'.format(idx),
                       'None')
            mod.reg_hotfix(Mod.LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..SpawnOrigin'.format(idx),
                        #f'(X={1500},Y={0},Z={0})')# what if we change to X to 0 from 1500
                        # was 1500 1500 1500
                        #f'(X={1500},Y={0},Z={0})')# what if we change to X to 0 from 1500
                        params["SpawnOrigin"])
            # We used AlwaysSpawn and it didn't necessarily work
            mod.reg_hotfix(Mod.LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..CollisionHandling'.format(idx),
                       params["collision"])
                       #'AdjustIfPossibleButAlwaysSpawn')
                       #'AlwaysSpawn')
            #"CollisionHandling" : "ESpawnActorCollisionHandlingMethod::AdjustIfPossibleButAlwaysSpawn",
            mod.reg_hotfix(Mod.LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..bOverrideCollisionHandling'.format(idx),
                       'True')
            mod.reg_hotfix(Mod.LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..ItemPoolToDropOnDeathAdditive'.format(idx),
                       'True')
            # should this be true or false?
            # False was what we were using
            mod.reg_hotfix(Mod.LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..bUseActorProperties'.format(idx),
                           params["UseActorProperties"])
            mod.reg_hotfix(Mod.LEVEL, IXORA_MAP, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..SpawnDetails'.format(idx),
                       '(Critical=AlwaysSpawn)')
            mod.reg_hotfix(Mod.EARLYLEVEL, IXORA_MAP, '{}:{}'.format(Mod.get_full(so),bpchar), 'TeamOverride', Mod.get_full_cond('/Game/Common/_Design/Teams/Team_Maliwan', 'Team'))
    
            #      "bUseActorProperties" : true,
            #      "ItemPoolToDropOnDeathAdditive" : false,
    
    
            # Might have to override more... especially loot and names
        done_so.add(so)

def modify_spawnpoints():
    spawnpoints = json.load(open('spawnpoints.json'))
    pp_ixora_path = f"/Ixora/Maps/FrostSite/FrostSite_Combat.FrostSite_Combat:PersistentLevel"
    #for (prefix,n) in [('OakSpawnPoint',784),('SpawnMesh_DoorSmall',363)]:
    #    for i in range(0,n):
    for sp in spawnpoints:
        #sp = f"{prefix}_{i}"
        for (obj,val) in [('SpawnAction','None'),
                          ('bFilterByTag','False'), # was None
                          ('FilterMatchType','None'),
                          ('Tags','None')]:
            mod.reg_hotfix(
                Mod.EARLYLEVEL, IXORA_MAP,
                f"{pp_ixora_path}.{sp}.SpawnPointComponent",
                obj,
                val,'',True)

make_ixora_spawns()
# modify_spawnpoints()
            
mod.close()

# TODOS
# - Current test is the pit to see if the trial boss spawns
# - [ ] Big Mobs not moving in the pit
# - [ ] Tiers of Big Guys
# Thoughts:
# - Pit is called ThunderDome, the spawn points are not detailed
# Maybe we need to address SpawnerComponent and deal with style?
# Big bosses have problems spawning
# Even gigamind?
# Flyers have problems spawning there's some aspect of spawn points
# Traunt would spawn and attack but staying in the same spot and not doing damage
