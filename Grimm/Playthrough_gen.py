from bl3hotfixmod import Mod

mod=Mod('Playthrough.bl3hotfix',
'Playthrough',
'Grimm',
[
    'Global changes : ',
    '-Enemies now gain more health and damage per level (makes TVHM harder)',
    '-Vending machines have more blue and purples, less legendaries',
    '-World drop is like in TPS',
    '-Changed the scaling of TKs to make them like the base game',
    'TVHM changes:',
    '-Enemies have more health and damage in TVHM',
    '-Elemental damage changes to be more punishing/more rewarding.',
    'Thanks to CodyCode, SsPyR, Apocalyptech, 10 FPS, HackerSmasher, FromDarkHell, Apple1417'

],
lic=Mod.CC_BY_SA_40,
)

mod.comment('Aligning World Drops to be like TPS // SspyR')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
'Uncommon',
'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
10
)
mod.newline()

mod.comment('Aligning World Drops to be like TPS // SspyR')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
'Rare',
'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
1
)
mod.newline()

mod.comment('Aligning World Drops to be like TPS // SspyR')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
'VeryRare',
'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
0.10
)
mod.newline()

mod.comment('Aligning World Drops to be like TPS // SspyR')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity',
'Legendary',
'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
0.010
)
mod.newline()

###VENDING MACHINES

mod.comment('Adjusting Veterans Machine Pool to Only Have Quest Rewards // SsPyr Code')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl',
'BalancedItems',
"""
(
    (
        ItemPoolData=ItemPoolData'\"/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards.DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards\"',
        Weight=(BaseValueConstant=3,DataTableValue=(),BaseValueAttribute=GbxAttributeData'\"/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare.Att_RarityWeight_03_Rare\"'BaseValueScale=0.3),
        Quantity=(BaseValueConstant=15.0)
    )
)
"""
)
mod.newline()

###WEAPONS

mod.comment('Adjusting Weapon Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons',
'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Weapon Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons',
'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Weapon Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons',
'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Weapon Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons',
'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Weapon Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons',
'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
0.01
)
mod.newline()

###WEAPON OF THE DAY

mod.comment('Adjusting Weapon of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons_OfTheDay',
'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Weapon of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons_OfTheDay',
'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Weapon of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons_OfTheDay',
'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
0.01
)
mod.newline()

###GRENADES

mod.comment('Adjusting Grenade Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Grenades',
'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Grenade Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Grenades',
'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Grenade Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Grenades',
'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Grenade Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Grenades',
'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Grenade Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Grenades',
'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
0.01
)
mod.newline()

###GRENADE OF THE DAY

mod.comment('Adjusting Grenade of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Ammo_OfTheDay',
'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Grenade of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Ammo_OfTheDay',
'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Grenade of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Ammo_OfTheDay',
'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
0.01
)
mod.newline()

###SHIELDS

mod.comment('Adjusting Shield Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Shields',
'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Shield Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Shields',
'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Shield Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Shields',
'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Shield Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Shields',
'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Shield Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Shields',
'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
0.01
)
mod.newline()

###CLASS MODS

mod.comment('Adjusting Class Mods Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_ClassMods',
'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Class Mods Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_ClassMods',
'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Class Mods Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_ClassMods',
'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Class Mods Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_ClassMods',
'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Class Mods Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_ClassMods',
'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
0.0
)
mod.newline()

###HEALTH OF THE DAY

mod.comment('Adjusting Shield of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Shield of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Shield of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
0.01
)
mod.newline()

mod.comment('Adjusting Class Mod of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
0.1
)
mod.newline()

mod.comment('Adjusting Class Mod of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
1.0
)
mod.newline()

mod.comment('Adjusting Class Mod of the Day Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
'BalancedItems.BalancedItems[5].Weight.BaseValueScale',
0.0
)
mod.newline()

###PLAYER DAMAGE

player_damage_base='/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_GlobalBase'
health_damage='/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers'
dots='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage'
barrel='/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_IO_Balance'
elerarity='/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity'
damage_tvhm='/Game/Enemies/_Shared/_Design/Balance/Table_DefaultEnemyBalance'
damagetype='/Game/GameData/Balance/HealthAndDamage/DataTable_HealthTypeBalance'

###Damage Types NVHM/TVHM

#Flesh

mod.comment('Flesh Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh',
'NonelementalModifier',
1.0
)
mod.newline()

