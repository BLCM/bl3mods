#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, Pool

mod = Mod('better_loot.txt',
        'Better Loot, ish',
        [],
        'BL',
        )

def set_legendary_odds(mod, charname, row, chance, obj_name='/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds.Table_LegendarySpecificLootOdds'):
    """
    Sets the drop odds for specific legendary loot pools, used for bosses.
    """
    # Note that the object is not loaded until the character using it is loaded!
    for attr in [
            'LegendaryDropChance_Playthrough1_48_4189D9DA42C2B912FC25209E8C353A26',
            'LegendaryDropChance_Playthrough2_50_11E6C8E8493E0A73AF9B35891E7CE111',
            'LegendaryDropChance_Mayhem_49_A4643C45437ECBC97BC6629ECC66F6B6',
            ]:
        # The Farming Frenzy event sets the values in this table using a regular SparkPatchEntry,
        # rather than by character, so we could probably do that too.  Since we're only doing
        # one hotfix per pool anyway, though, it doesn't really save us much, and if I changed
        # it I'd have to test, so I'm just leaving it as a Char hotfix for now.
        mod.table_hotfix(Mod.CHAR, charname,
                obj_name,
                row,
                attr,
                chance)

def set_death_pools(mod, char_name, obj_name, pools=[]):
    (_, obj_name_base) = obj_name.rsplit('/', 1)
    obj_name_full = '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(obj_name, obj_name_base)
    pool_collection = []
    for pool in pools:
        if type(pool) == tuple:
            (pool_name, times) = pool
            times_text = ',NumberOfTimesToSelectFromThisPool=(BaseValueConstant={})'.format(times)
        else:
            pool_name = pool
            times_text = ''
        (_, pool_name_base) = pool_name.rsplit('/', 1)
        pool_name = '{}.{}'.format(pool_name, pool_name_base)
        pool_collection.append('(ItemPool=ItemPoolData\'"{}"\',PoolProbability=(BaseValueConstant=1){})'.format(
            pool_name,
            times_text,
            ))
    mod.reg_hotfix(Mod.CHAR, char_name,
            obj_name_full,
            'DropOnDeathItemPools.ItemPools',
            '({})'.format(','.join(pool_collection)))

# Define new rarity weights.  Note that there's an `ExponentForGrowthRate` row for
# these which presumably defines how the rarities change in certain circumstances.
# Maybe just when you go into Mayhem?  Or maybe they even get better as you level up?
# Anyway, the exponents: 0, 0.3, 0.35, 0.5, 0.8

# Default weights set in the game:
#weights = [100, 5, 0.5, 0.05, 0.001]

# Theoretically Mayhem 1, ish, though I expect that the Mayhem values are more
# modifiers than values
#weights = [7, 7, 40, 50, 35]

# Theoretically "Excellent" Better Loot, ish
#weights = [8, 85, 65, 65, 3]

# Theoretically "Very Good" Better Loot, ish.
# Legendary chance bumped up very slightly, though
# I've used this for 2-3 playthroughs of the game, and in the end there's *too*
# much purple+legendary gear, even in Normal, so I'm bumping it down a bit.
#weights = [15, 35, 25, 13.5, 0.6]

# Fresh weights as of late Feb 2020.
weights = [15, 35, 25, 11.5, 0.3]

mod.header('Base drop weights.')
for (rarity, weight) in zip(
        ['Common', 'Uncommon', 'Rare', 'VeryRare', 'Legendary'],
        weights
        ):
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity.DataTable_ItemRarity',
            rarity,
            'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
            weight)
mod.newline()

# Increase Eridium and cosmetic drop chances (from standard enemies, anyway)
#
# PoolLists which get dropped, and their drop chances:
# (note that the ones with `WithMayhem_Total` in the name will have
# different numbers in mayhem mode)
#
#  0 - Health, /Game/GameData/Loot/ItemPools/Attributes/Att_Health_DropOdds -> anywhere from 0.03 to 0.4?
#  1 - needed ammo, 0.2
#  2 - 'emergency' ammo, /Game/GameData/Loot/ItemPools/Attributes/Att_GunsAndGear_AmmoEmergency -> 0.2
#  3 - money, /Game/GameData/Loot/ItemPools/Attributes/Att_Money_DropOdds -> 0.25
#  4 - Guns, /Game/GameData/Loot/ItemPools/Attributes/Att_GunsAndGear_DropOddsWithMayhem_Total -> 0.09
#  5 - COMs, /Game/GameData/Loot/ItemPools/Attributes/Att_ClassMods_DropOddsWithMayhem_Total -> 0.07 (lol, uses 'shields' constant)
#  6 - Shields, /Game/GameData/Loot/ItemPools/Attributes/Att_Shields_DropOddsWithMayhem_Total -> 0.07
#  7 - Artifacts, /Game/GameData/Loot/ItemPools/Attributes/Att_Artifact_DropOddsWithMayhem_Total -> 0.005
#  8 - Grenades, /Game/GameData/Loot/ItemPools/Attributes/Att_GrenadeMod_DropOddsWithMayhem_Total -> 0.01
#  9 - Cosmetics, /Game/GameData/Loot/ItemPools/Attributes/Att_PlayerHeads_DropOdds -> 0.005
#  10 - Eridium, /Game/GameData/Loot/ItemPools/Attributes/Att_EridiumStick_DropOddsWithMayhem_Total -> 0.008

mod.header('Increased Eridium chances')
for (pool, chars) in [
        ('/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear', [
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
            ]),

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
        ]:

    for char in chars:

        # Eridium.  80%, what the hell.  There's a lot to spend Eridium on.  Default is 0.8% but is modified
        # by Mayhem
        mod.reg_hotfix(Mod.CHAR, char,
                pool,
                'ItemPools[10].PoolProbability',
                BVCF(bvc=0.8))

mod.newline()

# Eridium quantities.  Originally taken from the Week 3 event
# Default during the event was 1.5 (we're using 3)
mod.header('Eridium Drop Quantity Buffs')

