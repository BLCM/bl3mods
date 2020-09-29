from bl3hotfixmod import Mod

# Just make them have 0 drop rate 4hed
# Adjust each anoint's weight to be really high apparently?



mod=Mod('no_anoint_balance.bl3hotfix',
'No Anoint Balance Pass',
'SSpyR',
[
    'No Anoints.',
    'Need to update.'
],
lic=Mod.CC_BY_SA_40,
cats='gear-anointments'
)

anoints=[
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_AccuracyHandling/GPart_All_SkillEnd_AccuracyHandling',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_CooldownRate/GPart_All_SkillEnd_CooldownRate',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_CritDamage/GPart_All_SkillEnd_CritDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_DamageReduction/GPart_All_SkillEnd_DamageReduction',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_EleChanceDamage/GPart_All_SkillEnd_EleChanceDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_FireRateReload/GPart_All_SkillEnd_FireRateReload',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_HealthRegen/GPart_All_SkillEnd_HealthRegen',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_LifeSteal/GPart_All_SkillEnd_LifeSteal',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_MeleeDamage/GPart_All_SkillEnd_MeleeDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_MoveSpeed/GPart_All_SkillEnd_MoveSpeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Corrosive/GPart_All_SkillEnd_NextMagBonusDamageCorrosive',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Cryo/GPart_All_SkillEnd_NextMagBonusDamageCryo',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Fire/GPart_All_SkillEnd_NextMagBonusDamageFire',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Radiation/GPart_All_SkillEnd_NextMagBonusDamageRadiation',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Shock/GPart_All_SkillEnd_NextMagBonusDamageShock',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_ProjectileSpeed/GPart_All_SkillEnd_ProjectileSpeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_SplashDamage/GPart_All_SkillEnd_SplashDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_UniqueEnemyDamage/GPart_All_SkillEnd_UniqueEnemyDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_WeaponDamage/GPart_All_SkillEnd_WeaponDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillStart_AddGrenade/GPart_All_SkillEnd_AddGrenade',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/AttackCommandLifeSteal/GPart_Beast_AttackCmd_Lifesteal',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/AttackCommandMovespeed/GPart_Beast_AttackCmd_Movespeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/Beast_Gamma_BonusRadiationDamage/GPart_BonusRadiationDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkAttackCharge/GPart_Beast_RakkCharge',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkSlag/GPart_Beast_RakkSlag',
    'Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkUsed_CritDamage/GPart_Beast_RakkCrit',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/StealthAccuracyHandling/GPart_Beast_Stealth_AccuracyHandling',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/StealthNova/GPart_Beast_ExitStealthNova',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/AutoBear_AmmoRegen/GPart_Gunner_AutoBear_AmmoRegen',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/AutoBear_FireDamage/GPart_Gunner_AutoBear_FireDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/EnterExit_Nova/GPart_Gunner_EnterExit_Nova',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_KillsLowerCooldown/GPart_Gunner_KillsLowerCooldown',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagFireDamage/GPart_Gunner_NextMagFireDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagFirerateCrit/GPart_Gunner_NextMagFirerateCrit',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagReloadHandling/GPart_Gunner_NextMagReloadHandling',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NoAmmoConsumption/GPart_Gunner_NoAmmoConsumption',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_ShieldMaxHealth/GPart_Gunner_ShieldHealthMax',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_SplashDamageIncrease/GPart_Gunner_SplashDamageIncrease',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/IBActive_ChanceGrenade/GPart_Gunner_IBGrenadeChance',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/BarrierActive_StatusEffectChance/GPart_Operative_BarrierActive_StatusEffectChance',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/BarrierActiveAccuracyCrit/GPart_Operative_BarrierActive_AccuracyCrit',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/BarrierDeployShieldRecharge/GPart_Operative_BarrierDeploy_ShieldRecharge',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneActiveHealthRegen/GPart_Operative_CloneActive_HealthRegen',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneActiveRegenAmmo/GPart_Operative_CloneActive_AmmoRegen',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneSwapDamage/GPart_CloneSwap_WeaponDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneSwapInstaReload/GPart_Operative_CloneSwapInstaReload',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveBonusDamage/GPart_Operative_DroneActiveBonusDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveFireRateReload/GPart_Operative_DroneActive_FireRateReload',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveMovespeed/GPart_Operative_DroneActiveMovespeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Cast_EleChance/GPart_Siren_Cast_ElementalChance',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Cast_WeaponDamage/GPart_Siren_Cast_WeaponDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_AccuracyCrit/GPart_Siren_Grasp_AccuracyCrit',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_ChargeSpeed/GPart_Siren_Grasp_ChargeSpeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_ConstantNova/GPart_Siren_Grasp_ConstantNova',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/SkillEnd_AttunedEleDamage/GPart_Siren_SkillEnd_AttunedSkillDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_DamageReduction/GPart_Siren_Slam_DamageReduction',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_MeleeDamage/GPart_Siren_Slam_MeleeDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_ReturnDamage/GPart_Siren_Slam_ReturnDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_WeaponDamage/GPart_Siren_Slam_WeaponDamage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/ConsecutiveHits_DmgStack/GPart_EG_Generic_ConsecutiveHitsDmgStack',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/GrenadeThrow_GlobalDamage/GPart_EG_GrenadeThrow_GlobalDamage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/KillStack_ReloadDamage/GPart_EG_Generic_KillStackReloadDamage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/LowHealth_Executor/GPart_EG_Generic_LowHealthExecutor',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/ModeSwitch_WeaponDamage/GPart_EG_ModeSwitch_WeaponDamage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Corrosive/GPart_EG_SkillEndBonusEleDamage_Corrosive',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Cryo/GPart_EG_SkillEndBonusEleDamage_Cryo',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Fire/GPart_EG_SkillEndBonusEleDamage_Fire',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Radiation/GPart_EG_SkillEndBonusEleDamage_Radiation',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Shock/GPart_EG_SkillEndBonusEleDamage_Shock',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/AccuracyAndHandling/GPart_EG_WhileAirborn_AccuracyHandling',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/CritDamage/GPart_EG_WhileAirborn_CritDamage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/Damage/GPart_EG_WhileAirborn_Damage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/FireRate/GPart_EG_WhileAirborn_FireRate',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/AccuracyAndHandling/GPart_EG_WhileSliding_AccuracyHandling',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/Damage/GPart_EG_WhileSliding_Damage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/FireRate/GPart_EG_WhileSliding_FireRate',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_All_CritStatusEffects/GPart_Passive_All_CritStatusEffect',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_All_RadDamage/GPart_All_unhealthyraddamage',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_HighHealth_Breaker/GPart_All_HighHealthBreaker',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_ShieldBreakAmp/GPart_All_ShieldBreakAmp',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_SlideRegenShields/GPart_All_SlideRegenShields',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_CyberSpike/GPart_EG_Gen_SkillEnd_CyberSpike',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_DamageMitigation/GPart_All_DamageMitigation',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_GrenadeDamage/GPart_All_GrenadeDamage',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_PulseNova/GPart_EG_Gen_SkillActive_PulseFireNova',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_ShockFeedback/GPart_All_ShockFeedback',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_UniqueEnemyDamage/GPart_All_UniqueEnemyDamage',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_WeaponDamage/GPart_All_WeaponDamage',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillEnd_HealingPool/GPart_All_HealingPool',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillStart_ShieldRecharge/GPart_All_SkillStart_OverchargeShield'
]

for anoint in anoints:
    mod.comment('Removing from Pool')
    mod.reg_hotfix(Mod.PATCH, '',
    anoint,
    'MinGameStage',
    '(BaseValueConstant=100.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)'
    )
    mod.newline()

mod.close()
    