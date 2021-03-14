#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

""" RUN command for Arch
cd bl3hotfixmodding_OLD
mitmdump --ignore-hosts '^(?![0-9\.]+:)(?!([^\.:]+\.)*discovery\.services\.gearboxsoftware\.com:)' -s hfinject.py
"""
import sys
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod
import random
import math
mod = Mod('3000_simple.bl3hotfix',
        '3000 Boss Rush slaughter',
        'altef_4 feat. SkruntSkrunt',
        ['turns maliwan slaughter star 3000',
        'into a boss rush slaughter'],
        lic=Mod.CC_BY_SA_40,
        v='0.9',
        cats='gameplay',)

from gen_3000_Char_list import *
from gen_3000_helper_functions import *
from decimal import Decimal

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

def HS(etype, value):
    if etype in "Normal":
        return Decimal(math.log(((100/float(value))/1)*base_hs*12.0))
    elif etype in "VeryGood":
        return Decimal(math.log(((100/float(value))/1)*base_hs*3.0))
    elif etype in "Badass":
        return Decimal(math.log(((100/float(value))/1)*base_hs*1.2))
    elif etype in "SuperBadass":
        return Decimal(math.log(((100/float(value))/1)*base_hs*1.5))
    elif etype in "UltimateBadass":
        return Decimal(math.log(((100/float(value))/1)*base_hs*1.7))
    else:
        return Decimal(math.log(((100/float(value))/1)*base_hs*1.2))
def DS(etype,value):
    if etype in "Normal":
        return Decimal(math.log(((float(value)/0.1)/1)*base_ds*1.0))
    elif etype in "VeryGood":
        return Decimal(math.log(((float(value)/0.1)/1)*base_ds*1.2))
    elif etype in "Badass":
        return Decimal(math.log(((float(value)/0.1)/1)*base_ds*1.5))
    elif etype in "SuperBadass":
        return Decimal(math.log(((float(value)/0.1)/1)*base_ds*1.7))
    elif etype in "UltimateBadass":
        return Decimal(math.log(((float(value)/0.1)/1)*base_ds*1.9))
    else:
        return Decimal(math.log(((float(value)/0.1)/1)*base_ds*1.0))

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

healh_chance = 52
def gen_mod(so, scale, list):
    c = len(list)
    global healh_chance
    healh_chance -= 1
    for idx, val in enumerate(list):
        #tval = val.split('.')
        #val = tval[0]
        if val == 'empty':
            continue
        var = val
        # var = eval(val+"(0)").split(".")
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
            
gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_1/SpawnOptions_KatagawaBallAdds_MeleeMix',
        size,[
            ("/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/BPChar_Enforcer_Bounty01", "Factory_SpawnFactory_OakAI"), # ??
            ("/Game/Enemies/ServiceBot/LOOT/_Design/Character/BPChar_ServiceBot_LOOT","Factory_SpawnFactory_OakAI_1"),
            ("/Game/Enemies/Skag/_Unique/Buttmunch/_Design/Character/BPChar_SkagButtmunch","Factory_SpawnFactory_OakAI_2"),
            ("/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue","Factory_SpawnFactory_OakAI_3"),
            ("/Game/Enemies/Heavy/_Unique/FootstepsOfGiants/_Design/Character/BPChar_HeavyFootstepsOfGiants","Factory_SpawnFactory_OakAI_4"),
            ("/Game/Enemies/Nog/_Unique/Beans/_Design/Character/BPChar_NogBeans","Factory_SpawnFactory_OakAI_5"),
        ])

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


#wave 1a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1a_Trooper1',
         size,[
             ("/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderBasicJUNK","SpawnFactory_OakAI_2")
         ])


#wave 1b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1b_TrooperBscShtGn',
    size,[
        ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_0"),
        ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_2")
    ])
