#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

""" RUN command for Arch
cd bl3hotfixmodding_OLD
mitmdump --ignore-hosts '^(?![0-9\.]+:)(?!([^\.:]+\.)*discovery\.services\.gearboxsoftware\.com:)' -s hfinject.py
"""
from bl3hotfixmod.bl3hotfixmod import Mod
import random
import math
mod = Mod('3000_hyperion_slaughter.bl3hotfix',
        '3000 hyperion slaughter',
        'altef_4',
        ['turns maliwan slaughter star 3000',
        'into hyperion slaughter'],
        lic=Mod.CC_BY_SA_40,
        v='1.0',
        cats='gameplay',)

""" some tests
    SparkCharacterLoadedEntry,(1,1,0,BPChar_Timothy),/Dandelion/NonPlayerCharacters/Timothy/_Design/Character/BPChar_Timothy.Default__BPChar_Timothy_C:CharacterMesh0,RelativeScale3D,0,,(X=2.0,Y=2.0,Z=2.0)
    SparkCharacterLoadedEntry,(1,1,0,BPChar_Timothy),/Dandelion/NonPlayerCharacters/Timothy/_Design/Character/BPChar_Timothy.Default__BPChar_Timothy_C:CharacterMesh0,AnimClass,0,,AnimBlueprintGeneratedClass'/Game/Enemies/Trooper/_Shared/Animation/BPAnim_Trooper.BPAnim_Trooper_C'
    SparkEarlyLevelPatchEntry,(1,1,0,TechSlaughter_P),/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.OakMissionSpawner_2326.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den,SpawnOptions,0,,SpawnOptionData'/Game/Enemies/_Spawning/Maliwan/Mechs/_Unique/SpawnOptions_Mech_TechSlaughterBoss1.SpawnOptions_Mech_TechSlaughterBoss1'

    fixes 
    SpawnerStyle_Bunch
    SpawnOptions_TechSlaughter_Round1Wave2a_Trooper
    SpawnOptions_TechSlaughter_Round2Wave3a
    SpawnOptions_TechSlaughter_Round3Wave2a
    SpawnOptions_TechSlaughter_Round4Wave4a
    SpawnOptions_TechSlaughter_Round5Wave3a


    scale = 0.8
    spawn = "/Game/Enemies/_Spawning/CotV/Enforcers/_Unique/SpawnOptions_EnforcerSacrificeBoss_Runnable"
    bpchar = "/Dandelion/Enemies/Looters/Enforcer/Bruiser/_Design/Character/BPChar_Enforcer_PrettyBoy"
    extspawn = '50,50,100'.split(',')
    last_bit = bpchar.split('/')[-1]

    mod.reg_hotfix(Mod.EARLYLEVEL, 'Sacrifice_P',
        Mod.get_full(spawn),
        'Options.Options[{}].Factory.Object..AIActorClass'.format(0),
        "BlueprintGeneratedClass'{}.{}_C'".format(bpchar, last_bit))

    mod.reg_hotfix(Mod.LEVEL, 'Sacrifice_P',
        Mod.get_full(spawn),
        'Options.Options[{}].Factory.Object..SpawnExtent'.format(0),
        f'(x={float(extspawn[0]) * scale},y={float(extspawn[1]) * scale},z={float(extspawn[2]) * scale})')

    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.Default__{}_C:CharacterMesh0'.format(bpchar, last_bit),
        'RelativeScale3D',
        f'(X={scale},Y={scale},Z={scale})')
    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.Default__{}_C'.format(bpchar, last_bit),
        'PreEnragedActorScale',
        f'(X={scale},Y={scale},Z={scale})')
    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.Default__{}_C'.format(bpchar, last_bit),
        'EnragedActorScale',
        f'(X={scale * 0.59},Y={scale * 0.59},Z={scale * 0.59})')
            
            
    mod.reg_hotfix(Mod.CHAR, last_bit,
            '/Game/PatchDLC/Dandelion/Enemies/Fabrikator/Basic/_Design/Character/BPChar_FabrikatorBasic.BPChar_FabrikatorBasic:AIBalanceState_GEN_VARIABLE',
            'DropLootPattern',
            "LootSpawnPatternData'/Game/GameData/Loot/SpawnPatterns/LootSpawnPattern_KingBoboSpit.LootSpawnPattern_KingBoboSpit'")

    mod.reg_hotfix(Mod.CHAR, last_bit,
            '/Game/GameData/Loot/SpawnPatterns/LootSpawnPattern_KingBoboSpit.LootSpawnPattern_KingBoboSpit',
            'Speed',
            '3000')
    mod.reg_hotfix(Mod.CHAR, last_bit,
            '/Game/GameData/Loot/SpawnPatterns/LootSpawnPattern_KingBoboSpit.LootSpawnPattern_KingBoboSpit',
            'MaxSpeed',
            '3000')
"""

from gen_3000_Char_list import *
from gen_3000_helper_functions import *
from decimal import Decimal
#full mod
run_all = True

#cartel extender
enable_cartel_extender = True

#test spawn switcher
test_spawn = False
test_round = 1 # 1..5
test_wave = 1 # wave +.1 for a +.2 for b
test_ab = 2 # 1 or 2 or 3

test_spawn2 = False
test2 = "WORK1"
test = "WORK1"

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



"""
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Single".format(m),
                'SpawnerComponent.Object..SpawnerStyle.Object.SpawnOptions',
                "SpawnOptionData'/Game/Enemies/_Spawning/Maliwan/Mechs/_Unique/SpawnOptions_Mech_TechSlaughterBoss1.SpawnOptions_Mech_TechSlaughterBoss1'")
            
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den".format(m),
                'SpawnOptions',
                "SpawnOptionData'/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave5.SpawnOptions_TechSlaughter_Round5Wave5'")
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_Den_0".format(m),
                'SpawnOptions',
                "SpawnOptionData'/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave5.SpawnOptions_TechSlaughter_Round5Wave5'")
           
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter".format(m),
                'Waves.Waves[0].SpawnPointGroupName',
                '"Right"')
            
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter".format(m),
                'Waves.Waves[1].SpawnPointGroupName',
                '"Center"')
            
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
                'bRandomizeSpawnPoints',
                'False',"",True)
            for i in range(3):
                mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
              #      "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
               #     'SpawnPointGroups[{}].bRandomize'.format(i),
                #    'True',"",True)
                #for l in range(20):
                #   mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
                    'SpawnPointGroups[{}]'.format(i),
                    "(SpawnPoints=(2421,2422,2423,2424,2425,2426,2427,2428,2429,2430,2431, 1677,1678,1680,1682,,1684,1685,1687,1689))","",True)

    1588 ->SpawnerLinkComponent-> 2392 Team ->
                            -> 1618 SpawnerComp -> SpawnNodeComponent, TerritoryComponent, OakSpawnerIconComponent 
                            -> 2290 LincComp ->
    for char in [
            'BPChar_WeeLoaderBasic',
            ]:
        for pool in [
                'ItemPool_CoVEnemyUse_AssaultRifles',
                'ItemPool_COVEnemyUse_HeavyWeapons',
                'ItemPool_CoVEnemyUse_Pistols',
                'ItemPool_CoVEnemyUse_Shotguns',
                'ItemPool_CoVEnemyUse_SMGs',
                'ItemPool_CoVEnemyUse_SniperRifles',
                ]:
            for num in range(10):
                mod.reg_hotfix(Mod.CHAR, char,
                        '/Game/Enemies/_Shared/_Design/ItemPools/{}.{}'.format(pool, pool),
                        'BalancedItems[{}].bDropOnDeath'.format(num),
                        'True')
    for i in range(4):
        mod.reg_hotfix(Mod.PATCH, 'BPChar_WeeLoaderBasic',
            "/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPool_WeeLoader_LeftArm.ItemPool_WeeLoader_LeftArm",
            'BalancedItems.BalancedItems[{}].InventoryBalanceData'.format(i),
            "/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob")
    mod.reg_hotfix(Mod.CHAR, 'BPChar_WeeLoaderBadass',
        "/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBadass/_Design/Character/BPChar_WeeLoaderBadass.Default__BPChar_WeeLoaderBadass_C:CharacterMesh0",
        'AnimClass',
        "AnimBlueprintGeneratedClass'/Game/Enemies/Ratch/_Shared/Animation/BPAnim_Ratch.BPAnim_Ratch_C'","", True)

    mod.reg_hotfix(Mod.CHAR, 'BPChar_WeeLoaderBasic',
            '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBasic/_Design/Character/BPChar_WeeLoaderBasic.Default__BPChar_WeeLoaderBasic_C',
            'DefaultBalanceWeaponData',
            Mod.get_full_cond('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner', 'InventoryBalanceData'))


    mod.reg_hotfix(Mod.CHAR, 'BPChar_WeeLoaderBasic',
        "/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBasic/_Design/Character/BPChar_WeeLoaderBasic.BPChar_WeeLoaderBasic_C:AIBalanceState_GEN_VARIABLE",
        'PlayThroughs.PlayThroughs[1].DropOnDeathItemPools[0]',
        "(ItemPool=ItemPoolData'/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon.ItemPool_TrialBossGoon',PoolProbability=(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000),NumberOfTimesToSelectFromThisPool=(BaseValueConstant=3.000000,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000),PartSelectionOverrides=)")

    mod.reg_hotfix(Mod.CHAR, 'BPChar_WeeLoaderBasic',
        "/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBasic/_Design/Character/BPChar_WeeLoaderBasic.BPChar_WeeLoaderBasic_C:AIBalanceState_GEN_VARIABLE",
        'PlayThroughs.PlayThroughs[1].bOverrideDropOnDeathItemPools',
        "True")
    mod.reg_hotfix(Mod.CHAR, 'BPChar_WeeLoaderBasic',
        "/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBasic/_Design/Character/BPChar_WeeLoaderBasic.BPChar_WeeLoaderBasic_C:AIBalanceState_GEN_VARIABLE",
        'PlayThroughs.PlayThroughs[1].EquippedItemPoolCollections',
        "((ItemPools=((ItemPool=ItemPoolData'/Game/GameData/Loot/ItemPools/Guns/ItemPool_AR_Shotgun_SMG_Legendary.ItemPool_AR_Shotgun_SMG_Legendary')))")
"""