# Enemies first.  This is probably not exhaustive, I should go over it at
# some point.
for label, poollist_name, pool_idx, chars in [
        ('Bosses', '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss', 7, [
            'BPChar_AureliaBoss',
            'BPChar_EnforcerKillaVolt',
            'BPChar_Goliath_CageArena',
            'BPChar_HeavyDarkTraunt',
            'BPChar_Heavy_Traunt',
            'BPChar_KJR',
            'BPChar_MechEvilAI',
            'BPChar_NogChipHolder',
            'BPChar_Oversphere_KatagawaSphere',
            'BPChar_PunkSpaceCowboy',
            'BPChar_Varkid_RaidBoss',
            ]),
        ('Terror', '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss_Terror', 2, [
            'BPChar_Terror',
            ]),
        ('Minibosses', '/Game/GameData/Loot/ItemPools/ItemPoolList_MiniBoss', 7, [
            'BPChar_ApeKingBobo',
            'BPChar_EnforcerSacrificeBoss',
            'BPChar_Enforcer_Bounty01',
            'BPChar_Enforcer_Bounty02',
            'BPChar_GoonBounty01',
            'BPChar_GoonMonsterTrucker',
            'BPChar_Goon_Rare01',
            'BPChar_GuardianCube_Spectre',
            'BPChar_GuardianCube_SpectreFinal',
            'BPChar_HeavyDinerBoss',
            'BPChar_HeavyFootstepsOfGiants',
            'BPChar_HeavyJavaCore',
            'BPChar_HeavyLoot',
            'BPChar_Heavy_Bounty01',
            'BPChar_Nog01_Bounty',
            'BPChar_NogBeans',
            'BPChar_PsychoLoot',
            'BPChar_PsychoRare02',
            'BPChar_PsychoRare03',
            'BPChar_PunkBounty02',
            'BPChar_Rakkman',
            'BPChar_Ratch_Hunt01',
            'BPChar_SaurianShiny',
            'BPChar_ServiceBot_LOOT',
            'BPChar_ServiceBot_Rare01',
            'BPChar_SkagAntEater',
            'BPChar_SkagChubby',
            'BPChar_SpiderantCakeRoyalty',
            'BPChar_SpiderantCoffer',
            'BPChar_SpiderantTarantella',
            'BPChar_Spiderant_Hunt01',
            'BPChar_TinkDemon',
            'BPChar_TinkMotorcadeBigD',
            'BPChar_TinkRedJabber',
            'BPChar_VarkidHunt01',
            ]),
        ('Vault Monsters', '/Game/GameData/Loot/ItemPools/ItemPoolList_VaultBossEnemy', 7, [
            'BPChar_EdenBoss',
            'BPChar_FinalBoss',
            'BPChar_Rampager',
            'BPChar_TroyBoss',
            ]),
        ('Anointed Enemies', '/Game/GameData/Loot/ItemPools/ItemPoolList_AnointedEnemyGunsGear', 4, [
            'BPChar_EnforcerAnointed',
            'BPChar_Goliath_Anointed',
            'BPChar_Goliath_Elemental',
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

    mod.comment(label)
    for char_name in chars:
        mod.reg_hotfix(Mod.CHAR, char_name,
                poollist_name,
                'ItemPools.ItemPools[{}].NumberOfTimesToSelectFromThisPool.BaseValueScale'.format(pool_idx),
                3)
    mod.newline()

# The old week 3 event used 1.5 for the scale, I'm bumping it to 5.
mod.comment('Slaughters')
for level_name in [
        'COVSlaughter_P',
        'CreatureSlaughter_P',
        'TechSlaughter_P',
        ]:
    mod.reg_hotfix(Mod.LEVEL, level_name,
            '/Game/GameData/Loot/ItemPools/ItemPoolList_SlaughterMoney',
            'ItemPools.ItemPools[7].NumberOfTimesToSelectFromThisPool.BaseValueScale',
            5)
mod.newline()

# Eridium crystal growths (I think).  Event scale was 1.5, using 3 here.
mod.comment('Eridium Crystal Growths')
for pool_name in [
        '/Game/GameData/Loot/ItemPools/Eridium/ItemPool_EridiumCrystal',
        '/Game/GameData/Loot/ItemPools/Eridium/ItemPool_EridiumCrystal_Large',
        ]:
    mod.reg_hotfix(Mod.PATCH, '',
            pool_name,
            'Quantity.BaseValueScale',
            3)
mod.newline()

# Guaranteed boss drops!
mod.header('DataTable-Based Guaranteed Boss Drop Statements')

# Associating entries from Table_LegendarySpecificLootOdds with characters.  These
# ones seem to be referenced, but the chars in question don't actually drop anything
# specific (though I haven't doublechecked that myself).
#
# Antalope,Antalope,BPChar_Spiderant_Hunt01
# Shiv,Shiv,BPChar_PsychoBadassPrologue
# Red Rain,TechSlaughterBoss,BPChar_GiganticMech1
# Blue Fire,TechSlaughterBoss,BPChar_GiganticMech2

# This var is referenced by Pain's `BPChar_Terror` (I know, it's weird), but we're
# axing it out of that object since the relevant pools are also dropped elsewhere,
# and I don't want them doubling up.
#('Pain', 'Terror', 'BPChar_Terror'),

# In terms of loot drops specifically, Katagawa Jr. is actually BPChar_KJR
# This one might be more useful for other things though?  Perhaps KJR is
# only the death-animated one?
#
# Katagawa Jr.,KatagawaJr,BPChar_KatagawaJR

# Rows which don't seem to be referenced anywhere (at least under /Enemies)
#
# BigFoot,
# CoVSlaughterBoss,
# CreatureSlaughterBoss,
# Cyranid,
# ElDragonJunior,  <- I think El Dragon Jr might use "RoadDog"
# Guardian,
# HopperSwarmer,
# RaidBoss,
# RaidMiniBoss1,
# RaidMiniboss2,
# RaidMiniboss3,
# SirenSkag,
# TrialBoss1,
# TrialBoss2,
# TrialBoss3,
# TrialBoss4,
# TrialBoss5,
# TrialBoss6,
# TrialBoss7,
# TrialBoss8,
# Verminvorous,

# Now on to the ones we're reasonably sure of (this still needs testing)
for (label, row_name, char_name) in [
        ('Anointed Alpha', 'AnnointedJoe', 'BPChar_AnointedJoe'),
        ('Atomic', 'SylestroAndAtomic', 'BPChar_Trooper_Bounty01'),
        ('Aurelia', 'Aurelia', 'BPChar_AureliaBoss'),
        ('Baron Noggin', 'BaronNoggin', 'BPChar_Nog01_Bounty'),
        ('Blinding Banshee', 'BlindingBanshee', 'BPChar_Nekrobug_Hunt01'),
        ('Borman Nates', 'BoremanNates', 'BPChar_PsychoRare02'),
        ('Chonk Stomp', 'ChonkStomp', 'BPChar_Saurian_Hunt01'),
        ('Chupacabratch', 'Chupacabratch', 'BPChar_Ratch_Hunt01'),
        ('Crawley Family (Cybil)', 'LavenderCrawly', 'BPChar_VarkidHunt02_LarvaA'),
        ('Crawley Family (Edie)', 'LavenderCrawly', 'BPChar_VarkidHunt02_LarvaB'),
        ('Crawley Family (Martha)', 'LavenderCrawly', 'BPChar_VarkidHunt02_LarvaC'),
        ('Crawley Family (Matty)', 'LavenderCrawly', 'BPChar_VarkidHunt02_LarvaD'),
        ('Crushjaw', 'Crushjaw', 'BPChar_GoonBounty01'),
        ('DJ Deadsk4g', 'DJBlood', 'BPChar_Enforcer_Bounty02'),
        # I don't think this is used...
        #('Demoskaggon', 'DemoSkag', 'BPChar_Skag_Rare01'),
        ('Dinklebot', 'Dinklebot', 'BPChar_OversphereRare01'),
        # I don't think these are used...
        #('Force Trooper Citrine', 'PowerTroopers', 'BPChar_Trooper_Rare01b'),
        #('Force Trooper Onyx', 'PowerTroopers', 'BPChar_Trooper_Rare01a'),
        #('Force Trooper Ruby', 'PowerTroopers', 'BPChar_Trooper_Rare01c'),
        #('Force Trooper Sapphire', 'PowerTroopers', 'BPChar_Trooper_Rare01e'),
        #('Force Trooper Tourmaline', 'PowerTroopers', 'BPChar_Trooper_Rare01d'),
        ('GenIVIV', 'GeneVIV', 'BPChar_MechEvilAI'),
        ('Gigamind', 'Gigamind', 'BPChar_NogChipHolder'),
        ('Graveward', 'Graveward', 'BPChar_EdenBoss'),
        ('Handsome Jackie', 'HandsomeJackie', 'BPChar_PunkBounty02'),
        ('Heckle', 'HeckleAndHyde', 'BPChar_Goliath_Bounty01'),
        ('Hot Karl', 'Roadblock', 'BPChar_Enforcer_Bounty01'),
        ('I\'m Rakkman', 'Rakkman', 'BPChar_Rakkman'),
        # Don't think this is used...
        #('Indo Tyrant', 'IndoTyrant', 'BPChar_Saurian_Rare01'),
        ('Jabbermogwai', 'Jabbermogwai', 'BPChar_Ape_Hunt01'),
        ('Judge Hightower', 'JudgeHightower', 'BPChar_AtlasSoldier_Bounty01'),
        ('Katagawa Ball', 'KatagawaBall', 'BPChar_Oversphere_KatagawaSphere'),
        ('Katagawa Jr.', 'KatagawaJr', 'BPChar_KJR'),
        ('Killavolt', 'KillaVolt', 'BPChar_EnforcerKillavolt'),
        ('Lagromar', 'TinkDemon', 'BPChar_TinkDemon'),
        ('Manvark', 'Mothman', 'BPChar_VarkidHunt01'),
        ('Maxitrillion', 'Maxitrillion', 'BPChar_ServiceBot_Rare01'),
        ('Mouthpiece', 'Mouthpiece', 'BPChar_EnforcerSacrificeBoss'),
        ('One Punch', 'OnePunch', 'BPChar_OnePunch'),
        ('Phoenix', 'Phoenix', 'BPChar_Rakk_Hunt01'),
        ('Princess Tarantella II', 'Tarantella', 'BPChar_SpiderantTarantella'),
        ('Private Beans', 'Beans', 'BPChar_NogBeans'),
        ('Psychobillies (Billee)', 'GoreGirls', 'BPChar_Punk_Bounty01d'),
        ('Psychobillies (Billi)', 'GoreGirls', 'BPChar_Punk_Bounty01c'),
        ('Psychobillies (Billie)', 'GoreGirls', 'BPChar_Punk_Bounty01b'),
        ('Psychobillies (Billy)', 'GoreGirls', 'BPChar_Punk_Bounty01a'),
        ('Road Dog', 'RoadDog', 'BPChar_Goliath_Rare02'),
        ('Skrakk', 'Skrakk', 'BPChar_Rakk_HuntSkrakk'),
        ('Sky Bully', 'SkyBullies', 'BPChar_Tink_Bounty01'),
        ('Sloth', 'CaptainThunkandSloth', 'BPChar_Goon_Rare01'),
        ('Sylestro', 'SylestroAndAtomic', 'BPChar_Heavy_Bounty01'),
        ('The Unstoppable', 'TheUnstoppable', 'BPChar_Goliath_Rare01'),
        ('Tyreen the Destroyer', 'TyreenFinalBoss', 'BPChar_FinalBoss'),
        ('Urist McEnforcer', 'EnforcerUrist', 'BPChar_EnforcerUrist'),
        ('Warden', 'Warden', 'BPChar_Goliath_CageArena'),
        ('Wick', 'VicandWarty', 'BPChar_PsychoRare03'),
        ]:

    mod.comment(label)
    set_legendary_odds(mod, char_name, row_name, 1)
    mod.newline()

# Maliwan Takedown Bosses
# These should be hotfixable with a LEVEL on Raid_P, rather than having to do it by character,
# but IMO it's not worth the re-test.
for (label, row_name, char_name) in [
        ('Wotan the Invincible', 'RaidBoss', 'BPChar_BehemothRaid'),
        ("Wotan's Brain", 'RaidBoss', 'BPChar_SpiderBrain'),
        ("Wotan's Better Half", 'RaidBoss', 'BPChar_UpperHalf'),
        ('Valkyrie Squad', 'MiniBoss', 'BPChar_MechRaidBossBar'),
        ]:

    mod.comment(label)
    set_legendary_odds(mod, char_name, row_name, 1, obj_name='/Game/PatchDLC/Raid1/GameData/Loot/Table_Legendary_SpecificLootOdds_Raid1.Table_Legendary_SpecificLootOdds_Raid1')
    mod.newline()

# DLC1 (Dandelion; Moxxi's Heist) drop rates
for (label, row_name, char_name) in [
        ('DEGEN-3', 'Kill_Degen3', 'BPChar_LoaderBadass_Venchy'),
        ('Evil St. Lawrence', 'Kill_StLawrence', 'BPChar_EnforcerBadass_Lawrence'),
        ('Fabricator', 'Fabricator', 'BPChar_FabrikatorBasic'),
        ('Freddie the Traitor', 'Freddie', 'BPChar_TraitorEddie'),
        ('Gorgeous Armada', 'Kill_GorgeousArmada', 'BPChar_TinkBadass_Giorgio'),
        ("Jackpot the Jack's Bot", 'Jackbot', 'BPChar_JackBot'), # Three items in this pool!
        ('Scraptrap Prime', 'ScraptrapPrime', 'BPChar_ClaptrapQueen'), # Two items in this pool!

        # Loco Chantelle and Junpai Goat Eater seem to be using each other's pools, weirdly.
        ('Loco Chantelle', 'Kill_GoatEater', 'BPChar_GoonBadass_Coco'),
        ('Junpai Goat Eater', 'Kill_LocoChantelle', 'BPChar_PunkBadass_Gaudy'),
        ]:

    mod.comment(label)
    set_legendary_odds(mod, char_name, row_name, 1, obj_name='/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/Table_Legendary_SpecificLootOdds_Dandelion.Table_Legendary_SpecificLootOdds_Dandelion')
    mod.newline()

mod.header('Extra Guaranteed Boss Drop Statements')

# Set Mouthpiece's "/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All.ItemPool_Guns_All" drop to zero-weight
mod.comment('Mouthpiece')
mod.reg_hotfix(Mod.CHAR, 'BPChar_EnforcerSacrificeBoss',
        '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/ItemPool/ItemPool_EnforcerSacrificeBoss_Shotgun.ItemPool_EnforcerSacrificeBoss_Shotgun',
        'BalancedItems[1].Weight',
        '(BaseValueConstant=0.000000)')
mod.newline()

# Adding Legendary COM to Pain/Terror/A9k, which was in the Week 1 event.  Also doing some
# housekeeping on these pools so that they work exactly how I want.

# So here's the deal with Pain/Terror/Agonizer9k drops:
#
#    1) Internally, Pain and Terror are backwards namingwise.  Any object referencing "Terror" actually
#       applies to Pain, and vice-versa.  This makes data inspection very fun.
#
#    2) Terror drops from `ItemPoolList_Boss_Pain`, which includes ItemPool_Pain_Loot by default, at
#       index 3
#
#    3) Pain drops from `ItemPoolList_Boss_Terror`, which includes ItemPool_Agonizer1500_Terror
#       because of a GBX hotfix, which ends up at index 3 (SparkCharacterLoadedEntry437)
#
#       3a) If you're altering ItemPoolList_Boss_Terror in any way, make sure to use BPChar_Terror
#           as the hotfix key, otherwise that GBX hotfix might not fire, since they use the prev-value
#           field.  Using BPChar_Agonizer_9k, for instance, causes the GBX hotfix to fail because
#           BPChar_Agonizer_9k is apparently loaded before BPChar_Terror.
#
#    4) Pain's DropOnDeathItemPools (in `BPChar_Terror`, remember) also includes
#       ItemPool_Agonizer1500_Terror, so technically he could drop from that pool twice.
#
#    5) Agonizer9k drops from both `ItemPoolList_Boss_Pain` and `ItemPoolList_Boss_Terror`
#
#    6) Both ItemPool_Pain_Loot and ItemPool_Agonizer1500_Terror get expanded by ItemPoolExpansion
#       objects.
#
#       6a) ItemPool_Pain_Loot (Terror's drops):
#           - Agonizer 1500 (base pool)
#           - Dicatator (from expansion)
#           - White Elephant (from expansion)
#
#       6b) ItemPool_Agonizer1500_Terror (Pain's drops, can drop twice from Pain himself (but not from A9k)):
#           - Agonizer 1500 (base pool)
#           - Damned (from expansion)
#           - Loaded Dice (from expansion)
#           - Crader's EM-P5 (M4-only) (from expansion)
#
# So that's the vanilla situation; we're modifying that a bit for our own purposes here.

# Guaranteed drops
mod.comment('Terror Guaranteed Drop (and also half of Agonizer 9000\'s drops)')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Agonizer_9k',
        '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss_Pain',
        'ItemPools.ItemPools[3].PoolProbability.BaseValueConstant',
        1)
mod.newline()
mod.comment('Pain Guaranteed Drop (and also half of Agonizer 9000\'s drops)')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Terror',
        '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss_Terror',
        'ItemPools.ItemPools[3].PoolProbability.BaseValueConstant',
        1)
mod.newline()

# De-weight the Agonizer 1500 drop a bit, so it's less likely to come up twice
# (Terror's is below)
mod.comment('De-weight Agonizer 1500 a bit')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Terror',
        '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Agonizer1500_Terror',
        'BalancedItems.BalancedItems[0].Weight',
        BVCF(bvc=0.5))
