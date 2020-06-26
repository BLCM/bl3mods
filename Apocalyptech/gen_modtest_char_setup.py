#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
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

import math
from bl3hotfixmod.bl3hotfixmod import Mod

level_to = 60

mod = Mod('modtest_char_setup.txt',
        'Set Up Mod-Testing Char (at beginning of the game)',
        'Apocalyptech',
        [
            "Does a couple of things:",
            "",
            "1) Discovering the first zone (right after Claptrap gets sucked",
            "   up by the magnet) will level your char to {}.  (This will".format(level_to),
            "   need tweaking as the game's level cap gets raised.)  Note that",
            "   any future zone discoveries will produce massive amounts of",
            "   Guardian Rank, so make sure to restart without this mod once",
            "   you're levelled.",
            "",
            "2) Alters the first gun chest to contain a Crader's EM-P5 and a",
            "   Transformer shield (identical to first_gun_testing_gear.txt).",
            "",
            "3) Sets Covenant Pass's Game Stage to be {}, so the gear should".format(level_to),
            "   be levelled that far.",
            "",
            "So, basisically, open that starting chest to get a set of level-{}".format(level_to),
            "starting gear, then hop in to the first fight area to level up your",
            "character.  Exit the game, disable this mod, and hop back in.",
            "You'll have yourself a max-levelled character with max-level testing",
            "gear, right from the start of the game.",
            "",
            "This is obviously intended to be used alongside my EM-P5 and",
            "Transformer Super Buff mods.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Taken directly from first_gun_testing_gear.txt
mod.header('First Gun Chest Contents')

mod.reg_hotfix(Mod.EARLYLEVEL, 'Recruitment_P',
        '/Game/Missions/Plot/EP01_ChildrenOfTheVault/LootDef_Global_WhiteChest_ChildrenOfTheVault',
        'DefaultLoot.DefaultLoot[0].ItemAttachments',
        """(
            (
                ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_FirstGun.ItemPool_Pistols_FirstGun"',
                AttachmentPointName=TopLeft,
                Probability=(BaseValueConstant=1)
            ),
            (
                ItemPool=ItemPoolData'"/Game/Gear/Shields/_Design/_Uniques/Transformer/Balance/ItemPool_Shield_Recharger.ItemPool_Shield_Recharger"',
                AttachmentPointName=BottomRight,
                Probability=(BaseValueConstant=1)
            )
        )""")

mod.reg_hotfix(Mod.LEVEL, 'Recruitment_P',
        '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_FirstGun',
        'BalancedItems.BalancedItems[0].InventoryBalanceData',
        Mod.get_full_cond('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5'))

mod.reg_hotfix(Mod.LEVEL, 'Recruitment_P',
        '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_FirstGun',
        'BalancedItems.BalancedItems[0].ResolvedInventoryBalanceData',
        Mod.get_full_cond('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5', 'InventoryBalanceData'))

mod.newline()

# Forcing Covenant Pass to appropriate level.  There's cleaner ways to do this,
# but I don't quite care enough to try and figure it out.  For an example, see
# /Game/Missions/Side/Zone_4/Desolate/Homeopathological/LootDef_Homeopathological_Chest,
# which provides a level-50 common gun to the player during that quest.  It
# uses a LootGameStageVarianceFormula attribute in there, which points to
# Init_Homeopathological_LootChestStage (in the same dir), but JWP can't usefully
# serialize it, so I'd have to poke around with `getall` and hope I got lucky.
mod.header('Force Covenant Pass to Level {}'.format(level_to))

# I find it pretty weird that this statement is required, but if we leave it off,
# the items spawned in the opening chest will remain level 1.  Go figure.
mod.reg_hotfix(Mod.LEVEL, 'Recruitment_P',
        '/Game/GameData/Regions/RegionManagerData',
        'PlayThroughs.PlayThroughs[0].bGameStageTracksPlayerLevelAboveMinimum',
        'True')

# No idea which of these three regions is *actually* the one that's used when
# that chest spawns, but it won't hurt us to just do all three.
for r_idx in [1, 2, 4]:
    mod.reg_hotfix(Mod.LEVEL, 'Recruitment_P',
            '/Game/GameData/Regions/RegionManagerData',
            'PlayThroughs.PlayThroughs[0].Regions.Regions[{}].MinGameStage'.format(r_idx),
            level_to)
    mod.reg_hotfix(Mod.LEVEL, 'Recruitment_P',
            '/Game/GameData/Regions/RegionManagerData',
            'PlayThroughs.PlayThroughs[0].Regions.Regions[{}].MaxGameStage'.format(r_idx),
            100)
mod.newline()

# This wouldn't work because items just plain ol' Don't Spawn At All if you're not at least
# at their MinGameStage.
#mod.header("Lock Crader's EM-P5 and Transformer to Level {}".format(level_to))
#mod.table_hotfix(Mod.PATCH, '',
#        '/Game/PatchDLC/Raid1/Re-Engagement/Balance/DataTable_ReEngagement1_Weapons',
#        'CraderMP5',
#        'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
#        level_to)
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/Gear/Shields/_Design/_Uniques/Transformer/Balance/InvBalD_Shield_LGD_Transformer',
#        'Manufacturers.Manufacturers[0].GameStageWeight.MinGameStage.BaseValueConstant',
#        level_to)
#mod.newline()

mod.header('Zone-Discovery XP Buff')

# There's honestly probably not a great reason *not* to just set this even
# higher, so it wouldn't have to be touched when the level cap goes up.
# For now we're just setting it to match, anyway.
#
# It looks like the "base" XP you get for discovering a zone is 268 or so.
# The default BaseValueConstant for this is 0.2, so I guess you'd get 53XP
# or so for discovering the first zone.  Presumably that 268 value goes up
# as you progress/level, so having this active on a levelled-up char will
# probably result in GR ridiculousness.
#
# Anyway, the XP numbers appear to be identical to BL2/TPS, so for level
# 53 we need to get at least 4,037,543 XP from the first zone discovery.
# 268*15100 = 4,046,800.  So that's what we'll use for now!

level_to_xp = {
    53: 4037543,
    54: 4254491,
    55: 4478792,
    56: 4710556,
    57: 4949890,
    58: 5196902,
    59: 5451701,
    60: 5714393,
    61: 5985086,
    62: 6263885,
    63: 6550897,
    64: 6846227,
    65: 7149982,
    66: 7462266,
    67: 7783184,
    68: 8112840,
    69: 8451340,
    70: 8798786,
    71: 9155282,
    72: 9520932,
    73: 9895840,
    74: 10280105,
    75: 10673832,
    76: 11077123,
    77: 11490079,
    78: 11912803,
    79: 12345396,
    80: 12787958,
    }

# Bit of math to round up, on the likely assumption that we've probably
# got the math very slightly wrong.
required_bvc = math.ceil(level_to_xp[level_to]/268/100)*100
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Balance/ExperienceGlobals',
        'BaseDiscoverAreaExperienceFormula.BaseValueConstant',
        required_bvc)
mod.newline()

mod.close()

