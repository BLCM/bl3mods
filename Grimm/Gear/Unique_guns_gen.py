from bl3hotfixmod import Mod

mod=Mod('Unique_guns.bl3hotfix',
'Unique guns damage',
'Grimm',
[
    'Rebalance of all unique guns in BL3.',
    'Trash guns were buffed whereas great guns were nerfed.',
    'This bring the balance closer as a whole.',
    'Thanks to CodyCode, SsPyR, Apocalyptech, 10 FPS, HackerSmasher, FromDarkHell, Apple1417'
],
lic=Mod.CC_BY_SA_40,
)

atlas='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_ATL'
cov='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_COV'
dalh='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_DAL'
hyperion='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_HYP'
jakobs='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_JAK'
maliwan='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_MAL'
tediore='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_TED'
torgue='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_TOR'
vladof='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_VLA'
mind='/Game/PatchDLC/Alisma/Gear/Weapon/DataTable_WeaponBalance_Alisma'
jackpot='/Game/PatchDLC/Dandelion/Gear/Weapon/DataTable_WeaponBalance_Dandelion'
cartel='/Game/PatchDLC/Event2/Gear/Weapon/DataTable_WeaponBalance_Event2'
valentines='/Game/PatchDLC/EventVDay/Gear/Weapon/DataTable_WeaponBalance_EventVDay'
bounty='/Game/PatchDLC/Geranium/Gear/Weapon/DataTable_WeaponBalance_Geranium'
tentacles='/Game/PatchDLC/Hibiscus/Gear/Weapon/DataTable_WeaponBalance_Hibiscus'
mayhem2='/Game/PatchDLC/Mayhem2/Gear/Weapon/DataTable_WeaponBalance_Mayhem2'
raid1='/Game/PatchDLC/Raid1/Gear/Balance/DataTable_Raid1_Weapons'
guardian='/Game/PatchDLC/Takedown2/Gear/Weapons/DataTable_WeaponBalance_Takedown2'
harvest='Game/PatchDLC/BloodyHarvest/Gear/_Design/Balance/DataTable_Weapon_BloodyHarvest'
mayhem4 = '/Game/PatchDLC/Raid1/Re-Engagement/Balance/DataTable_ReEngagement1_Weapons'
ixora='/Game/PatchDLC/Ixora/Gear/Weapons/DataTable_WeaponBalance_Ixora'

mod.header('all unique guns damage')

mod.header('ATLAS TABLE')

mod.comment('RebelYell')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Parts/Part_AR_ATL_Barrel_RebelYell.Part_AR_ATL_Barrel_RebelYell',
'InventoryAttributeEffects.InventoryAttributeEffects[0]',
"""
(
    AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage"',
    ModifierType=ScaleSimple,
    ModifierValue=(BaseValueConstant=1.2,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
)
"""
)
mod.newline()