#test spawn
if test_spawn:
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
        "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den".format('OakMissionSpawner_Round1Wave'),
        'SpawnOptions',
        "SpawnOptionData'{}'".format(mod.get_full(spawn_conf(test_round,test_wave,test_ab, "spawn"))))
#mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
 #   "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.OakMissionSpawner_Round1Wave.EnabledCondition_MissionEnableConditionObjective",
  #  'ObjectiveRef',
   # '(Mission=/Game/Missions/Side/Slaughters/TechSlaughter/Mission_TechSlaughter1.Mission_TechSlaughter1_C,ObjectiveName="Obj_StartRound_2_Objective",ObjectiveGuid=1EED25294E31DC05DD17029253781EB0)')


revert_enum = False
def rev(cnt, idx):
    if revert_enum:
        return cnt - idx - 1
    else:
        return idx
"""
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01',
        'Manufacturers.Manufacturers[2].WeaponTypes.WeaponTypes[1].Materials.Materials[0].Material',
        Mod.get_full_cond('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/Model/Materials/Legendary/MI_Hyp_SG_Legendary_04_A'))
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01',
        'Manufacturers.Manufacturers[6].WeaponTypes.WeaponTypes[2].Materials.Materials[0].Material',
        Mod.get_full_cond('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/Model/Materials/Unique/MI_AR_Tor_AmberManagment'))
"""
mob_health_color(mod)

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

