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

import collections
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, Balance

mod = Mod('hellwalker_to_purple_parts.txt',
        'Hellwalker -> "Stock" Purple-part Jakbobs Shotgun',
        'Apocalyptech',
        [
            "Replaces the Hellwalker balance/partset with the balance/partset from",
            "a regular purple-part Jakobs Shotgun.  Just a test to see if the",
            "NamingStrategy objects would still do their thing, really.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Add the parts
data = BL3Data()
bal = Balance.from_data(data, '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_04_VeryRare')
bal.set_balance_to('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Balance/Balance_SG_JAK_Hellwalker', data)
bal.hotfix_full(mod)

mod.close()
