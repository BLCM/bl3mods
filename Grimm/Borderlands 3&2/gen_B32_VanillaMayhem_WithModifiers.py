from bl3hotfixmod import Mod

mod=Mod('B3&2_VanillaMayhem_WithModifiers.bl3hotfix',
'Borderlands 3&2',
'Grimm',
[
    'Categories: major-pack, mode-balance, scaling, mayhem, gear-general, gear-anointments, gear-brand, gear-pack, gear-ar, gear-pistol, gear-heavy, gear-shotgun, gear-smg, gear-sniper, gear-grenade, vendor, qol',
    'Huge overhaul that includes: QOL, TVHM is harder, DLC4 bosses rescale, Takedowns rescale, overall weapon and grenade balance, and all the unique gear rebalanced as well.',
    'QOL stuff : No more anointed enemies, no more engorged rakks in the slaughters, loot enemies spawn more often, you can get all the gear from lvl1, and all the slots are uvailable at lvl1 (uncompatible with early bloomer, it does the same thing) and CoV badasses have less rocket launchers',
    'Changes in this version only : Mayhem is exactly like normal.',
    'All the guns/grenades should now be closer to each other in term of each other, and a 2.5 damage multiplier has been applied to ALL the weapons and nades in the game (including non uniques).',
    'You should now be able to use everything in mayhem.',
    'This mod took a long time to make, please report any issues, stuff that dont work, or works too well. The balance is not definitive, so please report that as well. And ofc enjoy',
    'Thanks to CodyCode, SsPyR, Apocalyptech, 10 FPS, HackerSmasher, FromDarkHell, Apple1417'

],
lic=Mod.CC_BY_SA_40,
)

player_damage_base='/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_GlobalBase'
health_damage='/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers'
dots='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage'
barrel='/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_IO_Balance'
elerarity='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity'
damage_tvhm='/Game/Enemies/_Shared/_Design/Balance/Table_DefaultEnemyBalance'
damagetype='/Game/GameData/Balance/HealthAndDamage/DataTable_HealthTypeBalance'

