#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2021 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

# TODO: Should probably find out if the DLC emotes are actually guaranteed or not, and
# add them in here if they aren't.

# Leaving out the Final Form cosmetics, which are all just given to you automatically if
# you have the required DLCs.  The balances, for reference:
#    /Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin51/CustomSkin_Beastmaster_51.InvBal_CustomSkin_Beastmaster_51
#    /Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin51/CustomSkin_Gunner_51.InvBal_CustomSkin_Gunner_51
#    /Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin51/CustomSkin_Operative_51.InvBal_CustomSkin_Operative_51
#    /Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin51/CustomSkin_Siren_51.InvBal_CustomSkin_Siren_51
#    /Game/PatchDLC/Ixora/PlayerCharacters/Beastmaster/Heads/DA_BMHead39.InvBal_DA_BMHead39
#    /Game/PatchDLC/Ixora/PlayerCharacters/Gunner/Heads/DA_GNRHead39.InvBal_DA_GNRHead39
#    /Game/PatchDLC/Ixora/PlayerCharacters/Operative/Heads/DA_OPHead39.InvBal_DA_OPHead39
#    /Game/PatchDLC/Ixora/PlayerCharacters/SirenBrawler/Heads/DA_SRNHead39.InvBal_DA_SRNHead39

def set_pool(mod, pool_to_set, balances, char=None):
    parts = []
    for bal in balances:
        if type(bal) is tuple:
            (bal1, bal2) = bal
        else:
            bal1 = bal
            bal2 = bal
        part = '(InventoryBalanceData={},ResolvedInventoryBalanceData=InventoryBalanceData\'"{}"\',Weight=(BaseValueConstant=1))'.format(
                bal1,
                bal2,
                )
        parts.append(part)
    if char is None:
        hf_subtype = Mod.PATCH
        hf_pkg = ''
    else:
        hf_subtype = Mod.CHAR
        hf_pkg = char
    mod.reg_hotfix(hf_subtype, hf_pkg,
            pool_to_set,
            'BalancedItems',
            '({})'.format(','.join(parts)))

