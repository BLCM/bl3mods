#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

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
weights = [15, 35, 25, 13.5, 0.6]

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

mod.header('Increased Eridium and Cosmetic chances')
for char in [
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

    # attempts to alter drop odds table, didn't seem to do anything
    #mod.table_hotfix(Mod.CHAR, char,
    #        '/Game/GameData/Loot/ItemPools/Table_SimpleLootDropChances.Table_SimpleLootDropChances',
    #        'Eridium_Bar',
    #        'Drop_Chances_2_2811F91D40768DBD4FEBB791F8286836',
    #        10000)
    #mod.table_hotfix(Mod.CHAR, char,
    #        '/Game/GameData/Loot/ItemPools/Table_SimpleLootDropChances.Table_SimpleLootDropChances',
    #        'Eridium_Stick',
    #        'Drop_Chances_2_2811F91D40768DBD4FEBB791F8286836',
    #        10000)

    # direct pool finagling.  This works!

    # Cosmetics.  3%?  I'm guessing that's better than they generally are, 'cause I'd hardly see them
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

    # Eridium.  75%, what the hell.  There's a lot to spend Eridium on.
    mod.reg_hotfix(Mod.CHAR, char,
            '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear',
            'ItemPools[10].PoolProbability',
            """(
                BaseValueConstant=0.750000,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.000000
            )""")

mod.newline()

# Guaranteed boss drops!
mod.header('Basic Guaranteed Boss Drop Statements')

# Associating entries from Table_LegendarySpecificLootOdds with characters.  These
# ones seem to be referenced, but the chars in question don't actually drop anything
# specific (though I haven't doublechecked that myself).
#
# Antalope,Antalope,BPChar_Spiderant_Hunt01
# Shiv,Shiv,BPChar_PsychoBadassPrologue
# Red Rain,TechSlaughterBoss,BPChar_GiganticMech1
# Blue Fire,TechSlaughterBoss,BPChar_GiganticMech2

# Not sure if this one is used or not, since that boss fight's a bit weird.  I
# believe those drops are handled via other means:
#
# Terror,Terror,BPChar_Terror

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
# JudgeHightower,
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
        ('Demoskaggon', 'DemoSkag', 'BPChar_Skag_Rare01'),
        ('Dinklebot', 'Dinklebot', 'BPChar_OversphereRare01'),
        ('Force Trooper Citrine', 'PowerTroopers', 'BPChar_Trooper_Rare01b'),
        ('Force Trooper Onyx', 'PowerTroopers', 'BPChar_Trooper_Rare01a'),
        ('Force Trooper Ruby', 'PowerTroopers', 'BPChar_Trooper_Rare01c'),
        ('Force Trooper Sapphire', 'PowerTroopers', 'BPChar_Trooper_Rare01e'),
        ('Force Trooper Tourmaline', 'PowerTroopers', 'BPChar_Trooper_Rare01d'),
        ('GenIVIV', 'GeneVIV', 'BPChar_MechEvilAI'),
        ('Gigamind', 'Gigamind', 'BPChar_NogChipHolder'),
        ('Graveward', 'Graveward', 'BPChar_EdenBoss'),
        ('Handsome Jackie', 'HandsomeJackie', 'BPChar_PunkBounty02'),
        ('Heckle', 'HeckleAndHyde', 'BPChar_Goliath_Bounty01'),
        ('Hot Karl', 'Roadblock', 'BPChar_Enforcer_Bounty01'),
        ('I\'m Rakkman', 'Rakkman', 'BPChar_Rakkman'),
        ('Indo Tyrant', 'IndoTyrant', 'BPChar_Saurian_Rare01'),
        ('Jabbermogwai', 'Jabbermogwai', 'BPChar_Ape_Hunt01'),
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

mod.header_lines(['Extra Guaranteed Boss Drop Statements', '(mostly gleaned from the Week 1 hotfixes)'])

# Set Mouthpiece's "/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All.ItemPool_Guns_All" drop to zero-weight
mod.comment('Mouthpiece')
mod.reg_hotfix(Mod.CHAR, 'BPChar_EnforcerSacrificeBoss',
        '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/ItemPool/ItemPool_EnforcerSacrificeBoss_Shotgun.ItemPool_EnforcerSacrificeBoss_Shotgun',
        'BalancedItems[1].Weight',
        '(BaseValueConstant=0.000000)')
mod.newline()

# Guaranteed drop from Agonizer 9000, and also fold in some more drops:
#   1) Legendary COM drop from the Week 1 event
#   2) Presumably-intended drop additions of Damned, Loaded Dice, and Crader MP5, which
#      only actually drop (probably) during the storyline mission when Pain+Terror are
#      actually in-game.
# Note that the MH4/MT patch also adds the Dictator and White Elephant to this pool,
# so there's a LOT in here.
mod.comment('Agonizer 9000 (Pain+Terror)')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Agonizer_9k',
        '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss_Pain.ItemPoolList_Boss_Pain',
        'ItemPools.ItemPools[3].PoolProbability.BaseValueConstant',
        1)