mod.comment('General Changes')
if True:

    mod.comment('Reducing The Weight of HW For COV Badasses')
    if True:
        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_COVEnemyUse_HeavyWeapons',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_ForAI/Balance_HW_COV_AI_UseONLY.Balance_HW_COV_AI_UseONLY,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_ForAI/Balance_HW_COV_AI_UseONLY.Balance_HW_COV_AI_UseONLY\"',
                Weight=(BaseValueConstant=0.5,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/AI/Balance_AR_VLA_AI.Balance_AR_VLA_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/AI/Balance_AR_VLA_AI.Balance_AR_VLA_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/AI/Balance_PS_JAK_AI.Balance_PS_JAK_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/AI/Balance_PS_JAK_AI.Balance_PS_JAK_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/AI/Balance_SG_HYP_AI.Balance_SG_HYP_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/AI/Balance_SG_HYP_AI.Balance_SG_HYP_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/AI/Balance_SM_DAHL_AI.Balance_SM_DAHL_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/AI/Balance_SM_DAHL_AI.Balance_SM_DAHL_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/AI/Balance_SR_DAL_AI.Balance_SR_DAL_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/AI/Balance_SR_DAL_AI.Balance_SR_DAL_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()

        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/Enemies/Punk_Female/Badass/_Design/Weapon/ItemPools/ItemPool_BadassPunk_HeavyWeapons',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_ForAI/Balance_HW_COV_AI_UseONLY.Balance_HW_COV_AI_UseONLY,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_ForAI/Balance_HW_COV_AI_UseONLY.Balance_HW_COV_AI_UseONLY\"',
                Weight=(BaseValueConstant=0.5,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/AI/Balance_AR_VLA_AI.Balance_AR_VLA_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/AI/Balance_AR_VLA_AI.Balance_AR_VLA_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/AI/Balance_PS_JAK_AI.Balance_PS_JAK_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/AI/Balance_PS_JAK_AI.Balance_PS_JAK_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/AI/Balance_SG_HYP_AI.Balance_SG_HYP_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/AI/Balance_SG_HYP_AI.Balance_SG_HYP_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/AI/Balance_SM_DAHL_AI.Balance_SM_DAHL_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/AI/Balance_SM_DAHL_AI.Balance_SM_DAHL_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/AI/Balance_SR_DAL_AI.Balance_SR_DAL_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/AI/Balance_SR_DAL_AI.Balance_SR_DAL_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()

    mod.comment('Promethea Slaughter Changes')
    if True:

        mod.comment('Removing The Engorged Rakks From The Slaughter')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round4/SpawnOptions_CreatureSlaughter_Round4Wave4b_RatchJabbermonVarkid',
            'Options.Options[11].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave5b',
            'Options.Options[2].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave5c',
            'Options.Options[18].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()
        
        mod.comment('Makes The Slaughter Available From The Start')
        if True:

            dep=Mod.get_full_cond('/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Mission_Ep01_ChildrenOfTheVault_C', 'Mission')

            mod.comment('Code courtesy of Apocalyptech')
            mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
            '/Game/Missions/Side/Slaughters/CreatureSlaughter/Mission_CreatureSlaughter.Default__Mission_CreatureSlaughter_C',
            'MissionDependencies',
            f'({dep})'
            )
            mod.newline()
   
    mod.comment('Increasing Spawn Rate of Loot Enemies')
    if True:

        mod.comment('Increasing Spawn Rate of Jabber Thieves')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix',
            'Options.Options[4].WeightParam.AttributeInitializationData.BaseValueConstant',
            0.08
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix_NoBadass',
            'Options.Options[3].WeightParam.AttributeInitializationData.BaseValueConstant',
            0.08
            )
            mod.newline()

        mod.comment('Increasing Spawn Rate of Shiny Grogs')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Saurian/_Mixes/SpawnOptions_SaurianMix_Wetlands_NoTyrant',
            'Options.Options[3].WeightParam.AttributeInitializationData.BaseValueScale',
            0.6
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Saurian/_Mixes/SpawnOptions_SaurianMix_Wetlands',
            'Options.Options[6].WeightParam.AttributeInitializationData.BaseValueScale',
            0.6
            )
            mod.newline()

        
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_Prologue',
            'Options.Options[5].WeightParam.Range.Value',
            0.1
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_Sacrifice',
            'Options.Options[6].WeightParam.Range.Value',
            0.1
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_CityVault',
            'Options.Options[5].WeightParam.Range.Value',
            0.1
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Mansion/SpawnOptions_CoVMix_Mansion1',
            'Options.Options[9].WeightParam.AttributeInitializationData.BaseValueConstant',
            0.5
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Marshfields/SpawnOptions_CoVMix_MarshFields',
            'Options.Options[7].WeightParam.Range.Value',
            0.6
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Prison/SpawnOptions_CotVFullMix_Prison1',
            'Options.Options[12].WeightParam.Range.Value',
            0.3
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeFestival_FullMix',
            'Options.Options[15].WeightParam.Range.Value',
            0.275
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeInterior_FullMix',
            'Options.Options[17].WeightParam.Range.Value',
            0.4
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/SpawnOptions_CoVMix_Desert',
            'Options.Options[10].WeightParam.Range.Value',
            0.6
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_4/Crypt/SpawnOptions_CoVMix_Crypt',
            'Options.Options[7].WeightParam.Range.Value',
            0.1
            )
            mod.newline()

        mod.comment('Increasing Spawn Rate of Loot Bots')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/ServiceBots/_Mixes/SpawnOptions_ServiceBotMix_City',
            'Options.Options[5].WeightParam.Range.Value',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/ServiceBots/_Mixes/SpawnOptions_ServiceBotMix_RiseAndGrind',
            'Options.Options[3].WeightParam.Range.Value',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/ServiceBots/_Mixes/SpawnOptions_ServiceBotMix_Towers',
            'Options.Options[5].WeightParam.Range.Value',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/ServiceBots/_Mixes/SpawnOptions_ServiceBotMix_Watereship',
            'Options.Options[6].WeightParam.Range.Value',
            0.15
            )
            mod.newline()

        mod.comment('Increasing Spawn Rate of Chubby Skags')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Skags/_Mixes/SpawnOptions_SkagFullMix',
            'Options.Options[6].WeightParam.AttributeInitializationData.BaseValueScale',
            0.15
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Skags/_Mixes/Zone0/SpawnOptions_SkagEarlyMix',
            'Options.Options[2].WeightParam.AttributeInitializationData.BaseValueConstant',
            0.06
            )
            mod.newline()
        
        mod.comment('Increasing Spawn Rate of Engorged Rakks')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Rakk/_Mixes/SpawnOptions_Rakk_MixBadasses',
            'Options.Options[2].WeightParam.AttributeInitializationData.BaseValueScale',
            2.0
            )
            mod.newline()

    mod.comment('Removes The Anointed Enemies')
    if True:

        mod.comment('Removes the Anointed Goliaths')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Goliaths/Variants/SpawnOptions_GoliathAnointed',
            'Options.Options[0].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Mansion/SpawnOptions_CoVMix_MansionBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Marshfields/SpawnOptions_CoVMix_MarshFieldsBadassess',
            'Options.Options[9].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVaultBadasses',
            'Options.Options[10].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_GoliathMix_COVSlaughter',
            'Options.Options[4].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Missions/Plot/MarshFields/SpawnOptions_CoVMix_MarshFieldsBadassess_MudNecks',
            'Options.Options[9].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

        mod.comment('Removes the Anointed Pyschos')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_CityVaultBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_TowersBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Mansion/SpawnOptions_CoVMix_MansionBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Marshfields/SpawnOptions_CoVMix_MarshFieldsBadassess',
            'Options.Options[7].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Prison/SpawnOptions_CotVFullMix_PrisonBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/SpawnOptions_CoVMix_WetlandsBadasses',
            'Options.Options[5].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/WetlandsVault/SpawnOptions_CoVMix_WetlandsVaultBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVaultBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/SpawnOptions_CoVMix_DesertBadasses',
            'Options.Options[3].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Psychos/Variants/SpawnOptions_PsychoAnointedMale',
            'Options.Options[0].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_PsychoMix_COVSlaughter',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Missions/Plot/MarshFields/SpawnOptions_CoVMix_MarshFieldsBadassess_MudNecks',
            'Options.Options[7].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()
        
        mod.comment('Removes the Anointed Punks')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_PrologueBadass',
            'Options.Options[4].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions__CoVMix_OrbitalBadasses',
            'Options.Options[5].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_CityVaultBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_TowersBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Mansion/SpawnOptions_CoVMix_MansionBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Marshfields/SpawnOptions_CoVMix_MarshFieldsBadassess',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Prison/SpawnOptions_CotVFullMix_PrisonBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/SpawnOptions_CoVMix_WetlandsBadasses',
            'Options.Options[4].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/WetlandsVault/SpawnOptions_CoVMix_WetlandsVaultBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVaultBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Mine/SpawnOptions_CoVMix_MineBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/SpawnOptions_CoVMix_DesertBadasses',
            'Options.Options[2].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Punks/Variants/SpawnOptions_PunkAnointed',
            'Options.Options[0].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_PunkMix_COVSlaughter',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Missions/Plot/MarshFields/SpawnOptions_CoVMix_MarshFieldsBadassess_MudNecks',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()
        
        mod.comment('Removes the Anointed Tinks')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_PrologueBadass',
            'Options.Options[5].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions__CoVMix_OrbitalBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_CityVaultBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_TowersBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Mansion/SpawnOptions_CoVMix_MansionBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Marshfields/SpawnOptions_CoVMix_MarshFieldsBadassess',
            'Options.Options[8].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Prison/SpawnOptions_CotVFullMix_PrisonBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Tinks/_Mixes/SpawnOptions_TinkMix',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Tinks/Variants/SpawnOptions_TinkAnointed',
            'Options.Options[0].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/ProvingGrounds/SpawnOptions_TinkBadassMix_ProvingGrounds',
            'Options.Options[2].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_TinkMix_COVSlaughter',
            'Options.Options[5].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Missions/Plot/MarshFields/SpawnOptions_CoVMix_MarshFieldsBadassess_MudNecks',
            'Options.Options[8].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

        mod.comment('Removes the Anointed Enforcers')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions__CoVMix_OrbitalBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_CityVaultBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_TowersBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Prison/SpawnOptions_CotVFullMix_PrisonBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/WetlandsVault/SpawnOptions_CoVMix_WetlandsVaultBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVaultBadasses',
            'Options.Options[11].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Mine/SpawnOptions_CoVMix_MineBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeBadasses',
            'Options.Options[10].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_EnforcerMix_COVSlaughter',
            'Options.Options[4].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

        mod.comment('Removes the Anointed Goons')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVaultBadasses',
            'Options.Options[12].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Mine/SpawnOptions_CoVMix_MineBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Goons/Variants/SpawnOptions_GoonAnointed',
            'Options.Options[0].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_GoonMix_COVSlaughter',
            'Options.Options[3].Factory.Object..AIActorClass',
            ''
            )
            mod.newline()

    mod.comment('Removing The Gear Level Restrictions')
    if True:

        mod.comment('Makes All Manufacturer Available From lv1')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Dahl',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Jakobs',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Hyperion',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Vladof',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Tediore',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_COV',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Torgue',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Maliwan',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Atlas',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Anshin',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Pangolin',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

        mod.comment('Makes All Elements Available From lv1')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Element_Fire',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Element_Cryo',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Element_Corrosive',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Element_Shock',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Element_Radiation',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

        mod.comment('Makes All Gear Available From lv1')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_ETech',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_Pistol',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_Shotgun',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_SMG',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_AssaultRifle',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_SniperRifle',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_Heavy',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Shields',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'ClassMods',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Artifacts',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'GrenadeMods',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Ammo',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

        mod.comment('Unlocks All The Slots at lv1')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon3',
            'InitiallyEnabled',
            'True'
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon4',
            'InitiallyEnabled',
            'True'
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Gear/ClassMods/_Design/_Data/BPInvSlot_ClassMod',
            'InitiallyEnabled',
            'True'
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/Gear/Artifacts/_Design/_Data/BPInvSlot_Artifact',
            'InitiallyEnabled',
            'True'
            )
            mod.newline()

    mod.comment('Aligning World Drops to be like BL2 // SspyR')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
        'Uncommon',
        'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
        10
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
        'Rare',
        'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
        1
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
        'VeryRare',
        'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
        0.1
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
        'Legendary',
        'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
        0.005
        )
        mod.newline()

    mod.comment('Adjusting Vending Machine Pool')
    if True:

        mod.comment('Adjusting Weapon Machine Pool')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons',
            'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons',
            'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons',
            'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
            1.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons',
            'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
            10.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons',
            'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
            5.0
            )
            mod.newline()

        mod.comment('Adjusting Weapon of the Day Machine Pool')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons_OfTheDay',
            'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
            1.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons_OfTheDay',
            'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
            10.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons_OfTheDay',
            'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
            5.0
            )
            mod.newline()

        mod.comment('Adjusting Grenade Machine Pool')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Grenades',
            'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Grenades',
            'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Grenades',
            'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
            1.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Grenades',
            'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
            10.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Grenades',
            'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
            5.0
            )
            mod.newline()

        mod.comment('Adjusting Grenade of the Day Machine Pool')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Ammo_OfTheDay',
            'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
            1.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Ammo_OfTheDay',
            'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
            10.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Ammo_OfTheDay',
            'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
            5.0
            )
            mod.newline()

        mod.comment('Adjusting Shield Machine Pool')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Shields',
            'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Shields',
            'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Shields',
            'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
            1.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Shields',
            'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
            10.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Shields',
            'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
            5.0
            )
            mod.newline()

        mod.comment('Adjusting Class Mods Machine Pool')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_ClassMods',
            'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_ClassMods',
            'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_ClassMods',
            'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
           1.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_ClassMods',
            'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
            10.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_ClassMods',
            'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
            5.0
            )
            mod.newline()

        mod.comment('Adjusting Shield of the Day Machine Pool')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
            1.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
            10.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
            5.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
            1.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
            10.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[5].Weight.BaseValueScale',
            5.0
            )
            mod.newline()

        mod.comment('Adjusting Veterans Machine Pool to Only Have Quest Rewards // SsPyr')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl',
            'BalancedItems',
            """
            (
                (
                    ItemPoolData=ItemPoolData'\"/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards.DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards\"',
                    Weight=(BaseValueConstant=3,DataTableValue=(),BaseValueAttribute=GbxAttributeData'\"/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare.Att_RarityWeight_03_Rare\"'BaseValueScale=0.3),
                    Quantity=(BaseValueConstant=50.0)
                )
            )
            """
            )
            mod.newline()

    mod.comment('Changed The Spawn Rate of Elements on Guns')
    if True:

        mod.comment('Common Elemental Rarity')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Common',
            'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Common',
            'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
            0.0625

            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Common',
            'Shock_8_684654654B332D94359F79BEB2DB90AA',
            0.0625

            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Common',
            'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
            0.0625

            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Common',
            'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
            0.0625

            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Common',
            'Radiation_13_2500317646FAD2F4916D158835B29E83',
            0.0625

            )
            mod.newline()

        mod.comment('UnCommon Elemental Rarity')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'UnCommon',
            'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'UnCommon',
            'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
            0.125
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'UnCommon',
            'Shock_8_684654654B332D94359F79BEB2DB90AA',
            0.125
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'UnCommon',
            'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
            0.125
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'UnCommon',
            'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
            0.125
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'UnCommon',
            'Radiation_13_2500317646FAD2F4916D158835B29E83',
            0.125
            )
            mod.newline()

        mod.comment('Rare Elemental Rarity')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Rare',
            'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Rare',
            'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
            0.250
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Rare',
            'Shock_8_684654654B332D94359F79BEB2DB90AA',
            0.250
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Rare',
            'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
            0.250
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Rare',
            'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
            0.250
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'Rare',
            'Radiation_13_2500317646FAD2F4916D158835B29E83',
            0.250
            )
            mod.newline()

        mod.comment('VeryRare Elemental Rarity')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'VeryRare',
            'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'VeryRare',
            'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
            0.50
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'VeryRare',
            'Shock_8_684654654B332D94359F79BEB2DB90AA',
            0.50
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'VeryRare',
            'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
            0.50
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'VeryRare',
            'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
            0.50
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            elerarity,
            'VeryRare',
            'Radiation_13_2500317646FAD2F4916D158835B29E83',
            0.50
            )
            mod.newline()

