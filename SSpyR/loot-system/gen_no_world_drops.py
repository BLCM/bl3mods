from bl3hotfixmod import Mod

# Make Legendaries not World Drop (Except DLC COMs)
# Look Back Here and Edit for DLC4

mod=Mod('no_world_drops.bl3hotfix',
'Legendaries No World Drop',
'SSpyR',
[
    'Taking Away World Drop Legendaries.',
    'Except Those That are Only World Drops.',
    'Still need to update this file specifically with DLC stuff.'
],
lic=Mod.CC_BY_SA_40,
cats='loot-system'
)

pools=[
    '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_All',
    '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All',
    '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts',
    '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Pistols_All',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_SniperAndHeavy_All',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_ARandSMG_All',
    '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_Shields_All_Hibiscus',
    '/Game/PatchDLC/Geranium/GameData/Loot/ItemPool_GrenadeMods_All_Geranium'
]

for pool in pools:
    mod.comment('Adjusting to Remove Legendaries from World Drops')
    mod.reg_hotfix(Mod.PATCH, '',
    pool,
    'BalancedItems.BalancedItems[4].Weight',
    '(BaseValueConstant=0,BaseValueAttribute=None,BaseValueScale=0)'
    )
    mod.newline()

dlcpools=[
    '/Game/PatchDLC/Dandelion/GameData/Loot/ItemPool_Guns_All_Dandelion',
    '/Game/PatchDLC/Dandelion/GameData/Loot/ItemPool_Guns_All_Dandelion_Boss',
    '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_Guns_All_Hibiscus',
    '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_GrenadeMods_All_Hibiscus', 
    '/Game/PatchDLC/Geranium/GameData/Loot/ItemPool_Guns_All_Geranium',
    '/Game/PatchDLC/Geranium/GameData/Loot/ItemPool_Shields_All_Geranium'
]

for dlcpool in dlcpools:
    mod.comment('Adjusting to Remove Legendaries from World Drops')
    mod.reg_hotfix(Mod.PATCH, '',
    dlcpool,
    'BalancedItems.BalancedItems[4].Weight',
    '(BaseValueConstant=0,BaseValueAttribute=None,BaseValueScale=0)'
    )
    mod.newline()
    mod.comment('Adjusting to Remove Legendaries from World Drops')
    mod.reg_hotfix(Mod.PATCH, '',
    dlcpool,
    'BalancedItems.BalancedItems[5].Weight',
    '(BaseValueConstant=0,BaseValueAttribute=None,BaseValueScale=0)'
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