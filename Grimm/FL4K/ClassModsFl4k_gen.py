from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('ClassModsFl4k.bl3hotfix',
'ClassMods',
'Grimm',
[
    'ClassMods overhaul for fl4k.',
    'Class mods now have no passives.',
    'All class mods are redone from scratch, each mod now has new skills.',
    'White mods have 4 points, green have 6, blue have 8 and purple have 10.',
    'Thanks to CodyCode, SsPyR, Apocalyptech, 10 FPS, HackerSmasher, FromDarkHell, Apple1417'
],
lic=Mod.CC_BY_SA_40,
)

cmbal=[
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_BountyHunter',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_CosmicStalker',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_DE4DEYE',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_FriendBot',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RakkCommander',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RedFang',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1',       #RakkPack
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_DLC1',    #StackBot
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Hib',      #Trainer
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Alisma',     #Peregrine
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_01_Common',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_02_Uncommon',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_03_Rare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_04_VeryRare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_05_Legendary'
]

cmpartset=[
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_BountyHunter',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_CosmicStalker',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_DE4DEYE',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_FriendBot',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_RakkCommander',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_RedFang',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/PartSet_CM_Beastmaster_Raid1',       #RakkPack
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/PartSet_CM_Beastmaster_DLC1',    #StackBot
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/PartSet_CM_Beastmaster_Hib',      #Trainer
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/PartSet_CM_Beastmaster_Alisma',     #Peregrine
    '/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod_Beastmaster_01_Common',
    '/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod_Beastmaster_02_Uncommon',
    '/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod_Beastmaster_03_Rare',
    '/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod_Beastmaster_04_VeryRare',
    '/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod_Beastmaster_05_Legendary'
]

