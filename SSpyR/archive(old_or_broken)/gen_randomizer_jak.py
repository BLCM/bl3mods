from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('randomizer_jak.txt',
'Jakobs Weapon Randomizer',
'SSpyR',
[
    'One in the set of many randomizer classes.',
    'This one for Jakobs. The reason this is by manufacturer',
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
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_02_Uncommon',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Balance/Balance_SR_JAK_Headsplosion',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Balance/Balance_SR_JAK_Monocle',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Balance/Balance_SR_JAK_Hunter',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Hunted/Balance/Balance_SR_JAK_Hunted',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Huntress/Balance/Balance_SR_JAK_Huntress',
    '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/CockyBastard/Balance/Balance_SR_JAK_CockyBastard',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat'
]

#Now the Barrels
sniper_barrel=[
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SR_JAK_Barrel_01',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SR_JAK_Barrel_02',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SR_JAK_Barrel_03',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Parts/Part_SR_JAK_Barrel_Monocle',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Hunted/Part_SR_JAK_Barrel_Hunted',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Huntress/Part_SR_JAK_Barrel_Huntress',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Parts/Part_SR_JAK_Barrel_Hunter'
]

#Now the Materials
sniper_material=[
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Material/Part_SR_JAK_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Material/Part_SR_JAK_02_Uncommon',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Material/Part_SR_JAK_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Material/Part_SR_JAK_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Parts/Part_SR_JAK_Material_Headsplosion',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Parts/Part_SR_JAK_IceQueen',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Parts/Part_SR_JAK_MAT_Monocle',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Parts/Part_SR_JAK_MAterial_Hunter',
    '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Parts/Part_SR_JAK_Mat_WeddingInvite',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/CockyBastard/Parts/Part_SR_JAK_MAT_CockyBastard',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Parts/Part_SR_JAK_MAT_Skullmasher',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Parts/Part_SR_JAK_Material_UnseenThreat'
]

#Now the Bolts
sniper_bolt=[
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Bolt/Part_SR_JAK_Bolt_01',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Bolt/Part_SR_JAK_Bolt_02',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Bolt/Part_SR_JAK_Bolt_03',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Parts/Part_SR_JAK_Bolt_Headsplosion',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Parts/Part_SR_JAK_Bolt_IceQueen',
    '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Parts/Part_SR_JAK_Bolt_WeddingInvite',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/CockyBastard/Parts/Part_SR_JAK_Bolt_CockyBastard',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Parts/Part_SR_JAK_Bolt_Skullmasher',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Parts/Part_SR_JAK_Bolt_UnseenThreat'
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
        if cat.index==5:
            for bolt in sniper_bolt:
                cat.add_part_name(bolt, 1)
        if cat.index==mat_type-1:
            for material in sniper_material:
                cat.add_part_name(material, 1)
            break
    sniper_bals.hotfix_full(mod)


#Shotguns

#List the Balances
shotgun_bal_name=[
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_01_Common',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_02_UnCommon',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Balance/Balance_SG_JAK_Garcia',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Balance/Balance_SG_JAK_Hellwalker',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Balance/Balance_SG_JAK_Nimble',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/OnePunch/Balance/Balance_SG_JAK_OnePunch',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Balance/Balance_SG_JAK_LGD_Sledge',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/Balance_SG_JAK_Fingerbiter',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Balance/Balance_SG_JAK_Unique_Wave',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheCure/Balance/Balance_SG_JAK_TheCure'
]

#Now the Barrels
shotgun_barrel=[
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SG_JAK_Barrel_01',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SG_JAK_Barrel_02',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SG_JAK_Barrel_03',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Parts/Part_SG_JAK_Barrel_Garcia',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Parts/Part_SG_JAK_Barrel_Hellwalker',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Parts/Part_SG_JAK_Barrel_Nimble',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/OnePunch/Parts/Part_SG_JAK_Barrel_OnePunch',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Parts/Part_SG_JAK_Barrel_Sledge',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Parts/Part_SG_JAK_Barrel_TidalWave',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Parts/Part_SG_JAK_Barrel_TKWave',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheCure/Parts/Part_SG_JAK_Barrel_TheCure'
]

#Now the Materials
shotgun_material=[
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Material/Part_SG_JAK_Material_01_Common',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Material/Part_SG_JAK_Material_02_UnCommon',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Material/Part_SG_JAK_Material_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Material/Part_SG_JAK_Material_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Parts/Part_SG_JAK_Material_Garcia',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Parts/Part_SG_JAK_Material_Hellwalker',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Parts/Part_SG_JAK_Material_Nimble',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/OnePunch/Parts/Part_SG_JAK_Material_OnePunch',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Parts/Part_SG_JAK_Material_LGD_Sledge',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Parts/Part_SG_JAK_Material_Fingerbiter',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheCure/Parts/Part_SG_JAK_Material_TheCure'
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
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_01_Common',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_03_Rare',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AureliaBackup/Balance/Balance_PS_JAK_AureliaPistol',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/Balance_PS_JAK_Buttplug',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/GodMother/Balance/Balance_PS_JAK_GodMother',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Balance/Balance_PS_JAK_Malevolent',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Balance/Balance_PS_JAK_MelsCompanion',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Balance_PS_JAK_SpyRevolver',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Balance/Balance_PS_JAK_TheDuc',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TortureTruck/Balance_PS_JAK_TortureTruck',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Balance/Balance_PS_JAK_Unforgiven',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Balance/Balance_PS_JAK_WagonWheel',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Balance/Balance_PS_JAK_Lucky7',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/BiteSize/Balance/Balance_PS_JAK_BiteSize',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LittleYeeti/Balance/Balance_PS_JAK_LittleYeeti',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill_Legendary',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Balance/Balance_PS_JAK_SeventhSense',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Balance/Balance_PS_JAK_SS_L',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Balance/Balance_PS_JAK_TheSeventhSense'
]

#Now the Barrels
pistol_barrel=[
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_JAK_Barrel_01',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_JAK_Barrel_02',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_JAK_Barrel_03',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Parts/Part_PS_JAK_Barrel_AmazingGrace',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Parts/Part_PS_JAK_Barrel_Buttplug',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Parts/Part_PS_JAK_Barrel_Doc',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/GodMother/Parts/Part_PS_JAK_Barrel_GodMother',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Parts/Part_PS_JAK_Barrel_Maggie',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Parts/Part_PS_JAK_Barrel_Malevolent',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Parts/Part_PS_JAK_Barrel_MelsCompanion',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Part_PS_JAK_Barrel_SpyRevolver',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Parts/Part_PS_JAK_Barrel_TheDuc',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Parts/Part_PS_JAK_Barrel_Unforgiven',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Parts/Part_PS_JAK_Barrel_WagonWheel',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Parts/Part_PS_JAK_Barrel_RoboMasher',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Parts/Part_PS_JAK_Barrel_Lucky7',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/BiteSize/Parts/Part_PS_JAK_Barrel_BiteSize',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LittleYeeti/Parts/Part_PS_JAK_Barrel_02_LittleYeeti',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Legendary/Parts/Part_PS_JAK_Barrel_LoveDrill_Legendary',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Parts/Part_PS_JAK_Barrel_LoveDrill',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Parts/Part_PS_JAK_Barrel_SeventhGhost',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Parts/Part_PS_JAK_Barrel_SS_L',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Parts/Part_PS_JAK_Barrel_TheSeventhSense'
]

#Now the Materials
pistol_material=[
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Material/Part_PS_JAK_Material_01_Common',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Material/Part_PS_JAK_Material_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Material/Part_PS_JAK_Material_03_Rare',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Material/Part_PS_JAK_Material_04_Epic',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Parts/Part_PS_JAK_Material_AmazingGrace',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Parts/Part_PS_JAK_Material_Buttplug',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Parts/Part_PS_JAK_Material_Doc',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/GodMother/Parts/Part_PS_JAK_Material_GodMother',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Parts/Part_PS_JAK_Material_Maggie',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Parts/Part_PS_JAK_Material_Malevolent',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Parts/Part_PS_JAK_Material_MelsCompanion',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Part_PS_JAK_Material_SpyRevolver',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Parts/Part_PS_JAK_Material_TheDuc',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Parts/Part_PS_JAK_Material_Unforgiven',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Parts/Part_PS_JAK_Material_WagonWheel',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Parts/Part_PS_JAK_Material_RoboMasher',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Parts/Part_PS_JAK_Material_Lucky7',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/BiteSize/Parts/Part_PS_JAK_Material_BiteSize',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LittleYeeti/Parts/Part_PS_JAK_Material_LittleYeeti',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Legendary/Parts/Part_PS_JAK_Material_LoveDrill_Legendary',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Parts/Part_PS_JAK_Material_LoveDrill',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Parts/Part_PS_JAK_Material_SeventhSense',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Parts/Part_PS_JAK_Material_SS_L',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Parts/Part_PS_JAK_Material_TheSeventhSense'
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
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Balance/Balance_AR_JAK_Bekah',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Balance/Balance_AR_JAK_04_GatlingGun',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/Balance_AR_JAK_HandOfGlory',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Balance/Balance_AR_JAK_LeadSprinkler',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/Balance_AR_JAK_PasRifle',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Balance/Balance_AR_JAK_RowansCall',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/Balance_AR_JAK_TraitorsDeath',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant'
]

#Now the Barrels
ar_barrel=[
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_AR_JAK_Barrel_01',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_02/Part_AR_JAK_Barrel_02',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_03/Part_AR_JAK_Barrel_03',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Parts/Part_AR_JAK_Barrel_Bekah',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Parts/Part_AR_JAK_Barrel_GatlingGun',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Parts/Part_AR_JAK_Barrel_HandOfGlory',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Parts/Part_AR_JAK_Barrel_LeadSprinkler',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Parts/Part_AR_JAK_Barrel_PasRifle',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Parts/Part_AR_JAK_Barrel_RowansCall',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Parts/Part_AR_JAK_Barrel_TraitorsDeath',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Parts/Part_AR_JAK_Barrel_01_Clairvoyance',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Parts/Part_AR_JAK_Barrel_Mutant'
]

#Now the Materials
ar_material=[
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Parts/Material/Part_AR_JAK_Material_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Parts/Material/Part_AR_JAK_Material_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Parts/Material/Part_AR_JAK_Material_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Parts/Material/Part_AR_JAK_Material_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Parts/Part_AR_JAK_Material_Bekah',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Parts/Part_AR_JAK_Material_GatlingGun',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Parts/Part_AR_JAK_Material_HandOfGlory',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Parts/Part_AR_JAK_Material_LeadSprinkler',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Parts/Part_AR_JAK_Material_PasRifle',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Parts/Part_AR_JAK_Material_RowansCall',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Parts/Part_AR_JAK_Material_TraitorsDeath',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Parts/Part_AR_JAK_Material_Clairvoyance',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Parts/Part_AR_JAK_Material_Mutant'
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


mod.close()