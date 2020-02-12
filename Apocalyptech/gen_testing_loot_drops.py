#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

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

mod = Mod('testing_loot_drops.txt',
        'Testing loot drops...',
        [],
        'Drops',
        )

do_pool_set = True
drop_quantity = 5

# This one's my usual 'rotating' pool that gets used
pool_to_set = '/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary'
#pool_to_set = '/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary'
#pool_to_set = '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary'
#pool_to_set = '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary'
#pool_to_set = '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_05_Legendary'
#pool_to_set = '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary'
#pool_to_set = '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster_05_Legendary'
#pool_to_set = '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner_05_Legendary'
#pool_to_set = '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative_05_Legendary'
#pool_to_set = '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_03_Rare'
#pool_to_set = '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts'
#pool_to_set = '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All'
#pool_to_set = '/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_VeryRare'

# Hoovering up cosmetics
#pool_to_set = '/Game/GameData/Loot/ItemPools/ItemPool_SkinsAndMisc'
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/Heads/ItemPool_Customizations_Heads_Loot_Siren'
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/Heads/ItemPool_Customizations_Heads_Loot_Beastmaster'
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/Skins/ItemPool_Customizations_Skins_Loot_Beastmaster'
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/Heads/ItemPool_Customizations_Heads_Loot_Gunner'
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/PlayerRoomDeco/ItemPool_Customizations_RoomDeco_Loot'
#pool_to_set = '/Game/Gear/WeaponTrinkets/_Design/ItemPools/ItemPool_Customizations_WeaponTrinkets_Loot'
#pool_to_set = '/Game/PlayerCharacters/_Customizations/EchoDevice/ItemPools/ItemPool_Customizations_Echo_Loot'
#pool_to_set = '/Game/Gear/WeaponSkins/_Design/ItemPools/ItemPool_Customizations_WeaponSkins_Loot'

