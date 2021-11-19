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
        v='1.1.0',
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

hf_type = Mod.LEVEL
hf_target = 'MatchAll'

# This *does* have to be a CHAR hotfix or it doesn't work all the time.  The Black Markets
# Everywhere mod has to use CHAR, too.  Yay?
mod.comment('Update main itempool')
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
        '/Game/PatchDLC/Ixora2/Loot/VendingMachines/DA_ItemPool_BlackMarket',
        'BalancedItems',
        str(pool))
mod.newline()

# With the Vault Card 3 release, Gearbox patched this machine to no longer rely on hotfixes to
# change its weekly loot, and it did so via some newish attributes inside ExpansionData_VaultCard3.
# Clear those out so that it doesn't happen anymore.  These can be LEVEL and it seems to
# work just fine.
mod.comment('Prevent weekly ItemPool overwrites')
expansion_obj = '/Game/PatchDLC/VaultCard3/Data/ExpansionData_VaultCard3'
mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
        expansion_obj,
        'RandomDateBasedItemPools',
        '()')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
        expansion_obj,
        'ItemPoolToReplaceWithRandomItemPool',
        'None')
mod.newline()

mod.close()

# Original mod idea; was gonna be a collection of mods which let you choose
# between what week's rewards should be active, or a combination of *all*
# weeks, or simply expanding it to the world drops.  In the end, I realized
# that there's no way I'd want to keep maintaining this thing every week,
# and I wouldn't want all that junk polluting the ModCabinet anyway, so
# whatever, get rid of it.  I'm keeping it here in case I ever change my
# mind, though.
if False:
    contents = [
            ('On-Disk Data', 'on_disk', [
                '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Balance/Balance_SG_JAK_Hellwalker',
                '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman',
                '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Nemesis/Balance/Balance_DAL_PS_Nemesis',
                ]),
            ('Week 1: April 8, 2021', 'week_001', [
                '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth',
                '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/BOTD/Balance/Balance_DAL_AR_BOTD',
                '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/RedLiner/Balance/Balance_SG_Torgue_RedLine',
                ]),
            ('Week 2: April 15, 2021', 'week_002', [
                '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Balance/Balance_VLA_SR_Lyuda',
                '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Kaos/Balance/Balance_DAL_AR_Kaos',
                '/Game/Gear/GrenadeMods/_Design/_Unique/Seeker/Balance/InvBalD_GM_Seeker',
                ]),
            ('Week 3: April 22, 2021', 'week_003', [
                '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/_Bangarang/Balance/Balance_PS_TED_Bangerang',
                '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Bitch/Balance/Balance_SM_HYP_Bitch',
                '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Balance/Balance_AR_VLA_Faisor',
                ]),
            ('Week 4: April 29, 2021', 'week_004', [
                '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa',
                '/Game/Gear/Shields/_Design/_Uniques/BlackHole/Balance/InvBalD_Shield_LGD_BlackHole',
                ]),
            ('Week 5: May 6, 2021', 'week_005', [
                '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle',
                '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Balance/Balance_SG_HYP_ConferenceCall',
                '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc',
                ]),
            # Hardcoded special case here
            ('World Drop Legendaries', 'world_drops', None),
            ]
    all_historical = []
    for _, _, balances in contents:
        if balances is not None:
            all_historical.extend(balances)
    contents.append(('Combined Historical Pools (all weeks)', 'combined', all_historical))

    for label, filename, balances in contents:

        mod = Mod(f'customizable_black_market_{filename}.bl3hotfix',
                f'Customizable Black Market: {label}',
                'Apocalyptech',
                [
                ],
                lic=Mod.CC_BY_SA_40,
                v='1.0.0',
                cats='gear-general, gear-artifact',
                )

        pool = ItemPool('/Game/PatchDLC/Ixora2/Loot/VendingMachines/DA_ItemPool_BlackMarket')
        if balances is None:
            # We're basically recreating a BL2/TPS-style "GunsAndGear" ItemPool here, which isn't something that's
            # really found anywhere in BL3.  So, I've chosen these relative weights here from the BL2 version, and
            # modified it slightly.  The stock BL2 weights are:
            #   Guns: 100
            #   Shields: 45
            #   Grenades: 35
            #   COMs: 25
            #   Artifacts: 20
            # I'm scaling the non-guns to 80% so that you'll get guns half the time (total weight of 200)
            pool.add_pool('/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary', BVC(bvc=1, bvs=1)),
            pool.add_pool('/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary', BVC(bvc=1, bvs=.36)),
            pool.add_pool('/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary', BVC(bvc=1, bvs=.28)),
            pool.add_pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster_05_Legendary', BVC(
                bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Beastmaster', bvs=.2)),
            pool.add_pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner_05_Legendary', BVC(
                bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Gunner', bvs=.2)),
            pool.add_pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative_05_Legendary', BVC(
                bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Operative', bvs=.2)),
            pool.add_pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Siren_05_Legendary', BVC(
                bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Siren', bvs=.2)),
            pool.add_pool('/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_05_Legendary', BVC(bvc=1, bvs=.16)),
        else:
            for balance in balances:
                pool.add_balance(balance)

        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/PatchDLC/Ixora2/Loot/VendingMachines/DA_ItemPool_BlackMarket',
                'BalancedItems',
                str(pool))

        mod.close()
