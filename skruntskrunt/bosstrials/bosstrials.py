#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Trial Fact Extractor for BL3
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
sys.path.append('../bossrace')
import boss
import ixorabosses
import argparse


OUTPUT='bosstrials.bl3hotfix'
SPAWNOUT='spawnoptions.output.json'
BPCHAR=1
SEED=None # 42
our_seed = SEED
version = '0.1.2'

EASY="easy"
MEDIUM="medium"
HARD="hard"

LEVELS = sorted(["ProvingGrounds_Trial8_P","ProvingGrounds_Trial7_P","ProvingGrounds_Trial6_P","ProvingGrounds_Trial5_P","ProvingGrounds_Trial4_P","ProvingGrounds_Trial1_P"])
MISSION_NUMBERS=[1,4,5,6,7,8]
INSTINCT="Instinct"
FERVOR="Fervor"
CUNNING="Cunning"
SUPREMACY="Supremacy"
DISCIPLINE="Discipline"
SURVIVAL="Survival"
TITLES = {
    1:SURVIVAL,
    "ProvingGrounds_Trial1_P":SURVIVAL,
    4:FERVOR,
    "ProvingGrounds_Trial4_P":FERVOR,
    5:CUNNING,
    "ProvingGrounds_Trial5_P":CUNNING,
    6:SUPREMACY,
    "ProvingGrounds_Trial6_P":SUPREMACY,
    7:DISCIPLINE,
    "ProvingGrounds_Trial7_P":DISCIPLINE,
    8:INSTINCT,
    "ProvingGrounds_Trial8_P":INSTINCT,
}

# These spawn options cause a lot of trouble so we ignore them
ignore_list = [
    ('ProvingGrounds_Trial1_P','/Game/Enemies/_Spawning/Skags/_Mixes/SpawnOptions_SkagFullMix'), # solves it on most seeds
    ('ProvingGrounds_Trial6_P',"/Game/Enemies/_Spawning/Maliwan/Troopers/Variants/SpawnOptions_TrooperBasicDark"),
    ('ProvingGrounds_Trial7_P','/Game/Enemies/_Spawning/ProvingGrounds/Trial7/SpawnOptions_PGTrial7_Maliwan_OversphereMix'),
]

# Default__ProvingGrounds_Trial{trial}_Dynamic_C

def trial_path(trial):
    #return (f'/Game/Maps/ProvingGrounds/Trial{trial}/ProvingGrounds_Trial{trial}_Dynamic.Default__ProvingGrounds_Trial{trial}_Dynamic_C', f'ProvingGrounds_Trial{trial}_P')
    return (f'/Game/Maps/ProvingGrounds/Trial{trial}/ProvingGrounds_Trial{trial}_Dynamic.ProvingGrounds_Trial{trial}_Dynamic', f'ProvingGrounds_Trial{trial}_P')
    # return (f'/Game/Maps/ProvingGrounds/Trial{trial}/ProvingGrounds_Trial{trial}_P.ProvingGrounds_Trial{trial}_P', f'ProvingGrounds_Trial{trial}_P')

def parse_args():
    parser = argparse.ArgumentParser(description=f'Boss Trial Generator v{version}')
    parser.add_argument('--seed', type=int, default=SEED, help='Seed of random number generator.')
    parser.add_argument('--input', type=str, default='trial1.json',help='Trial Input JSON')
    parser.add_argument('--spawnoptions', type=str, default='spawnoptions.1.json',help='Spawn Options for the Trial')
    parser.add_argument('--overridespawn', action='store_true',help='Use the spawnoptions json to override spawn choices')
    parser.add_argument('--output', type=str, default=OUTPUT, help='Hotfix output file')
    parser.add_argument('--spawnout',type=str, default=SPAWNOUT, help='SpawnOptions output file')
    parser.add_argument('--trial', type=int, default=1, help='Trial number {MISSION_NUMBERS}')
    return parser.parse_args()

args = parse_args()
our_seed = args.seed

if our_seed is None:
    our_seed = random.randint(0,2**32-1)
else:
    our_seed = int(our_seed)

our_trial = args.trial
title = f'Boss Trials: {TITLES[our_trial]} seed {our_seed}'
# we abuse ixora to fill in the trials?

# raw_ixora_spawn_list = [
#     ("/Game/Enemies/_Spawning/Varkids/Variants/SpawnOptions_VarkidLarva", "SpawnFactory_OakAI_0", 0, [EASY]),
#     ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI", 0, [EASY]),
#     ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_0", 1, [EASY]),
#     ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_1", 2, [EASY]),
#     ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_2", 3, [EASY]),
#     ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_3", 4, [EASY]),
#     ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_4", 5, [EASY]),
#     ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_5", 6, [EASY]),
#     ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_6", 7, [EASY]),
#     ("/Game/Enemies/_Spawning/Spiderants/Variants/SpawnOptions_SpiderantBasic", "SpawnFactory_OakAI", 0, [EASY]),
# ]
# 

