#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('better_loot.txt',
        'Better Loot, ish',
        [],
        'BL',
        )
# Define new rarity weights.  No idea what the defaults are for these, though.

# Theoretically Mayhem 1, ish, though I expect that the Mayhem values are more
# modifiers than values
#weights = [7, 7, 40, 50, 35]

# Theoretically "Excellent" Better Loot, ish
#weights = [8, 85, 65, 65, 3]

# Theoretically "Very Good" Better Loot, ish.
# Legendary chance bumped up very slightly, though
weights = [15, 35, 25, 13.5, 0.6]

mod.comment('Base drop weights.  No idea what the defaults are, unfortunately')
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

# Testing guaranteed drops, didn't seem to actually affect anything though.
# I suspect that this object may not exist until the actual pawns have been
# spawned...
#mod.table_hotfix(Mod.PATCH, '',
#        '/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds.Table_LegendarySpecificLootOdds',
#        'Mouthpiece',
#        'LegendaryDropChance_Playthrough1_48_4189D9DA42C2B912FC25209E8C353A26',
#        1)

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

mod.comment('Increased Eridium and Cosmetic chances')
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