healh_chance = 52
def gen_mod(so, scale, list):
    c = len(list)
    global healh_chance
    healh_chance -= 1
    for idx, val in enumerate(list):
        tval = val.split('.')
        val = tval[0]
        if val != 'empty':
            var = eval(val+"(0)").split(".")
            obj = var[1].replace("_C'","")
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P', Mod.get_full(so), 'Options.Options[{}].Factory.Object..AIActorClass'.format(rev(c,idx)), "{}.{}".format(var[0],var[1]))
            data = eval(val+"(2)").split(",")
            if obj not in ready_list:
                ready_list.append(obj)
                for i in range(6):
                    if i == 5:
                        if health_dmg_multiply:
                            if health_dmg_with_log:
                                mod.table_hotfix(Mod.CHAR, obj, Mod.get_full(data[0]), data[1], HM[i], round(Decimal(float(data[8])*DS(data[7],data[8])),2))
                            else:
                                mod.table_hotfix(Mod.CHAR, obj, Mod.get_full(data[0]), data[1], HM[i], round(Decimal(float(data[8])*base_ds),2))
                        else:
                            mod.table_hotfix(Mod.CHAR, obj, Mod.get_full(data[0]), data[1], HM[i], float(data[8]) + base_ds)
                    else:
                        if health_dmg_multiply:
                            if health_dmg_with_log:
                                mod.table_hotfix(Mod.CHAR, obj, Mod.get_full(data[0]), data[1], HM[i], round(Decimal(float(data[i+2])*HS(data[7],data[i+2])),2))
                            else:
                                mod.table_hotfix(Mod.CHAR, obj, Mod.get_full(data[0]), data[1], HM[i], round(Decimal(float(data[i+2]) * base_hs),2))
                        else:
                            mod.table_hotfix(Mod.CHAR, obj, Mod.get_full(data[0]), data[1], HM[i], float(data[i+2]) + base_hs)
                            


            bpchar = var[0].replace("BlueprintGeneratedClass'","")
            last_bit = bpchar.split('/')[-1]


            if last_bit not in move_list:
                move_list.append(last_bit)
                is_boss = eval("{}(7)".format(val))
                if not is_boss:
                    mob_held_wpn(mod,bpchar,last_bit,enemy_legendaries(data[7]))
                    mob_health_override(mod,bpchar,last_bit,int('FIX' not in val),(100-healh_chance//2)*0.01,(100-healh_chance)*0.01)
                    
                #char_move = eval("{}(4)".format(val))
                #if char_move != "":
                mob_move_speed(mod, bpchar, last_bit, mob_speed)

                '''mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format(bpchar,last_bit),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..bShowInZoneMap',
                    "True")
                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format(bpchar,last_bit),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestTransform.Object..Scale3D',
                    "(X=0.1,Y=0.1,Z=0.1)")

                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format(bpchar,last_bit),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..POISprite',
                    enemy_icon(data[7]))

                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format(bpchar,last_bit),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..IconFrameName',
                    'miniLegendary')
                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '/Game/Enemies/_Shared/_Design/BPChar_Enemy.BPChar_Enemy_C:OakMinimapIcon_GEN_VARIABLE',
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..bShowInZoneMap',
                    "True")

                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '/Game/Enemies/_Shared/_Design/BPChar_Enemy.BPChar_Enemy_C:OakMinimapIcon_GEN_VARIABLE',
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..POISprite',
                    enemy_icon(data[7]))

                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '/Game/Enemies/_Shared/_Design/BPChar_Enemy.BPChar_Enemy_C:OakMinimapIcon_GEN_VARIABLE',
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestTransform.Scale3D',
                    "(X=0.1,Y=0.1,Z=0.1)")'''




                '''mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format('/Game/Enemies/_Shared/_Design/BPChar_Enemy','BPChar_Enemy'),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..bShowInZoneMap',
                    "True")

                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format('/Game/Enemies/_Shared/_Design/BPChar_Enemy','BPChar_Enemy'),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..POISprite',
                    enemy_icon(data[7]))

                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format('/Game/Enemies/_Shared/_Design/BPChar_Enemy','BPChar_Enemy'),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..POIClass',
                    "POIClass'{}.{}_C'".format(bpchar,last_bit),'', True)

                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format('/Game/Enemies/_Shared/_Design/BPChar_Enemy','BPChar_Enemy'),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..POIIconComponentClass',
                    "POIIconComponentClass'{}.{}_C'".format('/Game/InteractiveObjects/GameSystemMachines/ZoneMap/Design/BP_ZoneMap_AIPOI','BP_ZoneMap_AIPOI'),'', True)'''

                '''mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format('/Game/Enemies/_Shared/_Design/BPChar_Enemy','BPChar_Enemy'),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..POISprite',
                    enemy_icon(data[7]),'', True)

                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format('/Game/Enemies/_Shared/_Design/BPChar_Enemy','BPChar_Enemy'),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..IconFrameName',
                    'Enemy','', True)

                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format('/Game/Enemies/_Shared/_Design/BPChar_Enemy','BPChar_Enemy'),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..IconZOffset',
                    '0.0','', True)'''

                '''mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:SkeletalMesh_GEN_VARIABLE'.format(bpchar,last_bit),
                    'OverrideMaterials.OverrideMaterials[0]',
                    "MaterialInstanceConstant{}".format("'/Game/Enemies/Mech/_Shared/Model/Materials/MI_MechGenIVIV.MI_MechGenIVIV'"))
                    
                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format(bpchar,last_bit),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..bShowInZoneMap',
                    "True")
                    
                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format(bpchar,last_bit),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..POISprite',
                    "{}".format(enemy_icon("Normal")))
                    
                mod.reg_hotfix(Mod.CHAR, last_bit,
                    '{}.{}_C:OakMinimapIcon_GEN_VARIABLE'.format(bpchar,last_bit),
                    'MinimapIconProperties.ZoneMapPOIData.PointOfInterestType.Object..IconFrameName',
                    "Enemy"))'''


            if last_bit not in mesh_list:
                mesh_list.append(last_bit)
                anim = eval("{}(6)".format(val))
                if anim != "":
                    mod.reg_hotfix(Mod.CHAR, last_bit,
                        '{}.Default__{}_C:CharacterMesh0'.format(bpchar, last_bit),
                        'AnimClass',
                        "{}".format(anim),"",True)

            


          
                base_scale = float(eval("{}(5)".format(val)))
                print("{}_{}.from_{}".format(last_bit,base_scale,val))
                if size_mod:
                    if scale != 1.0:
                        scale_char(mod,bpchar,last_bit,base_scale,scale)

            extend = eval(val+"(1)").replace('(x=','').replace('y=','').replace('z=','').replace(')','').split(',')
            if size_mod == False:
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
            
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P', '{}:{}'.format(Mod.get_full(so),tval[1]), 'TeamOverride', Mod.get_full_cond('/Game/Common/_Design/Teams/Team_Maliwan', 'Team'))



def cartel():
    gen_mod('/Game/Enemies/_Spawning/Maliwan/Troopers/Variants/SpawnOptions_TrooperMedic',
        size,[
            "BPChar_TrooperMedic_C.Factory_SpawnFactory_OakAI"
        ])
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/SpawnOptions_MaliwanFullMix',
        size,[
            "BPChar_TrooperMelee_C.Factory_SpawnFactory_OakAI",
            "BPChar_TrooperBasic_C.Factory_SpawnFactory_OakAI_1",
            "BPChar_TrooperFlash_C.Factory_SpawnFactory_OakAI_2",
            "BPChar_TrooperJetpack_C.Factory_SpawnFactory_OakAI_3",
            "BPChar_TrooperBadass_C.Factory_SpawnFactory_OakAI_5",
            "empty",
        ])
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_4/DarkMaliwan_mixes/SpawnOptions_Maliwan_Dark_TrooperMix',
        size,[
            "BPChar_TrooperBasicDark_C.Factory_SpawnFactory_OakAI",
            "BPChar_TrooperMeleeDark_C.Factory_SpawnFactory_OakAI_1",
            "BPChar_TrooperMedicDark_C.Factory_SpawnFactory_OakAI_2",
            "BPChar_TrooperFlashDark_C.Factory_SpawnFactory_OakAI_3",
            "BPChar_TrooperJetpackDark_C.Factory_SpawnFactory_OakAI_4",
            "BPChar_TrooperShotgunDark_C.Factory_SpawnFactory_OakAI_5",
            "BPChar_TrooperBadassDark_C.Factory_SpawnFactory_OakAI_6"
        ])
    gen_mod('/Game/Enemies/_Spawning/Maliwan/Heavies/Variants/SpawnOptions_HeavyBadassDark_Random',
        size,[
            "BPChar_Heavy_BadassDark_C.Factory_SpawnFactory_OakAI",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_0",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_1",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_2"
        ])
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_4/DarkMaliwan_mixes/SpawnOptions_Maliwan_Dark_HeavyMix',
        size,[
            "BPChar_Heavy_BasicDark_C.Factory_SpawnFactory_OakAI",
            "BPChar_Heavy_AcidrainDark_C.Factory_SpawnFactory_OakAI_1",
            "BPChar_Heavy_IcebreakerDark_C.Factory_SpawnFactory_OakAI_2",
            "BPChar_Heavy_PowerhouseDark_C.Factory_SpawnFactory_OakAI_3",
            "BPChar_HeavyGunnerDark_C.Factory_SpawnFactory_OakAI_5",
            "empty",
        ])
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_4/DarkMaliwan_mixes/SpawnOptions_Maliwan_Dark_NogMix',
        size,[
            "BPChar_NogBasicDark_C.Factory_SpawnFactory_OakAI",
            "BPChar_NogNinjaDark_C.Factory_SpawnFactory_OakAI_1",
            "BPChar_NogBadassDark_C.Factory_SpawnFactory_OakAI_2"
        ])
    gen_mod('/Game/Enemies/_Spawning/Maliwan/Overspheres/Variants/SpawnOptions_OversphereDark_RandomElement',
        size,[
            "BPChar_OversphereDark_C.Factory_SpawnFactory_OakAI"
        ])
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_4/DarkMaliwan_mixes/SpawnOptions_Maliwan_Dark_OversphereMix',
        size,[
            "BPChar_OversphereStingerDark_C.Factory_SpawnFactory_OakAI_1",
            "BPChar_OversphereHarbingerDark_C.Factory_SpawnFactory_OakAI_2",
            "BPChar_OversphereDefenderDark_C.Factory_SpawnFactory_OakAI_3",
            "empty",
        ])
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_4/DarkMaliwan_mixes/SpawnOptions_Maliwan_Dark_MechMix',
        size,[
            "BPChar_MechBasicDark_C.Factory_SpawnFactory_OakAI",
            "BPChar_MechCharger_C.Factory_SpawnFactory_OakAI_1",
            "BPChar_MechGrenadier_C.Factory_SpawnFactory_OakAI_3",
            "BPChar_MechMG_C.Factory_SpawnFactory_OakAI_4"
        ])
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_4/DarkMaliwan_mixes/SpawnOptions_Maliwan_Dark_FrontrunnerMix',
        size,[
            "BPChar_FrontrunnerBasic_C.Factory_SpawnFactory_OakAI",
            "BPChar_FrontrunnerJammer_C.Factory_SpawnFactory_OakAI_1",
            "BPChar_FrontrunnerStriker_C.Factory_SpawnFactory_OakAI_2",
            "BPChar_Frontrunner_Badass_C.Factory_SpawnFactory_OakAI_3"
        ])
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_4/DarkMaliwan_mixes/SpawnOptions_Maliwan_DarkBadasses',
        size,[
            "BPChar_TrooperBadassDark_C.SpawnFactory_OakAI_0",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_1",
            "BPChar_NogBadassDark_C.SpawnFactory_OakAI_2",
            "BPChar_MechGrenadierDark_C.SpawnFactory_OakAI_3"
        ])
    """    
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_4/DarkMaliwan_mixes/SpawnOptions_Maliwan_Dark_FullMix',
        size,[
            "empty",
            "empty",
            "empty",
            "empty",
            "empty",
            "empty",
            "empty"
        ])
    """

#ROUND 1 fix on 2a badass basic
if test_spawn2:
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_1/SpawnOptions_KatagawaBallAdds_MeleeMix',
        size,[
            "{}.Factory_SpawnFactory_OakAI".format(test),
            "{}.Factory_SpawnFactory_OakAI_1".format(test),
            "{}.Factory_SpawnFactory_OakAI_2".format(test),
            "{}.Factory_SpawnFactory_OakAI_3".format(test),
            "{}.Factory_SpawnFactory_OakAI_4".format(test),
            "{}.Factory_SpawnFactory_OakAI_5".format(test)
        ])

    #wave 1a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1a_Trooper1',
        size,[
            "{}.SpawnFactory_OakAI_2".format(test2)
        ])