mod.reg_hotfix(Mod.CHAR, 'BPChar_Agonizer_9k',
        '/Game/Enemies/Tink/_Unique/Pain/_Design/Character/ItemPool_Pain_Loot.ItemPool_Pain_Loot',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror.Balance_HW_COV_Terror,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror.Balance_HW_COV_Terror"',
                Weight=(BaseValueConstant=1)
            ),
            (
                ItemPoolData=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary.ItemPool_ClassMods_05_Legendary"',
                Weight=(BaseValueConstant=1)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Balance/Balance_AR_VLA_Damn.Balance_AR_VLA_Damn,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Balance/Balance_AR_VLA_Damn.Balance_AR_VLA_Damn"',
                Weight=(BaseValueConstant=1)
            ),
            (
                InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Artifacts/LoadedDice/InvBalD_Artifact_LoadedDice.InvBalD_Artifact_LoadedDice,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/PatchDLC/Raid1/Gear/Artifacts/LoadedDice/InvBalD_Artifact_LoadedDice.InvBalD_Artifact_LoadedDice"',
                Weight=(BaseValueConstant=1)
            ),
            (
                InventoryBalanceData=/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5.Balance_SM_DAHL_CraderMP5,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5.Balance_SM_DAHL_CraderMP5"',
                Weight=(BaseValueConstant=1)
            )
        )
        """)
mod.reg_hotfix(Mod.CHAR, 'BPChar_Agonizer_9k',
        '/Game/Enemies/Tink/_Unique/Pain/_Design/Character/ItemPool_Pain_Loot.ItemPool_Pain_Loot',
        'Quantity',
        '(BaseValueConstant=7)')
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
        'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability.BaseValueConstant',
        1)
mod.newline()

# The Rampager.  A currently-active hotfix sets the scale to 0.2; in the past the BVC has been
# set weirdly as well.  Just set the whole PoolProbability attribute and be done with it.
mod.comment('The Rampager')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Rampager',
        '/Game/Enemies/PrometheaBoss/Rampager/_Design/Character/BPChar_Rampager.BPChar_Rampager_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
        """(
            BaseValueConstant=1,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
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

# Judge Hightower - doesn't seem to actually drop from his pool properly, so see if we
# can fix that?  EDIT: nope, couldn't figure this out.  Both Hightower and his gang
# only ever seem to drop a single AR ammo, no matter what I do.  Weird.
# TODO: How about trying to modify /Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01/SpawnOptions_AtlasSoldier_Bounty01
# ... and set that object's `ItemPoolToDropOnDeath` attribute?  For example, see:
# /Game/Enemies/_Spawning/CotV/Enforcers/_Unique/SpawnOptions_EnforcerSacrificeBoss_Runnable
# (Update on todo: either that doesn't work either, or I have the syntax wrong)
#mod.comment('Judge Hightower')
#mod.reg_hotfix(Mod.CHAR, 'BPChar_AtlasSoldier_Bounty01',
#        '/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01/SpawnOptions_AtlasSoldier_Bounty01.SpawnOptions_AtlasSoldier_Bounty01',
#        'ItemPoolToDropOnDeath',
#        '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Sabre_JudgeHightower.ItemPool_Sabre_JudgeHightower')
#mod.reg_hotfix(Mod.LEVEL, 'Towers_P',
#        '/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01/SpawnOptions_AtlasSoldier_Bounty01.SpawnOptions_AtlasSoldier_Bounty01',
#        'ItemPoolToDropOnDeath',
#        '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Sabre_JudgeHightower.ItemPool_Sabre_JudgeHightower')
#mod.reg_hotfix(Mod.CHAR, 'BPChar_AtlasSoldier_Bounty01',
#        '/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01.BPChar_AtlasSoldier_Bounty01_C:AIBalanceState_GEN_VARIABLE',
#        'DropOnDeathItemPools',
#        """(
#            ItemPools=(
#                (
#                    ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Unique/ItemPool_Sabre_JudgeHightower.ItemPool_Sabre_JudgeHightower"',
#                    PoolProbability=(BaseValueConstant=1)
#                )
#            ),
#            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_MiniBoss.ItemPoolList_MiniBoss"')
#        )""")
#
#mod.newline()

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

mod.header('Rare Spawn updates taken from Week 2 Event')

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
            """(
                BaseValueConstant=100.000000,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.000000
            )""")
    mod.newline()

