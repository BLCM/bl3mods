from bl3hotfixmod import Mod

#!no beuno
mod=Mod('jakobs_pistols_fix.txt',
'Jakobs Pistols Buff Fix',
'SSpyR',
[
    ''
],
lic=Mod.CC_BY_SA_40,
)

mod.comment('Attempt a MatchAll to Fix Issue')
mod.table_hotfix(Mod.PATCH, 'MatchAll',
'/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Base_Data.DataTable_Weapon_Base_Data',
'Pistol',
'DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39',
1.3
)

#mod.comment('Trying MatchAll Back on the Jakobs Nerf')
#mod.table_hotfix(Mod.PATCH, '',
#'/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_DamageScale.DataTable_Weapon_DamageScale',
#'Pistol',
#'Jakobs_60_F95FBBA045F4F1899B3F7AB7A2CF0F22',
#1.3
#)