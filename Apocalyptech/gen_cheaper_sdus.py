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

start_price = 500
increment = 2
default_levels = 8
max_price = 1024000

mod = Mod('cheaper_sdus.txt',
        'SDUs are much cheaper',
        [])

for table_data in [
        'Table_SDU_AssaultRifle',
        ('Table_SDU_Backpack', 13),
        ('Table_SDU_Bank', 23),
        'Table_SDU_Grenade',
        ('Table_SDU_Heavy', 13),
        'Table_SDU_LostLoot',
        'Table_SDU_Pistol',
        'Table_SDU_Shotgun',
        'Table_SDU_SMG',
        ('Table_SDU_SniperRifle', 13),
        ]:
    if type(table_data) == tuple:
        (table, levels) = table_data
    else:
        table = table_data
        levels = default_levels
    price = start_price
    for level in range(levels):
        mod.table_hotfix(Mod.PATCH, '',
                '/Game/Pickups/SDU/{}.{}'.format(table, table),
                'Lv{}'.format(level+1),
                'SDUPrice',
                price)
        if price < max_price:
            price = int(price*increment)

mod.close()