cmstats=[
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_WeaponDamage.ClassMod_Part_Stat_Primary_WeaponDamage', 
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_FireRate.ClassMod_Part_Stat_Primary_FireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_CritDamage.ClassMod_Part_Stat_Primary_CritDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_Accuracy.ClassMod_Part_Stat_Primary_Accuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_ChargeTime.ClassMod_Part_Stat_Primary_ChargeTime',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_Handling.ClassMod_Part_Stat_Primary_Handling',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_MagazineSize.ClassMod_Part_Stat_Primary_MagazineSize',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_ReloadSpeed.ClassMod_Part_Stat_Primary_ReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_GrenadeDamage.ClassMod_Part_Stat_Primary_GrenadeDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_GrenadeRadius.ClassMod_Part_Stat_Primary_GrenadeRadius',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_GrenadeAmmo.ClassMod_Part_Stat_Primary_GrenadeAmmo',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_AreaDamage.ClassMod_Part_Stat_Primary_AreaDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_AreaDamageRadius.ClassMod_Part_Stat_Primary_AreaDamageRadius',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_ActionSkillCooldownRate.ClassMod_Part_Stat_Primary_ActionSkillCooldownRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_MeleeDamage.ClassMod_Part_Stat_Primary_MeleeDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_HealthMax.ClassMod_Part_Stat_Primary_HealthMax',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_HealthRegen.ClassMod_Part_Stat_Primary_HealthRegen',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_ShieldCapacity.ClassMod_Part_Stat_Primary_ShieldCapacity',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_ShieldRegenDelay.ClassMod_Part_Stat_Primary_ShieldRegenDelay',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_ShieldRegenRate.ClassMod_Part_Stat_Primary_ShieldRegenRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_AssaultRifleDamage.ClassMod_Part_Stat_Primary_AssaultRifleDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_SMGDamage.ClassMod_Part_Stat_Primary_SMGDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_ShotgunDamage.ClassMod_Part_Stat_Primary_ShotgunDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_PistolDamage.ClassMod_Part_Stat_Primary_PistolDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_SniperRifleDamage.ClassMod_Part_Stat_Primary_SniperRifleDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_HeavyDamage.ClassMod_Part_Stat_Primary_HeavyDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Elemental/Resistance/ClassMod_Part_Stat_Primary_Elemental_Resistance_Normal.ClassMod_Part_Stat_Primary_Elemental_Resistance_Normal',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Elemental/Resistance/ClassMod_Part_Stat_Primary_Elemental_Resistance_Cryo.ClassMod_Part_Stat_Primary_Elemental_Resistance_Cryo',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Elemental/Resistance/ClassMod_Part_Stat_Primary_Elemental_Resistance_Fire.ClassMod_Part_Stat_Primary_Elemental_Resistance_Fire',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Elemental/Resistance/ClassMod_Part_Stat_Primary_Elemental_Resistance_Corrosive.ClassMod_Part_Stat_Primary_Elemental_Resistance_Corrosive',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Elemental/Resistance/ClassMod_Part_Stat_Primary_Elemental_Resistance_Radiation.ClassMod_Part_Stat_Primary_Elemental_Resistance_Radiation',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Elemental/Resistance/ClassMod_Part_Stat_Primary_Elemental_Resistance_Shock.ClassMod_Part_Stat_Primary_Elemental_Resistance_Shock',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Vladof_WeaponDamage.ClassMod_Part_Stat_Primary_Vladof_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Vladof_WeaponFireRate.ClassMod_Part_Stat_Primary_Vladof_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Vladof_WeaponReloadSpeed.ClassMod_Part_Stat_Primary_Vladof_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Vladof_WeaponAccuracy.ClassMod_Part_Stat_Primary_Vladof_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Torgue_WeaponDamage.ClassMod_Part_Stat_Primary_Torgue_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Torgue_WeaponReloadSpeed.ClassMod_Part_Stat_Primary_Torgue_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Torgue_WeaponAccuracy.ClassMod_Part_Stat_Primary_Torgue_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Torgue_WeaponProjectileSpeed.ClassMod_Part_Stat_Primary_Torgue_WeaponProjectileSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Tediore_WeaponReloadSpeed.ClassMod_Part_Stat_Primary_Tediore_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Tediore_WeaponAccurac.ClassMod_Part_Stat_Primary_Tediore_WeaponAccurac',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Tediore_WeaponDamage.ClassMod_Part_Stat_Primary_Tediore_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Tediore_WeaponFireRate.ClassMod_Part_Stat_Primary_Tediore_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Maliwan_WeaponDamage.ClassMod_Part_Stat_Primary_Maliwan_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Maliwan_WeaponFireRate.ClassMod_Part_Stat_Primary_Maliwan_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Maliwan_WeaponAccuracy.ClassMod_Part_Stat_Primary_Maliwan_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Maliwan_WeaponReloadSpeed.ClassMod_Part_Stat_Primary_Maliwan_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Jakobs_WeaponCriticalDamage.ClassMod_Part_Stat_Primary_Jakobs_WeaponCriticalDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Jakobs_WeaponDamage.ClassMod_Part_Stat_Primary_Jakobs_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Jakobs_WeaponReloadSpeed.ClassMod_Part_Stat_Primary_Jakobs_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Jakobs_WeaponAccuracy.ClassMod_Part_Stat_Primary_Jakobs_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_CoV_WeaponFireRate.ClassMod_Part_Stat_Primary_CoV_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_CoV_WeaponDamage.ClassMod_Part_Stat_Primary_CoV_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_CoV_WeaponAccuracy.ClassMod_Part_Stat_Primary_CoV_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Hyperion_WeaponCriticalDamage.ClassMod_Part_Stat_Primary_Hyperion_WeaponCriticalDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Hyperion_WeaponDamage.ClassMod_Part_Stat_Primary_Hyperion_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Hyperion_WeaponFireRate.ClassMod_Part_Stat_Primary_Hyperion_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Hyperion_WeaponReloadSpeed.ClassMod_Part_Stat_Primary_Hyperion_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Maliwan_WeaponAccuracy.ClassMod_Part_Stat_Primary_Maliwan_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_DAHL_WeaponReloadSpeed.ClassMod_Part_Stat_Primary_DAHL_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_DAHL_WeaponAccuracy.ClassMod_Part_Stat_Primary_DAHL_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_DAHL_WeaponDamage.ClassMod_Part_Stat_Primary_DAHL_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_DAHL_WeaponCriticalDamage.ClassMod_Part_Stat_Primary_DAHL_WeaponCriticalDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_DAHL_WeaponFireRate.ClassMod_Part_Stat_Primary_DAHL_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_ATLAS_WeaponFireRate.ClassMod_Part_Stat_Primary_ATLAS_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_ATLAS_WeaponReloadSpeed.ClassMod_Part_Stat_Primary_ATLAS_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_ATLAS_WeaponDamage.ClassMod_Part_Stat_Primary_ATLAS_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_ATLAS_WeaponCriticalDamage.ClassMod_Part_Stat_Primary_ATLAS_WeaponCriticalDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/ClassMod_Part_Stat_Secondary_ActionSkillCooldownRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/ClassMod_Part_Stat_Secondary_HealthMax',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/ClassMod_Part_Stat_Secondary_HealthRegen',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/ClassMod_Part_Stat_Secondary_MeleeDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/ClassMod_Part_Stat_Secondary_ShieldCapacity',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/ClassMod_Part_Stat_Secondary_ShieldRegenDelay',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/ClassMod_Part_Stat_Secondary_ShieldRegenRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/AOE/ClassMod_Part_Stat_Secondary_AreaDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/AOE/ClassMod_Part_Stat_Secondary_AreaDamageRadius',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/AOE/ClassMod_Part_Stat_Secondary_GrenadeDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/AOE/ClassMod_Part_Stat_Secondary_GrenadeRadius',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/AOE/ClassMod_Part_Stat_Secondary_GrenadeAmmo',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Weapon/ClassMod_Part_Stat_Secondary_Accuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Weapon/ClassMod_Part_Stat_Secondary_ChargeTime',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Weapon/ClassMod_Part_Stat_Secondary_CritDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Weapon/ClassMod_Part_Stat_Secondary_FireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Weapon/ClassMod_Part_Stat_Secondary_Handling',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Weapon/ClassMod_Part_Stat_Secondary_MagazineSize',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Weapon/ClassMod_Part_Stat_Secondary_ReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Weapon/ClassMod_Part_Stat_Secondary_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/WeaponType/ClassMod_Part_Stat_Secondary_AssaultRifleDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/WeaponType/ClassMod_Part_Stat_Secondary_HeavyDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/WeaponType/ClassMod_Part_Stat_Secondary_PistolDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/WeaponType/ClassMod_Part_Stat_Secondary_ShotgunDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/WeaponType/ClassMod_Part_Stat_Secondary_SMGDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/WeaponType/ClassMod_Part_Stat_Secondary_SniperRifleDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Torgue_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Torgue_WeaponProjectileSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Torgue_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Torgue_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Vladof_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Vladof_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Vladof_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Vladof_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_DAHL_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_DAHL_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_DAHL_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_DAHL_WeaponCriticalDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_DAHL_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Maliwan_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Maliwan_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Maliwan_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Maliwan_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Hyperion_WeaponCriticalDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Hyperion_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Hyperion_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Hyperion_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Jakobs_WeaponCriticalDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Jakobs_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Jakobs_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Jakobs_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Tediore_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Tediore_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Tediore_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_Tediore_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_CoV_WeaponAccuracy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_CoV_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_CoV_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_ATLAS_WeaponCriticalDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_ATLAS_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_ATLAS_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Manufacturer/ClassMod_Part_Stat_Secondary_ATLAS_WeaponReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Elemental/Resistance/ClassMod_Part_Stat_Secondary_Elemental_Resistance_Corrosive',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Elemental/Resistance/ClassMod_Part_Stat_Secondary_Elemental_Resistance_Cryo',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Elemental/Resistance/ClassMod_Part_Stat_Secondary_Elemental_Resistance_Fire',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Elemental/Resistance/ClassMod_Part_Stat_Secondary_Elemental_Resistance_Normal',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Elemental/Resistance/ClassMod_Part_Stat_Secondary_Elemental_Resistance_Radiation',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Secondary_Stat/Parts/Elemental/Resistance/ClassMod_Part_Stat_Secondary_Elemental_Resistance_Shock'
]