mod.header('Mayhem 4 / Maliwan Takedown enemy compatibility fixes')

# Enemies which follow were all affected by the Mayhem 4 / Maliwan Takedown Nov 21 2019
# patch, adding more drops to their DropOnDeathItemPools via the object
# /Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1
# The ones using ItemPoolExpansions we can work with more subtly, but the
# DropOnDeathItemPools I have no idea how to edit properly.  So the added drops for
# these can technically happen twice - once for our guaranteed drop which we set up
# below, and once for the usually-10% "legit" chance.

# Mother of Grogans.  The MH4/MT patch adds Creeping Death, and we want to keep our
# Week 2 Legendary Artifact drop, too.
mod.comment('Mother of Grogans')
mod.reg_hotfix(Mod.CHAR, 'BPChar_PunkMotherOfDragons',
        '/Game/Enemies/Punk_Female/_Unique/MotherOfDragons/_Design/Character/BPChar_PunkMotherOfDragons.BPChar_PunkMotherOfDragons_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=(
                (
                    ItemPool=ItemPoolData'"/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_05_Legendary.ItemPool_Artifacts_05_Legendary"',
                    PoolProbability=(BaseValueConstant=1.000000)
                ),
                (
                    ItemPool=ItemPoolData'"/Game/Enemies/Punk_Female/_Unique/MotherOfDragons/_Design/Loot/ItemPool_MotherOfDragons_Loot.ItemPool_MotherOfDragons_Loot"',
                    PoolProbability=(BaseValueConstant=1.000000)
                )
            ),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear"'),
        )""")
mod.newline()

# Demoskaggon.  The MH4/MT patch adds Hunted, Monocle, and Night Hawkin.  We'll
# keep the Week 2 Leg. shield drop, too.  Since two spawn at once, though, we're
# dropping our chances/counts for those.
mod.comment('Demoskaggon')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Skag_Rare01',
        '/Game/Enemies/Skag/_Unique/Rare01/_Design/Character/BPChar_Skag_Rare01.BPChar_Skag_Rare01_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools.ItemPools',
        """(
            (
                ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary.ItemPool_Shields_05_Legendary"',
                PoolProbability=(BaseValueConstant=0.5)
            ),
            (
                ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_DemoSkaggon.ItemPool_DemoSkaggon"',
                PoolProbability=(BaseValueConstant=1),
                NumberOfTimesToSelectFromThisPool=(BaseValueConstant=2)
            )
        )""")
mod.newline()

# Power Troopers!  Week 2 added in legendary COMs, we'll keep those in, in addition to
# the MH4/MT gear additions.  Only dropping 1 from all of these pools, there's already
# a crazy amount of legendaries being dropped here.
mod.comment('Onyx Force Trooper')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Trooper_Rare01a',
        '/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01a.BPChar_Trooper_Rare01a_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=(
                (
                    ItemPool=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster_05_Legendary.ItemPool_ClassMods_Beastmaster_05_Legendary"',
                    PoolProbability=(BaseValueConstant=1)
                ),
                (
                    ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper01.ItemPool_PowerTrooper01"',
                    PoolProbability=(BaseValueConstant=1),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=1)
                )
            ),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear"')
        )""")
