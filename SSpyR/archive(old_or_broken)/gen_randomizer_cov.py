from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('randomizer_cov.txt',
'CoV Weapon Randomizer',
'SSpyR',
[
    'One in the set of many randomizer classes.',
    'This one for CoV. The reason this is by manufacturer',
    'is due to wanting the ability to keep the weapons on save-quit.',
    'In order to meet that only guns of the same Type and Manufacturer can',
    'be randomized with each other. I might make a runtime randomizer of everything',
    'in the future but we are starting here for now.'
],
lic=Mod.CC_BY_SA_40,
)

data=BL3Data()

#Pistols

#List the Balances
pistol_bal_name=[
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_01_Common',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_02_Uncommon',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_03_Rare',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/Balance_PS_COV_Chad',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Balance/Balance_PS_COV_Legion',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/Balance_PS_COV_Mouthpiece',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Balance/Balance_PS_COV_PsychoStabber',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Balance/Balance_PS_COV_Skeksis',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Hydrafrost/Balance/Balance_PS_COV_Hydrafrost'
]

#Now the Barrels
pistol_barrel=[
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_COV_Barrel_01',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_COV_Barrel_02',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_COV_Barrel_03',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Parts/Part_PS_COV_Barrel_Chad',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Parts/Part_PS_COV_Barrel_Contagion',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Parts/Part_PS_COV_Barrel_Legion',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Parts/Part_PS_COV_Barrel_Mouthpiece',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Parts/Part_PS_COV_Barrel_PsychoStabber',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Parts/Part_PS_COV_Barrel_Skeksis',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Hydrafrost/Parts/Part_PS_COV_Barrel_Hydrafrost'
]

#Now the Materials
pistol_material=[
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_PS_COV_Material_01_Common',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_PS_COV_Material_02_Uncommon',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_PS_COV_Material_03_Rare',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_PS_COV_Material_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Parts/Part_PS_COV_Material_Chad',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Parts/Part_PS_COV_Material_Contagion',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Parts/Part_PS_COV_Material_Legion',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Parts/Part_PS_COV_Material_Mouthpiece',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Parts/Part_PS_COV_Material_PsychoStabber',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Parts/Part_PS_COV_Material_Skeksis',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Hydrafrost/Parts/Part_PS_COV_Material_Hydrafrost'
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
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Balance/Balance_AR_COV_Sawbar',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/PewPew/Balance/Balance_AR_COV_PewPew'
]

#Now the Barrels
ar_barrel=[
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_01/Part_AR_COV_Barrel_01',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_02/Part_AR_COV_Barrel_02',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_03/Part_AR_COV_Barrel_03',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Damage/Part_AR_COV_Barrel_HeatDamage',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/FireRate/Part_AR_COV_Barrel_HeatFirerate',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Parts/Part_AR_COV_Barrel_Sawbar',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Parts/Part_AR_COV_Barrel_Zheitsev',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Parts/Part_AR_COV_Barrel_Homicidal',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Parts/Part_AR_COV_Barrel_SparkyBoom',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/PewPew/Parts/Part_AR_COV_Barrel_PewPew'
]

#Now the Materials
ar_material=[
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_AR_COV_Material_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_AR_COV_Material_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_AR_COV_Material_03_rare',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_AR_COV_Material_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Part_AR_COV_Material_KriegAR',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Parts/Part_AR_COV_Material_Sawbar',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Parts/Part_AR_COV_Material_Zheitsev',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Parts/Part_AR_COV_Material_Homicidal',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Parts/Part_AR_COV_Material_SparkyBoom',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/PewPew/Parts/Part_AR_COV_Material_PewPew'
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
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_01_Common',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_02_UnCommon',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_03_rare',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_04_VeryRare',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Balance/Balance_HW_COV_HotDrop',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/Balance_HW_COV_PortaPooper',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/YellowCake/Balance/Balance_HW_COV_ETech_YellowCake'
]

#Now the Barrels
heavy_barrel=[
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_01/Part_HW_COV_Barrel_01',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_02/Part_HW_COV_Barrel_02',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_03/Part_HW_COV_Barrel_03',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Parts/Part_HW_COV_Barrel_HotDrop',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Part/Part_HW_COV_Barrel_PortaPooper',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Parts/Part_HW_COV_Barrel_Terror',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/YellowCake/Parts/Part_HW_COV_Barrel_ETech_YellowCake'
]

#Now the Materials
heavy_material=[
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_HW_COV_Material_01_Common',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_HW_COV_Material_02_Uncommon',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_HW_COV_Material_03_Rare',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Parts/Material/Part_HW_COV_Material_04_VeryRare',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Parts/Part_HW_COV_Material_HotDrop',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Part/Part_HW_COV_Material_PortaPooper',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Parts/Part_HW_COV_Material_Terror'
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