cmskills = [
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2',              #Eager to Impress               # 4 FriendBot, DE4DEYE, DarPaw, ThrillBot
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3',              #Who Rescued Who?               # 2 RedFang, Trainer
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4',              #Go for the Eyes!               # 2 DE4DEYE, DarPaw
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7',              #Ferocity                       # 4 FriendBot, Divergent, Trainer, T4mer
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11',             #He Bites!                      # 3 RedFang, Tr4iner, Trainer
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame',      #The most dangerous game        # 2 BountyHunter, Divergent
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry',       #Turn Tail and Run              # 2 BushMaster, SuperCharger
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy',             #Frenzy                         # 1 ThrillBot
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank',           #The Fast and the Furryous      # 3 BountyHunter, St4ckBot, FullAutomaton
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GeneticLink',        #Hive Mind                      # 1 FriendBot
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GotThisForYou',      #Psycho Head on a Stick         # 2 Tr4iner, DLC5
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount',          #Big Game                       # 2 CosmicStalker, OverDrive
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1',                #Furious Attack                 # 1 St4ckBot
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2',                #Sic 'Em                        # 1 C3md
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3',                #Rage and Recover               # 1 SuperCharger
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4',                #Self-Repairing System          # 2 RakkCommander, SuperCharger
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7',                #All My BFFs                    # 2 DarPaw, Divergent
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8',                #Overclocked                    # 1 FullAutomaton
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9',                #Hidden Machine                 # 1 BushMaster
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1',              #Leave No Trace                 # 2 DE4DEYE, FullAutomaton
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt2',              #Second Intention               # 1 St4ckBot
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5',              #Ambush Predator                # 2 BountyHunter, HeadCase
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye',         #HuntersEye                     # 2 CosmicStalker, HeadCase
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker',       #Interplanetary Stalker         # 1 CosmicStalker
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_LifeTraining',       #Who Rescued Who?2              # 1 DLC5
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis',          #Barbaric Yawp                  # 1 ThrillBot
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang',            #Two fang                       # 1 BushMaster         
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1',                      #Grim Harvest                   # 1 RakkCommander
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1',                        #Headcount                      # 1 HeadCase
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_PackTactics_Raid1',                      #Pack Tactics                   # 1 RakkCommander
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_Ferocity',                  #Ferocity2                      # 1 Tr4iner
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest',               #Grim Harvest2                  # 1 RakkPack
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_PackTac',                   #Pack Tactics2                  # 1 RakkPack
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_Furry_dlc1',            #The Fast and The Furious2      # 1 Peregrine
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1',       #Hunters Eyes2                  # 1 RakkPack
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_PackTac',               #Pack Tactics3                  # 1 Peregrine
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma',           #Ambush Predator2               # 1 OverDrive
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_EagerToImpress_Alisma',           #Eager To Impress2              # 1 C3md
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma',    #Interplanetary Stalker2        # 1 Peregrine
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4',                              #Better Toys                    # 1 OverDrive
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_11',                             #Not Even A Challenge           # 1 RedFang
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13',                             #Throatripper                   # 1 T4mer
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_15',                             #Keep Them Safe                 # 1 T4mer
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16',                             #Gotta Go Fast                  # 1 DLC5
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_18'                              #Capacitance                    # 1 C3md
]  

for bal in cmbal:
    mod.comment('Setting Each COM to Have its Own PartSet and Balance')
    mod.reg_hotfix(Mod.PATCH, '',
    bal,
    'BaseSelectionData',
    'None'
    )
    mod.newline()

for ps in cmpartset:
    mod.comment('Setting Each COM to Have its Own PartSet and Balance')
    mod.reg_hotfix(Mod.PATCH, '',
    ps,
    'ActorPartReplacementMode',
    'Additive'
    )
    mod.newline()

#############################
#######WORLD DROP LEG########
#############################

mod.comment('World Drop Legendaries')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod_Beastmaster_05_Legendary',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_05_Legendary',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=6
    ),
    (
        StartIndex=7,
        NumParts=1
    ),
    (
        StartIndex=7,
        NumParts=0
    ),
    (
        StartIndex=7,
        NumParts=0
    ),
    (
        StartIndex=7,
        NumParts=113
    ),
    (
        StartIndex=120,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_05_Legendary',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/BeastMaster/_Unique/Beastmaster_Unique_01/ClassMod_Part_Beastmaster_Unique_01_Friendbot.ClassMod_Part_Beastmaster_Unique_01_Friendbot,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_02/ClassMod_Part_Beastmaster_Unique_02_CosmicStalker.ClassMod_Part_Beastmaster_Unique_02_CosmicStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_03/ClassMod_Part_Beastmaster_Unique_03_BountyHunter.ClassMod_Part_Beastmaster_Unique_03_BountyHunter,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_04/ClassMod_Part_Beastmaster_Unique_04_DE4DEYE.ClassMod_Part_Beastmaster_Unique_04_DE4DEYE,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_05/ClassMod_Part_Beastmaster_Unique_05_RakkCommander.ClassMod_Part_Beastmaster_Unique_05_RakkCommander,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_06/ClassMod_Part_Beastmaster_Unique_06_RedFang.ClassMod_Part_Beastmaster_Unique_06_RedFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GeneticLink.ClassMod_Part_Skill_BeastMaster_GeneticLink,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GeneticLink.ClassMod_Part_Skill_BeastMaster_GeneticLink,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GeneticLink.ClassMod_Part_Skill_BeastMaster_GeneticLink,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_PackTactics_Raid1.CM_Part_Skill_BeastMaster_PackTactics_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_PackTactics_Raid1.CM_Part_Skill_BeastMaster_PackTactics_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_PackTactics_Raid1.CM_Part_Skill_BeastMaster_PackTactics_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_11.CM_Part_Skill_BSM_DLCSkill_11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_11.CM_Part_Skill_BSM_DLCSkill_11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_11.CM_Part_Skill_BSM_DLCSkill_11,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
    """
)
mod.newline()

#############################
########FRIEND BOT###########
#############################

mod.comment('Friend Bot')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_FriendBot',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_FriendBot',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=1
    ),
    (
        StartIndex=2,
        NumParts=1
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=113
    ),
    (
        StartIndex=116,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_FriendBot',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/BeastMaster/_Unique/Beastmaster_Unique_01/ClassMod_Part_Beastmaster_Unique_01_Friendbot.ClassMod_Part_Beastmaster_Unique_01_Friendbot,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GeneticLink.ClassMod_Part_Skill_BeastMaster_GeneticLink,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GeneticLink.ClassMod_Part_Skill_BeastMaster_GeneticLink,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GeneticLink.ClassMod_Part_Skill_BeastMaster_GeneticLink,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
    """
)
mod.newline()

