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

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('remove_mayhem_gear_bonuses.bl3hotfix',
        'Remove Mayhem gear Bonuses',
        'Apocalyptech',
        [
            "Removes the bonuses applied by Mayhem parts on your gear, so they",
            "function just like gear without the Mayhem part applied.  The gear",
            "*will* continue to display its Mayhem part on the item card, but",
            "it won't have any effect so long as this mod is active."
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='mayhem, gear-general',
        )

for mayhem_level in range(1, 11):
    mod.comment('Mayhem {}'.format(mayhem_level))
    obj_name = '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_{:02d}'.format(mayhem_level)
    mod.reg_hotfix(Mod.PATCH, '',
            obj_name,
            'MayhemLevel',
            0)
    mod.reg_hotfix(Mod.PATCH, '',
            obj_name,
            'MonetaryValueModifier.BaseValueConstant',
            1)
    mod.reg_hotfix(Mod.PATCH, '',
            obj_name,
            'InventoryScoreModifier.BaseValueConstant',
            0)
    mod.newline()

mod.close()
