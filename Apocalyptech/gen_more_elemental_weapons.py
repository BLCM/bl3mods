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

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

weight_no_element = 1.5
weight_element = 0.5
total = weight_no_element+(weight_element*5)
chance_element = round((weight_element*5)/total*100)

mod = Mod('more_elemental_weapons.txt',
        'More Elemental Weapons',
        [
            "Increases the chances of having elements spawn on all weapons which support",
            "elements.  The stock chances of getting an element (for weapons which can",
            "spawn in all elements, anyway) are:",
            "",
            "   Common: 9%",
            "   Uncommon: 14%",
            "   Rare: 23%",
            "   Very Rare: 41%",
            "",
            "This mod increases the chance to {}%, across the board.".format(chance_element),
        ])

for row in [
        'Common',
        'UnCommon',
        'Rare',
        'VeryRare',
        ]:
    for col, value in [
            ('No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1', weight_no_element),
            ('Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54', weight_element),
            ('Shock_8_684654654B332D94359F79BEB2DB90AA', weight_element),
            ('Corrosive_9_FCB69C7740260C055C8D32B7E96603D1', weight_element),
            ('Cryo_10_FE2073AF44E3E00A723784B1D44C2D50', weight_element),
            ('Radiation_13_2500317646FAD2F4916D158835B29E83', weight_element),
            ]:
        mod.table_hotfix(Mod.PATCH, '',
                '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
                row,
                col,
                value)

mod.close()