mod.comment('Giving Eager To Impress to the FriendBot')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/BeastMaster/_Unique/Beastmaster_Unique_01/ClassMod_Part_Beastmaster_Unique_01_Friendbot.ClassMod_Part_Beastmaster_Unique_01_Friendbot','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Hive Mind to the FriendBot')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GeneticLink.ClassMod_Part_Skill_BeastMaster_GeneticLink',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/BeastMaster/_Unique/Beastmaster_Unique_01/ClassMod_Part_Beastmaster_Unique_01_Friendbot.ClassMod_Part_Beastmaster_Unique_01_Friendbot','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Ferocity to the FriendBot')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/BeastMaster/_Unique/Beastmaster_Unique_01/ClassMod_Part_Beastmaster_Unique_01_Friendbot.ClassMod_Part_Beastmaster_Unique_01_Friendbot','BlueprintGeneratedClass')
)
mod.newline()

#############################
#######COSMIC STALKER########
#############################

mod.comment('Cosmic Stalker')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_CosmicStalker',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_CosmicStalker',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=1
    ),
    (
        StartIndex=2,
        NumParts=1
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=113
    ),
    (
        StartIndex=116,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_CosmicStalker',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_02/ClassMod_Part_Beastmaster_Unique_02_CosmicStalker.ClassMod_Part_Beastmaster_Unique_02_CosmicStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
"""
)
mod.newline()

mod.comment('Giving Hunters Eye to the CosmicStalker')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_02/ClassMod_Part_Beastmaster_Unique_02_CosmicStalker.ClassMod_Part_Beastmaster_Unique_02_CosmicStalker','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Big Game to the CosmicStalker')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker.ClassMod_Part_Skill_BeastMaster_InterStalker',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_02/ClassMod_Part_Beastmaster_Unique_02_CosmicStalker.ClassMod_Part_Beastmaster_Unique_02_CosmicStalker','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Interplanetary Stalker to the CosmicStalker')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_02/ClassMod_Part_Beastmaster_Unique_02_CosmicStalker.ClassMod_Part_Beastmaster_Unique_02_CosmicStalker','BlueprintGeneratedClass')
)
mod.newline()

#############################
#######BOUNTY HUNTER#########
#############################

mod.comment('Bounty Hunter')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_BountyHunter',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_BountyHunter',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=1
    ),
    (
        StartIndex=2,
        NumParts=1
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=113
    ),
    (
        StartIndex=116,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_BountyHunter',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_03/ClassMod_Part_Beastmaster_Unique_03_BountyHunter.ClassMod_Part_Beastmaster_Unique_03_BountyHunter,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
"""
)
mod.newline()

mod.comment('Giving The Fast And The Furrious to the BountyHunter')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_03/ClassMod_Part_Beastmaster_Unique_03_BountyHunter.ClassMod_Part_Beastmaster_Unique_03_BountyHunter','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Dangerous Game to the BountyHunter')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_03/ClassMod_Part_Beastmaster_Unique_03_BountyHunter.ClassMod_Part_Beastmaster_Unique_03_BountyHunter','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Ambush Predator to the BountyHunter')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_03/ClassMod_Part_Beastmaster_Unique_03_BountyHunter.ClassMod_Part_Beastmaster_Unique_03_BountyHunter','BlueprintGeneratedClass')
)
mod.newline()

#############################
##########DE4DEYE############
#############################

mod.comment('DE4DEYE')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_DE4DEYE',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_DE4DEYE',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=1
    ),
    (
        StartIndex=2,
        NumParts=1
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=113
    ),
    (
        StartIndex=116,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_DE4DEYE',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_04/ClassMod_Part_Beastmaster_Unique_04_DE4DEYE.ClassMod_Part_Beastmaster_Unique_04_DE4DEYE,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
"""
)
mod.newline()

mod.comment('Giving Eager To Impress to the DE4DEYE')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_04/ClassMod_Part_Beastmaster_Unique_04_DE4DEYE.ClassMod_Part_Beastmaster_Unique_04_DE4DEYE','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Go For The Eyes to the DE4DEYE')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_04/ClassMod_Part_Beastmaster_Unique_04_DE4DEYE.ClassMod_Part_Beastmaster_Unique_04_DE4DEYE','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Leave No Trace to the DE4DEYE')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_04/ClassMod_Part_Beastmaster_Unique_04_DE4DEYE.ClassMod_Part_Beastmaster_Unique_04_DE4DEYE','BlueprintGeneratedClass')
)
mod.newline()

#############################
######RAKK COMMANDER#########
#############################

mod.comment('RakkCommander')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_RakkCommander',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RakkCommander',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=1
    ),
    (
        StartIndex=2,
        NumParts=1
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=113
    ),
    (
        StartIndex=116,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RakkCommander',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_05/ClassMod_Part_Beastmaster_Unique_05_RakkCommander.ClassMod_Part_Beastmaster_Unique_05_RakkCommander,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_PackTactics_Raid1.CM_Part_Skill_BeastMaster_PackTactics_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_PackTactics_Raid1.CM_Part_Skill_BeastMaster_PackTactics_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_PackTactics_Raid1.CM_Part_Skill_BeastMaster_PackTactics_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
)
"""
)
mod.newline()