mod.comment('Damage And Health, NVHM And TVHM')
if True:

    mod.comment('Miscellanious')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        barrel,
        'Barrel',
        'Damage_13_560366A1463D4183F137F3AB10204686',
        1.05
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        health_damage,
        'Vehicle_HealthScaler',
        'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
        2.5
        )
        mod.newline()

    mod.comment('Increasing The Slam, Melee And Slide Damage')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        player_damage_base,
        'PlayerMeleeDamage',
        'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
        28
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        player_damage_base,
        'PlayerGroundSlamDamage',
        'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
        100
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        player_damage_base,
        'PlayerSlideDamage',
        'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
        18
        )
        mod.newline()

    mod.comment('Flesh, Shield And Armor Damage')
    if True:

        mod.comment('NVHM')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh',
            'NonelementalModifier',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh',
            'CorrosiveModifier',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh',
            'CryoModifier',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh',
            'FireModifier',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh',
            'ShockModifier',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh',
            'RadiationModifier',
            1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield',
            'NonelementalModifier',
            1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield',
            'CorrosiveModifier',
            0.7
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield',
            'CryoModifier',
            0.7
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield',
            'FireModifier',
            0.7
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield',
            'ShockModifier',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield',
            'RadiationModifier',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor',
            'NonelementalModifier',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor',
            'CorrosiveModifier',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor',
            'CryoModifier',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor',
            'FireModifier',
            0.7
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor',
            'ShockModifier',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor',
            'RadiationModifier',
            0.7
            )
            mod.newline()

        mod.comment('TVHM')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh_PT2',
            'NonelementalModifier',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh_PT2',
            'CorrosiveModifier',
            0.65
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh_PT2',
            'CryoModifier',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh_PT2',
            'FireModifier',
            1.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh_PT2',
            'ShockModifier',
            0.65
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Flesh_PT2',
            'RadiationModifier',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield_PT2',
            'NonelementalModifier',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield_PT2',
            'CorrosiveModifier',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield_PT2',
            'CryoModifier',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield_PT2',
            'FireModifier',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield_PT2',
            'ShockModifier',
            2.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Shield_PT2',
            'RadiationModifier',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor_PT2',
            'NonelementalModifier',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor_PT2',
            'CorrosiveModifier',
            1.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor_PT2',
            'CryoModifier',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor_PT2',
            'FireModifier',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor_PT2',
            'ShockModifier',
            0.65
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            damagetype,
            'Armor_PT2',
            'RadiationModifier',
            0.5
            )
            mod.newline()

    mod.comment('Enemies Gain More Health Per Level')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        health_damage,
        'AI_AdditionalHealthPerLevel',
        'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
        0.07
        )
        mod.newline()

    mod.comment('Enemies Deal Less Damage Per Level')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        health_damage,
        'AI_AdditionalDamagePerLevel',
        'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
        0.024
        )
        mod.newline()

    mod.comment('TVHM Health And Damage Changes')
    if True: 

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        health_damage,
        'Playthrough2_GlobalHealthScaler',
        'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
        1.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        damage_tvhm,
        'Default_PT2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
        1.05
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Enemies/_Shared/_Design/Balance/Table_Playthrough_SpawnWeights',
        'Playthrough.PlaythroughOne.BaseValueConstant',
        1.0
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Enemies/_Shared/_Design/Balance/Table_Playthrough_SpawnWeights',
        'Playthrough.PlaythroughTwoAndBeyond.BaseValueConstant',
        1.5
        )
        mod.newline()

    mod.comment('Increasing DOTs Damage')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dots,
        'DamageScale_DOT',
        'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dots,
        'DamageScale_DOT',
        'Shock_8_684654654B332D94359F79BEB2DB90AA',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dots,
        'DamageScale_DOT',
        'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dots,
        'DamageScale_DOT',
        'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dots,
        'DamageScale_DOT',
        'Radiation_13_2500317646FAD2F4916D158835B29E83',
        1.2
        )
        mod.newline()

behemoth='/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth'
frontrunner='/Game/PatchDLC/Raid1/Enemies/Frontrunner/_Shared/_Design/Balance/Table_Balance_FrontrunnerRaid1'
heavy='/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1'
mech='/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1'
oversphere='/Game/PatchDLC/Raid1/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_OversphereRaid1'
ratch='/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1'
trooper='/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1'
guardiantk2='/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2'
bossestk2='/Game/PatchDLC/Takedown2/Enemies/GuardianBrute/_Shared/_Design/Balance/Table_Balance_GuardianBrute'
bugstk2='/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2'

