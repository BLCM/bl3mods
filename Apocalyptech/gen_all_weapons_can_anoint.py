#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('all_weapons_can_anoint.txt',
        'All Weapons Can Anoint',
        [
            "Adds anointment parts to all the weapons which can't ordinarily",
            "have them.  (This doesn't *guarantee* anointments -- use my",
            "Better Loot for that.)",
        ],
        'AllAnoint',
        )

# Weight attributes
(NONE,
        GENERIC,
        SIREN,
        OPERATIVE,
        BEASTMASTER,
        GUNNER) = range(6)

anoint_parts = {
        NONE: '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/Att_EndGame_NoneChanceGuns.Att_EndGame_NoneChanceGuns',
        GENERIC: '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/Att_EndGame_GenericPartChance.Att_EndGame_GenericPartChance',
        SIREN: '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/Att_EndGame_Siren_PartChance.Att_EndGame_Siren_PartChance',
        OPERATIVE: '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/Att_EndGame_Operative_PartChance.Att_EndGame_Operative_PartChance',
        BEASTMASTER: '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/Att_EndGame_BEastmaster_PartChance.Att_EndGame_Beastmaster_PartChance',
        GUNNER: '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/Att_EndGame_Gunner_PartChance.Att_EndGame_Gunner_PartChance',
        }

# Anointment list.  We actually only need to put the base game Anointments in here -- the others
# will be added automatically by the GPartExpansion objects.  Those don't apply to these
# weapons ordinarily because they don't have a GenericParts array to alter.  Since we're adding
# that in with this mod, they'll pick up the new ones automatically (including, say, Bloody Harvest
# anoints when that event's active, etc).
anointments = [
        ('None', NONE),

        # Base game generics
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_AccuracyHandling/GPart_All_SkillEnd_AccuracyHandling', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_SplashDamage/GPart_All_SkillEnd_SplashDamage', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_CritDamage/GPart_All_SkillEnd_CritDamage', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_FireRateReload/GPart_All_SkillEnd_FireRateReload', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_LifeSteal/GPart_All_SkillEnd_LifeSteal', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_MeleeDamage/GPart_All_SkillEnd_MeleeDamage', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_UniqueEnemyDamage/GPart_All_SkillEnd_UniqueEnemyDamage', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_WeaponDamage/GPart_All_SkillEnd_WeaponDamage', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Fire/GPart_All_SkillEnd_NextMagBonusDamageFire', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Shock/GPart_All_SkillEnd_NextMagBonusDamageShock', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Radiation/GPart_All_SkillEnd_NextMagBonusDamageRadiation', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Cryo/GPart_All_SkillEnd_NextMagBonusDamageCryo', GENERIC),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Corrosive/GPart_All_SkillEnd_NextMagBonusDamageCorrosive', GENERIC),
        
        # Base game Siren
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Cast_WeaponDamage/GPart_Siren_Cast_WeaponDamage', SIREN),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_AccuracyCrit/GPart_Siren_Grasp_AccuracyCrit', SIREN),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/SkillEnd_AttunedEleDamage/GPart_Siren_SkillEnd_AttunedSkillDamage', SIREN),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_MeleeDamage/GPart_Siren_Slam_MeleeDamage', SIREN),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_WeaponDamage/GPart_Siren_Slam_WeaponDamage', SIREN),

        # Base game Operative
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/BarrierActiveAccuracyCrit/GPart_Operative_BarrierActive_AccuracyCrit', OPERATIVE),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneActiveRegenAmmo/GPart_Operative_CloneActive_AmmoRegen', OPERATIVE),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneSwapDamage/GPart_CloneSwap_WeaponDamage', OPERATIVE),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneSwapInstaReload/GPart_Operative_CloneSwapInstaReload', OPERATIVE),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveBonusDamage/GPart_Operative_DroneActiveBonusDamage', OPERATIVE),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveFireRateReload/GPart_Operative_DroneActive_FireRateReload', OPERATIVE),

        # Base game Beastmaster
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/AttackCommandLifeSteal/GPart_Beast_AttackCmd_Lifesteal', BEASTMASTER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/Beast_Gamma_BonusRadiationDamage/GPart_BonusRadiationDamage', BEASTMASTER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkAttackCharge/GPart_Beast_RakkCharge', BEASTMASTER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkSlag/GPart_Beast_RakkSlag', BEASTMASTER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkUsed_CritDamage/GPart_Beast_RakkCrit', BEASTMASTER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/StealthAccuracyHandling/GPart_Beast_Stealth_AccuracyHandling', BEASTMASTER),

        # Base game Gunner
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagFireDamage/GPart_Gunner_NextMagFireDamage', GUNNER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagFirerateCrit/GPart_Gunner_NextMagFirerateCrit', GUNNER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagReloadHandling/GPart_Gunner_NextMagReloadHandling', GUNNER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/AutoBear_AmmoRegen/GPart_Gunner_AutoBear_AmmoRegen', GUNNER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/AutoBear_FireDamage/GPart_Gunner_AutoBear_FireDamage', GUNNER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NoAmmoConsumption/GPart_Gunner_NoAmmoConsumption', GUNNER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_KillsLowerCooldown/GPart_Gunner_KillsLowerCooldown', GUNNER),
        ('/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_SplashDamageIncrease/GPart_Gunner_SplashDamageIncrease', GUNNER),

        ]