mod.comment('Giving Grim Harvest to the Rakk Commander')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1.CM_Part_Skill_BeastMaster_GrimHarvest_Raid1',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/BeastMaster/_Unique/Beastmaster_Unique_05/ClassMod_Part_Beastmaster_Unique_05_RakkCommander.ClassMod_Part_Beastmaster_Unique_05_RakkCommander','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Self Repairing System to the Rakk Commander')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_05/ClassMod_Part_Beastmaster_Unique_05_RakkCommander.ClassMod_Part_Beastmaster_Unique_05_RakkCommander','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Pack Tactics to the Rakk Commander')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_PackTactics_Raid1.CM_Part_Skill_BeastMaster_PackTactics_Raid1',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_05/ClassMod_Part_Beastmaster_Unique_05_RakkCommander.ClassMod_Part_Beastmaster_Unique_05_RakkCommander','BlueprintGeneratedClass')
)
mod.newline()

#############################
##########RED FANG###########
#############################

mod.comment('Red Fang')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_RedFang',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RedFang',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=1
    ),
    (
        StartIndex=2,
        NumParts=1
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=113
    ),
    (
        StartIndex=116,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RedFang',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_06/ClassMod_Part_Beastmaster_Unique_06_RedFang.ClassMod_Part_Beastmaster_Unique_06_RedFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_11.CM_Part_Skill_BSM_DLCSkill_11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_11.CM_Part_Skill_BSM_DLCSkill_11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_11.CM_Part_Skill_BSM_DLCSkill_11,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
)
"""
)
mod.newline()

mod.comment('Giving He Bites ! to the Red Fang')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_06/ClassMod_Part_Beastmaster_Unique_06_RedFang','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Who Rescued Who ? to the Red Fang')
mod.reg_hotfix(Mod.PATCH, '',
'Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_06/ClassMod_Part_Beastmaster_Unique_06_RedFang','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Not Even a Challenge to the Red Fang')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_11.CM_Part_Skill_BSM_DLCSkill_11',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/_Unique/Beastmaster_Unique_06/ClassMod_Part_Beastmaster_Unique_06_RedFang','BlueprintGeneratedClass')
)
mod.newline()

#############################
##########RAKK PACK##########
#############################

mod.comment('Rakk Pack')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/PartSet_CM_Beastmaster_Raid1',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=1
    ),
    (
        StartIndex=2,
        NumParts=1
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=113
    ),
    (
        StartIndex=116,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/Part_CM_Beastmaster_Raid1.Part_CM_Beastmaster_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1.ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1.ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1.ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1.ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1.ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest.ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest.ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest.ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest.ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest.ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_PackTac.ClassMod_Part_Skill_Hib_BeastMaster_PackTac,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_PackTac.ClassMod_Part_Skill_Hib_BeastMaster_PackTac,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_PackTac.ClassMod_Part_Skill_Hib_BeastMaster_PackTac,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
)
"""
)
mod.newline()

mod.comment('Giving Pack Tactics to the Rakk Pack')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_PackTac.ClassMod_Part_Skill_Hib_BeastMaster_PackTac',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/Part_CM_Beastmaster_Raid1.Part_CM_Beastmaster_Raid1','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Grim Harvest to the Rakk Pack')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest.ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/Part_CM_Beastmaster_Raid1.Part_CM_Beastmaster_Raid1','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Hunters Eye to the Rakk Pack')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1.ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/Part_CM_Beastmaster_Raid1.Part_CM_Beastmaster_Raid1','BlueprintGeneratedClass')
)
mod.newline()

#############################
##########STACKBOT###########
#############################

mod.comment('StackBot')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/PartSet_CM_Beastmaster_DLC1',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_DLC1',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=1
    ),
    (
        StartIndex=2,
        NumParts=1
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=113
    ),
    (
        StartIndex=116,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_DLC1',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Part_CM_Beastmaster_DLC1.Part_CM_Beastmaster_DLC1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt2.ClassMod_Part_Skill_BeastMaster_Hunt2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt2.ClassMod_Part_Skill_BeastMaster_Hunt2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt2.ClassMod_Part_Skill_BeastMaster_Hunt2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt2.ClassMod_Part_Skill_BeastMaster_Hunt2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt2.ClassMod_Part_Skill_BeastMaster_Hunt2,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
"""
)
mod.newline()

mod.comment('Giving The Fast And The Furrious to the StackBot')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Part_CM_Beastmaster_DLC1.Part_CM_Beastmaster_DLC1','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Furrious Attack to the StackBot')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Part_CM_Beastmaster_DLC1.Part_CM_Beastmaster_DLC1','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Second Intention to the StackBot')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt2.ClassMod_Part_Skill_BeastMaster_Hunt2',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Part_CM_Beastmaster_DLC1.Part_CM_Beastmaster_DLC1','BlueprintGeneratedClass')
)
mod.newline()

#############################
##########TRAINER###########
#############################

mod.comment('Trainer')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/PartSet_CM_Beastmaster_Hib',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Hib',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=1
    ),
    (
        StartIndex=2,
        NumParts=1
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=113
    ),
    (
        StartIndex=116,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Hib',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/Part_CM_Beastmaster_Hib.Part_CM_Beastmaster_Hib,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GotThisForYou.ClassMod_Part_Skill_BeastMaster_GotThisForYou,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_Ferocity.ClassMod_Part_Skill_Hib_BeastMaster_Ferocity,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_Ferocity.ClassMod_Part_Skill_Hib_BeastMaster_Ferocity,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_Ferocity.ClassMod_Part_Skill_Hib_BeastMaster_Ferocity,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_Ferocity.ClassMod_Part_Skill_Hib_BeastMaster_Ferocity,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_Ferocity.ClassMod_Part_Skill_Hib_BeastMaster_Ferocity,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
"""
)
mod.newline()

mod.comment('Giving Ferocity to the Trainer')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_Ferocity.ClassMod_Part_Skill_Hib_BeastMaster_Ferocity',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/Part_CM_Beastmaster_Hib.Part_CM_Beastmaster_Hib','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving He Bites ! to the Trainer')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/Part_CM_Beastmaster_Hib.Part_CM_Beastmaster_Hib','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Psycho Head to the Trainer')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GotThisForYou.ClassMod_Part_Skill_BeastMaster_GotThisForYou',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/Part_CM_Beastmaster_Hib.Part_CM_Beastmaster_Hib','BlueprintGeneratedClass')
)
mod.newline()