else:
    #wave 1a
    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_1/SpawnOptions_KatagawaBallAdds_MeleeMix',
        size,[
            "BPChar_TrooperMelee_C.Factory_SpawnFactory_OakAI",
            "BPChar_TrooperMelee_C.Factory_SpawnFactory_OakAI_1",
            "BPChar_TrooperMelee_C.Factory_SpawnFactory_OakAI_2",
            "BPChar_TrooperMelee_C.Factory_SpawnFactory_OakAI_3",
            "BPChar_TrooperMelee_C.Factory_SpawnFactory_OakAI_4",
            "BPChar_TrooperMelee_C.Factory_SpawnFactory_OakAI_5"
        ])

    #wave 1a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1a_Trooper1',
        size,[
            "BPChar_TrooperBasic_C.SpawnFactory_OakAI_2"
        ])
if run_all:    
    #wave 1b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1b_TrooperBscShtGn',
        size,[
            "BPChar_TrooperShotgun_C.SpawnFactory_OakAI_0",
            "BPChar_TrooperBasic_C.SpawnFactory_OakAI_2"
        ])
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2a_Trooper',
        size,[
            "BPChar_TrooperBadass_C_FIX.Factory_SpawnFactory_OakAI",
            "BPChar_TrooperShotgun_C_FIX.SpawnFactory_OakAI_0",
            "BPChar_TrooperMelee_C_FIX.SpawnFactory_OakAI_1",
            "BPChar_TrooperBasic_C_FIX.SpawnFactory_OakAI_2"
        ])
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2b_TrprShtMleJtpk',
        size,[
            "BPChar_TrooperShotgun_C.SpawnFactory_OakAI_0",
            "BPChar_TrooperMelee_C.SpawnFactory_OakAI_1",
            "BPChar_TrooperBasic_C.SpawnFactory_OakAI_2",
            "BPChar_TrooperJetpack_C.SpawnFactory_OakAI_3"
        ])
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3a',
        size,[
            "BPChar_TrooperBadass_C.SpawnFactory_OakAI_0",
            "BPChar_TrooperShotgun_C.SpawnFactory_OakAI_1",
            "BPChar_TrooperMelee_C.SpawnFactory_OakAI_2",
            "BPChar_TrooperBasic_C.SpawnFactory_OakAI_3",
            "BPChar_TrooperJetpack_C.SpawnFactory_OakAI_4"
        ])
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3b',
        size,[
            "BPChar_TrooperShotgun_C.SpawnFactory_OakAI_0",
            "BPChar_TrooperMelee_C.SpawnFactory_OakAI_1",
            "BPChar_TrooperBasic_C.SpawnFactory_OakAI_2",
            "BPChar_TrooperJetpack_C.SpawnFactory_OakAI_3",
            "BPChar_Heavy_Basic_C.SpawnFactory_OakAI_4",
            "BPChar_TrooperBadass_C.SpawnFactory_OakAI_5"
        ])

    #ROUND 2 fix on 3a medic, basic, jetpack, badass

    #wave 1_0
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave1',
        size,[
            "BPChar_TrooperShotgunDark_C.SpawnFactory_OakAI_0",
            "BPChar_TrooperMelee_C.SpawnFactory_OakAI_1",
            "BPChar_TrooperBasicDark_C.SpawnFactory_OakAI_2",
            "BPChar_TrooperJetpack_C.SpawnFactory_OakAI_3",
            "BPChar_HeavyGunner_C.SpawnFactory_OakAI_4",
            "BPChar_TrooperMedic_C.SpawnFactory_OakAI_5",
            "BPChar_TrooperFlash_C.SpawnFactory_OakAI_6",
            "BPChar_TrooperBadass_C.SpawnFactory_OakAI_7"
        ])
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2a',
        size,[
            "BPChar_TrooperShotgunDark_C.SpawnFactory_OakAI_0",
            "BPChar_TrooperMeleeDark_C.SpawnFactory_OakAI_1",
            "BPChar_TrooperBasicDark_C.SpawnFactory_OakAI_2",
            "BPChar_TrooperJetpackDark_C.SpawnFactory_OakAI_3",
            "BPChar_TrooperBadass_C.SpawnFactory_OakAI_4",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_5",
            "BPChar_TrooperFlashDark_C.SpawnFactory_OakAI_6",
            "BPChar_HeavyGunner_C.SpawnFactory_OakAI_9"
        ])
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2b',
        size,[
            "BPChar_TrooperShotgunDark_C.SpawnFactory_OakAI_0",
            "BPChar_TrooperMeleeDark_C.SpawnFactory_OakAI_1",
            "BPChar_Heavy_Basic_C.SpawnFactory_OakAI_10",
            "BPChar_TrooperBasicDark_C.SpawnFactory_OakAI_2",
            "BPChar_TrooperJetpackDark_C.SpawnFactory_OakAI_3",
            "BPChar_TrooperBadass_C.SpawnFactory_OakAI_4",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_5",
            "BPChar_TrooperFlashDark_C.SpawnFactory_OakAI_6",
            "BPChar_Heavy_Powerhouse_C.SpawnFactory_OakAI_8",
            "BPChar_HeavyGunner_C.SpawnFactory_OakAI_9"
        ])
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3a',
        size,[
            "BPChar_TrooperShotgunDark_C_FIX.SpawnFactory_OakAI_0",
            "BPChar_TrooperMeleeDark_C_FIX.SpawnFactory_OakAI_1",
            "BPChar_HeavyGunner_C_FIX.SpawnFactory_OakAI_10",
            "BPChar_TrooperBasicDark_C_FIX.SpawnFactory_OakAI_2",
            "BPChar_TrooperJetpackDark_C_FIX.SpawnFactory_OakAI_3",
            "BPChar_TrooperBadass_C_FIX.SpawnFactory_OakAI_4",
            "BPChar_TrooperMedicDark_C_FIX.SpawnFactory_OakAI_5",
            "BPChar_TrooperFlashDark_C_FIX.SpawnFactory_OakAI_6"
        ])
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3b',
        size,[
            "BPChar_TrooperShotgunDark_C.SpawnFactory_OakAI_0",
            "BPChar_TrooperMeleeDark_C.SpawnFactory_OakAI_1",
            "BPChar_HeavyGunner_C.SpawnFactory_OakAI_10",
            "BPChar_TrooperBasicDark_C.SpawnFactory_OakAI_2",
            "BPChar_TrooperJetpackDark_C.SpawnFactory_OakAI_3",
            "BPChar_Heavy_Icebreaker_C.SpawnFactory_OakAI_4",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_5",
            "BPChar_TrooperFlashDark_C.SpawnFactory_OakAI_6",
            "BPChar_Heavy_Acidrain_C.SpawnFactory_OakAI_7",
            "BPChar_TrooperBadass_C.SpawnFactory_OakAI_8"
        ])
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4a',
        size,[
            "BPChar_TrooperMeleeDark_C.SpawnFactory_OakAI_1",
            "BPChar_HeavyGunner_C.SpawnFactory_OakAI_10",
            "BPChar_Heavy_Badass_C.SpawnFactory_OakAI_11",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_5",
            "BPChar_Heavy_Acidrain_C.SpawnFactory_OakAI_7",
            "BPChar_Heavy_Basic_C.SpawnFactory_OakAI_9",
        ])
    #wave 4b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4b',
        size,[
            "BPChar_TrooperBadass_C.SpawnFactory_OakAI_0",
            "BPChar_HeavyGunner_C.SpawnFactory_OakAI_10",
            "BPChar_Heavy_Badass_C.SpawnFactory_OakAI_11",
            "BPChar_NogBasic_C.SpawnFactory_OakAI_12",
            "BPChar_Heavy_Icebreaker_C.SpawnFactory_OakAI_4",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_5",
            "BPChar_Heavy_Powerhouse_C.SpawnFactory_OakAI_8"
        ])

    #ROUND 3 FIX on 2a dark heavy, dogs, nogs

    #wave 1a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1a',
        size,[
            "BPChar_TrooperFlashDark_C.Factory_SpawnFactory_OakAI",
            "BPChar_NogBasic_C.SpawnFactory_OakAI_16",
            "BPChar_TrooperShotgunDark_C.SpawnFactory_OakAI_2",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_3",
        ])
    #wave 1b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1b',
        size,[
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_19",
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_24",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_25",
            "BPChar_NogBasic_C.SpawnFactory_OakAI_26",
            "BPChar_NogNinja_C.SpawnFactory_OakAI_27",
        ])
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2a',
        size,[
            "BPChar_FrontrunnerBasic_C_FIX.Factory_SpawnFactory_OakAI",
            "BPChar_HeavyGunnerDark_C_FIX.SpawnFactory_OakAI_24",
            "BPChar_Heavy_PowerhouseDark_C_FIX.SpawnFactory_OakAI_25",
            "BPChar_NogBasic_C_FIX.SpawnFactory_OakAI_26",
            "BPChar_Heavy_BasicDark_C_FIX.SpawnFactory_OakAI_28",
        ])
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2b',
        size,[
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_24",
            "BPChar_Heavy_PowerhouseDark_C.SpawnFactory_OakAI_25",
            "BPChar_NogBasic_C.SpawnFactory_OakAI_26",
            "BPChar_NogNinja_C.SpawnFactory_OakAI_27",
            "BPChar_Heavy_BasicDark_C.SpawnFactory_OakAI_28",
            "BPChar_NogNogromancer_C.SpawnFactory_OakAI_29",
        ])
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3a',
        size,[
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_24",
            "BPChar_Heavy_PowerhouseDark_C.SpawnFactory_OakAI_25",
            "BPChar_NogBasic_C.SpawnFactory_OakAI_26",
            "BPChar_NogNinja_C.SpawnFactory_OakAI_27",
            "BPChar_Heavy_BasicDark_C.SpawnFactory_OakAI_28",
        ])
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3b',
        size,[
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_24",
            "BPChar_Heavy_PowerhouseDark_C.SpawnFactory_OakAI_25",
            "BPChar_NogBasic_C.SpawnFactory_OakAI_26",
            "BPChar_NogNinja_C.SpawnFactory_OakAI_27",
            "BPChar_Heavy_BasicDark_C.SpawnFactory_OakAI_28",
            "BPChar_NogNogromancer_C.SpawnFactory_OakAI_29",
        ])
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Maliwan/Overspheres/Variants/SpawnOptions_Oversphere_RandomElement',
        size,[
            "BPChar_Oversphere_C.Factory_SpawnFactory_OakAI",
        ])
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave4a',
        size,[
            "BPChar_Oversphere_C.Factory_SpawnFactory_OakAI",
            "BPChar_Heavy_PowerhouseDark_C.SpawnFactory_OakAI_25",
            "BPChar_Heavy_BasicDark_C.SpawnFactory_OakAI_28",
            "BPChar_Oversphere_C.SpawnFactory_OakAI_3",
            "BPChar_NogBasicDark_C.SpawnFactory_OakAI_4",
            "BPChar_NogNinjaDark_C.SpawnFactory_OakAI_5",
            "BPChar_NogNogromancer_C.SpawnFactory_OakAI_6",
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_7",
        ])

    #ROUND 4 fix on 4a? fix, dogs, dark medic 3b? heavy spawn

    #wave_1
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave1',
        size,[
            "BPChar_Oversphere_C.Factory_SpawnFactory_OakAI",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_0",
            "BPChar_TrooperShotgunDark_C.SpawnFactory_OakAI_1",
            "BPChar_TrooperBasicDark_C.SpawnFactory_OakAI_2",
            "BPChar_NogBasicDark_C.SpawnFactory_OakAI_4",
            "BPChar_NogNinjaDark_C.SpawnFactory_OakAI_5",
            "BPChar_NogNogromancer_C.SpawnFactory_OakAI_6",
            "BPChar_Oversphere_C.SpawnFactory_OakAI_7",
        ])
    #wave 2
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave2',
        size,[
            "BPChar_Oversphere_C.Factory_SpawnFactory_OakAI",
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_0",
            "BPChar_Heavy_PowerhouseDark_C.SpawnFactory_OakAI_1",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_2",
            "BPChar_Heavy_BasicDark_C.SpawnFactory_OakAI_28",
            "BPChar_NogBasicDark_C.SpawnFactory_OakAI_4",
            "BPChar_NogNinjaDark_C.SpawnFactory_OakAI_5",
            "BPChar_NogNogromancer_C.SpawnFactory_OakAI_6",
            "BPChar_Oversphere_C.SpawnFactory_OakAI_7",
            "BPChar_OversphereDefender_C.SpawnFactory_OakAI_8",
        ])
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3a',
        size,[
            "BPChar_Oversphere_C.Factory_SpawnFactory_OakAI",
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_0",
            "BPChar_Heavy_PowerhouseDark_C.SpawnFactory_OakAI_1",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_2",
            "BPChar_Heavy_BasicDark_C.SpawnFactory_OakAI_28",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_3",
            "BPChar_NogBasicDark_C.SpawnFactory_OakAI_4",
            "BPChar_NogNinjaDark_C.SpawnFactory_OakAI_5",
            "BPChar_NogNogromancer_C.SpawnFactory_OakAI_6",
            "BPChar_Oversphere_C.SpawnFactory_OakAI_7",
            "BPChar_OversphereDefender_C.SpawnFactory_OakAI_8",
            "BPChar_TrooperJetpackDark_C.SpawnFactory_OakAI_9",
        ])
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3b',
        size,[
            "BPChar_Oversphere_C.Factory_SpawnFactory_OakAI",
            "BPChar_TrooperBasicDark_C.SpawnFactory_OakAI_0",
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_1",
            "BPChar_OversphereHarbinger_C.SpawnFactory_OakAI_10",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_2",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_3",
            "BPChar_NogNinjaDark_C.SpawnFactory_OakAI_5",
            "BPChar_NogNogromancer_C.SpawnFactory_OakAI_6",
            "BPChar_Oversphere_C.SpawnFactory_OakAI_7",
            "BPChar_OversphereDefender_C.SpawnFactory_OakAI_8",
            "BPChar_TrooperShotgunDark_C.SpawnFactory_OakAI_9",
        ])
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4a',
        size,[
            "BPChar_Oversphere_C.Factory_SpawnFactory_OakAI",
            "BPChar_Frontrunner_Badass_C_FIX.SpawnFactory_OakAI_0",
            "BPChar_FrontrunnerJammer_C_FIX.SpawnFactory_OakAI_1",
            "BPChar_OversphereDark_C.SpawnFactory_OakAI_11",
            "BPChar_TrooperMedicDark_C_FIX.SpawnFactory_OakAI_15",
            "BPChar_TrooperBasicDark_C_FIX.SpawnFactory_OakAI_16",
            "BPChar_OversphereStinger_C.SpawnFactory_OakAI_17",
            "BPChar_FrontrunnerStriker_C_FIX.SpawnFactory_OakAI_20",
        ])
    #wave 4b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4b',
        size,[
            "BPChar_Oversphere_C.Factory_SpawnFactory_OakAI",
            "BPChar_OversphereDark_C.SpawnFactory_OakAI_11",
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_18",
            "BPChar_Heavy_BasicDark_C.SpawnFactory_OakAI_22",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_23",
            "BPChar_OversphereHarbingerDark_C.SpawnFactory_OakAI_25",
            "BPChar_OversphereStinger_C.SpawnFactory_OakAI_126",
            "BPChar_MechBasic_C.SpawnFactory_OakAI_27",
            "BPChar_NogNinjaDark_C.SpawnFactory_OakAI_30",
        ])

    #ROUND 5 fix on 3a fix darc centurion, basic_mech

    #wave_1a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1a',
        size,[
            "BPChar_MechChargerDark_C.SpawnFactory_OakAI_10",
            "BPChar_MechBasicDark_C.SpawnFactory_OakAI_11",
            "BPChar_TrooperShotgunDark_C.SpawnFactory_OakAI_12",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_13",
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_15",
            "BPChar_OversphereDefenderDark_C.SpawnFactory_OakAI_24",
            "BPChar_OversphereHarbingerDark_C.SpawnFactory_OakAI_25",
        ])
    #wave_1b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1b',
        size,[
            "BPChar_MechChargerDark_C.SpawnFactory_OakAI_10",
            "BPChar_MechBasicDark_C.SpawnFactory_OakAI_11",
            "BPChar_TrooperMedicDark_C.SpawnFactory_OakAI_12",
            "BPChar_TrooperFlashDark_C.SpawnFactory_OakAI_13",
            "BPChar_OversphereDefenderDark_C.SpawnFactory_OakAI_24",
            "BPChar_OversphereHarbingerDark_C.SpawnFactory_OakAI_25",
        ])
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2a',
        size,[
            "BPChar_MechBasicDark_C.SpawnFactory_OakAI_11",
            "BPChar_TrooperBasicDark_C.SpawnFactory_OakAI_12",
            "BPChar_TrooperFlashDark_C.SpawnFactory_OakAI_13",
            "BPChar_MechChargerDark_C.SpawnFactory_OakAI_14",
            "BPChar_OversphereBadass_C.SpawnFactory_OakAI_24",
            "BPChar_OversphereHarbingerDark_C.SpawnFactory_OakAI_25",
            "BPChar_OversphereDefenderDark_C.SpawnFactory_OakAI_26",
        ])
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2b',
        size,[
            "BPChar_MechBasicDark_C.SpawnFactory_OakAI_11",
            "BPChar_MechChargerDark_C.SpawnFactory_OakAI_14",
            "BPChar_MechGrenadierDark_C.SpawnFactory_OakAI_15",
            "BPChar_MechMGDark_C.SpawnFactory_OakAI_16",
            "BPChar_OversphereBadass_C.SpawnFactory_OakAI_24",
            "BPChar_OversphereHarbingerDark_C.SpawnFactory_OakAI_25",
            "BPChar_OversphereDefenderDark_C.SpawnFactory_OakAI_26",
        ])
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3a',
        size,[
            "BPChar_HeavyGunnerDark_C_FIX.SpawnFactory_OakAI_0",
            "BPChar_Heavy_BadassDark_C_FIX.SpawnFactory_OakAI_1",
            "BPChar_MechBasicDark_C_FIX.SpawnFactory_OakAI_11",
            "BPChar_MechChargerDark_C_FIX.SpawnFactory_OakAI_14",
            "BPChar_MechGrenadierDark_C_FIX.SpawnFactory_OakAI_15",
            "BPChar_MechMGDark_C_FIX.SpawnFactory_OakAI_16",
            "BPChar_FrontrunnerStriker_C_FIX.SpawnFactory_OakAI_2",
            "BPChar_OversphereBadass_C.SpawnFactory_OakAI_24",
            "BPChar_OversphereHarbingerDark_C.SpawnFactory_OakAI_25",
        ])
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3b',
        size,[
            "BPChar_HeavyGunnerDark_C.SpawnFactory_OakAI_0",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_1",
            "BPChar_MechBasicDark_C.SpawnFactory_OakAI_11",
            "BPChar_MechChargerDark_C.SpawnFactory_OakAI_14",
            "BPChar_MechGrenadierDark_C.SpawnFactory_OakAI_15",
            "BPChar_MechMGDark_C.SpawnFactory_OakAI_16",
            "BPChar_FrontrunnerJammer_C.SpawnFactory_OakAI_2",
            "BPChar_OversphereBadass_C.SpawnFactory_OakAI_24",
            "BPChar_OversphereDefenderDark_C.SpawnFactory_OakAI_26",
            "BPChar_Frontrunner_Badass_C.SpawnFactory_OakAI_3",
            "BPChar_OversphereStingerDark_C.SpawnFactory_OakAI_4",
        ])
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4a',
        size,[
            "BPChar_MechBasicDark_C.SpawnFactory_OakAI_0",
            "BPChar_MechChargerDark_C.SpawnFactory_OakAI_1",
            "BPChar_FrontrunnerStriker_C.SpawnFactory_OakAI_10",
            "BPChar_Frontrunner_Badass_C.SpawnFactory_OakAI_12",
            "BPChar_MechGrenadierDark_C.SpawnFactory_OakAI_6",
            "BPChar_MechMGDark_C.SpawnFactory_OakAI_7",
            "BPChar_FrontrunnerBasic_C.SpawnFactory_OakAI_8",
            "BPChar_FrontrunnerJammer_C.SpawnFactory_OakAI_9",
        ])
    #wave 4b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4b',
        size,[
            "BPChar_MechBasicDark_C.SpawnFactory_OakAI_11",
            "BPChar_MechChargerDark_C.SpawnFactory_OakAI_14",
            "BPChar_MechGrenadierDark_C.SpawnFactory_OakAI_15",
            "BPChar_MechMGDark_C.SpawnFactory_OakAI_16",
            "BPChar_FrontrunnerBasic_C.SpawnFactory_OakAI_2",
            "BPChar_FrontrunnerJammer_C.SpawnFactory_OakAI_3",
            "BPChar_Frontrunner_Badass_C.SpawnFactory_OakAI_4",
            "BPChar_FrontrunnerStriker_C.SpawnFactory_OakAI_5",
        ])
    #wave 5a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave5',
        size,[
            "BPChar_NogBadassDark_C.SpawnFactory_OakAI_1",
            "BPChar_TrooperBadassDark_C.SpawnFactory_OakAI_11",
            "BPChar_Heavy_PowerhouseDark_C.SpawnFactory_OakAI_12",
            "BPChar_Heavy_BadassDark_C.SpawnFactory_OakAI_13",
            "BPChar_Heavy_AcidrainDark_C.SpawnFactory_OakAI_14",
            "BPChar_Heavy_IcebreakerDark_C.SpawnFactory_OakAI_15",
            "BPChar_OversphereBadass_C.SpawnFactory_OakAI_2",
            "BPChar_MechMGDark_C.SpawnFactory_OakAI_3",
            "BPChar_Frontrunner_Badass_C.SpawnFactory_OakAI_5",
        ])
    #wave5b
    gen_mod('/Game/Enemies/_Spawning/ProvingGrounds/Trial7/SpawnOptions_PGTrial7_Maliwan_MechAdds',
        size,[
            "BPChar_TrooperBasic_C.Factory_SpawnFactory_OakAI",
            "BPChar_TrooperMedic_C.Factory_SpawnFactory_OakAI_3",
            "BPChar_TrooperFlash_C.Factory_SpawnFactory_OakAI_4"
        ])
    #BOSS 2
    gen_mod('/Game/Enemies/_Spawning/Maliwan/Mechs/_Unique/SpawnOptions_Mech_TechSlaughterBoss2',
        float(boss_size[1]),[
            "BPChar_GiganticMech2_C.Factory_SpawnFactory_OakAI"
        ])
 
    #BOSS 1 !bug here
    gen_mod('/Game/Enemies/_Spawning/Maliwan/Mechs/_Unique/SpawnOptions_Mech_TechSlaughterBoss1',
        float(boss_size[0]),[
            "BPChar_GiganticMech2_C.Factory_SpawnFactory_OakAI",
        ])
    