mod.comment('Scaling the TakeDowns to be 50% Harder Than The Base Game')
if True:

    mod.comment('TakeDown2')
    if True:

        mod.comment('Bugs Health Takedown2')
        if True:

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_GroundTD2',
            bugstk2,
            'Nekrobug_GroundTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_FlyerTD2',
            bugstk2,
            'Nekrobug_FlyerTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0

            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_HopperTD2',
            bugstk2,
            'Nekrobug_HopperTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
            bugstk2,
            'Nekrobug_BadassTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
            bugstk2,
            'Nekrobug_BadassTD2',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
            bugstk2,
            'Nekrobug_BadassTD2',
            'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
            bugstk2,
            'Nekrobug_BadassTD2',
            'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
            bugstk2,
            'Nekrobug_BadassTD2',
            'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BroodlingTD2',
            bugstk2,
            'Nekrobug_BroodlingTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.3
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BomberTD2',
            bugstk2,
            'Nekrobug_BomberTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.35
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_Flyer_FodderTD2',
            bugstk2,
            'Nekrobug_Flyer_FodderTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_GroundTD2_BossAdd',
            bugstk2,
            'Nekrobug_GroundBossFodderTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_HopperTD2_BossAdd',
            bugstk2,
            'Nekrobug_HopperBossFodderTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BroodlingTD2_BossAdd',
            bugstk2,
            'Nekrobug_BroodlingBossFodderTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2_BossAdd',
            bugstk2,
            'Nekrobug_BadassBossFodderTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2_BossAdd',
            bugstk2,
            'Nekrobug_BadassBossFodderTD2',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2_BossAdd',
            bugstk2,
            'Nekrobug_BadassBossFodderTD2',
            'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2_BossAdd',
            bugstk2,
            'Nekrobug_BadassBossFodderTD2',
            'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2_BossAdd',
            bugstk2,
            'Nekrobug_BadassBossFodderTD2',
            'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113',1.5*
            3.0
            )
            mod.newline()

        mod.comment('Guardians Health Takedown2')
        if True:

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2',
            guardiantk2,
            'Guardian_WraithTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2',
            guardiantk2,
            'Guardian_WraithTD2',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSpectreTD2',
            guardiantk2,
            'Guardian_SpectreTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.7
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSpectreTD2',
            guardiantk2,
            'Guardian_SpectreTD2',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.35
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraTD2',
            guardiantk2,
            'Guardian_SeraTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraTD2',
            guardiantk2,
            'Guardian_SeraTD2',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianHeraldTD2',
            guardiantk2,
            'Guardian_HeraldTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianHeraldTD2',
            guardiantk2,
            'Guardian_HeraldTD2',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBadassTD2',
            guardiantk2,
            'Guardian_WraithBadassTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBadassTD2',
            guardiantk2,
            'Guardian_WraithBadassTD2',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBossFodderTD2',
            guardiantk2,
            'Guardian_WraithBossFodderTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.2
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBossFodderTD2',
            guardiantk2,
            'Guardian_WraithBossFodderTD2',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSpectreBossFodderTD2',
            guardiantk2,
            'Guardian_SpectreBossFodderTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.2
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSpectreBossFodderTD2',
            guardiantk2,
            'Guardian_SpectreBossFodderTD2',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraBossFodderTD2',
            guardiantk2,
            'Guardian_SeraBossFodderTD2',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraBossFodderTD2',
            guardiantk2,
            'Guardian_SeraBossFodderTD2',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianReaperTD2',
            guardiantk2,
            'Guardian_Reaper',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.8
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianReaperTD2',
            guardiantk2,
            'Guardian_Reaper',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianReaperTD2',
            guardiantk2,
            'Guardian_Reaper',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianReaperTD2',
            guardiantk2,
            'Guardian_Reaper',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2_LOWXP',
            guardiantk2,
            'Guardian_WraithTD2_LOWXP',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2_LOWXP',
            guardiantk2,
            'Guardian_WraithTD2_LOWXP',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2_LOWXP',
            guardiantk2,
            'BPChar_GuardianSpectreTD2_LOWXP',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.7
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2_LOWXP',
            guardiantk2,
            'BPChar_GuardianSpectreTD2_LOWXP',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.35
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraTD2_LOWXP',
            guardiantk2,
            'Guardian_SeraTD2_LOWXP',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraTD2_LOWXP',
            guardiantk2,
            'Guardian_SeraTD2_LOWXP',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianHeraldTD2_LOWXP',
            guardiantk2,
            'Guardian_HeraldTD2_LOWXP',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianHeraldTD2_LOWXP',
            guardiantk2,
            'Guardian_HeraldTD2_LOWXP',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBadassTD2_LOWXP',
            guardiantk2,
            'Guardian_WraithBadassTD2_LOWXP',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBadassTD2_LOWXP',
            guardiantk2,
            'Guardian_WraithBadassTD2_LOWXP',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteBomber',
            bossestk2,
            'GuardianBrute_Bomber',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteBomber_BossFodder',
            bossestk2,
            'GuardianBrute_BomberFodder',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.7
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteMiniboss',
            bossestk2,
            'GuardianBrute_Miniboss',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            35.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteMiniboss',
            bossestk2,
            'GuardianBrute_Miniboss',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            35.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteMiniboss',
            bossestk2,
            'GuardianBrute_Miniboss',
            'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
            35.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteBoss',
            bossestk2,
            'GuardianBrute_Boss',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            55.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteBoss',
            bossestk2,
            'GuardianBrute_Boss',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            65.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteBoss',
            bossestk2,
            'GuardianBrute_Boss',
            'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
            75.0
            )
            mod.newline()

    mod.comment('Takedown1')
    if True:

        mod.comment('Behemoths')
        if True:

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothMiniWalker',
            behemoth,
            'Behemoth_MiniWalker',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothMiniWalker',
            behemoth,
            'Behemoth_MiniWalker',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothGunner',
            behemoth,
            'Behemoth_Gunner',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            12.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothGunner',
            behemoth,
            'Behemoth_Gunner',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothRocketeer',
            behemoth,
            'Behemoth_Rocketeer',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            15.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothRocketeer',
            behemoth,
            'Behemoth_Rocketeer',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothCarrier',
            behemoth,
            'Behemoth_Carrier',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            12.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothCarrier',
            behemoth,
            'Behemoth_Carrier',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            12.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothRaid',
            behemoth,
            'Behemoth_Raid',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            80.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothRaid',
            behemoth,
            'Behemoth_Raid',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            80.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_BehemothRaid',
            behemoth,
            'Behemoth_Raid',
            'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
            50.0
            )
            mod.newline()
        
        mod.comment('FrontRunners')
        if True:

            mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerBasic_Raid1',
            frontrunner,
            'Frontrunner',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerBasic_Raid1',
            frontrunner,
            'Frontrunner',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.4
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerJammer_Raid1',
            frontrunner,
            'GunWolf',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerJammer_Raid1',
            frontrunner,
            'GunWolf',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerStriker_Raid1',
            frontrunner,
            'Nullhound',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerStriker_Raid1',
            frontrunner,
            'Nullhound',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Frontrunner_Badass_Raid1',
            frontrunner,
            'Fronttunner_Badass',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Frontrunner_Badass_Raid1',
            frontrunner,
            'Fronttunner_Badass',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            4.0
            )
            mod.newline()
        
        mod.comment('Heavies')
        if True:

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_GunnerDarkRaid1',
            heavy,
            'Heavy_Gunner',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_BasicDarkRaid1',
            heavy,
            'Heavy_Pyrotech',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_BasicDarkRaid1',
            heavy,
            'Heavy_Pyrotech',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_PowerhouseDarkRaid1',
            heavy,
            'Heavy_Powerhouse',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_PowerhouseDarkRaid1',
            heavy,
            'Heavy_Powerhouse',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_IcebreakerDarkRaid1',
            heavy,
            'Heavy_Icebreaker',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_IcebreakerDarkRaid1',
            heavy,
            'Heavy_Icebreaker',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_AcidrainDarkRaid1',
            heavy,
            'Heavy_Acidrain',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_AcidrainDarkRaid1',
            heavy,
            'Heavy_Acidrain',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_BadassDarkRaid1',
            heavy,
            'Heavy_Badass',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            10.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_BadassDarkRaid1',
            heavy,
            'Heavy_Badass',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            2.0
            )
            mod.newline()
        
        mod.comment('Mechs')
        if True:
            
            mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossBar',
            mech,
            'Mech_Raid_BossBar',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            45.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossA',
            mech,
            'Mech_RaidBossA',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            15.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossA',
            mech,
            'Mech_RaidBossA',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            10.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossB',
            mech,
            'Mech_RaidBossB',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            15.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossB',
            mech,
            'Mech_RaidBossB',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            10.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossC',
            mech,
            'MechRaidBossC',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            15.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossC',
            mech,
            'MechRaidBossC',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            10.0
            )
            mod.newline()
        
        mod.comment('Ratches')
        if True:

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'Ratch_Larva',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchPupRaid1',
            ratch,
            'Ratch_Pup',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'Ratch_Basic',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'Ratch_Basic',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'Ratch_Basic',
            'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchSpitterRaid1',
            ratch,
            'Ratch_Spitter',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchSpitterRaid1',
            ratch,
            'Ratch_Spitter',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchSpitterRaid1',
            ratch,
            'Ratch_Spitter',
            'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'Ratch_Swarm',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'Ratch_Birther',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'Ratch_Birther',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBadassRaid1',
            ratch,
            'Ratch_Badass',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            6.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBadassRaid1',
            ratch,
            'Ratch_Badass',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBadassRaid1',
            ratch,
            'Ratch_Badass',
            'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'Ratch_Hive',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            8.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'Ratch_Hive',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'Ratch_Hive',
            'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchPupRaid1',
            ratch,
            'RatchEgg_Pup',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.75
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
            ratch,
            'RatchEgg_Basic',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_RatchBadassRaid1',
            ratch,
            'RatchEgg_Badass',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            5.0
            )
            mod.newline()
        
        mod.comment('Troopers')
        if True:

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
            trooper,
            'Trooper_Basic',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.85
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
            trooper,
            'Trooper_Basic',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperMedicDarkRaid1',
            trooper,
            'Trooper_Medic',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperMedicDarkRaid1',
            trooper,
            'Trooper_Medic',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperFlashDarkRaid1',
            trooper,
            'Trooper_Flash',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperFlashDarkRaid1',
            trooper,
            'Trooper_Flash',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
            trooper,
            'Trooper_Melee',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
            trooper,
            'Trooper_Melee',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperJetpackDarkRaid1',
            trooper,
            'Trooper_Jetpack',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperJetpackDarkRaid1',
            trooper,
            'Trooper_Jetpack',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
            trooper,
            'Trooper_Shotgun',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            2.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
            trooper,
            'Trooper_Shotgun',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBadassDarkRaid1',
            trooper,
            'Trooper_Badass',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBadassDarkRaid1',
            trooper,
            'Trooper_Badass',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperReflectDark',
            trooper,
            'Trooper_Reflect',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperReflectDark',
            trooper,
            'Trooper_Reflect',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperStealthDark',
            trooper,
            'Trooper_Stealth',
            'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.CHAR,'BPChar_TrooperStealthDark',
            trooper,
            'Trooper_Stealth',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
            0.5
            )
            mod.newline()

train='/Alisma/Enemies/TrainBoss/_Shared/_Design/Balance/Table_Balance_TrainBoss_PT1'
benedict='/Alisma/Enemies/DrBenedict/_Shared/_Design/Balance/Table_Balance_DrBenedict_PT1'
sponge='/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss'
brick='/Alisma/Enemies/DarkVH/DarkBrick/_Design/Balance/Table_Balance_DarkBrick_PT1'
mordecai='/Alisma/Enemies/DarkVH/DarkMordecai/_Design/Balance/Table_Balance_DarkMordecai'
lilith='/Alisma/Enemies/DarkVH/DarkLilith/_Design/Balance/Table_Balance_DarkLilith_PT1'
final='/Alisma/Enemies/Psychodin/_Shared/_Design/Balance/Table_Balance_Psychodin'

mod.comment('Rescaling The DLC4 Bosses')
if True:

    mod.table_hotfix(Mod.CHAR,'BPChar_TrainBoss',
    train,
    'Basic',
    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
    85.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'MatchBPChar_DrBenedictAll',
    benedict,
    'Basic',
    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
    30.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_DrBenedict',
    benedict,
    'Basic',
    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
    18.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_SpongeBoss',
    sponge,
    'SpongeBoss',
    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
    45.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_SpongeBoss',
    sponge,
    'SpongeBoss',
    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
    45.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_SpongeBoss',
    sponge,
    'SpongeBoss',
    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
    45.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_SpongeBoss',
    sponge,
    'SpongeBoss',
    'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',
    45.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_SpongeBoss',
    sponge,
    'SpongeBoss',
    'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113',
    45.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_DarkBrick',
    brick,
    'Basic',
    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
    38.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_DarkLilith',
    lilith,
    'Basic',
    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
    45.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_DarkMordecai',
    mordecai,
    'Basic',
    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
    38.0    
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_Psychodin',
    final,
    'Basic',
    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
    60.0   
    )
    mod.newline()

    mod.table_hotfix(Mod.CHAR,'BPChar_Psychodin',
    final,
    'Basic',
    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
    60.0   
    )
    mod.newline()

