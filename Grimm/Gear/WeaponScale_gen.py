from bl3hotfixmod import Mod

mod=Mod('WeaponScale.bl3hotfix',
'Weapon Scale',
'Grimm',
[
    'Complete rebalance of all weapon types, manufacturer and E tech guns.',
    'Also buffs Atlas N system and V system ARs',
    'Thanks to CodyCode, SsPyR, Apocalyptech, 10 FPS, HackerSmasher, FromDarkHell, Apple1417'
],
lic=Mod.CC_BY_SA_40,
)

weapontype='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Base_Data'
weaponbrand='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_DamageScale'
brandstats='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Manufacturer_Base_Data'
ar='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_AR_Barrel_Init'
hw='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_HW_Barrel_Init'
ps='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_PS_Barrel_Init'
sg='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_SG_Barrel_Init'
sm='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_SM_Barrel_Init'
sr='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_SR_Barrel_Init'

###BARRELS

#ATLAS AR

mod.comment('Atlas N System')
mod.table_hotfix(Mod.PATCH, '',
ar,
'ATL_Barrel_01',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.2
)
mod.newline()

mod.comment('Atlas V System')
mod.table_hotfix(Mod.PATCH, '',
ar,
'ATL_Barrel_03',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.3
)
mod.newline()

###E TECH ARS

mod.comment('CoV E Tech')
mod.table_hotfix(Mod.PATCH, '',
ar,
'COV_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.5
)
mod.newline()

mod.comment('Dahl E Tech')
mod.table_hotfix(Mod.PATCH, '',
ar,
'DAL_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.65
)
mod.newline()

mod.comment('Torgue E Tech')
mod.table_hotfix(Mod.PATCH, '',
ar,
'TOR_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.75
)
mod.newline()

mod.comment('Vladof E Tech')
mod.table_hotfix(Mod.PATCH, '',
ar,
'VLA_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.6
)
mod.newline()

###E TECH HEAVIES

mod.comment('CoV E Tech')
mod.table_hotfix(Mod.PATCH, '',
hw,
'COV_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.25
)
mod.newline()

mod.comment('Torgue E Tech')
mod.table_hotfix(Mod.PATCH, '',
hw,
'TOR_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
2.0
)
mod.newline()

mod.comment('Vladof E Tech')
mod.table_hotfix(Mod.PATCH, '',
hw,
'VLA_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
2.2
)
mod.newline()

###E TECH PISTOLS

mod.comment('CoV E Tech')
mod.table_hotfix(Mod.PATCH, '',
ps,
'COV_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.75
)
mod.newline()

mod.comment('Dahl E Tech')
mod.table_hotfix(Mod.PATCH, '',
ps,
'DAL_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.9
)
mod.newline()

mod.comment('Maliwan E Tech')
mod.table_hotfix(Mod.PATCH, '',
ps,
'MAL_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.25
)
mod.newline()

mod.comment('Torgue E Tech')
mod.table_hotfix(Mod.PATCH, '',
ps,
'TOR_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.9
)
mod.newline()

mod.comment('Tediore E Tech')
mod.table_hotfix(Mod.PATCH, '',
ps,
'TED_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.0
)
mod.newline()

mod.comment('Vladof E Tech')
mod.table_hotfix(Mod.PATCH, '',
ps,
'VLA_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.45
)
mod.newline()

###E TECH SHOTGUNS

mod.comment('Hyperion E Tech')
mod.table_hotfix(Mod.PATCH, '',
sg,
'HYP_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
8.0
)
mod.newline()

mod.comment('Maliwan E Tech')
mod.table_hotfix(Mod.PATCH, '',
sg,
'MAL_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
9.0
)
mod.newline()

mod.comment('Torgue E Tech')
mod.table_hotfix(Mod.PATCH, '',
sg,
'TOR_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
5.0
)
mod.newline()

mod.comment('Tediore E Tech')
mod.table_hotfix(Mod.PATCH, '',
sg,
'TED_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
8.0
)
mod.newline()

##E TECH SMGS