mod.newline()

# Remove Crader's EM-P5 M4 requirement
mod.comment('Remove Crader\'s EM-P5 M4 Requirement')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Terror',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Agonizer1500_Terror',
        'BalancedItems.BalancedItems[2].Weight',
        BVCF())
mod.newline()

# Remove the specific ItemPool_Agonizer1500_Terror reference in Pain's DropOnDeathItemPool,
# since it's included in ItemPoolList_Boss_Terror thanks to GBX hotfix SparkCharacterLoadedEntry437.
# We'd otherwise drop from that pool twice.
mod.comment('Remove doubled Pain drop')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Terror',
        '/Game/Enemies/Enforcer/_Unique/Terror/_Design/Character/BPChar_Terror.BPChar_Terror_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
        BVCF(bvc=0))
mod.newline()

# Add the COM drop
mod.comment('Add Legendary COM to Terror')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Agonizer_9k',
        '/Game/Enemies/Tink/_Unique/Pain/_Design/Character/ItemPool_Pain_Loot.ItemPool_Pain_Loot',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror.Balance_HW_COV_Terror,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror.Balance_HW_COV_Terror"',
                Weight=(BaseValueConstant=0.5)
            ),
            (
                ItemPoolData=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary.ItemPool_ClassMods_05_Legendary"',
                Weight=(BaseValueConstant=1)
            )
        )
        """)
mod.newline()

# Katagawa Jr.  Adding in the Legendary COM chance from the Week 1 event.  Note that
# the MH4/MT patch also adds in Crossroad, so there's three total drops in here.
mod.comment('Katagawa Jr.')
mod.reg_hotfix(Mod.CHAR, 'BPChar_KJR',
        '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Storm_Katagawa.ItemPool_Storm_Katagawa',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm"',
                Weight=(BaseValueConstant=1)
            ),
            (
                ItemPoolData=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary.ItemPool_ClassMods_05_Legendary"',
                Weight=(BaseValueConstant=1)
            )
        )
        """)
