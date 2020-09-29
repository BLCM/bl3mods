from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('randomizer_ted.txt',
'Tediore Weapon Randomizer',
'SSpyR',
[
    'One in the set of many randomizer classes.',
    'This one for Tediore. The reason this is by manufacturer',
    'is due to wanting the ability to keep the weapons on save-quit.',
    'In order to meet that only guns of the same Type and Manufacturer can',
    'be randomized with each other. I might make a runtime randomizer of everything',
    'in the future but we are starting here for now.'
],
lic=Mod.CC_BY_SA_40,
)

data=BL3Data()

#SMGs

#List the Balances
smg_bal_name=[
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_01_Common',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_02_UnCommon',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_03_Rare',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_04_VeryRare',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Balance/Balance_SM_TED_Beans',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Balance/Balance_SM_TED_NotAFlamethrower',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Balance/Balance_SM_TED_SpiderMind',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Balance/Balance_SM_TED_TenGallon',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/NeedleGun/Balance/Balance_SM_TED_NeedleGun'
]

#Now the Barrels
smg_barrel=[
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SM_TED_Barrel_01',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SM_TED_Barrel_02',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SM_TED_Barrel_03',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Parts/Part_SM_TED_Barrel_Beans',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Parts/Part_SM_TED_Barrel_NotAFlamethrower',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Parts/Part_SM_TED_Barrel_SpiderMind',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Parts/Part_SM_TED_Barrel_TenGallon',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/NeedleGun/Parts/Part_SM_TED_Barrel_NeedleGun'
]

#Now the Materials
smg_material=[
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Parts/Material/Part_SM_TED_Material_01_Common',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Parts/Material/Part_SM_TED_Material_02_UnCommon',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Parts/Material/Part_SM_TED_Material_03_Rare',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Parts/Material/Part_SM_TED_Material_04_VeryRare',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Parts/Part_SM_TED_Material_Beans',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Parts/Part_SM_TED_Material_NotAFlamethrower',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Parts/Part_SM_TED_Material_SpiderMind',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Parts/Part_SM_TED_Material_TenGallon',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/NeedleGun/Parts/Part_SM_TED_Material_NeedleGun'
]

for bal in smg_bal_name:
    smg_bals=Balance.from_data(data, bal)
    mat_type=len(smg_bals.categories)
    for cat in smg_bals.categories:
        if cat.index==2:
            for barrel in smg_barrel:
                cat.add_part_name(barrel, 1)
                cat.select_multiple=True
                cat.num_min=1
                cat.num_max=3
        if cat.index==mat_type-1:
            for material in smg_material:
                cat.add_part_name(material, 1)
            break
    smg_bals.hotfix_full(mod)


#Shotguns

#List the Balances
shotgun_bal_name=[
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_01_Common',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_02_Uncommon',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/FriendZone/Balance/Balance_SG_TED_FriendZone',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Balance/Balance_SG_TED_Horizon',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Balance/Balance_SG_TED_Polybius',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Balance/Balance_SG_TED_Anarchy',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SacrificalLamb/Balance/Balance_SG_TED_SacrificialLamb'
]

#Now the Barrels
shotgun_barrel=[
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SG_TED_Barrel_01',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SG_TED_Barrel_02',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SG_TED_Barrel_03',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/FriendZone/Parts/Part_SG_TED_Barrel_FriendZone',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Parts/Part_SG_TED_Barrel_Horizon',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Parts/Part_SG_TED_Barrel_Polybius',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Parts/Part_SG_TED_Barrel_Sludge',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Parts/Part_SG_TED_Barrel_Anarchy',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Parts/Part_SG_TED_Barrel_Omen',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SacrificalLamb/Parts/Part_SG_TED_Barrel_SacrificialLamb'
]

#Now the Materials
shotgun_material=[
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Material/Part_SG_TED_Material_01_Common',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Material/Part_SG_TED_Material_02_Uncommon',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Material/Part_SG_TED_Material_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Material/Part_SG_TED_Material_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/FriendZone/Parts/Part_SG_TED_Material_FriendZone',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Parts/Part_SG_TED_Material_Horizon',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Parts/Part_SG_TED_Material_Polybius',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Parts/Part_SG_TED_Material_Sludge',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Parts/Part_SG_TED_Material_Anarchy',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Parts/Part_SG_TED_Material_Omen'
]

for bal in shotgun_bal_name:
    shotgun_bals=Balance.from_data(data, bal)
    mat_type=len(shotgun_bals.categories)
    for cat in shotgun_bals.categories:
        if cat.index==2:
            for barrel in shotgun_barrel:
                cat.add_part_name(barrel, 1)
                cat.select_multiple=True
                cat.num_min=1
                cat.num_max=3
        if cat.index==mat_type-1:
            for material in shotgun_material:
                cat.add_part_name(material, 1)
            break
    shotgun_bals.hotfix_full(mod)


#Pistols

#List the Balances
pistol_bal_name=[
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_01_Common',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_03_Rare',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/_Bangarang/Balance/Balance_PS_TED_Bangerang',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Balance_PS_Tediore_BabyMaker',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Balance/Balance_PS_TED_Gunerang',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute'
]

#Now the Barrels
pistol_barrel=[
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/Parts/Barrels/Barrel_01/Part_PS_TED_Barrel_01',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/Parts/Barrels/Barrel_02/Part_PS_TED_Barrel_02',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/Parts/Barrels/Barrel_03/Part_PS_TED_Barrel_03',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Parts/Part_PS_TED_Barrel_BabyMaker',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Parts/Part_PS_TED_Barrel_Gunerang',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Parts/Part_PS_TED_Barrel_Sabre',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Parts/Part_PS_TED_Barrel_Execute'
]

#Now the Materials
pistol_material=[
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/Parts/Material/Part_PS_TED_Material_01_Common',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/Parts/Material/Part_PS_TED_Material_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/Parts/Material/Part_PS_TED_Material_03_Rare',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/Parts/Material/Part_PS_TED_Material_04_Epic',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/_Bangarang/Part_PS_TED_Material_Bangerang',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Parts/Part_PS_TED_Material_BabyMaker',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Parts/Part_PS_TED_Material_Gunerang',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Parts/Part_PS_TED_Material_Sabre',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Parts/Part_PS_TED_Material_Execute'
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


mod.close()