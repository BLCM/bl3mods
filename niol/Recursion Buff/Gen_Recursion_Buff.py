from bl3hotfixmod import Mod

mod = Mod('RecursionBuff.bl3hotfix',
		  'Recursion Buff',
		  'niol',
		  [
            'This mod buff the projectile recursion by',
			'Giving it almost unlimited projectile bounce',
			'And increasing its damage by 50%',
          ],
		  lic=Mod.CC_BY_SA_40,
		  v='1.0.0',
		  cats='gear-shotgun',)

mod.comment("Extra Projectiles")
mod.reg_hotfix(Mod.PATCH, '',
			   '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/LightProjectile_MAL_SG_Recursion.Default__LightProjectile_MAL_SG_Recursion_C',
			   'NumRecursions',
               999)

mod.newline()
mod.comment("Damage Increase")
mod.table_hotfix(Mod.PATCH,'',
                    '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_MAL',
                    'SG_Recursion',
                    'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
                    1.5)
mod.close()