mod.reg_hotfix(Mod.CHAR, 'BPChar_KJR',
        '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Storm_Katagawa.ItemPool_Storm_Katagawa',
        'Quantity',
        '(BaseValueConstant=3)')
mod.newline()

# Graveward!  Adding in the Earworm from the Week 1 event.  Note that
# the MH4/MT patch brings the total item count to 5.
mod.comment('Graveward')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Loot/ItemPools/Unique/ItemPool_GraveandWard_Graveward.ItemPool_GraveandWard_Graveward',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/Grave/Balance/InvBalD_Artifact_Grave.InvBalD_Artifact_Grave,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/Grave/Balance/InvBalD_Artifact_Grave.InvBalD_Artifact_Grave"',
                Weight=(BaseValueConstant=0.500000)
            ),
            (
                InventoryBalanceData=/Game/Gear/Shields/_Design/_Uniques/Ward/Balance/InvBalD_Shield_Ward.InvBalD_Shield_Ward,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/Gear/Shields/_Design/_Uniques/Ward/Balance/InvBalD_Shield_Ward.InvBalD_Shield_Ward"',
                Weight=(BaseValueConstant=0.500000)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Earworm/Balance/Balance_DAL_AR_Earworm.Balance_DAL_AR_Earworm,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Earworm/Balance/Balance_DAL_AR_Earworm.Balance_DAL_AR_Earworm"',
                Weight=(BaseValueConstant=0.500000)
            )
        )
        """)
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Loot/ItemPools/Unique/ItemPool_GraveandWard_Graveward.ItemPool_GraveandWard_Graveward',
        'Quantity',
        '(BaseValueConstant=5)')
mod.newline()

# Guaranteed drop from Troy (this may actually already be the default -- it looks like
# the Week 1 event actually *nerfed* his drop.)
mod.comment('Troy')
mod.reg_hotfix(Mod.CHAR, 'BPChar_TroyBoss',
        '/Game/NonPlayerCharacters/Troy/_TheBoss/_Design/Character/BPChar_TroyBoss.BPChar_TroyBoss_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
        BVCF())
mod.newline()

# The Rampager.  A currently-active hotfix sets the scale to 0.2; in the past the BVC has been
# set weirdly as well.  Just set the whole PoolProbability attribute and be done with it.
mod.comment('The Rampager')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Rampager',
        '/Game/Enemies/PrometheaBoss/Rampager/_Design/Character/BPChar_Rampager.BPChar_Rampager_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
        BVCF())
mod.newline()

# Billy, the Anointed - set the ItemPool_Guns_All drop to zero-weight
mod.comment('Billy, the Anointed')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Goliath_Anointed',
        '/Game/GameData/Loot/ItemPools/Unique/ItemPool_LeadSprinkler_AnointedIntro.ItemPool_LeadSprinkler_AnointedIntro',
        'BalancedItems[1].Weight',
        '(BaseValueConstant=0.000000)')
mod.newline()

# Captain Haunt (from the Bloody Harvest event)
# (a GBX-provided hotfix against this table doesn't require any char-based hotfixes)
# TODO: This is definitely not working.  Also he should really have a quantity/numtimes defined
mod.comment('Captain Haunt (untested)')
mod.table_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/BloodyHarvest/GameData/Balance/BloodyHarvest/DataTable_Season_Halloween.DataTable_Season_Halloween',
        'HarvestBoss_LootDropChance',
        'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
        1)
mod.newline()

# Red Jabber - Add in legendary grenade, as the Week 2 event did.
mod.comment('Red Jabber')
mod.reg_hotfix(Mod.CHAR, 'BPChar_TinkRedJabber',
        '/Game/Enemies/Tink/_Unique/RedJabber/_Design/Character/BPChar_TinkRedJabber.BPChar_TinkRedJabber_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=((ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary.ItemPool_GrenadeMods_05_Legendary"',PoolProbability=(BaseValueConstant=1.000000))),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_MiniBoss.ItemPoolList_MiniBoss"')
        )""")
