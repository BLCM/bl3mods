#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('expanded_customization_pools.txt',
        'Expanded Customization Pools',
        [
            'The global drop pools for the various customization types in BL3 only include',
            'a subset of available customizations.  This mod adds in nearly all available',
            "customizations, so you'll be able to get them all just via world drops -- the",
            'ones left out are customizations you get automatically via preorders or deluxe',
            "editions.  (Those aren't useful as drops for anyone without the prerequisite.)",
            'The mod also increases the global drop rate for cutomizations.',
            ''
            'Slot machine rewards are unaffected!',
        ],
        'CustomPools',
        )

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

mod.comment('Increased Cosmetic chances')
for char in [
        # TODO: need to figure out which things actually need definition in here.
        'BPChar_Ape',
        'BPChar_EnforcerShared',
        'BPChar_Frontrunner',
        'BPChar_Goon',
        'BPChar_GuardianShared',
        'BPChar_Heavy_Shared',
        'BPChar_Nekrobug_Shared',
        'BPChar_Nog',
        'BPChar_OversphereShared',
        'BPChar_PsychoShared',
        'BPChar_PunkShared',
        'BPChar_Rakk',
        'BPChar_Ratch',
        'BPChar_Saurian_Shared',
        'BPChar_ServiceBot',
        'BPChar_SkagShared',
        'BPChar_Spiderant',
        'BPChar_Tink',
        'BPChar_Tink_Turret',
        'BPChar_Trooper',
        'BPChar_VarkidShared',

        # Characters used in GBX's own hotfix for the Week 3 Eridium event:
        # (just these five!)
        #'BPChar_PunkBasic',
        #'BPChar_NogBasic',
        #'BPChar_RakkBasic',
        #'BPChar_GuardianWraith',
        #'BPChar_ApeBasic',

        # Don't actually need all the individual ones, thankfully.
        #'BPChar_PsychoSuicide',
        #'BPChar_PsychoLoot',
        #'BPChar_PsychoShared',
        #'BPChar_PsychoFirebrand',
        #'BPChar_PsychoSlugger',
        #'BPChar_PsychoBadass',
        #'BPChar_PsychoBasic',
        #'BPChar_PunkShotgunner',
        #'BPChar_PunkBasic',
        #'BPChar_PunkBadass',
        #'BPChar_PunkShared',
        #'BPChar_PunkAssaulter',
        ]:

    # Cosmetics at 3%, same as Better Loot.
    mod.reg_hotfix(Mod.CHAR, char,
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
mod.comment('Guarantee drop')
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
#
# NOTE: basically all of these have "holes" in the enumeration, so we're setting some
# balances which don't exist.  Whatever.  Those just never drop, so it's fine.

# Skins/Heads first.
for (dirname, shortname) in [
        ('Beastmaster', 'Beastmaster'),
        ('Gunner', 'Gunner'),
        ('Operative', 'Operative'),
        ('SirenBrawler', 'Siren'),
        ]:

    # Skins
    pool_name = f'/Game/Pickups/Customizations/_Design/ItemPools/Skins/ItemPool_Customizations_Skins_Loot_{shortname}.ItemPool_Customizations_Skins_Loot_{shortname}'
    balances = []
    # Base Game
    # 34 is retro pack, 35 is neon pack 
    blacklist = {34, 35}
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
    mod.comment(f'{shortname} Skins')
    set_pool(mod, pool_name, balances)
    mod.newline()

    # Heads
    pool_name = f'/Game/Pickups/Customizations/_Design/ItemPools/Heads/ItemPool_Customizations_Heads_Loot_{shortname}.ItemPool_Customizations_Heads_Loot_{shortname}'
    balances = []
    # Base Game
    for num in range(1, 27):
        balances.append(f'/Game/PlayerCharacters/_Customizations/{dirname}/Heads/CustomHead_{shortname}_{num}.InvBal_CustomHead_{shortname}_{num}')
    # Bloody Harvest, Ordering Bonuses, etc
    # 28 is retro pack, 29 is neon pack (26 doesn't exist)
    for num in [25, 27]:
        balances.append(f'/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/{dirname}/Heads/CustomHead_{shortname}_{num}.InvBal_CustomHead_{shortname}_{num}')
    # DLC1 - Dandelion
    balances.append(f'/Game/PatchDLC/Dandelion/PlayerCharacters/_Customizations/_Shared/CustomHead_{shortname}_30.InvBal_CustomHead_{shortname}_30')
    mod.comment(f'{shortname} Heads')
    set_pool(mod, pool_name, balances)
    mod.newline()

# Weapon Skins
balances = []
# Base Game
# 21 is gold pack, 22 is gbx pack, 23 is retro pack, 24 is butt stallion pack
blacklist = {21, 22, 23, 24}
for num in range(1, 26):
    if num not in blacklist:
        balances.append(f'/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_{num}.InvBal_WeaponSkin_{num}')
# Bloody Harvest
balances.append('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01.InvBal_WeaponSkin_BloodyHarvest_01')
mod.comment('Weapon Skins')
set_pool(mod, '/Game/Gear/WeaponSkins/_Design/ItemPools/ItemPool_Customizations_WeaponSkins_Loot.ItemPool_Customizations_WeaponSkins_Loot', balances)
mod.newline()

# Weapon Trinkets
balances = []
# Base Game
# 51 is gold pack, 52 is neon pack, 53 is butt stallion pack, 54 is gbx pack, 58 is toy box pack
blacklist = {51, 52, 53, 54, 58}
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
mod.comment('Weapon Trinkets')
set_pool(mod, '/Game/Gear/WeaponTrinkets/_Design/ItemPools/ItemPool_Customizations_WeaponTrinkets_Loot.ItemPool_Customizations_WeaponTrinkets_Loot', balances)
mod.newline()

# ECHO Skins
balances = []
# Base Game
# 12 is retro pack, 13 is neon pack
blacklist = {12, 13}
for num in range(1, 35):
    if num not in blacklist:
        balances.append(f'/Game/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_{num:02d}.InvBal_ECHOTheme_{num:02d}')
# Unknown weird theme out in a strange location - AMD-themed, can't seem to drop it.
#balances.append('/Game/UI/_Shared/CustomIconsEcho/ECHOTheme_35.InvBal_ECHOTheme_35')
# Uncategorized DLC
balances.append('/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_37.InvBal_ECHOTheme_37')
# Bloody Harvest
balances.append('/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_11.InvBal_ECHOTheme_11')
# Maliwan Takedown
balances.append('/Game/PatchDLC/Raid1/Customizations/EchoDevice/ECHOTheme_38.InvBal_ECHOTheme_38')
# DLC1 - Dandelion
for num in [36, 64, 65, 66]:
    balances.append(f'/Game/PatchDLC/Dandelion/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_{num}.InvBal_ECHOTheme_{num}')
mod.comment('ECHO Skins')
set_pool(mod, '/Game/PlayerCharacters/_Customizations/EchoDevice/ItemPools/ItemPool_Customizations_Echo_Loot.ItemPool_Customizations_Echo_Loot', balances)
mod.newline()

# Room Decorations
balances = []
# Base Game
for num in range(1, 68):
    balances.append(f'/Game/Pickups/RoomDecoration/RoomDecoration_{num}.InvBal_RoomDecoration_{num}')
# Maliwan Takedown
balances.append('/Game/PatchDLC/Raid1/Customizations/RoomDeco/RoomDeco_Raid1_1.InvBal_RoomDeco_Raid1_1')
# DLC1 - Dandelion
for num in range(1, 7):
    balances.append(f'/Game/PatchDLC/Dandelion/Customizations/RoomDeco/RoomDeco_DLC1_{num}.InvBal_RoomDeco_DLC1_{num}')
mod.comment('Room Decorations')
set_pool(mod, '/Game/Pickups/Customizations/_Design/ItemPools/PlayerRoomDeco/ItemPool_Customizations_RoomDeco_Loot.ItemPool_Customizations_RoomDeco_Loot', balances)
mod.newline()

mod.close()
