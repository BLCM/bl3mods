from bl3hotfixmod import Mod, Balance, ItemPool, ItemPoolEntry, BVC
from bl3data import BL3Data

#TODO Talk to FPS when its time for Custom Items (only unused items, maybe powercreeped ones)
#TODO Maybe give some specific mob packs specific drops (like Cobra in BL2) (Areas like Konrads Hold?)
#TODO Update other FL4K Hunt Skills to Update the Card with Bonuses
#TODO Some IB Weapons got Nerfed too hard (Capacitive Armature, Shock Hammer?)
#TODO Make FFYL mean something again?
#TODO Buff Lifesteal % on Lifesteal Weapons and Nerf Lifesteal on Skills
#TODO Up priority of Mayhem Exclusive text

#! Gear Balance Idea List
#! overall buff went well, specific balance is key now
#! use MatchAlls for number tuning
"""
Add Shock to Rebel Yell
Buff Weapons that use more than 1 ammo per shot (More Damage or More Mag)
Buff E-Tech ARs (Torgue ARs especially)
Buff EMP
Give some CoV ARs more elements
Give Seein Dead more Kill Skill Duration too
Buff Tidal and TK Wave Damage and Spread
Buff Redis Damage
Buff Tunguska Damage
Buff Woodblocker Damage
Buff Unforgiven Damage
Buff Maliwan E-Tech SMGs?
"""

#! Skill Balance List
"""
Catharsis
Higher Health Regen Bonuses on FL4 skill
Buff Passives on Pets (at least 10% instead of 5%)
Reduce Amara CDs (except TTB and Base Grasp)
"""

mod=Mod('bl3_sspypatch.bl3hotfix',
'BL3 SspyPatch',
'SSpyR',
[
    'My personal take on a large-scale overhaul mod for Borderlands 3.',
    'This mod takes things from some of my other mods and puts them together with a',
    'bunch of other changes, examples being: No More Anoints, Melee Can Crit, Skill Formula Adjustments',
    'and more. This mod so far is very much in the early stages and some portions could likely be made',
    'irrelevant by Gearbox at some point but it will be an active project for right now.',
    'Name Credit: Pirek'
],
lic=Mod.CC_BY_SA_40,
cats='major-pack, mayhem, event, char-overhaul, gear-general, gear-anointments, enemy-drops, loot-system, loot-sources, text, qol, bugfix'
)

###
### LOOT ADJUSTMENTS
###

### WORLD DROP ADJUSTMENTS ###
#! Adding back in world drops, making them like TPS pools

#pools=[
#    '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_All',
#    '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All',
#    '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts',
#    '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods',
#    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All',
#    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Pistols_All',
#    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_SniperAndHeavy_All',
#    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_ARandSMG_All',
#    '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_Shields_All_Hibiscus',
#    '/Game/PatchDLC/Geranium/GameData/Loot/ItemPool_GrenadeMods_All_Geranium'
#]

#for pool in pools:
#    mod.comment('Adjusting to Remove Legendaries from World Drops')
#    mod.reg_hotfix(Mod.PATCH, '',
#    pool,
#    'BalancedItems.BalancedItems[4].Weight',
#    '(BaseValueConstant=0,BaseValueAttribute=None,BaseValueScale=0)'
#    )
#    mod.newline()

#dlcpools=[
#    '/Game/PatchDLC/Dandelion/GameData/Loot/ItemPool_Guns_All_Dandelion',
#    '/Game/PatchDLC/Dandelion/GameData/Loot/ItemPool_Guns_All_Dandelion_Boss',
#    '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_Guns_All_Hibiscus',
#    '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_GrenadeMods_All_Hibiscus', 
#    '/Game/PatchDLC/Geranium/GameData/Loot/ItemPool_Guns_All_Geranium',
#    '/Game/PatchDLC/Geranium/GameData/Loot/ItemPool_Shields_All_Geranium',
#    '/Game/PatchDLC/Alisma/GameData/Loot/ItemPool_Guns_All_Alisma',
#    '/Game/PatchDLC/Alisma/GameData/Loot/ItemPool_Shields_All_Alisma'
#]

#for dlcpool in dlcpools:
#    mod.comment('Adjusting to Remove Legendaries from World Drops')
#    mod.reg_hotfix(Mod.PATCH, '',
#    dlcpool,
#    'BalancedItems.BalancedItems[4].Weight',
#    '(BaseValueConstant=0,BaseValueAttribute=None,BaseValueScale=0)'
#    )
#    mod.newline()
#    mod.comment('Adjusting to Remove Legendaries from World Drops')
#    mod.reg_hotfix(Mod.PATCH, '',
#    dlcpool,
#    'BalancedItems.BalancedItems[5].Weight',
#    '(BaseValueConstant=0,BaseValueAttribute=None,BaseValueScale=0)'
#    )
#    mod.newline()

#legendary=[
#    '/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Legendary',
#    '/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Legendary',
#    '/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary',
#    '/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary',
#    '/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Legendary',
#    '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Legendary',
#    '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary',
#    '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary',
#    '/Game/PatchDLC/Dandelion/GameData/Loot/Legendary/ItemPool_Dandelion_Guns_Legendary',
#    '/Game/PatchDLC/Dandelion/GameData/Loot/Legendary/ItemPool_Dandelion_Shields_Legendary',
#    '/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Guns_Legendary',
#    '/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Shields_Legendary',
#    '/Game/PatchDLC/Geranium/GameData/Loot/Legendary/ItemPool_Geranium_Guns_Legendary',
#    '/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Guns_Legendary',
#    '/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Shields_Legendary'
#]

##!test ingame to see if it works (DLCs 2-4 just Don't Change)
#for wdrop in legendary:
#    mod.comment('Adjusting to Remove Legendaries from World Drops')
#    mod.reg_hotfix(Mod.PATCH, '',
#    wdrop,
#    'BalancedItems',
#    ''
#    )
#    mod.newline()

#mod.comment('Attempting to Fix DLC4 Still Getting World Drops')
#mod.reg_hotfix(Mod.PATCH, '',
#'/Game/PatchDLC/Alisma/GameData/Loot/EnemyPools/ItemPoolList_Boss_Alisma.ItemPoolList_Boss_Alisma',
#'ItemPools.Itempools[7].PoolProbability',
#'(BaseValueConstant=0,BaseValueScale=0)'
#)
#mod.newline()

#mod.comment('Attempting to Fix DLC4 Still Getting World Drops')
#mod.reg_hotfix(Mod.PATCH, '',
#'/Game/PatchDLC/Alisma/GameData/Loot/EnemyPools/ItemPoolList_Boss_Alisma.ItemPoolList_Boss_Alisma',
#'ItemPools.Itempools[8].PoolProbability',
#'(BaseValueConstant=0,BaseValueScale=0)'
#)
#mod.newline()

#mod.comment('Attempting to Fix DLC2 Still Getting World Drops')
#mod.reg_hotfix(Mod.PATCH, '',
#'/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_Hib_MinionLoot.ItemPoolList_Hib_MinionLoot',
#'ItemPools.Itempools[12].PoolProbability',
#'(BaseValueConstant=0,BaseValueScale=0)'
#)
#mod.newline()

mod.comment('Adjusting to Remove Base Game Legendary Class Mods from World Drops')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary',
'BalancedItems',
''
)
mod.newline()

mod.comment('Aligning World Drops to be like TPS')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
'Uncommon',
'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
10
)
mod.newline()

mod.comment('Aligning World Drops to be like TPS')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
'Rare',
'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
1
)
mod.newline()

mod.comment('Aligning World Drops to be like TPS')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
'VeryRare',
'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
0.10
)
mod.newline()

mod.comment('Aligning World Drops to be like TPS')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
'Legendary',
'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
0.010
)
mod.newline()

mod.comment('Adding Firestorm Back to Traunt')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Heavy_Traunt',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CaptTraunt',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/GrenadeMods/_Design/_Unique/FireStorm/Balance/InvBalD_GM_VLA_FireStorm.InvBalD_GM_VLA_FireStorm,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/GrenadeMods/_Design/_Unique/FireStorm/Balance/InvBalD_GM_VLA_FireStorm.InvBalD_GM_VLA_FireStorm\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Giving Wendigo Seeryul Killur')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Wendigo',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_SparkyBoom',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom.Balance_AR_COV_SparkyBoom,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom.Balance_AR_COV_SparkyBoom\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal.Balance_AR_COV_Homicidal,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal.Balance_AR_COV_Homicidal\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Wendigos Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Wendigo',
'/Hibiscus/Enemies/Wendigo/Design/Character/BPChar_Wendigo.BPChar_Wendigo_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[1].PoolProbability',
'(BaseValueConstant=50.00)'
)
mod.newline()

