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
from bl3hotfixmod.bl3hotfixmod import Mod, ItemPool, BVC

mod = Mod('black_market_world_drops.bl3hotfix',
        'Black Market World Drops',
        'Apocalyptech',
        [
            "Sets the Black Market vending machines to use the world-drop Legendary",
            "pools, instead of the three items set by Gearbox.  More or less",
            "intended to be used by my Expanded Legendary Pools mod, to provide the",
            "most variety in the machines.  The machines will contain weapons,",
            "shields, grenade mods, COMs, and relics.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.1.1',
        cats='vendor',
        )

# We're basically recreating a BL2/TPS-style "GunsAndGear" ItemPool here, which isn't something that's
# really found anywhere in BL3.  So, I've chosen these relative weights here from the BL2 version, and
# modified it slightly.  The stock BL2 weights are:
#   Guns: 100
#   Shields: 45
#   Grenades: 35
#   COMs: 25
#   Artifacts: 20
# I'm scaling the non-guns to 60% so that you'll get guns for about 2/3 of the time.
non_gun_scale = .6
pool = ItemPool('/Game/PatchDLC/Ixora2/Loot/VendingMachines/DA_ItemPool_BlackMarket')
pool.add_pool('/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary', BVC(bvc=1, bvs=1)),
pool.add_pool('/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary', BVC(bvc=1, bvs=.45*non_gun_scale)),
pool.add_pool('/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary', BVC(bvc=1, bvs=.35*non_gun_scale)),
pool.add_pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster_05_Legendary', BVC(
    bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Beastmaster', bvs=.25*non_gun_scale)),
pool.add_pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner_05_Legendary', BVC(
    bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Gunner', bvs=.25*non_gun_scale)),
pool.add_pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative_05_Legendary', BVC(
    bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Operative', bvs=.25*non_gun_scale)),
pool.add_pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Siren_05_Legendary', BVC(
    bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Siren', bvs=.25*non_gun_scale)),
pool.add_pool('/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_05_Legendary', BVC(bvc=1, bvs=.20*non_gun_scale)),

# We could theoretically be more clever about this and only do the "full" set on a single week's
# pool, and have BalancedItems on the others just point to that one week.  Just in case there's
# something which causes unused weeks' objects to be garbage collected, though, I'll continue
# to use the full BalancedItems on each.  (I don't think it's *likely* to be GC'd, since they're
# still referenced by `ExpansionData_VaultCard3`, but whatever.)
pool_str = str(pool)
for num in range(1, 53):
    mod.reg_hotfix(Mod.PATCH, '',
            f'/Game/PatchDLC/Ixora2/Loot/VendingMachines/WeeklyPools/ItemPool_BMV_Week{num}',
            'BalancedItems',
            pool_str)

mod.close()

###
### What follows is my original "updated" attempt after the 2021-11-18 patch, which introduced
### the code-based Black Market rotation.  I'd basically gotten a false positive with this,
### because it *does* start working properly if you enter the game, then quit all the way back
### out to the title screen, and then hop back in-game again.  But it does *not* work on that
### very first load, so it's hardly ideal.
###

# This *does* have to be a CHAR hotfix or it doesn't work all the time.  The Black Markets
# Everywhere mod has to use CHAR, too.  Yay?
#mod.comment('Update main itempool')
#mod.reg_hotfix(Mod.CHAR, 'MatchAll',
#        '/Game/PatchDLC/Ixora2/Loot/VendingMachines/DA_ItemPool_BlackMarket',
#        'BalancedItems',
#        str(pool))
#mod.newline()

# With the Vault Card 3 release, Gearbox patched this machine to no longer rely on hotfixes to
# change its weekly loot, and it did so via some newish attributes inside ExpansionData_VaultCard3.
# Clear those out so that it doesn't happen anymore.  These can be LEVEL and it seems to
# work just fine.
#mod.comment('Prevent weekly ItemPool overwrites')
#expansion_obj = '/Game/PatchDLC/VaultCard3/Data/ExpansionData_VaultCard3'
#mod.reg_hotfix(Mod.EARLYLEVEL, 'MatchAll',
#        expansion_obj,
#        'RandomDateBasedItemPools',
#        '()',
#        notify=True)
#mod.reg_hotfix(Mod.EARLYLEVEL, 'MatchAll',
#        expansion_obj,
#        'ItemPoolToReplaceWithRandomItemPool',
#        'None',
#        notify=True)
#mod.newline()

