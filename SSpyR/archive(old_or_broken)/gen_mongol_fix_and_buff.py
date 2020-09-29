from bl3hotfixmod import Mod

mod=Mod('mongol_fix_and_buff.txt',
'Mongol Spawn Fix and Buff',
'SSpyR',
[
    'Enables the Mongol to Drop and Buffs it to Respectable Levels.'
],
lic=Mod.CC_BY_SA_40
)

mod.comment('Making it drop')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Goon_Rare01',
'/Game/GameData/Loot/ItemPools/Unique/ItemPool_Piss_ThunkandSloth.ItemPool_Piss_ThunkandSloth',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/Gear/GrenadeMods/_Design/_Unique/Piss/Balance/InvBalD_GM_Piss.InvBalD_GM_Piss,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/GrenadeMods/_Design/_Unique/Piss/Balance/InvBalD_GM_Piss.InvBalD_GM_Piss\"',
        Weight=(BaseValueConstant=1)
    ),
    (
        InventoryBalancedData=/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol.Balance_HW_VLA_Mongol,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol.Balance_HW_VLA_Mongol\"',
        Weight=(BaseValueConstant=1)
    )
)
""")
mod.newline()

new_val=2.3

mod.comment('Buffing it')
mod.table_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_VLA.DataTable_WeaponBalance_Unique_VLA',
'HW_Mongol',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
new_val)
mod.newline()

mod.close