#wave 2a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2a_Trooper',
    size,[
        ("BPChar_TrooperBadass_C_FIX","Factory_SpawnFactory_OakAI"),
        ("BPChar_TrooperShotgun_C_FIX","SpawnFactory_OakAI_0"),
        ("BPChar_TrooperMelee_C_FIX","SpawnFactory_OakAI_1"),
        ("BPChar_TrooperBasic_C_FIX","SpawnFactory_OakAI_2"),
    ])
#wave 2b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2b_TrprShtMleJtpk',
    size,[
        ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_0"),
        ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_1"),
        ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_2"),
        ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_3"),
    ])
#wave 3a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3a',
    size,[
        ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_0"),
        ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_1"),
        ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_2"),
        ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_3"),
        ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_4"),
    ])
#wave 3b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3b',
    size,[
        ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_0"),
        ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_1"),
        ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_2"),
        ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_3"),
        ("BPChar_Heavy_Basic_C","SpawnFactory_OakAI_4"),
        ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_5"),
    ])

#ROUND 2 fix on 3a medic, basic, jetpack, badass

#wave 1_0
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave1',
    size,[
        ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_0"),
        ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_1"),
        ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
        ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_3"),
        ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_4"),
        ("BPChar_TrooperMedic_C","SpawnFactory_OakAI_5"),
        ("BPChar_TrooperFlash_C","SpawnFactory_OakAI_6"),
        ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_7"),
    ])
#wave 2a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2a',
    size,[
        ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_0"),
        ("BPChar_TrooperMeleeDark_C","SpawnFactory_OakAI_1"),
        ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
        ("BPChar_TrooperJetpackDark_C","SpawnFactory_OakAI_3"),
        ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_4"),
        ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
        ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_6"),
        ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_9"),
    ])
#wave 2b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2b',
    size,[
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
    ])
#wave 3a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3a',
    size,[
        ("BPChar_TrooperShotgunDark_C_FIX.SpawnFactory_OakAI_0"),
        ("BPChar_TrooperMeleeDark_C_FIX.SpawnFactory_OakAI_1"),
        ("BPChar_HeavyGunner_C_FIX.SpawnFactory_OakAI_10"),
        ("BPChar_TrooperBasicDark_C_FIX.SpawnFactory_OakAI_2"),
        ("BPChar_TrooperJetpackDark_C_FIX.SpawnFactory_OakAI_3"),
        ("BPChar_TrooperBadass_C_FIX.SpawnFactory_OakAI_4"),
        ("BPChar_TrooperMedicDark_C_FIX.SpawnFactory_OakAI_5"),
        ("BPChar_TrooperFlashDark_C_FIX.SpawnFactory_OakAI_6"),
    ])
#wave 3b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3b',
    size,[
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
    ])
#wave 4a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4a',
    size,[
        ("BPChar_TrooperMeleeDark_C","SpawnFactory_OakAI_1"),
        ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_10"),
        ("BPChar_Heavy_Badass_C","SpawnFactory_OakAI_11"),
        ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
        ("BPChar_Heavy_Acidrain_C","SpawnFactory_OakAI_7"),
        ("BPChar_Heavy_Basic_C","SpawnFactory_OakAI_9"),
    ])
#wave 4b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4b',
    size,[
        ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_0"),
        ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_10"),
        ("BPChar_Heavy_Badass_C","SpawnFactory_OakAI_11"),
        ("BPChar_NogBasic_C","SpawnFactory_OakAI_12"),
        ("BPChar_Heavy_Icebreaker_C","SpawnFactory_OakAI_4"),
        ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
        ("BPChar_Heavy_Powerhouse_C","SpawnFactory_OakAI_8"),
    ])

#ROUND 3 FIX on 2a dark heavy, dogs, nogs

#wave 1a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1a',
    size,[
        ("BPChar_TrooperFlashDark_C","Factory_SpawnFactory_OakAI"),
        ("BPChar_NogBasic_C","SpawnFactory_OakAI_16"),
        ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_2"),
        ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_3"),
    ])
#wave 1b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1b',
    size,[
        ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_19"),
        ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
        ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_25"),
        ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
        ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
    ])
