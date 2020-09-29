from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('randomizer_vla.txt',
'Vladof Weapon Randomizer',
'SSpyR',
[
    'One in the set of many randomizer classes.',
    'This one for Vladof. The reason this is by manufacturer',
    'is due to wanting the ability to keep the weapons on save-quit.',
    'In order to meet that only guns of the same Type and Manufacturer can',
    'be randomized with each other. I might make a runtime randomizer of everything',
    'in the future but we are starting here for now.'
],
lic=Mod.CC_BY_SA_40,
)

data=BL3Data()

#Snipers

#List the Balances
sniper_bal_name=[
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_02_UnCommon',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Balance/Balance_VLA_SR_Lyuda',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/Balance_VLA_SR_Prison'
]

#Now the Barrels
sniper_barrel=[
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SR_VLA_Barrel_01',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SR_VLA_Barrel_02',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SR_VLA_Barrel_03',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Parts/Part_SR_VLA_Barrel_Lyuda',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Parts/Part_SR_VLA_Barrel_Prison'
]

#Now the Materials
sniper_material=[
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Parts/Material/Part_SR_VLA_Material_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Parts/Material/Part_SR_VLA_Material_02_Uncommon',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Parts/Material/Part_SR_VLA_Material_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Parts/Material/Part_SR_VLA_Material_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Parts/Part_SR_VLA_Material_Lyuda',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Parts/Part_SR_VLA_Material_Prison'
]

for bal in sniper_bal_name:
    sniper_bals=Balance.from_data(data, bal)
    mat_type=len(sniper_bals.categories)
    for cat in sniper_bals.categories:
        if cat.index==2:
            for barrel in sniper_barrel:
                cat.add_part_name(barrel, 1)
                cat.select_multiple=True
                cat.num_min=1
                cat.num_max=3
        if cat.index==mat_type-1:
            for material in sniper_material:
                cat.add_part_name(material, 1)
            break
    sniper_bals.hotfix_full(mod)


#Pistols

#List the Balances
pistol_bal_name=[
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_01_Common',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_03_Rare',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Balance/Balance_PS_VLA_BoneShredder',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Balance/Balance_PS_VLA_Infiniti',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech'
]

#Now the Barrels
pistol_barrel=[
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/Parts/Barrels/Barrel_01/Part_PS_VLA_Barrel_01',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/Parts/Barrels/Barrel_02/Part_PS_VLA_Barrel_02',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/Parts/Barrels/Barrel_03/Part_PS_VLA_Barrel_03',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Parts/Part_PS_VLA_Barrel_BoneShredder',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Parts/Part_PS_VLA_Barrel_Infiniti',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Parts/Part_PS_VLA_Barrel_Magnificent',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Parts/Part_PS_VLA_Underbarrel_TheLeech'
]

#Now the Materials
pistol_material=[
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/Parts/Material/Part_PS_VLA_Material_01_Common',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/Parts/Material/Part_PS_VLA_Material_02_Uncommon',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/Parts/Material/Part_PS_VLA_Material_03_Rare',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/Parts/Material/Part_PS_VLA_Material_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Parts/Part_PS_VLA_Material_BoneShredder',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Parts/Part_PS_VLA_Material_Infiniti',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Parts/Part_PS_VLA_Material_Magnificent',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Parts/Part_PS_VLA_Material_TheLeech'
]

for bal in pistol_bal_name:
    pistol_bals=Balance.from_data(data, bal)
    mat_type=len(pistol_bals.categories)
    for cat in pistol_bals.categories:
        if cat.index==2:
            for barrel in pistol_barrel:
                cat.add_part_name(barrel, 1)
                cat.select_multiple=True
                cat.num_min=1
                cat.num_max=3
        if cat.index==mat_type-1:
            for material in pistol_material:
                cat.add_part_name(material, 1)
            break
    pistol_bals.hotfix_full(mod)


#ARs

#List the Balances
ar_bal_name=[
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Balance_AR_VLA_BigSucc',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Balance/Balance_AR_VLA_Damn',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Balance/Balance_AR_VLA_Dictator',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Balance/Balance_AR_VLA_Faisor',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Balance/Balance_AR_VLA_LuciansCall',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Balance/Balance_AR_VLA_Ogre',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Balance/Balance_AR_VLA_Sherdifier',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch'
]