mod.newline()

mod.comment('Citrine Force Trooper')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Trooper_Rare01b',
        '/Game/Enemies/Trooper/_Unique/Rare01b/_Design/Character/BPChar_Trooper_Rare01b.BPChar_Trooper_Rare01b_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=(
                (
                    ItemPool=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner_05_Legendary.ItemPool_ClassMods_Gunner_05_Legendary"',
                    PoolProbability=(BaseValueConstant=1)
                ),
                (
                    ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper01.ItemPool_PowerTrooper01"',
                    PoolProbability=(BaseValueConstant=1),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=1)
                )
            ),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear"')
        )""")
mod.newline()

mod.comment('Ruby Force Trooper')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Trooper_Rare01c',
        '/Game/Enemies/Trooper/_Unique/Rare01c/_Design/Character/BPChar_Trooper_Rare01c.BPChar_Trooper_Rare01c_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=(
                (
                    ItemPool=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative_05_Legendary.ItemPool_ClassMods_Operative_05_Legendary"',
                    PoolProbability=(BaseValueConstant=1)
                ),
                (
                    ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper01.ItemPool_PowerTrooper01"',
                    PoolProbability=(BaseValueConstant=1),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=1)
                )
            ),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear"')
        )""")
mod.newline()

mod.comment('Tourmaline Force Trooper')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Trooper_Rare01d',
        '/Game/Enemies/Trooper/_Unique/Rare01d/_Design/Character/BPChar_Trooper_Rare01d.BPChar_Trooper_Rare01d_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=(
                (
                    ItemPool=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Siren_05_Legendary.ItemPool_ClassMods_Siren_05_Legendary"',
                    PoolProbability=(BaseValueConstant=1.000000)
                ),
                (
                    ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper02.ItemPool_PowerTrooper02"',
                    PoolProbability=(BaseValueConstant=1),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=1)
                )
            ),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear"')
        )""")
mod.newline()

mod.comment('Sapphire Force Trooper')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Trooper_Rare01e',
        '/Game/Enemies/Trooper/_Unique/Rare01e/_Design/Character/BPChar_Trooper_Rare01e.BPChar_Trooper_Rare01e_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=(
                (
                    ItemPool=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary.ItemPool_ClassMods_05_Legendary"',
                    PoolProbability=(BaseValueConstant=1.000000)
                ),
                (
                    ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper02.ItemPool_PowerTrooper02"',
                    PoolProbability=(BaseValueConstant=1),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=1)
                )
            ),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear"')
        )""")
mod.newline()

# IndoTyrant - gets Unforgiven, Gunerang, and Woodblocker.  Keeping the Week 2
# addition of a cosmetic item, too
mod.comment('IndoTyrant')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Saurian_Rare01',
        '/Game/Enemies/Saurian/_Unique/Rare01/_Design/Character/BPChar_Saurian_Rare01.BPChar_Saurian_Rare01_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools.ItemPools',
        """(
            (
                ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Currency/ItemPool_Money.ItemPool_Money"',
                NumberOfTimesToSelectFromThisPool=(
                    BaseValueConstant=0,
                    AttributeInitializer=BlueprintGeneratedClass'"/Game/GameData/Loot/ItemPools/Init_RandomLootCount_Buttload.Init_RandomLootCount_Buttload_C"'
                )
            ),
            (
                ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/ItemPool_SkinsAndMisc.ItemPool_SkinsAndMisc"',
                PoolProbability=(BaseValueConstant=1)
            ),
            (
                ItemPool=ItemPoolData'"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_IndoTyrant.ItemPool_IndoTyrant"',
                PoolProbability=(BaseValueConstant=1),
                NumberOfTimesToSelectFromThisPool=(BaseValueConstant=3)
            )
        )""")
mod.newline()