#wave 2a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2a',
    size,[
        ("BPChar_FrontrunnerBasic_C_FIX.Factory_SpawnFactory_OakAI"),
        ("BPChar_HeavyGunnerDark_C_FIX.SpawnFactory_OakAI_24"),
        ("BPChar_Heavy_PowerhouseDark_C_FIX.SpawnFactory_OakAI_25"),
        ("BPChar_NogBasic_C_FIX.SpawnFactory_OakAI_26"),
        ("BPChar_Heavy_BasicDark_C_FIX.SpawnFactory_OakAI_28"),
    ])
#wave 2b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2b',
    size,[
        ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
        ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
        ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
        ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
        ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
        ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_29"),
    ])
#wave 3a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3a',
    size,[
        ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
        ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
        ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
        ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
        ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
    ])
#wave 3b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3b',
    size,[
        ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
        ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
        ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
        ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
        ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
        ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_29"),
    ])
#wave 4a
gen_mod('/Game/Enemies/_Spawning/Maliwan/Overspheres/Variants/SpawnOptions_Oversphere_RandomElement',
    size,[
        ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
    ])
#wave 4a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave4a',
    size,[
        ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
        ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
        ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
        ("BPChar_Oversphere_C","SpawnFactory_OakAI_3"),
        ("BPChar_NogBasicDark_C","SpawnFactory_OakAI_4"),
        ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
        ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
        ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_7"),
    ])

#ROUND 4 fix on 4a? fix, dogs, dark medic 3b? heavy spawn

#wave_1
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave1',
    size,[
        ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
        ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_0"),
        ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_1"),
        ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
        ("BPChar_NogBasicDark_C","SpawnFactory_OakAI_4"),
        ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
        ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
        ("BPChar_Oversphere_C","SpawnFactory_OakAI_7"),
    ])
#wave 2
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave2',
    size,[
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
    ])
#wave 3a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3a',
    size,[
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
    ])
#wave 3b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3b',
    size,[
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
    ])
#wave 4a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4a',
    size,[
        ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
        ("BPChar_Frontrunner_Badass_C_FIX.SpawnFactory_OakAI_0"),
        ("BPChar_FrontrunnerJammer_C_FIX.SpawnFactory_OakAI_1"),
        ("BPChar_OversphereDark_C","SpawnFactory_OakAI_11"),
        ("BPChar_TrooperMedicDark_C_FIX.SpawnFactory_OakAI_15"),
        ("BPChar_TrooperBasicDark_C_FIX.SpawnFactory_OakAI_16"),
        ("BPChar_OversphereStinger_C","SpawnFactory_OakAI_17"),
        ("BPChar_FrontrunnerStriker_C_FIX.SpawnFactory_OakAI_20"),
    ])
#wave 4b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4b',
    size,[
        ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
        ("BPChar_OversphereDark_C","SpawnFactory_OakAI_11"),
        ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_18"),
        ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_22"),
        ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_23"),
        ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
        ("BPChar_OversphereStinger_C","SpawnFactory_OakAI_126"),
        ("BPChar_MechBasic_C","SpawnFactory_OakAI_27"),
        ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_30"),
    ])

#ROUND 5 fix on 3a fix darc centurion, basic_mech

#wave_1a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1a',
    size,[
        ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_10"),
        ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
        ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_12"),
        ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_13"),
        ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_15"),
        ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_24"),
        ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
    ])
#wave_1b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1b',
    size,[
        ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_10"),
        ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
        ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_12"),
        ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_13"),
        ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_24"),
        ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
    ])
#wave 2a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2a',
    size,[
        ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
        ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_12"),
        ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_13"),
        ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
        ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
        ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
        ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_26"),
    ])
#wave 2b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2b',
    size,[
        ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
        ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
        ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_15"),
        ("BPChar_MechMGDark_C","SpawnFactory_OakAI_16"),
        ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
        ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
        ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_26"),
    ])