mod.comment('Giving Amach Old God')
mod.reg_hotfix(Mod.CHAR, 'BPChar_ZealotPilfer_Child_Rare',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_UnseenThreat',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat.Balance_SR_JAK_UnseenThreat,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat.Balance_SR_JAK_UnseenThreat\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/OldGod/Balance/InvBalD_Shield_OldGod.InvBalD_Shield_OldGod,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/OldGod/Balance/InvBalD_Shield_OldGod.InvBalD_Shield_OldGod\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Amachs Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_ZealotPilfer_Child_Rare',
'/Hibiscus/Enemies/_Unique/Rare_ZealotPilfer/Character/BPChar_ZealotPilfer_Child_Rare.BPChar_ZealotPilfer_Child_Rare_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
'(BaseValueConstant=50.00)'
)
mod.newline()

mod.comment('Giving Gmork Insider')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Gmork_B_Wolf_Child',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_UnseenThreat',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing.Balance_SG_MAL_TheNothing,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing.Balance_SG_MAL_TheNothing\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider.Balance_SG_MAL_ETech_Insider,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider.Balance_SG_MAL_ETech_Insider\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Gmorks Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Gmork_B_Wolf_Child',
'/Hibiscus/Enemies/_Unique/Hunt_Gmork/Character/BPChar_Gmork_B_Wolf_Child.BPChar_Gmork_B_Wolf_Child_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
'(BaseValueConstant=50.00)'
)
mod.newline()

mod.comment('Giving Empowered Grawn Torch')
mod.reg_hotfix(Mod.CHAR, 'BPChar_LunaticPossessed',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Lunacy',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/Lunacy/Balance/InvBalD_Artifact_Lunacy.InvBalD_Artifact_Lunacy,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/Lunacy/Balance/InvBalD_Artifact_Lunacy.InvBalD_Artifact_Lunacy\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Torch/Balance/InvBalD_Shield_Legendary_Torch.InvBalD_Shield_Legendary_Torch,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Torch/Balance/InvBalD_Shield_Legendary_Torch.InvBalD_Shield_Legendary_Torch\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Empowered Grawns Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_LunaticPossessed',
'/Hibiscus/Enemies/Lunatic/Possessed/_Design/Character/BPChar_LunaticPossessed.BPChar_LunaticPossessed_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
'(BaseValueConstant=30.00)'
)
mod.newline()

mod.comment('Giving Kritchy Oldridian')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Hib_Hunt_Kritchy',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hunt_Mothman',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance.Balance_AR_JAK_Clairvoyance,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance.Balance_AR_JAK_Clairvoyance\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian.Balance_SM_HYP_Oldridian,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian.Balance_SM_HYP_Oldridian\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Kritchys Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Hib_Hunt_Kritchy',
'/Hibiscus/Enemies/_Unique/Hunt_Kritchy/Character/BPChar_Hib_Hunt_Kritchy.BPChar_Hib_Hunt_Kritchy_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
'(BaseValueConstant=50.00)'
)
mod.newline()

mod.comment('Giving Fungal Gorger Flama Diddle')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Lost_Mush_Child',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Mutant',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant.Balance_AR_JAK_Mutant,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant.Balance_AR_JAK_Mutant\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen.Balance_SG_TED_Omen,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen.Balance_SG_TED_Omen\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Fungal Gorgers Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Lost_Mush_Child',
'//Hibiscus/Enemies/_Unique/Rare_MushroomGiant/Character/BPChar_Lost_Mush_Child.BPChar_Lost_Mush_Child_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
'(BaseValueConstant=70.00)'
)
mod.newline()

mod.comment('Giving Graveward Earworm')
mod.reg_hotfix(Mod.CHAR, 'BPChar_EdenBoss',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_GraveandWard_Graveward',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob.Balance_SG_Torgue_ETech_TheLob,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob.Balance_SG_Torgue_ETech_TheLob\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Earworm/Balance/Balance_DAL_AR_Earworm.Balance_DAL_AR_Earworm,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Earworm/Balance/Balance_DAL_AR_Earworm.Balance_DAL_AR_Earworm\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

### ANOINT POOL ADJUSTMENTS ###

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
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillStart_ShieldRecharge/GPart_All_SkillStart_OverchargeShield',
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
    '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror9/GPart_All_Passive_TerrorProjectilesPerShot'
]

#! single nade anoint for utility isnt worth it, repurpose others to be utility if I want to use them
utilanoints=[
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_CooldownRate/GPart_All_SkillEnd_CooldownRate',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_DamageReduction/GPart_All_SkillEnd_DamageReduction',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_FireRateReload/GPart_All_SkillEnd_FireRateReload',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_MoveSpeed/GPart_All_SkillEnd_MoveSpeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_ProjectileSpeed/GPart_All_SkillEnd_ProjectileSpeed',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/FireRate/GPart_EG_WhileSliding_FireRate'
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/AccuracyAndHandling/GPart_EG_WhileSliding_AccuracyHandling',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/AccuracyAndHandling/GPart_EG_WhileAirborn_AccuracyHandling',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/FireRate/GPart_EG_WhileAirborn_FireRate',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_SlideRegenShields/GPart_All_SlideRegenShields',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillEnd_HealingPool/GPart_All_HealingPool',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_DamageMitigation/GPart_All_DamageMitigation'
]

utility=False
for anoint in anoints:
    if utility==True:
        if anoint in utilanoints:
            continue
    mod.comment('Removing Anoint from Pool')
    mod.reg_hotfix(Mod.PATCH, '',
    anoint,
    'MinGameStage',
    '(BaseValueConstant=100.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)'
    )
    mod.newline()

#!if utility==true:
    #!Reduce anoint spawn here

### MISC LOOT ADJUSTMENTS ###

mod.comment('Adding the Trials Pools to Trials Gem Goblin')
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianGemGoblin',
'/Game/Enemies/Guardian/_Unique/GemGoblin/_Design/Character/BPChar_GuardianGemGoblin.BPChar_GuardianGemGoblin_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools',
"""
(
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSkag.ItemPool_TrialBossSkag\"',
        PoolProbability=(BaseValueConstant=0.100000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGuardian.ItemPool_TrialBossGuardian\"',
        PoolProbability=(BaseValueConstant=0.100000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink.ItemPool_TrialBossTink\"',
        PoolProbability=(BaseValueConstant=0.100000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon.ItemPool_TrialBossGoon\"',
        PoolProbability=(BaseValueConstant=0.100000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech.ItemPool_TrialBossMech\"',
        PoolProbability=(BaseValueConstant=0.100000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSaurian.ItemPool_TrialBossSaurian\"',
        PoolProbability=(BaseValueConstant=0.100000)
    )
)
""")
mod.newline()

mod.comment('Adding DLC World Drops to Gun Gun (Made Basically Obsolete by No World Drops Method Now, Oops)')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/Fabricator/ItemPool_FabricatorGuns_AltFire',
'BalancedItems',
"""
(
    (
        ItemPoolData=ItemPoolData'\"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary.ItemPool_Guns_Legendary\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards.DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards\"',
        Weight=(BaseValueConstant=0.25,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Dandelion/GameData/Loot/Legendary/ItemPool_Dandelion_Guns_Legendary.ItemPool_Dandelion_Guns_Legendary\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Guns_Legendary.ItemPool_Hibiscus_Guns_Legendary\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Geranium/GameData/Loot/Legendary/ItemPool_Geranium_Guns_Legendary.ItemPool_Geranium_Guns_Legendary\"',
        Weight=(BaseValueConstant=1,,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Guns_Legendary.ItemPool_Alisma_Guns_Legendary\"',
        Weight=(BaseValueConstant=1,,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Adjusting Veterans Machine Pool to Only Have Quest Rewards')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl',
'BalancedItems',
"""
(
    (
        ItemPoolData=ItemPoolData'\"/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards.DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards\"',
        Weight=(BaseValueConstant=3,DataTableValue=(),BaseValueAttribute=GbxAttributeData'\"/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare.Att_RarityWeight_03_Rare\"'BaseValueScale=0.3),
        Quantity=(BaseValueConstant=9)
    )
)
"""
)
mod.newline()

mod.comment('Adding in Heckle and Hyde')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Goliath_Bounty01',
'/Game/GameData/Loot/ItemPools/Unique/ItemPool_Pestilence_HeckleandHyde.ItemPool_Pestilence_HeckleandHyde',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion.Balance_PS_COV_Contagion,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion.Balance_PS_COV_Contagion\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1) 
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Adjust Heckle and Hyde Pool Drop Rate Accordingly')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds.Table_LegendarySpecificLootOdds',
'HeckleAndHyde',
'LegendaryDropChance_Playthrough2_50_11E6C8E8493E0A73AF9B35891E7CE111',
0.60
)
mod.newline()

mod.comment('Adjusting weights and pool of Wotan (adding Networker too)')
mod.reg_hotfix(Mod.CHAR, 'BPChar_BehemothRaid',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom\"',
        Weight=(BaseValueConstant=0,BaseValueScale=0)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger\"',
        Weight=(BaseValueConstant=0,BaseValueScale=0)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart\"',
        Weight=(BaseValueConstant=0,BaseValueScale=0)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner\"',
        Weight=(BaseValueConstant=0,BaseValueScale=0)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link.Balance_SM_MAL_Link,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link.Balance_SM_MAL_Link\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries.ItemPool_Mayhem4_Legendaries\"',
        Weight=(BaseValueConstant=1,BaseValueScale=0.60)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Raid1/Customizations/ItemPool_Raid1_Customization.ItemPool_Raid1_Customization\"',
        Weight=(BaseValueConstant=1)
    )
)
""")
mod.newline()

