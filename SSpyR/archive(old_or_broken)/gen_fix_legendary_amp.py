from bl3hotfixmod import Mod

mod=Mod('fix_legendary_amp.txt',
        'Making Legendary Amp Shields Apply to Each Pellet',
        'SSpyR',
        [
            ''
        ],
        lic=Mod.CC_BY_SA_40
        )

mod.comment('Adjusting Re-Router')
mod.reg_hotfix(Mod.PATCH, '',
               '/Game/Gear/Shields/_Design/_Uniques/Vamp/ShieldAug_VAMP',
               'bDistributeBetweenProjectiles',
               'false'
               )
mod.newline()

mod.comment('Adjusting Version O.m')
mod.reg_hotfix(Mod.PATCH, '',
               '/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/ShieldAug_VersionOmNom',
               'bDistributeBetweenProjectiles',
               'false'
               )
mod.newline()

mod.close()