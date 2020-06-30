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

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF

mod = Mod('boss_drop_randomizer.txt',
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
        lic=Mod.CC_BY_SA_40,
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
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_UnseenThreat', [SR]),
            ]),
        ('Anathema the Relentless', 'BPChar_GuardianBruteMiniboss', [
            ('/Game/PatchDLC/Takedown2/GameData/Loot/ItemPool_TD2_Miniboss', [SH, SH, GM, None]),
            ('/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries', [SM, AR, SR, SG, AR, PS, CM, CM, CM, CM, AR]),
            ]),
        # I am 99.999% certain that Anathema's Shadow can't actually drop, but may as well leave this in.
        ("Anathema's Shadow", 'BPChar_GuardianBruteMinibossClone', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool', [SH, SH, SH, SH, None]),
            ('/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries', [SM, AR, SR, SG, AR, PS, CM, CM, CM, CM, AR]),
            ]),
        ('Anointed Alpha', 'BPChar_AnointedJoe', [
            ('/Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/ItemPools/ItemPool_AnointedJoe', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_AnointedJoe', [AR, PS]),
            ]),
        ('Antalope', 'BPChar_Spiderant_Hunt01', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Antalope', [SG, AF, SH]),
            ]),
        ('Arbalest of Discipline', 'BPChar_Mech_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech', [CM, CM, CM, CM, CM]),
            ]),
        ('Atomic', 'BPChar_Trooper_Bounty01', [
            ('/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/ItemPool_Trooper_Bounty01', [PS, SH]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Trooper_Bounty01', [AR, AF]),
            ]),
        ('Aurelia', 'BPChar_AureliaBoss', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_IceQueen_Aurelia', [SR]),
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_IceShield_Aurelia', [SH]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AureliaBoss', [GM, AR]),
            ]),
        ('Baron Noggin', 'BPChar_Nog01_Bounty', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_EMPGrenade_BaronNoggin', [GM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_EMPGrenade_BaronNoggin', [PS]),
            ]),
        ('Billy, the Anointed', 'BPChar_Goliath_Anointed', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_LeadSprinkler_AnointedIntro', [AR, None]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_MansionBoss', [AR, AR, CM]),
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
        ('Captain Haunt', 'BPChar_HarvestBoss', [
            ('/Game/PatchDLC/BloodyHarvest/GameData/Loot/ItemPool_BloodyHarvest_Legendary', [SG, SR, SH, GM]),
            ]),
        ('Captain Thunk', 'BPChar_TinkRare02', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Thunk', [PS, GM]),
            ]),
        ('Captain Traunt', 'BPChar_Heavy_Traunt', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CaptTraunt', [GM, SM, SR]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SMG_Legendary1', [SM]),
            ]),
        ('Chonk Stomp', 'BPChar_Saurian_Hunt01', [
            ('/Game/Enemies/Saurian/_Unique/Hunt01/_Design/Character/ItemPool_Saurian01_Hunt', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Saurian01_Hunt', [HW, HW]),
            ]),
        ('Chupacabratch', 'BPChar_Ratch_Hunt01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_BloodSucker_Chupacabratch', [GM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_BloodSucker_Chupacabratch', [GM, PS]),
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
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_LootOGram_ConvertedToGuns', [None, PS, SG, AR]),
            ]),
        ('El Dragon Jr.', 'BPChar_Goliath_Rare03', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_UnleashTheDragon_ElDragonJr', [AF]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_UnleashTheDragon_ElDragonJr', [SH, GM]),
            ]),
        ('Eleanor and the Heart', 'BPChar_HeartBoss', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_LoveDrill', [PS]),
            ]),
        ('Empowered Grawn', 'BPChar_LunaticPossessed', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Lunacy', [AF]),
            ]),
        ('Empowered Scholar', 'BPChar_MinionPossessed', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_VoidRift', [SH]),
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
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Mutant', [AR]),
            ]),
        ('General Traunt', 'BPChar_HeavyDarkTraunt', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_GenTraunt', [SG, AF, PS]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SMG_Legendary2', [SM]),
            ]),
        ('GenIVIV', 'BPChar_MechEvilAI', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_MessyBreakup_GeneVIV', [SH]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_MessyBreakup_GeneVIV', [SG, SM, GM]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SG_Legendary', [SG]),
            ]),
        ('Gideon', 'BPChar_Gideon', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_ClassMods_Legendary_Hibiscus', [CM, CM, CM, CM]),
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Guns_Legendary', [SG, AR, SM, SG, SG]),
            ]),
        ('Gigamind', 'BPChar_NogChipHolder', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Spidermind_Gigamind', [SM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Spidermind_Gigamind', [SH, PS]),
            ]),
        ('Gmork', 'BPChar_Gmork_B_Wolf_Child', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hunt_GMork', [SG]),
            ]),
        ('Gorgeous Armada', 'BPChar_TinkBadass_Giorgio', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_GorgeousArmada', [SG]),
            ]),
        ('Graveward', 'BPChar_EdenBoss', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_GraveandWard_Graveward', [AF, SH, AR]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_GraveandWard_Graveward', [AF, SG]),
            ]),
        ('Hag of Fervor', 'BPChar_Goon_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon', [CM, CM, CM]),
            ]),
        ('Handsome Jackie', 'BPChar_PunkBounty02', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_NimbleJack_HandsomeJackie', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_NimbleJack_HandsomeJackie', [SG, SM]),
            ]),
        ('Heckle', 'BPChar_Goliath_Bounty01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Pestilence_HeckleandHyde', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Pestilence_HeckleandHyde', [AR, AR]),
            ]),
        ('Holder', 'BPChar_PrisonerHugs', [
            ('/Game/Missions/Side/Zone_2/Prison/FreeHugs/ItemPool_FreeHugs_Fingerbiter', [SG]),
            ]),
        ('Holy Dumptruck', 'BPChar_Enforcer_BountyPrologue', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_HolyDumptruck', [SG]),
            ]),
        ('Hot Karl', 'BPChar_Enforcer_Bounty01', [
            ('/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/ItemPool_Enforcer_Bounty01', [SG, HW]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Enforcer_Bounty01', [PS, AR]),
            ]),
        ('I\'m Rakkman', 'BPChar_Rakkman', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Rakkman_Rakkman', [PS]),
            ('Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Rakkman_Rakkman', [SM, AF]),
            ]),
        ('Indo Tyrant', 'BPChar_Saurian_Rare01', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_IndoTyrant', [PS, PS, SR]),
            ]),
        ('Jabbermogwai', 'BPChar_Ape_Hunt01', [
            ('/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/ItemPool_Ape01_Hunt', [GM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Ape01_Hunt', [AR, PS]),
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
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Sabre_JudgeHightower', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Sabre_JudgeHightower', [AR, SG]),
            ]),
        ('Junpai Goat Eater', 'BPChar_PunkBadass_Gaudy', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_LocoChantelle', [HW]),
            ]),
        ('Katagawa Ball', 'BPChar_Oversphere_KatagawaSphere', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Tsunami_KatagawaBall', [SM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Tsunami_KatagawaBall', [SG, SG]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_PS_Legendary', [PS]),
            ]),
        ('Katagawa Jr.', 'BPChar_KJR', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Storm_Katagawa', [SR, None]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Storm_Katagawa', [SM]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SR_Legendary', [SR]),
            ]),
        ('Killavolt', 'BPChar_EnforcerKillavolt', [
            ('/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Weapon/ItemPool_KillaVolt_Ninevolt', [SM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_KillaVolt_Ninevolt', [SH, GM]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_AR_Legendary', [AR]),
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
        ('Manvark', 'BPChar_VarkidHunt01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Headsplosion_Mothman', [SR]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Headsplosion_Mothman', [SG, AR]),
            ]),
        ('Maxitrillion', 'BPChar_ServiceBot_Rare01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Horizon_Maxitrillion', [SG]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Horizon_Maxitrillion', [SH, SR]),
            ]),
        ('Mother of Grogans', 'BPChar_PunkMotherOfDragons', [
            ('/Game/Enemies/Punk_Female/_Unique/MotherOfDragons/_Design/Loot/ItemPool_MotherOfDragons_Loot', [SG]),
            ]),
        ('Mouthpiece', 'BPChar_EnforcerSacrificeBoss', [
            ('/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/ItemPool/ItemPool_EnforcerSacrificeBoss_Gun', [PS]),
            ('/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/ItemPool/ItemPool_EnforcerSacrificeBoss_Shotgun', [SG, None]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_MouthpieceDedicated', [GM, PS]),
            ]),
        ('Mr. Titan', 'BPChar_Goliath_SlaughterBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/Itempool_CoVSlaughterBoss', [AR, SG, GM, AR]),
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
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Westergun_TheBoo', [SM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Westergun_TheBoo', [SH, SG]),
            ]),
        ('Procurer', 'BPChar_Zealot_Badass_Procurer', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_ClassMods_Legendary_Hibiscus', [CM, CM, CM, CM]),
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Guns_Legendary', [SG, AR, SM, SG, SG]),
            ]),
        # Just doing one Psychobillie here
        ('Psychobillies', 'BPChar_Punk_Bounty01a', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_ElectricBanjo_GoreGirls', [AF]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_ElectricBanjo_GoreGirls', [PS, PS, AR]),
            ]),
        ('Rampager', 'BPChar_Rampager', [
            ('/Game/Enemies/PrometheaBoss/_Shared/_Design/LootPools/ItemPool_Rampager_Gun', [HW]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Rampager_Gun', [PS, SR, AR]),
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
            ('/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries', [SM, AR, SR, SG, AR, PS, CM, CM, CM, CM, AR]),
            ]),
        ('Scraptrap Prime', 'BPChar_ClaptrapQueen', [
            ('/Game/PatchDLC/Dandelion/GameData/Loot/UniqueEnemyDrops/ItemPool_ScraptrapPrime', [SM, PS]),
            ]),
        ('Sera of Supremacy', 'BPChar_Guardian_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGuardian', [CM, CM, CM, CM]),
            ]),
        ('Shiverous the Unscathed', 'BPChar_Rare_Frost_Dragon', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hydrafrost', [PS]),
            ]),
        ('Skag of Survival', 'BPChar_Skag_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSkag', [CM, CM, CM]),
            ]),
        ('Skrakk', 'BPChar_Rakk_HuntSkrakk', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Skeksis_Skrakk', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Skeksis_Skrakk', [AR]),
            ]),
        ('Sky Bully', 'BPChar_Tink_Bounty01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_ShootingStar_SkyBullies', [SH]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_ShootingStar_SkyBullies', [AR, GM]),
            ]),
        ('Sloth', 'BPChar_Goon_Rare01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Piss_ThunkandSloth', [GM]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Piss_ThunkandSloth', [AF]),
            ]),
        ('Sylestro', 'BPChar_Heavy_Bounty01', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Sylvestro', [SH, AR, CM]),
            # ItemPoolExpansion wouldn't occur here because it's keyed off BPChar_Goliath_Bounty01
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Pestilence_HeckleandHyde', [GM]),
            ]),
        ('Terror (and half of A9K)', 'BPChar_Pain', [
            ('/Game/Enemies/Tink/_Unique/Pain/_Design/Character/ItemPool_Pain_Loot', [HW, None]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Pain_Loot', [AF, AR]),
            ]),
        ('The Tenderizer', 'BPChar_Tink_Tenderizer', [
            ('/Game/PatchDLC/Event2/GameData/Loot/ItemPool_Event02_Unique_Meat', [SG, AR, PS]),
            ]),
        ('The Unstoppable', 'BPChar_Goliath_Rare01', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool__BandsofSytorak_Unstoppable', [SH]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_BandsofSytorak_Unstoppable', [SH, PS]),
            ]),
        ('Tink of Cunning', 'BPChar_Tink_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink', [CM, CM, CM, CM]),
            ]),
        ('Tom', 'BPChar_LostTwo_BigBro', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Soulrender', [AR]),
            ]),
        ('Tremendous Rex', 'BPChar_Saurian_SlaughterBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CreatureSlaughterBoss', [PS, SR]),
            ]),
        ('Troy Calypso', 'BPChar_TroyBoss', [
            ('/Game/NonPlayerCharacters/Troy/_TheBoss/_Design/Character/ItemPool_Troy_Gun', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TroyDedicated', [SH, SG]),
            ]),
        ('Tyrant of Instinct', 'BPChar_Saurian_TrialBoss', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSaurian', [CM, CM, CM, CM]),
            ]),
        ('Tyreen the Destroyer', 'BPChar_FinalBoss', [
            ('/Game/Enemies/FinalBoss/_Shared/_Design/LootPools/ItemPool_FinalBoss_KingsCall', [PS]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_FinalBoss_KingsCall', [AF, SM]),
            ]),
        ('Tyrone Smallums', 'BPChar_TrooperBadassTinyEvent2', [
            ('/Game/PatchDLC/Event2/GameData/Loot/ItemPool_Event02_Unique_Tiny', [SH, GM, HW]),
            ]),
        ('Urist McEnforcer', 'BPChar_EnforcerUrist', [
            ('/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/ItemPool_EnforcerUrist', [SR]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_EnforcerUrist', [SH, SH]),
            ]),
        ('Valkyrie Squad', 'BPChar_MechRaidBossBar', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool', [SH, SH, SH, SH, None]),
            ('/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries', [SM, AR, SR, SG, AR, PS, CM, CM, CM, CM, AR]),
            ]),
        ('Vincent', 'BPChar_Vincent', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Shield_initiative', [SH]),
            ]),
        ('Voltborn', 'BPChar_ZealotNightmareShocker_Rare', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Shocker', [SG]),
            ]),
        ('Warden', 'BPChar_Goliath_CageArena', [
            ('/Game/GameData/Loot/ItemPools/Unique/ItemPool_Freeman_Warden', [HW]),
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Freeman_Warden', [PS, AR]),
            ('/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_HW_Legendary2', [HW]),
            ]),
        ('Warty', 'BPChar_Tink_Rare01', [
            ('/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Warty', [PS, GM]),
            ]),
        ('Wendigo', 'BPChar_Wendigo', [
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_SparkyBoom', [AR]),
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
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Soulrender', [AR]),
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
        ]):

    mod.comment(label)
    if char_name is None:
        hf_type = Mod.PATCH
        hf_target = ''
    else:
        hf_type = Mod.CHAR
        hf_target = char_name
    for pool_name, contents in pools:
        for idx, drop_type in enumerate(contents):
            if drop_type is not None:
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

mod.comment('Remove partlock attempt for Anointed Alpha drop')
mod.reg_hotfix(Mod.CHAR, 'BPChar_AnointedJoe',
        '/Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/ItemPools/ItemPool_AnointedJoe',
        'PartSelectionOverrides',
        '()')
mod.newline()

mod.close()
