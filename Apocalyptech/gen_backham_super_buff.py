#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('backham_super_buff.txt',
        'Super buff for Back Ham.  Cheating!',
        [
        ],
        'BackHam',
        )

# Pretty sure that this value defines a fractional scale, so we'll approach
# 100% but not quite get there.  Also I'm guessing that probably only
# Primary_1 is used, but since they're all set to -1.25 in the vanilla data
# files, I'll set for all of 'em anyway.
mod.comment('Damage Reduction (default value: -1.25)')
for attr in [
        'Primary_1_56_207C26E1450330458D6C38B245C338C5',
        'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
        'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
        ]:
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/Gear/Shields/_Design/Balance/ShieldAug_Unique_BalanceData.ShieldAug_Unique_BalanceData',
            'BackHam',
            attr,
            -1000)
mod.newline()

# Apply reduction to all angles
mod.comment('Apply damage reduction regardless of direction')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Gear/Shields/_Design/_Uniques/BackHam/CDM_BackHam.CDM_BackHam',
        'bUseHitDirectionAngle',
        'False')
mod.newline()

mod.close()
