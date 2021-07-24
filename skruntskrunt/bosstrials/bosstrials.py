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
BPCHAR=1
SEED=None # 42
our_seed = SEED
version = '0.1.0'

EASY="easy"
MEDIUM="medium"
HARD="hard"

LEVELS = sorted(["ProvingGrounds_Trial8_P","ProvingGrounds_Trial7_P","ProvingGrounds_Trial6_P","ProvingGrounds_Trial5_P","ProvingGrounds_Trial4_P","ProvingGrounds_Trial1_P"])
MISSION_NUMBERS=[1,4,5,6,7,8]

# Default__ProvingGrounds_Trial{trial}_Dynamic_C

def trial_path(trial):
    #return (f'/Game/Maps/ProvingGrounds/Trial{trial}/ProvingGrounds_Trial{trial}_Dynamic.Default__ProvingGrounds_Trial{trial}_Dynamic_C', f'ProvingGrounds_Trial{trial}_P')
    return (f'/Game/Maps/ProvingGrounds/Trial{trial}/ProvingGrounds_Trial{trial}_Dynamic.ProvingGrounds_Trial{trial}_Dynamic', f'ProvingGrounds_Trial{trial}_P')
    # return (f'/Game/Maps/ProvingGrounds/Trial{trial}/ProvingGrounds_Trial{trial}_P.ProvingGrounds_Trial{trial}_P', f'ProvingGrounds_Trial{trial}_P')

def parse_args():
    parser = argparse.ArgumentParser(description=f'Boss Trial Generator v{version}')
    parser.add_argument('--seed', type=int, default=SEED, help='Seed of random number generator.')
    parser.add_argument('--input', type=str, default='trial1.json',help='Trial Input JSON')
    parser.add_argument('--output', type=str, default=OUTPUT, help='Hotfix output file')
    parser.add_argument('--trial', type=int, default=1, help='Trial number {MISSION_NUMBERS}')
    return parser.parse_args()

args = parse_args()
our_seed = args.seed

