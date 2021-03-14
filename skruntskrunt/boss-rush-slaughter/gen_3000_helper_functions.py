#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod
import random
import math
from gen_3000_Char_list import *
from decimal import Decimal

full_list = r_gun(0)
for gun in range(len(loot_base)):
    if gun != 0:
        full_list = "{},{}".format(full_list,r_gun(gun))

def mob_held_wpn(mod, bpchar, last_bit, legy_count):
    rdm = random.randrange(0, len(loot_base))
    
    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
        'PlayThroughs.PlayThroughs[1].EquippedItemPoolCollections.EquippedItemPoolCollections[0].ItemPools',
        "((ItemPool=ItemPoolData'{}',PoolProbability=(BaseValueConstant=1.00000)))".format(loot_pool[1]))

    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
        'PlayThroughs.PlayThroughs[1].EquippedItemPoolCollections.EquippedItemPoolCollections[0].ItemPools.ItemPools[0].ItemPool.BalancedItems',
        "({})".format(full_list))


    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
        'PlayThroughs.PlayThroughs[1].bOverrideDropOnDeathItemPools',
        "True")

    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
        'PlayThroughs.PlayThroughs[1].DropOnDeathItemPools.ItemPools',
        "((ItemPool=ItemPoolData'{}',PoolProbability=(BaseValueConstant={})))".format(loot_pool[1], 0.01 * legy_count))

    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
        'BPlayThroughs.PlayThroughs[1].DropOnDeathItemPools.ItemPools.ItemPools[0].ItemPool.BalancedItems',
        "({})".format(full_list))
    
    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
        'BPlayThroughs.PlayThroughs[1].DropOnDeathItemPools.ItemPools.ItemPools[0].NumberOfTimesToSelectFromThisPool.BaseValueConstant',
        "{}".format(legy_count))
    
    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
        'PlayThroughs.PlayThroughs[1].bEquipSingleItemFromCollection',
        "False")
    
    '''mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
        'PlayThroughs.PlayThroughs[1]',
        "((AttributeToSetBaseValueOf=GbxAttributeData'/Game/GameData/Attributes/Health/AI_Health/Att_AI_Health_01_Primary_OnIdleRegenerationDelay.Att_AI_Health_01_Primary_OnIdleRegenerationDelay',BaseValue=(BaseValueConstant=15.000000)),(AttributeToSetBaseValueOf=GbxAttributeData'/Game/GameData/Attributes/Health/AI_Health/Att_AI_Health_01_Primary_OnIdleRegenerationRate.Att_AI_Health_01_Primary_OnIdleRegenerationRate',BaseValue=(AttributeInitializer=BlueprintGeneratedClass'/Game/GameData/Balance/HealthAndDamage/Calc/Init_HealthCalc_AI_01_Primary.Init_HealthCalc_AI_01_Primary_C',BaseValueScale=0.200000)))")
    '''
def mob_move_speed(mod, full_list, b_b, spd=1.0, nav=0):
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'NavMovementOptions',
        "(PathingData=(UserEdges=HavokPathFindingData'{}'),IdleDirectionTime=0.25)".format(nav_list[nav]))
    """
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'NavMovementOptions.PathingData.UserEdges.UserEdges[0].Action',
        "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Navigation/ANav_WeeLoaderBadass_Jump.ANav_WeeLoaderBadass_Jump_C'")
    """

        
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'MaxGroundSpeedScale',
        "(BaseValue={})".format(spd))#ground speed scale 
    """
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'FallingFloorTraceDistance',
        "250.0")
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'bCanMove',
        "False")

    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'bBlockMomentumAdd',
        "False")

    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'JumpGoal_Default',
        "(InitialZVelocity=1050,GoalHeight=120,bUseInitialZVelocity=True)")
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'JumpGoal_Sprinting',
        "(InitialZVelocity=950,GoalHeight=120,bUseInitialZVelocity=True)")
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'MaxInjuredSprintSpeed',
        '(BaseValue={})'.format(spd * 2.30))
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'MaxWalkSpeedInjured',
        '(BaseValue={})'.format(spd * 1.25))
    
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'MaxSprintSpeed',
        '(BaseValue={})'.format(spd * 3.2))
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'MaxWalkSpeed',
        '(BaseValue={})'.format(spd))
    
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'MaxSprintAngle',
        "60.0")
    

    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'NavAvoidanceOptions',
        "(bAvoidanceSteering=False,bAvoidPawnsBehindMe=True,bAvoidWithNoGoal=True)")

    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'FallingFloorUpdateInterval',
        "0.1")
    mod.reg_hotfix(Mod.CHAR, '{}'.format(b_b),
        '{}.Default__{}_C:CharMoveComp'.format(full_list,b_b),
        'bCanClimbLadders',
        "True")
    """
