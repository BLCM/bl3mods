#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# TODO: Earl's loot-o-gram pool

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('better_loot.txt',
        'Better Loot, ish',
        [],
        'BL',
        )

def set_legendary_odds(mod, charname, row, chance):
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
                '/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds.Table_LegendarySpecificLootOdds',
                row,
                attr,
                chance)

# Define new rarity weights.  No idea what the defaults are for these, though.

# Theoretically Mayhem 1, ish, though I expect that the Mayhem values are more
# modifiers than values
#weights = [7, 7, 40, 50, 35]

# Theoretically "Excellent" Better Loot, ish
#weights = [8, 85, 65, 65, 3]

# Theoretically "Very Good" Better Loot, ish.
# Legendary chance bumped up very slightly, though
weights = [15, 35, 25, 13.5, 0.6]

mod.header('Base drop weights.  No idea what the defaults are, unfortunately')
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

# Increase Eridium and cosmetic drop chances
#
# Figuring out what elements in the standard drop pool control what
# Still don't have a great method, but, seems to be:
#  0 - Health
#  1 - ammo
#  2 - 'emergency' ammo
#  3 - money
#  4 - Guns
#  5 - COMs
#  6 - Shields
#  7 - Artifacts
#  8 - Grenades
#  9 - Cosmetics
#  10 - Eridium
#
# The object references
#
# Methods tried:
#   SparkPatchEntry
#   SparkLevelPatchEntry, with no level
#   SparkLevelPatchEntry, with specific level
#   SparkCharacterLoadedEntry, with no character
#   SparkCharacterLoadedEntry, with specific character <- this *does* seem to work, but then you're defining
#       that bastard for every char which uses it, yeah? - Update: we can, at least, limit the characters
#       to ones which specifically reference the pool, which is the "Shared" object for nearly all of 'em.
#       So at least we don't have to define every single variation of BPChar_*
#   SparkCharacterLoadedEntry, with BPChar_Enemy
#   SparkPostLoadedEntry, with no extra arg.  (no idea what this would look like, anyway)
#   SparkPostLoadedEntry, with ItemPoolList_StandardEnemyGunsandGear
#   SparkStreamedPackageEntry, with ItemPoolList_StandardEnemyGunsandGear
#
# Not tried yet since I just found out about 'em:
#   SparkStreamedPackageEntry

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

    # Slightly more subtle eridium scale change
    # .... this... doesn't work?  wtf.
    #mod.reg_hotfix(Mod.CHAR, char,
    #        '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear',
    #        'ItemPools[10].PoolProbability.BaseValueScale',
    #        2000000)

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

# The Rampager (this may actually already be the default -- it looks like
# the Week 1 event actually *nerfed* his drop.)
mod.comment('The Rampager')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Rampager',
        '/Game/Enemies/PrometheaBoss/Rampager/_Design/Character/BPChar_Rampager.BPChar_Rampager_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability.BaseValueConstant',
        1)
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

mod.header('Mayhem 4 / Maliwan Takedown compatibility fixes')

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