mod.comment('Flesh Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh',
'CorrosiveModifier',
0.8
)
mod.newline()

mod.comment('Flesh Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh',
'CryoModifier',
1.0
)
mod.newline()

mod.comment('Flesh Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh',
'FireModifier',
1.5
)
mod.newline()

mod.comment('Flesh Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh',
'ShockModifier',
0.8
)
mod.newline()

mod.comment('Flesh Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh',
'RadiationModifier',
1
)
mod.newline()

#Shield

mod.comment('Shield Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield',
'NonelementalModifier',
1
)
mod.newline()

mod.comment('Shield Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield',
'CorrosiveModifier',
0.7
)
mod.newline()

mod.comment('Shield Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield',
'CryoModifier',
0.7
)
mod.newline()

mod.comment('Shield Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield',
'FireModifier',
0.7
)
mod.newline()

mod.comment('Shield Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield',
'ShockModifier',
2.0
)
mod.newline()

mod.comment('Shield Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield',
'RadiationModifier',
1.2
)
mod.newline()

#Armor

mod.comment('Armor Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor',
'NonelementalModifier',
0.8
)
mod.newline()

mod.comment('Armor Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor',
'CorrosiveModifier',
1.5
)
mod.newline()

mod.comment('Armor Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor',
'CryoModifier',
1.2
)
mod.newline()

mod.comment('Armor Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor',
'FireModifier',
0.7
)
mod.newline()

mod.comment('Armor Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor',
'ShockModifier',
0.8
)
mod.newline()

mod.comment('Armor Type NVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor',
'RadiationModifier',
0.7
)
mod.newline()

#Flesh_PT2

mod.comment('Flesh Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh_PT2',
'NonelementalModifier',
1.0
)
mod.newline()

mod.comment('Flesh Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh_PT2',
'CorrosiveModifier',
0.65
)
mod.newline()

mod.comment('Flesh Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh_PT2',
'CryoModifier',
1.0
)
mod.newline()

mod.comment('Flesh Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh_PT2',
'FireModifier',
1.75
)
mod.newline()

mod.comment('Flesh Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh_PT2',
'ShockModifier',
0.65
)
mod.newline()

mod.comment('Flesh Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Flesh_PT2',
'RadiationModifier',
1.0
)
mod.newline()

#Shield_PT2

mod.comment('Shield Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield_PT2',
'NonelementalModifier',
1.0
)
mod.newline()

mod.comment('Shield Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield_PT2',
'CorrosiveModifier',
0.5
)
mod.newline()

mod.comment('Shield Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield_PT2',
'CryoModifier',
0.5
)
mod.newline()

mod.comment('Shield Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield_PT2',
'FireModifier',
0.5
)
mod.newline()

mod.comment('Shield Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield_PT2',
'ShockModifier',
2.5
)
mod.newline()

mod.comment('Shield Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Shield_PT2',
'RadiationModifier',
1.5
)
mod.newline()

#Armor_PT2

mod.comment('Armor Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor_PT2',
'NonelementalModifier',
0.8
)
mod.newline()

mod.comment('Armor Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor_PT2',
'CorrosiveModifier',
1.75
)
mod.newline()

mod.comment('Armor Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor_PT2',
'CryoModifier',
1.5
)
mod.newline()

mod.comment('Armor Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor_PT2',
'FireModifier',
0.5
)
mod.newline()

mod.comment('Armor Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor_PT2',
'ShockModifier',
0.65
)
mod.newline()

mod.comment('Armor Type TVHM')
mod.table_hotfix(Mod.PATCH, '',
damagetype,
'Armor_PT2',
'RadiationModifier',
0.5
)
mod.newline()


#Character Base Damage

mod.newline()
mod.comment('Increasing Base Melee Damage')
mod.table_hotfix(Mod.PATCH, '',
player_damage_base,
'PlayerMeleeDamage',
'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
28
)
mod.newline()

mod.comment('Increasing Base Slam Damage')
mod.table_hotfix(Mod.PATCH, '',
player_damage_base,
'PlayerGroundSlamDamage',
'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
100
)
mod.newline()

mod.table_hotfix(Mod.PATCH, '',
player_damage_base,
'PlayerSlideDamage',
'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
18
)
mod.newline()

mod.table_hotfix(Mod.PATCH, '',
player_damage_base,
'PlayerGrenadeModDamage',
'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
75
)
mod.newline()

###ENEMIES DAMAGE

