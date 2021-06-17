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
SEED=None # 42
CHUBBY=True # include the Chubby mod for Arm's Race
our_seed = SEED
version = '0.2.1'


def parse_args():
    parser = argparse.ArgumentParser(description=f'Boss Race Generator v{version}')
    parser.add_argument('--seed', type=int, default=SEED, help='Seed of random number generator.')
    parser.add_argument('--output', type=str, default=OUTPUT, help='Hotfix output file')
    parser.add_argument('--nochubby',action='store_true', default=False, help='Disable Chubby Mod')
    parser.add_argument('--bias',action='store_true', default=False, help='Bias Item Rarity against whites')
    parser.add_argument('--nogreen',action='store_true', default=False, help='Disable Green Chest')
    parser.add_argument('--mitosis',action='store_true', default=False, help='Enable Mitosis Harker')
    parser.add_argument('--justmitosis',action='store_true', default=False, help='Only generate Mitosis Mod')
    return parser.parse_args()

args = parse_args()
our_seed = args.seed
chubby_mod = not args.nochubby
bias_items = args.bias
green_chest = not args.nogreen
mitosis = args.mitosis
just_mitosis = args.justmitosis

title = 'Boss Race'
if just_mitosis:
    title = 'Mitosis Harker'

if our_seed is None:
    our_seed = random.randint(0,2**32-1)
else:
    our_seed = int(our_seed)

random.seed(our_seed)

DFL_LEVEL=Mod.EARLYLEVEL
output_filename = args.output
mod = Mod(output_filename,
          title,
          'skruntskrunt',
          ["Turns Arm's Race into a weird boss rush"],
          lic=Mod.CC_BY_SA_40,
          v=version,
          cats=['gameplay','armsrace'],
)

mod.comment(f"Seed {our_seed}")
EASY="easy"
MEDIUM="medium"
HARD="hard"

harker = "/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/BPChar_FrontRider_Mount"
# # crashed?
# harker_pool = [
#     ("Harker and Pet",'/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/BPChar_FrontRider_Mount',"/Ixora/Enemies/GearUpBoss/_Shared/Balance/Table_GearUpBoss_Balance","Rider_And_Mount"),
#     ("Harker","/Ixora/Enemies/GearUpBoss/Rider/_Design/Character/BPChar_FrontRider_Rider",None,None),
#     ("Harker Pet","/Ixora/Enemies/GearUpBoss/Pet/_Design/Character/BPChar_FrontRider_Pet",None,None),
#     ("Harker","/Ixora/Enemies/GearUpBoss/Rider/_Design/Character/BPChar_FrontRider_Rider",None,None),
#     ("Harker Pet","/Ixora/Enemies/GearUpBoss/Pet/_Design/Character/BPChar_FrontRider_Pet",None,None),
# ]
# 
# doesn't crash
harker_pool = [
    ("Harker and Pet",'/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/BPChar_FrontRider_Mount',"/Ixora/Enemies/GearUpBoss/_Shared/Balance/Table_GearUpBoss_Balance","Rider_And_Mount"),
    ("Harker and Pet",'/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/BPChar_FrontRider_Mount',"/Ixora/Enemies/GearUpBoss/_Shared/Balance/Table_GearUpBoss_Balance","Rider_And_Mount"),
    ("Harker and Pet",'/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/BPChar_FrontRider_Mount',"/Ixora/Enemies/GearUpBoss/_Shared/Balance/Table_GearUpBoss_Balance","Rider_And_Mount"),
]
# Works but he's sunken?
# harker_pool = [
#     ("Harker","/Ixora/Enemies/GearUpBoss/Rider/_Design/Character/BPChar_FrontRider_Rider",None,None),
#     ("Harker","/Ixora/Enemies/GearUpBoss/Rider/_Design/Character/BPChar_FrontRider_Rider",None,None),
#     ("Harker","/Ixora/Enemies/GearUpBoss/Rider/_Design/Character/BPChar_FrontRider_Rider",None,None),
# ]
# # Works fine
# harker_pool = [
#     ("Harker Pet","/Ixora/Enemies/GearUpBoss/Pet/_Design/Character/BPChar_FrontRider_Pet",None,None),
#     ("Harker Pet","/Ixora/Enemies/GearUpBoss/Pet/_Design/Character/BPChar_FrontRider_Pet",None,None),
#     ("Harker Pet","/Ixora/Enemies/GearUpBoss/Pet/_Design/Character/BPChar_FrontRider_Pet",None,None),
# ]
harker_pool = [
    #("Harker","/Ixora/Enemies/GearUpBoss/Rider/_Design/Character/BPChar_FrontRider_Rider",None,None),
    #("Harker","/Ixora/Enemies/GearUpBoss/Rider/_Design/Character/BPChar_FrontRider_Rider",None,None),
    #("Harker","/Ixora/Enemies/GearUpBoss/Rider/_Design/Character/BPChar_FrontRider_Rider",None,None),
    #("Harker Pet","/Ixora/Enemies/GearUpBoss/Pet/_Design/Character/BPChar_FrontRider_Pet",None,None),
    #("Harker Pet","/Ixora/Enemies/GearUpBoss/Pet/_Design/Character/BPChar_FrontRider_Pet",None,None),
    ("Harker Pet","/Ixora/Enemies/GearUpBoss/Pet/_Design/Character/BPChar_FrontRider_Pet",None,None),
    ("Harker and Pet",'/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/BPChar_FrontRider_Mount',"/Ixora/Enemies/GearUpBoss/_Shared/Balance/Table_GearUpBoss_Balance","Rider_And_Mount"),
]




