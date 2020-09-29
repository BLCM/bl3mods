rom bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

#Might do auto barrel and material stuff? otherwise fill out later

mod=Mod('randomizer_hyp.txt',
'Hyperion Weapon Randomizer',
'SSpyR',
[
    'One in the set of many randomizer classes.',
    'This one for Hyperion. The reason this is by manufacturer',
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
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_01_Common',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_02_UnCommon',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_03_Rare',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_04_VeryRare',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Bitch/Balance/Balance_SM_HYP_Bitch',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Balance/Balance_SM_HYP_Crossroad',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Fork/Balance/Balance_SM_HYP_Fork',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Handsome/Balance/Balance_SM_HYP_Handsome',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/L0V3M4CH1N3/Balance/Balance_SM_HYP_L0V3M4CH1N3',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/PredatoryLending/Balance/Balance_SM_HYP_PredatoryLending',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/XZ/Balance/Balance_SM_HYP_XZ',
    '/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/CheapTips/Balance/Balance_SM_HYP_CheapTips',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian',
    '/Game/PatchDLC/Steam/Gear/Weapons/SteamGun/Balance/Balance_SM_HYP_ShortStick',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/Pricker/Balance/Balance_SM_HYP_Pricker'
]

#Now the Barrels
smg_barrel=[

]

#Now the Materials
smg_material=[

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
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_02_Uncommon',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/MasterworkCrossbow/Balance/Balance_SR_HYP_Masterwork',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/Balance_SR_HYP_TwoTime',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/Woodblocks/Balance/Balance_SR_HYP_Woodblocks',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman'
]

#Now the Barrels
sniper_barrel=[

]

#Now the Materials
sniper_material=[

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
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_01_Common',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_02_Uncommon',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Brick/Balance/Balance_SG_HYP_Brick',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Balance/Balance_SG_HYP_ConferenceCall',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Phebert/Balance/Balance_SG_HYP_Phebert',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Redistributor/Balance/Balance_SG_HYP_Redistributor',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/TheButcher/Balance/Balance_SG_HYP_TheButcher',
    '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Fearmonger/Balance/Balance_SG_HYP_ETech_Fearmonger',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/MeltFacer/Balance/Balance_SG_HYP_MeltFacer',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/HeartBreaker/Balance/Balance_SG_HYP_HeartBreaker',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/SlowHand/Balance/Balance_SG_HYP_SlowHand',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Firecracker/Balance/Balance_SG_HYP_Firecracker',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IceBurger/Balance/Balance_SG_HYP_IceBurger',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Reflux/Balance/Balance_SG_HYP_Reflux'
]

#Now the Barrels
shotgun_barrel=[

]

#Now the Materials
shotgun_material=[

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


mod.close()