mod.comment('Increasing Enemy Damage')
mod.table_hotfix(Mod.PATCH, '',
health_damage,
'AI_AdditionalDamagePerLevel',
'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
0.1
)
mod.newline()

mod.comment('Increasing Enemy Health')
mod.table_hotfix(Mod.PATCH, '',
health_damage,
'AI_AdditionalHealthPerLevel',
'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
0.1
)
mod.newline()

mod.comment('Increasing Enemy Health in TVHM')
mod.table_hotfix(Mod.PATCH, '',
health_damage,
'Playthrough2_GlobalHealthScaler',
'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
1.4
)
mod.newline()

mod.comment('Increasing Enemy Damage in TVHM')
mod.table_hotfix(Mod.PATCH, '',
damage_tvhm,
'Default_PT2',
'DamageMultiplier_LevelBased_23_3CAF34804D650A98AB8FAFAB37CB87FF',
1.12
)
mod.newline()

###GENERAL CHANGES

mod.comment('Decreasing Barrel Damage')
mod.table_hotfix(Mod.PATCH, '',
barrel,
'Barrel',
'Damage_13_560366A1463D4183F137F3AB10204686',
1.05
)
mod.newline()

mod.comment('Increasing Vehicle Health')
mod.table_hotfix(Mod.PATCH, '',
health_damage,
'Vehicle_HealthScaler',
'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
2.5
)
mod.newline()

mod.comment('Increasing DOTs Damage')
mod.table_hotfix(Mod.PATCH, '',
dots,
'DamageScale_DOT',
'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
1.2
)
mod.newline()

mod.comment('Increasing DOTs Damage')
mod.table_hotfix(Mod.PATCH, '',
dots,
'DamageScale_DOT',
'Shock_8_684654654B332D94359F79BEB2DB90AA',
1.2
)
mod.newline()

mod.comment('Increasing DOTs Damage')
mod.table_hotfix(Mod.PATCH, '',
dots,
'DamageScale_DOT',
'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
1.2
)
mod.newline()

mod.comment('Increasing DOTs Damage')
mod.table_hotfix(Mod.PATCH, '',
dots,
'DamageScale_DOT',
'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
1.2
)
mod.newline()

mod.comment('Increasing DOTs Damage')
mod.table_hotfix(Mod.PATCH, '',
dots,
'DamageScale_DOT',
'Radiation_13_2500317646FAD2F4916D158835B29E83',
1.2
)
mod.newline()

###ELEMENTAL RARITY

mod.comment('Common Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Common',
'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
1.0
)
mod.newline()

mod.comment('Common Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Common',
'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
0.0625

)
mod.newline()

mod.comment('Common Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Common',
'Shock_8_684654654B332D94359F79BEB2DB90AA',
0.0625

)
mod.newline()

mod.comment('Common Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Common',
'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
0.0625

)
mod.newline()

mod.comment('Common Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Common',
'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
0.0625

)
mod.newline()

mod.comment('Common Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Common',
'Radiation_13_2500317646FAD2F4916D158835B29E83',
0.0625

)
mod.newline()

mod.comment('UnCommon Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'UnCommon',
'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
1.0
)
mod.newline()

mod.comment('UnCommon Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'UnCommon',
'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
0.125
)
mod.newline()

mod.comment('UnCommon Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'UnCommon',
'Shock_8_684654654B332D94359F79BEB2DB90AA',
0.125
)
mod.newline()

mod.comment('UnCommon Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'UnCommon',
'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
0.125
)
mod.newline()

mod.comment('UnCommon Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'UnCommon',
'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
0.125
)
mod.newline()

mod.comment('UnCommon Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'UnCommon',
'Radiation_13_2500317646FAD2F4916D158835B29E83',
0.125
)
mod.newline()

mod.comment('Rare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Rare',
'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
1.0
)
mod.newline()

mod.comment('Rare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Rare',
'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
0.250
)
mod.newline()

mod.comment('Rare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Rare',
'Shock_8_684654654B332D94359F79BEB2DB90AA',
0.250
)
mod.newline()

mod.comment('Rare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Rare',
'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
0.250
)
mod.newline()

mod.comment('Rare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Rare',
'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
0.250
)
mod.newline()

mod.comment('Rare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'Rare',
'Radiation_13_2500317646FAD2F4916D158835B29E83',
0.250
)
mod.newline()

mod.comment('VeryRare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'VeryRare',
'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
1.0
)
mod.newline()