mod.comment('Dahl E Tech')
mod.table_hotfix(Mod.PATCH, '',
sm,
'DAL_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.95
)
mod.newline()

mod.comment('Hyperion E Tech')
mod.table_hotfix(Mod.PATCH, '',
sm,
'HYP_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.0
)
mod.newline()

mod.comment('Maliwan E Tech')
mod.table_hotfix(Mod.PATCH, '',
sm,
'MAL_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.85
)
mod.newline()

mod.comment('Tediore E Tech')
mod.table_hotfix(Mod.PATCH, '',
sm,
'TED_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.95
)
mod.newline()

##E TECH SNIPERS

mod.comment('Dahl E Tech')
mod.table_hotfix(Mod.PATCH, '',
sr,
'DAL_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.0
)
mod.newline()

mod.comment('Hyperion E Tech')
mod.table_hotfix(Mod.PATCH, '',
sr,
'HYP_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.8
)
mod.newline()

mod.comment('Maliwan E Tech')
mod.table_hotfix(Mod.PATCH, '',
sr,
'MAL_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.8
)
mod.newline()

mod.comment('Vladof E Tech')
mod.table_hotfix(Mod.PATCH, '',
sr,
'VLA_Barrel_ETech',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.85
)
mod.newline()

mod.header('Changing the stats for weapon types')

###ASSAULT RIFLES

mod.comment('AssaultRifle damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.85
)
mod.newline()

mod.comment('AssaultRifle crit')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
1.0
)
mod.newline()

mod.comment('AssaultRifle fire rate')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('AssaultRifle spread')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'Spread_23_03553D4547FA30186E792BA391B2FFDE',
1.5
)
mod.newline()

mod.comment('AssaultRifle accuracy max')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
8.0
)
mod.newline()

mod.comment('AssaultRifle accuracy min')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
2.0
)
mod.newline()

mod.comment('AssaultRifle accuracy')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
0.85
)
mod.newline()

mod.comment('AssaultRifle accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
1.0
)
mod.newline()

mod.comment('AssaultRifle recoil height')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.25
)
mod.newline()

mod.comment('AssaultRifle recoil width')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('AssaultRifle zoom time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
1.15
)
mod.newline()

mod.comment('AssaultRifle reload time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
1.15
)
mod.newline()

mod.comment('AssaultRifle equip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
0.90
)
mod.newline()

mod.comment('AssaultRifle desequip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
0.45
)
mod.newline()

mod.comment('AssaultRifle elemental chance')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
0.1
)
mod.newline()

mod.comment('AssaultRifle elemental damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'AssaultRifle',
'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
1.15
)
mod.newline()

###SMGS

mod.comment('SMG damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.7
)
mod.newline()

mod.comment('SMG crit')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
1.0
)
mod.newline()

mod.comment('SMG fire rate')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('SMG spread')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'Spread_23_03553D4547FA30186E792BA391B2FFDE',
3.0
)
mod.newline()

mod.comment('SMG accuracy max')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
6.5
)
mod.newline()

mod.comment('SMG accuracy min')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
3.0
)
mod.newline()

mod.comment('SMG accuracy')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
0.65
)
mod.newline()

mod.comment('SMG accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
0.9
)
mod.newline()

mod.comment('SMG recoil height')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.25
)
mod.newline()

mod.comment('SMG recoil width')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.25
)
mod.newline()

mod.comment('SMG zoom time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
0.75
)
mod.newline()

mod.comment('SMG reload time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
1.0
)
mod.newline()

mod.comment('SMG equip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
0.60
)
mod.newline()

mod.comment('SMG desequip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
0.30
)
mod.newline()

mod.comment('SMG elemental chance')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
0.15
)
mod.newline()

mod.comment('SMG elemental damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SMG',
'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
1.2
)
mod.newline()

###PISTOLS

mod.comment('Pistol damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.0
)
mod.newline()

mod.comment('Pistol crit')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
1.0
)
mod.newline()

