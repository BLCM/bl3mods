#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Boss Rush 3000 Slaughter Generator
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
import argparse
import sys
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod
import random
import math
SEED=42

def parse_args():
    parser = argparse.ArgumentParser(description='Boss Rush 3000 Slaughter Generator')
    parser.add_argument('--seed', type=int, default=SEED, help='Seed of random number generator.')
    parser.add_argument('--time', action='store_true', default=False, help='Use time for a seed')
    return parser.parse_args()

args = parse_args()
our_seed = int(args.seed)
if not args.time:
    random.seed(our_seed)

mod = Mod('3000_simple.bl3hotfix',
          '3000 Boss Rush slaughter: Billy and the Clone-a-saurus',
          'altef_4 feat. SkruntSkrunt',
          ['turns maliwan slaughter star 3000',
           'into a boss rush slaughter'],
          lic=Mod.CC_BY_SA_40,
          v='0.9',
          cats='gameplay',
)

mod.comment( f'Seed for this generation: {our_seed}' )

# from gen_3000_Char_list import *
# from gen_3000_helper_functions import *
from decimal import Decimal
import boss

#additional or multiply health/dmg scalling, false = (src_health|src_dmg) + (base_hs|base_ds), true = (src_health|src_dmg) * (base_hs|base_ds)
health_dmg_multiply = False
health_dmg_with_log = False
#health scalling
base_hs = 6
#damage scalling
base_ds = 0.8



#size mod
size_mod = True
#mob size
size = 1
#boss size
boss_size = '1.5,3.75'.split(',')
#mob speed
mob_speed = 1.5

HM = ['HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
    'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',
    'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113',
    'DamageMultiplier_LevelBased_23_3CAF34804D650A98AB8FAFAB37CB87FF']


ready_list = []
mesh_list = []
mission = []
move_list = []
item_pool_list = []


revert_enum = False
def rev(cnt, idx):
    if revert_enum:
        return cnt - idx - 1
    else:
        return idx

def enemy_type(etype):
    return {
        'Normal': "'/Game/GameData/ZoneMap/POI_Types/POI_CrewChallengeEnemy.POI_CrewChallengeEnemy'",
        'None': "'/Game/GameData/ZoneMap/POI_Types/POI_Enemy.POI_Enemy'",
        'VeryGood': "'/Game/GameData/ZoneMap/POI_Types/POI_CrewChallengeEnemy.POI_CrewChallengeEnemy'",
        'Badass': "'/Game/GameData/ZoneMap/POI_Types/POI_CrewChallengeEnemy.POI_CrewChallengeEnemy'",
        'SuperBadass': "'/Game/GameData/ZoneMap/POI_Types/POI_Boss.POI_Boss'",
        'UltimateBadass': "'/Game/GameData/ZoneMap/POI_Types/POI_Boss.POI_Boss'",
    }.get(etype,'!ERR_etype.{}'.format(etype))
def enemy_icon(etype):
    return {
        'None': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/MinimapIcon_Enemy.MinimapIcon_Enemy'",
        'Normal': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/MinimapIcon_Pinging_Hostile.MinimapIcon_Pinging_Hostile'",
        'VeryGood': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/crewIcon_Hunt.crewIcon_Hunt'",
        'Badass': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/MinimapIcon_MiniBoss.MinimapIcon_MiniBoss'",
        'SuperBadass': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/MinimapIcon_Boss.MinimapIcon_Boss'",
        'UltimateBadass': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/MinimapIcon_Boss.MinimapIcon_Boss'",
    }.get(etype,'!ERR_etype.{}'.format(etype))
    
def enemy_legendaries(etype):
    return {
        'None': 1,
        'Normal': 2,
        'VeryGood': 3,
        'Badass': 6,
        'SuperBadass': 10,
        'UltimateBadass': 15,
    }.get(etype,'!ERR_etype.{}'.format(etype))

def get_bpchar(s):
    return s.split('/')[-1]

def print_and_comment(s):
    print(s)
    mod.comment(s)