mod.comment('Carrier damage')
mod.table_hotfix(Mod.PATCH, '',
atlas,
'AR_Carrier',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('Linc damage')
mod.table_hotfix(Mod.PATCH, '',
atlas,
'PS_Drill',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.7
)
mod.newline()

mod.comment('Peacemonger damage')
mod.table_hotfix(Mod.PATCH, '',
atlas,
'PS_Peacemonger',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('Freeman damage')
mod.table_hotfix(Mod.PATCH, '',
atlas,
'HW_Freeman',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.8
)
mod.newline()

mod.comment('RubysWrath damage')
mod.table_hotfix(Mod.PATCH, '',
atlas,
'HW_RubysWrath',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.header('COV TABLE')

mod.comment('SawBar damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'AR_SAWBAR',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('SawBar chiild radius')
mod.table_hotfix(Mod.PATCH, '',
cov,
'AR_SAWBAR',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
250
)
mod.newline()

mod.comment('PainIsPower damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'AR_KreigDamage',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.1
)
mod.newline()

mod.comment('PainIsPower firerate')
mod.table_hotfix(Mod.PATCH, '',
cov,
'AR_KreigFirerate',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('EmbraceThePain damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'AR_CHAOS',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('TheKillingWord damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'PS_Mouthpiece',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.45
)
mod.newline()

mod.comment('Linoge damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'PS_Linoge',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.5
)
mod.newline()

mod.comment('Sekskil damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'PS_SKEKSIS',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.9
)
mod.newline()

mod.comment('Sekskil additional projectile')
mod.table_hotfix(Mod.PATCH, '',
cov,
'PS_SKEKSIS',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
0.95
)
mod.newline()

mod.comment('Pestilence damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'PS_Contagion',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('Pestilence aoe')
mod.table_hotfix(Mod.PATCH, '',
cov,
'PS_Contagion',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
0.8
)
mod.newline()

mod.comment('HanginChadd damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'PS_Chad',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('PsychoStabber damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'PS_PsychoStabber',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('PoopGun damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'HW_PortaPooper',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.65
)
mod.newline()

mod.comment('HotDrop damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'HW_HotDrop',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Agonizer1500 damage')
mod.table_hotfix(Mod.PATCH, '',
cov,
'HW_Terror',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.55
)
mod.newline()

mod.header('DAHL TABLE')

mod.comment('BreathOfTheDying damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_BOTD',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.comment('Warlord damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_Warlord',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Warlord Ammo regen')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_Warlord',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
0.4
)
mod.newline()

mod.comment('Barrage damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_Barrage',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Barrage crit')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_Barrage',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
1.35
)
mod.newline()

mod.comment('StarHelix damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_StarHelix',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Earworm damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_Earworm',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Hail damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_Hail',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.90
)
mod.newline()

mod.comment('Hail crit')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_Hail',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.95
)
mod.newline()

mod.comment('Kaos damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_Kaos',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('Ripper damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'SM_Ripper',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.5
)
mod.newline()

mod.comment('Ripper bonus after melee')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'SM_Ripper',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
4.0
)
mod.newline()

mod.comment('Vanquisher damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'SM_Vanquisher',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('Vanquisher slide sped')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'SM_Vanquisher',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
1.35
)
mod.newline()

mod.comment('Hellfire damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'SM_Hellfire',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('Hellfire dot')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'SM_Hellfire',
'Custom_B_11_6D4E8C1140CC269ED614BC958ECB0E22',
3.5
)
mod.newline()

mod.comment('9Volt damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'SM_9Volt',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('Hornet damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'PS_Hornet',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Irradiater damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'PS_Irradiater',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Nemesis damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'PS_Nemesis',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('AAA damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'PS_AAA',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('Rakkman damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'PS_Rakkman',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.45
)
mod.newline()

mod.comment('BreathOfTheDying damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'AR_BOTD',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Omniloader damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'PS_Omniloader',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('BrashisDedication damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'SR_BrashisDedication',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('WorldDestroyer damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'SR_WorldDestroyer',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('MalaksBane damage')
mod.table_hotfix(Mod.PATCH, '',
dalh,
'SR_MalaksBane',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.75
)
mod.newline()

mod.header('HYPERION TABLE')

mod.comment('Butcher damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SG_Butcher',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.75
)
mod.newline()

mod.comment('Redistributor damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SG_Redistributor',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.comment('ConferenceCall damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SG_ConferenceCall',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Brick damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SG_Brick',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.6
)
mod.newline()

mod.comment('Phebert damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SG_Phebert',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
8.0
)
mod.newline()

mod.comment('Crossroad damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SM_Crossroad',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Handsome damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SM_Handsome',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Handsome explosion')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SM_Handsome',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
0.5
)
mod.newline()

mod.comment('PredatoryLending damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SM_PredatoryLending',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Fork damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SM_Fork',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('Fork amp')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SM_Fork',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
4.0
)
mod.newline()

mod.comment('XZ damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SM_XZ',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Bitch damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SM_Bitch',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.6
)
mod.newline()

mod.comment('Bitch crit')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SM_Bitch',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
1.75
)
mod.newline()

mod.comment('Quad damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SR_Quad',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('TheTwoTime damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SR_TheTwoTime',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.9
)
mod.newline()

mod.comment('Masterwork damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SR_Masterwork',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
5.0
)
mod.newline()

mod.comment('Masterwork crit')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'SR_Masterwork',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.0
)
mod.newline()

mod.comment('L0V3M4CH1N3 damage')
mod.table_hotfix(Mod.PATCH, '',
hyperion,
'L0V3M4CH1N3',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.header('JAKOBS TABLE')

mod.comment('LeadSprinkler damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'AR_LeadSprinkler',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('LeadSprinkler crit')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'AR_LeadSprinkler',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
5.0
)
mod.newline()


mod.comment('GatlingGun damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'AR_GatlingGun',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('HandOfGlory damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'AR_HandOfGlory',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('TraitorsDeath damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'AR_TraitorsDeath',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('TraitorsDeath elemental chance')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'AR_TraitorsDeath',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
0.2
)
mod.newline()

mod.comment('TraitorsDeath bonus damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'AR_TraitorsDeath',
'Custom_B_11_6D4E8C1140CC269ED614BC958ECB0E22',
3.0
)
mod.newline()

mod.comment('Bekah damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'AR_Bekah',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.7
)
mod.newline()

mod.comment('Rowan damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'AR_Rowan',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Unforgiven damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_Unforgiven',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Unforgiven crit')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_Unforgiven',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.5
)
mod.newline()

mod.comment('WagonWheel damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_WagonWheel',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Companion damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_Companion',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('Maggie damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_Maggie',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.22
)
mod.newline()

mod.comment('Doc damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_Doc',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('TheDuc damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_TheDuc',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Malevolent damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_Malevolent',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('Malevolent amp')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_Malevolent',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.5
)
mod.newline()

mod.comment('AmazingGrace damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_AmazingGrace',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.5
)
mod.newline()

mod.comment('Buttplug damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_Buttplug',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.08
)
mod.newline()

mod.comment('Buttplug back')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_Buttplug',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
4.0
)
mod.newline()

mod.comment('GodQueen damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'PS_GodQueen',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('Wave damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SG_Wave',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('HellWalker damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SG_HellWalker',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Sledge damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SG_Sledge',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.8
)
mod.newline()

mod.comment('Fingerbiter damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SG_Fingerbiter',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('NimbleJack damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SG_NimbleJack',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Garcia damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SG_Garcia',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('OnePumpChump damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SG_OnePumpChump',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
12.0
)
mod.newline()

mod.comment('Monocle damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SR_Monocle',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('Monocle crit')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SR_Monocle',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.5
)
mod.newline()

mod.comment('Headsplosion damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SR_Headsplosion',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('IceQueen damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SR_IceQueen',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('Hunter damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SR_Hunter',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Hunted damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SR_Hunted',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Huntress damage')
mod.table_hotfix(Mod.PATCH, '',
jakobs,
'SR_Huntress',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.header('MALIWAN TABLE')

mod.comment('Storm damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SR_Storm',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.5
)
mod.newline()

mod.comment('ASMD damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SR_ASMD',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Krakatoa damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SR_Krakatoa',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.5
)
mod.newline()

mod.comment('Ikelos damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SR_Ikelos',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Lucian damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_Lucian',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Cutsman damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_Cutsman',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
3.5
)
mod.newline()

mod.comment('Tsunami damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_Tsunami',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('DestructoSpin damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_DestructoSpin',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Kevins damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_Kevins',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.7
)
mod.newline()

mod.comment('VibraPulse damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_VibraPulse',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('CloudKill damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_CloudKill',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Devoted damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_Devoted',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('westergun damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_westergun',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.05
)
mod.newline()

mod.comment('Egon damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_Egon',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('Emporer damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'Emporer',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Crit damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SM_Crit',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.comment('Recursion damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SG_Recursion',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
8.0
)
mod.newline()

mod.comment('Recursion distance')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SG_Recursion',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
4000.0
)
mod.newline()

mod.comment('Wisp damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SG_Wisp',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
6.0
)
mod.newline()

mod.comment('Mindkiller damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SG_Mindkiller',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('Shriek damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SG_Shriek',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
9.0
)
mod.newline()

mod.comment('Trev damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'SG_Trev',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
2.2
)
mod.newline()

mod.comment('ThunderballFists damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'PS_ThunderballFists',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.comment('Hellshock damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'PS_Hellshock',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('HyperHydrator damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'PS_HyperHydrator',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Starkiller damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'PS_Starkiller',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('Sellout damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'PS_Sellout',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('PS_Plumber damage')
mod.table_hotfix(Mod.PATCH, '',
maliwan,
'PS_Plumber',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.header('TEDIORE TABLE')

mod.comment('Sludge damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'SG_Sludge',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.9
)
mod.newline()

mod.comment('Horizon damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'SG_Horizon',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('Polybius damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'SG_Polybius',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('FriendZone damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'SG_FriendZone',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.15
)
mod.newline()

mod.comment('TenGallon damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'SM_TenGallon',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('Beans damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'SM_Beans',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('SpiderMind damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'SM_SpiderMind',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
2.5
)
mod.newline()

mod.comment('NotAFlamethrower damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'SM_NotAFlamethrower',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('BabyMaker damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'PS_BabyMaker',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.comment('Gunerang damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'PS_Gunerang',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Bangerang damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'PS_Bangerang',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Sabre damage')
mod.table_hotfix(Mod.PATCH, '',
tediore,
'PS_Sabre',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.header('TORGUE TABLE')

mod.comment('Devestator damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'PS_Devestator',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Foursome damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'PS_Foursome',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.5
)
mod.newline()

mod.comment('Troy damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'PS_Troy',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.comment('Echo damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'PS_Echo',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('NURF damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'PS_NURF',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('Heckle damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'PS_Heckle',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Hyde damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'PS_Hyde',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('RoisensThorns damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'PS_RoisensThorns',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('Redline damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'SG_Redline',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Flakker damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'SG_Flakker',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
2.5
)
mod.newline()

mod.comment('Thumper damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'SG_Thumper',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.8
)
mod.newline()

mod.comment('Brewha damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'SG_Brewha',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
3.0
)
mod.newline()

mod.comment('Balrog damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'SG_Balrog',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.8
)
mod.newline()

mod.comment('TheLob damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'SG_TheLob',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('LaserSploder damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'AR_LaserSploder',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('LaserSploder interval')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'AR_LaserSploder',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
0.3
)
mod.newline()

mod.comment('TryBolt damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'AR_TryBolt',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
2.0
)
mod.newline()

mod.comment('Bearcat damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'AR_Bearcat',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
2.0
)
mod.newline()

mod.comment('AmberManagement damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'AR_AmberManagement',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('AmberManagement dot')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'AR_AmberManagement',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
0.45
)
mod.newline()

mod.comment('Alchemist damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'AR_Alchemist',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('Swarm damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'HW_Swarm',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Tunguska damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'HW_Tunguska',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.45
)
mod.newline()

mod.comment('Rampager damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'HW_Rampager',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Hive damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'HW_Hive',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('RYNO damage')
mod.table_hotfix(Mod.PATCH, '',
torgue,
'HW_RYNO',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.header('VLADOF TABLE')

mod.comment('Mongol damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'HW_Mongol',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Cloudburst damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'HW_Cloudburst',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('Sickle damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'AR_Sickle',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.5
)
mod.newline()

mod.comment('Shreddifier damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'AR_Shreddifier',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Dictator damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'AR_Dictator',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.9
)
mod.newline()

mod.comment('Ogre damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'AR_Ogre',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('Faisor damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'AR_Faisor',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.9
)
mod.newline()

mod.comment('LuciansCall damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'AR_LuciansCall',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.1
)
mod.newline()

mod.comment('Damned damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'AR_Damned',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Magnificent damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'PS_Magnificent',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('BoneShredder damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'PS_BoneShredder',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('Infiniti damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'PS_Infiniti',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('TheLeech damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'PS_TheLeech',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Lyuda damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'SR_Lyuda',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.6
)
mod.newline()

mod.comment('Lyuda crit')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'SR_Lyuda',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.5
)
mod.newline()

mod.comment('Prison damage')
mod.table_hotfix(Mod.PATCH, '',
vladof,
'SR_Prison',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.header('JACKPOT TABLE')

mod.comment('JustCaustic damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'SM_JustCaustic',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Trash damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'AR_Trash',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.15
)
mod.newline()

mod.comment('IonCannon damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'HW_IonCannon',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
4.0
)
mod.newline()

mod.comment('IonLaser damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'SM_IonLaser',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Nukem damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'HW_Nukem',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
2.5
)
mod.newline()

mod.comment('HeartBreaker damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'SG_HeartBreaker',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.4
)
mod.newline()

mod.comment('RoboMasher damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'PS_RoboMasher',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Varlope damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'AR_Varlope',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.1
)
mod.newline()

mod.comment('EmbersPurge damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'SM_EmbersPurge',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Boomer damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'SM_Boomer',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Scoville damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'PS_Scoville',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
2.25
)
mod.newline()

mod.comment('AutoAime damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'SR_AutoAime',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Digby damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'AR_Digby',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('Creamer damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'HW_Creamer',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.comment('Craps damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'PS_Craps',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('CheapTip damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'SM_CheapTip',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('SlowHand damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'SG_SlowHand',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.4
)
mod.newline()

mod.comment('Lucky7 damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'PS_Lucky7',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.7
)
mod.newline()

mod.header('TENTACLES TABLE')

mod.comment('Skullmasher damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SR_Skullmasher',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.5
)
mod.newline()

mod.comment('Mutant damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'AR_Mutant',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Mutant_2 damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'AR_Mutant_2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Omen damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_Omen',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('Homicidal damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'AR_Homicidal',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Homicidal_A damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'AR_Homicidal_A',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('CockyBastard damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SR_CockyBastard',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('CockyBastard crit')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SR_CockyBastard',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.0
)
mod.newline()

mod.comment('Insider damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_Insider',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.35
)
mod.newline()

mod.comment('Oldridian damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SM_Oldridian',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Anarchy damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_Anarchy',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.7
)
mod.newline()

mod.comment('Anarchy scale')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_Anarchy',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
1.2
)
mod.newline()

mod.comment('Anarchy_2 damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_Anarchy_2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('TheCure damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_TheCure',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.4
)
mod.newline()

mod.comment('LoveDrill damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'PS_LoveDrill',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('LoveDrill_Leg damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'PS_LoveDrill_Leg',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.6
)
mod.newline()

mod.comment('Firecracker damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_Firecracker',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
5.0
)
mod.newline()

mod.comment('SacrificialLamb damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_SacrificialLamb',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.comment('Kaleidoscope damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'PS_Kaleidoscope',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.9
)
mod.newline()

mod.comment('Kaleidoscope amp')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'PS_Kaleidoscope',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
1.0
)
mod.newline()

mod.comment('FrozenDevil damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'PS_FrozenDevil',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.2
)
mod.newline()

mod.comment('FrozenDevil_2 damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'PS_FrozenDevil_2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('SFForce damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SM_SFForce',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Frostbite damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'PS_Frostbite',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('shocker damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_shocker',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('LittleYeeti damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'PS_LittleYeeti',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.5
)
mod.newline()

mod.comment('Clairvoyance damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'AR_Clairvoyance',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.55
)
mod.newline()

mod.comment('UnseenThreat damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SP_UnseenThreat',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('UnseenThreat ricochet')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SP_UnseenThreat',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
5.0
)
mod.newline()

mod.comment('TheNothing damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_TheNothing',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
5.0
)
mod.newline()

mod.comment('TheNothing_2 damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'SG_TheNothing_2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('SparkyBoom damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'AR_SparkyBoom',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('"SparkyBoom_2":  damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'"AR_SparkyBoom_2": ',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('SparkyBoom_3 damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'AR_SparkyBoom_3',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Soulrender damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'AR_Soulrender',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('TheSeventh damage')
mod.table_hotfix(Mod.PATCH, '',
tentacles,
'PS_TheSeventh',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.5
)
mod.newline()

mod.header('BOUNTY TABLE')

mod.comment('QuickDraw damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_QuickDraw',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('QuickDraw amp')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_QuickDraw',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.0
)
mod.newline()

mod.comment('CoolBeans damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'AR_CoolBeans',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Dakota damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SG_Dakota',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Dakota damage scale')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SG_Dakota',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.0
)
mod.newline()

mod.comment('Rose damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_Rose',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('ImaginaryNumber damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SR_ImaginaryNumber',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Lasocannon damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_Lasocannon',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Miscreant damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_Miscreant',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('SpeakEasy damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SG_SpeakEasy',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.15
)
mod.newline()

mod.comment('Gargoyle damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_Gargoyle',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('Gargoyle reload damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_Gargoyle',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.0
)
mod.newline()

mod.comment('Gargoyle_2 damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_Gargoyle_2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Shoveler damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SG_Shoveler',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Fakobs damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SG_Fakobs',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
5.0
)
mod.newline()

mod.comment('BubbleBlaster damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_BubbleBlaster',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Earthbound damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SM_Earthbound',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Brightside damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SG_Brightside',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.5
)
mod.newline()

mod.comment('McSmugger damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'AR_McSmugger',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Splinter damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SG_Splinter',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Peashooter damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_Peashooter',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Contained damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'AR_Contained',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Contained_2 damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'AR_Contained_2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('PrivateInvestigator damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_PrivateInvestigator',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Flipper damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SM_Flipper',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('Plumage damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'HW_Plumage',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('UnkemptHarold damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_UnkemptHarold',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('Decoupler damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'PS_Decoupler',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Frequency damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SG_Frequency',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('BioBetsy damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'AR_BioBetsy',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Satistfaction damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'HW_Satistfaction',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.8
)
mod.newline()

mod.comment('Narp damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SR_Narp',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Dowsing damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'AR_Dowsing',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Copybeast damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SM_Copybeast',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Antler damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SG_Antler',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('StoneThrow damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'AR_StoneThrow',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.header('MIND TABLE')

mod.comment('Sawhorse damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'AR_Sawhorse',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('BanditLauncher damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'HW_BanditLauncher',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.8
)
mod.newline()

mod.comment('Pat_Mk3 damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'SM_Pat_Mk3',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('LovableRogue damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'AR_LovableRogue',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('BlindBandit damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'SG_BlindBandit',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Septimator damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'SR_Septimator',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.15
)
mod.newline()

mod.comment('Septimator_2 damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'SR_Septimator_2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Voice damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'PS_Voice',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('AshenBeast damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'SM_AshenBeast',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('AshenBeast_2 damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'SM_AshenBeast_2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Convergence damage')
mod.table_hotfix(Mod.PATCH, '',
mind,
'SG_Convergence',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.header('MAYHEM2 TABLE')

mod.comment('Reflux damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem2,
'SG_Reflux',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.6
)
mod.newline()

mod.comment('DNA damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem2,
'SM_DNA',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.55
)
mod.newline()

mod.comment('TheMonarch damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem2,
'AR_TheMonarch',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('Plague damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem2,
'HW_Plague',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('Backburner damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem2,
'HW_Backburner',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('Kaoson damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem2,
'Kaoson',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('Multitap damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem2,
'PS_Multitap',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('SandHawk damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem2,
'SR_SandHawk',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.header('CARTEL TABLE')

mod.comment('IcePick damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'IcePick',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.15
)
mod.newline()

mod.comment('IceBurger damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'IceBurger',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.8
)
mod.newline()

mod.comment('IceBurger_part2 damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'IceBurger_part2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Pricker damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'Pricker',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('YellowCake damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'YellowCake',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('PewPew damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'PewPew',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('OPQS damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'OPQS',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.55
)
mod.newline()

mod.comment('GreaseTrap_Mode1 damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'PS_GreaseTrap_Mode1',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('GreaseTrap_Mode2 damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'PS_GreaseTrap_Mode2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.25
)
mod.newline()

mod.comment('NeedleGun damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'SM_NeedleGun',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.25
)
mod.newline()

mod.comment('NeedleGun_2 damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'SM_NeedleGun_2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('NeedleGun_3 damage')
mod.table_hotfix(Mod.PATCH, '',
cartel,
'SM_NeedleGun_3',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.header('VALENTINES TABLE')

mod.comment('PolyAim damage')
mod.table_hotfix(Mod.PATCH, '',
valentines,
'PolyAim',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('WeddingInvitation damage')
mod.table_hotfix(Mod.PATCH, '',
valentines,
'WeddingInvitation',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('WeddingInvitation ricochet')
mod.table_hotfix(Mod.PATCH, '',
valentines,
'WeddingInvitation',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
2.5
)
mod.newline()

mod.comment('WeddingInvitation2 damage')
mod.table_hotfix(Mod.PATCH, '',
valentines,
'WeddingInvitation2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.header('RAID1 TABLE')

mod.comment('KybsWorth damage')
mod.table_hotfix(Mod.PATCH, '',
raid1,
'KybsWorth',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('P2PNetworker damage')
mod.table_hotfix(Mod.PATCH, '',
raid1,
'P2PNetworker',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('TiggsBoom damage')
mod.table_hotfix(Mod.PATCH, '',
raid1,
'SG_TiggsBoom',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('HandCannon damage')
mod.table_hotfix(Mod.PATCH, '',
raid1,
'PS_HandCannon',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.45
)
mod.newline()

mod.comment('HandCannon_PT2 damage')
mod.table_hotfix(Mod.PATCH, '',
raid1,
'PS_HandCannon_PT2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Fork2 damage')
mod.table_hotfix(Mod.PATCH, '',
raid1,
'SM_Fork2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('Fork2 amp')
mod.table_hotfix(Mod.PATCH, '',
raid1,
'SM_Fork2',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
4.0
)
mod.newline()

mod.header('GUARDIAN TABLE')

mod.comment('Smog damage')
mod.table_hotfix(Mod.PATCH, '',
guardian,
'SM_Smog',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('WebSlinger damage')
mod.table_hotfix(Mod.PATCH, '',
guardian,
'AR_WebSlinger',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Webslinger_Underbarrel damage')
mod.table_hotfix(Mod.PATCH, '',
guardian,
'AR_Webslinger_Underbarrel',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Globetrotter damage')
mod.table_hotfix(Mod.PATCH, '',
guardian,
'HW_Globetrotter',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.header('HARVEST TABLE')

mod.comment('Fearmonger damage')
mod.table_hotfix(Mod.PATCH, '',
harvest,
'SG_Fearmonger',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.65
)
mod.newline()

mod.comment('FrostBolt damage')
mod.table_hotfix(Mod.PATCH, '',
harvest,
'SR_FrostBolt',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.header('MAYHEM4 TABLE')

mod.comment('Tankman damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem4,
'Tankman',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Zheitsev damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem4,
'Zheitsev',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.1
)
mod.newline()

mod.comment('Zheitsev_part2 damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem4,
'Zheitsev_part2',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Juju damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem4,
'Juju',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.comment('CraderMP5 damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem4,
'CraderMP5',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('Deathgrip damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem4,
'Deathgrip',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
2.0
)
mod.newline()

mod.comment('Execute damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem4,
'Execute',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

mod.comment('Juliet damage')
mod.table_hotfix(Mod.PATCH, '',
mayhem4,
'Juliet',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.header('IXORA TABLE')

mod.comment('Boogeyman damage')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'Boogeyman',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.95
)
mod.newline()

mod.comment('CriticalThug damage')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'CriticalThug',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('Firefly damage')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'Firefly',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.8
)
mod.newline()

mod.comment('PlasmaCoil damage')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'PlasmaCoil',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('HotfootTeddy damage')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'HotfootTeddy',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.8
)
mod.newline()

mod.comment('Trickshot damage')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'Trickshot',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('DarkArmy damage')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'DarkArmy',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('IceAge damage')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'IceAge',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.75
)
mod.newline()

mod.comment('IceAge frozen')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'IceAge',
'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
3.5
)
mod.newline()

mod.comment('Tizzy damage')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'Tizzy',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
0.85
)
mod.newline()

mod.comment('SpiritOfMaya damage')
mod.table_hotfix(Mod.PATCH, '',
ixora,
'SpiritOfMaya',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.0
)
mod.newline()

gbase='/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Balance_Table'
gunique='/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Unique_Balance_Table'
gguardian='/Game/PATCHDLC/Takedown2/Gear/GrenadeMods/GrenadeMod_Unique_BalanceTable_Takedown2'
gbounty='/Game/PATCHDLC/Geranium/Gear/Grenade/GrenadeMod_Geranium_Table'
gjackpot='/Game/PATCHDLC/Dandelion/Gear/Grenade/GrenadeMod_Dandelion_Table'
gcartel='/Game/PATCHDLC/Event2/Gear/GrenadeMods/GrenadeMod_Event2_Table'