for (label, filename_addition, drop_mission, drop_earl, drop_vaultcard, extra_texts) in [
        ('All Customizations', 'all',
            True, True, True,
            ["literally all \"useful\" customizations will world-drop."]),
        ('All but Mission Rewards', 'no_mission_rewards',
            False, True, True,
            ["all customizations except for mission rewards",
            "will world-drop (non-main-game mission rewards *are* included)."]),
        ('All but Mission Rewards and Earl\'s Shop', 'no_mission_rewards_or_earl',
            False, False, True,
            ["all customizations except for mission rewards",
            "and those available in Earl's shop will world-drop (non-main-game mission",
            "rewards *are* included)."]),
        ('All but Mission Rewards, Earl\'s Shop, and Vault Cards', 'no_mission_rewards_earl_or_vaultcard',
            False, False, False,
            ["all customizations except for mission rewards, Vault Card rewards,",
            "and those available in Earl's shop will world-drop (non-main-game mission",
            "rewards *are* included)."]),
        ]:

    filename_full = 'expanded_customization_pools_{}.bl3hotfix'.format(filename_addition)

    full_desc = [
        "The global drop pools for the various customization types in BL3 excludes various",
        "customizations, such as SHiFT rewards, Twitch streamer rewards, or even just some",
        "which appear to have no availability at all.  This mod adds all those in to the",
        "global drop pools, so you'll be able to find them just through playing the game.",
        "",
        "In this version of the mod, {}".format(extra_texts[0]),
        ]
    full_desc.extend(extra_texts[1:])
    full_desc.extend(["",
        "This mod *does* leave out the customizations that you automatically get from",
        "preorders or deluxe editions and the like, since those drops will never be",
        "useful to anyone.",
        "",
        "The mod also increases the global drop rate for customizations, to offset the",
        "increased pool sizes, flattens the pool probabilities so that all customizations",
        "in their pools will drop equally, and skews the pool probabilities so that each",
        "type of customization is weighted according to how many items are in the pool.",
        "(In other words: each customization in the pools should have an equal chance of",
        "dropping.)  This does assume you're using my No Wasted Gear mod, and playing in",
        "single player, in terms of head/skin drops.",
        "",
        "Slot machine rewards are unaffected!",
        ])

    mod = Mod(filename_full,
            'Expanded Customization Pools: {}'.format(label),
            'Apocalyptech',
            full_desc,
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.5.1',
            cats='loot-system, enemy-drops',
            )

    # Cosmetics at 3%, same as Better Loot.
    mod.header('Increased Cosmetic chances')
    mod.reg_hotfix(Mod.CHAR, 'MatchAll',
            '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear',
            'ItemPools[9].PoolProbability',
            """(
                BaseValueConstant=0.030000,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.000000
            )""")

    mod.newline()

    # The pool has its Quantity set to /Game/GameData/Loot/ItemPools/Init_RandomLootCount_Normal,
    # which seems to sometimes dip below 1, and cause the pool to not produce anything.  It's
    # weird.  Set it to 1 instead, so that every time the pool is chosen, it'll drop.
    mod.comment('Guarantee cosmetic drop when the pool is rolled (which weirdly isn\'t')
    mod.comment('the case, ordinarily.')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/Loot/ItemPools/ItemPool_SkinsAndMisc.ItemPool_SkinsAndMisc',
            'Quantity',
            """(
                BaseValueConstant=1,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1
            )""")
    mod.newline()

    # Now the pool expansions.
    mod.header('Customization Pool Expansions')

    # Skins/Heads first.
    for (dirname, shortname, abbrev) in [
            ('Beastmaster', 'Beastmaster', 'BM'),
            ('Gunner', 'Gunner', 'GNR'),
            ('Operative', 'Operative', 'OP'),
            ('SirenBrawler', 'Siren', 'SRN'),
            ]:

        ###
        ### Skins
        ###

        pool_name = f'/Game/Pickups/Customizations/_Design/ItemPools/Skins/ItemPool_Customizations_Skins_Loot_{shortname}.ItemPool_Customizations_Skins_Loot_{shortname}'
        balances = []
        # Base Game
        blacklist = {
                # These indexes plain ol' don't exist
                33, 38, 40,
                # 34 is retro pack, 35 is neon pack 
                34, 35,
                }
        if not drop_earl:
            blacklist |= {5, 7, 8, 9, 10, 11, 13, 14, 15, 18, 39}
        if not drop_mission:
            blacklist |= {29, 30, 31, 32, 36}
        for num in range(1, 44):
            if num not in blacklist:
                balances.append(f'/Game/PlayerCharacters/_Customizations/{dirname}/Skins/CustomSkin_{shortname}_{num}.InvBal_CustomSkin_{shortname}_{num}')
        # Bloody Harvest
        balances.append(f'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/{dirname}/Skins/CustomSkin_{shortname}_40.InvBal_CustomSkin_{shortname}_40')
        # Maliwan Takedown
        balances.append(f'/Game/PatchDLC/Raid1/PlayerCharacters/_Customizations/{shortname}/CustomSkin_{shortname}_45.InvBal_CustomSkin_{shortname}_45')
        # DLC1 - Dandelion
        for num in [44, 46]:
            balances.append(f'/Game/PatchDLC/Dandelion/PlayerCharacters/_Customizations/_Shared/CustomSkin_{shortname}_{num}.InvBal_CustomSkin_{shortname}_{num}')
        # Broken Hearts
        balances.append(f'/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_{shortname}_50.InvBal_CustomSkin_{shortname}_50')
        # DLC2 - Hibiscus - TODO: need to figure out if this should be in a blacklist
        balances.append(f'/Game/PatchDLC/Hibiscus/PlayerCharacters/_Customizations/_Shared/CustomSkin_{shortname}_DLC2_01.InvBal_CustomSkin_{shortname}_DLC2_01')
        # Citizen Science stuff (came long with DLC2)
        balances.append(f'/Game/PatchDLC/CitizenScience/PlayerCharacters/_Customizations/{dirname}/Skins/CustomSkin_{shortname}_CS.InvBal_CustomSkin_{shortname}_CS')
        # Revenge of the Cartels
        balances.append(f'/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/{dirname}/Skins/CustomSkin_{shortname}_47.InvBal_CustomSkin_{shortname}_47')
        # Guardian Takedown
        balances.append(f'/Game/PatchDLC/Takedown2/PlayerCharacters/_Customizations/PlayerSkins/CustomSkin_{shortname}_52.InvBal_CustomSkin_{shortname}_52')
        # DLC3 - Geranium - TODO: need to figure out if this should be in a blacklist
        balances.append(f'/Game/PatchDLC/Geranium/Customizations/PlayerSkin/CustomSkin_{shortname}_DLC3_1.InvBal_CustomSkin_{shortname}_DLC3_1')
        # DLC4 - Alisma - TODO: need to figure out if this should be in a blacklist
        # Note the stupidity with the names here...
        if shortname == 'Operative' or shortname == 'Siren':
            alisma_underscore = '__'
        else:
            alisma_underscore = '_'
        balances.append(f'/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/_Shared/CustomSkin_{shortname}_DLC4_01.InvBal_CustomSkin_{shortname}{alisma_underscore}DLC4_01')
        # Bloody Harvest 2020
        balances.append(f'/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/{dirname}/Skins/CustomSkin_{shortname}_63.InvBal_CustomSkin_{shortname}_63')
        # DLC5 - Ixora - TODO: need to figure out if this should be in a blacklist
        balances.append(f'/Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin62/CustomSkin_{shortname}_62.InvBal_CustomSkin_{shortname}_62')
        # Broken Hearts 2021 + Others
        balances.append(f'/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_{shortname}_65.InvBal_CustomSkin_{shortname}_65')
        balances.append(f'/Game/PatchDLC/EventVDay/TwitchDrops/PlayerCharacters/_Customizations/{shortname}/Skins/CustomSkin_{shortname}_61.InvBal_CustomSkin_{shortname}_61')
        # DLC6 - Ixora2 - TODO: need to figure out if this should be in a blacklist
        balances.append(f'/Game/PatchDLC/Ixora2/PlayerCharacters/_Shared/Skins/CustomSkin_{shortname}_66.InvBal_CustomSkin_{shortname}_66')
        # Vault Card #1
        if drop_vaultcard:
            balances.append(f'/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_{shortname}_67.InvBal_CustomSkin_{shortname}_67')
            balances.append(f'/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_{shortname}_68.InvBal_CustomSkin_{shortname}_68')
            balances.append(f'/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_{shortname}_69.InvBal_CustomSkin_{shortname}_69')
            balances.append(f'/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_{shortname}_70.InvBal_CustomSkin_{shortname}_70')
        # Cartels 2021
        balances.append(f'/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/{dirname}/Skins/CustomSkin_{shortname}_48.InvBal_CustomSkin_{shortname}_48')
        # Vault Card #2
        if drop_vaultcard:
            for num in [75, 76, 77, 78]:
                balances.append(f'/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_{shortname}_{num}.InvBal_CustomSkin_{shortname}_{num}')

        # Now output
        mod.comment(f'{shortname} Skins')
        set_pool(mod, pool_name, balances)
        mod.newline()
        # Technically this gets set multiple times, but whatever
        num_skins = len(balances)

        ###
        ### Heads
        ###

        pool_name = f'/Game/Pickups/Customizations/_Design/ItemPools/Heads/ItemPool_Customizations_Heads_Loot_{shortname}.ItemPool_Customizations_Heads_Loot_{shortname}'
        balances = []
        # Base Game
        blacklist = {
                # These indexes just plain ol' don't exist
                2, 3, 25
                }
        if not drop_earl:
            blacklist |= {7, 9, 10, 11, 12, 13, 14, 16, 18, 19}
        if not drop_mission:
            blacklist |= {5, 20, 21, 22, 23, 24}
        for num in range(1, 27):
            if num not in blacklist:
                balances.append(f'/Game/PlayerCharacters/_Customizations/{dirname}/Heads/CustomHead_{shortname}_{num}.InvBal_CustomHead_{shortname}_{num}')
        # Bloody Harvest, Ordering Bonuses, etc
        # 28 is retro pack, 29 is neon pack (26 doesn't exist)
        for num in [25, 27]:
            balances.append(f'/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/{dirname}/Heads/CustomHead_{shortname}_{num}.InvBal_CustomHead_{shortname}_{num}')
        # DLC1 - Dandelion
        balances.append(f'/Game/PatchDLC/Dandelion/PlayerCharacters/_Customizations/_Shared/CustomHead_{shortname}_30.InvBal_CustomHead_{shortname}_30')
        # Broken Hearts (actually a Twitch Prime reward, most likely)
        balances.append(f'/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomHead_{shortname}_Twitch.InvBal_CustomHead_{shortname}_Twitch')
        # DLC2 - Hibiscus - TODO: need to figure out if this should be in a blacklist
        balances.append(f'/Game/PatchDLC/Hibiscus/PlayerCharacters/_Customizations/_Shared/CustomHead_{shortname}_DLC2_01.InvBal_CustomHead_{shortname}_DLC2_01')
        # Citizen Science stuff (came long with DLC2)
        balances.append(f'/Game/PatchDLC/CitizenScience/PlayerCharacters/_Customizations/{dirname}/Heads/CustomHead_{shortname}_CS.InvBal_CustomHead_{shortname}_CS')
        # Revenge of the Cartels
        balances.append(f'/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/{dirname}/Heads/CustomHead_{shortname}_34.InvBal_CustomHead_{shortname}_34')
        # Guardian Takedown
        balances.append(f'/Game/PatchDLC/Takedown2/PlayerCharacters/_Customizations/CustomHeads/CustomHead46/CustomHead_{shortname}_46.InvBal_CustomHead_{shortname}_46')
        # DLC3 - Geranium - TODO: need to figure out if this should be in a blacklist
        balances.append(f'/Game/PatchDLC/Geranium/Customizations/PlayerHead/CustomHead38/CustomHead_{shortname}_38.InvBal_CustomHead_{shortname}_38')
        # DLC4 - Alisma - TODO: need to figure out if this should be in a blacklist
        balances.append(f'/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/_Shared/CustomHead_{shortname}_DLC4_01.InvBal_CustomHead_{shortname}_DLC4_01')
        # Introduced in Broken Hearts 2021, though not actually Broken Hearts...
        for num in [33, 35, 36, 37]:
            balances.append(f'/Game/PatchDLC/EventVDay/TwitchDrops/PlayerCharacters/_Customizations/{shortname}/Heads/DA_{abbrev}Head{num}.InvBal_DA_{abbrev}Head{num}')
        if drop_vaultcard:
            # Vault Card 1
            balances.append(f'/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomHeads/CustomHead47/CustomHead_{shortname}_47.InvBal_CustomHead_{shortname}_47')
            # Vault Card 2
            balances.append(f'/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomHeads/CustomHead_{shortname}_49.InvBal_CustomHead_{shortname}_49')
        # Introduced with VC2 but not actually *on* VC2
        balances.append(f'/Game/PatchDLC/VaultCard2/PlayerCharacters/{dirname}/Heads/DA_{abbrev}Head03.InvBal_DA_{abbrev}Head03')

        # Now output
        mod.comment(f'{shortname} Heads')
        set_pool(mod, pool_name, balances)
        mod.newline()
        # Technically this gets set multiple times, but whatever
        num_heads = len(balances)

    ###
    ### Weapon Skins
    ###

    balances = []
    # Base Game
    blacklist = {
            # 21 is gold pack, 22 is gbx pack, 23 is retro pack, 24 is butt stallion pack
            21, 22, 23, 24,
            }
    if not drop_earl:
        blacklist |= {1, 2, 8, 12, 13, 14, 15, 16, 20}
    for num in range(1, 26):
        if num not in blacklist:
            balances.append(f'/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_{num}.InvBal_WeaponSkin_{num}')
    # Bloody Harvest
    balances.append('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01.InvBal_WeaponSkin_BloodyHarvest_01')
    # Broken DLC3 weapon skin; not adding it!
    #balances.append('/Game/PatchDLC/Geranium/Customizations/WeaponSkin/WeaponSkin_DLC3_1.InvBal_WeaponSkin_DLC3_1')
    # Bloody Harvest 2020
    balances.append('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_02.InvBal_WeaponSkin_BloodyHarvest_02')
    # Vault Card 1
    if drop_vaultcard:
        for num in [1, 2, 3]:
            balances.append(f'/Game/PatchDLC/VaultCard/Customizations/WeaponSkin/WeaponSkin_VC1_{num}.InvBal_WeaponSkin_VC1_{num}')
    # Cartels 2021
    balances.append(f'/Game/PatchDLC/Event2/Gear/_Design/WeaponSkins/WeaponSkin_Event2_2.InvBal_WeaponSkin_Event2_2')
    # Vault Card 2
    if drop_vaultcard:
        balances.append(f'/Game/PatchDLC/VaultCard2/Gear/_Design/WeaponSkins/WeaponSkin_VC2_1.InvBal_WeaponSkin_VC2_1')

    # Now output
    mod.comment('Weapon Skins')
    set_pool(mod, '/Game/Gear/WeaponSkins/_Design/ItemPools/ItemPool_Customizations_WeaponSkins_Loot.ItemPool_Customizations_WeaponSkins_Loot', balances)
    mod.newline()
    num_weap_skins = len(balances)

    ###
    ### Weapon Trinkets
    ###

    balances = []
    # Base Game
    blacklist = {
            # These indexes plain ol' don't exist
            1, 23, 36, 55, 56,
            # 51 is gold pack, 52 is neon pack, 53 is butt stallion pack, 54 is gbx pack, 58 is toy box pack
            51, 52, 53, 54, 58,
            }
    if not drop_earl:
        blacklist |= {5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 24, 27, 31, 34, 41}
    if not drop_mission:
        blacklist |= {6, 20, 22, 28, 29, 30}
    for num in range(1, 59):
        if num not in blacklist:
            balances.append(f'/Game/Gear/WeaponTrinkets/_Design/TrinketParts/WeaponTrinket_{num}.InvBal_WeaponTrinket_{num}')
    # Uncategorized DLC
    balances.append('/Game/PatchDLC/Customizations/Gear/Weapons/WeaponTrinkets/WeaponTrinket_59.InvBal_WeaponTrinket_59')
    # Bloody Harvest
    balances.append('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponTrinkets/_Shared/Trinket_League_BloodyHarvest_1.InvBal_Trinket_League_BloodyHarvest_1')
    # DLC1 - Dandelion
    balances.append('/Game/PatchDLC/Dandelion/Gear/WeaponTrinkets/_Shared/Trinket_Dandelion_01_JackGoldenMask.InvBal_Trinket_Dandelion_01_JackGoldenMask')
    balances.append('/Game/PatchDLC/Dandelion/Gear/WeaponTrinkets/_Shared/Trinket_Dandelion_02_Mimic.InvBal_Trinket_Dandelion_02_Mimic')
    balances.append('/Game/PatchDLC/Dandelion/Gear/WeaponTrinkets/_Shared/Trinket_MercenaryDay_01_CandyCane.InvBal_Trinket_MercenaryDay_01_CandyCane')
    # Broken Hearts
    balances.append('/Game/PatchDLC/EventVDay/Gear/Weapon/WeaponTrinkets/_Shared/Trinket_League_VDay_1.InvBal_Trinket_League_VDay_1')
    # DLC2 - Hibiscus - TODO: Need to figure out if these should be on a blacklist
    balances.append('/Game/PatchDLC/Hibiscus/Gear/WeaponTrinkets/_Shared/Trinket_Hibiscus_01_Squidly.InvBal_Trinket_Hibiscus_01_Squidly')
    balances.append('/Game/PatchDLC/Hibiscus/Gear/WeaponTrinkets/_Shared/Trinket_Hibiscus_02_Necrocookmicon.InvBal_Trinket_Hibiscus_02_Necrocookmicon')
    # DLC2 Email reward of some sort?  Keeping it out for now, but I'm guessing that Not Everyone actually gets it?
    #balances.append('/Game/PatchDLC/Steam/Gear/WeaponTrinkets/WeaponTrinket_SteamPunk.InvBal_WeaponTrinket_SteamPunk')
    # Revenge of the Cartels
    balances.append('/Game/PatchDLC/Event2/Gear/_Design/WeaponTrinkets/WeaponTrinket_Cartels_1.InvBal_WeaponTrinket_Cartels_1')
    # DLC3 - Geranium - Commenting these because they're currently broken
    #balances.append('/Game/PatchDLC/Geranium/Customizations/WeaponTrinket/WeaponTrinket_DLC3_1.InvBal_WeaponTrinket_DLC3_1')
    #balances.append('/Game/PatchDLC/Geranium/Customizations/WeaponTrinket/WeaponTrinket_DLC3_2.InvBal_WeaponTrinket_DLC3_2')
    # DLC4 - Alisma - TODO: Need to figure out if these should be on a blacklist
    balances.append('/Game/PatchDLC/Alisma/Gear/WeaponTrinkets/Trinket_DLC4_Trinket_01.InvBal_Trinket_DLC4_Trinket_01')
    balances.append('/Game/PatchDLC/Alisma/Gear/WeaponTrinkets/Trinket_DLC4_Trinket_02.InvBal_Trinket_DLC4_Trinket_02')
    # Bloody Harvest 2020
    balances.append('/Game/PatchDLC/Alisma/Gear/WeaponTrinkets/_Shared/Trinket_League_BloodyHarvest_2020.InvBal_Trinket_League_BloodyHarvest_2020'),
    # DLC5 - Ixora - TODO: Need to figure out if these should be on a blacklist
    balances.append('/Game/PatchDLC/Ixora/Gear/Weapons/WeaponTrinkets/_Design/WeaponTrinket_GearUp.InvBal_WeaponTrinket_GearUp')
    # Broken Hearts 2021 + Others
    balances.append('/Game/PatchDLC/EventVDay/Gear/Weapon/WeaponTrinkets/_Shared/Trinket_League_VDay_2.InvBal_Trinket_League_VDay_2')
    balances.append('/Game/PatchDLC/EventVDay/TwitchDrops/Gear/Weapon/WeaponTrinkets/_Shared/Trinket_Twitch.InvBal_Trinket_Twitch')
    # Vault Card 1
    if drop_vaultcard:
        for num in [1, 2, 3, 4]:
            balances.append(f'/Game/PatchDLC/VaultCard/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC1_{num}.InvBal_WeaponTrinket_VC1_{num}')
    # Cartels 2021
    balances.append('/Game/PatchDLC/Event2/Gear/_Design/WeaponTrinkets/WeaponTrinket_Cartels_2021.InvBal_WeaponTrinket_Cartels_2021')
    # Vault Card 2
    if drop_vaultcard:
        for num in [1, 2, 3, 4, 5, 6]:
            balances.append(f'/Game/PatchDLC/VaultCard2/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC2_{num}.InvBal_WeaponTrinket_VC2_{num}')

    # Now output
    mod.comment('Weapon Trinkets')
    set_pool(mod, '/Game/Gear/WeaponTrinkets/_Design/ItemPools/ItemPool_Customizations_WeaponTrinkets_Loot.ItemPool_Customizations_WeaponTrinkets_Loot', balances)
    mod.newline()
    num_trinkets = len(balances)

    ###
    ### ECHO Skins
    ###

    balances = []
    # Base Game
    blacklist = {
            # These indexes plain ol' don't exist
            11, 25,
            # 12 is retro pack, 13 is neon pack
            12, 13,
            }
    if not drop_earl:
        blacklist |= {1, 2, 3, 4, 5, 6, 8, 9, 10, 26, 27, 28, 29, 30}
    for num in range(1, 36):
        if num not in blacklist:
            balances.append(f'/Game/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_{num:02d}.InvBal_ECHOTheme_{num:02d}')
    # Uncategorized DLC
    balances.append('/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_37.InvBal_ECHOTheme_37')
    # Bloody Harvest
    balances.append('/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_11.InvBal_ECHOTheme_11')
    # Maliwan Takedown
    balances.append('/Game/PatchDLC/Raid1/Customizations/EchoDevice/ECHOTheme_38.InvBal_ECHOTheme_38')
    # DLC1 - Dandelion
    for num in [36, 64, 65, 66]:
        balances.append(f'/Game/PatchDLC/Dandelion/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_{num}.InvBal_ECHOTheme_{num}')
    # Broken Hearts
    balances.append('/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/ECHODevice/EchoTheme_Valentines_01.InvBal_EchoTheme_Valentines_01')
    # DLC2 - Hibiscus - TODO: figure out if any of these should be blacklisted
    for num in [1, 2, 3, 4]:
        balances.append(f'/Game/PatchDLC/Hibiscus/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_DLC2_{num:02d}.InvBal_ECHOTheme_DLC2_{num:02d}')
    # Revenge of the Cartels
    balances.append('/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_44.InvBal_ECHOTheme_44')
    # Guardian Takedown
    balances.append('/Game/PatchDLC/Takedown2/PlayerCharacters/_Customizations/EchoDevice/EchoTheme_Takedown2.InvBal_EchoTheme_Takedown2')
    # DLC3 - Geranium - TODO: figure out if any of these should be blacklisted
    for num in [73, 74, 75, 76]:
        balances.append(f'/Game/PatchDLC/Geranium/Customizations/EchoTheme/ECHOTheme_{num}.InvBal_ECHOTheme_{num}')
    # DLC4 - Alisma - TODO: figure out if any of these should be blacklisted
    for num in [1, 2, 3, 4]:
        balances.append(f'/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_DLC4_{num:02d}.InvBal_ECHOTheme_DLC4_{num:02d}')
    # Bloody Harvest 2020
    balances.append('/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_79.InvBal_ECHOTheme_79')
    # DLC5 - Ixora - TODO: figure out if any of these should be blacklisted
    for num in ['50', '52', '57a', '58']:
        balances.append(f'/Game/PatchDLC/Ixora/Customizations/ECHOTheme/ECHOTheme_{num}.InvBal_ECHOTheme_{num}')
    # Broken Hearts 2021 + Others
    balances.append('/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/ECHODevice/EchoTheme_Valentines_02.InvBal_EchoTheme_Valentines_02')
    balances.append('/Game/PatchDLC/EventVDay/TwitchDrops/PlayerCharacters/_Shared/ECHODevice/ECHOTheme_46.InvBal_ECHOTheme_46')
    # Vault Card 1
    if drop_vaultcard:
        for num in [1, 2, 3, 4]:
            balances.append(f'/Game/PatchDLC/VaultCard/Customizations/EchoDevice/ECHOTheme_VC1_{num}.InvBal_ECHOTheme_VC1_{num}')
    # Cartels 2021
    balances.append('/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_40.InvBal_ECHOTheme_40')
    # Vault Card 2
    if drop_vaultcard:
        for num in [1, 2, 3, 4, 5]:
            balances.append(f'/Game/PatchDLC/VaultCard2/Customizations/EchoDevice/ECHOTheme_VC2_{num}.InvBal_ECHOTheme_VC2_{num}')

    # Now output
    mod.comment('ECHO Skins')
    set_pool(mod, '/Game/PlayerCharacters/_Customizations/EchoDevice/ItemPools/ItemPool_Customizations_Echo_Loot.ItemPool_Customizations_Echo_Loot', balances)
    mod.newline()
    num_echo_skins = len(balances)

    ###
    ### Room Decorations
    ###

    balances = []
    # Base Game
    blacklist = {
            # These indexes plain ol' don't exist
            1, 2, 3, 14, 53, 54,
            }
    if not drop_earl:
        blacklist |= {4, 6, 7, 8, 10, 11, 12, 13, 15, 17, 18, 19, 23, 24, 26, 27, 41, 42, 43, 52, 55, 61, 65}
    if not drop_mission:
        blacklist |= {5}
    for num in range(1, 68):
        balances.append(f'/Game/Pickups/RoomDecoration/RoomDecoration_{num}.InvBal_RoomDecoration_{num}')
    # Maliwan Takedown
    balances.append('/Game/PatchDLC/Raid1/Customizations/RoomDeco/RoomDeco_Raid1_1.InvBal_RoomDeco_Raid1_1')
    # DLC1 - Dandelion
    for num in range(1, 7):
        balances.append(f'/Game/PatchDLC/Dandelion/Customizations/RoomDeco/RoomDeco_DLC1_{num}.InvBal_RoomDeco_DLC1_{num}')
    # DLC2 - Hibiscus - TODO: Figure out if any of these should be on a blacklist
    for num in range(1, 9):
        balances.append(f'/Game/PatchDLC/Hibiscus/Customizations/RoomDeco/RoomDeco_DLC2_{num}.InvBal_RoomDeco_DLC2_{num}')
    # Revenge of the Cartels
    balances.append('/Game/PatchDLC/Event2/Pickups/RoomDecoration/RoomDecoration_Event2_3.InvBal_RoomDecoration_Event2_3')
    # Guardian Takedown
    balances.append('/Game/PatchDLC/Takedown2/InteractiveObjects/PlayerQuarters/RoomDeco_Takedown2.InvBal_RoomDeco_Takedown2')
    # DLC3 - Geranium - TODO: Figure out if any of these should be on a blacklist
    # this one's broken, omit
    #balances.append('/Game/PatchDLC/Geranium/Customizations/RoomDeco/RoomDeco_DLC3_1.InvBal_RoomDeco_DLC3_1')
    for num in [2, 3, 4, 5, 6, 7]:
        balances.append(f'/Game/PatchDLC/Geranium/Customizations/RoomDeco/RoomDecoration_Geranium_{num}.InvBal_RoomDecoration_Geranium_{num}')
    for num in [1, 2, 3]:
        balances.append(f'/Game/PatchDLC/Geranium/Customizations/RoomDeco/RoomDecoration_Geranium_IO_{num}.RoomDecoration_Geranium_IO_{num}')
    balances.append('/Game/PatchDLC/Geranium/Customizations/RoomDeco/RoomDecoration_KeyToCity.InvBal_RoomDecoration_KeyToCity')
    # DLC4 - Alisma - TODO: Figure out if any of these should be on a blacklist
    balances.append('/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/RoomDeco/RoomDeco_DLC4_01_Orbs.InvBal_RoomDeco_DLC4_01_Orbs')
    balances.append('/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/RoomDeco/RoomDeco_DLC4_02_Trophy.InvBal_RoomDeco_DLC4_02_Trophy')
    balances.append('/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/RoomDeco/RoomDeco_DLC4_03_Axe.InvBal_RoomDeco_DLC4_03_Axe')
    balances.append('/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/RoomDeco/RoomDeco_DLC4_04_Moon.InvBal_RoomDeco_DLC4_04_Moon')
    balances.append('/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/RoomDeco/RoomDeco_DLC4_05_Mask.InvBal_RoomDeco_DLC4_05_Mask')
    # Vault Card 1
    if drop_vaultcard:
        for num in [1, 2, 3]:
            balances.append(f'/Game/PatchDLC/VaultCard/Customizations/RoomDeco/RoomDecoration_VC1_{num}.InvBal_RoomDecoration_VC1_{num}')
    # Cartels 2021
    balances.append('/Game/PatchDLC/Event2/Pickups/RoomDecoration/RoomDecoration_Event2_2.InvBal_RoomDecoration_Event2_2')
    # Vault Card 2
    if drop_vaultcard:
        for num in [1, 2]:
            balances.append(f'/Game/PatchDLC/VaultCard2/Customizations/RoomDeco/RoomDecoration_VC2_{num}.InvBal_RoomDecoration_VC2_{num}')

    # Now output
    mod.comment('Room Decorations')
    set_pool(mod, '/Game/Pickups/Customizations/_Design/ItemPools/PlayerRoomDeco/ItemPool_Customizations_RoomDeco_Loot.ItemPool_Customizations_RoomDeco_Loot', balances)
    mod.newline()
    num_decorations = len(balances)

    ###
    ### Now set our weighting on the main customization-drop pool
    ###

    mod.header('Overall customization-type weighting')
    # Keep the "average" weight in this pool to the default 0.05, in case anything weird happens to the
    # pool later.
    target_total = 6*0.05
    total_weight = num_heads + num_skins + num_weap_skins + num_trinkets + num_echo_skins + num_decorations
    for idx, individual_weight in enumerate([
            num_heads,
            num_skins,
            num_weap_skins,
            num_trinkets,
            num_echo_skins,
            num_decorations,
            ]):
        weight = individual_weight/total_weight*target_total
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/GameData/Loot/ItemPools/ItemPool_SkinsAndMisc',
                'BalancedItems.BalancedItems[{}].Weight'.format(idx),
                BVCF(bvc=weight))

    mod.close()