# Rampager.  This is actually somewhat easier than the rest; this is just working around
# the Mayhem 4-locked drop which was added here.  Would be more cleanly applied on that
# pool-modification object, but eh.  Note that with this change, if you DO fight the
# Rampager on MH4, you'll get a double chance to drop the Good Juju.  That weird
# money drop in the middle there is... somewhat intentional.  GBX has flopped back and
# forth on that for awhile, but the most recent hotfixes (as of 2019-11-26) have disabled
# the drop, so eh.
mod.comment('Rampager')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Rampager',
        '/Game/Enemies/PrometheaBoss/_Shared/_Design/LootPools/ItemPool_Rampager_Gun.ItemPool_Rampager_Gun',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Rampager/Balance/Balance_HW_TOR_Rampager.Balance_HW_TOR_Rampager,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Rampager/Balance/Balance_HW_TOR_Rampager.Balance_HW_TOR_Rampager"',
                Weight=(BaseValueConstant=1)
            ),
            (
                ItemPoolData=ItemPoolData'/Game/GameData/Loot/ItemPools/Currency/ItemPool_Money_Normal.ItemPool_Money_Normal',
                Weight=(BaseValueConstant=0)
            ),
            (
                InventoryBalanceData=/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju.Balance_DAL_AR_ETech_Juju,
                ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju.Balance_DAL_AR_ETech_Juju"',
                Weight=(BaseValueConstant=1)
            )
        )
        """)
mod.newline()

# Aurelia.  She very helpfully uses a boss-drop constant already, so we don't have to
# mess with the DropOnDeath stuff.  We *do* need to make sure that the M4-specific drop
# gets non-M4'd though.
# I didn't actually test this enough to be sure, but I *think* that we have to set the
# whole Weight tuple to clear out the M4-locked BVA in there (or at least, we'd have
# to set BVA in addition to BVC) - *just* setting BVC looked like it might not be
# enough.
mod.comment('Aurelia')
mod.reg_hotfix(Mod.CHAR, 'BPChar_AureliaBoss',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AureliaBoss.ItemPool_AureliaBoss',
        'BalancedItems[1].Weight',
        """(
            BaseValueConstant=1,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# Holy Dumptruck
mod.comment('Holy Dumptruck')
set_death_pools(mod, 'BPChar_Enforcer_BountyPrologue',
        '/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_HolyDumptruck',
            ],
        )
mod.newline()

# Mouthpiece
mod.comment('Mouthpiece')
set_death_pools(mod, 'BPChar_EnforcerSacrificeBoss',
        '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/Character/BPChar_EnforcerSacrificeBoss',
        pools=[
            '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/ItemPool/ItemPool_EnforcerSacrificeBoss_Gun',
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_MouthpieceDedicated', 2),
            ],
        )
mod.newline()

# Red Rain
mod.comment('Red Rain')
set_death_pools(mod, 'BPChar_GiganticMech1',
        '/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Character/BPChar_GiganticMech1',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_RedRain',
            ],
        )
mod.newline()

# Blue Fire
mod.comment('Blue Fire')
set_death_pools(mod, 'BPChar_GiganticMech2',
        '/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Character/BPChar_GiganticMech2',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_BlueFire',
            ],
        )
mod.newline()

# Mr. Titan.  We also need to alter the pool to allow the M4-specific drop in non-M4
mod.comment('Mr. Titan')
set_death_pools(mod, 'BPChar_Goliath_SlaughterBoss',
        '/Game/Enemies/Goliath/_Unique/SlaughterBoss/_Design/Character/BPChar_Goliath_SlaughterBoss',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/Itempool_CoVSlaughterBoss',
            ],
        )
