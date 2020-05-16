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

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, Pool

mod = Mod('deluxe_badass_combustor_unlock.txt',
        'Deluxe Badass Combustor Unlock',
        [
            "Allows the Deluxe Badass Combustor shield to function at any level",
            "of the game, instead of until level 10.",
        ])

# This looks *so simple* from the JWP serialization, but I'm still not great at modifying
# BlueprintGeneratedClasses.  The BGC exists out on the main menu, but I couldn't even figure
# out how to get data out of it with a `getall`, so I'd have to hop in-game to find out if
# the in-level object got the things applied or not (which it didn't, of course).  For the
# record, a `getall Condition_InventoryAbility_PlayerLevelReq_C` in-level will spit out
# a level-prefixed object which looks like:
#
#     ...BP_ShieldMod_C_1.InventoryAbilityManagerComponent.Ability_ShieldAug_XPLoot_C_0.Condition_Condition_ActorLevelRequirement
#
# And that object has `Level` and `Method` as you'd hope.  Anyway, giving up on this for now
# since I'd probably never use the shield anyway, so it's stopped seeming to be worth the
# effort.

if True:
    mod.reg_hotfix(Mod.PATCH, '',
            #'/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Ability_ShieldAug_XPLoot.Default__Condition_InventoryAbility_PlayerLevelReq_C',
            #'/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Ability_ShieldAug_XPLoot.Default__Ability_ShieldAug_XPLoot_C',
            #'/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Ability_ShieldAug_XPLoot.Condition_Condition_ActorLevelRequirement',
            #'/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Ability_ShieldAug_XPLoot.Condition_InventoryAbility_PlayerLevelReq_C',
            #'Level',

            '/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Ability_ShieldAug_XPLoot.Default__Ability_ShieldAug_XPLoot_C',
            'Condition.Object..Level',

            0)

    mod.reg_hotfix(Mod.PATCH, '',
            #'/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Ability_ShieldAug_XPLoot.Default__Condition_InventoryAbility_PlayerLevelReq_C',
            #'/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Ability_ShieldAug_XPLoot.Default__Ability_ShieldAug_XPLoot_C',
            #'/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Ability_ShieldAug_XPLoot.Condition_Condition_ActorLevelRequirement',
            #'/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Ability_ShieldAug_XPLoot.Condition_InventoryAbility_PlayerLevelReq_C',
            #'Method',

            '/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Ability_ShieldAug_XPLoot.Default__Ability_ShieldAug_XPLoot_C',
            'Condition.Object..Method',

            'GE')

if False:
    # This here is just laughable, I didn't have any faith that it'd actually do the right thing, but figured
    # I may as well take the longshot.  In addition to all the other assumptions I was making, I highly doubt
    # that the `Ability.Object` jump would work.
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Parts/Part_Shield_Aug_XPLootBooster.Part_Shield_Aug_XPLootBooster',
            'AspectList.AspectList[1].Object..Abilities.Abilities[0].Ability.Object..Condition.Object..Level',
            0)

mod.close()
