#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import collections
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('heart_of_gold_better_gifts.txt',
        'Heart of Gold: Better Gifts',
        [
            "I always felt that the gifts you get from Joy in the mission 'Heart",
            "of Gold' are a bit pathetic.  Not that you need the resources or",
            "anything, but IMO it'd be nicer if it turned out that Joy was sitting",
            "on a small fortune all this time.",
            "",
            "Buffing this up to *actually* impressive levels isn't really possible",
            "but we can at least bump up the quantity and throw in Eridium as well,",
            "which may make it seem more impressive.",
        ])

# Improve the pool
mod.comment('Improve Gift Pool')
money_obj = '/Game/Pickups/Money/DA_InventoryBalance_Currency_MoneyTripleStack'
eridium_obj = '/Game/Pickups/Eridium/InvBal_Eridium_Stack'
mod.reg_hotfix(Mod.LEVEL, 'Trashtown_P',
        '/Dandelion/Missions/Side/HeartOfGold/ItemPool_Money_HeartOfGold',
        'BalancedItems',
        """(
            (
                InventoryBalanceData={},
                ResolvedInventoryBalanceData={},
                Weight=(BaseValueConstant=1)
            ),
            (
                InventoryBalanceData={},
                ResolvedInventoryBalanceData={},
                Weight=(BaseValueConstant=0.5)
            )
        )""".format(
            money_obj, Mod.get_full_cond(money_obj, 'InventoryBalanceData'),
            eridium_obj, Mod.get_full_cond(eridium_obj, 'InventoryBalanceData'),
            ))
mod.newline()

# Default value: 10.
mod.comment('Increase quantity')
mod.reg_hotfix(Mod.LEVEL, 'Trashtown_P',
        '/Dandelion/Missions/Side/HeartOfGold/ItemPool_Money_HeartOfGold',
        'Quantity.BaseValueConstant',
        40)
mod.newline()

mod.close()
