#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import collections
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('sisterly_love_more_money.txt',
        'Sisterly Love: More Money',
        [
            "I always felt that the malfunctioning-slot-machine money drop in",
            "the DLC2 mission Sisterly Love was pretty anemic and unimpressive.",
            "This mod buffs it up slightly, though it turns out there's not a",
            "*lot* that we can really do with it.",
        ])

# Default is a single stack; I couldn't find anything bigger than the triple, which is
# still pretty meh.
mod.comment('Use "biggest" money drop')
to_obj_name = '/Game/Pickups/Money/DA_InventoryBalance_Currency_MoneyTripleStack'
mod.reg_hotfix(Mod.LEVEL, 'Strip_P',
        '/Dandelion/Missions/Side/BrotherlyLove/ItemPool_Money_BrotherlyLove',
        'BalancedItems.BalancedItems[0]',
        """(
            InventoryBalanceData={},
            ResolvedInventoryBalanceData={},
            Weight=(BaseValueConstant=1)
        )""".format(to_obj_name, Mod.get_full_cond(to_obj_name, 'InventoryBalanceData')))
mod.newline()

# Default value: 20.  Going to 150 makes a noticeable (though extremely slight) little
# freeze while they're populating, 200 is even more noticeable.  I'd tried 1000 initially
# and thought that I'd frozen the game permanently before it recovered.  So: eh.  This
# doesn't really feel that much different from stock.
mod.comment('Increase initial money drop count')
mod.reg_hotfix(Mod.LEVEL, 'Strip_P',
        '/Dandelion/Missions/Side/BrotherlyLove/ItemPool_Money_BrotherlyLove',
        'Quantity.BaseValueConstant',
        100)
mod.newline()

mod.close()