#wave 3a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3a',
    size,[
        ("BPChar_HeavyGunnerDark_C_FIX.SpawnFactory_OakAI_0"),
        ("BPChar_Heavy_BadassDark_C_FIX.SpawnFactory_OakAI_1"),
        ("BPChar_MechBasicDark_C_FIX.SpawnFactory_OakAI_11"),
        ("BPChar_MechChargerDark_C_FIX.SpawnFactory_OakAI_14"),
        ("BPChar_MechGrenadierDark_C_FIX.SpawnFactory_OakAI_15"),
        ("BPChar_MechMGDark_C_FIX.SpawnFactory_OakAI_16"),
        ("BPChar_FrontrunnerStriker_C_FIX.SpawnFactory_OakAI_2"),
        ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
        ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
    ])
#wave 3b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3b',
    size,[
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
    ])
#wave 4a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4a',
    size,[
        ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_0"),
        ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_1"),
        ("BPChar_FrontrunnerStriker_C","SpawnFactory_OakAI_10"),
        ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_12"),
        ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_6"),
        ("BPChar_MechMGDark_C","SpawnFactory_OakAI_7"),
        ("BPChar_FrontrunnerBasic_C","SpawnFactory_OakAI_8"),
        ("BPChar_FrontrunnerJammer_C","SpawnFactory_OakAI_9"),
    ])
#wave 4b
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4b',
    size,[
        ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
        ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
        ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_15"),
        ("BPChar_MechMGDark_C","SpawnFactory_OakAI_16"),
        ("BPChar_FrontrunnerBasic_C","SpawnFactory_OakAI_2"),
        ("BPChar_FrontrunnerJammer_C","SpawnFactory_OakAI_3"),
        ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_4"),
        ("BPChar_FrontrunnerStriker_C","SpawnFactory_OakAI_5"),
    ])
#wave 5a
gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave5',
    size,[
        ("BPChar_NogBadassDark_C","SpawnFactory_OakAI_1"),
        ("BPChar_TrooperBadassDark_C","SpawnFactory_OakAI_11"),
        ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_12"),
        ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_13"),
        ("BPChar_Heavy_AcidrainDark_C","SpawnFactory_OakAI_14"),
        ("BPChar_Heavy_IcebreakerDark_C","SpawnFactory_OakAI_15"),
        ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_2"),
        ("BPChar_MechMGDark_C","SpawnFactory_OakAI_3"),
        ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_5"),
    ])
#wave5b
gen_mod('/Game/Enemies/_Spawning/ProvingGrounds/Trial7/SpawnOptions_PGTrial7_Maliwan_MechAdds',
    size,[
        ("BPChar_TrooperBasic_C","Factory_SpawnFactory_OakAI"),
        ("BPChar_TrooperMedic_C","Factory_SpawnFactory_OakAI_3"),
        ("BPChar_TrooperFlash_C","Factory_SpawnFactory_OakAI_4"),
    ])
#BOSS 2
gen_mod('/Game/Enemies/_Spawning/Maliwan/Mechs/_Unique/SpawnOptions_Mech_TechSlaughterBoss2',
    float(boss_size[1]),[
        ("BPChar_GiganticMech2_C","Factory_SpawnFactory_OakAI"),
    ])

#BOSS 1 !bug here
gen_mod('/Game/Enemies/_Spawning/Maliwan/Mechs/_Unique/SpawnOptions_Mech_TechSlaughterBoss1',
    float(boss_size[0]),[
        ("BPChar_GiganticMech2_C","Factory_SpawnFactory_OakAI"),
    ])




# gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1b_TrooperBscShtGn',
#         size,[
#             "BPChar_TrooperShotgun_C.SpawnFactory_OakAI_0",
#             "BPChar_TrooperBasic_C.SpawnFactory_OakAI_2"
#         ])
# gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2a_Trooper',
#         size,[
#             "BPChar_TrooperBadass_C_FIX.Factory_SpawnFactory_OakAI",
#             "BPChar_TrooperShotgun_C_FIX.SpawnFactory_OakAI_0",
#             "BPChar_TrooperMelee_C_FIX.SpawnFactory_OakAI_1",
#             "BPChar_TrooperBasic_C_FIX.SpawnFactory_OakAI_2"
#         ])
# 
mod.close()