difficulty_pools = {
    EASY:ixorabosses.easy_bosses,
    MEDIUM:ixorabosses.medium_bosses,
    HARD:ixorabosses.hard_bosses,
    "heavy":ixorabosses.heavy_bosses,
    "all":ixorabosses.safe_bosses,
    "harker":harker_pool,
}

# @piggy:~/projects/bl3data/extracted_new/frost-site/pp$ for file in `cat SpawnOptions`; do echo; bash json-of.sh $file | fgrep jwp_object_name | sed -e "s#^#'$file',#"; done | fgrep Factory | sed -e 's/"_jwp_object_name" : //'
harker_boss_adds = [
    # ('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "Factory_SpawnFactory_OakAI",0,["harker"]),
    ('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "SpawnFactory_OakAI_1",1,["harker"]),
    ('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "SpawnFactory_OakAI_2",2,["harker"]),
    ('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "SpawnFactory_OakAI_3",3,["harker"]),
]

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





def make_ixora_spawns(params,raw_ixora_spawn_list):
    done_so = set()
    for entry in raw_ixora_spawn_list:
        row,factory,idx,pools = entry
        so = row
        # 'Options.Options[{}].Factory.Object..AIActorClass'.format(rev(c,idx))
        pool = "all"
        if params.get("heavy",False):
            pool = "heavy"
        elif params.get("pool",False):
            pool = params["pool"]
        elif len(pools) > 0:
            pool = random.choice(pools)
        mod.comment(f"From Pool: {pool}")
        mob = random.choice(difficulty_pools[pool])
        bpchar = mob[BPCHAR]
        mod.comment(f"so:{row} factory:{factory}")
        mod.comment(f"bpchar:{bpchar}")
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

def modify_spawnpoints(params):
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

def bias_item_rarity():
    # we can't guarantee initial chest but we can bias against it
    GEARUP = "/Game/PatchDLC/Ixora/GameData/Balance/Table_GearUp_ItemRarity_Standard"
    WHITE  = "Common"
    GREEN  =  "Uncommon"
    BLUE   = "Rare"
    PURPLE = "VeryRare"
    ORANGE = "Legendary"
    BASEWEIGHT = "BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191"
    mod.comment("This is stolen from Poïpoï's Legendary Arm's race CC-BY-SA 4.0 ")
    mod.comment("at https://github.com/BLCM/bl3mods/blob/master/Po%C3%AFpo%C3%AF/Legendary%20Arms%20Race.bl3hotfix")
    mod.table_hotfix(DFL_LEVEL, IXORA_MAP, GEARUP, WHITE ,BASEWEIGHT,   1)   # 30
    mod.table_hotfix(DFL_LEVEL, IXORA_MAP, GEARUP, GREEN ,BASEWEIGHT, 749)   # 50
    mod.table_hotfix(DFL_LEVEL, IXORA_MAP, GEARUP, BLUE  ,BASEWEIGHT, 200)   # 15
    mod.table_hotfix(DFL_LEVEL, IXORA_MAP, GEARUP, PURPLE,BASEWEIGHT,  40)   #  4
    mod.table_hotfix(DFL_LEVEL, IXORA_MAP, GEARUP, ORANGE,BASEWEIGHT,  10)   #  1

def change_chest_rarity(change_key=False):
    # Ok now we manipulate the itempools instead
    valuename = "BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191"
    # 1% chance here
    valuevalue = "Legendary"
    pistol_equippable = "/Game/PatchDLC/Ixora/GameData/Loot/ItemPools/Chest/ItemPool_GearUp_Chest_PS_Equippable"
    pistol_key =  "BalancedItems.BalancedItems[0].ItemPoolData"
    pistol_key2 = "BalancedItems.BalancedItems[0].Weight.DataTableValue"
    pistol_v2 = "None"
    # Could use this
    '(DataTable=None,RowName="",ValueName="")'
    # could us this for weight instead
    '(BaseValueConstant=0,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=0)'
    uc_pistols = "/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Uncommon"
    itempool_pistols = f"ItemPoolData'\"{uc_pistols}\"'"
    mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, pistol_equippable, pistol_key, itempool_pistols)
    smg_equippable = "/Game/PatchDLC/Ixora/GameData/Loot/ItemPools/Chest/ItemPool_GearUp_Chest_AR_SG_SMG_Equippable"
    smg_key = pistol_key
    smg_key2 = pistol_key2
    smg_v2 = "None"
    uc_smg = "/Game/GameData/Loot/ItemPools/Guns/ItemPool_AR_Shotgun_SMG_Uncommon"
    itempool_smg = f"ItemPoolData'\"{uc_smg}\"'"
    mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, smg_equippable, smg_key, itempool_smg)
    shield_equippable = "/Game/PatchDLC/Ixora/GameData/Loot/ItemPools/Chest/ItemPool_GearUp_Chest_Shields_Equippable"
    shield_key = pistol_key
    shield_key2 = smg_key2
    shield_v2 = smg_v2
    uc_shield = "/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_02_Uncommon"
    itempool_shield = f"ItemPoolData'\"{uc_shield}\"'"    
    mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, shield_equippable, shield_key, itempool_shield)
    if change_key:
        mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, smg_equippable, smg_key2, smg_v2)
        mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, pistol_equippable, pistol_key2, pistol_v2)
        mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, shield_equippable, shield_key2, shield_v2)

