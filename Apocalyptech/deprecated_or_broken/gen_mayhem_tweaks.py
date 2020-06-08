#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF

# Just a tiny test to make sure it was possible, no real plans to actually
# do anything with this.
#
# Observations:
#  - The UI won't show more than five modifiers
#  - Even at five, the display is a bit wonky
#  - Not even actually sure if the 6+th ones are *actually* active?

mod = Mod('mayhem_tweaks.txt',
        'Mayhem Tweaks',
        'Apocalyptech',
        [
        ],
        lic=Mod.CC_BY_SA_40,
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