healh_chance = 52
def gen_mod(so, scale, list):
    c = len(list)
    global healh_chance
    healh_chance -= 1
    for idx, val in enumerate(list):
        if (isinstance(val[0],tuple)):
            # this means we're using (name,bpchar,balance,balancerow,extras)
            print_and_comment(f'Deploying {val[0][0]}')
            # new tuple of bpchar and prior spawn factory
            val = (val[0][1],val[1])
        else:
            print_and_comment(f'Deploying {val[0]}')            
        if val == 'empty':
            continue
        var = val
        obj = var[1].replace("_C'","")
        print(var,obj,val)
        mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P', Mod.get_full(so), 'Options.Options[{}].Factory.Object..AIActorClass'.format(rev(c,idx)), "BlueprintGeneratedClass'{}.{}_C'".format(var[0],get_bpchar(var[0])))
        if obj not in ready_list:
            ready_list.append(obj)
            bpchar = var[0].replace("BlueprintGeneratedClass'","")
            last_bit = bpchar.split('/')[-1]
            # extend = eval(val+"(1)").replace('(x=','').replace('y=','').replace('z=','').replace(')','').split(',')
            # should extent be looked up from a table?
            extend = (70,70,119)
            scale = 1.0
            mod.reg_hotfix(Mod.LEVEL, 'TechSlaughter_P', Mod.get_full(so),
                'Options.Options[{}].Factory.Object..SpawnExtent'.format(rev(c,idx)),
                f'(X={scale * float(extend[0])},Y={scale * float(extend[1])},Z={scale * float(extend[2])})')
            mod.reg_hotfix(Mod.LEVEL, 'TechSlaughter_P', Mod.get_full(so),
                'Options.Options[{}].Factory.Object..SpawnOrigin'.format(rev(c,idx)),
                f'(X={1500},Y={0},Z={0})')
            mod.reg_hotfix(Mod.LEVEL, 'TechSlaughter_P', Mod.get_full(so),
                'Options.Options[{}].Factory.Object..CollisionHandling'.format(rev(c,idx)),
                'AlwaysSpawn')
            mod.reg_hotfix(Mod.LEVEL, 'TechSlaughter_P', Mod.get_full(so),
                'Options.Options[{}].Factory.Object..bOverrideCollisionHandling'.format(rev(c,idx)),
                'True')
            mod.reg_hotfix(Mod.LEVEL, 'TechSlaughter_P', Mod.get_full(so),
                'Options.Options[{}].Factory.Object..SpawnDetails'.format(rev(c,idx)),
                '(Critical=AlwaysSpawn)')
            
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P', '{}:{}'.format(Mod.get_full(so),val[1]), 'TeamOverride', Mod.get_full_cond('/Game/Common/_Design/Teams/Team_Maliwan', 'Team'))


# "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderEXP_JUNK.BPChar_LoaderEXP_JUNK_C'",
            

# gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_1/SpawnOptions_KatagawaBallAdds_MeleeMix',
#         size,[
#             ("/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderEXP_JUNK",
#              "Factory_SpawnFactory_OakAI"), # ??
#             ("/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderEXP_JUNK",
#              "Factory_SpawnFactory_OakAI_1"),
#             ("/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderEXP_JUNK",
#              "Factory_SpawnFactory_OakAI_2"),
#             ("/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderEXP_JUNK",
#              "Factory_SpawnFactory_OakAI_3"),
#             ("/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderEXP_JUNK",
#              "Factory_SpawnFactory_OakAI_4"),
#             ("/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderEXP_JUNK",
#              "Factory_SpawnFactory_OakAI_5"),
#         ])

def replace_enemy(l):
    return [(boss.choose_random_slaughter_boss(),x[1]) for x in l]

