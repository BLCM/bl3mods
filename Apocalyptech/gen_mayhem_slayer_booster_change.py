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

from bl3hotfixmod.bl3hotfixmod import Mod, ItemPool, BVC

mod = Mod('mayhem_slayer_booster_change.txt',
        'Mayhem 2.0: Change Slayer Boosters',
        'Apocalyptech',
        [
            "The Mayhem 2.0 Easy modifier 'Slayer' drops shield boosters by default, which",
            "can interfere with roid-shield-based melee builds.  This changes those booster",
            "drops to be either health charges or damage-reduction charges instead.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Boosters to switch to
new_boosters = [
        '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Charges/HealthCharge/HealthChargePickup/InvBal_HealthCharge',
        '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Charges/FortifyCharge/FortifyCharge_Pickup/InvBal_FortifyCharge',
        # Not gonna do the damage one, since this is probably gonna be used by melee-focused builds.
        #'/Game/Gear/Shields/_Design/PartSets/Part_Augment/Charges/PowerCharge/PowerCharge_Pickup/InvBal_PowerCharge',
        ]
booster_weight = 1/len(new_boosters)

# Set up the pool
pool = ItemPool('/Game/PatchDLC/Mayhem2/Abilities/Enemy/FinishThem/ItemPool_Mayhem2_FinishThem')
pool.add_balance('/Game/Pickups/Health/DA_InventoryBalance_Health.DA_InventoryBalance_Health')
for booster in new_boosters:
    pool.add_balance(booster, weight=BVC(bvc=booster_weight))

# Write the hotfix
mod.reg_hotfix(Mod.EARLYLEVEL, 'MatchAll',
        pool.pool_name,
        'BalancedItems',
        str(pool))

mod.close()

