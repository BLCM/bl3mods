#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

start_price = 500
increment = 2
levels = 8

mod = Mod('cheaper_sdus.txt',
        'SDUs are much cheaper',
        [],
        'SDU',
        )

for table in [
        'Table_SDU_AssaultRifle',
        'Table_SDU_Backpack',
        'Table_SDU_Bank',
        'Table_SDU_Grenade',
        'Table_SDU_Heavy',
        'Table_SDU_LostLoot',
        'Table_SDU_Pistol',
        'Table_SDU_Shotgun',
        'Table_SDU_SMG',
        'Table_SDU_SniperRifle',
        ]:
    price = start_price
    for level in range(levels):
        mod.table_hotfix(Mod.PATCH, '',
                '/Game/Pickups/SDU/{}.{}'.format(table, table),
                'Lv{}'.format(level+1),
                'SDUPrice',
                price)
        price = int(price*increment)

mod.close()
