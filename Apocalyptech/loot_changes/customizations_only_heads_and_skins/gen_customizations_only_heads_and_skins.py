#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2022 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF

mod = Mod('customizations_only_heads_and_skins.bl3hotfix',
        'Customizations: Only Heads and Skins',
        'Apocalyptech',
        [
            "Only drop heads+skins from the global customization drop pool.",
            "With recent shenanigans I've completed my collections of all",
            "other customization types, but I think I'm only full up on",
            "heads+skins for Amara, and possibly FL4K.  So, gonna cut the",
            "other pools out of here.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.1',
        cats='enemy-drops',
        )

for idx in [2, 3, 4, 5]:
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/Loot/ItemPools/ItemPool_SkinsAndMisc',
            f'BalancedItems[{idx}].Weight.BaseValueConstant',
            0)

mod.close()
