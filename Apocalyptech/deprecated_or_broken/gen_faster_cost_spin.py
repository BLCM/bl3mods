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
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('faster_cost_spin.txt',
        'Faster Cost Spin',
        'Apocalyptech',
        [
            "Attempt to speed up the cost spinner (inventory, etc)",
            "",
            "The hotfixes active in here *do* technically change the values they're going",
            "after, but the card doesn't change.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Objects:
# /Game/UI/CurrencyWidget/BPWidget_CurrencyWidget
# /Game/UI/ItemCard/BPWidget_GFxItemCard

# Does not seem to update attr
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/UI/CurrencyWidget/BPWidget_CurrencyWidget.Default__BPWidget_CurrencyWidget_C',
#        'DelayAfterResurrect',
#        0.1)

# Does not seem to update attr
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/UI/CurrencyWidget/BPWidget_CurrencyWidget.Default__BPWidget_CurrencyWidget_C',
#        'CostSpinTimeOnResurrect',
#        0.1)

# Does not actually change the value
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/UI/CurrencyWidget/BPWidget_CurrencyWidget.Default__BPWidget_CurrencyWidget_C',
#        'MaxTimeUntilStopAdvancing',
#        0.1)

# Does change the value, but doesn't seem to affect the card
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/UI/CurrencyWidget/BPWidget_CurrencyWidget.Default__BPWidget_CurrencyWidget_C',
        'CostSpinTime',
        0.1)

# This one does *not* change the value; I suspect it's dynamically set on creation with
# blueprint stuff.
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/UI/CurrencyWidget/BPWidget_CurrencyWidget.Default__BPWidget_CurrencyWidget_C',
#        'CostSpinTimeOnResurrect',
#        0.1)

# Also changes the value properly, but doesn't seem to affect the card
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/UI/CurrencyWidget/BPWidget_CurrencyWidget.Default__BPWidget_CurrencyWidget_C',
        'PauseOnNewValueTime',
        0.1)

# Also changes the value properly, but doesn't seem to affect the card
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/UI/ItemCard/BPWidget_GFxItemCard.Default__BPWidget_GFxItemCard_C',
        'ItemCardObject.CostSpinTime',
        0.05)

# Just a laff -- wonder if I can make Maliwan elemental notifications spastic
# Does *not* actually update the var on the object, alas.
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/UI/ItemCard/BPWidget_GFxItemCard.Default__BPWidget_GFxItemCard_C',
#        'ItemCardObject.UpdateElementalInfoTime',
#        0.1)

# Huge stretch here, have never actually seen this before
# (does not actually update any values)
#mod.reg_hotfix(Mod.PATCH, '',
#        'GFxCurrencyCounterClip',
#        'CostSpinTime',
#        0.01)

# An even bigger stretch here
# (does not actually update any values)
#mod.reg_hotfix(Mod.PATCH, '',
#        'GFxCurrencyCounterClip.Default__GFxCurrencyCounterClip_C',
#        'CostSpinTime',
#        0.01)

mod.close()

