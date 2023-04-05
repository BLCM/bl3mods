#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2021 Christopher J. Kucera
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

start_price = 500
increment = 2
max_price = 1024000

mod = Mod('cheaper_sdus.bl3hotfix',
        'Cheaper SDUs',
        'Apocalyptech',
        [
            "Makes the purchaseable SDUs in the game significantly cheaper.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.2.0',
        cats='cheat, economy',
        )

# This is stupid, but so is this updated object.
row_hardcodes = {
        'Table_SDU_Bank': {
            23: 'NewRow',
            24: 'NewRow_0',
            25: 'NewRow_1',
            26: 'NewRow_2',
            27: 'NewRow_3',
            },
        }

for table, levels in [
        ('Table_SDU_AssaultRifle', 10),
        ('Table_SDU_Backpack', 13),
        ('Table_SDU_Bank', 28),
        ('Table_SDU_Grenade', 10),
        ('Table_SDU_Heavy', 13),
        ('Table_SDU_LostLoot', 10),
        ('Table_SDU_Pistol', 10),
        ('Table_SDU_Shotgun', 10),
        ('Table_SDU_SMG', 10),
        ('Table_SDU_SniperRifle', 13),
        ]:
    mod.comment(table)
    price = start_price
    for level in range(levels):
        if table in row_hardcodes and level in row_hardcodes[table]:
            row_name = row_hardcodes[table][level]
        else:
            row_name = 'Lv{}'.format(level+1)
        mod.table_hotfix(Mod.PATCH, '',
                '/Game/Pickups/SDU/{}'.format(table),
                row_name,
                'SDUPrice',
                price)
        if price < max_price:
            price = int(price*increment)
    mod.newline()

mod.close()