#############################
##########PEREGRINE##########
#############################

mod.comment('Peregrine')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/PartSet_CM_Beastmaster_Alisma',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=5,Max=5),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Alisma',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=1
    ),
    (
        StartIndex=2,
        NumParts=1
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=0
    ),
    (
        StartIndex=3,
        NumParts=113
    ),
    (
        StartIndex=116,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Alisma',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/Part_CM_Beastmaster_Alisma.Part_CM_Beastmaster_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_05_Legendary.ClassMod_Part_Beastmaster_Rarity_05_Legendary,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma.ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma.ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma.ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma.ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma.ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_Furry_dlc1.ClassMod_Part_Skill_BeastMaster_Furry_dlc1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_Furry_dlc1.ClassMod_Part_Skill_BeastMaster_Furry_dlc1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_Furry_dlc1.ClassMod_Part_Skill_BeastMaster_Furry_dlc1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_PackTac.ClassMod_Part_Skill_BeastMaster_PackTac,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_PackTac.ClassMod_Part_Skill_BeastMaster_PackTac,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_PackTac.ClassMod_Part_Skill_BeastMaster_PackTac,Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0)),
    (PartData='',Weight=(BaseValueConstant=1.0))
"""
)
mod.newline()

mod.comment('Giving Interplanetary Stalker to the Peregrine')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma.ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/Part_CM_Beastmaster_Alisma.Part_CM_Beastmaster_Alisma','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Pack Tactics to the Peregrine')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_PackTac.ClassMod_Part_Skill_BeastMaster_PackTac',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/Part_CM_Beastmaster_Alisma.Part_CM_Beastmaster_Alisma','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving The Fast And The Furrious to the Peregrine')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_Furry_dlc1.ClassMod_Part_Skill_BeastMaster_Furry_dlc1',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/Part_CM_Beastmaster_Alisma.Part_CM_Beastmaster_Alisma','BlueprintGeneratedClass')
)
mod.newline()

#############################
###########COMMON############
#############################

mod.comment('Common')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod_Beastmaster_01_Common',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=4,Max=4),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_01_Common',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=10
    ),
    (
        StartIndex=11,
        NumParts=1
    ),
    (
        StartIndex=12,
        NumParts=0
    ),
    (
        StartIndex=12,
        NumParts=0
    ),
    (
        StartIndex=12,
        NumParts=113
    ),
    (
        StartIndex=125,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_01_Common',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_01_QuickCharge.ClassMod_Part_Mod_Beastmaster_01_QuickCharge,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_02_Divergent.ClassMod_Part_Mod_Beastmaster_02_Divergent,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_03_Bushmaster.ClassMod_Part_Mod_Beastmaster_03_Bushmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_04_Whistleblower.ClassMod_Part_Mod_Beastmaster_04_Whistleblower,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_05_DARPAW.ClassMod_Part_Mod_Beastmaster_05_DARPAW,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_06_Overdriven.ClassMod_Part_Mod_Beastmaster_06_Overdriven,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_07_Thrillbotting.ClassMod_Part_Mod_Beastmaster_07_Thrillbotting,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_08_TurboCharged.ClassMod_Part_Mod_Beastmaster_08_TurboCharged,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_09_Headcase.ClassMod_Part_Mod_Beastmaster_09_Headcase,Weight=(BaseValueConstant=1.0)),   
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_10_Botmaster.ClassMod_Part_Mod_Beastmaster_10_Botmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_01_Common.ClassMod_Part_Beastmaster_Rarity_01_Common,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0))
    
"""
)
mod.newline()

#############################
##########UNCOMMON###########
#############################

mod.comment('Uncommon')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod_Beastmaster_02_Uncommon',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=6,Max=6),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_02_Uncommon',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=10
    ),
    (
        StartIndex=11,
        NumParts=1
    ),
    (
        StartIndex=12,
        NumParts=0
    ),
    (
        StartIndex=12,
        NumParts=0
    ),
    (
        StartIndex=12,
        NumParts=113
    ),
    (
        StartIndex=125,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_02_Uncommon',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_01_QuickCharge.ClassMod_Part_Mod_Beastmaster_01_QuickCharge,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_02_Divergent.ClassMod_Part_Mod_Beastmaster_02_Divergent,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_03_Bushmaster.ClassMod_Part_Mod_Beastmaster_03_Bushmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_04_Whistleblower.ClassMod_Part_Mod_Beastmaster_04_Whistleblower,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_05_DARPAW.ClassMod_Part_Mod_Beastmaster_05_DARPAW,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_06_Overdriven.ClassMod_Part_Mod_Beastmaster_06_Overdriven,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_07_Thrillbotting.ClassMod_Part_Mod_Beastmaster_07_Thrillbotting,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_08_TurboCharged.ClassMod_Part_Mod_Beastmaster_08_TurboCharged,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_09_Headcase.ClassMod_Part_Mod_Beastmaster_09_Headcase,Weight=(BaseValueConstant=1.0)),   
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_10_Botmaster.ClassMod_Part_Mod_Beastmaster_10_Botmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_02_Uncommon.ClassMod_Part_Beastmaster_Rarity_02_Uncommon,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0))
    
"""
)
mod.newline()

#############################
############RARE#############
#############################

mod.comment('Rare')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod_Beastmaster_03_Rare',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=8,Max=8),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_03_Rare',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=10
    ),
    (
        StartIndex=11,
        NumParts=1
    ),
    (
        StartIndex=12,
        NumParts=0
    ),
    (
        StartIndex=12,
        NumParts=0
    ),
    (
        StartIndex=12,
        NumParts=113
    ),
    (
        StartIndex=125,
        NumParts=0
    )
)
"""
)
mod.newline()


mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_03_Rare',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_01_QuickCharge.ClassMod_Part_Mod_Beastmaster_01_QuickCharge,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_02_Divergent.ClassMod_Part_Mod_Beastmaster_02_Divergent,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_03_Bushmaster.ClassMod_Part_Mod_Beastmaster_03_Bushmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_04_Whistleblower.ClassMod_Part_Mod_Beastmaster_04_Whistleblower,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_05_DARPAW.ClassMod_Part_Mod_Beastmaster_05_DARPAW,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_06_Overdriven.ClassMod_Part_Mod_Beastmaster_06_Overdriven,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_07_Thrillbotting.ClassMod_Part_Mod_Beastmaster_07_Thrillbotting,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_08_TurboCharged.ClassMod_Part_Mod_Beastmaster_08_TurboCharged,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_09_Headcase.ClassMod_Part_Mod_Beastmaster_09_Headcase,Weight=(BaseValueConstant=1.0)),   
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_10_Botmaster.ClassMod_Part_Mod_Beastmaster_10_Botmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_03_Rare.ClassMod_Part_Beastmaster_Rarity_03_Rare,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0))
"""
)
mod.newline()

#############################
##########VERYRARE###########
#############################

mod.comment('Very Rare')

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod_Beastmaster_04_VeryRare',
'ActorPartLists',
"""
(
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=1,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=3,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=5,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=10,Max=10),bEnabled=False,Parts=()),
    (PartTypeEnum=/Game/Gear/ClassMods/_Design/_Data/EPartList_ClassMod.EPartList_ClassMod,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=())    
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_04_VeryRare',
'RuntimePartList.PartTypeTOC',
"""
(
    (
        StartIndex=0,
        NumParts=1
    ),
    (
        StartIndex=1,
        NumParts=10
    ),
    (
        StartIndex=11,
        NumParts=1
    ),
    (
        StartIndex=12,
        NumParts=0
    ),
    (
        StartIndex=12,
        NumParts=0
    ),
    (
        StartIndex=12,
        NumParts=113
    ),
    (
        StartIndex=125,
        NumParts=0
    )
)
"""
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_04_VeryRare',
'RuntimePartList.AllParts',
"""
(
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Character/ClassMod_Part_Character_Beastmaster.ClassMod_Part_Character_Beastmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_01_QuickCharge.ClassMod_Part_Mod_Beastmaster_01_QuickCharge,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_02_Divergent.ClassMod_Part_Mod_Beastmaster_02_Divergent,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_03_Bushmaster.ClassMod_Part_Mod_Beastmaster_03_Bushmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_04_Whistleblower.ClassMod_Part_Mod_Beastmaster_04_Whistleblower,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_05_DARPAW.ClassMod_Part_Mod_Beastmaster_05_DARPAW,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_06_Overdriven.ClassMod_Part_Mod_Beastmaster_06_Overdriven,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_07_Thrillbotting.ClassMod_Part_Mod_Beastmaster_07_Thrillbotting,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_08_TurboCharged.ClassMod_Part_Mod_Beastmaster_08_TurboCharged,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_09_Headcase.ClassMod_Part_Mod_Beastmaster_09_Headcase,Weight=(BaseValueConstant=1.0)),   
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_10_Botmaster.ClassMod_Part_Mod_Beastmaster_10_Botmaster,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Rarity/ClassMod_Part_Beastmaster_Rarity_04_VeryRare.ClassMod_Part_Beastmaster_Rarity_04_VeryRare,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1.ClassMod_Part_Skill_BeastMaster_HR1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0)),
    (PartData=/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16,Weight=(BaseValueConstant=1.0))
"""
)
mod.newline()

###QUICKCHARGE

mod.comment('Giving Turn Tail And Run to the QuickCharge')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_01_QuickCharge.ClassMod_Part_Mod_Beastmaster_01_QuickCharge','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Self Repairing Systems to the QuickCharge')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4.ClassMod_Part_Skill_BeastMaster_HR4',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_01_QuickCharge.ClassMod_Part_Mod_Beastmaster_01_QuickCharge','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving rage and Recover to the QuickCharge')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3.ClassMod_Part_Skill_BeastMaster_HR3',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_01_QuickCharge.ClassMod_Part_Mod_Beastmaster_01_QuickCharge','BlueprintGeneratedClass')
)
mod.newline()

###DIVERGENT

mod.comment('Giving The Most Dangerous Game to the Divergent')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame.ClassMod_Part_Skill_BeastMaster_DangerousGame',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_02_Divergent.ClassMod_Part_Mod_Beastmaster_02_Divergent','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving All My BFFs to the Divergent')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_02_Divergent.ClassMod_Part_Mod_Beastmaster_02_Divergent','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Ferocity to the Divergent')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_02_Divergent.ClassMod_Part_Mod_Beastmaster_02_Divergent','BlueprintGeneratedClass')
)
mod.newline()

###BUSHMASTER

mod.comment('Giving Hidden Machine to the BushMaster')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9.ClassMod_Part_Skill_BeastMaster_HR9',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_03_Bushmaster.ClassMod_Part_Mod_Beastmaster_03_Bushmaster','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Turn Tail and Run to the BushMaster')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry.ClassMod_Part_Skill_BeastMaster_FastAndFurry',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_03_Bushmaster.ClassMod_Part_Mod_Beastmaster_03_Bushmaster','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Two Fang to the BushMaster')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang.ClassMod_Part_Skill_BeastMaster_TwoFang',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_03_Bushmaster.ClassMod_Part_Mod_Beastmaster_03_Bushmaster','BlueprintGeneratedClass')
)
mod.newline()

###WHISTLEBLOWER

mod.comment('Giving Who Rescued Who ? to the WhistleBlower')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3.ClassMod_Part_Skill_BeastMaster_Bond3',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_04_Whistleblower.ClassMod_Part_Mod_Beastmaster_04_Whistleblower','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Ferocity to the WhistleBlower')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7',
'Dependencies.Dependencies[2]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_04_Whistleblower.ClassMod_Part_Mod_Beastmaster_04_Whistleblower','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving He Bites ! to the WhistleBlower')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11.ClassMod_Part_Skill_BeastMaster_Bond11',
'Dependencies.Dependencies[2]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_04_Whistleblower.ClassMod_Part_Mod_Beastmaster_04_Whistleblower','BlueprintGeneratedClass')
)
mod.newline()

###DARPAW

