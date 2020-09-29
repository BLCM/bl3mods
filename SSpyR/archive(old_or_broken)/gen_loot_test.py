from bl3hotfixmod import Mod 

mod=Mod('loot_test.txt',
'Loot Test',
'SSpyR',
[
    'Mod to up Drop Rate to test things.',
    'I change this each time I need a new char to test.'
],
lic=Mod.CC_BY_SA_40
)

mod.comment('Adjusting rate to 100%')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothRaid',
'/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds',
'RaidBoss',
'LegendaryDropChance_Playthrough2_50_11E6C8E8493E0A73AF9B35891E7CE111',
1.00
)
mod.newline()

mod.comment('Adjusting quantity drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_BehemothRaid',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool',
'Quantity',
'(BaseValueConstant=20)')
mod.newline()

mod.close()