balances = [

        # Testing Gear!
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5.Balance_SM_DAHL_CraderMP5',
        '/Game/Gear/Shields/_Design/_Uniques/Transformer/Balance/InvBalD_Shield_LGD_Transformer.InvBalD_Shield_LGD_Transformer',

        # Atlas Gear (which have multiple tracker types; this isn't exhaustive)
        #'/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_01_Common.Balance_ATL_AR_01_Common',
        #'/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_02_UnCommon.Balance_ATL_AR_02_UnCommon',
        #'/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_03_Rare.Balance_ATL_AR_03_Rare',
        #'/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_04_VeryRare.Balance_ATL_AR_04_VeryRare',
        #'/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/Balance_ATL_AR_Carrier.Balance_ATL_AR_Carrier',
        #'/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_01_Common.Balance_HW_ATL_01_Common',
        #'/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_02_UnCommon.Balance_HW_ATL_02_UnCommon',
        #'/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_03_Rare.Balance_HW_ATL_03_Rare',
        #'/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_04_VeryRare.Balance_HW_ATL_04_VeryRare',
        #'/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_01_Common.Balance_PS_ATL_01_Common',
        #'/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_02_UnCommon.Balance_PS_ATL_02_UnCommon',
        #'/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_03_Rare.Balance_PS_ATL_03_Rare',
        #'/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_04_VeryRare.Balance_PS_ATL_04_VeryRare',

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

        # Bloody Harvest rewards:
        #'/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponTrinkets/_Shared/Trinket_League_BloodyHarvest_1.InvBal_Trinket_League_BloodyHarvest_1',
        #'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_11.InvBal_ECHOTheme_11',
        #'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_40.InvBal_CustomSkin_Beastmaster_40',
        #'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_40.InvBal_CustomSkin_Gunner_40',
        #'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_40.InvBal_CustomSkin_Operative_40',
        #'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_40.InvBal_CustomSkin_Siren_40',
        #'/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01.InvBal_WeaponSkin_BloodyHarvest_01',

        # NOG Heads:
        #'/Game/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_22.InvBal_CustomHead_Beastmaster_22',
        #'/Game/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_22.InvBal_CustomHead_Gunner_22',
        #'/Game/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_22.InvBal_CustomHead_Operative_22',
        #'/Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_22.InvBal_CustomHead_Siren_22',

        # Golden weapon skin + trinket.  Technically we already have these, as it turns out, but they're not
        # active unless you actually have the preorder "DLC" or whatever.
        #'/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_21.InvBal_WeaponSkin_21',
        #'/Game/Gear/WeaponTrinkets/_Design/TrinketParts/WeaponTrinket_51.InvBal_WeaponTrinket_51',

        # Weapons which don't have anointments in the base game
        #'/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace',
        #'/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/AmberManagement/Balance/Balance_AR_TOR_AmberManagement',
        #'/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Salvage/Balance_PS_Tediore_BabyMaker_Salvage',
        #'/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Balance_AR_VLA_BigSucc',
        #'/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Balance/Balance_SG_TOR_Brewha',
        #'/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Balance/Balance_SR_DAL_BrashisDedication',
        #'/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/Balance_PS_JAK_Buttplug',
        #'/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/Balance_PS_COV_Chad',
        #'/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/Balance_VLA_SR_Prison',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer',
        #'/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/Balance_SG_JAK_Fingerbiter',
        #'/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Balance/Balance_HW_TOR_BurgerCannon',
        #'/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf',
        #'/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/Balance_AR_JAK_HandOfGlory',
        #'/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Balance/Balance_HW_COV_HotDrop',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator',
        #'/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic',
        #'/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Balance/Balance_SR_DAL_WorldDestroyer',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins',
        #'/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/Balance_PS_COV_Mouthpiece',
        #'/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech',
        #'/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Balance/Balance_PS_ATL_Drill',
        #'/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/ZeroForPlayer/Balance_SR_HYP_ZeroForPlayer',
        #'/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/Balance_AR_JAK_PasRifle',
        #'/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/Balance_PS_ATL_Warmonger',
        #'/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/Balance_HW_COV_PortaPooper',
        #'/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/Balance_HW_TOR_RYNO',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher',
        #'/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Balance_PS_JAK_SpyRevolver',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller',
        #'/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/Balance_AR_JAK_TraitorsDeath',
        #'/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/Balance_SR_HYP_TwoTime',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3',
        #'/Game/PatchDLC/BloodyHarvest/Gear/GrenadeMods/_Design/_Unique/FontOfDarkness/Balance/InvBalD_GM_TOR_FontOfDarkness',

        # Testing my no-Projected-aug mod
        #'/Game/PatchDLC/Dandelion/Gear/Shield/DoubleDowner/Balance/InvBalD_Shield_DoubleDowner',
        #'/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner',
        #'/Game/Gear/Shields/_Design/_Uniques/Transformer/Balance/InvBalD_Shield_LGD_Transformer',
        #'/Game/Gear/Shields/_Design/_Uniques/Re-Charger/Balance/InvBalD_Shield_LGD_ReCharger',
        #'/Game/Gear/Shields/_Design/_Uniques/FrontLoader/Balance/InvBalD_Shield_LGD_FrontLoader',
        #'/Game/Gear/Shields/_Design/_Uniques/StopGap/Balance/InvBalD_Shield_LGD_StopGap',
        #'/Game/Gear/Shields/_Design/_Uniques/Rectifier/Balance/InvBalD_Shield_LGD_Rectifier',
        #'/Game/Gear/Shields/_Design/_Uniques/MessyBreakup/bALANCE/InvBalD_Shield_MessyBreakup',
        ]

last_bit = pool_to_set.split('/')[-1]
pool_to_set_full = '{}.{}'.format(pool_to_set, last_bit)

# Set the pool, if we've been told to
if do_pool_set:
    set_pool(mod, pool_to_set_full, balances)

# TODO: Would like to get trash piles back in here too, though I think we'd
# have to have a level hotfix for each level, and I don't feel like scripting
# that out yet.
#
# These definitions *should* be pretty thorough, though note that bosses and
# minibosses have been left alone, since I'm only gonna be mobbing while
# testing this stuff.