mod.comment('Pistol fire rate')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Pistol spread')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'Spread_23_03553D4547FA30186E792BA391B2FFDE',
1.65
)
mod.newline()

mod.comment('Pistol accuracy max')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
5.0
)
mod.newline()

mod.comment('Pistol accuracy min')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Pistol accuracy')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
0.75
)
mod.newline()

mod.comment('Pistol accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
1.2
)
mod.newline()

mod.comment('Pistol recoil height')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.0
)
mod.newline()

mod.comment('Pistol recoil width')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('Pistol zoom time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
0.55
)
mod.newline()

mod.comment('Pistol reload time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
0.75
)
mod.newline()

mod.comment('Pistol equip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
0.40
)
mod.newline()

mod.comment('Pistol desequip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
0.20
)
mod.newline()

mod.comment('Pistol elemental chance')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
0.15
)
mod.newline()

mod.comment('Pistol elemental damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Pistol',
'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
0.95
)
mod.newline()

###SHOTGUNS

mod.comment('Shotgun damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.5
)
mod.newline()

mod.comment('Shotgun crit')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
1.0
)
mod.newline()

mod.comment('Shotgun fire rate')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Shotgun spread')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'Spread_23_03553D4547FA30186E792BA391B2FFDE',
5.0
)
mod.newline()

mod.comment('Shotgun accuracy max')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
2.0
)
mod.newline()

mod.comment('Shotgun accuracy min')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Shotgun accuracy')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
1.0
)
mod.newline()

mod.comment('Shotgun accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
1.0
)
mod.newline()

mod.comment('Shotgun recoil height')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.5
)
mod.newline()

mod.comment('Shotgun recoil width')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.5
)
mod.newline()

mod.comment('Shotgun zoom time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
0.90
)
mod.newline()

mod.comment('Shotgun reload time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
1.0
)
mod.newline()

mod.comment('Shotgun equip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
0.90
)
mod.newline()

mod.comment('Shotgun desequip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
0.45
)
mod.newline()

mod.comment('Shotgun elemental chance')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
0.08
)
mod.newline()

mod.comment('Shotgun elemental damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Shotgun',
'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
1.6
)
mod.newline()

###SNIPER RIFLES

mod.comment('SniperRifle damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
2.0   
)
mod.newline()

mod.comment('SniperRifle crit')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
1.25
)
mod.newline()

mod.comment('SniperRifle fire rate')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('SniperRifle spread')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'Spread_23_03553D4547FA30186E792BA391B2FFDE',
1.5
)
mod.newline()

mod.comment('SniperRifle accuracy max')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
8.0
)
mod.newline()

mod.comment('SniperRifle accuracy min')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('SniperRifle accuracy')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
2.0
)
mod.newline()

mod.comment('SniperRifle accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
0.85
)
mod.newline()

mod.comment('SniperRifle recoil height')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.0
)
mod.newline()

mod.comment('SniperRifle recoil width')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('SniperRifle zoom time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
0.65
)
mod.newline()

mod.comment('SniperRifle reload time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
1.25
)
mod.newline()

mod.comment('SniperRifle equip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
1.2
)
mod.newline()

mod.comment('SniperRifle desequip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
0.6
)
mod.newline()

mod.comment('SniperRifle elemental chance')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
0.2
)
mod.newline()

mod.comment('SniperRifle elemental damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'SniperRifle',
'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
1.2
)
mod.newline()

###HEAVY

mod.comment('Heavy damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
3.5
)
mod.newline()

mod.comment('Heavy crit')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
1.0
)
mod.newline()

mod.comment('Heavy fire rate')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Heavy spread')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'Spread_23_03553D4547FA30186E792BA391B2FFDE',
2.0
)
mod.newline()

mod.comment('Heavy accuracy max')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
4.0
)
mod.newline()

mod.comment('Heavy accuracy min')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Heavy accuracy')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
1.5
)
mod.newline()

mod.comment('Heavy accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
1.0
)
mod.newline()

mod.comment('Heavy recoil height')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.0
)
mod.newline()

