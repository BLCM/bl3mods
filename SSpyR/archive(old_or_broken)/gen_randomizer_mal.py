from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

#First one so notes go here
#Barrel is PartType 2 (index)
#Material is last PartType (index length - 1?)
#Will have to see if this pattern stays true (Barrel should)
#Create lists, iterate through with double for loops to add to each gun (should be straightforward)

mod=Mod('randomizer_mal.txt',
'Maliwan Weapon Randomizer',
'SSpyR',
[
    'One in the set of many randomizer classes.',
    'This one for Maliwan. The reason this is by manufacturer',
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
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_01_Common',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_02_Uncommon',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_03_Rare',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_04_VeryRare',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun',
    '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth',
    '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Balance/Balance_SM_MAL_EmbersPurge',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Balance/Balance_SM_MAL_IonLaser',
    '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Balance/Balance_SM_MAL_SFForce'
]

#Now the Barrels
smg_barrel=[
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SM_MAL_Barrel_01',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SM_MAL_Barrel_02',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SM_MAL_Barrel_03',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Parts/Part_SM_MAL_Barrel_CloudKill',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Parts/Part_SM_MAL_Barrel_Crit',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Parts/Part_SM_MAL_Barrel_Cutsman',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Part/Part_SM_MAL_Barrel_DestructoSpin',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Parts/Part_SM_MAL_Barrel_Devoted',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Parts/Part_SM_MAL_Barrel_Egon',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Parts/Part_SM_MAL_Barrel_Emporer',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Parts/Part_SM_MAL_Barrel_Tsunami',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Parts/Part_SM_MAL_Barrel_VibraPulse',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Parts/Part_SM_MAL_Barrel_westergun',
    '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Parts/Part_SM_MAL_Barrel_KybsWorth',
    '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Parts/Part_SM_MAL_Barrel_Link',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Parts/Part_SM_MAL_Barrel_EmbersPurge',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Parts/Part_SM_MAL_Barrel_IonLaser',
    '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Parts/Part_SM_MAL_Barrel_01_PolyAim',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Parts/Part_SM_MAL_Barrel_SFForce'
]

#Now the Materials
smg_material=[
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Material/Part_SM_MAL_Material_01_Common',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Material/Part_SM_MAL_Material_02_Uncommon',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Material/Part_SM_MAL_Material_03_Rare',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Material/Part_SM_MAL_Material_04_Epic',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Parts/Part_SM_MAL_Material_CloudKill',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Parts/Part_SM_MAL_Material_Crit',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Parts/Part_SM_MAL_Material_Cutsman',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Part/Part_SM_MAL_Material_DestructoSpin',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Parts/Part_SM_MAL_Material_Devoted',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Part_SM_MAL_Material_E3',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Parts/Part_SM_MAL_Material_Egon',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Parts/Part_SM_MAL_Material_Emporer',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Parts/Part_SM_MAL_Material_Kevins',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Parts/Part_SM_MAL_Material_Tsunami',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Parts/Part_SM_MAL_Material_VibraPulse',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Parts/Part_SM_MAL_Material_westergun',
    '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Parts/Part_SM_MAL_Material_KybsWorth',
    '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Parts/Part_SM_MAL_Material_Link',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Parts/Part_SM_MAL_Material_EmbersPurge',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Parts/Part_SM_MAL_Material_IonLaser',
    '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Parts/Part_SM_MAL_Material_PolyAim',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Parts/Part_SM_MAL_Material_SFforce'
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



#Snipers

#List the Balances
sniper_bal_name=[
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_02_UnCommon',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm'
]

#Now the Barrels
sniper_barrel=[
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Barrel_ASMD',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Parts/Part_MAL_SR_Barrel_Krakatoa',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Parts/Part_MAL_SR_Barrel_Soleki',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Parts/Part_MAL_SR_Barrel_FireStorm',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Parts/Part_MAL_SR_Barrel_Storm'
]

#Now the Materials
sniper_material=[
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Material/Part_MAL_SR_Material_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Material/Part_MAL_SR_Material_02_UnCommon',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Material/Part_MAL_SR_Material_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Material/Part_MAL_SR_Material_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Material_ASMD',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Parts/Part_MAL_SR_Material_Krakatoa',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Parts/Part_MAL_SR_Material_Soleki',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Parts/Part_MAL_SR_Material_LGD_FireStorm',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Parts/Part_MAL_SR_Material_LGD_Storm'
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


#Shotguns

#List the Balances
shotgun_bal_name=[
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_01_Common',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_02_Uncommon',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Balance/Balance_SG_MAL_Mouthpiece2',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing'
]

#Now the Barrels
shotgun_barrel=[
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SG_MAL_Barrel_01',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SG_MAL_Barrel_02',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SG_MAL_Barrel_03',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Parts/Part_SG_MAL_Barrel_Mouthpiece2',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Parts/Part_SG_MAL_Barrel_Recursion',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Parts/Part_SG_MAL_Barrel_Shriek',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Parts/Part_SG_MAL_Barrel_Trev',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Parts/Part_SG_MAL_Barrel_Wisp',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Parts/Part_SG_MAL_Barrel_DeathGrip',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Parts/Part_SG_MAL_Barrel_Insider',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Parts/Part_SG_MAL_Barrel_TheNothing'
]

#Now the Materials
shotgun_material=[
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Material/Part_SG_MAL_Material_01_Common',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Material/Part_SG_MAL_Material_02_UnCommon',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Material/Part_SG_MAL_Material_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Material/Part_SG_MAL_Material_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Parts/Part_SG_MAL_Material_Mouthpiece2',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Parts/Part_SG_MAL_Material_Recursion',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Parts/Part_SG_MAL_Material_Shriek',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Parts/Part_SG_MAL_Material_Trev',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Parts/Part_SG_MAL_Material_Wisp',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Parts/Part_SG_MAL_Material_DeathGrip',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Parts/Part_SG_MAL_Material_Insider',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Parts/Part_SG_MAL_Material_TheNothing'
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
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_01_Common',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_03_Rare',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Balance/Balance_PS_MAL_FrozenDevil',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Balance/Balance_PS_MAL_GreaseTrap'
]

#Now the Barrels
pistol_barrel=[
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_MAL_Barrel_01',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_MAL_Barrel_02',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_MAL_Barrel_03',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Parts/Part_PS_MAL_Barrel_HellShock',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Parts/Part_PS_MAL_Barrel_HyperHydrator',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Parts/Part_PS_MAL_Barrel_Plumber',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Parts/Part_PS_MAL_Barrel_Starkiller',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Parts/Part_PS_MAL_Barrel_SuckerPunch',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Parts/Part_PS_MAL_Barrel_ThunderballFists',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Parts/Part_PS_MAL_Barrel_FrozenDevil',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Parts/Part_PS_MAL_Barrel_GreaseTrap'
]

#Now the Materials
pistol_material=[
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Material/Part_PS_MAL_Material_01_Common',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Material/Part_PS_MAL_Material_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Material/Part_PS_MAL_Material_03_Rare',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Material/Part_PS_MAL_Material_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Parts/Part_PS_MAL_Material_Hellshock',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Parts/Part_PS_MAL_Material_HyperHydrator',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Parts/Part_PS_MAL_Material_Plumber',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Parts/Part_PS_MAL_Material_Starkiller',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Parts/Part_PS_MAL_Material_SuckerPunch',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Parts/Part_PS_MAL_Material_ThunderballFists',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Parts/Part_PS_MAL_Material_FrozenDevil',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Parts/Part_PS_MAL_Material_GreaseTrap'
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
