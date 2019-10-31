#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

def set_pool(mod, pool_to_set, balances, mainattr='InventoryBalanceData', baltype='InventoryBalanceData', char=None):

    parts = []
    for bal in balances:
        if type(bal) is tuple:
            (bal1, bal2) = bal
        else:
            bal1 = bal
            bal2 = bal
        part = '({}={},ResolvedInventoryBalanceData={}\'"{}"\',Weight=(BaseValueConstant=1))'.format(
                mainattr,
                bal1,
                baltype,
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

mod = Mod('testing_loot_drops.txt',
        'Testing loot drops...',
        [],
        'Drops',
        )

# This one's my usual 'rotating' pool that gets used
pool_to_set = '/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary'
extra_pool_bit = 'ItemPool_SnipeRifles_Legendary'
#pool_to_set = '/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary'
#extra_pool_bit = 'ItemPool_Shotguns_Legendary'
#pool_to_set = '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary'
#extra_pool_bit = 'ItemPool_Shields_05_Legendary'
#pool_to_set = '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary'
#extra_pool_bit = 'ItemPool_GrenadeMods_05_Legendary'
#pool_to_set = '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts'
#extra_pool_bit = 'ItemPool_Artifacts'

# Weapon skin test, don't recall if this worked or not.
#pool_to_set = '/Game/Gear/WeaponSkins/_Design/ItemPools/ItemPool_Customizations_WeaponSkins_Loot',
#extra_pool_bit = 'ItemPool_Customizations_WeaponSkins_Loot'

# Attempt to get the NOG heads; doesn't work -- I suspect that pool might not
# exist outside the the mission it's ordinarily referenced from (that or the
# heads themselves are broken)
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/Heads/ItemPool_Customizations_Heads_Mission_Luchador'
#extra_pool_bit = 'ItemPool_Customizations_Heads_Mission_Luchador'

# Hoovering up cosmetics
#pool_to_set = '/Game/GameData/Loot/ItemPools/ItemPool_SkinsAndMisc'
#extra_pool_bit = 'ItemPool_SkinsAndMisc'
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/Heads/ItemPool_Customizations_Heads_Loot_Siren'
#extra_pool_bit = 'ItemPool_Customizations_Heads_Loot_Siren'

# Gold weapon skin might be: '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_21.InvBal_WeaponSkin',
# ... I couldn't seem to hardcode specific drops to any of those, though.  The pool which ordinarily
# drops them (but not WeaponSkin_21, among others) is /Game/Gear/WeaponSkins/_Design/ItemPools/ItemPool_Customizations_WeaponSkins_Loot
# Heh, and setting *that* pool to be what standards drop from actually goes so far as to crash the
# game.  Gonna give up on customization dropping for now.  :)

# Attempts to cheat Bloody Harvest
# No actual items in this one, as expected
#pool_to_set = '/Game/PatchDLC/BloodyHarvest/GameData/Challenges/ItemPool_LeagueChallenge_GlobalWeaponSkin'
#extra_pool_bit = 'ItemPool_LeagueChallenge_GlobalWeaponSkin'
# This works but it's also the most trivial one to get
#pool_to_set = '/Game/PatchDLC/BloodyHarvest/GameData/Challenges/ItemPool_LeagueChallenge_Trinket1'
#extra_pool_bit = 'ItemPool_LeagueChallenge_Trinket1'

balances = [
        #'/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Balance/Balance_PS_TOR_Devestator.Balance_PS_TOR_Devestator',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre.Balance_PS_Tediore_Sabre',
        #'/Game/Gear/GrenadeMods/_Design/_Unique/ObviousTrap/Balance/InvBalD_GM_ObviousTrap.InvBalD_GM_ObviousTrap',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm',

        # Playing around with modding Maliwan charge times, here's some spawns for Maliwan guns
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_04_VeryRare.Balance_PS_MAL_04_VeryRare',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_04_VeryRare.Balance_SG_MAL_04_VeryRare',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_04_VeryRare.Balance_SM_MAL_04_VeryRare',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_04_VeryRare.Balance_MAL_SR_04_VeryRare',
        #'/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_Rare.Balance_PS_MAL_ETech_Rare',
        #'/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Maliwan/Balance/Balance_SG_MAL_ETech_VeryRare.Balance_SG_MAL_ETech_VeryRare',
        #'/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Maliwan/Balance/Balance_SM_MAL_ETech_VeryRare.Balance_SM_MAL_ETech_VeryRare',
        #'/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Maliwan/Balance/Balance_SR_MAL_ETech_VeryRare.Balance_SR_MAL_ETech_VeryRare',

        # Maliwan uniques/legendaries
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3.Balance_SM_MAL_E3',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock.Balance_PS_MAL_Hellshock',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber.Balance_PS_MAL_Plumber',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists.Balance_PS_MAL_ThunderballFists',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator.Balance_PS_MAL_HyperHydrator',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller.Balance_PS_MAL_Starkiller',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch.Balance_PS_MAL_SuckerPunch',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion.Balance_SG_MAL_Recursion',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev.Balance_SG_MAL_Trev',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp.Balance_SG_MAL_Wisp',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Balance/Balance_SG_MAL_Mouthpiece2.Balance_SG_MAL_Mouthpiece2',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek.Balance_SG_MAL_Shriek',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman.Balance_SM_MAL_Cutsman',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin.Balance_SM_MAL_DestructoSpin',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted.Balance_SM_MAL_Devoted',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill.Balance_SM_MAL_CloudKill',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit.Balance_SM_MAL_Crit',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon.Balance_SM_MAL_Egon',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer.Balance_SM_MAL_Emporer',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins.Balance_SM_MAL_Kevins',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami.Balance_SM_MAL_Tsunami',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse.Balance_SM_MAL_VibraPulse',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun.Balance_SM_MAL_westergun',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD.Balance_MAL_SR_ASMD',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa.Balance_MAL_SR_Krakatoa',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki.Balance_MAL_SR_Soleki',

        # Various attempts to figure out how the heck to add skin/head drops.  Have not figured it out yet.
        #('/Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren', '/Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_1.InvBal_CustomHead_Siren'),
        #('/Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_1', '/Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_1.InvBal_CustomHead_Siren'),
        #('/Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_1.InvBal_CustomHead_Siren', '/Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren'),
        #'/Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_1.InvBal_CustomHead_Siren',

        # This works to spawn the top-tier bloody harvest reward!
        #'/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01.InvBal_WeaponSkin_BloodyHarvest_01',
        ]

set_pool(mod, '{}.{}'.format(pool_to_set, extra_pool_bit), balances)
#, mainattr='CustomizationInventoryBalanceData', baltype='CustomizationInventoryBalanceData')

for char in [
        # TODO: This isn't actually sufficient; if you spawn in Floodmoor Basin, for
        # instance, the enemies around the lodge area don't trigger it.  May have to
        # expand this list after all!
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
        ]:

    #set_pool(mod, '{}.{}'.format(pool_to_set, extra_pool_bit), balances, char=char)
    mod.reg_hotfix(Mod.CHAR, char,
            '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear',
            'ItemPools[0].PoolProbability',
            """(
                BaseValueConstant=1.000000,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.000000
            )""")
    mod.reg_hotfix(Mod.CHAR, char,
            '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear',
            'ItemPools[0].ItemPool',
            'ItemPoolData\'"{}"\''.format(pool_to_set))
    mod.reg_hotfix(Mod.CHAR, char,
            '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear',
            'ItemPools[0].NumberOfTimesToSelectFromThisPool',
            """(
                BaseValueConstant=5.000000,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.000000
            )""")

mod.close()