# Construct the anointment PartList
parts = []
for (part_obj, part_type) in anointments:
    if part_type == NONE:
        part_bit = Mod.get_full_cond(part_obj)
    else:
        part_bit = """InventoryGenericPartData'"{}"'""".format(Mod.get_full_cond(part_obj))
    parts.append("""(
        PartData={},
        Weight=(
            BaseValueConstant=1,
            BaseValueAttribute=GbxAttributeData'"{}"',
            BaseValueScale=1
        )
    )""".format(
        part_bit,
        anoint_parts[part_type],
        ))
part_data = '({})'.format(','.join(parts))

# List of weapons which don't have anoints
weapons = [
        ("Amazing Grace",
           '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace',
           '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/InvPartSet_PS_JAK_AmazingGrace'),
        ("Amber Management",
           '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/AmberManagement/Balance/Balance_AR_TOR_AmberManagement',
           '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/AmberManagement/Balance/InvPartSet_AR_TOR_AmberManagement'),
        ("Baby Maker ++ (from Clapslist Reward)",
           '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Salvage/Balance_PS_Tediore_BabyMaker_Salvage',
           '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Salvage/InvPartSet_PS_TED_BabyMaker_Salvage'),
        ("Big Succ",
           '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Balance_AR_VLA_BigSucc',
           '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/InvPart_VLA_AR_BigSucc'),
        ("Black Flame",
           '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Balance/Balance_SG_TOR_Brewha',
           '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Balance/InvPartSet_SG_TOR_Brewha'),
        ("Brashi's Dedication",
           '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Balance/Balance_SR_DAL_BrashisDedication',
           '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Balance/PartSet_SR_DAL_BrashisDedication'),
        ("Buttplug",
           '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/Balance_PS_JAK_Buttplug',
           '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/InvPartSet_PS_JAK_Buttplug'),
        ("Extreme Hangin' Chadd",
           '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/Balance_PS_COV_Chad',
           '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/PartSet_PS_COV_Chad'),

        ("Cold Shoulder",
           '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/Balance_VLA_SR_Prison',
           '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/PartSet_VLA_SR_Prison'),
        ("Emperor's Condiment",
           '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer',
           '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/InvPartSet_SM_MAL_Emporer'),
        ("Fingerbiter",
           '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/Balance_SG_JAK_Fingerbiter',
           '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/PartSet_SG_JAK_Fingerbiter'),
        ("Gettleburger",
           '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Balance/Balance_HW_TOR_BurgerCannon',
           '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Balance/PartSet_HW_TOR_BurgerCannon'),
        ("Girth Blaster Elite",
           '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf',
           '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/PartSet_PS_TOR_Nurf'),
        ("Hand of Glory",
           '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/Balance_AR_JAK_HandOfGlory',
           '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/InvPartSet_JAK_AR_HandOfGlory'),
        ("Hot Drop",
           '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Balance/Balance_HW_COV_HotDrop',
           '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Balance/PartSet_HW_COV_HotDrop'),
        ("Hyper-Hydrator",
           '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator',
           '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/InvPartSet_PS_MAL_HyperHydrator'),
        ("Ice Queen",
           '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen',
           '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/PartSet_SR_JAK_IceQueen'),
        ("Just Kaus",
           '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic',
           '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/InvPartSet_SM_HYP_JustCaustic'),
        ("Kenulox",
           '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Balance/Balance_SR_DAL_WorldDestroyer',
           '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Balance/PartSet_SR_DAL_WorldDestroyer'),
        ("Kevin's Chilly",
           '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins',
           '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/InvPartSet_SM_MAL_Kevins'),
        ("Killing Word",
           '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/Balance_PS_COV_Mouthpiece',
           '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/PartSet_PS_COV_Mouthpiece'),
        ("Leech",
           '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech',
           '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/InvPart_VLA_PS_TheLeech'),
        ("Linc",
           '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Balance/Balance_PS_ATL_Drill',
           '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Balance/PartSet_PS_ATL_Drill'),
        ("Null Pointer",
           '/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/ZeroForPlayer/Balance_SR_HYP_ZeroForPlayer',
           '/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/ZeroForPlayer/PartSet_SR_HYP_ZeroForPlayer'),
        ("Pa's Rifle",
           '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/Balance_AR_JAK_PasRifle',
           '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/InvPartSet_JAK_AR_PasRifle'),
        ("Peacemonger",
           '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/Balance_PS_ATL_Warmonger',
           '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/PartSet_PS_ATL_Warmonger'),
        ("Porta-Pooper 5000",
           '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/Balance_HW_COV_PortaPooper',
           '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/PartSet_HW_COV_PortaPooper'),
        ("R.Y.N.A.H.",
           '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/Balance_HW_TOR_RYNO',
           '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/PartSet_HW_TOR_RYNO'),
        ("Robo-Melter",
           '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher',
           '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/InvPartSet_PS_JAK_RoboMasher'),
        ("Rogue-Sight",
           '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Balance_PS_JAK_SpyRevolver',
           '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/InvPartSet_PS_JAK_SpyRevolver'),
        ("Sellout",
           '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch',
           '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/InvPartSet_PS_MAL_SuckerPunch'),
        ("Starkiller",
           '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller',
           '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/InvPartSet_PS_MAL_Starkiller'),
        ("Traitor's Death",
           '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/Balance_AR_JAK_TraitorsDeath',
           '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/InvPartSet_JAK_AR_TraitorsDeath'),
        ("TWO TIME",
           '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/Balance_SR_HYP_TwoTime',
           '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/PartSet_SR_HYP_TwoTime'),
        ]

# Now do the actual mod
for (label, balance, partset) in sorted(weapons):
    mod.comment(label)

    # First the Balance
    mod.reg_hotfix(Mod.PATCH, '',
            balance,
            'RuntimeGenericPartList.bEnabled',
            'True')
    mod.reg_hotfix(Mod.PATCH, '',
            balance,
            'RuntimeGenericPartList.PartList',
            part_data)

    # Then the PartSet
    mod.reg_hotfix(Mod.PATCH, '',
            partset,
            'GenericParts.bEnabled',
            'True')
    mod.reg_hotfix(Mod.PATCH, '',
            partset,
            'GenericParts.PartList',
            part_data)

    mod.newline()

mod.close()