def round1():

    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_1/SpawnOptions_KatagawaBallAdds_MeleeMix',
            size,replace_enemy([
                ("/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/BPChar_Enforcer_Bounty01", "Factory_SpawnFactory_OakAI"), # ??
                ("/Game/Enemies/ServiceBot/LOOT/_Design/Character/BPChar_ServiceBot_LOOT","Factory_SpawnFactory_OakAI_1"),
                ("/Game/Enemies/Skag/_Unique/Buttmunch/_Design/Character/BPChar_SkagButtmunch","Factory_SpawnFactory_OakAI_2"),
                ("/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue","Factory_SpawnFactory_OakAI_3"),
                ("/Game/Enemies/Heavy/_Unique/FootstepsOfGiants/_Design/Character/BPChar_HeavyFootstepsOfGiants","Factory_SpawnFactory_OakAI_4"),
                ("/Game/Enemies/Nog/_Unique/Beans/_Design/Character/BPChar_NogBeans","Factory_SpawnFactory_OakAI_5"),
            ]))


    #wave 1a
    # Junk loader is the test enemy that we know works
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1a_Trooper1',
             size,[
                 ("/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderBasicJUNK","SpawnFactory_OakAI_2")
             ])
    
    # After this point everything is random
    #wave 1b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1b_TrooperBscShtGn',
        size,replace_enemy([
            ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_2")
        ]))
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2a_Trooper',
        size,replace_enemy([
            ("BPChar_TrooperBadass_C_FIX","Factory_SpawnFactory_OakAI"),
            ("BPChar_TrooperShotgun_C_FIX","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMelee_C_FIX","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasic_C_FIX","SpawnFactory_OakAI_2"),
        ]))
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2b_TrprShtMleJtpk',
        size,replace_enemy([
            ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_3"),
        ]))
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3a',
        size,replace_enemy([
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_3"),
            ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_4"),
        ]))
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3b',
        size,replace_enemy([
            ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_3"),
            ("BPChar_Heavy_Basic_C","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_5"),
        ]))
        
def round2():
    #ROUND 2 fix on 3a medic, basic, jetpack, badass

    #wave 1_0
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave1',
        size,replace_enemy([
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_3"),
            ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedic_C","SpawnFactory_OakAI_5"),
            ("BPChar_TrooperFlash_C","SpawnFactory_OakAI_6"),
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_7"),
        ]))
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2a',
        size,replace_enemy([
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMeleeDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpackDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_6"),
            ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2b',
        size,replace_enemy([
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMeleeDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_Heavy_Basic_C","SpawnFactory_OakAI_10"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpackDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_6"),
            ("BPChar_Heavy_Powerhouse_C","SpawnFactory_OakAI_8"),
            ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3a',
        size,replace_enemy([
            ("BPChar_TrooperShotgunDark_C_FIX","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMeleeDark_C_FIX","SpawnFactory_OakAI_1"),
            ("BPChar_HeavyGunner_C_FIX","SpawnFactory_OakAI_10"),
            ("BPChar_TrooperBasicDark_C_FIX","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpackDark_C_FIX","SpawnFactory_OakAI_3"),
            ("BPChar_TrooperBadass_C_FIX","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedicDark_C_FIX","SpawnFactory_OakAI_5"),
            ("BPChar_TrooperFlashDark_C_FIX","SpawnFactory_OakAI_6"),
        ]))
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3b',
        size,replace_enemy([
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMeleeDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_10"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpackDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_Heavy_Icebreaker_C","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_6"),
            ("BPChar_Heavy_Acidrain_C","SpawnFactory_OakAI_7"),
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_8"),
        ]))
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4a',
        size,replace_enemy([
            ("BPChar_TrooperMeleeDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_10"),
            ("BPChar_Heavy_Badass_C","SpawnFactory_OakAI_11"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_Heavy_Acidrain_C","SpawnFactory_OakAI_7"),
            ("BPChar_Heavy_Basic_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 4b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4b',
        size,replace_enemy([
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_0"),
            ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_10"),
            ("BPChar_Heavy_Badass_C","SpawnFactory_OakAI_11"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_12"),
            ("BPChar_Heavy_Icebreaker_C","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_Heavy_Powerhouse_C","SpawnFactory_OakAI_8"),
        ]))

def round3():
    #ROUND 3 FIX on 2a dark heavy, dogs, nogs
    
    #wave 1a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1a',
        size,replace_enemy([
            ("BPChar_TrooperFlashDark_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_16"),
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_3"),
        ]))
    #wave 1b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1b',
        size,replace_enemy([
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_19"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
            ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
        ]))
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2a',
        size,replace_enemy([
            ("BPChar_FrontrunnerBasic_C_FIX","Factory_SpawnFactory_OakAI"),
            ("BPChar_HeavyGunnerDark_C_FIX","SpawnFactory_OakAI_24"),
            ("BPChar_Heavy_PowerhouseDark_C_FIX","SpawnFactory_OakAI_25"),
            ("BPChar_NogBasic_C_FIX","SpawnFactory_OakAI_26"),
            ("BPChar_Heavy_BasicDark_C_FIX","SpawnFactory_OakAI_28"),
        ]))
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2b',
        size,replace_enemy([
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
            ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_29"),
        ]))
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3a',
        size,replace_enemy([
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
            ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
        ]))
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3b',
        size,replace_enemy([
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
            ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_29"),
        ]))
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Maliwan/Overspheres/Variants/SpawnOptions_Oversphere_RandomElement',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
        ]))
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave4a',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
            ("BPChar_Oversphere_C","SpawnFactory_OakAI_3"),
            ("BPChar_NogBasicDark_C","SpawnFactory_OakAI_4"),
            ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_7"),
        ]))