random.seed(our_seed)
DFL_LEVEL=Mod.EARLYLEVEL
# DFL_LEVEL=Mod.LEVEL
output_filename = args.output
spawnoptions_filename = args.spawnoptions
mod = Mod(output_filename,
          title,
          'skruntskrunt',
          ["Turns Proving Grounds Trials into a weird boss rush trials."],
          lic=Mod.CC_BY_SA_40,
          v=version,
          cats=['trials','gameplay'],
)
mod.comment(f"Seed {our_seed}")
mod.comment(f"Trial {our_trial}")

debug_pool = """M /Game/PatchDLC/Event2/Enemies/Cyber/Trooper/Capo/_Design/Character/BPChar_CyberTrooperCapo"""


difficulty_pools = {
    EASY:ixorabosses.easy_bosses,
    MEDIUM:ixorabosses.medium_bosses,
    HARD:ixorabosses.hard_bosses,
    "heavy":ixorabosses.heavy_bosses,
    "all":ixorabosses.safe_bosses,
    "any":ixorabosses.easy_bosses + ixorabosses.medium_bosses + ixorabosses.hard_bosses,
    "debug":[ixorabosses.tuple_line_to_bpchar(x) for x in debug_pool.split("\n")]
}

def get_bpchar(s):
    return s.split('/')[-1]

def mk_mob_tuple(bpchar_name):
    bpchar = bpchar_name.split(".")[0]
    return (bpchar,bpchar,None,None)

def make_ixora_spawns(mod, mapcode, raw_ixora_spawn_list, params, ignore_list=ignore_list):
    done_so = set()
    outentries = []
    for entry in raw_ixora_spawn_list:
        row,factory,idx,pools = entry[0:4]
        so = row
        # 'Options.Options[{}].Factory.Object..AIActorClass'.format(rev(c,idx))
        pool = "any"
        # look this is a dumb override
        # essentially if our entry is large and then override it
        if len(entry) > 4:
            mob_name = entry[4]
            mod.comment(f"Override with: {mob_name}")
            mob = mk_mob_tuple(mob_name)
        else:
            if len(pools) > 0:
                pool = random.choice(pools)
            mod.comment(f"From Pool: {pool}")
            mob = random.choice(difficulty_pools[pool])            
        bpchar = mob[BPCHAR]
        # we want to save out the raw_ixora_spawn_list
        outentry = [None,None,None,None]
        outentry[0:4] = entry[0:4]
        outentry[3] = mob[BPCHAR]
        print(outentry)
        outentries.append(outentry)
        # we ignore after the random choice
        # to maintain our seeds better        
        if (mapcode,row) in ignore_list:
            print(mapcode,row)
            mod.comment(f"Ignoring: so:{row} factory:{factory}")
            mod.comment(f"Ignoring: bpchar:{bpchar}")
            continue
        mod.comment(f"so:{row} factory:{factory}")
        mod.comment(f"bpchar:{bpchar}")
        mod.reg_hotfix(DFL_LEVEL,
                       mapcode,
                       row,
                       f'Options.Options[{idx}].Factory.Object..AIActorClass',
                       f"BlueprintGeneratedClass'{bpchar}.{get_bpchar(bpchar)}_C'",
        )
        # nope team didn't help
        # mod.reg_hotfix(Mod.EARLYLEVEL,
        #                mapcode,
        #                row,
        #                f'Options.Options[{idx}].Factory.Object..CachedTeam',
        #                mod.get_full_cond(f"/Game/Common/_Design/Teams/Team_Maliwan",'Team')
        # )

        extend = params["extend"]
        scale = 1.0
        # return# disable this stuff
        if not so in done_so:
            if not extend == 'None':
                mod.reg_hotfix(DFL_LEVEL, mapcode, Mod.get_full(so),
                               'Options.Options[{}].Factory.Object..SpawnExtent'.format(idx),
                               f'(X={scale * float(extend[0])},Y={scale * float(extend[1])},Z={scale * float(extend[2])})')
            else:
                mod.reg_hotfix(DFL_LEVEL, mapcode, Mod.get_full(so),
                               'Options.Options[{}].Factory.Object..SpawnExtent'.format(idx),
                               'None')
            mod.reg_hotfix(DFL_LEVEL, mapcode, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..UINameOverride'.format(idx),
                       'None')
            mod.reg_hotfix(DFL_LEVEL, mapcode, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..SpawnOrigin'.format(idx),
                        params["SpawnOrigin"])
            # We used AlwaysSpawn and it didn't necessarily work
            mod.reg_hotfix(DFL_LEVEL, mapcode, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..CollisionHandling'.format(idx),
                       params["collision"])
            mod.reg_hotfix(DFL_LEVEL, mapcode, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..bOverrideCollisionHandling'.format(idx),
                       'True')
            mod.reg_hotfix(DFL_LEVEL, mapcode, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..ItemPoolToDropOnDeathAdditive'.format(idx),
                       'True')
            mod.reg_hotfix(DFL_LEVEL, mapcode, Mod.get_full(so),
                       'Options.Options[{}].Factory.Object..bUseActorProperties'.format(idx),
                           params["UseActorProperties"])
            # # Disabled This stuff
            # if params.get("IrrelevantAction",False):
            #     action = params.get("IrrelevantAction")
            #     if action == True:
            #         action = "Nothing"
            #     mod.reg_hotfix(DFL_LEVEL, mapcode, Mod.get_full(so),
            #            'Options.Options[{}].Factory.Object..SpawnDetails'.format(idx),
            #            f'(Critical={params.get("Critical","AlwaysSpawn")},bOverrideCritical=True,IrrelevantAction={action},bOverrideIrrelevantAction=True)')
            # else:
            #     mod.reg_hotfix(DFL_LEVEL, mapcode, Mod.get_full(so),
            #            'Options.Options[{}].Factory.Object..SpawnDetails'.format(idx),
            #            '(Critical=AlwaysSpawn,bOverrideCritical=True)') # added this
            # perhaps team was the issue?
            # mod.reg_hotfix(DFL_LEVEL, mapcode, '{}:{}'.format(Mod.get_full(so),bpchar), 'TeamOverride', Mod.get_full_cond('/Game/Common/_Design/Teams/Team_Maliwan', 'Team'))    
        done_so.add(so)
    return outentries