mod.comment('Adjusting weights and pool of Valkyries')
mod.reg_hotfix(Mod.CHAR, 'BPChar_MechRaidBossBar',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool.ItemPool_RaidMiniBosses_Pool',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries.ItemPool_Mayhem4_Legendaries\"',
        Weight=(BaseValueConstant=1,BaseValueScale=0.60)
    )
)
""")
mod.newline()

gerleg=[
    '/Game/PatchDLC/Geranium/GameData/Loot/Guns/ItemPool_GER_AssaultRifles_Legendary',
    '/Game/PatchDLC/Geranium/GameData/Loot/Guns/ItemPool_GER_Shotguns_Legendary',
    '/Game/PatchDLC/Geranium/GameData/Loot/Guns/ItemPool_GER_SMGs_Legendary',
    '/Game/PatchDLC/Geranium/GameData/Loot/Guns/ItemPool_GER_Pistols_Legendary'
]
for ger in gerleg:
    mod.comment('Zeroing Out Geranium Legendary Pools')
    mod.reg_hotfix(Mod.PATCH, '',
    ger,
    'BalancedItems',
    ''
    )
    mod.newline()

mod.comment('Taking Facepuncher Out of a Spawn')
mod.reg_hotfix(Mod.CHAR, 'BPChar_EnforcerAnointed',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Muldock',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/Gear/Shields/_Design/_Uniques/Rectifier/Balance/InvBalD_Shield_LGD_Rectifier.InvBalD_Shield_LGD_Rectifier,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Shields/_Design/_Uniques/Rectifier/Balance/InvBalD_Shield_LGD_Rectifier.InvBalD_Shield_LGD_Rectifier\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All.ItemPool_Guns_All\"',
        Weight=(BaseValueConstant=4.5,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Adding Vibra Pulse to Moxxi Tip Pool')
mod.reg_hotfix(Mod.CHAR, '',
'/Game/InteractiveObjects/TipJar/ItemPool_MoxxiTip_GunRewards',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Hail/Balance/Balance_DAL_AR_Hail.Balance_DAL_AR_Hail,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Hail/Balance/Balance_DAL_AR_Hail.Balance_DAL_AR_Hail\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit.Balance_SM_MAL_Crit,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit.Balance_SM_MAL_Crit\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse.Balance_SM_MAL_VibraPulse,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse.Balance_SM_MAL_VibraPulse\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

#! (Structure of code Credit to apocalyptech)
#! seeing how these feel back as legendaries but with anoint beam
#'/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner',
#'/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DNA/Balance/Balance_SM_MAL_DNA',
#'/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Balance/Balance_PS_ATL_DoubleTap',
#'/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson',
#'/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch',
#'/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Plague/Balance/Balance_HW_TOR_Plague',
#'/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Reflux/Balance/Balance_SG_HYP_Reflux',
#'/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/SandHawk/Balance/Balance_SR_DAL_SandHawk',
#'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5',
#'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip',
#'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute',
#'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju',
#'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop',
#'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman',
#'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev',
newuniques=[
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Balance/Balance_PS_COV_PsychoStabber',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/HeartBreaker/Balance/Balance_SG_HYP_HeartBreaker',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/SlowHand/Balance/Balance_SG_HYP_SlowHand',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Creamer/Balance/Balance_HW_TOR_Creamer',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Balance/Balance_SG_JAK_Unique_Wave',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Bearcat/Balance/Balance_AR_TOR_Bearcat',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Hive/Balance/Balance_HW_TOR_Hive',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Rampager/Balance/Balance_HW_TOR_Rampager',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle',
    '/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom',
    '/Game/Gear/Shields/_Design/_Uniques/BigBoomBlaster/Balance/InvBalD_Shield_LGD_BigBoomBlaster',
    '/Game/Gear/Shields/_Design/_Uniques/MessyBreakup/bALANCE/InvBalD_Shield_MessyBreakup',
    '/Game/Gear/Shields/_Design/_Uniques/BlackHole/Balance/InvBalD_Shield_LGD_BlackHole',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Piss/Balance/InvBalD_GM_Piss',
    '/Game/Gear/GrenadeMods/_Design/_Unique/TranFusion/Balance/InvBalD_GM_TranFusion'
]

data=BL3Data()
to_rarity = '/Game/GameData/Loot/RarityData/RarityData_03_Rare.RarityData_03_Rare'
to_rarity_full = Mod.get_full_cond(to_rarity, 'OakInventoryRarityData')

for leg in newuniques:
    bal=data.get_data(leg)[0]
    if bal['RarityData'][1] != to_rarity:
        mod.comment('Making a Unique instead of Legendary')
        mod.reg_hotfix(Mod.PATCH, '',
        leg,
        'RarityData',
        to_rarity_full
        )
        mod.newline()

mayhemguns=[
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Parts/Part_HW_VLA_Barrel_ETech_BackBurner',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DNA/Parts/Part_SM_MAL_Barrel_DNA',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Parts/Part_PS_ATL_Barrel_DoubleTap',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Parts/Part_SM_DAL_Barrel_Kaoson',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Parts/Part_AR_VLA_Barrel_Monarch',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Plague/Parts/Part_HW_TOR_Barrel_ETech_Plague',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Reflux/Parts/Part_SG_Hyp_Barrel_Reflux',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/SandHawk/PArts/Part_SR_DAL_Barrel_SandHawk',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Parts/Part_SM_DAL_Barrel_CraderMP5',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Parts/Part_SG_MAL_Barrel_DeathGrip',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Parts/Part_PS_TED_Barrel_Execute',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Parts/Part_DAL_AR_Barrel_ETech_Juju',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Parts/Part_AR_TOR_Barrel_Juliet',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Parts/Part_SR_HYP_Barrel_Tankman',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Parts/Part_AR_COV_Barrel_Zheitsev'
]

data=BL3Data()

for gun in mayhemguns:
    part=data.get_data(gun)[1]
    try:
        part['UIStats'][0]
    except KeyError:
        part=data.get_data(gun)[0]
    if part['UIStats'][0]!=None:
        uistat=part['UIStats'][0]
        uistat=uistat['UIStat'][1]
        cond=uistat.split('/')
        cond='.'+cond[len(cond)-1]
        uistat=uistat+cond
        mod.comment('Giving Mayhem Exclusives Anoint Beam')
        mod.reg_hotfix(Mod.PATCH, '',
        gun,
        'UIStats',
        """
        (
            (
                UIStat='\"{}\"',
                PriorityIncrease=0
            ),
            (
                UIStat='\"/Game/Gear/Weapons/_Shared/_Design/EndGameParts/UIStat/UIStat_Generic_WeaponFoiler.UIStat_Generic_WeaponFoiler\"',
                PriorityIncrease=0
            )
        )
        """.format(uistat)
        )
        mod.newline()

mod.comment('Adjusting Anointed Text to say Mayhem Exclusive')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/_Shared/_Design/EndGameParts/UIStat/UIStat_Generic_WeaponFoiler',
'FormatText',
'[endgamebold]Mayhem Exclusive.[/endgamebold]'
)
mod.newline()



###
### MAYHEM MODE ADJUSTMENTS
###

### REMOVAL OF TIERED MODIFIERS ###

mod.comment('Setting Easy Modifiers Weights to 0')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_EAsy.ModSet_Mayhem2_EAsy',
'ModifierSets',
"""
(
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/PartyTime/Ability_Mayhem2_PartyTime.Ability_Mayhem2_PartyTime_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/AimForTheSky/Ability_Mayhem2_AimForTheSky.Ability_Mayhem2_AimForTheSky_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/RoidRage/Ability_Mayhem2_RoidRage.Ability_Mayhem2_RoidRage_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/SoulStealer/Ability_Mayhem2_SoulStealer.Ability_Mayhem2_SoulStealer_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Shared/Bighetti/Ability_Mayhem2_Bighetti.Ability_Mayhem2_Bighetti_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/FinishThem/Ability_Mayhem2_FinishThem.Ability_Mayhem2_FinishThem_C,
        Weight=(BaseValueConstant=0)
    )
)
""")
mod.newline()

mod.comment('Setting Medium Modifiers Weights to 0')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Medium.ModSet_Mayhem2_Medium',
'ModifierSets',
"""
(
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/FloorIsLava/Ability_Mayhem2_FLoorIsLava.Ability_Mayhem2_FloorIsLava_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/FrozenPulse/Ability_Mayhem2_FrozenPulse.Ability_Mayhem2_FrozenPulse_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/Rally/Ability_Mayhem2_Rally.Ability_Mayhem2_Rally_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/OlSwitcheroo/Ability_Mayhem2_OlSwitcheroo.Ability_Mayhem2_OlSwitcheroo_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Corrosive.Ability_Mayhem2_ElementalInfusion_Corrosive_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Cryo.Ability_Mayhem2_ElementalInfusion_Cryo_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Fire.Ability_Mayhem2_ElementalInfusion_Fire_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Radiation.Ability_Mayhem2_ElementalInfusion_Radiation_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Shock.Ability_Mayhem2_ElementalInfusion_Shock_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/HealNo/Ability_Mayhem2_HealNo.Ability_Mayhem2_HealNo_C,
        Weight=(BaseValueConstant=0)
    )
)
""")
mod.newline()

mod.comment('Setting Hard Modifiers Weights to 0')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Hard.ModSet_Mayhem2_Hard',
'ModifierSets',
"""
(
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ChainGang/Ability_Mayhem2_ChainGang.Ability_Mayhem2_ChainGang_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ArcaneEnchanter/Ability_Mayhem2_ArcaneEnchanter.Ability_Mayhem2_ArcaneEnchanter_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/DroneBuddy/Ability_Mayhem2_DroneBuddy.Ability_Mayhem2_DroneBuddy_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/EleBreaker/Ability_Mayhem2_Ele_Breaker.Ability_Mayhem2_Ele_Breaker_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/StayBack/Ability_Mayhem2_StayBack.Ability_Mayhem2_StayBack_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/BegoneDot/Ability_Mayhem2_BegoneDot.Ability_Mayhem2_BegoneDot_C,
        Weight=(BaseValueConstant=0)
    )
)
""")
mod.newline()

mod.comment('Setting Very Hard Modifiers Weights to 0')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_VeryHard.ModSet_Mayhem2_VeryHard',
'ModifierSets',
"""
(
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/DeathFromBeyond/Ability_Mayhem2_DeathFromBeyond.Ability_Mayhem2_DeathFromBeyond_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/RogueLite/Ability_Mayhem2_RogueLite.Ability_Mayhem2_RogueLite_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/CriticalFailure/Ability_Mayhem2_CritFail.Ability_Mayhem2_CritFail_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/Sharpshot/Ability_Mayhem2_Sharpshot.Ability_Mayhem2_Sharpshot_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/PriorityTarget/Ability_Mayhem2_PriorityTarget.Ability_Mayhem2_PriorityTarget_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_All.Ability_Mayhem2_ElementalInfusion_All_C,
        Weight=(BaseValueConstant=0)
    )
)
""")
mod.newline()

### SCALING VALUE ADJUSTMENTS ###

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

for hptype in enemyhp:
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '1',
    hptype,
    1.275
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '2',
    hptype,
    2.55
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '3',
    hptype,
    3.825
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '4',
    hptype,
    5.1
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '5',
    hptype,
    9.5625
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '6',
    hptype,
    19.125
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '7',
    hptype,
    28.6875
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '8',
    hptype,
    38.25
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '9',
    hptype,
    51.0
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '10',
    hptype,
    63.75
    )
    mod.newline()

mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'1',
melee,
2.4
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'2',
melee,
2.8
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'3',
melee,
3.2
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'4',
melee,
3.6
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'5',
melee,
5.0
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'6',
melee,
8.0
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'7',
melee,
11.0
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'8',
melee,
14.0
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'9',
melee,
18.0
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'10',
melee,
32.0
)
mod.newline()

mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'1',
asd,
3.2
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'2',
asd,
4.4
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'3',
asd,
5.6
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'4',
asd,
6.8
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'5',
asd,
11.0
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'6',
asd,
20.0
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'7',
asd,
29.0
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'8',
asd,
38.0
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'9',
asd,
50.0
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'10',
asd,
61.0
)
mod.newline()

mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'1',
asd,
4.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'2',
asd,
6.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'3',
asd,
8.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'4',
asd,
10.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'5',
asd,
17.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'6',
asd,
32.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'7',
asd,
47.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'8',
asd,
62.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'9',
asd,
82.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'10',
asd,
102.0
)
mod.newline()

mlevel=1
while mlevel <= 10:
    mod.comment('Adjusting Passive Skill Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    mlevel,
    passiveskill,
    0
    )
    mod.newline()
    mlevel+=1

mlevel=1
while mlevel <= 10:
    mod.comment('Adjusting Environmental Damage Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    mlevel,
    env,
    0
    )
    mod.newline()
    mlevel+=1

mlevel=1
while mlevel <= 10:
    mod.comment('Adjusting Mayhem World Drop Weights')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    mlevel,
    drop5,
    0.1
    )
    mod.newline()
    mlevel+=1

mlevel=1
while mlevel <= 10:
    mod.comment('Adjusting Mayhem World Drop Weights')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    mlevel,
    drop4,
    1
    )
    mod.newline()
    mlevel+=1

mlevel=1
while mlevel <= 10:
    mod.comment('Adjusting Mayhem World Drop Weights')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    mlevel,
    drop3,
    1
    )
    mod.newline()
    mlevel+=1

mlevel=1
while mlevel <= 10:
    mod.comment('Adjusting Mayhem World Drop Weights')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    mlevel,
    drop2,
    0.001
    )
    mod.newline()
    mlevel+=1

mlevel=1
while mlevel <= 10:
    mod.comment('Adjusting Mayhem World Drop Weights')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    mlevel,
    drop2,
    0.0001
    )
    mod.newline()
    mlevel+=1



###
### BALANCE ADJUSTMENTS
###

### GEAR ###

## WEAPONS

#! Datatable References
atl='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_ATL'
cov='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_COV'
dal='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_DAL'
hyp='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_HYP'
jak='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_JAK'
mal='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_MAL'
ted='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_TED'
tor='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_TOR'
vla='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_VLA'
alisma='/Game/PatchDLC/Alisma/Gear/Weapon/DataTable_WeaponBalance_Alisma'
dande='/Game/PatchDLC/Dandelion/Gear/Weapon/DataTable_WeaponBalance_Dandelion'
cartel='/Game/PatchDLC/Event2/Gear/Weapon/DataTable_WeaponBalance_Event2'
vday='/Game/PatchDLC/EventVDay/Gear/Weapon/DataTable_WeaponBalance_EventVDay'
geran='/Game/PatchDLC/Geranium/Gear/Weapon/DataTable_WeaponBalance_Geranium'
hibis='/Game/PatchDLC/Hibiscus/Gear/Weapon/DataTable_WeaponBalance_Hibiscus'
mayhem2='/Game/PatchDLC/Mayhem2/Gear/Weapon/DataTable_WeaponBalance_Mayhem2'
gtd='/Game/PatchDLC/Takedown2/Gear/Weapons/DataTable_WeaponBalance_Takedown2'

#mod.comment('')
#mod.table_hotfix(Mod.PATCH, 'MatchAll',
#,
#'',
#'',

#)
#mod.newline()

mod.comment('Buffing Destructo Spinner Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
mal,
'SM_DestructoSpin',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.4
)
mod.newline()

mod.comment('Buffing Rebel Yell and Carrier Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
atl,
'AR_Carrier',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1
)
mod.newline()

mod.comment('Nerfing Monarch Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
mayhem2,
'AR_TheMonarch',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Nerfing Reflux Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
mayhem2,
'SG_Reflux',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.4
)
mod.newline()

mod.comment('Buffing Robins Call Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
geran,
'SG_SpeakEasy',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.47
)
mod.newline()

mod.comment('Buffing Magnificient Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
vla,
'PS_Magnificent',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1
)
mod.newline()

mod.comment('Buffing Polybius Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
ted,
'SG_Polybius',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.4
)
mod.newline()

mod.comment('Buffing Creeping Death Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
ted,
'SG_Sludge',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.3
)
mod.newline()

mod.comment('Buffing Scourge Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
tor,
'HW_Swarm',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.25
)
mod.newline()

mod.comment('Nerfing Psycho Stabber Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
cov,
'PS_PsychoStabber',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.10
)
mod.newline()

mod.comment('Buffing Hail Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
dal,
'AR_Hail',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.35
)
mod.newline()

mod.comment('Buffing Bekah Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
jak,
'AR_Bekah',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Nerfing Prompt Critical Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
alisma,
'PS_Voice',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.1
)
mod.newline()

mod.comment('Buffing Devoted Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
mal,
'SM_Devoted',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.2
)
mod.newline()

mod.comment('Buffing Thunderball Fist Damage')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
mal,
'PS_ThunderballFists',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
1.45
)
mod.newline()

mod.comment('Buffing Sniper Crit Bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Base_Data.DataTable_Weapon_Base_Data',
'SniperRifle',
'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
1.5
)
mod.newline()

mod.comment('Buffing Purples')
mod.table_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Rarity_Stats',
'VeryRare',
'DamageScale_6_44C1C8784B7991DCCCF68DA3127A53C0',
1.22
)
mod.newline()

mod.comment('Buffing Blues')
mod.table_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Rarity_Stats',
'Rare',
'DamageScale_6_44C1C8784B7991DCCCF68DA3127A53C0',
1.15
)
mod.newline()

mod.comment('Buffing Weapons Overall')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_GlobalBase.DataTable_Damage_GlobalBase',
'PlayerWeaponDamage',
'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
13.5
)
mod.newline()

## GRENADES

mod.comment('Buffing Grenades')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_GlobalBase.DataTable_Damage_GlobalBase',
'PlayerGrenadeModDamage',
'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
115
)
mod.newline()

## SHIELDS

mod.comment('Removing Nova Berner Scaling from Stinger')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Takedown2/Gear/Shields/Stinger/Parts/Part_Shield_Aug_Stinger',
'SecondaryStackValues.SecondaryStackValues[0]',
'DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\")'
)
mod.newline()

mod.comment('Removing Nova Berner Scaling from Stinger')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Takedown2/Gear/Shields/Stinger/Parts/Part_Shield_Aug_Stinger',
'SecondaryStackValues.SecondaryStackValues[1]',
'DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\")'
)
mod.newline()

mod.comment('Removing Nova Berner Scaling from Stinger')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Takedown2/Gear/Shields/Stinger/Parts/Part_Shield_Aug_Stinger',
'SecondaryStackValues.SecondaryStackValues[2]',
'DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\")'
)
mod.newline()

mod.comment('Adjusting Re-Router Amp Pellet Split')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/Shields/_Design/_Uniques/Vamp/Parts/Part_Shield_Aug_ANS_LGD_ReRouter.Part_Shield_Aug_ANS_LGD_ReRouter:AspectList_ShieldAugmentAspectData.Augment_ShieldAug_VersionOmNom.ShotModifier_WeaponShotModifier',
'bDistributeBetweenProjectiles',
'false'
)
mod.newline()

mod.comment('Adjusting Version O.m Amp Pellet Split')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Parts/Part_Shield_Aug_ANS_LGD_VersionOmNom.Part_Shield_Aug_ANS_LGD_VersionOmNom:AspectList_ShieldAugmentAspectData_0.Augment_ShieldAug_VersionOmNom.ShotModifier_WeaponShotModifier',
'bDistributeBetweenProjectiles',
'false'
)
mod.newline()

## CLASS MODS
#! balance Class Mods after this
#! zerker no cdr for sure
#! reduced effect on flare

cmbal=[
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_BountyHunter',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_CosmicStalker',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_DE4DEYE',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_FriendBot',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RakkCommander',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RedFang',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_BearTrooper',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_BlastMaster',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_BloodLetter',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_MindSweeper',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_Rocketeer',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_ColdWarrior',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_Executor',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_FireBrand',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_Infiltrator',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_Techspert',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Breaker',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Dragon',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Elementalist',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Nimbus',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Phasezerker',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_DLC1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_DLC1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_DLC1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_DLC1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Hib',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/GUN/InvBalD_CM_Gunner_Hib',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/OPE/InvBalD_CM_Operative_Hib',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Hib',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/GUN/InvBalD_CM_Gunner_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/OPE/InvBalD_CM_Operative_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Alisma'
]

cmpartset=[
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_BountyHunter',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_CosmicStalker',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_DE4DEYE',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_FriendBot',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_RakkCommander',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/PartSet_ClassMod_Beastmaster_RedFang',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/PartSet_ClassMod_Gunner_BearTrooper',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/PartSet_ClassMod_Gunner_BlastMaster',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/PartSet_ClassMod_Gunner_BloodLetter',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/PartSet_ClassMod_Gunner_MindSweeper',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/PartSet_ClassMod_Gunner_Rocketeer',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/PartSet_ClassMod_Operative_ColdWarrior',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/PartSet_ClassMod_Operative_Executor',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/PartSet_ClassMod_Operative_FireBrand',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/PartSet_ClassMod_Operative_Infiltrator',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/PartSet_ClassMod_Operative_Techspert',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/PartSet_ClassMod_Siren_Breaker',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/PartSet_ClassMod_Siren_Dragon',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/PartSet_ClassMod_Siren_Elementalist',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/PartSet_ClassMod_Siren_Nimbus',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/PartSet_ClassMod_Siren_Phasezerker',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/PartSet_CM_Beastmaster_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/GUN/PartSet_CM_Gunner_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/PartSet_CM_Operative_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/PartSet_CM_Siren_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/PartSet_CM_Beastmaster_DLC1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/PartSet_CM_Gunner_DLC1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/OPE/PartSet_CM_Operative_DLC1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/SRN/PartSet_CM_Siren_DLC1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/PartSet_CM_Beastmaster_Hib',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/GUN/PartSet_CM_Gunner_Hib',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/OPE/PartSet_CM_Operative_Hib',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/PartSet_CM_Siren_Hib',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/PartSet_CM_Beastmaster_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/GUN/PartSet_CM_Gunner_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/OPE/PartSet_CM_Operative_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/SRN/PartSet_CM_Siren_Alisma'
]

cmprimary=[
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_ReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_HealthRegen',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_ShotgunDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_AreaDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_ActionSkillCooldownRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_AreaDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_MagazineSize',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_HeavyDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_CritDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_ActionSkillCooldownRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_MeleeDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_SniperRifleDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_GrenadeDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_FireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_AreaDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_ActionSkillDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_MeleeDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Elemental/DOT/ClassMod_Part_Stat_Primary_Elemental_DoT_Damage_Shock',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_SMGDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_ReloadSpeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_ActionSkillDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/ClassMod_Part_Stat_Primary_HealthMax',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_AssaultRifleDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_ChargeTime',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_CritDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Vladof_WeaponMagazineSize',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_FireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Manufacturer/ClassMod_Part_Stat_Primary_Maliwan_WeaponFireRate',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_PistolDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/WeaponType/ClassMod_Part_Stat_Primary_AssaultRifleDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_MagazineSize',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_WeaponDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_GrenadeRadius',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Elemental/Resistance/ClassMod_Part_Stat_Primary_Elemental_Resistance_Fire',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Weapon/ClassMod_Part_Stat_Primary_CritDamage',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/AOE/ClassMod_Part_Stat_Primary_GrenadeDamage'
]

for (bal, ps, prim) in zip(cmbal, cmpartset, cmprimary):
    mod.comment('Setting Each COM to Have its Own PartSet and Balance')
    mod.reg_hotfix(Mod.PATCH, '',
    bal,
    'BaseSelectionData',
    'None'
    )
    mod.newline()

    mod.comment('Setting Each COM to Have its Own PartSet and Balance')
    mod.reg_hotfix(Mod.PATCH, '',
    ps,
    'ActorPartReplacementMode',
    'Additive'
    )
    mod.newline()

    data = BL3Data()
    mod.comment('Setting Primary and Secondary Stats')
    com_bal = Balance.from_data(data, bal, replace=True)
    for cat in com_bal.categories:
        if cat.index == 3:
            cat.add_part_name(prim, 1)
            cat.select_multiple=False
            break
    com_bal.hotfix_full(mod)
    mod.newline()

mod.comment('Removing Kill Skill Activation from Seein Dead')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/Table_CM_DLC1',
'OperativeDLC1ClassMod',
'Value_A_2_4C4DFC67484D02BA3DBB029A999F015E',
0.0
)
mod.newline()

mod.comment('Adjusting Seein Dead')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/OPE/UIStat_CM_OP_DLC1_Desc',
'FormatText',
'Zane\'s Kill Skills gain a bonus [skillbold]$VALUE$ effect bonus[/skillbold]. This effect stacks wtih similar effects.'
)
mod.newline()

### CHARACTERS ###

## FORMULA/ATTRIBUTE CHANGE

#! edit descriptions too maybe
#! confident competence didnt get text update
#! click click still shows 0%
passive_to_v1=[
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/LowHpDamage/PassiveSkill_Gunner_LowHPDamage.Default__PassiveSkill_Gunner_LowHPDamage_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/TenaciousDefense/Passive_Gunner_Tenacious.Default__Passive_Gunner_Tenacious_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/ClickClick/PassiveSkill_Gunner_ClickClick.Default__PassiveSkill_Gunner_ClickClick_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/MultiTasker/PassiveSkill_Operative_Multitasker.Default__PassiveSkill_Operative_Multitasker_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ConfidentCompetence/PassiveSkill_Operative_ConfidentCompetence.Default__PassiveSkill_Operative_ConfidentCompetence_C:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer_0',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Samsara/PassiveSkill_Siren_Samsara.Default__PassiveSkill_Siren_Samsara_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/BareKnuckle/PassiveSkill_Siren_BareKnuckle.Default__PassiveSkill_Siren_BareKnuckle_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute'
]
status_to_v1=[
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/LowHpDamage/Status_FullCan_LowHPDamage_P',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/TenaciousDefense/Status_Gunner_Tenacious_WeaponDamage_DA',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/ClickClick/StatusEffect_Gunner_ClickClick_WeaponDamage_DA',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ConfidentCompetence/StatusEffect_Operative_ConfidentCompetence',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/MultiTasker/StatusEffect_Operative_Multitasker',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Samsara/StatusEffect_Siren_Samsara',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/BareKnuckle/StatusEffect_Siren_BareKnuckle_DA'
]

for status in status_to_v1:
    mod.comment('Making Skills V1')
    mod.reg_hotfix(Mod.PATCH, '',
    status,
    'AttributeEffects.AttributeEffects[0].AttributeData',
    '/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier.Att_DamageDealtMultiplier'
    )
    mod.newline()

for passive in passive_to_v1:
    mod.comment('Adjusting Cards for V1 Changes')
    mod.reg_hotfix(Mod.PATCH, '',
     passive,
    'Attribute',
    '/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier.Att_DamageDealtMultiplier'
    )
    mod.newline()

for passive in passive_to_v1:
    desc='[skillbold]Bonus Damage:[/skillbold] $VALUE$'
    if 'LowHPDamage' in passive or 'ConfidentCompetence' in passive or 'ClickClick' in passive:
        desc='[skillbold]Bonus Damage:[/skillbold] Up to $VALUE$'
    if 'Samsara' in passive:
        desc='[skillbold]Bonus Damage:[/skillbold] $VALUE$ per enemy damaged'
    if 'Multitasker' in passive:
        desc='[skillbold]Bonus Damage:[/skillbold] $VALUE$ per active action skill'
    mod.comment('Adjusting Cards for V1 Changes')
    mod.reg_hotfix(Mod.PATCH, '',
    passive,
    'FormatText',
    desc
    )
    mod.newline()

mod.comment('Updating Full Skill Description for V1 Change')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/LowHpDamage/PassiveSkill_Gunner_LowHPDamage.Default__PassiveSkill_Gunner_LowHPDamage_C',
'AbilityDescription',
"Moze\'s [skillbold]Bonus Damage[/skillbold] and [actionskill]Iron Bear\'s[/actionskill] [skillbold]Hard Point Damage[/skillbold] are increased depending on how low their health is. The lower their health, the greater the increase."
)
mod.newline()

mod.comment('Updating Full Skill Description for V1 Change')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/TenaciousDefense/Passive_Gunner_Tenacious.Default__Passive_Gunner_Tenacious_C',
'AbilityDescription',
'Whenever Moze\'s shield is fully depleted, she instantly restores a portion of her [skillbold]shield[/skillbold], and her [skillbold]Bonus Damage[/skillbold] is increased for a short time.<br><br>This skill can only trigger after Moze\'s shields have fully recharged.'
)
mod.newline()

mod.comment('Updating Full Skill Description for V1 Change')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/ClickClick/PassiveSkill_Gunner_ClickClick.Default__PassiveSkill_Gunner_ClickClick_C',
'AbilityDescription',
'Moze gains increased [skillbold]Bonus Damage[/skillbold] as her magazine empties. The less ammo there is remaining, the greater the increase.<br><br>If Moze has a [skillbold]COV[/skillbold] gun equipped, she gains [skillbold]Bonus Damage[/skillbold] as her gun\'s heat increases.'
)
mod.newline()

mod.comment('Updating Full Skill Description for V1 Change')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/MultiTasker/PassiveSkill_Operative_Multitasker.Default__PassiveSkill_Operative_Multitasker_C',
'AbilityDescription',
'Whenever one or more of Zane\'s action skills are active, he gains increased [skillbold]Bonus Damage[/skillbold] for each active action skill.'
)
mod.newline()

mod.comment('Updating Full Skill Description for V1 Change')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ConfidentCompetence/PassiveSkill_Operative_ConfidentCompetence.Default__PassiveSkill_Operative_ConfidentCompetence_C',
'AbilityDescription',
'While Zane\'s shields are active, he gains increased [skillbold]Bonus Damage[/skillbold] and [skillbold]Accuracy[/skillbold]. This bonus is based on the amount of shields he has. The more percent full, the greater the bonus.'
)
mod.newline()

mod.comment('Updating Full Skill Description for V1 Change')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Samsara/PassiveSkill_Siren_Samsara.Default__PassiveSkill_Siren_Samsara_C',
'AbilityDescription',
'Whenever Amara deals damage to an enemy with her [actionskill]Action Skill[/actionskill], she adds a stack of [skillbold]Samsara[/skillbold]. For every stack of [skillbold]Samsara[/skillbold], Amara gains increased [skillbold]Bonus Damage[/skillbold] and [skillbold]Health Regeneration[/skillbold] for a few seconds. Stacks decay after a few seconds.'
)
mod.newline()

mod.comment('Updating Full Skill Description for V1 Change')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/BareKnuckle/PassiveSkill_Siren_BareKnuckle.Default__PassiveSkill_Siren_BareKnuckle_C',
'AbilityDescription',
'Whenever Amara deals melee damage to an enemy, she gains increased [skillbold]Action Skill Damage[/skillbold] and increased [skillbold]Bonus Damage[/skillbold] for a few seconds.'
)
mod.newline()

mod.comment('Changing Fire in the Skag Den to Scale with Passives (Credit to 10 FPS)')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/FireInTheSkagDen/ConditionalDamage_FireInSkagDen.ConditionalDamage_FireInSkagDen',
'OptionalOverrideDamageSource',
'DamageSource_Passive_Skill.DamageSource_Passive_Skill_C'
)
mod.newline()

mod.comment('Giving Nerves of Steel Crit Damage')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/NervesOfSteel/StatusEffect_Operative_NervesOfSteel',
'AttributeEffects.AttributeEffects[0].AttributeData',
'/Game/GameData/Weapons/Att_CriticalHitDamageBonus.Att_CriticalHitDamageBonus'
)
mod.newline()

#! still shows 0%, check back on this
mod.comment('Adjusting Short Description for Nerves of Steel Crit Damage')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/NervesOfSteel/PassiveSkill_Operative_NervesOfSteel.Default__PassiveSkill_Operative_NervesOfSteel_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
'FormatText',
'[skillbold]Critical Damage:[/skillbold] $VALUE$ per second'
)
mod.newline()

mod.comment('Adjusting Description for Nerves of Steel Crit Damage')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/NervesOfSteel/PassiveSkill_Operative_NervesOfSteel.Default__PassiveSkill_Operative_NervesOfSteel_C',
'AbilityDescription',
'Zane gains increasing [skillbold]Critical Damage[/skillbold] and [skillbold]Handling[/skillbold]. The longer his shield is full, the greater the bonus.'
)
mod.newline()

mod.comment('Adjusting Description for Power Inside Flat Bonus')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun11/Passive_Beastmaster_HitAndRun11.Default__Passive_Beastmaster_HitAndRun11_C',
'AbilityDescription',
'FL4K and FL4K\'s [actionskill]Pet[/actionskill] gain increased [skillbold]Damage[/skillbold] when FL4K activates an Action Skill.'
)
mod.newline()

mod.comment('Adjusting Short Description for Arms Deal No Splash Resist')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/ArmsDeal/PassiveSkill_Siren_ArmsDeal.Default__PassiveSkill_Siren_ArmsDeal_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
'FormatText',
''
)
mod.newline()

mod.comment('Adjusting Description for Nerves of Arms Deal No Splash Resis')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/ArmsDeal/PassiveSkill_Siren_ArmsDeal.Default__PassiveSkill_Siren_ArmsDeal_C',
'AbilityDescription',
'Amara deals increased [skillbold]Splash Damage[/skillbold].'
)
mod.newline()

## NUMBER TUNING

mod.comment('Buffing Samsara Damage Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Siren/DataTable_Siren_ConstantValues',
'Samsara_GunDamage',
'Value',
'(BaseValueConstant=0.0498)'
)
mod.newline()

mod.comment('Buffing Wrath Damage Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Siren/DataTable_Siren_ConstantValues',
'Wrath_DamageBonus',
'Value',
'(BaseValueConstant=0.1665)'
)
mod.newline()

mod.comment('Nerfing Overall Iron Bear Damage')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/Att_Calc_Gunner_GlobalSkillDamage',
'Value.Power',
'(BaseValueConstant=0.225)'
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Minigun',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.018
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Minigun_Mod1',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.018
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Minigun_Mod2',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.19
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Minigun_Mod3',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.06
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'BearFist',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.21
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'BearFist_Mod1',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.10
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'BearFist_Mod2',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.14
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'BearFist_Mod3',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.10
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'GL',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.07
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'GL_Mod1',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.032
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'GL_Mod2',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.29
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'GL_Mod3',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.056
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'FalconStrike',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.05
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'FalconStrike_Mod1',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.0174
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'FalconStrike_Mod2',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.023
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'FalconStrike_Mod3',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.17
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Salamander',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.005
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Salamander_Mod1',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.195
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Salamander_Mod2',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.06
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Salamander_Mod3',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.013
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Railgun',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.19
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Railgun_Mod2',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.08
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Railgun_Mod3',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.15
)
mod.newline()

mod.comment('Nerfing Iron Bear Weapons')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Railgun_Mod3_Corrosive',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
0.04
)
mod.newline()

mod.comment('Buffing Duct Tape Mod Chance')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'DuctTapeMod_Chance',
'Value',
'(BaseValueConstant=0.08,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

mod.comment('Buffing Like a Ghost Chance')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'MatrixEffect_DodgeChance',
'Value',
'(BaseValueConstant=0.05,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

mod.comment('Adjusting Like a Ghost Additional Chance')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'MatrixEffect_AdditionalDodgeChance',
'Value',
'(BaseValueConstant=0.025,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

mod.comment('Buffing Pocket Full of Grenades Regen')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'PocketFullOfGrenades_Regen',
'Value',
'(BaseValueConstant=0.10,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

mod.comment('Buffing Best Served Cold Damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_SimpleFormulas',
'NotOrdinaryOrdnance_DamagePerRankCalc',
'Multiplier',
'(BaseValueConstant=0.50,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

mod.comment('Adjusting Values for Nerves of Steel Crit Damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'NervesOfSteal_Accuracy',
'Value',
'(BaseValueConstant=0.025,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

mod.comment('Nerfing Confident Competence')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'ConfidentComfidence_GunDamage',
'Value',
'(BaseValueConstant=0.20,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

mod.comment('Making Power Inside Just a Straight Bonus (No Reliance on Health)')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun_11',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.50
)
mod.newline()

mod.comment('Getting Rid of Full Health Bonus on Power Inside')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas',
'HitAndRun11_TotalDamageBonus',
'Level',
'(BaseValueConstant=0.0,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

mod.comment('Buffing Ambush Predator Crit Damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_Ranged5',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.08
)
mod.newline()

mod.comment('Buffing Grim Harvest Gun Damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_Ranged8',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.05
)
mod.newline()

mod.comment('Reducing LNT CD')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_Ranged11',
'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
1.0
)
mod.newline()

mod.comment('Buffing Rage and Recover Health Regen')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun3',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.040
)
mod.newline()

mod.comment('Buffing Rage and Recover Duration')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun3',
'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
9.0
)
mod.newline()

#! doesnt work currently, need to look into
mod.comment('Buffing Forceful Expression Bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Siren/DataTable_Siren_SimpleFormulas',
'Channeler_BonusDamage',
'Multiplier',
'(BaseValueConstant=0.35,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

mod.comment('Buffing Vigor Movespeed')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Siren/DataTable_Siren_ConstantValues',
'Vigor_MoveSpeed',
'Value',
'(BaseValueConstant=0.06,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

mod.comment('Removing Splash Resistance from Arms Deal')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Siren/DataTable_Siren_ConstantValues',
'ArmsDeal_DamageReduction',
'Value',
'(BaseValueConstant=0.0,DataTableValue=None,BaseValueAttribute=None,BaseValueScale=1.0)'
)
mod.newline()

## SKILL MOVEMENT

mod.comment('Swapping Cloud of Lead and Scrappy')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_BottomlessMag',
'Tiers.Tiers[2].Object..Items.Items[2].Object..AbilityClass',
Mod.get_full_cond('/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/CloudOfLead/PassiveSkill_Gunner_CloudOfLead.PassiveSkill_Gunner_CloudOfLead_C','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Swapping Cloud of Lead and Scrappy')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_BottomlessMag',
'Tiers.Tiers[2].Object..Items.Items[2].Object..ItemFrameName',
'cloudOfLead'
)
mod.newline()

mod.comment('Swapping Cloud of Lead and Scrappy')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_BottomlessMag',
'Tiers.Tiers[1].Object..Items.Items[2].Object..AbilityClass',
Mod.get_full_cond('/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/Scrappy/PassiveSkill_Gunner_Scrappy.PassiveSkill_Gunner_Scrappy_C','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Swapping Cloud of Lead and Scrappy')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_BottomlessMag',
'Tiers.Tiers[1].Object..Items.Items[2].Object..ItemFrameName',
'scrappy'
)
mod.newline()

mod.comment('Swapping Why Cant I Carry All These Grenades and Means of Destruction')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_Explosions',
'Tiers.Tiers[4].Object..Items.Items[1].Object..AbilityClass',
Mod.get_full_cond('/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/MeansOfDestruction/PassiveSkill_Gunner_MeansOfDestruction.PassiveSkill_Gunner_MeansOfDestruction_C','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Swapping Why Cant I Carry All These Grenades and Means of Destruction')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_Explosions',
'Tiers.Tiers[4].Object..Items.Items[1].Object..ItemFrameName',
'meansOfDestruction'
)
mod.newline()

mod.comment('Swapping Why Cant I Carry All These Grenades and Means of Destruction')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_Explosions',
'Tiers.Tiers[2].Object..Items.Items[0].Object..AbilityClass',
Mod.get_full_cond('/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/WhyCantICarryAllTheseGrenades/PassiveSkill_Gunner_WhyCantICarryAllTheseGrenades.PassiveSkill_Gunner_WhyCantICarryAllTheseGrenades_C','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Swapping Why Cant I Carry All These Grenades and Means of Destruction')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_Explosions',
'Tiers.Tiers[2].Object..Items.Items[0].Object..ItemFrameName',
'whyCantICarry'
)
mod.newline()

mod.comment('Swaping Ambush Predator and Grim Harvest')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_RangedSupport',
'Tiers.Tiers[5].Object..Items.Items[0].Object..AbilityClass',
Mod.get_full_cond('/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged5/Passive_Beastmaster_Ranged5.Passive_Beastmaster_Ranged5_C','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Swaping Ambush Predator and Grim Harvest')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_RangedSupport',
'Tiers.Tiers[5].Object..Items.Items[0].Object..ItemFrameName',
'ambushPredator'
)
mod.newline()

mod.comment('Swaping Ambush Predator and Grim Harvest')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_RangedSupport',
'Tiers.Tiers[2].Object..Items.Items[1].Object..AbilityClass',
Mod.get_full_cond('/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged8/Passive_Beastmaster_Ranged8.Passive_Beastmaster_Ranged8_C','BlueprintGeneratedClass')
)
mod.newline()

mod.comment('Swaping Ambush Predator and Grim Harvest')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_RangedSupport',
'Tiers.Tiers[2].Object..Items.Items[1].Object..ItemFrameName',
'grimHarvest'
)
mod.newline()

### MISC BALANCE ###

mod.comment('Nerfing Barrel Damage')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/InteractiveObjects/ExplodingBarrels/_Shared/_Design/Balance/Att_Destructible_Barrel_DamageScalar.Att_Destructible_Barrel_DamageScalar:BP_ConstantValueResolver_C_0',
'Value.BaseValueConstant',
0.00010
)
mod.newline()

mod.comment('Nerfing Barrel Damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_GlobalBase.DataTable_Damage_GlobalBase',
'InteractiveObjectDamage',
'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
5.0
)
mod.newline()


###
### MISC ADJUSTMENTS/FIXES
###

mod.comment('Making Melee Crit (10 FPSs Credit Here)')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/DamageSources/DamageSource_Melee.Default__DamageSource_Melee_C',
'bCanCauseCriticals',
'true'
)
mod.newline()

mod.comment('Fixing Green Monster Click Click Points')
gm_bal_name='/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_DLC1'
clickclick_part='/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/Skills/ClassMod_Part_Skill_Gunner_ClickClikc_DLC1' 

data = BL3Data()
gm_bal = Balance.from_data(data, gm_bal_name)
for cat in gm_bal.categories:
    if cat.index == 5 & cat.num_max == 5:
        cat.add_part_name(clickclick_part, 1)
        cat.add_part_name(clickclick_part, 1)
        break
gm_bal.hotfix_full(mod)
mod.newline()

mod.comment('FL4K Pets Can Melee Crit')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/DamageSources/DamageSource_BeastmasterPet_Melee.DamageSource_BeastmasterPet_Melee',
'bCanCauseCriticals',
'true'
)
mod.newline()

#!(Credit to apocalyptech)
mod.comment('Global Cartel activation switches')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/GameplayGlobals',
        'LeagueInstance',
        1)
mod.newline()

mod.comment('Global Cartel activation switches')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/GameplayGlobals',
        'ActiveLeague',
        'OL_TheCartels')
mod.newline()

mod.comment('Global Cartel activation switches')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Spawning/GlobalSpawnDLCData',
        'DLCs',
        """(
            (
                Data=/Game/PatchDLC/Event2/GameData/SpawnDLCSCripts/SpawnDLC_Cartels.SpawnDLC_Cartels,
                IsEnabled=(BaseValueConstant=1.000000)
            )
        )""")
mod.newline()

mod.comment('Cartel Seasonal NPC')
mod.reg_hotfix(Mod.EARLYLEVEL, 'Sanctuary3_P',
        '/Game/Maps/Sanctuary3/Sanctuary3_Season.Sanctuary3_Season:PersistentLevel.OakMissionSpawner_1.SpawnerComponent.SpawnerStyle_SpawnerStyle_Single',
        'SpawnOptions',
        "SpawnOptionData'/Game/PatchDLC/Event2/NonPlayerCharacters/LeagueNPC/_Design/Spawning/SpawnOptions_LeagueNPC_Season02.SpawnOptions_LeagueNPC_Season02'")

mod.newline()

mod.comment('Cartel Main Menu')
mod.table_hotfix(Mod.PATCH, '',
        '/Game/Common/_Design/Table_MicropatchSwitches',
        'MainMenuAltBackground',
        'Value',
        BVC(bvc=5))
mod.newline()

mod.comment('Cartel Bugfixes')
mod.reg_hotfix(Mod.LEVEL, 'Cartels_P',
        '/Game/PatchDLC/Event2/Maps/Cartels_Mission.Cartels_Mission:PersistentLevel.OakMissionWaypointBox_ACtivateStairSlide.CollisionComp',
        'RelativeScale3D',
        '(X=1.000000,Y=1.000000,Z=1.600000)')
mod.newline()

mod.comment('Fixing P2P Networker secondary element parts (Credit to apocalyptech)')
p2p_bal_name = '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link'
extra_elements = [
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_01_Fire',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_02_Cryo',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_03_Shock',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_04_Radiation',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_05_Corrosive',
        ]

data = BL3Data()
p2p_bal = Balance.from_data(data, p2p_bal_name)
for cat in p2p_bal.categories:
    if len(cat) == 0:
        cat.enabled = True
        for element in extra_elements:
            cat.add_part_name(element, 1)
        break
p2p_bal.hotfix_full(mod)
mod.newline()

mod.comment('Fixing Purple E-Tech Pistols not Spawning')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_ETech_VeryRare',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/COV/Balance/Balance_PS_COV_ETech_VeryRare.Balance_PS_COV_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/COV/Balance/Balance_PS_COV_ETech_VeryRare.Balance_PS_COV_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Dahl/Balance/Balance_DAL_PS_ETech_VeryRare.Balance_DAL_PS_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Dahl/Balance/Balance_DAL_PS_ETech_VeryRare.Balance_DAL_PS_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_VeryRare.Balance_PS_MAL_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_VeryRare.Balance_PS_MAL_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TED/Balance/Balance_PS_Tediore_ETech_VeryRare.Balance_PS_Tediore_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TED/Balance/Balance_PS_Tediore_ETech_VeryRare.Balance_PS_Tediore_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TOR/Balance/Balance_PS_TOR_ETech_VeryRare.Balance_PS_TOR_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TOR/Balance/Balance_PS_TOR_ETech_VeryRare.Balance_PS_TOR_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Vladof/Balance/Balance_PS_VLA_ETech_VeryRare.Balance_PS_VLA_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Vladof/Balance/Balance_PS_VLA_ETech_VeryRare.Balance_PS_VLA_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Giving Psycho Stabber Bullets Melee Damage Instead')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Parts/Part_PS_COV_Barrel_PsychoStabber.Part_PS_COV_Barrel_PsychoStabber:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
'DamageSource',
'BlueprintGeneratedClass\'/Game/GameData/DamageSources/DamageSource_Melee.DamageSource_Melee_C\''
)
mod.newline()

mod.comment('Adjusting Hails Arc to be more akin to BL2s')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Hail/LightProjectile_Hail.Default__LightProjectile_Hail_C',
'InitialRelativeRotation',
'(pitch=14,yaw=0,roll=0)'
)
mod.newline()

mod.comment('Adjusting Harold to be Proper DPUH (Credit to 10 FPS)')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/UnkemptHarold/Parts/Part_PS_TOR_Barrel_UnkemptHarold.Part_PS_TOR_Barrel_UnkemptHarold',
'InventoryAttributeEffects',
"""
(
    (
        AttributeToModify=GbxAttributeData'"/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_BarrelType.Att_BarrelType"',
        ModifierType=OverrideBaseValue,
        ModifierValue=(BaseValueConstant=3.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
    ),
    (
        AttributeToModify=GbxAttributeData'"/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_Weapon_OverrideManufacturerDescription.Att_Weapon_OverrideManufacturerDescription"',
        ModifierType=OverrideBaseValue,
        ModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
    ),
    (
        AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage"',
        ModifierType=ScaleSimple,
        ModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=DataTable'"/Game/PatchDLC/Geranium/Gear/Weapon/DataTable_WeaponBalance_Geranium.DataTable_WeaponBalance_Geranium"',RowName="PS_UnkemptHarold",ValueName="DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
    ),
    (
        AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_MaxLoadedAmmo.Att_Weapon_MaxLoadedAmmo"',
        ModifierType=OverrideBaseValue,
        ModifierValue=(BaseValueConstant=16.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)),(AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_ProjectilesPerShot.Att_Weapon_ProjectilesPerShot"',ModifierType=OverrideBaseValue,ModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
    ),
    (
        AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_ProjectilesPerShot.Att_Weapon_ProjectilesPerShot"',
        ModifierType=ScaleSimple,
        ModifierValue=(BaseValueConstant=7.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
    )
)
"""
)
mod.newline()

mod.comment('Adjusting Harold to be Proper DPUH (Credit to 10 FPS)')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/UnkemptHarold/LightProjectile_TOR_PS_UnkemptHarold.Default__LightProjectile_TOR_PS_UnkemptHarold_C',
'TimedEvents',
'(None)'
)
mod.newline()

mod.comment('Adjusting Harold to be Proper DPUH (Credit to 10 FPS)')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/UnkemptHarold/FiringPattern_UnkemptHarold.FiringPattern_UnkemptHarold',
'RequiredProjectilesPerShot',
0
)
mod.newline()

mod.comment('Adjusting Harold to be Proper DPUH (Credit to 10 FPS)')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/UnkemptHarold/FiringPattern_UnkemptHarold.FiringPattern_UnkemptHarold',
'Samples',
"""
(
    (
        StartRotation=(pitch=-1,yaw=5,roll=0.0),
        EndRotation=(pitch=1.0,yaw=0.0,roll=0.0),
        bUseEndRotation=false,
        bUseID=false,
        ID=1
    ),
    (
        StartRotation=(pitch=-1,yaw=3,roll=0.0),
        EndRotation=(pitch=1.0,yaw=0.0,roll=0.0),
        bUseEndRotation=false,
        bUseID=false,
        ID=2
    ),
    (
        StartRotation=(pitch=-1,yaw=1,roll=0.0),
        EndRotation=(pitch=1.0,yaw=0.0,roll=0.0),
        bUseEndRotation=false,
        bUseID=false,
        ID=3
    ),
    (   
        StartRotation=(pitch=-1,yaw=0,roll=0.0),
        EndRotation=(pitch=1.0,yaw=0.0,roll=0.0),
        bUseEndRotation=false,
        bUseID=false,
        ID=4
    ),
    (
        StartRotation=(pitch=1,yaw=-1,roll=0.0),
        EndRotation=(pitch=1.0,yaw=0.0,roll=0.0),
        bUseEndRotation=false,
        bUseID=false,
        ID=5
    ),
    (
        StartRotation=(pitch=-1,yaw=-3,roll=0.0),
        EndRotation=(pitch=1.0,yaw=0.0,roll=0.0),
        bUseEndRotation=false,
        bUseID=false,
        ID=6
    ),
    (
        StartRotation=(pitch=-1,yaw=-5,roll=0.0),
        EndRotation=(pitch=1.0,yaw=0.0,roll=0.0),
        bUseEndRotation=false,
        bUseID=false,
        ID=7
    )
)
"""
)
mod.newline()


mod.close()