mod.newline()

# Psychobillies!  A set of official hotfixes from GBX clears out the drop pools for
# all but one of the Psychobillies.  That won't do!  Reinstate those (we're just
# going to set it for all four, to be sure.
mod.comment('Psychobillies')
for letter in ['a', 'b', 'c', 'd']:
    mod.reg_hotfix(Mod.CHAR, 'BPChar_Punk_Bounty01{}'.format(letter),
            '/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/{}/BPChar_Punk_Bounty01{}.BPChar_Punk_Bounty01{}_C:AIBalanceState_GEN_VARIABLE'.format(letter, letter, letter),
            'DropOnDeathItemPools.ItemPools',
            """
            (
                (
                    ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Unique/ItemPool_ElectricBanjo_GoreGirls.ItemPool_ElectricBanjo_GoreGirls"',
                    PoolProbability=(
                        DataTableValue=(
                            DataTable=DataTable'"/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds.Table_LegendarySpecificLootOdds"',
                            RowName="GoreGirls",
                            ValueName="LegendaryDropChance_Playthrough2_50_11E6C8E8493E0A73AF9B35891E7CE111"
                        )
                    )
                )
            )
            """)
mod.newline()

# Loot O' Gram (obviously not a boss, but them's the breaks)
# The first item in the pool is a "common" gun drop, the rest are the uniques
mod.comment("Loot O' Gram")
mod.reg_hotfix(Mod.LEVEL, 'Sanctuary3_P',
        '/Game/GameData/Loot/ItemPools/Unique/ItemPool_LootOGram_ConvertedToGuns.ItemPool_LootOGram_ConvertedToGuns',
        'BalancedItems[0].Weight.BaseValueConstant',
        0)
mod.newline()

# Dinklebot -- this ordinarily drops the Loot O' Gram item itself, which must be
# turned in to Earl in order to get loot, but I'm going to also change it to
# dump from the Earl pool itself (assuming that the pool is loaded in Skywell-27;
# I'll have to check that)
mod.comment('Dinklebot')
set_death_pools(mod, 'BPChar_OversphereRare01',
        '/Game/Enemies/Oversphere/_Unique/Rare01/_Design/Character/BPChar_OversphereRare01',
        pools=[
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_LootOGram_ConvertedToGuns', 3),
            ],
        )
mod.newline()

# Some more guaranteed drops which were taken from the Week 2 event
for (label, bpchar, obj_name) in [
        ('Urist McEnforcer', 'BPChar_EnforcerUrist', '/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/BPChar_EnforcerUrist.BPChar_EnforcerUrist_C:AIBalanceState_GEN_VARIABLE'),
        ('The Unstoppable', 'BPChar_Goliath_Rare01', '/Game/Enemies/Goliath/_Unique/Rare01/Character/BPChar_Goliath_Rare01.BPChar_Goliath_Rare01_C:AIBalanceState_GEN_VARIABLE'),
        ('Road Dog', 'BPChar_Goliath_Rare02', '/Game/Enemies/Goliath/_Unique/Rare02/_Design/Character/BPChar_Goliath_Rare02.BPChar_Goliath_Rare02_C:AIBalanceState_GEN_VARIABLE'),
        ('El Dragon Jr.', 'BPChar_Goliath_Rare03', '/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03.BPChar_Goliath_Rare03_C:AIBalanceState_GEN_VARIABLE'),
        ('Sloth', 'BPChar_Goon_Rare01', '/Game/Enemies/Goon/_Unique/Rare01/_Design/Character/BPChar_Goon_Rare01.BPChar_Goon_Rare01_C:AIBalanceState_GEN_VARIABLE'),
        ('Borman Nates', 'BPChar_PsychoRare02', '/Game/Enemies/Psycho_Male/_Unique/Rare02/_Design/Character/BPChar_PsychoRare02.BPChar_PsychoRare02_C:AIBalanceState_GEN_VARIABLE'),
        ('Wick', 'BPChar_PsychoRare03', '/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03.BPChar_PsychoRare03_C:AIBalanceState_GEN_VARIABLE'),
        ("I'm Rakkman", 'BPChar_Rakkman', '/Game/Enemies/Psycho_Male/_Unique/Rakkman/_Design/Character/BPChar_Rakkman.BPChar_Rakkman_C:AIBalanceState_GEN_VARIABLE'),
        ('Maxitrillion', 'BPChar_ServiceBot_Rare01', '/Game/Enemies/ServiceBot/_Unique/Rare01/_Design/Character/BPChar_ServiceBot_Rare01.BPChar_ServiceBot_Rare01_C:AIBalanceState_GEN_VARIABLE'),
        ('Princess Tarantella II', 'BPChar_SpiderantTarantella', '/Game/Enemies/Spiderant/_Unique/Tarantella/_Design/Character/BPChar_SpiderantTarantella.BPChar_SpiderantTarantella_C:AIBalanceState_GEN_VARIABLE'),
        ]:
    mod.comment(label)
    mod.reg_hotfix(Mod.CHAR, bpchar,
            obj_name,
            'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
            BVCF())
    mod.newline()

# Mayhem 4 / Maliwan Takedown additions, using the CharacterItemPoolExpansions_Raid1 object
for char_name, idx, num in [
        ('Aurelia', 42, 2),
        ('Holy Dumptruck', 43, 1),
        ('Mouthpiece', 44, 2),
        # Sylestro spawns with Atomic, reducing this from 3 to 2
        ('Sylestro', 50, 2),
        ('Captain Traunt', 51, 3),
        ('General Traunt', 52, 3),
        ('Billy, The Anointed', 53, 3),
        ('Brood Mother', 55, 3),
        ('Antalope', 63, 3),
        ('Warty', 64, 2),
        ('Captain Thunk', 65, 2),
        ('Troy Calypso', 72, 2),

        # Slaughters
        ('Tremendous Rex', 59, 2),
        ('Mr. Titan', 47, 4),
        ('Red Rain', 45, 2),
        ('Blue Fire', 46, 2),

        # Trials (all legendary COMs)
        ('Hag of Fervor', 48, 3),
        ('Sera of Supremacy', 49, 4),
        ('Arbalest of Discipline', 54, 5),
        ('Tyrant of Instinct', 60, 4),
        ('Skag of Survival', 62, 3),
        ('Tink of Cunning', 66, 4),

        ]:
    # This object's available right from the main menu no need to do CHAR-based
    # hotfixes with it.
    mod.comment(char_name)
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
            'CharacterExpansions.CharacterExpansions_Value[{}].DropOnDeathItemPools[0].PoolProbability'.format(idx),
            BVCF())
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
            'CharacterExpansions.CharacterExpansions_Value[{}].DropOnDeathItemPools[0].NumberOfTimesToSelectFromThisPool.BaseValueConstant'.format(idx),
            num)
    mod.newline()