def round4():
    #ROUND 4 fix on 4a? fix, dogs, dark medic 3b? heavy spawn
    
    #wave_1
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave1',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_NogBasicDark_C","SpawnFactory_OakAI_4"),
            ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
            ("BPChar_Oversphere_C","SpawnFactory_OakAI_7"),
        ]))
    #wave 2
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave2',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
            ("BPChar_NogBasicDark_C","SpawnFactory_OakAI_4"),
            ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
            ("BPChar_Oversphere_C","SpawnFactory_OakAI_7"),
            ("BPChar_OversphereDefender_C","SpawnFactory_OakAI_8"),
        ]))
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3a',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_NogBasicDark_C","SpawnFactory_OakAI_4"),
            ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
            ("BPChar_Oversphere_C","SpawnFactory_OakAI_7"),
            ("BPChar_OversphereDefender_C","SpawnFactory_OakAI_8"),
            ("BPChar_TrooperJetpackDark_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3b',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_OversphereHarbinger_C","SpawnFactory_OakAI_10"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
            ("BPChar_Oversphere_C","SpawnFactory_OakAI_7"),
            ("BPChar_OversphereDefender_C","SpawnFactory_OakAI_8"),
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4a',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_Frontrunner_Badass_C_FIX","SpawnFactory_OakAI_0"),
            ("BPChar_FrontrunnerJammer_C_FIX","SpawnFactory_OakAI_1"),
            ("BPChar_OversphereDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_TrooperMedicDark_C_FIX","SpawnFactory_OakAI_15"),
            ("BPChar_TrooperBasicDark_C_FIX","SpawnFactory_OakAI_16"),
            ("BPChar_OversphereStinger_C","SpawnFactory_OakAI_17"),
            ("BPChar_FrontrunnerStriker_C_FIX","SpawnFactory_OakAI_20"),
        ]))
    #wave 4b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4b',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_OversphereDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_18"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_22"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_23"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_OversphereStinger_C","SpawnFactory_OakAI_126"),
            ("BPChar_MechBasic_C","SpawnFactory_OakAI_27"),
            ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_30"),
        ]))