for (pool, chars) in [

        # Base-game Standard Enemy drop list
        ('/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear', [

            # TODO: This isn't always sufficient; if you spawn in Floodmoor Basin, for
            # instance, the enemies around the lodge area don't trigger it, nor do Saurians
            # in Floodmoor Basin.  Saurians in particular have proven difficult; even
            # enumerating all the BPChar* entries which reference the "Shared" one didn't
            # seem to do it.  Hrmph.  Giving up for now!
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

            # These are all the BPChars which reference BPChar_Saurian_Shared...
            #'BPChar_Saurian_Grog_Poison_Fodder',
            #'BPChar_SaurianLaser',
            #'BPChar_SaurianShield',
            #'BPChar_Saurian_SlaughterBoss',
            #'BPChar_Saurian_TrialBoss',
            #'BPChar_Saurian_Grog',
            #'BPChar_Saurian_Grog_Fire',
            #'BPChar_Saurian_Grog_Poison',
            #'BPChar_Saurian_Hamtaurus',
            #'BPChar_Saurian_Hamtaurus_Badass',
            #'BPChar_Saurian_Predator',
            #'BPChar_Saurian_Predator_X',
            #'BPChar_Saurian_Pygmimus',
            #'BPChar_SaurianShiny',
            #'BPChar_Saurian_Slinger',
            #'BPChar_Saurian_Tyrant',
            #'BPChar_SaurianForager',

            'BPChar_ServiceBot',
            'BPChar_SkagShared',
            'BPChar_Spiderant',
            'BPChar_Tink',
            'BPChar_Tink_Turret',
            'BPChar_Trooper',
            'BPChar_VarkidShared',
            'BPChar_LootTracker',

            # Maliwan Takedown
            'BPChar_MechBasicMini',
            'BPChar_MechMeleeMini',

            # Moxxi's Heist
            'BPChar_EnforcerShared_Stripped',
            'BPChar_Goon_Stripped',
            'BPChar_PsychoShared_Stripped',
            'BPChar_PunkShared_Stripped',
            'BPChar_TinkStripped',
            ]),

        # Goliaths
        ('/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_Godliath', ['BPChar_Goliath', 'BPChar_Goliath_Stripped']),
        ('/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_NonEnraging', ['BPChar_Goliath', 'BPChar_Goliath_Stripped']),
        ('/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_Ultimate', ['BPChar_Goliath', 'BPChar_Goliath_Stripped']),
        ('/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_SuperRaging', ['BPChar_Goliath', 'BPChar_Goliath_Stripped']),
        ('/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_MegaRaging', ['BPChar_Goliath', 'BPChar_Goliath_Stripped']),

        # Dandelion standard-enemy drop list
        ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Dandelion', [
            'BPChar_AcidTrip_EarlyPrototype',
            'BPChar_EnforcerBruiser_Looter',
            'BPChar_GoliathBasic_Looter',
            'BPChar_GoliathMidget_Looter',
            'BPChar_GoonBasic_looter',
            'BPChar_GoonVortex_Looter',
            'BPChar_PsychoBasic_Looter',
            'BPChar_PsychoFirebrand_Looter',
            'BPChar_PsychoSlugger_Looter',
            'BPChar_PsychoSuicide_Looter',
            'BPChar_PunkAssaulter_Looter',
            'BPChar_PunkBasic_Looter',
            'BPChar_PunkShotgunner_Looter',
            'BPChar_PunkSniper_Looter',
            'BPChar_TinkBasic_Looter',
            'BPChar_TinkPsycho_Looter',
            'BPChar_TinkShotgun_Looter',
            'BPChar_TinkSuicide_Looter',
            'BPChar_CasinoBot_BigJanitor',
            ]),

        # Dandelion standard-loader drop list
        ('/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPoolList_StandardEnemyGunsandGearLoader', [
            # Moxxi's Heist
            'BPChar_HyperionTurretBasic',
            'BPChar_LoaderShared',
            'BPChar_WeeLoaderBasic',
            ]),

        # Base game badass enemy drop list
        ('/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear', [

            # Base Game (don't actually care about the unique enemies in here, but
            # it was less work to just leave 'em in)
            'BPChar_Ape_Hunt01',
            'BPChar_ApeJungleMonarch',
            'BPChar_ApeBadass',
            'BPChar_ApeLoot',
            'BPChar_Enforcer_BountyPrologue',
            'BPChar_EnforcerUrist',
            'BPChar_EnforcerBadass',
            'BPChar_Frontrunner_Badass',
            'BPChar_Goliath_Badass',
            'BPChar_GoonBadass',
            'BPChar_GuardianGemGoblin',
            'BPChar_GuardianWraithBadass',
            'BPChar_Heavy_Badass',
            'BPChar_Mech',
            'BPChar_Nekrobug_Badass',
            'BPChar_NogBadass',
            'BPChar_NogNogromancer',
            'BPChar_OversphereBadass',
            'BPChar_PsychoBadass',
            'BPChar_Punk_Bounty01a',
            'BPChar_Punk_Bounty01b',
            'BPChar_Punk_Bounty01c',
            'BPChar_Punk_Bounty01d',
            'BPChar_PunkBrewHag',
            'BPChar_PunkMotherOfDragons',
            'BPChar_PunkBadass',
            'BPChar_Rakk_Dragon',
            'BPChar_Rakk_DragonCryo',
            'BPChar_Rakk_Hunt01',
            'BPChar_Rakk_HuntSkrakk',
            'BPChar_RakkBadassCryo',
            'BPChar_RakkChromatic',
            'BPChar_RakkQueen',
            'BPChar_RatchBadass',
            'BPChar_RatchHive',
            'BPChar_Saurian_Grog_Poison',
            'BPChar_Saurian_Hamtaurus_Badass',
            'BPChar_Saurian_Tyrant',
            'BPChar_ServiceBot_SWAT',
            'BPChar_Skag_Rare01',
            'BPChar_SkagBadass',
            'BPChar_SpiderantKing',
            'BPChar_SpiderantQueen',
            'BPChar_Tink_Bounty01',
            'BPChar_TinkRare02',
            'BPChar_TinkUndertaker',
            'BPChar_TinkBadass',
            'BPChar_Tink_SentryRocketPodBigD',
            'BPChar_TrooperBadass',
            'BPChar_VarkidBadass',
            'BPChar_AtlasSoldier_Bounty01',

            # Maliwan Takedown
            'BPChar_Behemoth',

            # Moxxi's Heist
            'BPChar_EnforcerBadass_Stripped',
            'BPChar_Goliath_Badass_Stripped',
            'BPChar_GoonBadass_Stripped',
            'BPChar_PunkBadass_Stripped',
            'BPChar_TinkBadass_Stripped',
            'BPChar_Mimic',
            'BPChar_WeeLoaderShared',
            ]),

        # Dandelion Badass enemy list
        ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_BadassEnemyGunsGear_Dandelion', [
            'BPChar_SisterlyLove_DebtCollectorLoader',
            'BPChar_GreatEscape_Rudy',
            'BPChar_RagingBot_MachineGunMikey',
            'BPChar_EnforcerBadass_Looter',
            'BPChar_Enforcer_PrettyBoy',
            'BPChar_GoliathBadass_Looter',
            'BPChar_GoonBadass_Looter',
            'BPChar_PsychoBadass_Looter',
            'BPChar_PunkArmored_LooterVIP',
            'BPChar_PunkBadass_Looter',
            'BPChar_TinkBadass_Looter',
            'BPChar_TinkBadassArmored_Looter',
            # /Dandelion/Missions/Plot/Ep05_ThePlan/SpawnOption_TricksyNick_Farmable but eh.
            ]),

        # Dandelion Badass loader list
        ('/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPoolList_BadassEnemyGunsGearLoader1', [
            'BPChar_HyperionTurretBadass',
            'BPChar_LoaderBadass',
            ]),

        # Dandelion Constructors
        ('/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/ItemPoolList_Constructor', [
            'BPChar_Constructor',
            ]),

        # Anointed Enemies
        ('/Game/GameData/Loot/ItemPools/ItemPoolList_AnointedEnemyGunsGear', [

            'BPChar_EnforcerAnointed',
            'BPChar_Goliath_Anointed',
            'BPChar_GoonAnointed',
            'BPChar_PsychoAnointed',
            'BPChar_Punk_Anointed',
            'BPChar_TinkAnointed',
            'BPChar_VarkidHunt02_LarvaA',
            'BPChar_VarkidHunt02_LarvaB',
            'BPChar_VarkidHunt02_LarvaC',
            'BPChar_VarkidHunt02_LarvaD',
            'BPChar_VarkidSuperBadass',
            ]),

        ]:

    last_bit = pool.split('/')[-1]
    full_pool = '{}.{}'.format(pool, last_bit)

    for char in chars:
        mod.reg_hotfix(Mod.CHAR, char,
                full_pool,
                'ItemPools',
                """(
                    (
                        ItemPool=ItemPoolData'"{}"'
                        PoolProbability=(
                            BaseValueConstant=1,
                            DataTableValue=(DataTable=None,RowName="",ValueName=""),
                            BaseValueAttribute=None,
                            AttributeInitializer=None,
                            BaseValueScale=1
                        ),
                        NumberOfTimesToSelectFromThisPool=(
                            BaseValueConstant={},
                            DataTableValue=(DataTable=None,RowName="",ValueName=""),
                            BaseValueAttribute=None,
                            AttributeInitializer=None,
                            BaseValueScale=1
                        )
                    )
                )""".format(pool_to_set_full, drop_quantity))

mod.close()
