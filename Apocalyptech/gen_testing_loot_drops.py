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
        #'/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre.Balance_PS_Tediore_Sabre',
        #'/Game/Gear/GrenadeMods/_Design/_Unique/ObviousTrap/Balance/InvBalD_GM_ObviousTrap.InvBalD_GM_ObviousTrap',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent.Balance_PS_VLA_Magnificent',

        # Bloody Harvest shenanigans
        #'/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie.Balance_PS_JAK_Maggie',
        #'/Game/PatchDLC/BloodyHarvest/Gear/Weapons/SniperRifles/Dahl/_Design/_Unique/Frostbolt/Balance/Balance_SR_DAL_ETech_Frostbolt.Balance_SR_DAL_ETech_Frostbolt',
        #'/Game/Gear/GrenadeMods/_Design/_Unique/ObviousTrap/Balance/InvBalD_GM_ObviousTrap.InvBalD_GM_ObviousTrap',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun.Balance_SM_MAL_westergun',

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
        #('/Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_1.InvBal_CustomSkin_Siren', '/Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren.InvBal_CustomSkin_Siren'),

        # This works to spawn the top-tier bloody harvest reward!
        #'/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01.InvBal_WeaponSkin_BloodyHarvest_01',

        # Maliwan Takedown weapons
        # Redistributor
        #'/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2',
        # Moonfire
        #'/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon',
        # Kyb's Worth
        #'/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth',
        # P2P Networker
        #'/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link.Balance_SM_MAL_Link',
        # Tiggs' Boom
        #'/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom',

        # Maliwan Takedown Shields
        # Version 0.m
        #'/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom',
        # Re-Charger Berner
        #'/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner',
        # Frozen Snowshoe
        #'/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart',
        # Re-Charger variant
        #'/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger',

        # Maliwan Takedown COMs
        # R4kk P4k
        #'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1.InvBalD_CM_Beastmaster_Raid1',
        # Raging Bear
        #'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_Raid1.InvBalD_CM_Gunner_Raid1',
        # Antifreeze
        #'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_Raid1.InvBalD_CM_Operative_Raid1',
        # Spiritual Driver
        #'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_Raid1.InvBalD_CM_Siren_Raid1',

        # Mayhem 4 Gear:
        # Crader's EM-P5
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5.Balance_SM_DAHL_CraderMP5',
        # Vosk's Deathgrip
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip.Balance_SG_MAL_DeathGrip',
        # S3RV-80S-EXECUTE
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute.Balance_PS_TED_Execute',
        # Good Juju
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju.Balance_DAL_AR_ETech_Juju',
        # Juliet's Dazzle
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet.Balance_AR_TOR_Juliet',
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop.Balance_AR_TOR_Juliet_WorldDrop',
        # Tankman's Shield
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman',
        # Zheitsev's Eruption
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev.Balance_AR_COV_Zheitsev',

        # More Maliwan Takedown patch additions, dunno what's up with these.  They seem to be basically identical
        # to their non-Maliwan-Takedown counterparts.
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/CommanderPlanetoid/InvBalD_Artifact_CommanderPlanetoid.InvBalD_Artifact_CommanderPlanetoid',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/CosmicCrater/InvBalD_Artifact_CosmicCrater.InvBalD_Artifact_CosmicCrater',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/Deathless/InvBalD_Artifact_Deathless.InvBalD_Artifact_Deathless',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/LoadedDice/InvBalD_Artifact_LoadedDice.InvBalD_Artifact_LoadedDice',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/MoxxisEndowment/InvBalD_Artifact_MoxxisEndowment.InvBalD_Artifact_MoxxisEndowment',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/OttoIdol/InvBalD_Artifact_OttoIdol.InvBalD_Artifact_OttoIdol',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/PullOutMethod/InvBalD_Artifact_PullOutMethod.InvBalD_Artifact_PullOutMethod',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/RocketBoots/InvBalD_Artifact_RocketBoots.InvBalD_Artifact_RocketBoots',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/Safegaurd/InvBalD_Artifact_Safegaurd.InvBalD_Artifact_Safegaurd',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/Salvo/InvBalD_Artifact_Salvo.InvBalD_Artifact_Salvo',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/SplatterGun/InvBalD_Artifact_SplatterGun.InvBalD_Artifact_SplatterGun',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/StaticTouch/InvBalD_Artifact_StaticTouch.InvBalD_Artifact_StaticTouch',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/VictoryRush/InvBalD_Artifact_VictoryRush.InvBalD_Artifact_VictoryRush',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/WhiteElephant/InvBalD_Artifact_WhiteElephant.InvBalD_Artifact_WhiteElephant',

        # Probably the same story, just with Siren COMs this time...
        #'/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Breaker.InvBalD_ClassMod_Siren_Breaker',
        #'/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Dragon.InvBalD_ClassMod_Siren_Dragon',
        #'/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Elementalist.InvBalD_ClassMod_Siren_Elementalist',
        #'/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Nimbus.InvBalD_ClassMod_Siren_Nimbus',
        #'/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Phasezerker.InvBalD_ClassMod_Siren_Phasezerker',
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