def modify_spawnpoints(mod, path, level, params,spawpoints):
    # path = f"/Ixora/Maps/FrostSite/FrostSite_Combat.FrostSite_Combat:PersistentLevel"
    path = f'{path}:PersistentLevel'
    mod.comment(f"Modifying SpawnPoints for {path}")
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
                DFL_LEVEL, level,
                f"{path}.{sp}.SpawnPointComponent",
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
                    DFL_LEVEL, level,
                    f"{path}.{sp}.SpawnerComponent",
                    obj,
                    val,'',True)



OAKMISSIONSPAWNER="OakMissionSpawner"
EXPORT_TYPE="export_type"
SPAWNERCOMPONENT="SpawnerComponent"
SPAWNERSTYLE="SpawnerStyle"
SPAWNOPTIONS="SpawnOptions"
WAVES="Waves"
NUMACTORS="NumActorsParam"
ATTRINIT="AttributeInitializationData"
BASEVALUECONSTANT="BaseValueConstant"

path,level = trial_path( args.trial )

params = {
     "extend":(150,150,180),
     'collision':'AdjustIfPossibleButAlwaysSpawn',
     "UseActorProperties":"False",
     'SpawnOrigin':f'(X={1000},Y={0},Z={180})',
     'heavy':False,
     "SpawnDetails":True,
     "SpecialEffects":True,
     'modify_spawnpoints':True,
     'NavCollisionSize':True,
}

def mk_spawn_list(spawnoption_facts,n=8):
    sp = set()
    choices = ['heavy']#[EASY,MEDIUM,HARD]
    for fact in spawnoption_facts:
        option = list(fact[SPAWNOPTIONS].keys())[0]
        val    = fact[SPAWNOPTIONS][option]
        sp.add(val)
    out = []
    for x in sp:
        for i in range(n):
            out.append( (x,None,i,[random.choice(choices)]) )
    return out

def load_so(filename,choices=None):
    if choices is None:
        # choices = ["debug"]#[EASY,MEDIUM,HARD]
        choices = [EASY,MEDIUM,HARD]
    arr = json.load(open(filename))
    return [(x[0],x[1],x[2],[random.choice(choices)]) for x in arr]

def load_so_override(filename):
    arr = json.load(open(filename))
    return [(x[0],x[1],x[2],[],x[3]) for x in arr]
    

facts = json.load(open(args.input))
spawnpoints = facts["spawnpoints"]
spawnoption_facts = facts["spawnoptions"]
# spawn_list = mk_spawn_list( spawnoption_facts )

if args.overridespawn:
    spawn_list = load_so_override( spawnoptions_filename )
else:
    spawn_list = load_so( spawnoptions_filename )

spawn_out = make_ixora_spawns( mod, level, spawn_list, params )
if args.spawnout:
    json.dump(spawn_out, open(args.spawnout,"w"), indent=1)

modify_spawnpoints( mod, path, level, params, spawnpoints )

        
mod.close()

# we're not going to get anywhere until we loosen up the spawn restrictions

# Notes
# It doesn't really like us changing the spawnoptiondata.
# I did manage to get billy to spawn instead of spiderants
# ...
# Theory: by properly assigning single spawns we can probably
#         spawn everyone safely
#         We'll need each spawnoption
# ... we're kinda stuck, maybe skags or rakks?
# ... varkid or skags, something with their spawns..