mod.comment('Heavy recoil width')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('Heavy zoom time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
0.65
)
mod.newline()

mod.comment('Heavy reload time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
1.25
)
mod.newline()

mod.comment('Heavy equip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
1.5
)
mod.newline()

mod.comment('Heavy desequip time')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
0.75
)
mod.newline()

mod.comment('Heavy elemental chance')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
0.25
)
mod.newline()

mod.comment('Heavy elemental damage')
mod.table_hotfix(Mod.PATCH, '',
weapontype,
'Heavy',
'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
0.7
)
mod.newline()

###SHOTGUNS BRAND DAMAGE SCALE

mod.comment('Shotgun damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Shotgun',
'Jakobs_60_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.1
)
mod.newline()

mod.comment('Shotgun damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Shotgun',
'Hyperion_61_03553D4547FA30186E792BA391B2FFDE',
1.0
)
mod.newline()

mod.comment('Shotgun damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Shotgun',
'Tediore_64_177AD05C46493B9713642FA9EEDB6DDC',
0.75
)
mod.newline()

mod.comment('Shotgun damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Shotgun',
'Torgue_75_E4646A97474FA2023598DE982B960083',
1.55
)
mod.newline()

mod.comment('Shotgun damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Shotgun',
'Maliwan_76_93DF9FBB4DB223F6D5697180435918B2',
1.3
)
mod.newline()

###PISTOLS BRAND DAMAGE SCALE

mod.comment('Pistol damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Pistol',
'DAHL_59_150C89A04BB4FCF0061CAC86E39E1A39',
1.15
)
mod.newline()

mod.comment('Pistol damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Pistol',
'Jakobs_60_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.75
)
mod.newline()

mod.comment('Pistol damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Pistol',
'Vladof_63_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
0.9
)
mod.newline()

mod.comment('Pistol damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Pistol',
'Tediore_64_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Pistol damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Pistol',
'CoV_65_A2A97C764F97EC46B630BB9F944FE44E',
0.8
)
mod.newline()

mod.comment('Pistol damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Pistol',
'Torgue_75_E4646A97474FA2023598DE982B960083',
2.0
)
mod.newline()

mod.comment('Pistol damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Pistol',
'Maliwan_76_93DF9FBB4DB223F6D5697180435918B2',
1.2
)
mod.newline()

mod.comment('Pistol damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Pistol',
'Atlas_78_8B8B7B8741EFF37DAC0B5D8739B6F0E4',
1.25
)
mod.newline()

###SMG BRAND DAMAGE SCALE

mod.comment('SMG damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'SMG',
'DAHL_59_150C89A04BB4FCF0061CAC86E39E1A39',
1.0
)
mod.newline()

mod.comment('SMG damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'SMG',
'Hyperion_61_03553D4547FA30186E792BA391B2FFDE',
1.25
)
mod.newline()

mod.comment('SMG damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'SMG',
'Tediore_64_177AD05C46493B9713642FA9EEDB6DDC',
0.95
)
mod.newline()

mod.comment('SMG damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'SMG',
'Maliwan_76_93DF9FBB4DB223F6D5697180435918B2',
1.1
)
mod.newline()

###ASSAULT RIFLES BRAND DAMAGE SCALE

mod.comment('AssaultRifle damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'AssaultRifle',
'Jakobs_60_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.6
)
mod.newline()

mod.comment('AssaultRifle damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'AssaultRifle',
'Vladof_63_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
0.65
)
mod.newline()

mod.comment('AssaultRifle damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'AssaultRifle',
'CoV_65_A2A97C764F97EC46B630BB9F944FE44E',
0.8
)
mod.newline()

mod.comment('AssaultRifle damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'AssaultRifle',
'Torgue_75_E4646A97474FA2023598DE982B960083',
1.4
)
mod.newline()

mod.comment('AssaultRifle damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'AssaultRifle',
'Atlas_78_8B8B7B8741EFF37DAC0B5D8739B6F0E4',
1.25
)
mod.newline()