title = 'Boss Trials'
# we abuse ixora to fill in the trials?
raw_ixora_spawn_list = [
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

raw_ixora_spawn_list = [
    ("/Game/Enemies/_Spawning/Varkids/Variants/SpawnOptions_VarkidLarva", "SpawnFactory_OakAI_0", 0, [EASY]),
    ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI", 0, [EASY]),
    ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_0", 1, [EASY]),
    ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_1", 2, [EASY]),
    ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_2", 3, [EASY]),
    ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_3", 4, [EASY]),
    ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_4", 5, [EASY]),
    ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_5", 6, [EASY]),
    ("/Game/Enemies/_Spawning/Spiderants/_Mixes/SpawnMix_SpiderantAll", "SpawnFactory_OakAI_6", 7, [EASY]),
    ("/Game/Enemies/_Spawning/Spiderants/Variants/SpawnOptions_SpiderantBasic", "SpawnFactory_OakAI", 0, [EASY]),
]

if our_seed is None:
    our_seed = random.randint(0,2**32-1)
else:
    our_seed = int(our_seed)

random.seed(our_seed)
DFL_LEVEL=Mod.EARLYLEVEL
# DFL_LEVEL=Mod.LEVEL
output_filename = args.output
mod = Mod(output_filename,
          title,
          'skruntskrunt',
          ["Turns Trials into a weird boss rush"],
          lic=Mod.CC_BY_SA_40,
          v=version,
          cats=['gameplay'],
)
mod.comment(f"Seed {our_seed}")

difficulty_pools = {
    EASY:ixorabosses.easy_bosses,
    MEDIUM:ixorabosses.medium_bosses,
    HARD:ixorabosses.hard_bosses,
    "heavy":ixorabosses.heavy_bosses,
    "all":ixorabosses.safe_bosses,
    "any":ixorabosses.easy_bosses + ixorabosses.medium_bosses + ixorabosses.hard_bosses,
}

def get_bpchar(s):
    return s.split('/')[-1]

def make_ixora_spawns(mod, mapcode, raw_ixora_spawn_list, params):
    done_so = set()
    for entry in raw_ixora_spawn_list:
        row,factory,idx,pools = entry
        so = row
        # 'Options.Options[{}].Factory.Object..AIActorClass'.format(rev(c,idx))
        pool = "any"
        if len(pools) > 0:
            pool = random.choice(pools)
        mod.comment(f"From Pool: {pool}")
        mob = random.choice(difficulty_pools[pool])
        bpchar = mob[BPCHAR]
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

facts = json.load(open(args.input))
spawnpoints = facts["spawnpoints"]
spawnoption_facts = facts["spawnoptions"]
spawn_list = mk_spawn_list( spawnoption_facts )
# make_ixora_spawns( mod, level, raw_ixora_spawn_list, params )
make_ixora_spawns( mod, level, spawn_list, params )

modify_spawnpoints( mod, path, level, params, spawnpoints )


# ./hotfixes_current.json:      "value": "(1,1,0,GuardianTakedown_P),/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_88.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den,SpawnOptions,167,SpawnOptionData'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown/MapSpecificAssets/SpawnOptions_Guardian_Possessed_FullMixTD2.SpawnOptions_Guardian_Possessed_FullMixTD2',SpawnOptionData'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown/MapSpecificAssets/SpawnOptions_Guardian_FullMix_TD2.SpawnOptions_Guardian_FullMix_TD2'"
# ./hotfixes_current.json:      "value": "(1,1,0,GuardianTakedown_P),/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_96.SpawnerComponent.SpawnerStyle_Encounter_3,Waves.Waves[0].Advancement.Percent,8,0.300000,.66"

def reassign_spawnoptions(mod,spawnoption_facts):
    mod.comment("Reassigning SpawnOptions")
    for fact in spawnoption_facts:
        option = list(fact[SPAWNOPTIONS].keys())[0]
        val    = fact[SPAWNOPTIONS][option]
        spawn_option  = random.choice(raw_ixora_spawn_list)[0]
        # options = option.split('.Waves.')
        # SpawnerComponent hacks
        options = option.split('.SpawnerComponent.')
        head = ".".join(options[:len(options)-1]) + ".SpawnerComponent"
        tail = "SpawnerComponent." + options[-1]
        # spawn_option = "/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_PsychoMix_DesertVault"
        # spawn_option = "/Game/Enemies/_Spawning/Varkids/Variants/SpawnOptions_VarkidLarva"    
        # this works:
        # SparkLevelPatchEntry,(1,1,0,ProvingGrounds_Trial1_P),/Game/Maps/ProvingGrounds/Trial1/ProvingGrounds_Trial1_Dynamic.ProvingGrounds_Trial1_Dynamic:PersistentLevel.OakSpawner_E1C.SpawnerComponent,SpawnerComponent.SpawnerStyle.Waves.Waves[0].SpawnerStyle.SpawnOptions,0,,SpawnOptionData'/Game/Enemies/_Spawning/Varkids/Variants/SpawnOptions_VarkidLarva.SpawnOptions_VarkidLarva'
        # EarlyLevel worked, but it didn't let us change the mobs?w
        mod.reg_hotfix(DFL_LEVEL,                   
                       level,
                       f'{path}:PersistentLevel.{head}',
                       # f'{path}:{head}',
                       f'{tail}',
                       f"SpawnOptionData'{spawn_option}.{get_bpchar(spawn_option)}'"
        )

# spawnoption_facts = facts["spawnoptions"]
# reassign_spawnoptions(mod,spawnoption_facts)

        
mod.close()

# we're not going to get anywhere until we loosen up the spawn restrictions

# Notes
# It doesn't really like us changing the spawnoptiondata.
# I did manage to get billy to spawn instead of spiderants