enemyhp=[
"HealthSimpleScalar_42_0499AACF43FDF39B7084E2BB63E4BF68",
"ArmorSimpleScalar_44_BCAAA445479831C25B0D55AF294A15D6",
"ShieldSimpleScalar_43_417C36C54DA2550A4CABC7B26A5E24A8"
]
exp="ExpGainScalar_39_2159F009466933AA733AE688E55B1B93"
cash="CashScalar_22_B7B11DC94BBB45C94A96279146EC193E"
drop1="DropWeightCommonScalar_21_59A2FB124E32B955768A7B9D93C25A99"
drop2="DropWeightUncommonScalar_25_809615334E7F0DB3B8712DAC221015C3"
drop3="DropWeightRareScalar_27_A09CF5314C51796896A83EA0806C7520"
drop4="DropWeightVeryRareScalar_29_F2CA570046CD50A7C514EDB0AE1BE591"
drop5="DropWeightLegendaryScalar_31_D9DA03C54065EA981BE218B11942C24E"
dropnum="DropNumberChanceSimpleScalar_40_115637764B3918F01E6FAFADDC005388"
eridium="DropEridiumChanceSimpleScalar_41_E89AD7E9473FDF3CBED395BA6641FA68"
loot="LootQuality_56_03E220E0495C6B37CD6C7195F5EA289B"
asd="DamageScalarActionSkill_60_39AF483140740A38FC71BA897155CBFF"
melee="DamageScalarMelee_67_9948929F4FF34364CED2EAB51A881946"
slide="DamageScalarSlide_68_B48D0E3A4DF57196839BB58D5AE3E638"
slam="DamageScalarSlam_69_15DB6EDC4CCA52620BF25398CFFD9B26"
petdmg="DamageScalarPet_72_0DD7977D44C4A71D0A6B56B7884E023C"
env="DamageScalarEnviornmental_111_E2A582AA47FC000789FC68BBD31D2CFC"
passiveskill="DamageScalarPassive_115_6A30229E4CC04F751ED01CB64A71880F"
vehicledmg="DamageDealtScalarVehicles_103_5739171948322B35CDA36487F78AF0CE"
vehiclehp="DamageTakenScalarVehicles_104_B75AB4EC482624FDEAAF31B0FA369A77"
gear="DamageScalarGear_119_9FC89117424C6619F2CA958FA2842FC2"
pethp="PetHealth_84_E5B903B4452F4310CCD13C931474E12B"
comphp="CompanionHealth_89_294A6BE7439072AE9F934CAA127D8D83"

mod.comment('Mayhem Changes')
if True:

    mod.comment('Increasing All Damage')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        player_damage_base,
        'PlayerWeaponDamage',
        'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
        20.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        player_damage_base,
        'PlayerGrenadeModDamage',
        'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
        137.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        player_damage_base,
        'VehicleWeaponDamage',
        'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
        30.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        player_damage_base,
        'VehicleRammingDamage',
        'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
        72.0
        )
        mod.newline()


weapontype='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Base_Data'
weaponbrand='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_DamageScale'
brandstats='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Manufacturer_Base_Data'
ar='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_AR_Barrel_Init'
hw='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_HW_Barrel_Init'
ps='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_PS_Barrel_Init'
sg='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_SG_Barrel_Init'
sm='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_SM_Barrel_Init'
sr='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_SR_Barrel_Init'

mod.comment('Overall Weapon Balance')
if True:

    mod.comment('Torgue Stickies Buff')
    if True:

        sg_mag1='/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_01'
        sg_mag2='/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_02'
        sg_mag3='/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_03'
        sg_mag4='/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_04'

        ar_mag1='/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Magazine/Part_AR_TOR_Magazine_01'
        ar_mag2='/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Magazine/Part_AR_TOR_Magazine_02'
        ar_mag3='/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Magazine/Part_AR_TOR_Magazine_03'

        ps_mag1='/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_01'
        ps_mag2='/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_02'
        ps_mag3='/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_03'

        hw_mag1='/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Parts/Magazine/Part_HW_TOR_Mag_01'
        hw_mag2='/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Parts/Magazine/Part_HW_TOR_Mag_02'
        hw_mag3='/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Parts/Magazine/Part_HW_TOR_Mag_03'


        mod.comment('Shotgun Stickies')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sg_mag1,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.05,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sg_mag2,
            'InventoryAttributeEffects.InventoryAttributeEffects[2].ModifierValue',
            """
            (
                BaseValueConstant=0.25,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sg_mag3,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.035,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sg_mag4,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.08,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

        mod.comment('Assault Rifle Stickies')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ar_mag1,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.08,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ar_mag2,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.11,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ar_mag3,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.06,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

        mod.comment('Pistol Stickies')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ps_mag1,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.12,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ps_mag2,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.18,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ps_mag3,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.24,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

        mod.comment('Heavy Stickies ')
        if True:

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            hw_mag1,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.6,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            hw_mag2,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.4,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            hw_mag3,
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=1.0,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
            hw_mag3,
            'InventoryAttributeEffects.InventoryAttributeEffects[2].ModifierValue',
            """
            (
                BaseValueConstant=1.0,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

    mod.comment('Atlas AR')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ar,
        'ATL_Barrel_01',
        'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ar,
        'ATL_Barrel_03',
        'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
        1.3
        )
        mod.newline()

    mod.comment('Alien Barrels balance')
    if True:

        mod.comment('Alien AR')
        if True:
            
            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ar,
            'COV_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ar,
            'DAL_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.65
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ar,
            'TOR_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ar,
            'VLA_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.6
            )
            mod.newline()

        mod.comment('Alien HW')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            hw,
            'COV_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            hw,
            'TOR_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            hw,
            'VLA_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            3.2
            )
            mod.newline()

        mod.comment('Alien Pistols')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ps,
            'COV_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ps,
            'DAL_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ps,
            'MAL_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ps,
            'TOR_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ps,
            'TED_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            ps,
            'VLA_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.45
            )
            mod.newline()

        mod.comment('Alien SG')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sg,
            'HYP_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            8.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sg,
            'MAL_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            9.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sg,
            'TOR_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sg,
            'TED_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            8.0
            )
            mod.newline()

        mod.comment('Alien SMG')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sm,
            'DAL_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.95
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sm,
            'HYP_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sm,
            'MAL_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.85
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sm,
            'TED_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.95
            )
            mod.newline()

        mod.comment('Alien SR')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sr,
            'DAL_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sr,
            'HYP_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sr,
            'MAL_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            sr,
            'VLA_Barrel_ETech',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.85
            )
            mod.newline()

    mod.comment('Weapon Type Balance')
    if True:

        mod.comment('Assault Rifle')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'Spread_23_03553D4547FA30186E792BA391B2FFDE',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            8.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
            0.85
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            1.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
            1.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
            0.90
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            0.45
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
            0.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'AssaultRifle',
            'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
            1.15
            )
            mod.newline()

        mod.comment('SMG')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.85
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'Spread_23_03553D4547FA30186E792BA391B2FFDE',
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            6.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
            0.65
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            0.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
            0.60
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            0.30
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
            0.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SMG',
            'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
            1.2
            )
            mod.newline()

        mod.comment('Pistol')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'Spread_23_03553D4547FA30186E792BA391B2FFDE',
            1.65
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
            0.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            0.55
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
            0.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
            0.40
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            0.20
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
            0.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Pistol',
            'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
            0.95
            )
            mod.newline()

        mod.comment('Shotgun')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'Spread_23_03553D4547FA30186E792BA391B2FFDE',
            5.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            0.90
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
            0.90
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            0.45
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
            0.08
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Shotgun',
            'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
            1.6
            )
            mod.newline()

        mod.comment('Sniper Rifle')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            2.5 
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'Spread_23_03553D4547FA30186E792BA391B2FFDE',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            8.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            0.85
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            0.65
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            0.6
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
            0.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'SniperRifle',
            'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
            1.2
            )
            mod.newline()

        mod.comment('Heavy')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            3.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'Spread_23_03553D4547FA30186E792BA391B2FFDE',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'MaxAccuracy_13_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'MinAccuracy_22_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'AccuracyImpulse_12_A2A97C764F97EC46B630BB9F944FE44E',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            0.65
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'ReloadTimeScale_62_E2E0A3154B4CD841A6ABE3A5A7DCFDB7',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'EquipTime_47_391D5B8C4D0759E7FA619A8947BE0458',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'PutDownTime_48_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            0.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'ElementalChance_68_946EB9244DC0A165542AD9A147B43613',
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weapontype,
            'Heavy',
            'ElementalDamageMultiplier_75_6839E3E84372485107A3168E13CB6B3E',
            0.7
            )
            mod.newline()

    mod.comment('Weapon Type Brand Damage')
    if True:

        mod.comment('Shotgun')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Shotgun',
            'Jakobs_60_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            0.95
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Shotgun',
            'Hyperion_61_03553D4547FA30186E792BA391B2FFDE',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Shotgun',
            'Tediore_64_177AD05C46493B9713642FA9EEDB6DDC',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Shotgun',
            'Torgue_75_E4646A97474FA2023598DE982B960083',
            1.4
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Shotgun',
            'Maliwan_76_93DF9FBB4DB223F6D5697180435918B2',
            1.0
            )
            mod.newline()

        mod.comment('Pistol')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Pistol',
            'DAHL_59_150C89A04BB4FCF0061CAC86E39E1A39',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Pistol',
            'Jakobs_60_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.6
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Pistol',
            'Vladof_63_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Pistol',
            'Tediore_64_177AD05C46493B9713642FA9EEDB6DDC',
            1.3
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Pistol',
            'CoV_65_A2A97C764F97EC46B630BB9F944FE44E',
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Pistol',
            'Torgue_75_E4646A97474FA2023598DE982B960083',
            2.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Pistol',
            'Maliwan_76_93DF9FBB4DB223F6D5697180435918B2',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Pistol',
            'Atlas_78_8B8B7B8741EFF37DAC0B5D8739B6F0E4',
            1.35
            )
            mod.newline()

        mod.comment('SMG')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'SMG',
            'DAHL_59_150C89A04BB4FCF0061CAC86E39E1A39',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'SMG',
            'Hyperion_61_03553D4547FA30186E792BA391B2FFDE',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'SMG',
            'Tediore_64_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'SMG',
            'Maliwan_76_93DF9FBB4DB223F6D5697180435918B2',
            1.1
            )
            mod.newline()

        mod.comment('Assault Rifle')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'AssaultRifle',
            'DAHL_59_150C89A04BB4FCF0061CAC86E39E1A39',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'AssaultRifle',
            'Jakobs_60_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'AssaultRifle',
            'Vladof_63_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            0.7
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'AssaultRifle',
            'CoV_65_A2A97C764F97EC46B630BB9F944FE44E',
            0.95
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'AssaultRifle',
            'Torgue_75_E4646A97474FA2023598DE982B960083',
            1.4
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'AssaultRifle',
            'Atlas_78_8B8B7B8741EFF37DAC0B5D8739B6F0E4',
            1.15
            )
            mod.newline()

        mod.comment('Sniper Rifle')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Sniper',
            'DAHL_59_150C89A04BB4FCF0061CAC86E39E1A39',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Sniper',
            'Jakobs_60_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.6
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Sniper',
            'Hyperion_61_03553D4547FA30186E792BA391B2FFDE',
            1.4
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Sniper',
            'Maliwan_76_93DF9FBB4DB223F6D5697180435918B2',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Sniper',
            'Vladof_63_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            1.0
            )
            mod.newline()

        mod.comment('Heavy')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Heavy',
            'CoV_65_A2A97C764F97EC46B630BB9F944FE44E',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Heavy',
            'Vladof_63_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Heavy',
            'Torgue_75_E4646A97474FA2023598DE982B960083',
            1.85
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            weaponbrand,
            'Heavy',
            'Atlas_78_8B8B7B8741EFF37DAC0B5D8739B6F0E4',
            1.2 
            )
            mod.newline()

    mod.comment('Brand Balance')
    if True:
                    
        mod.comment('Dahl')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
            0.85
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
            0.80
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            0.90
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
            0.80
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            0.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
            0.9
            )
            mod.newline()
            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Dahl',
            'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
            1.0
            )
            mod.newline()

        mod.comment('Jakobs ')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
            0.70
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            0.95
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
            0.80
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            0.75
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
            1.3
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
            0.7
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Jakobs',
            'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
            1.05
            )
            mod.newline()

        mod.comment('Hyperion')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            1.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
            0.70
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
            0.95
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Hyperion',
            'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
            1.05
            )
            mod.newline()

        mod.comment('Vladof')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.05
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            0.80
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Vladof',
            'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
            1.0
            )
            mod.newline()

        mod.comment('Tediore')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
            1.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Tediore',
            'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
            1.1
            )
            mod.newline()

        mod.comment('CoV')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.3
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
            0.85
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            0.6
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            1.10
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
            1.05
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
            1.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'CoV',
            'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
            1.0
            )
            mod.newline()

        mod.comment('Torgue')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
            0.7
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
            1.1
            )
            mod.newline()
            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Torgue',
            'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
            1.0
            )
            mod.newline()

        mod.comment('Maliwan')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            0.55
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
            0.85
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Maliwan',
            'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
            2.5
            )
            mod.newline()

        mod.comment('Atlas')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
            1.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'CritDamageScale_63_CD26C16D40CD2DDF676270956F04A694',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'FirerateScale_29_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'SpreadScale_64_03553D4547FA30186E792BA391B2FFDE',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'MaxAccuracyScale_65_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'MinAccuracyScale_66_177AD05C46493B9713642FA9EEDB6DDC',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'AccuracyImpulseScale_67_A2A97C764F97EC46B630BB9F944FE44E',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'OnIdleRegenerationScale_37_E15777FD4DDECFBFBB456B95714655CD',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'RecoilHeightScale_34_5BC534A04CD28A2CC42C52A4990EB588',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'RecoilWidthScale_35_BDD410724B43608670E3D1BB331D6488',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'ZoomTimeScale_51_AFCCE491453F50E193F0B6935706EEF2',
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'ReloadTimeScale_58_B4D939D14402A732AD06239E09FE64E1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'EquipTimeScale_68_391D5B8C4D0759E7FA619A8947BE0458',
            0.95
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'PutDownTimeScale_69_AA52E4FF4CF2E2BF8CEAC2B9E54CB3DA',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'WeaponHitForceScale_70_25A700B84BD1212FECA774B48D24FF76',
            0.9
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'ElementalChanceScale_73_C4EC9BCE44E98744632F78844B99DA83',
            0.6
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            brandstats,
            'Atlas',
            'ElementalDamageMultiplierScale_80_D457807F45510F5C3D23D69C7D7C7964',
            0.9
            )
            mod.newline()