mod.comment('VeryRare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'VeryRare',
'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
0.50
)
mod.newline()

mod.comment('VeryRare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'VeryRare',
'Shock_8_684654654B332D94359F79BEB2DB90AA',
0.50
)
mod.newline()

mod.comment('VeryRare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'VeryRare',
'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
0.50
)
mod.newline()

mod.comment('VeryRare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'VeryRare',
'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
0.50
)
mod.newline()

mod.comment('VeryRare Elemental Rarity')
mod.table_hotfix(Mod.PATCH, '',
elerarity,
'VeryRare',
'Radiation_13_2500317646FAD2F4916D158835B29E83',
0.50
)
mod.newline()

### Scaling Back Takedowns And DLC4 health

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

#BUGS TK2

mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_GroundTD2',
bugstk2,
'Nekrobug_GroundTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_FlyerTD2',
bugstk2,
'Nekrobug_FlyerTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0

)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_HopperTD2',
bugstk2,
'Nekrobug_HopperTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
bugstk2,
'Nekrobug_BadassTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
4.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
bugstk2,
'Nekrobug_BadassTD2',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
bugstk2,
'Nekrobug_BadassTD2',
'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
3.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
bugstk2,
'Nekrobug_BadassTD2',
'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',
3.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
bugstk2,
'Nekrobug_BadassTD2',
'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113',
3.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BroodlingTD2',
bugstk2,
'Nekrobug_BroodlingTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.3
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BomberTD2',
bugstk2,
'Nekrobug_BomberTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.35
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_Flyer_FodderTD2',
bugstk2,
'Nekrobug_Flyer_FodderTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.25
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_GroundTD2_BossAdd',
bugstk2,
'Nekrobug_GroundBossFodderTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_HopperTD2_BossAdd',
bugstk2,
'Nekrobug_HopperBossFodderTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BroodlingTD2_BossAdd',
bugstk2,
'Nekrobug_BroodlingBossFodderTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_Nekrobug_BadassTD2_BossAdd',
bugstk2,
'Nekrobug_BadassBossFodderTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
4.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_Nekrobug_BadassTD2_BossAdd',
bugstk2,
'Nekrobug_BadassBossFodderTD2',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.25
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_Nekrobug_BadassTD2_BossAdd',
bugstk2,
'Nekrobug_BadassBossFodderTD2',
'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
3.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_Nekrobug_BadassTD2_BossAdd',
bugstk2,
'Nekrobug_BadassBossFodderTD2',
'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',
3.0
)
mod.newline()

mod.comment('Bugs Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_Nekrobug_BadassTD2_BossAdd',
bugstk2,
'Nekrobug_BadassBossFodderTD2',
'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113',
3.0
)
mod.newline()

#GUARDIANS TK2

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithTD2',
guardiantk2,
'Guardian_WraithTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithTD2',
guardiantk2,
'Guardian_WraithTD2',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianSpectreTD2',
guardiantk2,
'Guardian_SpectreTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.7
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianSpectreTD2',
guardiantk2,
'Guardian_SpectreTD2',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.35
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianSeraTD2',
guardiantk2,
'Guardian_SeraTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianSeraTD2',
guardiantk2,
'Guardian_SeraTD2',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianHeraldTD2',
guardiantk2,
'Guardian_HeraldTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
3.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianHeraldTD2',
guardiantk2,
'Guardian_HeraldTD2',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
3.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithBadassTD2',
guardiantk2,
'Guardian_WraithBadassTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
3.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithBadassTD2',
guardiantk2,
'Guardian_WraithBadassTD2',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
3.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithBossFodderTD2',
guardiantk2,
'Guardian_WraithBossFodderTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.2
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithBossFodderTD2',
guardiantk2,
'Guardian_WraithBossFodderTD2',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianSpectreBossFodderTD2',
guardiantk2,
'Guardian_SpectreBossFodderTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.2
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianSpectreBossFodderTD2',
guardiantk2,
'Guardian_SpectreBossFodderTD2',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianSeraBossFodderTD2',
guardiantk2,
'Guardian_SeraBossFodderTD2',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.5
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianSeraBossFodderTD2',
guardiantk2,
'Guardian_SeraBossFodderTD2',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianReaperTD2',
guardiantk2,
'Guardian_Reaper',
'DamageMultiplier_LevelBased_23_3CAF34804D650A98AB8FAFAB37CB87FF',
1.8
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianReaperTD2',
guardiantk2,
'Guardian_Reaper',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
5.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianReaperTD2',
guardiantk2,
'Guardian_Reaper',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
5.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianReaperTD2',
guardiantk2,
'Guardian_Reaper',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
5.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithTD2_LOWXP',
guardiantk2,
'Guardian_WraithTD2_LOWXP',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithTD2_LOWXP',
guardiantk2,
'Guardian_WraithTD2_LOWXP',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithTD2_LOWXP',
guardiantk2,
'BPChar_GuardianSpectreTD2_LOWXP',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.7
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithTD2_LOWXP',
guardiantk2,
'BPChar_GuardianSpectreTD2_LOWXP',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.35
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianSeraTD2_LOWXP',
guardiantk2,
'Guardian_SeraTD2_LOWXP',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianSeraTD2_LOWXP',
guardiantk2,
'Guardian_SeraTD2_LOWXP',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianHeraldTD2_LOWXP',
guardiantk2,
'Guardian_HeraldTD2_LOWXP',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
3.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianHeraldTD2_LOWXP',
guardiantk2,
'Guardian_HeraldTD2_LOWXP',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
3.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithBadassTD2_LOWXP',
guardiantk2,
'Guardian_WraithBadassTD2_LOWXP',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
3.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianWraithBadassTD2_LOWXP',
guardiantk2,
'Guardian_WraithBadassTD2_LOWXP',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
3.0
)
mod.newline()