# M4/MT additions which we're adding to or altering in some way
for char_name, idx, pools in [
        # Keeping the week 2 guaranteed-cosmetic on here
        ('Indo Tyrant', 58, [
            Pool('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_IndoTyrant', num=3),
            Pool('/Game/GameData/Loot/ItemPools/ItemPool_SkinsAndMisc'),
            ]),
        # Two Demoskaggons spawn at once, so we're dropping the quantities from what we'd ordinarily do
        ('Demoskaggon', 61, [
            Pool('/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary', probability=0.5),
            Pool('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_DemoSkaggon', num=2),
            ]),
        # Keeping the week 2 Legendary Artifact drop
        ('Mother of Grogans', 73, [
            Pool('/Game/Enemies/Punk_Female/_Unique/MotherOfDragons/_Design/Loot/ItemPool_MotherOfDragons_Loot'),
            Pool('/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_05_Legendary'),
            ]),
        # Power Troopers - adding in the Week 2 legendary COMs - keeping the drop count for the
        # additional pools at 1, though, since there's so many legendaries even at that level.
        ('Black Force Trooper (Onyx)', 67, [
            Pool('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper01'),
            Pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster_05_Legendary'),
            ]),
        ('Yellow Force Trooper (Citrine)', 68, [
            Pool('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper01'),
            Pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner_05_Legendary'),
            ]),
        ('Red Force Trooper (Ruby)', 69, [
            Pool('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper01'),
            Pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative_05_Legendary'),
            ]),
        ('Pink Force Trooper (Tourmaline)', 70, [
            Pool('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper02'),
            Pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Siren_05_Legendary'),
            ]),
        ('Sapphire Force Trooper (Sapphire)', 71, [
            Pool('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper02'),
            Pool('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary'),
            ]),
        ]:
    mod.comment(char_name)
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
            'CharacterExpansions.CharacterExpansions_Value[{}].DropOnDeathItemPools.ItemPools'.format(idx),
            '({})'.format(','.join([str(pool) for pool in pools])))
    mod.newline()

# Since the MH4/MT patch, a lot of bosses have 2+ items in their drop pools.  Fix those up
# so that they drop N items to match, like Better Loot has historically done
mod.header_lines(['Drop Pool Quantity Tweaks', '(some of the above statements include some quantity fixes as well)'])