if enable_cartel_extender == True:
    cartel()

loot_pat = 'LootSpawnPattern_CrazyEarlDoor'
bosses_path = "{}|{}".format(eval("BPChar_GiganticMech2_C(0)").replace("BlueprintGeneratedClass'","").replace("_C'","").split(".")[0],eval("BPChar_GiganticMech2_C(0)").replace("BlueprintGeneratedClass'","").replace("_C'","").split(".")[0]).split("|")
bosses_bpchar = "{}|{}".format(bosses_path[0].split("/")[-1],bosses_path[1].split("/")[-1]).split("|")
for i in range(2):
    mod.reg_hotfix(Mod.CHAR, bosses_bpchar[i],
            '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bosses_path[i],bosses_bpchar[i]),
            'DropLootPattern',
            "LootSpawnPatternData'/Game/GameData/Loot/SpawnPatterns/{}.{}'".format(loot_pat,loot_pat))

    mod.reg_hotfix(Mod.CHAR, bosses_bpchar[i],
            '/Game/GameData/Loot/SpawnPatterns/{}.{}'.format(loot_pat,loot_pat),
            'Speed',
            '4500')
    mod.reg_hotfix(Mod.CHAR, bosses_bpchar[i],
            '/Game/GameData/Loot/SpawnPatterns/{}.{}'.format(loot_pat,loot_pat),
            'MaxSpeed',
            '7500')

    mod.reg_hotfix(Mod.CHAR, bosses_bpchar[i],
            '/Game/GameData/Loot/SpawnPatterns/{}.{}'.format(loot_pat,loot_pat),
            'AngularSpeed',
            '1500')
    mod.reg_hotfix(Mod.CHAR, bosses_bpchar[i],
            '/Game/GameData/Loot/SpawnPatterns/{}.{}'.format(loot_pat,loot_pat),
            'MaxAngularSpeed',
            '2000')
    if i == 1:
        roll = 180       
    else:
        roll = 180       
        mod.reg_hotfix(Mod.CHAR, bosses_bpchar[i],
                '{}.{}_C:ComponentDelegateBinding_1'.format(bosses_path[i],bosses_bpchar[i]),
                'ComponentDelegateBindings',
                ('((ComponentPropertyName="OakDamageComponent",DelegatePropertyName="OnDeath",FunctionNameToBind="BndEvt__OakDamageComponent_K2Node_ComponentBoundEvent_0_DamageCompDiedDelegate__DelegateSignature_{}"))'.format(bosses_bpchar[1])))

    mod.reg_hotfix(Mod.CHAR, bosses_bpchar[i],
            '/Game/GameData/Loot/SpawnPatterns/{}.{}'.format(loot_pat,loot_pat),
            'Direction.AdditionalRotation.Yaw',
            roll)
    mod.reg_hotfix(Mod.CHAR, bosses_bpchar[i],
            '/Game/GameData/Loot/SpawnPatterns/{}.{}'.format(loot_pat,loot_pat),
            'Direction.AdditionalRotation.Pitch',
            '20')

