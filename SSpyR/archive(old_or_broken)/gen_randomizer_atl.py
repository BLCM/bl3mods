from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('randomizer_atl.txt',
'Atlas Weapon Randomizer',
'SSpyR',
[
    'One in the set of many randomizer classes.',
    'This one for Atlas. The reason this is by manufacturer',
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
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_01_Common',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_03_Rare',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Balance/Balance_PS_ATL_Drill',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/Balance_PS_ATL_Warmonger',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Balance/Balance_PS_ATL_DoubleTap'
]

#Now the Barrels
pistol_barrel=[
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_ATL_Barrel_01',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_ATL_Barrel_02',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_ATL_Barrel_03',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Parts/Part_PS_ATL_Barrel_Drill',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Parts/Part_PS_ATL_Barrel_Warmonger',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Parts/Part_PS_ATL_Barrel_DoubleTap'
]

#Now the Materials
pistol_material=[
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Parts/Material/Part_PS_ATL_Material_01_Common',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Parts/Material/Part_PS_ATL_Material_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Parts/Material/Part_PS_ATL_Material_03_Rare',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Parts/Material/Part_PS_ATL_Material_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Parts/Part_PS_ATL_Material_Drill',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Parts/Part_PS_ATL_Material_Warmonger',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Parts/Part_PS_ATL_Material_DoubleTap'
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
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/Balance_ATL_AR_Carrier',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Balance/Balance_ATL_AR_RebelYell',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Portal/Balance/Balance_ATL_AR_Portals',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Balance/Balance_ATL_AR_OPQ'
]

#Now the Barrels
ar_barrel=[
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Parts/Barrel/Barrel_01/Part_AR_ATL_Barrel_01',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Parts/Barrel/Barrel_02/Part_AR_ATL_Barrel_02',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Parts/Barrel/Barrel_03/Part_AR_ATL_Barrel_03',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Parts/Part_AR_ATL_Barrel_Carrier',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Parts/Part_AR_ATL_Barrel_RebelYell',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Portal/Parts/Part_AR_ATL_Barrel_Portals',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Parts/Part_AR_ATL_Barrel_OPQ'
]

#Now the Materials
ar_material=[
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Parts/Material/Part_AR_ATL_Material_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Parts/Material/Part_AR_ATL_Material_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Parts/Material/Part_AR_ATL_Material_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Parts/Material/Part_AR_ATL_Material_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Parts/Part_AR_ATL_Material_Carrier',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Parts/Part_AR_ATL_Material_RebelYell',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Portal/Parts/Part_AR_ATL_Material_Portals',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Parts/Part_AR_ATL_Material_OPQ'
]

#Now the Trackers
ar_tracker=[
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Parts/Tracker/Part_AR_ATL_Tracker_01',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Parts/Tracker/Part_AR_ATL_Tracker_02',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Parts/Tracker/Part_AR_ATL_Tracker_03',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Parts/Part_AR_ATL_Tracker_RebelYell',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Parts/Part_AR_ATL_Tracker_OPQ'
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
        if cat.index==4:
            for tracker in ar_tracker:
                cat.add_part_name(tracker, 1)
        if cat.index==mat_type-1:
            for material in ar_material:
                cat.add_part_name(material, 1)
            break
    ar_bals.hotfix_full(mod)


#Heavy

#List the Balances
heavy_bal_name=[
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_01_Common',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_02_UnCommon',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_03_Rare',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_04_VeryRare',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Balance/Balance_HW_ATL_Freeman',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Balance/Balance_HW_ATL_RubysWrath'
]

#Now the Barrels
heavy_barrel=[
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/Parts/Barrel/Barrel_01/Part_ATL_Barrel_01',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/Parts/Barrel/Barrel_02/Part_ATL_Barrel_02',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/Parts/Barrel/Barrel_03/Part_ATL_Barrel_03',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Parts/Part_ATL_Barrel_Freeman',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Parts/Part_ATL_Barrel_RubysWrath'
]

#Now the Materials
heavy_material=[
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/Parts/Material/Part_ATL_Material_01_Common',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/Parts/Material/Part_ATL_Material_02_Uncommon',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/Parts/Material/Part_ATL_Material_03_Rare',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/Parts/Material/Part_ATL_Material_04_VeryRare',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Parts/Part_ATL_Material_Freeman',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Parts/Part_ATL_Material_RubysWrath'
]

#Now the Trackers
heavy_tracker=[
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/Parts/Marker/Part_ATL_Marker_01',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/Parts/Marker/Part_ATL_Marker_02',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/Parts/Marker/Part_ATL_Marker_03',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Parts/Part_ATL_Marker_Freeman',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Parts/Part_ATL_Marker_RubysWrath'
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
        if cat.index==4:
            for tracker in heavy_tracker:
                cat.add_part_name(tracker, 1)
        if cat.index==mat_type-1:
            for material in heavy_material:
                cat.add_part_name(material, 1)
            break
    heavy_bals.hotfix_full(mod)


mod.close()