#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('early_bloomer.txt',
        'Early Bloomer!',
        [],
        'Bloomer',
        )

def unlock_table(mod,
        label=None,
        rows=[],
        obj_name='/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule.DataTable_GameStage_Schedule',
        column='MinGameStage_17_2500317646FAD2F4916D158835B29E83',
        value=1,
        ):
    if label:
        mod.comment(label)
    for row in rows:
        mod.table_hotfix(Mod.PATCH, '',
                obj_name,
                row,
                column,
                value)
    mod.newline()

# Weapon types
unlock_table(mod, label='Weapon type unlocks', rows=[
    'Weapon_AssaultRifle',
    'Weapon_Heavy',
    'Weapon_Pistol',
    'Weapon_Shotgun',
    'Weapon_SMG',
    'Weapon_SniperRifle',
    ])

# Manufacturers
unlock_table(mod, label='Manufacturer unlocks', rows=[
    'Manufacturer_Anshin',
    'Manufacturer_Atlas',
    'Manufacturer_COV',
    'Manufacturer_Dahl',
    'Manufacturer_ETech',
    'Manufacturer_Hyperion',
    'Manufacturer_Jakobs',
    'Manufacturer_Maliwan',
    'Manufacturer_Pangolin',
    'Manufacturer_Tediore',
    'Manufacturer_Torgue',
    'Manufacturer_Vladof',
    ])

# Elements
unlock_table(mod, label='Element unlocks', rows=[
    'Element_Corrosive',
    'Element_Cryo',
    'Element_Fire',
    'Element_Radiation',
    'Element_Shock',
    ])

# Inventory slots
mod.comment('Unlock all inventory slots right from the start of the game')
for slot in [
        '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon3.BPInvSlot_Weapon3',
        '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon4.BPInvSlot_Weapon4',
        '/Game/Gear/ClassMods/_Design/_Data/BPInvSlot_ClassMod.BPInvSlot_ClassMod',
        '/Game/Gear/Artifacts/_Design/_Data/BPInvSlot_Artifact.BPInvSlot_Artifact',
        ]:
    mod.reg_hotfix(Mod.PATCH, '',
            slot,
            'InitiallyEnabled',
            'True')
mod.newline()

# Item types
mod.comment("Item type unlocks. Parts_EndGame is theoretically anointed parts, but I don't think anything")
mod.comment('actually uses this value.  Probably they prefer /Game/Gear/Weapons/_Shared/_Design/EndGameParts/Att_EndGame_MinGamestage')
unlock_table(mod, rows=[
    'Artifacts',
    'ClassMods',
    'GrenadeMods',
    'Parts_EndGame',
    'Shields',
    ])
mod.newline()

# Anointment shenanigans.  I can't seem to alter the attribute everything calls, which
# is one of:
#
#     /Game/Gear/Weapons/_Shared/_Design/EndGameParts/Att_EndGame_MinGamestage
#     /Game/PatchDLC/BloodyHarvest/Gear/_Design/_GearExtension/GParts/Att_EndGame_MinGamestage_BloodyHarvest
#
# (depending on if it's a Bloody Harvest anoint or not).  So instead we'll just hardcode
# all the individual parts.  Lame, but it works, unlike my other attempts!
mod.comment('Unlock Anointed parts')
for part in [

        # Base Game parts
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
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkUsed_CritDamage/GPart_Beast_RakkCrit',
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

        # Bloody Harvest parts
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror1/GPart_All_Passive_GenerateTerror_Melee',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror10/GPart_All_SkillEnd_GenerateTerror',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror11/GPart_All_SkillEnd_TerrorHeal',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror12/GPart_All_Passive_TerrorAccuracy',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror2/GPart_All_Passive_TerrorDamageFireRate',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror3/GPart_All_Passive_TerrorAmmoRegen',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror4/GPart_All_Passive_TerrorBonus_CryoDamage',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror5/GPart_All_Passive_TerrorBulletReflect',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror6/GPart_All_Passive_TerrorCritDamage',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror7/GPart_All_Passive_TerrorDamageMitigation',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror8/GPart_All_Passive_TerrorHealthRegen',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror9/GPart_All_Passive_TerrorProjectilesPerShot',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/Character/Beastmaster/AtkCmdTerrorFireDmg/GPart_Beast_AttackCmd_TerrorFireDMG',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/Character/Gunner/ReloadTerrorNova/GPart_Gunner_Reload_TerrorNova',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/Character/OP1/GPart_Operative_DroneActiveTerrorLifesteal',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/Character/Siren/Grasp_TerrorSkulls/GPart_Siren_Grasp_TerrorSkulls',

        # Takedown on Maliwan Blacksite parts
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
        ]:
    end_part = part.rsplit('/', 1)[-1]
    full_part = '{}.{}'.format(part, end_part)
    mod.reg_hotfix(Mod.PATCH, '',
            full_part,
            'MinGameStage',
            """(
                BaseValueConstant=1,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1
            )""")