#GUARDIANS BRUTE TK2

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianBruteBomber',
bossestk2,
'GuardianBrute_Bomber',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
3.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianBruteBomber_BossFodder',
bossestk2,
'GuardianBrute_BomberFodder',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.7
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianBruteMiniboss',
bossestk2,
'GuardianBrute_Miniboss',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
35.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianBruteMiniboss',
bossestk2,
'GuardianBrute_Miniboss',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
35.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianBruteMiniboss',
bossestk2,
'GuardianBrute_Miniboss',
'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
35.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianBruteBoss',
bossestk2,
'GuardianBrute_Boss',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
55.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianBruteBoss',
bossestk2,
'GuardianBrute_Boss',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
65.0
)
mod.newline()

mod.comment('Guardians Health Takedown2')
mod.table_hotfix(Mod.CHAR, 'BPChar_GuardianBruteBoss',
bossestk2,
'GuardianBrute_Boss',
'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
75.0
)
mod.newline()

#TAKEDOWN1 BEHEMOTHS

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothMiniWalker',
behemoth,
'Behemoth_MiniWalker',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
3.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothMiniWalker',
behemoth,
'Behemoth_MiniWalker',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
3.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothGunner',
behemoth,
'Behemoth_Gunner',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
12.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothGunner',
behemoth,
'Behemoth_Gunner',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothRocketeer',
behemoth,
'Behemoth_Rocketeer',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
15.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothRocketeer',
behemoth,
'Behemoth_Rocketeer',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
2.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothCarrier',
behemoth,
'Behemoth_Carrier',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
12.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothCarrier',
behemoth,
'Behemoth_Carrier',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
12.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothRaid',
behemoth,
'Behemoth_Raid',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
80.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothRaid',
behemoth,
'Behemoth_Raid',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
80.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothRaid',
behemoth,
'Behemoth_Raid',
'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
50.0
)
mod.newline()
 
#TAKEDOWN FRONTRUNNERS

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_FrontrunnerBasic_Raid1',
frontrunner,
'Frontrunner',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_FrontrunnerBasic_Raid1',
frontrunner,
'Frontrunner',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.4
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_FrontrunnerJammer_Raid1',
frontrunner,
'GunWolf',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_FrontrunnerJammer_Raid1',
frontrunner,
'GunWolf',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_FrontrunnerStriker_Raid1',
frontrunner,
'Nullhound',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
2.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_FrontrunnerStriker_Raid1',
frontrunner,
'Nullhound',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Frontrunner_Badass_Raid1',
frontrunner,
'Fronttunner_Badass',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
4.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Frontrunner_Badass_Raid1',
frontrunner,
'Fronttunner_Badass',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
4.0
)
mod.newline()

