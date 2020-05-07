#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('cheaper_slots.txt',
        'Cheaper Slot Machines',
        [
        ])

levels_money = [
        'Sanctuary3_P',
        'AtlasHQ_P',
        'OrbitalPlatform_P',
        'Mansion_P',
        'CasinoIntro_P',
        'Core_P',
        'Bar_P',
        ]

levels_eridium = [
        'Sanctuary3_P',
        'Bar_P',
        ]

mod.comment('Money-based machines')
for level in levels_money:
    mod.reg_hotfix(Mod.LEVEL, level,
            '/Game/UI/InteractionPrompt/UIData_PlaySlots',
            'Cost.BaseValueScale',
            0.2)
mod.newline()

mod.comment('Eridium-based machines')
for level in levels_eridium:
    mod.reg_hotfix(Mod.LEVEL, level,
            '/Game/UI/InteractionPrompt/UIData_PlaySlotsEridium',
            'Cost.BaseValueScale',
            0.2)
mod.newline()

mod.close()

