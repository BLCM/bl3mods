from bl3hotfixmod import Mod

#BPChar_GuardianGemGoblin_C:AIBalanceState_GEN_VARIABLE.DropOnDeathItemPools = 
#(ItemPools=,ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear"'))

mod=Mod('trials_loot_changes.bl3hotfix',
'Trials Loot Adjustments',
'SSpyR',
[
    'Adjusts Trial Boss Drop Rate and Quantity of Drops.',
    'Also gave the Mid-Trial Guardian a chance to drop something from all the Trial Pools.',
    '(Half of this is obsolete now but oh well)'
],
lic=Mod.CC_BY_SA_40,
cats='enemy-drops'
)

mod.comment('Adjusting Skag Rate')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds.Table_LegendarySpecificLootOdds',
'TrialBoss1',
'LegendaryDropChance_Playthrough2_50_11E6C8E8493E0A73AF9B35891E7CE111',
0.90
)
mod.newline()

mod.comment('Adjusting Guardian Rate')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1.CharacterItemPoolExpansions_Raid1',
'CharacterExpansions.CharacterExpansions_Value[49]',
'(DropOnDeathItemPools=((ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGuardian.ItemPool_TrialBossGuardian"',PoolProbability=(BaseValueConstant=0.900000))),ItemPoolExpansions=)',
'(DropOnDeathItemPools=((ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGuardian.ItemPool_TrialBossGuardian"',PoolProbability=(BaseValueConstant=0.200000))),ItemPoolExpansions=)'
)
mod.newline()

mod.comment('Adjusting Tink Rate')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1.CharacterItemPoolExpansions_Raid1',
'CharacterExpansions.CharacterExpansions_Value[66]',
'(DropOnDeathItemPools=((ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink.ItemPool_TrialBossTink"',PoolProbability=(BaseValueConstant=0.900000))),ItemPoolExpansions=)',
'(DropOnDeathItemPools=((ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink.ItemPool_TrialBossTink"',PoolProbability=(BaseValueConstant=0.200000))),ItemPoolExpansions=)'
)
mod.newline()

mod.comment('Adjusting Goon Rate')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1.CharacterItemPoolExpansions_Raid1',
'CharacterExpansions.CharacterExpansions_Value[48]',
'(DropOnDeathItemPools=((ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon.ItemPool_TrialBossGoon"',PoolProbability=(BaseValueConstant=0.900000))),ItemPoolExpansions=)',
'(DropOnDeathItemPools=((ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon.ItemPool_TrialBossGoon"',PoolProbability=(BaseValueConstant=0.200000))),ItemPoolExpansions=)'
)
mod.newline()

mod.comment('Adjusting Mech Rate')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1.CharacterItemPoolExpansions_Raid1',
'CharacterExpansions.CharacterExpansions_Value[54]',
'(DropOnDeathItemPools=((ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech.ItemPool_TrialBossMech"',PoolProbability=(BaseValueConstant=0.900000))),ItemPoolExpansions=)',
'(DropOnDeathItemPools=((ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech.ItemPool_TrialBossMech"',PoolProbability=(BaseValueConstant=0.200000))),ItemPoolExpansions=)'
)
mod.newline()

mod.comment('Adjusting Saurian Rate')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1.CharacterItemPoolExpansions_Raid1',
'CharacterExpansions.CharacterExpansions_Value[60]',
'(DropOnDeathItemPools=((ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSaurian.ItemPool_TrialBossSaurian"',PoolProbability=(BaseValueConstant=0.900000))),ItemPoolExpansions=)',
'(DropOnDeathItemPools=((ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSaurian.ItemPool_TrialBossSaurian"',PoolProbability=(BaseValueConstant=0.200000))),ItemPoolExpansions=)'
)
mod.newline()

mod.comment('Adjusting Skag quantity drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Skag_TrialBoss',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSkag.ItemPool_TrialBossSkag',
'Quantity',
"(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=BlueprintGeneratedClass'\"/Game/GameData/Loot/ItemPools/Init_RandomLootCount_SomeMinOne.Init_RandomLootCount_SomeMinOne_C\"',BaseValueScale=1.000000)",
'(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)')
mod.newline()

mod.comment('Adjusting Guardian quantity drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Guardian_TrialBoss',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGuardian.ItemPool_TrialBossGuardian',
'Quantity',
"(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=BlueprintGeneratedClass'\"/Game/GameData/Loot/ItemPools/Init_RandomLootCount_SomeMinOne.Init_RandomLootCount_SomeMinOne_C\"',BaseValueScale=1.000000)",
'(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)')
mod.newline()

mod.comment('Adjusting Tink quantity drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Tink_TrialBoss',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink.ItemPool_TrialBossTink',
'Quantity',
"(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=BlueprintGeneratedClass'\"/Game/GameData/Loot/ItemPools/Init_RandomLootCount_SomeMinOne.Init_RandomLootCount_SomeMinOne_C\"',BaseValueScale=1.000000)",
'(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)')
mod.newline()

mod.comment('Adjusting Goon quantity drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Goon_TrialBoss',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon.ItemPool_TrialBossGoon',
'Quantity',
"(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=BlueprintGeneratedClass'\"/Game/GameData/Loot/ItemPools/Init_RandomLootCount_SomeMinOne.Init_RandomLootCount_SomeMinOne_C\"',BaseValueScale=1.000000)",
'(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)')
mod.newline()

mod.comment('Adjusting Mech quantity drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Mech_TrialBoss',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech.ItemPool_TrialBossMech',
'Quantity',
"(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=BlueprintGeneratedClass'\"/Game/GameData/Loot/ItemPools/Init_RandomLootCount_SomeMinOne.Init_RandomLootCount_SomeMinOne_C\"',BaseValueScale=1.000000)",
'(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)')
mod.newline()

mod.comment('Adjusting Saurian quantity drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Saurian_TrialBoss',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSaurian.ItemPool_TrialBossSaurian',
'Quantity',
"(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=BlueprintGeneratedClass'\"/Game/GameData/Loot/ItemPools/Init_RandomLootCount_SomeMinOne.Init_RandomLootCount_SomeMinOne_C\"',BaseValueScale=1.000000)",
'(BaseValueConstant=1.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)')
mod.newline()

mod.comment('Adding the Pools to Gem Goblin')
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

mod.close()