###SNIPER RIFLES BRAND DAMAGE SCALE

mod.comment('Sniper damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Sniper',
'DAHL_59_150C89A04BB4FCF0061CAC86E39E1A39',
1.4
)
mod.newline()

mod.comment('Sniper damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Sniper',
'Jakobs_60_F95FBBA045F4F1899B3F7AB7A2CF0F22',
2.0
)
mod.newline()

mod.comment('Sniper damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Sniper',
'Hyperion_61_03553D4547FA30186E792BA391B2FFDE',
1.6
)
mod.newline()

mod.comment('Sniper damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Sniper',
'Maliwan_76_93DF9FBB4DB223F6D5697180435918B2',
1.7
)
mod.newline()

mod.comment('Sniper damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Sniper',
'Vladof_63_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
1.15
)
mod.newline()

###HEAVY BRAND DAMAGE SCALE

mod.comment('Heavy damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Heavy',
'CoV_65_A2A97C764F97EC46B630BB9F944FE44E',
1.35
)
mod.newline()

mod.comment('Heavy damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Heavy',
'Vladof_63_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
1.1
)
mod.newline()

mod.comment('Heavy damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Heavy',
'Torgue_75_E4646A97474FA2023598DE982B960083',
1.85
)
mod.newline()

mod.comment('Heavy damage')
mod.table_hotfix(Mod.PATCH, '',
weaponbrand,
'Heavy',
'Atlas_78_8B8B7B8741EFF37DAC0B5D8739B6F0E4',
1.2 
)
mod.newline()

mod.header('Brand Stats')

###DAHL

mod.comment('Dahl damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.0
)
mod.newline()

mod.comment('Dahl crit')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
1.0
)
mod.newline()

mod.comment('Dahl fire rate')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Dahl spread')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
0.85
)
mod.newline()

mod.comment('Dahl accuracy max')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
1.0
)
mod.newline()

mod.comment('Dahl accuracy min')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Dahl accuracy')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
0.80
)
mod.newline()

mod.comment('Dahl accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
1.0
)
mod.newline()

mod.comment('Dahl recoil height')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.0
)
mod.newline()

mod.comment('Dahl recoil width')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('Dahl zoom time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
0.90
)
mod.newline()

mod.comment('Dahl reload time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
1.0
)
mod.newline()

mod.comment('Dahl equip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
0.80
)
mod.newline()

mod.comment('Dahl desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
0.75
)
mod.newline()

mod.comment('Dahl desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
1.0
)
mod.newline()

mod.comment('Dahl elemental chance')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
0.9
)
mod.newline()

mod.comment('Dahl elemental damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Dahl',
'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
1.0
)
mod.newline()

###JAKOBS

mod.comment('Jakobs damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.0
)
mod.newline()

mod.comment('Jakobs crit')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
1.1
)
mod.newline()

mod.comment('Jakobs fire rate')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Jakobs spread')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
1.0
)
mod.newline()

mod.comment('Jakobs accuracy max')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
0.9
)
mod.newline()

mod.comment('Jakobs accuracy min')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Jakobs accuracy')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
0.70
)
mod.newline()

mod.comment('Jakobs accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
1.0
)
mod.newline()

mod.comment('Jakobs recoil height')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.1
)
mod.newline()

mod.comment('Jakobs recoil width')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.1
)
mod.newline()

mod.comment('Jakobs zoom time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
0.95
)
mod.newline()

mod.comment('Jakobs reload time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
1.0
)
mod.newline()

mod.comment('Jakobs equip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
0.80
)
mod.newline()

mod.comment('Jakobs desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
0.75
)
mod.newline()

mod.comment('Jakobs desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
1.3
)
mod.newline()

mod.comment('Jakobs elemental chance')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
0.7
)
mod.newline()

mod.comment('Jakobs elemental damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Jakobs',
'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
1.05
)
mod.newline()

###HYPERION

mod.comment('Hyperion damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.0
)
mod.newline()

mod.comment('Hyperion crit')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
1.1
)
mod.newline()