mod.reg_hotfix(Mod.CHAR, 'BPChar_Goliath_SlaughterBoss',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/Itempool_CoVSlaughterBoss.Itempool_CoVSlaughterBoss',
        'BalancedItems[3].Weight',
        """(
            BaseValueConstant=1,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# Hag of Fervor
mod.comment('Hag of Fervor')
set_death_pools(mod, 'BPChar_Goon_TrialBoss',
        '/Game/Enemies/Goon/_Unique/TrialBoss/_Design/Character/BPChar_Goon_TrialBoss',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon',
            ],
        )
mod.newline()

# Sera of Supremacy
mod.comment('Sera of Supremacy')
set_death_pools(mod, 'BPChar_Guardian_TrialBoss',
        '/Game/Enemies/Guardian/_Unique/TrialBoss/_Design/Character/BPChar_Guardian_TrialBoss',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGuardian',
            ],
        )
mod.newline()

# Sylestro - this one thankfully already uses the legendary drop rate table, so all we need
# to do is make the M4-specific drop not M4-specific.
mod.comment('Sylestro')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Heavy_Bounty01',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Sylvestro.ItemPool_Sylvestro',
        'BalancedItems[2].Weight',
        """(
            BaseValueConstant=1,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# Captain Traunt.  Need to un-M4-lock one item in here.
mod.comment('Captain Traunt')
set_death_pools(mod, 'BPChar_Heavy_Traunt',
        '/Game/Enemies/Heavy/_Unique/Traunt/_Design/Character/BPChar_Heavy_Traunt',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CaptTraunt',
            ],
        ),
mod.reg_hotfix(Mod.CHAR, 'BPChar_Heavy_Traunt',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CaptTraunt.ItemPool_CaptTraunt',
        'BalancedItems[2].Weight',
        """(
            BaseValueConstant=1,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# General Traunt.  Need to un-M4-lock an item in here too.
mod.comment('General Traunt')
set_death_pools(mod, 'BPChar_HeavyDarkTraunt',
        '/Game/Enemies/Heavy/_Unique/DarkTraunt/_Design/Character/BPChar_HeavyDarkTraunt',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_GenTraunt',
            ],
        )
mod.reg_hotfix(Mod.CHAR, 'BPChar_HeavyDarkTraunt',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_GenTraunt.ItemPool_GenTraunt',
        'BalancedItems[2].Weight',
        """(
            BaseValueConstant=1,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# Billy, the Anointed.  Need to un-M4-lock an item
mod.comment('Billy, The Anointed')
set_death_pools(mod, 'BPChar_MansionBoss',
        '/Game/Enemies/Goliath/Anointed/_Design/Character/BPChar_MansionBoss',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_MansionBoss',
            ],
        )
mod.reg_hotfix(Mod.CHAR, 'BPChar_MansionBoss',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_MansionBoss.ItemPool_MansionBoss',
        'BalancedItems[2].Weight',
        """(
            BaseValueConstant=1,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# Arbalest of Discipline.  Need to un-M4-lock an item
mod.comment('Arbalest of Discipline')
set_death_pools(mod, 'BPChar_Mech_TrialBoss',
        '/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Character/BPChar_Mech_TrialBoss',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech',
            ],
        )
mod.reg_hotfix(Mod.CHAR, 'BPChar_Mech_TrialBoss',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech.ItemPool_TrialBossMech',
        'BalancedItems[4].Weight',
        """(
            BaseValueConstant=1,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# Brood Mother
mod.comment('Brood Mother')
set_death_pools(mod, 'BPChar_Nekrobug_HopperSwarm',
        '/Game/Enemies/Nekrobug/_Unique/HopperSwarm/_Design/Character/BPChar_Nekrobug_HopperSwarm',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Broodmother',
            ],
        )
mod.newline()

# Tremendous Rex
mod.comment('Tremendous Rex')
set_death_pools(mod, 'BPChar_Saurian_SlaughterBoss',
        '/Game/Enemies/Saurian/_Unique/SlaughterBoss/_Design/Character/BPChar_Saurian_SlaughterBoss',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CreatureSlaughterBoss',
            ],
        )
mod.newline()

# Tyrant of Instinct
mod.comment('Tyrant of Instinct')
set_death_pools(mod, 'BPChar_Saurian_TrialBoss',
        '/Game/Enemies/Saurian/_Unique/TrialBoss/_Design/Character/BPChar_Saurian_TrialBoss',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSaurian',
            ],
        )
mod.newline()

# Skag of Survival
mod.comment('Skag of Survival')
set_death_pools(mod, 'BPChar_Skag_TrialBoss',
        '/Game/Enemies/Skag/_Unique/TrialBoss/_Design/Character/BPChar_Skag_TrialBoss',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSkag',
            ],
        )
mod.newline()