'''last_bit = 'BPChar_GiganticMech2'
bpchar = '/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Character/BPChar_GiganticMech2'
mod.reg_hotfix(Mod.CHAR, last_bit,
    '{}.Default__{}_C:CharacterMesh0'.format(bpchar, last_bit),
    'OverrideMaterials.OverrideMaterials[0]',
    "MaterialInstanceComponent'/Game/Enemies/Mech/_Shared/Model/Materials/MI_MechGenIVIV.MI_MechGenIVIV'",'',True)'''

'''mod.reg_hotfix(Mod.CHAR, last_bit,
    '{}.Default__{}_C:CharacterMesh0'.format(bpchar, last_bit),
    'GestaltPartList',
    "GestaltPartListData'/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Character/GPartList_Mech_TrialBoss.GPartList_Mech_TrialBoss'",'',True)'''

mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.ElevatorA_TechSlaughter_2.SpawnerComponent",
    'SpawnDetails',
    "(Critical=NotCritical,bOverrideCritical=True,RespawnStyle=Timed,bOverrideRespawnStyle=False,IrrelevantAction=Suspend,bOverrideIrrelevantAction=False,bCritical=False)",'',True)

mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.OakSpawner_Mech.SpawnerComponent",
    'SpawnDetails',
    "(Critical=NotCritical,bOverrideCritical=True,RespawnStyle=Timed,bOverrideRespawnStyle=False,IrrelevantAction=Suspend,bOverrideIrrelevantAction=False,bCritical=False)",'',True)

mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.OakSpawner_Mech_0.SpawnerComponent",
    'SpawnDetails',
    "(Critical=NotCritical,bOverrideCritical=True,RespawnStyle=Timed,bOverrideRespawnStyle=False,IrrelevantAction=Suspend,bOverrideIrrelevantAction=False,bCritical=False)",'',True)

#(ComponentClass=Class'/Script/OakGame.OakMinimapIconComponent',ComponentTemplate=OakMinimapIconComponent'/Game/PatchDLC/Dandelion/Enemies/Fabrikator/Basic/_Design/Character/BPChar_FabrikatorBasic.BPChar_FabrikatorBasic_C:OakMinimapIcon_GEN_VARIABLE',ComponentKey=(OwnerClass=BlueprintGeneratedClass'/Game/Enemies/_Shared/_Design/BPChar_Enemy.BPChar_Enemy_C'),SCSVariableName='OakMinimapIcon',AssociatedGuid='CDC48EF346D76605DA2C89AAFC36113D'CookedComponentInstancingData=())

'''mod.reg_hotfix(Mod.CHAR, 'BPChar_WeeLoaderBadass',
    "/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBadass/_Design/Character/BPChar_WeeLoaderBadass.BPChar_WeeLoaderBadass_C:InheritableComponentHandler",
    'Records',
    "((ComponentClass=Class'/Script/OakGame.AIBalanceStateComponent',ComponentTemplate=AIBalanceStateComponent'/Game/PatchDLC/Dandelion/Enemies/Fabrikator/Basic/_Design/Character/BPChar_FabrikatorBasic.BPChar_FabrikatorBasic_C:AIBalanceState_GEN_VARIABLE',ComponentKey=(OwnerClass=BlueprintGeneratedClass'/Game/Enemies/_Shared/_Design/BPChar_Enemy.BPChar_Enemy_C'),SCSVariableName='AIBalanceState',AssociatedGuid='C31D28FA4CDD242EA20669B558ADE1DB'CookedComponentInstancingData=()),(ComponentClass=Class'/Script/OakGame.OakMinimapIconComponent',ComponentTemplate=OakMinimapIconComponent'/Game/PatchDLC/Dandelion/Enemies/Fabrikator/Basic/_Design/Character/BPChar_FabrikatorBasic.BPChar_FabrikatorBasic_C:OakMinimapIcon_GEN_VARIABLE',ComponentKey=(OwnerClass=BlueprintGeneratedClass'/Game/Enemies/_Shared/_Design/BPChar_Enemy.BPChar_Enemy_C'),SCSVariableName='OakMinimapIcon',AssociatedGuid='CDC48EF346D76605DA2C89AAFC36113D'CookedComponentInstancingData=()))",'',True)
'''

#blue storm spawn offset BndEvt__OakDamageComponent_K2Node_ComponentBoundEvent_0_DamageCompDiedDelegate__DelegateSignature_BPChar_GiganticMech1
'''

mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.OakSpawnPoint_6.SpawnPointComponent",
    'RelativeLocation',
    '(X=0.0,Y=0.0,Z=4000.0)','',True)

mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.OakSpawnPoint_6.SpawnPointComponent",
    'RelativeLocation',
    '(X=15150.0,Y=-1100.0,Z=5000.0)','',True)'''

mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.OakSpawnPoint_6.SpawnPointComponent",
    'RelativeLocation',
    '(X=15150.0,Y=0.0,Z=5000.0)','',True)

mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.OakSpawnPoint_4.SpawnPointComponent",
    'RelativeLocation',
    '(X=0.0,Y=-1900.0,Z=100.0)','',True)
def r_type(id):
    return {
        0: 'RarityData_01_Common',
        1: 'RarityData_02_UnCommon',
        2: 'RarityData_03_Rare',
        3: 'RarityData_04_VeryRare',
        4: 'RarityData_05_Legendary',
        5: 'RarityData_00_Mission'
    }.get(id,'!err')
def r_stick(id):
    return {
        0: 'PS_ConsumableLocatorStick',
        1: 'PS_ItemLocatorStick_Common',
        2: 'PS_ItemLocatorStick_Uncommon',
        3: 'PS_ItemLocatorStick_Rare',
        4: 'PS_ItemLocatorStick_VeryRare',
        5: 'PS_ItemLocatorStick_Legendary'
    }.get(id,'!err')
def r_f_stick(id):
    return {
        0: 'PS_ConsumableLocatorStick',
        1: 'PS_ItemLocatorStick_Foil_Common',
        2: 'PS_ItemLocatorStick_Foil_Uncommon',
        3: 'PS_ItemLocatorStick_Foil_Rare',
        4: 'PS_ItemLocatorStick_Foil_VeryRare',
        5: 'PS_ItemLocatorStick_Foil_Legendary'
    }.get(id,'!err')
def r_color(id):
    return {
        0: '(R=1.0,G=1.0,B=1.0,A=1.0)',
        1: '(R=0.25,G=1.0,B=0.3,A=1.0)',
        2: '(R=0.0,G=0.5,B=1.0,A=1.0)',
        3: '(R=0.65,G=0.1,B=1.0,A=1.0)',
        4: '(R=1.0,G=0.278431,B=0.0,A=1.0)',
        5: '(R=0.0,G=1.0,B=1.0,A=1.0)'
    }.get(id,'!err')
def r_out_color(id):
    return {
        0: '(R=0.435,G=0.435,B=0.435,A=1.0)',
        1: '(R=0.049066,G=0.495,B=0.033667,A=1.0)',
        2: '(R=0.002663,G=0.126457,B=0.62,A=1.0)',
        3: '(R=0.605695,G=0.071247,B=0.935,A=1.0)',
        4: '(R=1.0,G=0.278431,B=0.0,A=1.0)',
        5: '(R=0.0,G=1.0,B=1.0,A=1.0)'
    }.get(id,'!err')