def gen_mitosis_harker(params):
    mparams = params.copy()
    mparams["pool"] = "harker"
    mod.comment("And now for mitosis harker")
    make_ixora_spawns(mparams, harker_boss_adds)

def gen_boss_race(params, raw_ixora_spawn_list):
    make_ixora_spawns(params, raw_ixora_spawn_list)
    
    if mitosis:
        gen_mitosis_harker(params)
    
    if params.get("modify_spawnpoints",False):
        modify_spawnpoints(params)
    
    if chubby_mod:
        mod.raw_line(open("ixorachubby.bl3hotfix.txt").read())
    
    if bias_items:
        bias_item_rarity()
    
    if green_chest:
        change_chest_rarity()
    
if just_mitosis:
    gen_mitosis_harker(params)    
else:
    gen_boss_race(params, raw_ixora_spawn_list)

mod.close()

# TODOS
# - Current test is the pit to see if the trial boss spawns
# - [X] Starting Chest Better?
# - [ ] Big Mobs not moving in the pit
# - [ ] Tiers of Big Guys
# Thoughts:
# - Pit is called ThunderDome, the spawn points are not detailed
# Maybe we need to address SpawnerComponent and deal with style?
# Big bosses have problems spawning
# Even gigamind?
# Flyers have problems spawning there's some aspect of spawn points
# Traunt would spawn and attack but staying in the same spot and not doing damage