#HEAVY TAKEDOWN1

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_GunnerDarkRaid1',
heavy,
'Heavy_Gunner',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
4.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_BasicDarkRaid1',
heavy,
'Heavy_Pyrotech',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
5.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_BasicDarkRaid1',
heavy,
'Heavy_Pyrotech',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_PowerhouseDarkRaid1',
heavy,
'Heavy_Powerhouse',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
5.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_PowerhouseDarkRaid1',
heavy,
'Heavy_Powerhouse',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_IcebreakerDarkRaid1',
heavy,
'Heavy_Icebreaker',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
5.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_IcebreakerDarkRaid1',
heavy,
'Heavy_Icebreaker',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_AcidrainDarkRaid1',
heavy,
'Heavy_Acidrain',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
5.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_AcidrainDarkRaid1',
heavy,
'Heavy_Acidrain',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_BadassDarkRaid1',
heavy,
'Heavy_Badass',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
10.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_Heavy_BadassDarkRaid1',
heavy,
'Heavy_Badass',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
2.0
)
mod.newline()

#MECHS TAKEDOWN1

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_MechRaidBossBar',
mech,
'Mech_Raid_BossBar',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
45.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_MechRaidBossA',
mech,
'Mech_RaidBossA',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
15.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_MechRaidBossA',
mech,
'Mech_RaidBossA',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
10.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_MechRaidBossB',
mech,
'Mech_RaidBossB',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
15.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_MechRaidBossB',
mech,
'Mech_RaidBossB',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
10.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_MechRaidBossC',
mech,
'MechRaidBossC',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
15.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_MechRaidBossC',
mech,
'MechRaidBossC',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
10.0
)
mod.newline()

#RATCHES TAKEDOWN1

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'Ratch_Larva',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.25
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchPupRaid1',
ratch,
'Ratch_Pup',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'Ratch_Basic',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'Ratch_Basic',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'Ratch_Basic',
'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchSpitterRaid1',
ratch,
'Ratch_Spitter',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchSpitterRaid1',
ratch,
'Ratch_Spitter',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchSpitterRaid1',
ratch,
'Ratch_Spitter',
'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'Ratch_Swarm',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
3.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'Ratch_Birther',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
3.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'Ratch_Birther',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
4.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBadassRaid1',
ratch,
'Ratch_Badass',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
6.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBadassRaid1',
ratch,
'Ratch_Badass',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
4.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBadassRaid1',
ratch,
'Ratch_Badass',
'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
4.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'Ratch_Hive',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
8.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'Ratch_Hive',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
5.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'Ratch_Hive',
'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
5.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchPupRaid1',
ratch,
'RatchEgg_Pup',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.75
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBasicRaid1',
ratch,
'RatchEgg_Basic',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.2
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_RatchBadassRaid1',
ratch,
'RatchEgg_Badass',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
5.0
)
mod.newline()

#TROPPERS TAKEDOWN1

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperBasicDarkRaid1',
trooper,
'Trooper_Basic',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.85
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperBasicDarkRaid1',
trooper,
'Trooper_Basic',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperMedicDarkRaid1',
trooper,
'Trooper_Medic',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
0.9
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperMedicDarkRaid1',
trooper,
'Trooper_Medic',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperFlashDarkRaid1',
trooper,
'Trooper_Flash',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperFlashDarkRaid1',
trooper,
'Trooper_Flash',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperBasicDarkRaid1',
trooper,
'Trooper_Melee',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.2
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperBasicDarkRaid1',
trooper,
'Trooper_Melee',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperJetpackDarkRaid1',
trooper,
'Trooper_Jetpack',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperJetpackDarkRaid1',
trooper,
'Trooper_Jetpack',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperBasicDarkRaid1',
trooper,
'Trooper_Shotgun',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
2.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperBasicDarkRaid1',
trooper,
'Trooper_Shotgun',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperBadassDarkRaid1',
trooper,
'Trooper_Badass',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
4.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperBadassDarkRaid1',
trooper,
'Trooper_Badass',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
1.0
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperReflectDark',
trooper,
'Trooper_Reflect',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.2
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperReflectDark',
trooper,
'Trooper_Reflect',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperStealthDark',
trooper,
'Trooper_Stealth',
'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
1.2
)
mod.newline()

mod.comment('Health Takedown1')
mod.table_hotfix(Mod.CHAR, 'BPChar_TrooperStealthDark',
trooper,
'Trooper_Stealth',
'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
0.5
)
mod.newline()