def random_color(tp):
        rgbl=["","",""]
        #random.shuffle(rgbl)
        if tp == "H":
                rgbl[0] = "{}".format(Decimal(random.randrange(500,999)*0.001).__round__(3))
                rgbl[1] = "0.0"
                rgbl[2] = "{}".format(Decimal(random.randrange(0,500)*0.001).__round__(3))
        elif tp == "A":
                rgbl[0] = "1.0"
                rgbl[1] = "{}".format(Decimal(random.randrange(650,900)*0.001).__round__(3))
                rgbl[2] = "{}".format(Decimal(random.randrange(50,350)*0.001).__round__(3))
        elif tp == "S":
                rgbl[0] = "{}".format(Decimal(random.randrange(50,450)*0.001).__round__(3))
                rgbl[1] = "{}".format(Decimal(random.randrange(600,999)*0.001).__round__(3))
                rgbl[2] = "1.0"
        
        rgba = '(R={},G={},B={},A=1.0)'.format(rgbl[0],rgbl[1],rgbl[2])
        #print(rgba)
        return rgba
def mob_health_color(mod):
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
            '/Game/GameData/ResourcePools/HealthTypes/HealthType_Flesh.HealthType_Flesh',
            'HealthTypeData.BarBackgroundFrameName',
            'shield')
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
            '/Game/GameData/ResourcePools/HealthTypes/HealthType_Flesh.HealthType_Flesh',
            'HealthTypeData.DisplayColor',
            random_color("H"))
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
            '/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor',
            'HealthTypeData.BarBackgroundFrameName',
            'shield')
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
            '/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor',
            'HealthTypeData.DisplayColor',
            random_color("A"))
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
            '/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield',
            'HealthTypeData.BarBackgroundFrameName',
            'shield')
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
            '/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield',
            'HealthTypeData.DisplayColor',
            random_color("S"))

def mob_health_override(mod,bpchar,last_bit,base_type,c1=0.85,c2=0.6):
        mod.reg_hotfix(Mod.CHAR, last_bit,
                '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
                'PlayThroughs.PlayThroughs[1].bOverrideHealthInformation',
                "True")
        mod.reg_hotfix(Mod.CHAR, last_bit,
                '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
                'PlayThroughs.PlayThroughs[1].HealthInformation',
                "({},{},{})".format(hfull(base_type,0,),hfull(random.randrange(base_type,3),1,c1),hfull(2,2,c2)))

def colision_capsule(mod,bpchar,last_bit,h,r):
    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.Default__{}_C'.format(bpchar, last_bit),
        'CollisionCylinder.CapsuleComponent.CapsuleHalfHeight',
        h,"",True)
    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.Default__{}_C'.format(bpchar, last_bit),
        'CollisionCylinder.CapsuleComponent.CapsuleRadius',
        r,"",True)


def scale_char(mod,bpchar,last_bit,base_scale,scale):                    
    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.Default__{}_C:CharacterMesh0'.format(bpchar, last_bit),
        'RelativeScale3D',
        f'(X={scale * base_scale},Y={scale * base_scale},Z={scale * base_scale})')
    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.Default__{}_C'.format(bpchar, last_bit),
        'PreEnragedActorScale',
        f'(X={scale * base_scale},Y={scale * base_scale},Z={scale * base_scale})')
    mod.reg_hotfix(Mod.CHAR, last_bit,
        '{}.Default__{}_C'.format(bpchar, last_bit),
        'EnragedActorScale',
        f'(X={scale * 0.59 * base_scale},Y={scale * 0.59 * base_scale},Z={scale * 0.59 * base_scale})')

def pre_nerf_test(mod):
        #recursion test
    mod.reg_hotfix(Mod.PATCH, '',
        "/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/LightProjectile_MAL_SG_Recursion.Default__LightProjectile_MAL_SG_Recursion_C",
        'NumRecursions',
        "20")
    #crosroad pre nerf
    mod.reg_hotfix(Mod.PATCH, '',
        "/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Parts/Part_SM_HYP_Barrel_Crossroad.Part_SM_HYP_Barrel_Crossroad",
        'InventoryAttributeEffects.InventoryAttributeEffects[0].ModifierValue.BaseValueConstant',
        "1.15")
    mod.reg_hotfix(Mod.PATCH, '',
        "/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Parts/Part_SM_HYP_Barrel_Crossroad.Part_SM_HYP_Barrel_Crossroad",
        'InventoryAttributeEffects.InventoryAttributeEffects[4].ModifierValue.BaseValueConstant',
        "1.7")
    mod.reg_hotfix(Mod.PATCH, '',
        "/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Parts/Part_SM_HYP_Barrel_Crossroad.Part_SM_HYP_Barrel_Crossroad",
        'InventoryAttributeEffects.InventoryAttributeEffects[2].ModifierValue.BaseValueConstant',
        "4")
    #hex pre
    mod.table_hotfix(Mod.PATCH, '',
        "/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Unique_Balance_Table.GrenadeMod_Unique_Balance_Table",
        "Seeker",
        'Damage_12_F33DA0994756D761207677A51A156787',
        "-0.8")
    mod.table_hotfix(Mod.PATCH, '',
        "/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Unique_Balance_Table.GrenadeMod_Unique_Balance_Table",
        "Seeker",
        'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
        "6.0")
    mod.table_hotfix(Mod.PATCH, '',
        "/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Unique_Balance_Table.GrenadeMod_Unique_Balance_Table",
        "Seeker",
        'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
        "7.0")
    mod.table_hotfix(Mod.PATCH, '',
        "/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Unique_Balance_Table.GrenadeMod_Unique_Balance_Table",
        "Seeker",
        'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
        "8.0")