grenadetype='/Game/Gear/GrenadeMods/_Design/Balance/Grenade_Balance_Table'
grenademods='/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Balance_Table'

mod.comment('Overall Grenade Balance')
if True:

    mod.comment('Grenade Augment Balance')
    if True:

        mod.comment('MIRV')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'MIRV',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'MIRV',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'MIRV',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'MIRV',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            8.0
            )
            mod.newline()

        mod.comment('Lingering')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Lingering',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.4
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Lingering',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Lingering',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            6.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Lingering',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            12.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Lingering',
            'Secondary_1_17_518A093F48377625749592BEC8275DC6',
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Lingering',
            'Secondary_2_18_AB999387440701CC75633C917E78FD7B',
            6.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Lingering',
            'Secondary_3_19_ACA59F5242FD94CFBAB2418760866307',
            12.0
            )
            mod.newline()

        mod.comment('Sticky')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Sticky',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Sticky',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Sticky',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Sticky',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            2.0
            )
            mod.newline()

        mod.comment('Bouncy')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Bouncy',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Bouncy',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Bouncy',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            6.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Bouncy',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            12.0
            )
            mod.newline()

        mod.comment('Singularity')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Singularity',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.3
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Singularity',
            'Radius_13_9DDB780D4981106D3843E19FAC0856D3',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Singularity',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Singularity',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Singularity',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            4.0
            )
            mod.newline()

        mod.comment('Transfusion')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Transfusion',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Transfusion',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            0.3
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Transfusion',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            0.6
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Transfusion',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            1.2
            )
            mod.newline()

        mod.comment('Large')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Large',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Large',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            0.4
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Large',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Large',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            1.6
            )
            mod.newline()

        mod.comment('Spring')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Spring',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.4
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Spring',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Spring',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Spring',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Spring',
            'Secondary_1_17_518A093F48377625749592BEC8275DC6',
            1.1
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Spring',
            'Secondary_2_18_AB999387440701CC75633C917E78FD7B',
            1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Spring',
            'Secondary_3_19_ACA59F5242FD94CFBAB2418760866307',
            1.4
            )
            mod.newline()

        mod.comment('MIRV_MIRV')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'MIRV_MIRV',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.3
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'MIRV_MIRV',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'MIRV_MIRV',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            6.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'MIRV_MIRV',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            12.0
            )
            mod.newline()

        mod.comment('Money')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Money',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Money',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            3.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Money',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            6.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Money',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            12.0
            )
            mod.newline()

        mod.comment('Generator')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Generator',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Generator',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            0.3
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Generator',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            0.6
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Generator',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            1.2
            )
            mod.newline()

        mod.comment('Nuke')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Nuke',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.6
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Nuke',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Nuke',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Nuke',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            3.0
            )
            mod.newline()

        mod.comment('Artillery')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Artillery',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.4
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Artillery',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            0.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Artillery',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            0.3
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Artillery',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            0.6
            )
            mod.newline()

        mod.comment('Link')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Link',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.3
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Link',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            0.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Link',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Link',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            0.5
            )
            mod.newline()

        mod.comment('Divider')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Divider',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.4
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Divider',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Divider',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Divider',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            4.0
            )
            mod.newline()
        
        mod.comment('Roider')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Roider',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Roider',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            0.3
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Roider',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            0.6
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Roider',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            1.2
            )
            mod.newline()

        mod.comment('Elemental')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'ElementalDamage',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.15
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'ElementalDamage',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            0.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'ElementalDamage',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            0.4
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'ElementalDamage',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'ElementalDamage',
            'Secondary_1_17_518A093F48377625749592BEC8275DC6',
            0.2
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'ElementalDamage',
            'Secondary_2_18_AB999387440701CC75633C917E78FD7B',
            0.4
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'ElementalDamage',
            'Secondary_3_19_ACA59F5242FD94CFBAB2418760866307',
            0.8
            )
            mod.newline()

        mod.comment('Rain')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Rain',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Rain',
            'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
            2.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Rain',
            'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
            4.0
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenademods,
            'Rain',
            'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
            8.0
            )
            mod.newline()

    mod.comment('Grenade Type Balance')
    if True:

        mod.comment('Exploder')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenadetype,
            'Manufacturer_Heavy',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.8
            )
            mod.newline()

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenadetype,
            'Manufacturer_Heavy',
            'Radius_13_9DDB780D4981106D3843E19FAC0856D3',
            0.2
            )
            mod.newline()

        mod.comment('Homing')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenadetype,
            'Manufacturer_Homing',
            'Damage_12_F33DA0994756D761207677A51A156787',
            -0.3
            )
            mod.newline()

        mod.comment('Longbow')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenadetype,
            'Manufacturer_Longbow',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.2
            )
            mod.newline()

        mod.comment('Airboosted')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenadetype,
            'Manufacturer_AirBoosted',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.5
            )
            mod.newline()

        mod.comment('Rubberized')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenadetype,
            'Manufacturer_Rubberized',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.3
            )
            mod.newline()

        mod.comment('Impact')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            grenadetype,
            'Manufacturer_Impact',
            'Damage_12_F33DA0994756D761207677A51A156787',
            0.5
            )
            mod.newline()

