from bl3hotfixmod import Mod

mod=Mod('fix_siren_rad.txt',
        'Fix for Siren Rad',
        'SSpyR',
        [
            ''
        ],
        lic=Mod.CC_BY_SA_40
        )

mod.reg_hotfix(Mod.PATCH, '',
               '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/SkillEnd_AttunedEleDamage/UIStat_Siren_SkillEnd_AttunedSkillDamage',
               'Initializer.DataTableValue.RowName',
               'Siren_SkillEnd_AttunedBonusDamage')
mod.newline()

mod.close