# Antalope
mod.comment('Antalope')
set_death_pools(mod, 'BPChar_Spiderant_Hunt01',
        '/Game/Enemies/Spiderant/_Unique/Hunt01/_Design/Character/BPChar_Spiderant_Hunt01',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Antalope',
            ],
        )
mod.newline()

# Warty
mod.comment('Warty')
set_death_pools(mod, 'BPChar_Tink_Rare01',
        '/Game/Enemies/Tink/_Unique/Rare01/_Design/Character/BPChar_Tink_Rare01',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Warty',
            ],
        )
mod.newline()

# Captain Thunk
mod.comment('Captain Thunk')
set_death_pools(mod, 'BPChar_TinkRare02',
        '/Game/Enemies/Tink/_Unique/Rare02/_Design/Character/BPChar_TinkRare02',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Thunk',
            ],
        )
mod.newline()

# Tink of Cunning - We also have to un-M4-lock an M4-locked item
mod.comment('Tink of Cunning')
set_death_pools(mod, 'BPChar_Tink_TrialBoss',
        '/Game/Enemies/Tink/_Unique/TrialBoss/_Design/Character/BPChar_Tink_TrialBoss',
        pools=[
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink',
            ],
        )
mod.reg_hotfix(Mod.CHAR, 'BPChar_Tink_TrialBoss',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink.ItemPool_TrialBossTink',
        'BalancedItems[3].Weight',
        """(
            BaseValueConstant=1,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# Troy Calypso - we also need to un-M4-lock one item
mod.comment('Troy Calypso')
set_death_pools(mod, 'BPChar_TroyBoss',
        '/Game/NonPlayerCharacters/Troy/_TheBoss/_Design/Character/BPChar_TroyBoss',
        pools=[
            '/Game/NonPlayerCharacters/Troy/_TheBoss/_Design/Character/ItemPool_Troy_Gun',
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TroyDedicated',
            ],
        )
mod.reg_hotfix(Mod.CHAR, 'BPChar_TroyBoss',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TroyDedicated.ItemPool_TroyDedicated',
        'BalancedItems[1].Weight',
        """(
            BaseValueConstant=1,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# Since the MH4/MT patch, a lot of bosses have 2+ items in their drop pools.  Fix those up
# so that they drop N items to match, like Better Loot has historically done
mod.header('Drop Pool Quantity Tweaks')

for (label, char_name, pool, quantity) in [

        # TODO: *really* the right way to do these in BL3 would be via the NumberOfTimesToDropFromThisPool
        # attr, or whatever it's called.  This could be especially notable with the new M4/MT pools,
        # since the only way we can guarantee drops is by putting the pool in there twice - if a pool
        # with a Quantity of 4 happens to hit the 10% chance in addition to our guaranteed one, you've
        # got 8 items on your hands instead of 5.  Still, I'm far enough along in testing that I'm not
        # gonna bother to change it now.  That's a problem for Future Me.

        # First up, pools which already existed, pre-MH4/MT.

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
        ('Atomic', 'BPChar_Trooper_Bounty01', '/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/ItemPool_Trooper_Bounty01.ItemPool_Trooper_Bounty01', 4),
        # Doublecheck that there's not more than one of these at a time, may not want to up the quantity. - yep, this'll spawn four times, omit it.
        #('Crawley Family', 'BPChar_VarkidHunt02_LarvaA', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_PredatoryLending_CrawlyFamily.ItemPool_PredatoryLending_CrawlyFamily', 2),
        ('Manvark', 'BPChar_VarkidHunt01', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_Headsplosion_Mothman.ItemPool_Headsplosion_Mothman', 3),

        # Now, new pools which were added by MH4/MT

        ('Aurelia', 'BPChar_AureliaBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AureliaBoss.ItemPool_AureliaBoss', 2),
        ('Red Rain', 'BPChar_GiganticMech1', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_RedRain.ItemPool_RedRain', 2),
        ('Blue Fire', 'BPChar_GiganticMech2', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_BlueFire.ItemPool_BlueFire', 2),
        ('Mr. Titan', 'BPChar_Goliath_SlaughterBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/Itempool_CoVSlaughterBoss.Itempool_CoVSlaughterBoss', 4),
        ('Hag of Fervor', 'BPChar_Goon_TrialBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon.ItemPool_TrialBossGoon', 3),
        ('Sera of Supremacy', 'BPChar_Guardian_TrialBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGuardian.ItemPool_TrialBossGuardian', 4),
        ('Sylestro', 'BPChar_Heavy_Bounty01', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Sylvestro.ItemPool_Sylvestro', 3),
        ('Captain Traunt', 'BPChar_Heavy_Traunt', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CaptTraunt.ItemPool_CaptTraunt', 3),
        ('General Traunt', 'BPChar_HeavyDarkTraunt', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_GenTraunt.ItemPool_GenTraunt', 3),
        ('Billy, the Anointed', 'BPChar_MansionBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_MansionBoss.ItemPool_MansionBoss', 3),
        ('Arbalest of Discipline', 'BPChar_Mech_TrialBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech.ItemPool_TrialBossMech', 5),
        ('Brood Mother', 'BPChar_Nekrobug_HopperSwarm', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Broodmother.ItemPool_Broodmother', 3),
        ('Tremendous Rex', 'BPChar_Saurian_SlaughterBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CreatureSlaughterBoss.ItemPool_CreatureSlaughterBoss', 2),
        ('Tyrant of Instinct', 'BPChar_Saurian_TrialBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSaurian.ItemPool_TrialBossSaurian', 4),
        ('Skag of Survival', 'BPChar_Skag_TrialBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSkag.ItemPool_TrialBossSkag', 3),
        ('Antalope', 'BPChar_Spiderant_Hunt01', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Antalope.ItemPool_Antalope', 3),
        ('Warty', 'BPChar_Tink_Rare01', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Warty.ItemPool_Warty', 2),
        ('Captain Thunk', 'BPChar_TinkRare02', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Thunk.ItemPool_Thunk', 2),
        ('Tink of Cunning', 'BPChar_Tink_TrialBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink.ItemPool_TrialBossTink', 4),
        ('Troy Calypso', 'BPChar_TroyBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TroyDedicated.ItemPool_TroyDedicated', 2),

        # There's a lot more than 4 items in here, but this'll do.
        # BPChar_BehemothRaid: Wotan the Invincible
        # BPChar_SpiderBrain: Wotan's Brain
        # BPChar_UpperHalf: Wotan's Better Half
        # BPChar_MechRaidBossBar: Valkyrie Squad
        ('Maliwan Takedown Legendaries (possibly not used?)', '', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_Raid1_Legendary.ItemPool_Raid1_Legendary', 4),
        ('Maliwan Takedown Raid Bosses', 'BPChar_BehemothRaid', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool', 4),
        ('Maliwan Takedown Raid Bosses', 'BPChar_SpiderBrain', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool', 4),
        ('Maliwan Takedown Raid Bosses', 'BPChar_UpperHalf', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool', 4),
        ('Maliwan Takedown Raid Minibosses', 'BPChar_MechRaidBossBar', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool.ItemPool_RaidMiniBosses_Pool', 4),

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
for char_name in [
        'BPChar_BehemothRaid',
        'BPChar_SpiderBrain',
        'BPChar_UpperHalf',
        ]:
    mod.reg_hotfix(Mod.CHAR, char_name,
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool',
            'BalancedItems[8].Weight.BaseValueConstant',
            1)
mod.newline()

# Unlock Mayhem 4 drops where appropriate (for non-boss-specific drops)
mod.header('Mayhem 4 Drop Unlocks')

# Again, kind of guessing at chars here.
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
for char_name in [
        'BPChar_BehemothRaid',
        'BPChar_SpiderBrain',
        'BPChar_UpperHalf',
        ]:
    mod.reg_hotfix(Mod.CHAR, char_name,
            '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool',
            'BalancedItems[8].Weight',
            """(
                BaseValueConstant=1,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1
            )""")
mod.reg_hotfix(Mod.CHAR, 'BPChar_MechRaidBossBar',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool.ItemPool_RaidMiniBosses_Pool',
        'BalancedItems[4].Weight',
        """(
            BaseValueConstant=0.5,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1
        )""")
mod.newline()

# Buff Anoint Drops
#
# Vanilla values:
#   Normal - ???
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