mod.comment('Giving Eager To Impress to the DarPaw')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2',
'Dependencies.Dependencies[2]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_05_DARPAW.ClassMod_Part_Mod_Beastmaster_05_DARPAW','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving All My BFFs to the DarPaw')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7.ClassMod_Part_Skill_BeastMaster_HR7',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_05_DARPAW.ClassMod_Part_Mod_Beastmaster_05_DARPAW','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Go For the Eyes to the DarPaw')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4.ClassMod_Part_Skill_BeastMaster_Bond4',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_05_DARPAW.ClassMod_Part_Mod_Beastmaster_05_DARPAW','BlueprintGeneratedClass')
)
mod.newline()

###OVERDRIVEN

mod.comment('Giving Big Game to the OverDriven')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount.ClassMod_Part_Skill_BeastMaster_HeadCount',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_06_Overdriven.ClassMod_Part_Mod_Beastmaster_06_Overdriven','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Better Toys to the OverDriven')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4.CM_Part_Skill_BSM_DLCSkill_4',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_06_Overdriven.ClassMod_Part_Mod_Beastmaster_06_Overdriven','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Ambush Predator to the OverDriven')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma.ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_06_Overdriven.ClassMod_Part_Mod_Beastmaster_06_Overdriven','BlueprintGeneratedClass')
)
mod.newline()

###TURBOCHARGED

mod.comment('Giving The Fast and the Furryous to the TurboCharged')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank.ClassMod_Part_Skill_BeastMaster_FullTank',
'Dependencies.Dependencies[2]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_08_TurboCharged.ClassMod_Part_Mod_Beastmaster_08_TurboCharged','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving OverClocked to the TurboCharged')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8.ClassMod_Part_Skill_BeastMaster_HR8',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_08_TurboCharged.ClassMod_Part_Mod_Beastmaster_08_TurboCharged','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Leave No Trace to the TurboCharged')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1.ClassMod_Part_Skill_BeastMaster_Hunt1',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_08_TurboCharged.ClassMod_Part_Mod_Beastmaster_08_TurboCharged','BlueprintGeneratedClass')
)
mod.newline()

###THRILLBOTTING

mod.comment('Giving Eager To Impress to the Thrillbot')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2.ClassMod_Part_Skill_BeastMaster_Bond2',
'Dependencies.Dependencies[3]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_07_Thrillbotting.ClassMod_Part_Mod_Beastmaster_07_Thrillbotting','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Frenzy to the Thrillbot')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy.ClassMod_Part_Skill_BeastMaster_Frenzy',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_07_Thrillbotting.ClassMod_Part_Mod_Beastmaster_07_Thrillbotting','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Barbaric Yawp to the Thrillbot')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis.ClassMod_Part_Skill_BeastMaster_Symbiosis',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_07_Thrillbotting.ClassMod_Part_Mod_Beastmaster_07_Thrillbotting','BlueprintGeneratedClass')
)
mod.newline()

###HEADCASE

mod.comment('Giving Head Count to the HeadCase')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1.CM_Part_Skill_BeastMaster_HeadCount_Raid1',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_09_Headcase.ClassMod_Part_Mod_Beastmaster_09_Headcase','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Ambush Predator to the HeadCase')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5.ClassMod_Part_Skill_BeastMaster_Hunt5',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_09_Headcase.ClassMod_Part_Mod_Beastmaster_09_Headcase','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Hunters Eye to the HeadCase')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye.ClassMod_Part_Skill_BeastMaster_HuntersEye',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_09_Headcase.ClassMod_Part_Mod_Beastmaster_09_Headcase','BlueprintGeneratedClass')
)
mod.newline()

###BOTMASTER

mod.comment('Giving Ferocity to the BotMaster')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7.ClassMod_Part_Skill_BeastMaster_Bond7',
'Dependencies.Dependencies[3]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_10_Botmaster.ClassMod_Part_Mod_Beastmaster_10_Botmaster','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving ThroatRipper to the BotMaster')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13.CM_Part_Skill_BSM_DLCSkill_13',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_10_Botmaster.ClassMod_Part_Mod_Beastmaster_10_Botmaster','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving SicEm to the BotMaster')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2.ClassMod_Part_Skill_BeastMaster_HR2',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/Gear/ClassMods/_Design/PartSets/Part_ClassMod/Beastmaster/ClassMod_Part_Mod_Beastmaster_10_Botmaster.ClassMod_Part_Mod_Beastmaster_10_Botmaster','BlueprintGeneratedClass')
)
mod.newline()

###DLC5

mod.comment('Giving Psycho Head On a Stick to the DLC5')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GotThisForYou.ClassMod_Part_Skill_BeastMaster_GotThisForYou',
'Dependencies.Dependencies[1]',
Mod.get_full_cond('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/ClassMod_Part_Mod_BSM_Ixora_01.ClassMod_Part_Mod_BSM_Ixora_01','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Who Rescued Who ? to the DLC5')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_LifeTraining.ClassMod_Part_Skill_BeastMaster_LifeTraining',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/ClassMod_Part_Mod_BSM_Ixora_01.ClassMod_Part_Mod_BSM_Ixora_01','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Gotta Go Fast to the DLC5')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16.CM_Part_Skill_BSM_DLCSkill_16',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/ClassMod_Part_Mod_BSM_Ixora_01.ClassMod_Part_Mod_BSM_Ixora_01','BlueprintGeneratedClass')
)
mod.newline()

###C3MD

mod.comment('Giving Kepp Them Safe to the C3MD')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_15.CM_Part_Skill_BSM_DLCSkill_15',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/L01/Part_CM_Ixora_BSM_L01.Part_CM_Ixora_BSM_L01','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Eager To Impress to the C3MD')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_EagerToImpress_Alisma.ClassMod_Part_Skill_BeastMaster_EagerToImpress_Alisma',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/L01/Part_CM_Ixora_BSM_L01.Part_CM_Ixora_BSM_L01','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Giving Capacitance to the C3MD')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_18.CM_Part_Skill_BSM_DLCSkill_18',
'Dependencies.Dependencies[0]',
Mod.get_full_cond('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/L01/Part_CM_Ixora_BSM_L01.Part_CM_Ixora_BSM_L01','BlueprintGeneratedClass')
)
mod.newline()

