#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

start_price = 500
increment = 2
default_levels = 8
max_price = 1024000

mod = Mod('cheaper_sdus.txt',
        'SDUs are much cheaper',
        [],
        'SDU',
        )

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
