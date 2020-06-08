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

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('mayhem_no_drop_scaling.txt',
        'Mayhem 2.0: No Extra Drop Scaling',
        'Apocalyptech',
        [
            "Mayhem 2.0 increases the drop rates pretty significantly, and when",
            "combined with my Better Loot mod, it's totally absurd.  I'm happy",
            "with my Better Loot drop weighting, so this should de-scale the",
            "loot so that Mayhem 2.0 modes are no different than in normal.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

# There's another column named LootQuality_56_03E220E0495C6B37CD6C7195F5EA289B which
# goes from 1 at M1, to 2 at M10.  No idea what that does, really, though it looks like
# it might only be referenced by a UI element.  So possibly nothing important...

for mayhem_level in range(1, 11):
    mod.comment('Mayhem {}'.format(mayhem_level))
    for col_name in [
            'DropWeightCommonScalar_21_59A2FB124E32B955768A7B9D93C25A99',
            'DropWeightUncommonScalar_25_809615334E7F0DB3B8712DAC221015C3',
            'DropWeightRareScalar_27_A09CF5314C51796896A83EA0806C7520',
            'DropWeightVeryRareScalar_29_F2CA570046CD50A7C514EDB0AE1BE591',
            'DropWeightLegendaryScalar_31_D9DA03C54065EA981BE218B11942C24E',
            ]:
        mod.table_hotfix(Mod.PATCH, '',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                mayhem_level,
                col_name,
                1)
    mod.newline()

mod.close()