mod.comment('Hyperion fire rate')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Hyperion spread')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
0.8
)
mod.newline()

mod.comment('Hyperion accuracy max')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
1.15
)
mod.newline()

mod.comment('Hyperion accuracy min')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Hyperion accuracy')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
0.70
)
mod.newline()

mod.comment('Hyperion accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
1.0
)
mod.newline()

mod.comment('Hyperion recoil height')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.0
)
mod.newline()

mod.comment('Hyperion recoil width')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('Hyperion zoom time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
1.0
)
mod.newline()

mod.comment('Hyperion reload time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
1.0
)
mod.newline()

mod.comment('Hyperion equip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
1.0
)
mod.newline()

mod.comment('Hyperion desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
1.0
)
mod.newline()

mod.comment('Hyperion weapon force')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
1.0
)
mod.newline()

mod.comment('Hyperion elemental chance')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
0.95
)
mod.newline()

mod.comment('Hyperion elemental damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Hyperion',
'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
1.05
)
mod.newline()

###VLADOF

mod.comment('Vladof damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.05
)
mod.newline()

mod.comment('Vladof crit')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
1.0
)
mod.newline()

mod.comment('Vladof fire rate')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Vladof spread')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
1.2
)
mod.newline()

mod.comment('Vladof accuracy max')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
1.0
)
mod.newline()

mod.comment('Vladof accuracy min')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Vladof accuracy')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
1.0
)
mod.newline()

mod.comment('Vladof accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
0.80
)
mod.newline()

mod.comment('Vladof recoil height')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.0
)
mod.newline()

mod.comment('Vladof recoil width')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('Vladof zoom time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
1.0
)
mod.newline()

mod.comment('Vladof reload time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
1.0
)
mod.newline()

mod.comment('Vladof equip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
1.1
)
mod.newline()

mod.comment('Vladof desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
1.0
)
mod.newline()

mod.comment('Vladof weapon force')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
1.0
)
mod.newline()

mod.comment('Vladof elemental chance')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
0.9
)
mod.newline()

mod.comment('Vladof elemental damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Vladof',
'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
1.0
)
mod.newline()

###TEDIORE

mod.comment('Tediore damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.0
)
mod.newline()

mod.comment('Tediore crit')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
1.0
)
mod.newline()

mod.comment('Tediore fire rate')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Tediore spread')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
1.25
)
mod.newline()

mod.comment('Tediore accuracy max')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
1.0
)
mod.newline()

mod.comment('Tediore accuracy min')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Tediore accuracy')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
0.8
)
mod.newline()

mod.comment('Tediore accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
0.8
)
mod.newline()

mod.comment('Tediore recoil height')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.0
)
mod.newline()

mod.comment('Tediore recoil width')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('Tediore zoom time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
1.0
)
mod.newline()

mod.comment('Tediore reload time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
0.8
)
mod.newline()

mod.comment('Tediore equip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
1.0
)
mod.newline()

mod.comment('Tediore desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
1.0
)
mod.newline()

mod.comment('Tediore weapon force')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
1.0
)
mod.newline()

mod.comment('Tediore elemental chance')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
1.0
)
mod.newline()

mod.comment('Tediore elemental damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Tediore',
'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
1.1
)
mod.newline()

###COV

mod.comment('CoV damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.1
)
mod.newline()

mod.comment('CoV crit')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
1.0
)
mod.newline()

mod.comment('CoV fire rate')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('CoV spread')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
2.0
)
mod.newline()

mod.comment('CoV accuracy max')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
0.8
)
mod.newline()

mod.comment('CoV accuracy min')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('CoV accuracy')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
0.85
)
mod.newline()

mod.comment('CoV accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
0.6
)
mod.newline()

mod.comment('CoV recoil height')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.15
)
mod.newline()

mod.comment('CoV recoil width')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.15
)
mod.newline()

mod.comment('CoV zoom time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
1.10
)
mod.newline()

mod.comment('CoV reload time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
1.05
)
mod.newline()

