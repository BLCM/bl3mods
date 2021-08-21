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

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF

mod = Mod('boss_drop_randomizer.bl3hotfix',
        'Boss Drop Randomizer',
        'Apocalyptech',
        [
            "Randomizes the unique drops provided by bosses, or in other words basically",
            "completely does away with specific boss drops.  Drop types should remain",
            "constant -- if a boss originally has a pistol and an AR in its pool, you",
            "should still get a legendary pistol or AR in the drops.",
            "",
            "Note that this does not affect drop rates at all, just the pool contents.",
            "",
            "More or less intended to be used alongside my Expanded Legendary Pools mod",
            "so you get as interesting as possible drops.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.3.2',
        cats='enemy-drops, randomizer',
        )

# There are various ways to accomplish this, and of course I go for a
# super over-engineered method.  Ah, well!

(AR, HW, PS, SG, SM, SR, SH, GM, CM, AF) = range(10)

leg_pools = {
        AR: '/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Legendary',
        HW: '/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Legendary',
        PS: '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Legendary',
        SG: '/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary',
        SM: '/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Legendary',
        SR: '/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary',
        SH: '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary',
        GM: '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary',
        CM: '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary',
        AF: '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_05_Legendary',
        }
for drop_type in leg_pools.keys():
    leg_pools[drop_type] = Mod.get_full_cond(leg_pools[drop_type], 'ItemPoolData')

# Here we go!
for (label, char_name, pools) in sorted([
        ('Amach', 'BPChar_ZealotPilfer_Child_Rare', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_UnseenThreat', [SR, AR]),
            ]),
        ('Anathema the Relentless', 'BPChar_GuardianBruteMiniboss', [
            ('/Game/PatchDLC/Takedown2/GameData/Loot/ItemPool_TD2_Miniboss', [SH, SH, GM, None]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPool_Mayhem2_Legendaries', [HW, SM, PS, SM, AR, HW, SG, SR]),
            ]),
        ('Anointed Alpha', 'BPChar_AnointedJoe', [
            ('/Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/ItemPools/ItemPool_AnointedJoe', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_AnointedJoe', [AR, PS]),
            ]),
        ('Anointed X-2 (and X-3)', 'BPChar_AnointedX2', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AnointedX2', [PS, PS]),
            ]),
        ('Anointed X-4', 'BPChar_PsychoAnointedX4', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AnointedX4', [CM, AR]),
            ]),
        ('Antalope', 'BPChar_Spiderant_Hunt01', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Antalope', [SG, SH, SR]),
            ]),
        ('Arbalest of Discipline', 'BPChar_Mech_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech', [CM, CM]),
            ]),
        ('Archer Rowe', 'BPChar_HeavyDinerBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_ArcherRowe', [CM, SH]),
            ]),
        ('Artemis', 'BPChar_ApeBadass', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Artemis', [AF, AF, None]),
            ]),
        ('Atomic', 'BPChar_Trooper_Bounty01', [
            ('/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/ItemPool_Trooper_Bounty01', [SH]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Trooper_Bounty01', [AR, GM]),
            ]),
        ('Aurelia', 'BPChar_AureliaBoss', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_IceQueen_Aurelia', [SR]),
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_IceShield_Aurelia', [SH]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AureliaBoss', [AR, GM]),
            ]),
        ('Azalea', 'BPChar_PunkBrewHag', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Azalea', [AF, CM]),
            ]),
        ('Baron Noggin', 'BPChar_Nog01_Bounty', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_EMPGrenade_BaronNoggin', [CM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_EMPGrenade_BaronNoggin', [PS]),
            ]),
        ('Big Donny', 'BPChar_TinkMotorcadeBigD', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_BigDonny', [SM, AF]),
            ]),
        ('Billy, the Anointed', 'BPChar_Goliath_Anointed', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_LeadSprinkler_AnointedIntro', [AR, None]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_MansionBoss', [CM]),
            ]),
        ('Blinding Banshee', 'BPChar_Nekrobug_Hunt01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Shriek_DevilBug', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Shriek_DevilBug', [AR, GM]),
            ]),
        ('Blue Fire', 'BPChar_GiganticMech2', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_BlueFire', [AR, AF]),
            ]),
        ('Borman Nates', 'BPChar_PsychoRare02', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_PsychoStabber_BormanNates', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_PsychoStabber_BormanNates', [AR, SM]),
            ]),
        ('Brood Mother / Vanda', 'BPChar_Nekrobug_HopperSwarm', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Broodmother', [HW, PS, SM]),
            ]),
        ('Buttmunch', 'BPChar_SkagButtmunch', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Buttmunch', [AR]),
            ]),
        # Using MatchAll for this on account of Loot Ghosts, who don't have thier own BPChar (they're projectiles)
        ('Captain Haunt (and Loot Ghosts)', 'MatchAll', [
            ('/Game/PatchDLC/BloodyHarvest/GameData/Loot/ItemPool_BloodyHarvest_Legendary', [SG, SR, SH, GM]),
            ]),
        ('Captain Thunk', 'BPChar_TinkRare02', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Thunk', [PS, GM]),
            ]),
        ('Captain Traunt', 'BPChar_Heavy_Traunt', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CaptTraunt', [SR]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SMG_Legendary1', [SM]),
            ]),
        ('Chonk Stomp', 'BPChar_Saurian_Hunt01', [
            ('/Game/Enemies/Saurian/_Unique/Hunt01/_Design/Character/ItemPool_Saurian01_Hunt', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Saurian01_Hunt', [HW]),
            ]),
        ('Chupacabratch', 'BPChar_Ratch_Hunt01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_BloodSucker_Chupacabratch', [GM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_BloodSucker_Chupacabratch', [GM]),
            ]),
        # Theoretically just one of these should do
        ('Crawly Family', 'BPChar_VarkidHunt02_LarvaA', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_PredatoryLending_CrawlyFamily', [SM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_PredatoryLending_CrawlyFamily', [PS]),
            ]),
        ('Crushjaw', 'BPChar_GoonBounty01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_BoneShredder_Crushjaw', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_BoneShredder_Crushjaw', [SH, HW]),
            ]),
        ('DEGEN-3', 'BPChar_LoaderBadass_Venchy', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_Degen3', [SG]),
            ]),
        ('DJ Deadsk4g', 'BPChar_Enforcer_Bounty02', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Thumper_DJBlood', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Thumper_DJBlood', [GM, AF]),
            ]),
        ('DJ Spinsmouth', 'BPChar_Spinsmouth', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_SFForce', [SM]),
            ]),
        ('Demoskaggon', 'BPChar_Skag_Rare01', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_DemoSkaggon', [SR, SR, SM]),
            ]),
        ('Dinklebot', 'BPChar_OversphereRare01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_LootOGram_ConvertedToGuns', [None, SG, AR]),
            ]),
        ('Dr. Benedict', 'BPChar_DrBenedict', [
            ('/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Legendary_Dedicate_Benedict', [SG, CM, SH]),
            ]),
        ('Dreg / Rage', 'BPChar_Rakk_Dragon', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_DregAndRage', [GM, HW]),
            ]),
        ('El Dragon Jr.', 'BPChar_Goliath_Rare03', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_UnleashTheDragon_ElDragonJr', [AF]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_UnleashTheDragon_ElDragonJr', [SH]),
            ]),
        ('Eleanor and the Heart', 'BPChar_HeartBoss', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_LoveDrill', [PS, SH]),
            ]),
        ('Empowered Grawn', 'BPChar_LunaticPossessed', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Lunacy', [AF, CM]),
            ]),
        ('Empowered Scholar', 'BPChar_MinionPossessed', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_VoidRift', [SH, SM]),
            ]),
        ('Evil Brick', 'BPChar_DarkBrick', [
            ('/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Legendary_Dedicate_DarkBrick', [AR]),
            ]),
        ('Evil Lilith', 'BPChar_DarkLilith', [
            ('/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Legendary_Dedicate_DarkLilith', [SM, PS, CM]),
            ]),
        ('Evil Mordecai', 'BPChar_DarkMordecai', [
            ('/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Legendary_Dedicate_DarkMordecai', [SR, CM]),
            ]),
        ('Evil St. Lawrence', 'BPChar_EnforcerBadass_Lawrence', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_StLawrence', [SM]),
            ]),
        ('Fabricator', 'BPChar_FabrikatorBasic', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_Fabricator', [HW]),
            ]),
        ('FISH SLAP!', 'BPChar_PsychoBadassTinyEvent2', [
            ('/Game/PatchDLC/Event2/GameData/Loot/ItemPool_Event02_Unique_Tiny', [SH, GM, HW]),
            ]),
        ('Force Trooper Citrine', 'BPChar_Trooper_Rare01b', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper01', [SH, AR, PS, GM]),
            ]),
        ('Force Trooper Onyx', 'BPChar_Trooper_Rare01a', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper01', [SH, AR, PS, GM]),
            ]),
        ('Force Trooper Ruby', 'BPChar_Trooper_Rare01c', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper01', [SH, AR, PS, GM]),
            ]),
        ('Force Trooper Sapphire', 'BPChar_Trooper_Rare01e', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper02', [SM, GM, SM, SM]),
            ]),
        ('Force Trooper Tourmaline', 'BPChar_Trooper_Rare01d', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_PowerTrooper02', [SM, GM, SM, SM]),
            ]),
        ('Franco Firewall', 'BPChar_CyberTrooperCapo', [
            ('/Game/PatchDLC/Event2/GameData/Loot/ItemPool_Event02_Unique_Cyborg', [AR, SM, SH]),
            ]),
        ('Freddie the Traitor', 'BPChar_TraitorEddie', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_Freddie', [SR]),
            ]),
        ('Fungal Gorger', 'BPChar_Lost_Mush_Child', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Mutant', [AR, CM]),
            ]),
        ('General Traunt', 'BPChar_HeavyDarkTraunt', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_GenTraunt', [SG]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SMG_Legendary2', [SM]),
            ]),
        ('GenIVIV', 'BPChar_MechEvilAI', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_MessyBreakup_GeneVIV', [SG, SM]),
            #('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_MessyBreakup_GeneVIV', [SG, SM, GM]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SG_Legendary', [SG]),
            ]),
        ('Gideon', 'BPChar_Gideon', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_ClassMods_Legendary_Hibiscus', [CM, CM, CM, CM]),
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Guns_Legendary', [SG, AR, SM, SG, SG]),
            ]),
        ('Gigamind', 'BPChar_NogChipHolder', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Spidermind_Gigamind', [SM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Spidermind_Gigamind', [SH]),
            ]),
        ('Gmork', 'BPChar_Gmork_B_Wolf_Child', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hunt_GMork', [SG, SH]),
            ]),
        ('Gorgeous Armada', 'BPChar_TinkBadass_Giorgio', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_GorgeousArmada', [SG]),
            ]),
        ('Graveward', 'BPChar_EdenBoss', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_GraveandWard_Graveward', [AF, SH]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_GraveandWard_Graveward', [SG]),
            ]),
        ('Hag of Fervor', 'BPChar_Goon_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon', [CM, CM]),
            ]),
        ('Handsome Jackie', 'BPChar_PunkBounty02', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_NimbleJack_HandsomeJackie', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_NimbleJack_HandsomeJackie', [SM]),
            ]),
        ('Heckle', 'BPChar_Goliath_Bounty01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Pestilence_HeckleandHyde', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Pestilence_HeckleandHyde', [AR]),
            ]),
        ('Holder', 'BPChar_PrisonerHugs', [
            ('/Game/Missions/Side/Zone_2/Prison/FreeHugs/ItemPool_FreeHugs_Fingerbiter', [SG]),
            ]),
        ('Holy Dumptruck', 'BPChar_Enforcer_BountyPrologue', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_HolyDumptruck', [SG]),
            ]),
        ('Hot Karl', 'BPChar_Enforcer_Bounty01', [
            ('/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/ItemPool_Enforcer_Bounty01', [HW, SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Enforcer_Bounty01', [AR]),
            ]),
        ('I\'m Rakkman', 'BPChar_Rakkman', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Rakkman_Rakkman', [PS]),
            ('Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Rakkman_Rakkman', [SM]),
            ]),
        ('Indo Tyrant', 'BPChar_Saurian_Rare01', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_IndoTyrant', [PS, PS, SR]),
            ]),
        ('Jabbermogwai', 'BPChar_Ape_Hunt01', [
            ('/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/ItemPool_Ape01_Hunt', [GM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Ape01_Hunt', [PS]),
            ('/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/ItemPool_Ape_Hunt01_FireDeath', [SM]),
            ]),
        ('Jackpot the Jack\'s Bot', 'BPChar_JackBot', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_Jackbot', [SM, PS, CM]),
            ]),
        ('Joey Ultraviolet', 'BPChar_CartelBoss', [
            ('/Game/PatchDLC/Event2/GameData/Loot/ItemPool_Event02_UniqueBoss', [AR, SM, SH, SG, AR, PS, SH, GM, HW]),
            ]),
        ('Josie Byte', 'BPChar_PunkCyberLt', [
            ('/Game/PatchDLC/Event2/GameData/Loot/ItemPool_Event02_Unique_Cyborg', [AR, SM, SH]),
            ]),
        ('Judge Hightower', 'BPChar_AtlasSoldier_Bounty01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Sabre_JudgeHightower', [AR, SG]),
            #('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Sabre_JudgeHightower', [AR, SG]),
            ]),
        ('Junpai Goat Eater', 'BPChar_PunkBadass_Gaudy', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_LocoChantelle', [HW]),
            ]),
        ('Katagawa Ball', 'BPChar_Oversphere_KatagawaSphere', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Tsunami_KatagawaBall', [SG]),
            #('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Tsunami_KatagawaBall', [SG, SG]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_PS_Legendary', [PS]),
            ]),
        ('Katagawa Jr.', 'BPChar_KJR', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Storm_Katagawa', [SR]),
            #('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Storm_Katagawa', [SM]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SR_Legendary', [SR]),
            ]),
        ('Killavolt', 'BPChar_EnforcerKillavolt', [
            ('/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Weapon/ItemPool_KillaVolt_Ninevolt', [SM]),
            #('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_KillaVolt_Ninevolt', [SH, GM]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_AR_Legendary', [AR]),
            ]),
        ('King Bobo', 'BPChar_ApeKingBobo', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_KingBobo', [AR, SR]),
            ]),
        ('King Gnasher', 'BPChar_ApeJungleMonarch', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_KingGnasher', [SM, CM]),
            ]),
        ('Kritchy', 'BPChar_Hib_Hunt_Kritchy', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hunt_Mothman', [AR]),
            ]),
        ('Kukuwajack', 'BPChar_Hib_Hunt_Hampton', [
            # SparkCharacterLoadedEntry682 adds Anarchy; if that hotfix ever goes away, the SG here won't work anymore
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hunt_Hampton', [PS, SG]),
            ]),
        ('Lagromar', 'BPChar_TinkDemon', [
            ('/Game/Enemies/Tink/_Unique/Demon/_Design/Loot/ItemPool_DemonDark_DemonTink_Loot', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_DemonDark_DemonTink_Loot', [PS, SM]),
            ]),
        ('Loco Chantelle', 'BPChar_GoonBadass_Coco', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_GoatEater', [HW]),
            ]),
        ('Locomöbius', 'BPChar_TrainBoss', [
            ('/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Legendary_Dedicate_Train', [SG, CM, SH]),
            ]),
        ('Loot Enemies (various)', 'MatchAll', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Loot_Enemies', [None, None, None, None, None, HW]),
            ]),
        # Loot Hearts are a projectile, and don't have their own BPChar
        ('Loot Hearts', 'MatchAll', [
            ('/Game/PatchDLC/EventVDay/GameData/Challenges/ChallengeRewards/ItemPool_VDay_Weapon_PolyAim', [SM]),
            ('/Game/PatchDLC/EventVDay/GameData/Challenges/ChallengeRewards/ItemPool_VDay_Weapon_WeddingInvitation', [SR]),
            ]),
        ('Lt. Preston', 'BPChar_HeavyFootstepsOfGiants', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_LtPreston', [CM, PS]),
            ]),
        ('Manvark', 'BPChar_VarkidHunt01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Headsplosion_Mothman', [SG, AR]),
            #('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Headsplosion_Mothman', [SG, AR]),
            ]),
        ('Max', 'BPChar_TrooperBounty03', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Max', [GM]),
            ]),
        ('Maxitrillion', 'BPChar_ServiceBot_Rare01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Horizon_Maxitrillion', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Horizon_Maxitrillion', [SH, SR]),
            ]),
        ('Mincemeat', 'BPChar_PsychoBadass', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Mincemeat', [HW, None]),
            ]),
        ('Mother of Grogans', 'BPChar_PunkMotherOfDragons', [
            ('/Game/Enemies/Punk_Female/_Unique/MotherOfDragons/_Design/Loot/ItemPool_MotherOfDragons_Loot', [SG, PS]),
            ]),
        ('Mouthpiece', 'BPChar_EnforcerSacrificeBoss', [
            ('/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/ItemPool/ItemPool_EnforcerSacrificeBoss_Gun', [PS]),
            ('/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/ItemPool/ItemPool_EnforcerSacrificeBoss_Shotgun', [SG, None]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_MouthpieceDedicated', [GM, PS]),
            ]),
        ('Mr. Titan', 'BPChar_Goliath_SlaughterBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/Itempool_CoVSlaughterBoss', [AR, SG, GM, AR]),
            ]),
        ('Muldock, the Anointed', 'BPChar_EnforcerAnointed', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Muldock', [SG, SH]),
            ]),
        ('One Punch', 'BPChar_OnePunch', [
            ('/Game/Enemies/Psycho_Male/_Unique/OnePunch/Design/Loot/ItemPool_OnePunch', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_OnePunch', [SM]),
            ]),
        ('Pain (and half of A9K)', 'BPChar_Terror', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Agonizer1500_Terror', [HW]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Agonizer1500_Terror', [AR, AF, SM]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_HW_Legendary1', [HW]),
            ]),
        ('Phoenix', 'BPChar_Rakk_Hunt01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_PhoenixTears_Phoenix', [AF]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_PhoenixTears_Phoenix', [SR, AF]),
            ]),
        ('Princess Tarantella II', 'BPChar_SpiderantTarantella', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Hive_Tarantella', [HW]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Hive_Tarantella', [SH, PS]),
            ]),
        ('Private Beans', 'BPChar_NogBeans', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Westergun_TheBoo', [SH, SG]),
            #('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Westergun_TheBoo', [SH, SG]),
            ('/Game/Missions/Side/Zone_1/Athenas/InvasionOfPrivacy/ItemPool_InvasionOfPrivacy_BeansRunnable', [SM, None]),
            ]),
        ('Procurer', 'BPChar_Zealot_Badass_Procurer', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_ClassMods_Legendary_Hibiscus', [CM, CM, CM, CM]),
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Guns_Legendary', [SG, AR, SM, SG, SG]),
            ]),
        # Just doing one Psychobillie here
        ('Psychobillies', 'BPChar_Punk_Bounty01a', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_ElectricBanjo_GoreGirls', [AF]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_ElectricBanjo_GoreGirls', [PS, AR]),
            ]),
        ('Psychoreaver', 'BPChar_PsychodinP2', [
            ('/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Legendary_Dedicate_Psychodin', [HW, AR]),
            ]),
        ('Queen Ant Wanette', 'BPChar_SpiderantCakeRoyalty', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_QueenAntWanette', [SH, AR]),
            ]),
        ('Rachael, the Anointed', 'BPChar_GoonAnointed', [
            ('Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_RacheltheAnointed', [AF, CM]),
            ]),
        ('Rampager', 'BPChar_Rampager', [
            ('/Game/Enemies/PrometheaBoss/_Shared/_Design/LootPools/ItemPool_Rampager_Gun', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Rampager_Gun', [AR]),
            ]),
        ('Rax', 'BPChar_TrooperBounty02', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Rax', [SH]),
            ]),
        ('Red Jabber', 'BPChar_TinkRedJabber', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_RedJabber', [SR, SH]),
            ]),
        ('Red Rain', 'BPChar_GiganticMech1', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_RedRain', [AR, AF]),
            ]),
        ('Road Dog', 'BPChar_Goliath_Rare02', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Redliner_Roaddog', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Redliner_Roaddog', [SG, AF]),
            ]),
        ('Roaster', 'BPChar_Punk_Roaster', [
            ('/Game/PatchDLC/Event2/GameData/Loot/ItemPool_Event02_Unique_Meat', [SG, AR, PS]),
            ]),
        ('Scourge the Invincible Martyr', 'BPChar_GuardianBruteBoss', [
            ('/Game/PatchDLC/Takedown2/GameData/Loot/ItemPool_TD2_Boss', [HW, SM, AR, None, None]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPool_Mayhem2_Legendaries', [HW, SM, PS, SM, AR, HW, SG, SR]),
            ]),
        ('Scraptrap Prime', 'BPChar_ClaptrapQueen', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_ScraptrapPrime', [SM, PS]),
            ]),
        ('Sera of Supremacy', 'BPChar_Guardian_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGuardian', [CM, CM]),
            ]),
        ('Sheega', 'BPChar_PunkSkagLady', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Sheega', [AR, AF]),
            ]),
        ('Shiv', 'BPChar_PsychoBadassPrologue', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Shiv', [SM, GM]),
            ]),
        ('Shiverous the Unscathed', 'BPChar_Rare_Frost_Dragon', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hydrafrost', [PS, CM]),
            ]),
        ('Skag of Survival', 'BPChar_Skag_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSkag', [CM, CM]),
            ]),
        ('Skrakk', 'BPChar_Rakk_HuntSkrakk', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Skeksis_Skrakk', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Skeksis_Skrakk', [CM]),
            ]),
        ('Sky Bully', 'BPChar_Tink_Bounty01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_ShootingStar_SkyBullies', [AR, GM]),
            #('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_ShootingStar_SkyBullies', [AR, GM]),
            ]),
        ('Sloth', 'BPChar_Goon_Rare01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Piss_ThunkandSloth', [GM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Piss_ThunkandSloth', [HW]),
            ]),
        ('SpongeBoss BulletPants', 'BPChar_SpongeBoss', [
            ('/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Legendary_Dedicate_Sponge', [SM]),
            ]),
        ('Sylestro', 'BPChar_Heavy_Bounty01', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Sylvestro', [CM]),
            # ItemPoolExpansion wouldn't occur here because it's keyed off BPChar_Goliath_Bounty01
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Pestilence_HeckleandHyde', [PS]),
            ]),
        ('Terror (and half of A9K)', 'BPChar_Pain', [
            ('/Game/Enemies/Tink/_Unique/Pain/_Design/Character/ItemPool_Pain_Loot', [HW, None]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Pain_Loot', [AF, AR]),
            ]),
        ('The Big-D', 'BPChar_Tink_SentryRocketPodBigD', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_BigDonnyTurret', [PS]),
            ]),
        ('The Tenderizer', 'BPChar_Tink_Tenderizer', [
            ('/Game/PatchDLC/Event2/GameData/Loot/ItemPool_Event02_Unique_Meat', [SG, AR, PS]),
            ]),
        ('The Tink-Train', 'BPChar_GoonMonsterTrucker', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TinkTrain', [PS, AF]),
            ]),
        ('The Unstoppable', 'BPChar_Goliath_Rare01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool__BandsofSytorak_Unstoppable', [SH]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_BandsofSytorak_Unstoppable', [SH, PS]),
            ]),
        ('Tink of Cunning', 'BPChar_Tink_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink', [CM, CM]),
            ]),
        ('Tom', 'BPChar_LostTwo_BigBro', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Soulrender', [AR, SG]),
            ]),
        ('Tremendous Rex', 'BPChar_Saurian_SlaughterBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CreatureSlaughterBoss', [CM, SR]),
            ]),
        ('Troy Calypso', 'BPChar_TroyBoss', [
            ('/Game/NonPlayerCharacters/Troy/_TheBoss/_Design/Character/ItemPool_Troy_Gun', [PS, None]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TroyDedicated', [SG]),
            ]),
        ('Trufflemunch', 'BPChar_SkagTrufflemunch', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Trufflemunch', [AR]),
            ]),
        ('Tumorhead', 'BPChar_PunkBadass_Tumorhead', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Tumorhead', [SR, CM]),
            ]),
        ('Turnkey Tim', 'BPChar_EnforcerTurnkey', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TurnkeyTim', [PS, SH]),
            ]),
        ('Tyrant of Instinct', 'BPChar_Saurian_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSaurian', [CM, CM]),
            ]),
        ('Tyreen the Destroyer', 'BPChar_FinalBoss', [
            ('/Game/Enemies/FinalBoss/_Shared/_Design/LootPools/ItemPool_FinalBoss_KingsCall', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_FinalBoss_KingsCall', [SM]),
            ]),
        ('Tyrone Smallums', 'BPChar_TrooperBadassTinyEvent2', [
            ('/Game/PatchDLC/Event2/GameData/Loot/ItemPool_Event02_Unique_Tiny', [SH, GM, HW]),
            ]),
        ('Undertaker', 'BPChar_TinkUndertaker', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Undertaker', [GM, SG]),
            ]),
        ('Urist McEnforcer', 'BPChar_EnforcerUrist', [
            ('/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/ItemPool_EnforcerUrist', [SR]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_EnforcerUrist', [SH]),
            ]),
        ('Valkyrie Squad', 'BPChar_MechRaidBossBar', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool', [SH, SH, SH, SH, None]),
            ('/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries', [SM, AR, SR, SG, AR, PS, CM, CM, CM, CM, AR]),
            ]),
        ('Vermilingua', 'BPChar_SkagAntEater', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Vermilingua', [PS, SM]),
            ]),
        ('Vice', 'BPChar_Rakk_DragonCryo', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Vice', [CM]),
            ]),
        ('Vincent', 'BPChar_Vincent', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Shield_initiative', [SH]),
            ]),
        ('Voltborn', 'BPChar_ZealotNightmareShocker_Rare', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Shocker', [SG, CM]),
            ]),
        ('Warden', 'BPChar_Goliath_CageArena', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Freeman_Warden', [HW]),
            #('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Freeman_Warden', [PS, AR]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_HW_Legendary2', [HW]),
            ]),
        ('Warty', 'BPChar_Tink_Rare01', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Warty', [PS, GM]),
            ]),
        ('Wendigo', 'BPChar_Wendigo', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_SparkyBoom', [AR, SG]),
            ]),
        ('Wick', 'BPChar_PsychoRare03', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Portals_VicAndWarty', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Portals_VicAndWarty', [SH]),
            ]),
        # Theoretically we can just do this one
        ('Wotan (all parts)', 'BPChar_BehemothRaid', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool', [PS, SM, SG, SM, SH, SH, SH, SH, None, None]),
            ('/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries', [SM, AR, SR, SG, AR, PS, CM, CM, CM, CM, AR]),
            ]),
        ('Xam', 'BPChar_LostTwo_ToughBro', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Soulrender', [AR, SG]),
            ]),
        ('Yeti', 'BPChar_Yeti', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hunt_Yeti', [PS]),
            ]),

        # DLC3 Drops
        ('Abbadoxis', 'BPChar_GerSaurianGrogzilla', [
            ('/Geranium/Enemies/GerSaurian/_Unique/Grogzilla/_Design/Character/ItemPool_Grogzilla', [AR]),
            ]),
        ('Garriden Loch', 'BPChar_GerTinkProhibitor', [
            ('/Geranium/Enemies/GerTink/_Unique/Prohibitor/_Design/Character/ItemPool_Prohibitor', [SG]),
            ]),
        ('Haddon Marr', 'BPChar_GerEnforcerYarp', [
            ('/Geranium/Enemies/GerEnforcer/_Unique/Yarp/_Design/Character/ItemPool_Yarp', [SR]),
            ]),
        ('Kormash', 'BPChar_SploderBoss', [
            ('/Geranium/Enemies/LodgeBoss/_Design/Character/ItemPool_LodgeBoss', [AR]),
            ]),
        ('Lani Dixon', 'BPChar_GerPunkNumber', [
            ('/Geranium/Enemies/GerPunk_Female/_Unique/Number/_Design/Character/ItemPool_ImaginaryNumber', [SR]),
            ]),
        ('Caber Dowd', 'BPChar_GerPunkLarry', [
            ('/Geranium/Enemies/GerPunk_Female/_Unique/Larry/_Design/Character/ItemPool_GerPunkLarry', [PS]),
            ]),
        ('Dickon Goyle', 'BPChar_GerPunkGreg_Rakk', [
            ('/Geranium/Enemies/GerPunk_Female/_Unique/Greg/_Design/Character/ItemPool_Gregoyle', [PS]),
            ]),
        ('Jerrick Logan', 'BPChar_GerPsychoPhaserPete', [
            ('/Geranium/Enemies/GerPsycho_Male/_Unique/PhaserPete/_Design/Character/ItemPool_PhaserPete', [PS]),
            ]),
        ('Minosaur', 'BPChar_GerSaurianSaurtaur', [
            ('/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/ItemPool_Saurtaur', [SM]),
            ]),
        ('The Quartermaster', 'BPChar_Quartermaster_Tink', [
            ('/Geranium/Enemies/Quartermaster/Tink/_Design/Character/ItemPool_FacilityBoss', [PS]),
            ]),
        ('Adelai Bronson', 'BPChar_GerSaurianHorsemen4', [
            ('/Geranium/Enemies/GerSaurian/_Unique/Horsemen4/_Design/Character/ItemPool_Horsemen', [SG]),
            ]),
        ('Ipswitch Dunne (v1)', 'BPChar_GerEnforcerDispatcher', [
            ('/Geranium/Enemies/GerEnforcer/_Unique/Dispatcher/_Design/Character/ItemPool_Dispatcher', [PS]),
            ]),
        ('Ipswitch Dunne (v2)', 'BPChar_GerSaurianDispatcher', [
            ('/Geranium/Enemies/GerEnforcer/_Unique/Dispatcher/_Design/Character/ItemPool_Dispatcher', [PS]),
            ]),
        ('Pterodomini', 'BPChar_GerRakkRod', [
            ('/Geranium/Enemies/GerRakk/_Unique/Rod/_Design/Character/ItemPool_GerRakkRod', [AR]),
            ]),
        ('Slithermaw', 'BPChar_GerRakkMother', [
            ('/Geranium/Enemies/GerRakk/_Unique/Mother/_Design/Character/ItemPool_RakkMother', [SM]),
            ]),
        ('Vorducken', 'BPChar_GerSaurianDevourer_Pygmimus', [
            ('/Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/ItemPool_Devourer', [HW]),
            ]),
        ('Wrendon Esk', 'BPChar_GyroPainless', [
            ('/Geranium/Enemies/Gyro/_Unique/Painless/_Design/Character/ItemPool_GyroPainless', [HW]),
            ]),
        ('The Ruiner', 'BPChar_RuinerBoss', [
            ('/Geranium/Enemies/Ruiner/Boss/_Design/Character/ItemPool_RuinerBoss', [PS]),
            ]),
        ('Bellik Primis', 'BPChar_Biobeast_AlteredBeast', [
            ('/Geranium/Enemies/Biobeast/_Unique/AlteredBeast/_Design/Character/ItemPool_BioBeastBoss', [SG]),
            ]),
        ('Hydragoian', 'BPChar_Biobeast_CopyBeast', [
            ('/Geranium/Enemies/Biobeast/_Unique/CopyBeast/_Design/Character/ItemPool_Copybeast', [SM]),
            ]),
        ('Lasodactyl', 'BPChar_GerRakkLasodactyl', [
            ('/Geranium/Enemies/GerRakk/_Unique/Lasodactyl/_Design/Character/ItemPool_LasoDactyl', [PS]),
            ]),
        ('Lectrikor', 'BPChar_Biobeast_PlasmaBeast', [
            ('/Geranium/Enemies/Biobeast/_Unique/PlasmaBeast/_Design/Character/ItemPool_PlasmaBeast', [SG]),
            ]),
        ('Waylon Hurd', 'BPChar_GerPsychoMoleMan', [
            ('/Geranium/Enemies/GerPsycho_Male/_Unique/MoleMan/_Design/Character/ItemPool_MoleMan', [SG]),
            ]),

        # DLC6 Drops (Wonder why I haven't been more consistent with keeping these DLCs separated out?)
        ('Beef Pliskken', 'BPChar_Punk_BanditChief', [
            ('/Game/PatchDLC/Ixora2/GameData/Loot/UniqueEnemyDrops/ItemPool_Ixora2_BanditChief', [PS]),
            ]),
        ('Hemovorous the Invincible', 'BPChar_Varkid_RaidBoss', [
            ('/Game/PatchDLC/Ixora2/GameData/Loot/UniqueEnemyDrops/ItemPool_Ixora2_VarkidRaidBoss', [PS, SR, GM, CM]),
            ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/ItemPool_CompanyMan', [CM, CM, CM, CM, CM, CM, CM, CM, CM]),
            ]),
        ('Sumo', 'BPChar_Goliath_CyberpunkBouncer', [
            ('/Game/PatchDLC/Ixora2/GameData/Loot/UniqueEnemyDrops/ItemPool_Ixora2_CyberpunkBouncer', [SH]),
            ]),
        ('The Gravekeeper', 'BPChar_Enforcer_Gravekeeper', [
            ('/Game/PatchDLC/Ixora2/GameData/Loot/UniqueEnemyDrops/ItemPool_Ixora2_Gravekeeper', [GM]),
            ]),
        ('The Seer', 'BPChar_GuardianBrute_Redeemer', [
            ('/Game/PatchDLC/Ixora2/GameData/Loot/UniqueEnemyDrops/ItemPool_Ixora2_Redeemer', [HW, CM, CM, CM, CM]),
            ]),
        ]):

    mod.comment(label)

    # Set up hotfix targets.  This is complex for Hemovorous because for some weird reason, that
    # BPChar *loves* to stay loaded, and even survives a quit to the title screen.  Which means
    # that hotfixes won't get re-applied when going back into the level, unless we *also* do
    # a Level hotfix.  Unfortunately *just* a Level hotfix isn't sufficient.
    targets = [(Mod.CHAR, char_name)]
    if char_name == 'BPChar_Varkid_RaidBoss':
        targets.append((Mod.LEVEL, 'SacrificeBoss_p'))

    for pool_name, contents in pools:
        for idx, drop_type in enumerate(contents):
            if drop_type is not None:
                for hf_type, hf_target in targets:
                    mod.reg_hotfix(hf_type, hf_target,
                            pool_name,
                            'BalancedItems.BalancedItems[{}].InventoryBalanceData'.format(idx),
                            'None')
                    mod.reg_hotfix(hf_type, hf_target,
                            pool_name,
                            'BalancedItems.BalancedItems[{}].ResolvedInventoryBalanceData'.format(idx),
                            'None')
                    mod.reg_hotfix(hf_type, hf_target,
                            pool_name,
                            'BalancedItems.BalancedItems[{}].ItemPoolData'.format(idx),
                            leg_pools[drop_type])
    mod.newline()

mod.comment('Special-case for Heavyweight Harker, in Stormblind Complex (also randomizes other enemies there)')
mod.reg_hotfix(Mod.CHAR, 'BPChar_FrontRider_Rider',
        '/Game/PatchDLC/Ixora/GameData/Loot/ItemPools/ItemPool_Ixora_Guns_Legendary',
        'BalancedItems',
        """(
            (
                ItemPoolData={},
                Weight={}
            )
        )""".format(
            Mod.get_full_cond('/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary', 'ItemPoolData'),
            BVC(bvc=1),
            ))
mod.newline()

mod.comment('Remove partlock attempt for Anointed Alpha drop')
mod.reg_hotfix(Mod.CHAR, 'BPChar_AnointedJoe',
        '/Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/ItemPools/ItemPool_AnointedJoe',
        'PartSelectionOverrides',
        '()')
mod.newline()

mod.close()
