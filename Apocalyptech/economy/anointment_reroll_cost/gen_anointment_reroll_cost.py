#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

for value in [
        0,
        1,
        10,
        25,
        50,
        100,
        150,
        200,
        ]:

    if value == 0:
        label = 'Free'
        filename_extra = 'free'
        cost_text = 'be free'
    else:
        label = value
        filename_extra = value
        cost_text = f'cost {value} Eridium'

    mod = Mod(f'anointment_reroll_cost_{filename_extra}.bl3hotfix',
            f'Anointment Re-Roll Cost: {label}',
            'Apocalyptech',
            [
                "Sets the Anointment Re-Roll Cost (at the station near Earl's) to",
                f"{cost_text}, instead of the usual 250 Eridium.",
                "",
                "All *real* credit for this goes to Nexus-Mistress, who found the",
                "proper attribute to use after I'd failed to do so myself!"
            ],
            lic=Mod.CC_BY_SA_40,
            v='1.0.0',
            cats='cheat, economy',
            )

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/_Shared/_Design/InventoryGlobals',
            'PartReRollCostFormula.BaseValueConstant',
            value)

    mod.close()