mod.comment('CoV equip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
1.5
)
mod.newline()

mod.comment('CoV desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
1.0
)
mod.newline()

mod.comment('CoV weapon force')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
1.0
)
mod.newline()

mod.comment('CoV elemental chance')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
1.0
)
mod.newline()

mod.comment('CoV elemental damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'CoV',
'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
1.0
)
mod.newline()

###TORGUE

mod.comment('Torgue damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.9
)
mod.newline()

mod.comment('Torgue crit')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
1.0
)
mod.newline()

mod.comment('Torgue fire rate')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Torgue spread')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
0.7
)
mod.newline()

mod.comment('Torgue accuracy max')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
0.8
)
mod.newline()

mod.comment('Torgue accuracy min')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Torgue accuracy')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
1.0
)
mod.newline()

mod.comment('Torgue accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
1.0
)
mod.newline()

mod.comment('Torgue recoil height')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.0
)
mod.newline()

mod.comment('Torgue recoil width')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('Torgue zoom time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
1.1
)
mod.newline()

mod.comment('Torgue reload time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
1.1
)
mod.newline()

mod.comment('Torgue equip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
1.1
)
mod.newline()

mod.comment('Torgue desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
1.0
)
mod.newline()

mod.comment('Torgue weapon force')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
1.2
)
mod.newline()

mod.comment('Torgue elemental chance')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
1.1
)
mod.newline()

mod.comment('Torgue elemental damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Torgue',
'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
1.0
)
mod.newline()

###MALIWAN

mod.comment('Maliwan damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
0.55
)
mod.newline()

mod.comment('Maliwan crit')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
1.0
)
mod.newline()

mod.comment('Maliwan fire rate')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Maliwan spread')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
1.0
)
mod.newline()

mod.comment('Maliwan accuracy max')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
1.0
)
mod.newline()

mod.comment('Maliwan accuracy min')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Maliwan accuracy')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
1.0
)
mod.newline()

mod.comment('Maliwan accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
1.0
)
mod.newline()

mod.comment('Maliwan recoil height')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.0
)
mod.newline()

mod.comment('Maliwan recoil width')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('Maliwan zoom time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
1.0
)
mod.newline()

mod.comment('Maliwan reload time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
0.85
)
mod.newline()

mod.comment('Maliwan equip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
1.0
)
mod.newline()

mod.comment('Maliwan desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
1.0
)
mod.newline()

mod.comment('Maliwan weapon force')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
1.1
)
mod.newline()

mod.comment('Maliwan elemental chance')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
2.0
)
mod.newline()

mod.comment('Maliwan elemental damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Maliwan',
'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
2.5
)
mod.newline()

###ATLAS

mod.comment('Atlas damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.15
)
mod.newline()

mod.comment('Atlas crit')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
1.0
)
mod.newline()

mod.comment('Atlas fire rate')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
1.0
)
mod.newline()

mod.comment('Atlas spread')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
1.0
)
mod.newline()

mod.comment('Atlas accuracy max')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
1.0
)
mod.newline()

mod.comment('Atlas accuracy min')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
1.0
)
mod.newline()

mod.comment('Atlas accuracy')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
1.0
)
mod.newline()

mod.comment('Atlas accuracy idle')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
1.0
)
mod.newline()

mod.comment('Atlas recoil height')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
1.0
)
mod.newline()

mod.comment('Atlas recoil width')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
1.0
)
mod.newline()

mod.comment('Atlas zoom time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
0.9
)
mod.newline()

mod.comment('Atlas reload time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
1.0
)
mod.newline()

mod.comment('Atlas equip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
0.95
)
mod.newline()

mod.comment('Atlas desequip time')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
1.0
)
mod.newline()

mod.comment('Atlas weapon force')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
0.9
)
mod.newline()

mod.comment('Atlas elemental chance')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
0.6
)
mod.newline()

mod.comment('Atlas elemental damage')
mod.table_hotfix(Mod.PATCH, '',
brandstats,
'Atlas',
'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
0.9
)
mod.newline()