grenademodsunique='/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Unique_Balance_Table'
jackpot='/Game/PatchDLC/Dandelion/Gear/Grenade/GrenadeMod_Dandelion_Table'
bounty='/Game/PatchDLC/Geranium/Gear/Grenade/GrenadeMod_Geranium_Table'
tk2='/Game/PatchDLC/Takedown2/Gear/GrenadeMods/GrenadeMod_Unique_BalanceTable_Takedown2'
cartel='/Game/PatchDLC/Event2/Gear/GrenadeMods/GrenadeMod_Event2_Table'

mod.comment('Unique Grenade Balance')
if True:

    mod.comment('Cartel')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'FishSlap',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.8
        )
        mod.newline()

    mod.comment('DLC1')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'AcidBurn',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'Slider',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.55
        )
        mod.newline()

    mod.comment('DLC3')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'CoreBurst',
        'Damage_12_F33DA0994756D761207677A51A156787',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SkagOil',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -0.1
        )
        mod.newline()
    
    mod.comment('Takedown2')
    if True:

        mod.comment('DAF_Lightspeed damage')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tk2,
        'DAF_Lightspeed',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.25
        )
        mod.newline()

    mod.comment('Base Game')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_BouncingBosom',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_Firestorm',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -0.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_Fastball',
        'Damage_12_F33DA0994756D761207677A51A156787',
        8.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_EMP',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_HipHop',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_WidowMaker',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_Surge',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -0.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_Nagate',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_Quasar',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -0.4
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_StormFront',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -0.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_HunterSeeker',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_Kryll',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'MSN_Shroom',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_RedQueen',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_Epicenter',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_WizardOfNOG',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_ECHO2',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_Chupa',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'LGD_TranFusion',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.4
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'Piss',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -0.45
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'ObviousTrap',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -0.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'BirthdaySuprise',
        'Damage_12_F33DA0994756D761207677A51A156787',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'Cupcake',
        'Damage_12_F33DA0994756D761207677A51A156787',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'Toiletbombs',
        'Damage_12_F33DA0994756D761207677A51A156787',
        0.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        grenademodsunique,
        'Seeker',
        'Damage_12_F33DA0994756D761207677A51A156787',
        -0.4
        )
        mod.newline()

atlas='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_ATL'
cov='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_COV'
dahl='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_DAL'
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
harvest='/Game/PatchDLC/BloodyHarvest/Gear/_Design/Balance/DataTable_Weapon_BloodyHarvest'
mayhem4 = '/Game/PatchDLC/Raid1/Re-Engagement/Balance/DataTable_ReEngagement1_Weapons'
ixora='/Game/PatchDLC/Ixora/Gear/Weapons/DataTable_WeaponBalance_Ixora'

