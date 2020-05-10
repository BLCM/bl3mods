#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('mayhem_level_cheats.txt',
        'Mayhem 2.0: Mayhem Level Cheats',
        [
            "Makes all Mayhem levels look identical in terms of difficulty-related",
            "scaling: 200% health/shield/armor scaling for enemies, and 2x Easy +",
            "1x Hard modifiers.",
            "",
            "Note that this and mayhem2_decreased_enemy_scaling both touch the same",
            "vars for enemy scaling, so they'll conflict (whichever is used 'last'",
            "will take precedence).",
        ])

enemy_scale = 2
modifiers = '({})'.format(','.join([Mod.get_full_cond(m, 'MayhemModifierSlotDataAsset') for m in [
    '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Easy',
    '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Easy',
    '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Hard',
    ]]))

for mayhem_level_minus_one in range(10):
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
                enemy_scale)
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Mayhem2/OverrideModSet_Mayhem2',
            'PerLevelOverrides.PerLevelOverrides[{}].RandomModifierSlotsOverride'.format(mayhem_level_minus_one),
            modifiers)
    mod.newline()

mod.close()