mod.newline()

# This was a shot in the dark, and doesn't seem to work.  The attribute name I'm trying here
# exists for other Att_* modified by official GBX hotfixes, but doesn't seem to exist in the
# object itself.  One attempt here seemed to crash the game, so eh.
if False:
    mod.comment('An anointed unlock attempt')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Att_EndGame_MinGamestage.Att_EndGame_MinGamestage:ValueResolver_EndGamePartMinGameStageAttributeValueResolver',
            'ValueResolver.Object.Value.Scalar.BaseValueScale',
            1)
    mod.newline()

# Some more anointment statements.  I'm honestly not sure what these are really used for,
# but I'm going to go ahead and set these.
mod.comment('More anointed part tweaks (not sure if these are useful or not)')
unlock_table(mod,
        obj_name='/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DataTable_EndGameParts.DataTable_EndGameParts',
        column='GameStage_5_7193729B453E1712D9DF4F8F73B3880E',
        rows=[
            'All_ActionSkillEnd_AccuracyHandling',
            'All_ActionSkillEnd_CooldownRate',
            'All_ActionSkillEnd_CritDamage',
            'All_ActionSkillEnd_DamageReduction',
            'All_ActionSkillEnd_ElementalChance',
            'All_ActionSkillEnd_FireRateReloadSpeed',
            'All_ActionSkillEnd_HealthRegen',
            'All_ActionSkillEnd_LifeSteal',
            'All_ActionSkillEnd_MeleeDamage',
            'All_ActionSkillEnd_MoveSpeed',
            'All_ActionSkillEnd_NextMagBonusDamage',
            'All_ActionSkillEnd_ProjectileSpeedScale',
            'All_ActionSkillEnd_SplashDamage',
            'All_ActionSkillEnd_UniqueEnemyDamage',
            'All_ActionSkillEnd_WeaponDamage',
            'All_ActionSkillStart_GiveGrenadeAmmo',
            'Beast_ActionSkillEnd_PetDamage',
            'Beast_AttackCmd_LifeSteal',
            'Beast_AttackCmd_MoveSpeed',
            'Beast_Gamma_AccuracyHandling',
            'Beast_Gamma_BonusRadiationDamage',
            'Beast_Passive_PetHealth',
            'Beast_Passive_Shield_GiveShield',
            'Beast_Rakk_Slag',
            'Beast_RakkAttackCharge',
            'Beast_RakkStart_CritDamage',
            'Beast_Shield_StealthNova',
            'Beast_SkillStarted_CritBonusCorrosive',
            'Beast_Stealth_AccuracyHandling',
            'Gunner_AutoBearActive_BonusFireDamage',
            'Gunner_AutoBearActive_RegenerateAmmo',
            'Gunner_IBActive_ChanceToGrenade',
            'Gunner_SkillEnd_FireBonusDamage',
            'Gunner_SkillEnd_KillsLowerCooldown',
            'Gunner_SkillEnd_LifeSteal',
            'Gunner_SkillEnd_NextMag_ReloadRecoil',
            'Gunner_SkillEnd_NextMagFirerateCrit',
            'Gunner_SkillEnd_NoAmmoConsumption',
            'Gunner_SkillEnd_ShieldHealthMax',
            'Gunner_SkillEnd_SplashDamage',
            'Gunner_SkillStart_Nova',
            'Operative_BarrierActive_AccuracyCrit',
            'Operative_BarrierActive_StatusEffectChance',
            'Operative_BarrierDeployed_StartRechargingShields',
            'Operative_CloneActive_Regen',
            'Operative_CloneActive_RegenAmmo',
            'Operative_CloneSwap_ReloadWeapon',
            'Operative_CloneSwap_WeaponDamage',
            'Operative_DroneActive_BonusDamage',
            'Operative_DroneActive_MoveSpeed',
            'Operative_DroneActive_ReloadAndFirerate',
            'Siren_Cast_EleChance',
            'Siren_Cast_WeaponDamage',
            'Siren_Grasp_AccuracyHandling',
            'Siren_Grasp_ChargeSpeed',
            'Siren_Grasp_ConstNova',
            'Siren_SkillEnd_AttunedBonusDamage',
            'Siren_SkillEnd_ReturnDamage',
            'Siren_Slam_DamageReduction',
            'Siren_Slam_MeleeDamage',
            'Siren_Slam_WeaponDamage',
            ])
mod.newline()

mod.close()