def round5():
    #ROUND 5 fix on 3a fix darc centurion, basic_mech
    
    #wave_1a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1a',
        size,replace_enemy([
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_10"),
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_12"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_13"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_15"),
            ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
        ]))
    #wave_1b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1b',
        size,replace_enemy([
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_10"),
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_12"),
            ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_13"),
            ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
        ]))
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2a',
        size,replace_enemy([
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_12"),
            ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_13"),
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
            ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_26"),
        ]))
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2b',
        size,replace_enemy([
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
            ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_15"),
            ("BPChar_MechMGDark_C","SpawnFactory_OakAI_16"),
            ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_26"),
        ]))
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3a',
        size,replace_enemy([
            ("BPChar_HeavyGunnerDark_C_FIX","SpawnFactory_OakAI_0"),
            ("BPChar_Heavy_BadassDark_C_FIX","SpawnFactory_OakAI_1"),
            ("BPChar_MechBasicDark_C_FIX","SpawnFactory_OakAI_11"),
            ("BPChar_MechChargerDark_C_FIX","SpawnFactory_OakAI_14"),
            ("BPChar_MechGrenadierDark_C_FIX","SpawnFactory_OakAI_15"),
            ("BPChar_MechMGDark_C_FIX","SpawnFactory_OakAI_16"),
            ("BPChar_FrontrunnerStriker_C_FIX","SpawnFactory_OakAI_2"),
            ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
        ]))
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3b',
        size,replace_enemy([
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
            ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_15"),
            ("BPChar_MechMGDark_C","SpawnFactory_OakAI_16"),
            ("BPChar_FrontrunnerJammer_C","SpawnFactory_OakAI_2"),
            ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_26"),
            ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_3"),
            ("BPChar_OversphereStingerDark_C","SpawnFactory_OakAI_4"),
        ]))
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4a',
        size,replace_enemy([
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_FrontrunnerStriker_C","SpawnFactory_OakAI_10"),
            ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_12"),
            ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_6"),
            ("BPChar_MechMGDark_C","SpawnFactory_OakAI_7"),
            ("BPChar_FrontrunnerBasic_C","SpawnFactory_OakAI_8"),
            ("BPChar_FrontrunnerJammer_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 4b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4b',
        size,replace_enemy([
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
            ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_15"),
            ("BPChar_MechMGDark_C","SpawnFactory_OakAI_16"),
            ("BPChar_FrontrunnerBasic_C","SpawnFactory_OakAI_2"),
            ("BPChar_FrontrunnerJammer_C","SpawnFactory_OakAI_3"),
            ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_4"),
            ("BPChar_FrontrunnerStriker_C","SpawnFactory_OakAI_5"),
        ]))
    #wave 5a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave5',
        size,replace_enemy([
            ("BPChar_NogBadassDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBadassDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_12"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_13"),
            ("BPChar_Heavy_AcidrainDark_C","SpawnFactory_OakAI_14"),
            ("BPChar_Heavy_IcebreakerDark_C","SpawnFactory_OakAI_15"),
            ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_2"),
            ("BPChar_MechMGDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_5"),
        ]))
    #wave5b
    gen_mod('/Game/Enemies/_Spawning/ProvingGrounds/Trial7/SpawnOptions_PGTrial7_Maliwan_MechAdds',
        size,replace_enemy([
            ("BPChar_TrooperBasic_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_TrooperMedic_C","Factory_SpawnFactory_OakAI_3"),
            ("BPChar_TrooperFlash_C","Factory_SpawnFactory_OakAI_4"),
        ]))
    # Let's try it without generating bosses
    # #BOSS 2
    # gen_mod('/Game/Enemies/_Spawning/Maliwan/Mechs/_Unique/SpawnOptions_Mech_TechSlaughterBoss2',
    #     float(boss_size[1]),[
    #         ("/Game/PatchDLC/Dandelion/Enemies/Fabrikator/Basic/_Design/Character/BPChar_FabrikatorBasic","Factory_SpawnFactory_OakAI"),
    #     ])
    # 
    # #BOSS 1 !bug here
    # gen_mod('/Game/Enemies/_Spawning/Maliwan/Mechs/_Unique/SpawnOptions_Mech_TechSlaughterBoss1',
    #     float(boss_size[0]),[
    #         ("/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Character/BPChar_Mech_TrialBoss","Factory_SpawnFactory_OakAI"),
    #     ])

# [ ] round1?
round1()
# [ ] round2?
round2()
# # [ ] round3?
round3()
# # [ ] round4?
round4()
# # [ ] round5?
round5()

mod.close()
