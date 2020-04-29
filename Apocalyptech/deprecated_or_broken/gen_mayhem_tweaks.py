#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, Pool

# Just a tiny test to make sure it was possible, no real plans to actually
# do anything with this.
#
# Observations:
#  - The UI won't show more than five modifiers
#  - Even at five, the display is a bit wonky
#  - Not even actually sure if the 6+th ones are *actually* active?

mod = Mod('mayhem_tweaks.txt',
        'Mayhem Tweaks',
        [
        ],
        'MayhemTweaks',
        )

EASY = '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_EAsy'
MED = '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Medium'
HARD = '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Hard'
VHARD = '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_VeryHard'

def patch_mayhem_level(level, mods):
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Mayhem2/OverrideModSet_Mayhem2',
            'PerLevelOverrides.PerLevelOverrides[{}].RandomModifierSlotsOverride'.format(level),
            '({})'.format(','.join(
                [Mod.get_full_cond(mod, 'MayhemModifierSlotDataAsset') for mod in mods]
                )))

patch_mayhem_level(0, [VHARD, VHARD, VHARD, VHARD])

mod.close()