#Now the Barrels
ar_barrel=[
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/Parts/Barrel/Barrel_01/Part_AR_VLA_Barrel_01',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/Parts/Barrel/Barrel_02/Part_AR_VLA_Barrel_02',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/Parts/Barrel/Barrel_03/Part_AR_VLA_Barrel_03',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Parts/Part_AR_VLA_Barrel_Damn',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Parts/Part_AR_VLA_Barrel_Dictator',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Parts/Part_AR_VLA_Barrel_Faisor',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Parts/Part_AR_VLA_Barrel_LuciansCall',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Parts/Part_AR_VLA_Barrel_Ogre',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Parts/Part_AR_VLA_Barrel_Shredifier',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Parts/Part_AR_VLA_Underbarrel_Sickle',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Parts/Part_AR_VLA_Barrel_Monarch'
]

#Now the Materials
ar_material=[
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/Parts/Material/Part_AR_VLA_Material_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/Parts/Material/Part_AR_VLA_Material_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/Parts/Material/Part_AR_VLA_Material_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/Parts/Material/Part_AR_VLA_Material_04_Epic',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Part_AR_VLA_Material_BigSucc',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Parts/Part_AR_VLA_Material_Damn',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Parts/Part_AR_VLA_Material_Dictator',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Parts/Part_AR_VLA_Material_Faisor',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Parts/Part_AR_VLA_Material_LuciansCall',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Parts/Part_AR_VLA_Material_Ogre',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Parts/Part_AR_VLA_Material_Shredifier',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Parts/Part_AR_VLA_Material_Sickel',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Parts/Part_AR_VLA_Material_Monarch'
]

for bal in ar_bal_name:
    ar_bals=Balance.from_data(data, bal)
    mat_type=len(ar_bals.categories)
    for cat in ar_bals.categories:
        if cat.index==2:
            for barrel in ar_barrel:
                cat.add_part_name(barrel, 1)
                cat.select_multiple=True
                cat.num_min=1
                cat.num_max=3
        if cat.index==mat_type-1:
            for material in ar_material:
                cat.add_part_name(material, 1)
            break
    ar_bals.hotfix_full(mod)


#Heavy

#List the Balances
heavy_bal_name=[
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_01_Common',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_02_Uncommon',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_03_Rare',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_04_VeryRare',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Balance/Balance_HW_VLA_CloudBurst',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Balance/Balance_HW_VLA_IonCannon',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner'
]

#Now the Barrels
heavy_barrel=[
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Parts/Barrel/Barrel_01/Part_HW_VLA_Barrel_01',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Parts/Barrel/Barrel_02/Part_HW_VLA_Barrel_02',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Parts/Barrel/Barrel_03/Part_HW_VLA_Barrel_03',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Parts/Part_HW_VLA_Barrel_CloudBurst',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Parts/Part_HW_VLA_Barrel_Mongol',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Parts/Part_HW_VLA_Barrel_IonCannon',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Parts/Part_HW_VLA_Barrel_ETech_BackBurner'
]

#Now the Materials
heavy_material=[
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Parts/Material/Part_HW_VLA_Material_01_Common',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Parts/Material/Part_HW_VLA_Material_02_Uncommon',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Parts/Material/Part_HW_VLA_Material_03_Rare',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Parts/Material/Part_HW_VLA_Material_04_VeryRare',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Parts/Part_HW_VLA_Material_CloudBurst',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Parts/Part_HW_VLA_Material_Mongol',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Parts/Part_HW_VLA_Material_IonCannon',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Parts/Part_HW_VLA_Material_BackBurner'
]

for bal in heavy_bal_name:
    heavy_bals=Balance.from_data(data, bal)
    mat_type=len(heavy_bals.categories)
    for cat in heavy_bals.categories:
        if cat.index==2:
            for barrel in heavy_barrel:
                cat.add_part_name(barrel, 1)
                cat.select_multiple=True
                cat.num_min=1
                cat.num_max=3
        if cat.index==mat_type-1:
            for material in heavy_material:
                cat.add_part_name(material, 1)
            break
    heavy_bals.hotfix_full(mod)


mod.close()