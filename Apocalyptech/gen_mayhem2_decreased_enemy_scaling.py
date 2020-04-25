#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('mayhem2_decreased_enemy_scaling.txt',
        'Mayhem 2.0: Decreased Enemy Scaling',
        [
            "I'd like to play around with Mayhem modifiers, but the extra bullet-",
            "sponginess doesn't really do it for me.  This'll drop the enemy",
            "health/shield/armor scaling down pretty significantly.",
        ],
        'M2EnemyScaling',
        )

# TODO: Honestly I should really nerf the Mayhem gun parts themselves, too,
# 'cause they're gonna end up OP as hell.  Unfortunately the actual part
# objects only seem to really have scaling for cost and weapon score in them,
# and not the actual scaling.  Presumably that's built-in somehow to the
# OakWeaponMayhemPartData object type.

# Default scaling values:
#scaling = [2, 4, 6, 8, 15, 30, 50, 75, 100, 125]

# My new values (hah, pathetic!)
scaling = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]

for mayhem_level_minus_one, scale_value in enumerate(scaling):
    mayhem_level = mayhem_level_minus_one + 1
    mod.comment('Mayhem {}'.format(mayhem_level))
    for col_name in [
            'HealthSimpleScalar_42_0499AACF43FDF39B7084E2BB63E4BF68',
            'ShieldSimpleScalar_43_417C36C54DA2550A4CABC7B26A5E24A8',
            'ArmorSimpleScalar_44_BCAAA445479831C25B0D55AF294A15D6',
            ]:
        mod.table_hotfix(Mod.PATCH, '',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                mayhem_level,
                col_name,
                scale_value)
    mod.newline()

mod.close()