mod.comment('Unique Weapon Balance')
if True:

    mod.comment('Atlas')
    if True:
            
        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Parts/Part_AR_ATL_Barrel_RebelYell',
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

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        atlas,
        'AR_Carrier',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        atlas,
        'PS_Drill',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        atlas,
        'PS_Peacemonger',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        atlas,
        'HW_Freeman',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        atlas,
        'HW_RubysWrath',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.1
        )
        mod.newline()

    mod.comment('CoV')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'AR_SAWBAR',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'AR_SAWBAR',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        250
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'AR_KreigDamage',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.1
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'AR_KreigFirerate',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'AR_CHAOS',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'PS_Mouthpiece',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.45
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'PS_Linoge',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'PS_SKEKSIS',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'PS_SKEKSIS',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'PS_Contagion',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'PS_Contagion',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        2.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'PS_Contagion',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'PS_Chad',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'PS_PsychoStabber',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'HW_PortaPooper',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'HW_HotDrop',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cov,
        'HW_Terror',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.0
        )
        mod.newline()

    mod.comment('Dahl')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_BOTD',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_BOTD',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_Warlord',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_Warlord',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        0.4
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_Barrage',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_Barrage',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_StarHelix',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_Earworm',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_Hail',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.90
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_Hail',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        2.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'AR_Kaos',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.25
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/SleepingGiant/Parts/Part_SM_DAL_Barrel_SleepingGiant',
        'InventoryAttributeEffects.InventoryAttributeEffects[0]',
        """
        (
            AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage"',
            ModifierType=ScaleSimple,
            ModifierValue=(BaseValueConstant=0.65,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
        )
        """
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Demoskag/Parts/Part_SM_DAL_Barrel_Demoskag',
        'InventoryAttributeEffects.InventoryAttributeEffects[0]',
        """
        (
            AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage"',
            ModifierType=ScaleSimple,
            ModifierValue=(BaseValueConstant=0.7,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
        )
        """
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'SM_Ripper',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'SM_Ripper',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        4.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'SM_Vanquisher',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'SM_Vanquisher',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'SM_Hellfire',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'SM_Hellfire',
        'Custom_B_11_6D4E8C1140CC269ED614BC958ECB0E22',
        5.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'SM_9Volt',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'PS_Hornet',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'PS_Irradiater',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'PS_Nemesis',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.1
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'PS_AAA',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'PS_Rakkman',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.45
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'PS_Omniloader',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'SR_BrashisDedication',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'SR_WorldDestroyer',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        dahl,
        'SR_MalaksBane',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/MalaksBane/Parts/Part_SR_DAL_Barrel_ETech_MalaksBane',
        'WeaponUseModeAttributeEffects.WeaponUseModeAttributeEffects[0].AttributeEffects.AttributeEffects[2]',
        """
        (
            AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage"',
            ModifierType=ScaleSimple,
            ModifierValue=(BaseValueConstant=2.5,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
        )
        """
        )
        mod.newline()

    mod.comment('Hyperion')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SG_Butcher',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SG_Redistributor',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SG_Redistributor',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SG_ConferenceCall',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SG_Brick',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.45
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SG_Phebert',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        8.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SM_Crossroad',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SM_Crossroad',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SM_Handsome',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SM_Handsome',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SM_PredatoryLending',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SM_Fork',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SM_XZ',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SM_Bitch',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SM_Bitch',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        1.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SR_Quad',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SR_TheTwoTime',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SR_Masterwork',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        4.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'SR_Masterwork',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        2.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        hyperion,
        'L0V3M4CH1N3',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

    mod.comment('Jakobs')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'AR_LeadSprinkler',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'AR_LeadSprinkler',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        5.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'AR_GatlingGun',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'AR_HandOfGlory',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'AR_TraitorsDeath',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'AR_TraitorsDeath',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        0.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'AR_TraitorsDeath',
        'Custom_B_11_6D4E8C1140CC269ED614BC958ECB0E22',
        2.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'AR_Bekah',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'AR_Rowan',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_Unforgiven',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_Unforgiven',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        3.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_WagonWheel',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_Companion',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_Companion',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_Maggie',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.32
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_Doc',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_TheDuc',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_TheDuc',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_Malevolent',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_Malevolent',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        2.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_AmazingGrace',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_Buttplug',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.08
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_Buttplug',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        4.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'PS_GodQueen',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SG_Wave',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SG_HellWalker',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SG_HellWalker',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SG_Sledge',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SG_Sledge',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SG_Fingerbiter',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SG_NimbleJack',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SG_Garcia',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.1
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SG_OnePumpChump',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        12.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SR_Monocle',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.32
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SR_Monocle',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        5.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SR_Headsplosion',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Parts/Part_SR_JAK_Bolt_Headsplosion',
        'InventoryAttributeEffects.InventoryAttributeEffects[4]',
        """
        (
            AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_CriticalHitDamageBonus.Att_CriticalHitDamageBonus"',
            ModifierType=ScaleSimple,
            ModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
        )
        """
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SR_IceQueen',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SR_Hunter',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SR_Hunted',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jakobs,
        'SR_Huntress',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

    mod.comment('Maliwan')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SR_Storm',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SR_ASMD',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SR_ASMD',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        4.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SR_ASMD',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SR_Krakatoa',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SR_Krakatoa',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Part_MAL_SR_Barrel_Soleki',
        'WeaponUseModeAttributeEffects.AttributeEffects[0]',
        """
        (
            AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage"',
            ModifierType=ScaleSimple,
            ModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_MAL.DataTable_WeaponBalance_Unique_MAL,RowName=SR_Ikelos,ValueName=DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
        )
        """
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SR_Ikelos',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Lucian',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Lucian',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Cutsman',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        3.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Cutsman',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Tsunami',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.45
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Tsunami',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_DestructoSpin',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_DestructoSpin',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Kevins',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_VibraPulse',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_CloudKill',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Devoted',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Devoted',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_westergun',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.05
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Egon',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Parts/Part_SM_MAL_Barrel_Emporer',
        'WeaponUseModeAttributeEffects.AttributeEffects[0]',
        """
        (
            AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage"',
            ModifierType=ScaleSimple,
            ModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_MAL.DataTable_WeaponBalance_Unique_MAL,RowName=SM_Emporer,ValueName=DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
        )
        """
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Emporer',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SM_Crit',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SG_Recursion',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        9.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SG_Recursion',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        4000.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SG_Recursion',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SG_Wisp',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        6.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SG_Wisp',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SG_Mindkiller',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SG_Shriek',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        12.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SG_Trev',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'PS_ThunderballFists',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'PS_ThunderballFists',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'PS_Hellshock',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'PS_Hellshock',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'PS_HyperHydrator',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'PS_Starkiller',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'PS_Sellout',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.LEVEL,'MatchAll',
        maliwan,
        'PS_Plumber',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

    mod.comment('Tediore')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'SG_Sludge',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.4
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SG_Sludge',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'SG_Horizon',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'SG_Polybius',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'SG_Polybius',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/FriendZone/Parts/Part_SG_TED_Barrel_FriendZone.Part_SG_TED_Barrel_FriendZone',
        'InventoryAttributeEffects.InventoryAttributeEffects[0]',
        """
        (
            AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage"',
            ModifierType=ScaleSimple,
            ModifierValue=(BaseValueConstant=1.2,DataTableValue=(DataTable=/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_TED.DataTable_WeaponBalance_Unique_TED,RowName=SG_FriendZone,ValueName=DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
        )
        """
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'SG_FriendZone',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'SM_TenGallon',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'SM_Beans',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'SM_SpiderMind',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'SM_NotAFlamethrower',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'PS_BabyMaker',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'PS_Gunerang',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'PS_Bangerang',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tediore,
        'PS_Sabre',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

    mod.comment('Torgue')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'PS_Devestator',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'PS_Foursome',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'PS_Troy',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'PS_Echo',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'PS_NURF',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'PS_Heckle',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'PS_Hyde',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'PS_RoisensThorns',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'SG_Redline',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'SG_Flakker',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        3.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'SG_Thumper',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.5
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Parts/Part_SG_Torgue_Barrel_Brewha',
        'InventoryAttributeEffects.InventoryAttributeEffects[0]',
        """
        (
            AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage"',
            ModifierType=ScaleSimple,
            ModifierValue=(BaseValueConstant=5.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
        )
        """
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'SG_Brewha',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        5.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'SG_Balrog',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.4
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'SG_TheLob',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'AR_LaserSploder',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'AR_LaserSploder',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        0.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'AR_TryBolt',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'AR_Bearcat',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'AR_AmberManagement',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'AR_AmberManagement',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        0.45
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'AR_Alchemist',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'HW_Swarm',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'HW_Tunguska',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.55
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'HW_Rampager',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'HW_Hive',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        torgue,
        'HW_RYNO',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Parts/Part_HW_TOR_Barrel_BurgerCannon',
        'WeaponUseModeAttributeEffects',
        """
        (
            AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage"',
            ModifierType=ScaleSimple,
            ModifierValue=(BaseValueConstant=3.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
        )
        """
        )
        mod.newline()

    mod.comment('Vladof')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'HW_Mongol',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'HW_Cloudburst',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'AR_Sickle',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'AR_Shreddifier',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'AR_Dictator',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'AR_Ogre',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.4
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'AR_Faisor',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'AR_LuciansCall',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.1
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        maliwan,
        'AR_LuciansCall',
        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'AR_Damned',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'PS_Magnificent',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'PS_BoneShredder',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'PS_Infiniti',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'PS_TheLeech',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'SR_Lyuda',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.45
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'SR_Lyuda',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        2.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        vladof,
        'SR_Prison',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.2
        )
        mod.newline()

    mod.comment('DLC 1')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'SM_JustCaustic',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'AR_Trash',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.15
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'HW_IonCannon',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        4.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'SM_IonLaser',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'SM_IonLaser',
        'Custom_B_11_6D4E8C1140CC269ED614BC958ECB0E22',
        0.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'HW_Nukem',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        3.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'SG_HeartBreaker',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'PS_RoboMasher',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.4
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'AR_Varlope',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.1
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'SM_EmbersPurge',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'SM_Boomer',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'PS_Scoville',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'SR_AutoAime',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'AR_Digby',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'HW_Creamer',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'PS_Craps',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'SM_CheapTip',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.6
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'SG_SlowHand',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.4
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        jackpot,
        'PS_Lucky7',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

    mod.comment('DLC 2')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SR_Skullmasher',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.30
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'AR_Mutant',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'AR_Mutant_2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_Omen',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'AR_Homicidal',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'AR_Homicidal_A',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SR_CockyBastard',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.6
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SR_CockyBastard',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_Insider',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        -0.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SM_Oldridian',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_Anarchy',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.6
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_Anarchy',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_Anarchy_2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_TheCure',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.4
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'PS_LoveDrill',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'PS_LoveDrill_Leg',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.6
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_Firecracker',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        5.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_SacrificialLamb',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'PS_Kaleidoscope',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'PS_Kaleidoscope',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'PS_FrozenDevil',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'PS_FrozenDevil_2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SM_SFForce',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'PS_Frostbite',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_shocker',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'PS_LittleYeeti',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'AR_Clairvoyance',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SP_UnseenThreat',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.05
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SP_UnseenThreat',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        5.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_TheNothing',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        5.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'SG_TheNothing_2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'AR_SparkyBoom',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        '"AR_SparkyBoom_2": ',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'AR_SparkyBoom_3',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'AR_Soulrender',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        tentacles,
        'PS_TheSeventh',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

    mod.comment('DLC 3')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_QuickDraw',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_QuickDraw',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        1.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'AR_CoolBeans',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SG_Dakota',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SG_Dakota',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        2.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_Rose',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SR_ImaginaryNumber',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_Lasocannon',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_Miscreant',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SG_SpeakEasy',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.15
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_Gargoyle',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_Gargoyle',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        2.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_Gargoyle_2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SG_Shoveler',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SG_Fakobs',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        5.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_BubbleBlaster',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SM_Earthbound',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SG_Brightside',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'AR_McSmugger',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SG_Splinter',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_Peashooter',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'AR_Contained',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'AR_Contained_2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_PrivateInvestigator',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SM_Flipper',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'HW_Plumage',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.62
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_UnkemptHarold',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'PS_Decoupler',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SG_Frequency',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'AR_BioBetsy',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'HW_Satistfaction',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SR_Narp',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'AR_Dowsing',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.55
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SM_Copybeast',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'SG_Antler',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        bounty,
        'AR_StoneThrow',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

    mod.comment('DLC 4')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'AR_Sawhorse',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'HW_BanditLauncher',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'SM_Pat_Mk3',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'AR_LovableRogue',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'SG_BlindBandit',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.95
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'SR_Septimator',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'SR_Septimator_2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'PS_Voice',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.55
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'SM_AshenBeast',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'SM_AshenBeast_2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mind,
        'SG_Convergence',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

    mod.comment('Mayhem 2')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem2,
        'SG_Reflux',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.6
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem2,
        'SM_DNA',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem2,
        'AR_TheMonarch',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.62
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem2,
        'HW_Plague',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.55
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem2,
        'HW_Backburner',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem2,
        'Kaoson',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem2,
        'PS_Multitap',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem2,
        'SR_SandHawk',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

    mod.comment('Cartel')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'IcePick',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.15
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'IceBurger',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'IceBurger_part2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'Pricker',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'YellowCake',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'PewPew',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'OPQS',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'PS_GreaseTrap_Mode1',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'PS_GreaseTrap_Mode2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'SM_NeedleGun',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.25
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'SM_NeedleGun_2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        cartel,
        'SM_NeedleGun_3',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

    mod.comment('Valentines Day')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        valentines,
        'PolyAim',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        valentines,
        'WeddingInvitation',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        valentines,
        'WeddingInvitation',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        2.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        valentines,
        'WeddingInvitation2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

    mod.comment('Takedown 1')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        raid1,
        'KybsWorth',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        raid1,
        'P2PNetworker',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        raid1,
        'SG_TiggsBoom',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        raid1,
        'PS_HandCannon',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        raid1,
        'PS_HandCannon_PT2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        raid1,
        'SM_Fork2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

    mod.comment('Takedown 2')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        guardian,
        'SM_Smog',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        -0.35
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        guardian,
        'AR_WebSlinger',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        guardian,
        'AR_Webslinger_Underbarrel',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.3
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        guardian,
        'HW_Globetrotter',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.65
        )
        mod.newline()

    mod.comment('Bloody Harvest')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        harvest,
        'SG_Fearmonger',
        'DamageScale_2_6249E51D41B75899C0DEDD8B5EFE89ED',
        0.65
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        harvest,
        'SR_FrostBolt',
        'DamageScale_2_6249E51D41B75899C0DEDD8B5EFE89ED',
        1.5
        )
        mod.newline()

    mod.comment('Mayhem 4')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem4,
        'Tankman',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem4,
        'Zheitsev',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.1
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem4,
        'Zheitsev_part2',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem4,
        'Juju',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.35
        )
        mod.newline()

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Parts/Part_SM_DAL_Barrel_CraderMP5',
        'AspectList.AspectList[0].Object..WeaponUseComponent.Object..FireRate.BaseValue',
        5.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem4,
        'Deathgrip',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        2.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem4,
        'Execute',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        mayhem4,
        'Juliet',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

    mod.comment('DLC 5')
    if True:

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'Boogeyman',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.7
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'CriticalThug',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.85
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'Firefly',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'PlasmaCoil',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        3.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'HotfootTeddy',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.8
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'Trickshot',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.2
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'DarkArmy',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'IceAge',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.75
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'IceAge',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        3.5
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'Tizzy',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        0.9
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        ixora,
        'SpiritOfMaya',
        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
        1.0
        )
        mod.newline()
