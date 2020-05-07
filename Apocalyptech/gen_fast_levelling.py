#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

# Default scales: PT1 - 10, PT2+ - 11
for (label, scale) in [
        ('Fast', 1000),
        ('Faster', 2500),
        ('Insane', 5000),
        ]:

    mod_filename = 'fast_levelling_{}.txt'.format(label.lower())

    mod = Mod(mod_filename,
            'Fast Levelling: {} Variant (very cheaty!)'.format(label),
            [
                "I wanted a way to quickly level a character up for testing purposes",
                "so that's what this mod provides.  Increases XP gains by {}x.".format(round(scale/10), 0),
            ])

    mod.comment('Base XP Scaling')

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/Balance/Experience/Att_BaseEnemyExperience.Att_BaseEnemyExperience:ValueResolver_PlayThroughDefinedAttributeValueResolver',
            'Value.PlaythroughOne.BaseValueConstant',
            scale)

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/Balance/Experience/Att_BaseEnemyExperience.Att_BaseEnemyExperience:ValueResolver_PlayThroughDefinedAttributeValueResolver',
            'Value.PlaythroughTwoAndBeyond.BaseValueConstant',
            scale)

    mod.newline()

    # Remove level-scaling differences
    mod.comment('Remove XP Scaling by level differences')
    for num in range(6):
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/GameData/Balance/ExperienceGlobals',
                'ExpScaleByLevelDifference.ExpScaleByLevelDifference[{}].HigherLevelEnemyExpScale'.format(num),
                1)
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/GameData/Balance/ExperienceGlobals',
                'ExpScaleByLevelDifference.ExpScaleByLevelDifference[{}].LowerLevelEnemyExpScale'.format(num),
                1)
    mod.newline()

    mod.close()
    print('Generated {}'.format(mod_filename))