for (label, char_name, pool, quantity) in [

        # TODO: *really* the right way to do these in BL3 would be via the NumberOfTimesToSelectFromThisPool
        # attr in the DropOnDeathItemPools structure, rather than Quantity in the ItemPool itself.  Since we
        # can't serialize BPChar objects yet, though, constructing equivalent statements without guesswork
        # would involve a lot of painful console `getall` shenanigans, which hardly seems worth it.

        # Handled already elsewhere in the mod:
        #  * Graveward
        #  * Katagawa Jr.
        #  * Agonizer 9000 (and, I guess, Pain+Terror.  Whatever.  They're too complex to bother with.)
        # Don't increase the count on this one - there's four in the pool now, but also four of the Psychobillies.
        # So it evens out.
        #('Psychobillies (Billy)', 'BPChar_Punk_Bounty01a', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_ElectricBanjo_GoreGirls.ItemPool_ElectricBanjo_GoreGirls', 4),
        ('Anointed Alpha', 'BPChar_AnointedJoe', '/Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/ItemPools/ItemPool_AnointedJoe.ItemPool_AnointedJoe', 3),
        ('Jabbermogwai', 'BPChar_Ape_Hunt01', '/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/ItemPool_Ape01_Hunt.ItemPool_Ape01_Hunt', 3),
        ('Judge Hightower', 'BPChar_AtlasSoldier_Bounty01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Sabre_JudgeHightower.ItemPool_Sabre_JudgeHightower', 3),
        ('Hot Karl', 'BPChar_Enforcer_Bounty01', '/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/ItemPool_Enforcer_Bounty01.ItemPool_Enforcer_Bounty01', 4),
        ('DJ Deadsk4g', 'BPChar_Enforcer_Bounty02', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Thumper_DJBlood.ItemPool_Thumper_DJBlood', 3),
        ('Killavolt', 'BPChar_EnforcerKillavolt', '/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Weapon/ItemPool_KillaVolt_Ninevolt.ItemPool_KillaVolt_Ninevolt', 3),
        ('Urist McEnforcer', 'BPChar_EnforcerUrist', '/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/ItemPool_EnforcerUrist.ItemPool_EnforcerUrist', 3),
        ('Tyreen the Destroyer', 'BPChar_FinalBoss', '/Game/Enemies/FinalBoss/_Shared/_Design/LootPools/ItemPool_FinalBoss_KingsCall.ItemPool_FinalBoss_KingsCall', 3),
        ('Heckle', 'BPChar_Goliath_Bounty01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Pestilence_HeckleandHyde.ItemPool_Pestilence_HeckleandHyde', 3),
        ('Warden', 'BPChar_Goliath_CageArena', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Freeman_Warden.ItemPool_Freeman_Warden', 3),
        ('The Unstoppable', 'BPChar_Goliath_Rare01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool__BandsofSytorak_Unstoppable.ItemPool__BandsofSytorak_Unstoppable', 3),
        ('Road Dog', 'BPChar_Goliath_Rare02', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Redliner_Roaddog.ItemPool_Redliner_Roaddog', 3),
        ('El Dragon Jr.', 'BPChar_Goliath_Rare03', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_UnleashTheDragon_ElDragonJr.ItemPool_UnleashTheDragon_ElDragonJr', 3),
        ('Crushjaw', 'BPChar_GoonBounty01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_BoneShredder_Crushjaw.ItemPool_BoneShredder_Crushjaw', 3),
        ('Sloth', 'BPChar_Goon_Rare01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Piss_ThunkandSloth.ItemPool_Piss_ThunkandSloth', 2),
        ('GenIVIV', 'BPChar_MechEvilAI', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_MessyBreakup_GeneVIV.ItemPool_MessyBreakup_GeneVIV', 4),
        ('Blinding Banshee', 'BPChar_Nekrobug_Hunt01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Shriek_DevilBug.ItemPool_Shriek_DevilBug', 3),
        ('Baron Noggin', 'BPChar_Nog01_Bounty', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_EMPGrenade_BaronNoggin.ItemPool_EMPGrenade_BaronNoggin', 2),
        ('Private Beans', 'BPChar_NogBeans', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Westergun_TheBoo.ItemPool_Westergun_TheBoo', 3),
        ('Gigamind', 'BPChar_NogChipHolder', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Spidermind_Gigamind.ItemPool_Spidermind_Gigamind', 3),
        ('One Punch', 'BPChar_OnePunch', '/Game/Enemies/Psycho_Male/_Unique/OnePunch/Design/Loot/ItemPool_OnePunch.ItemPool_OnePunch', 2),
        ('Katagawa Ball', 'BPChar_Oversphere_KatagawaSphere', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Tsunami_KatagawaBall.ItemPool_Tsunami_KatagawaBall', 3),
        ('Borman Nates', 'BPChar_PsychoRare02', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_PsychoStabber_BormanNates.ItemPool_PsychoStabber_BormanNates', 3),
        ('Wick', 'BPChar_PsychoRare03', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Portals_VicAndWarty.ItemPool_Portals_VicAndWarty', 2),
        ('Handsome Jackie', 'BPChar_PunkBounty02', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_NimbleJack_HandsomeJackie.ItemPool_NimbleJack_HandsomeJackie', 3),
        ('Phoenix', 'BPChar_Rakk_Hunt01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_PhoenixTears_Phoenix.ItemPool_PhoenixTears_Phoenix', 3),
        ('Skrakk', 'BPChar_Rakk_HuntSkrakk', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Skeksis_Skrakk.ItemPool_Skeksis_Skrakk', 2),
        ("I'm Rakkman", 'BPChar_Rakkman', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Rakkman_Rakkman.ItemPool_Rakkman_Rakkman', 3),
        ('Rampager', 'BPChar_Rampager', '/Game/Enemies/PrometheaBoss/_Shared/_Design/LootPools/ItemPool_Rampager_Gun.ItemPool_Rampager_Gun', 4),
        ('Chupacabratch', 'BPChar_Ratch_Hunt01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_BloodSucker_Chupacabratch.ItemPool_BloodSucker_Chupacabratch', 3),
        ('Chonk Stomp', 'BPChar_Saurian_Hunt01', '/Game/Enemies/Saurian/_Unique/Hunt01/_Design/Character/ItemPool_Saurian01_Hunt.ItemPool_Saurian01_Hunt', 3),
        ('Maxitrillion', 'BPChar_ServiceBot_Rare01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Horizon_Maxitrillion.ItemPool_Horizon_Maxitrillion', 3),
        ('Princess Tarantella II', 'BPChar_SpiderantTarantella', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Hive_Tarantella.ItemPool_Hive_Tarantella', 3),
        # Doublecheck that there's not more than one of these at a time, may not want to up the quantity. - yep, can get two at once.  Keeping this at 2, though.
        ('Sky Bully', 'BPChar_Tink_Bounty01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_ShootingStar_SkyBullies.ItemPool_ShootingStar_SkyBullies', 2),
        ('Lagromar', 'BPChar_TinkDemon', '/Game/Enemies/Tink/_Unique/Demon/_Design/Loot/ItemPool_DemonDark_DemonTink_Loot.ItemPool_DemonDark_DemonTink_Loot', 3),
        # Atomic an Sylestro spawn at the same time, reducing this from 4 to 2
        ('Atomic', 'BPChar_Trooper_Bounty01', '/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/ItemPool_Trooper_Bounty01.ItemPool_Trooper_Bounty01', 2),
        # Doublecheck that there's not more than one of these at a time, may not want to up the quantity. - yep, this'll spawn four times, omit it.
        #('Crawley Family', 'BPChar_VarkidHunt02_LarvaA', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_PredatoryLending_CrawlyFamily.ItemPool_PredatoryLending_CrawlyFamily', 2),
        ('Manvark', 'BPChar_VarkidHunt01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Headsplosion_Mothman.ItemPool_Headsplosion_Mothman', 3),

        # There are a *ton* of items that drop from these (15 total for the Valkyries,
        # 19 for Wotan), and you get four total drops from 'em: once from Valkyries
        # and then one for each Wotan part.
        #
        # Going to have each drop provide 3, which is still sort of too much, really,
        # but that'll give you 12 over the course of one run.  You'll need a few
        # runs through to get the complete set.
        #
        # BPChar_BehemothRaid: Wotan the Invincible
        # BPChar_SpiderBrain: Wotan's Brain
        # BPChar_UpperHalf: Wotan's Better Half
        # BPChar_MechRaidBossBar: Valkyrie Squad
        #('Maliwan Takedown Legendaries (possibly not used?)', '', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_Raid1_Legendary.ItemPool_Raid1_Legendary', 3),
        ('Maliwan Takedown Raid Bosses', 'BPChar_BehemothRaid', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool', 3),
        ('Maliwan Takedown Raid Bosses', 'BPChar_SpiderBrain', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool', 3),
        ('Maliwan Takedown Raid Bosses', 'BPChar_UpperHalf', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool', 3),
        ('Maliwan Takedown Raid Minibosses', 'BPChar_MechRaidBossBar', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool.ItemPool_RaidMiniBosses_Pool', 3),

        ]:
    mod.comment(label)
    if char_name == '':
        hf_type = Mod.PATCH
    else:
        hf_type = Mod.CHAR
    mod.reg_hotfix(hf_type, char_name,
            pool,
            'Quantity',
            '(BaseValueConstant={})'.format(quantity),
            )
    mod.newline()

# Newer-style quantity, which everything else should really be using.  Namely,
# NumberOfTimesToSelectFromThisPool.
for (label, bpchar_obj_base, bpchar_name, bpchar_idx, bpchar_qty) in [
        ("Jackpot the Jack's Bot - Legendary Pool",
            '/Dandelion/Enemies/JackBot/_Shared/_Design/Character',
            'BPChar_JackBot',
            0,
            3),
        ("Jackpot the Jack's Bot - Weapon Trinket",
            '/Dandelion/Enemies/JackBot/_Shared/_Design/Character',
            'BPChar_JackBot',
            1,
            1),
        ("Jackpot the Jack's Bot - Room Decoration",
            '/Dandelion/Enemies/JackBot/_Shared/_Design/Character',
            'BPChar_JackBot',
            2,
            1),
        ('Scraptrap Prime',
            'Game/PatchDLC/Dandelion/Enemies/Claptrap/Claptrap_Queen/_Design/Character',
            'BPChar_ClaptrapQueen',
            0,
            2),
        ]:
    mod.comment(label)
    full_obj_name = '{}/{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar_obj_base, bpchar_name, bpchar_name)
    mod.reg_hotfix(Mod.CHAR, bpchar_name,
            full_obj_name,
            'DropOnDeathItemPools.ItemPools[{}].PoolProbability'.format(bpchar_idx),
            """(
                BaseValueConstant=1,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1
            )""")
    mod.reg_hotfix(Mod.CHAR, bpchar_name,
            full_obj_name,
            'DropOnDeathItemPools.ItemPools[{}].NumberOfTimesToSelectFromThisPool'.format(bpchar_idx),
            """(
                BaseValueConstant={},
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1
            )""".format(bpchar_qty))
    mod.newline()

# A few more which can talk right to an ItemPoolList
for (label, bpchar_name, poollist, itempool_idx, drop_qty) in [
        # Yes, this is correct, the object names for Pain/Terror are mismatched.
        ('Pain', 'BPChar_Terror',
            '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss_Terror',
            3,
            4),
        # Could really use BPChar_Pain for this, but whatever.
        ('Terror', 'BPChar_Agonizer_9k',
            '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss_Pain',
            3,
            4),
        ]:
    mod.comment(label)
    mod.reg_hotfix(Mod.CHAR, bpchar_name,
            poollist,
            'ItemPools.ItemPools[{}].NumberOfTimesToSelectFromThisPool'.format(itempool_idx),
            BVCF(bvc=drop_qty))
    mod.newline()

# There's at least one case of gera which doesn't drop evenly, so smooth that out.
mod.header('Drop rate normalization')

mod.comment('Hot Karl')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Enforcer_Bounty01',
        '/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/ItemPool_Enforcer_Bounty01.ItemPool_Enforcer_Bounty01',
        'BalancedItems[1].Weight.BaseValueConstant',
        1)
mod.newline()

# I'm not making these *totally* even, but the BVC in the raw data is 0.25, which is
# too low for my liking.  Also sort of guessing at char references, etc.
mod.comment('Mayhem 4 / Maliwan Takedown Pools')
for idx in range(5, 8):
    # I think this first pool isn't actually referenced by anything, btw.
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_Raid1_Legendary.ItemPool_Raid1_Legendary',
            'BalancedItems[{}].Weight.BaseValueConstant'.format(idx),
            0.75)
    for char_name in [
            'BPChar_BehemothRaid',
            'BPChar_SpiderBrain',
            'BPChar_UpperHalf',
            ]:
        mod.reg_hotfix(Mod.CHAR, char_name,
                '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool',
                'BalancedItems[{}].Weight.BaseValueConstant'.format(idx),
                0.75)
mod.newline()

# Make sure that the Mayhem 4-locked gear is no longer Mayhem 4-locked.
mod.header('Remove Mayhem 4 Gear Restrictions')

for label, char_name, pool, idx in [
        ('Rampager', 'BPChar_Rampager', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Rampager_Gun', 2),
        ('Aurelia', 'BPChar_AureliaBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AureliaBoss', 1),
        ('Mr. Titan', 'BPChar_Goliath_SlaughterBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/Itempool_CoVSlaughterBoss', 3),
        ('Sylestro', 'BPChar_Heavy_Bounty01', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Sylvestro', 2),
        ('Captain Traunt', 'BPChar_Heavy_Traunt', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CaptTraunt', 2),
        ('General Traunt', 'BPChar_HeavyDarkTraunt', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_GenTraunt', 2),
        ('Billy, the Anointed', 'BPChar_MansionBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_MansionBoss', 2),
        ('Arbalest of Discipline', 'BPChar_Mech_TrialBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech', 4),
        ('Tink of Cunning', 'BPChar_Tink_TrialBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink', 3),
        ('Troy Calypso', 'BPChar_TroyBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TroyDedicated', 1),
        ]:
    mod.comment(label)
    mod.reg_hotfix(Mod.CHAR, char_name,
            pool,
            'BalancedItems[{}].Weight'.format(idx),
            BVCF())
    mod.newline()

# Kind of guessing at chars here.
mod.comment('General Maliwan Takedown Mayhem 4 Legendaries Pool')
for idx in range(11):
    for char_name in [
            'BPChar_BehemothRaid',
            'BPChar_SpiderBrain',
            'BPChar_UpperHalf',
            'BPChar_MechRaidBossBar',
            ]:
        mod.reg_hotfix(Mod.CHAR, char_name,
                '/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries.ItemPool_Mayhem4_Legendaries',
                'BalancedItems[{}].Weight'.format(idx),
                """(
                    BaseValueConstant=1,
                    DataTableValue=(DataTable=None,RowName="",ValueName=""),
                    BaseValueAttribute=None,
                    AttributeInitializer=None,
                    BaseValueScale=1
                )""")
mod.newline()

mod.comment('Maliwan Takedown Raid Boss Pool')
for char_name in [
        'BPChar_BehemothRaid',
        'BPChar_SpiderBrain',
        'BPChar_UpperHalf',
        ]:
    mod.reg_hotfix(Mod.CHAR, char_name,
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool',
            'BalancedItems[8].Weight',
            """(
                BaseValueConstant=11,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1
            )""")
mod.newline()

mod.comment('Maliwan Takedown Valkyrie Squad Pool')
mod.reg_hotfix(Mod.CHAR, 'BPChar_MechRaidBossBar',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool.ItemPool_RaidMiniBosses_Pool',
        'BalancedItems[4].Weight',
        """(
            BaseValueConstant=2,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# Buff Anoint Drops
#
# Vanilla values:
#   Normal - PT1: 28, PT2: 16
#   Mayhem 1 - PT1: 16, PT2: 12
#   Mayhem 2 - PT1: 12, PT2: 10
#   Mayhem 3 - PT1: 10, PT2: 6
# Week 4 values:
#   Normal - unchanged
#   Mayhem 1 - PT1: 6, PT2: 4.5
#   Mayhem 2 - PT1: 3, PT2: 1.8
#   Mayhem 3 - PT1: 1, PT2: 0.5
mod.header('Guaranteed Anointments')
for (label, row_name, chance) in [
        ('Regular Play', 'NoneChance', 0),
        ('Mayhem 1', 'NoneChance_Mayhem_01', 0),
        ('Mayhem 2', 'NoneChance_Mayhem_02', 0),
        ('Mayhem 3', 'NoneChance_Mayhem_03', 0),
        ]:
    mod.comment(label)
    for attr_name in [
            'PlaythroughOne',
            'PlaythroughTwoAndBeyond',
            ]:
        mod.table_hotfix(Mod.PATCH, '',
                '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/DataTable_EndGame_DropChance.DataTable_EndGame_DropChance',
                row_name,
                attr_name,
                """(
                    BaseValueConstant={chance},
                    DataTableValue=(DataTable=None,RowName="",ValueName=""),
                    BaseValueAttribute=None,
                    AttributeInitializer=None,
                    BaseValueScale=1
                )""".format(chance=chance))
    mod.newline()

# Bugfixes!
mod.header('Bugfixes')

# Judge Hightower (and his cronies) have data in PlayThroughs[0].DropOnDeathItemPools which override
# the actual pools, and causes them to only drop AR ammo.  Clear that out!  (This was fixed officially
# in GBX's 2020-01-16 hotfix update, though I'm keeping it in here for now because I get an Internet
# Gold Star for figuring it out before GBX.)
mod.comment('Fix Judge Hightower drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_AtlasSoldier_Bounty01',
        '/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01.BPChar_AtlasSoldier_Bounty01_C:AIBalanceState_GEN_VARIABLE',
        'PlayThroughs[0].bOverrideDropOnDeathItemPools',
        'False')
mod.reg_hotfix(Mod.CHAR, 'BPChar_AtlasSoldier_Bounty01',
        '/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01.BPChar_AtlasSoldier_Bounty01_C:AIBalanceState_GEN_VARIABLE',
        'PlayThroughs[0].DropOnDeathItemPools.ItemPools',
        '()')
mod.newline()

mod.comment('Fix Hightower Crew drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_AtlasSoldier_BountyGang',
        '/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_BountyGang.BPChar_AtlasSoldier_BountyGang_C:AIBalanceState_GEN_VARIABLE',
        'PlayThroughs[0].bOverrideDropOnDeathItemPools',
        'False')
mod.reg_hotfix(Mod.CHAR, 'BPChar_AtlasSoldier_BountyGang',
        '/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_BountyGang.BPChar_AtlasSoldier_BountyGang_C:AIBalanceState_GEN_VARIABLE',
        'PlayThroughs[0].DropOnDeathItemPools.ItemPools',
        '()')
mod.newline()

# Lilith's chest on Sanctuary doesn't actually *guarantee* legendaries because GBX doesn't
# realize that 0 is a number too.  The chances of a non-legendary are super slim, but FDH
# got a bit of white gear there once, so it's possible.  (Default modifiers for these are 1,
# while the legendary modifier is 5000000.)
mod.comment('Ensure legendaries in Lilith\'s game-end chest')
for col in [
        'CommonWeightModifier_21_3D483428462299E5B6AF02B6CC0F65CC',
        'UncommonWeightModifier_12_A1CB19B648A9D93482D9DC83713A2FB5',
        'RareWeightModifier_16_F11E138D458B57D473F062A6C52A5F58',
        'VeryRareWeightModifier_17_8A0A186D4D4FC53ADDFB71A8A7F589DA',
        ]:
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/GameData/Loot/RarityWeighting/DataTable_Lootable_BalanceData',
            'LilithEndChest',
            col,
            0)
mod.newline()

# Just some testing stuff at the end of the file, to make sure that the game
# is parsing all the way to the end of the file
if False:
    mod.comment('Effectively All Legendaries')
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity.DataTable_ItemRarity',
            'VeryRare',
            'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
            65)
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity.DataTable_ItemRarity',
            'Legendary',
            'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
            2000000)
if False:
    mod.comment('Effectively All Purps')
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity.DataTable_ItemRarity',
            'VeryRare',
            'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
            2000000)
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/GameData/Loot/RarityWeighting/DataTable_ItemRarity.DataTable_ItemRarity',
            'Legendary',
            'BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191',
            5)

mod.close()