def r_frame(id):
    return {
        0: 'Common',
        1: 'Uncommon',
        2: 'Rare',
        3: 'Epic',
        4: 'Legendary',
        5: 'Legendary'
    }.get(id,'!err')
for i in range(0,6):
    mod.reg_hotfix(Mod.PATCH, '',
        "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
        'RarityLootBeamOverride',
        "ParticleSystem'/Game/Pickups/_Shared/Effects/Systems/{}.{}'".format(r_stick(i),r_stick(i)))
    mod.reg_hotfix(Mod.PATCH, '',
        "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
        'RarityLootBeamForInventoryWithFoilParts',
        "ParticleSystem'/Game/Pickups/_Shared/Effects/Systems/Foil/{}.{}'".format(r_f_stick(i),r_f_stick(i)))
    mod.reg_hotfix(Mod.PATCH, '',
        "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
        'RarityColorFX',
        "{}".format(r_color(i)))
    mod.reg_hotfix(Mod.PATCH, '',
        "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
        'RarityColorOutline',
        "{}".format(r_out_color(i)))
    mod.reg_hotfix(Mod.PATCH, '',
        "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
        'RarityFrameName',
        "{}".format(r_frame(i)))
    if i == 5:
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'ZoneMapPOIType',
            "ZoneMapPOITypeData'{}'".format('/Game/GameData/ZoneMap/POI_Types/POI_LegendaryPickup.POI_LegendaryPickup'))
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'WeaponDataTableRow.DataTable',
            "DataTable'/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Rarity_Stats.DataTable_Weapon_Rarity_Stats'")
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'WeaponDataTableRow.RowName',
            "Legendary")
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'RarityDisplayname',
            "TOP TIER")
    
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'RaritySortValue',
            "8")     
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'RarityLootBeamHeight',
            "150")
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'RarityLootAudioStinger',
            "WwiseEvent'/Game/Audio/Events/UX/HUD/Loot/WE_Loot_Spawn_Legendary.WE_Loot_Spawn_Legendary'")
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'RarityLootAudioStinger',
            "WwiseEvent'/Game/Audio/Events/UX/HUD/Loot/WE_Loot_Spawn_Legendary.WE_Loot_Spawn_Legendary'")
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'ItemScoreRarityModifier.BaseValueConstant',
            "1.3")
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'MonetaryValueModifier.BaseValueAttribute',
            "GbxAttributeData'/Game/GameData/Economy/Rarity/Att_RarityCostMultiplier_05_Legendary.Att_RarityCostMultiplier_05_Legendary'")
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'OnPickedUpStat',
            "/Game/PlayerCharacters/_Shared/_Design/Stats/GameSystem/Loot/Stat_GameSystem_OrangeItemsLooted.Stat_GameSystem_OrangeItemsLooted")
    else:
        mod.reg_hotfix(Mod.PATCH, '',
            "/Game/GameData/Loot/RarityData/{}.{}".format(r_type(i),r_type(i)),
            'ZoneMapPOIType',
            "")
for i in range(23):
    mod.reg_hotfix(Mod.PATCH, '',
        "{}".format(loot_base[i]),
        'RarityData',
        "OakInventoryRarityData'{}'".format('/Game/GameData/Loot/RarityData/RarityData_00_Mission.RarityData_00_Mission'))

'''

mod.reg_hotfix(Mod.PATCH, '',
    "{}".format(loot_base[0]),
    'RarityData',
    "OakInventoryRarityData'{}'".format('/Game/GameData/Loot/RarityData/RarityData_05_Legendary.RarityData_05_Legendary'))
mod.reg_hotfix(Mod.PATCH, '',
    "{}".format(loot_base[0]),
    'RarityData',
    "OakInventoryRarityData'{}'".format('/Game/GameData/Loot/RarityData/RarityData_04_VeryRare.RarityData_04_VeryRare'))
mod.reg_hotfix(Mod.PATCH, '',
    "/Game/Pickups/_Shared/Effects/Systems/PS_ItemLocatorStick_VeryRare.PS_ItemLocatorStick_VeryRare:ParticleModuleSize_0",
    'StartSize.MaxValue',
    "110",'',True)
mod.reg_hotfix(Mod.PATCH, '',
    "/Game/Pickups/_Shared/Effects/Systems/PS_ItemLocatorStick_VeryRare.PS_ItemLocatorStick_VeryRare:ParticleModuleSize_0",
    'StartSize.MinValueVec',
    "(X=6.0,Y=110.0,Z=0.0)",'',True)
mod.reg_hotfix(Mod.PATCH, '',
    "/Game/Pickups/_Shared/Effects/Systems/PS_ItemLocatorStick_VeryRare.PS_ItemLocatorStick_VeryRare:ParticleModuleSize_0",
    'StartSize.MaxValueVec',
    "(X=6.0,Y=110.0,Z=0.0)",'',True)
mod.reg_hotfix(Mod.PATCH, '',
    "/Game/Pickups/_Shared/Effects/Systems/PS_ItemLocatorStick_VeryRare.PS_ItemLocatorStick_VeryRare:ParticleModuleSize_0",
    'StartSize.MaxValue',
    "110",'',True)
mod.reg_hotfix(Mod.PATCH, '',
    "/Game/Pickups/_Shared/Effects/Systems/PS_ItemLocatorStick_Legendary.PS_ItemLocatorStick_Legendary:ParticleModuleSize_0",
    'StartSize.MinValueVec',
    "(X=6.0,Y=110.0,Z=0.0)",'',True)
mod.reg_hotfix(Mod.PATCH, '',
    "/Game/Pickups/_Shared/Effects/Systems/PS_ItemLocatorStick_Legendary.PS_ItemLocatorStick_Legendary:ParticleModuleSize_0",
    'StartSize.MaxValueVec',
    "(X=6.0,Y=110.0,Z=0.0)",'',True)'''



base_off_X = -4000
base_off_Y = 0
base_off = 260

mod.reg_hotfix(Mod.CHAR, 'BPChar_Fabrikator_Shared',
    "/Game/PatchDLC/Dandelion/Enemies/Fabrikator/_Shared/_Design/Character/BPChar_Fabrikator_Shared.BPChar_Fabrikator_Shared_C:R_F_BotSpawnPoint_GEN_VARIABLE",
    'RelativeLocation',
    '(X={}.0,Y={}.0,Z=0.0)'.format(base_off_X+base_off,base_off_Y+base_off),'',True)
mod.reg_hotfix(Mod.CHAR, 'BPChar_Fabrikator_Shared',
    "/Game/PatchDLC/Dandelion/Enemies/Fabrikator/_Shared/_Design/Character/BPChar_Fabrikator_Shared.BPChar_Fabrikator_Shared_C:R_B_BotSpawnPoint_GEN_VARIABLE",
    'RelativeLocation',
    '(X={}.0,Y={}.0,Z=0.0)'.format(base_off_X-base_off,base_off_Y+base_off),'',True)
mod.reg_hotfix(Mod.CHAR, 'BPChar_Fabrikator_Shared',
    "/Game/PatchDLC/Dandelion/Enemies/Fabrikator/_Shared/_Design/Character/BPChar_Fabrikator_Shared.BPChar_Fabrikator_Shared_C:L_F_BotSpawnPoint_GEN_VARIABLE",
    'RelativeLocation',
    '(X={}.0,Y={}.0,Z=0.0)'.format(base_off_X+base_off,base_off_Y-base_off),'',True)
mod.reg_hotfix(Mod.CHAR, 'BPChar_Fabrikator_Shared',
    "/Game/PatchDLC/Dandelion/Enemies/Fabrikator/_Shared/_Design/Character/BPChar_Fabrikator_Shared.BPChar_Fabrikator_Shared_C:L_B_BotSpawnPoint_GEN_VARIABLE",
    'RelativeLocation',
    '(X={}.0,Y={}.0,Z=0.0)'.format(base_off_X-base_off,base_off_Y-base_off),'',True)

#colision_capsule(mod,bosses_path[1],bosses_bpchar[1],150.0,120.0)
#scale_char(mod,'/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/BallBeam/Character/BP_CharBallBeam','BP_CharBallBeam',4.0,0.1)
#colision_capsule(mod,'/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/BallBeam/Character/BP_CharBallBeam','BP_CharBallBeam',0.0,0.0)
#scale_char(mod,'/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/BallGun/Character/BPChar_BallGun','BPChar_BallGun',1.0,0.1)

mod.close()
