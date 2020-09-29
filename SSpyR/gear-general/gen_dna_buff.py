from bl3hotfixmod import Mod 

#Buff other aspects (bullet speed and firerate feel weird for it)

mod=Mod('dna_buff.bl3hotfix',
'Buff for DNA',
'SSpyR',
[
    ''
],
lic=Mod.CC_BY_SA_40,
cats='gear-smg'
)

mod.comment('Buffing')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Gear/Weapon/DataTable_WeaponBalance_Mayhem2',
'SM_DNA',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
4.5
)
mod.newline()

mod.close()