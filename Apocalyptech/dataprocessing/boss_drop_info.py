#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import json
import lzma
import appdirs
from bl3data.bl3data import BL3Data
from bl3save.datalib import DataWrapper
from bl3hotfixmod.bl3hotfixmod import BVC

# Utility which attempts to look through the data and find as much info as
# possible about the unique drops from bosses, taking into consideration the
# Raid1-introduced character drop expansion objects.  This has a couple of
# limitations:
#
#   * This will, of course, not include anything changed via GBX hotfixes
#   * It can fail (or at least be incomplete) in multi-boss situations where
#     there's more than one at the same time.  For instance, the Pain/Terror/A9K
#     drops will almost certainly have to be sorted by hand.
#   * We can't actually serialize BPChar objects, so we can't be totally sure
#     about the itempools we see listed in there, though it seems pretty good
#     regardless.
#
# As you can tell from the imports, this makes use of bl3data, bl3hotfixmod,  and
# also some data lookup functions from bl3-cli-saveedit.

# Cache dir/file
cache_dir = appdirs.user_cache_dir('bl3charpaths', 'Apocalyptech')
cache_file = os.path.join(cache_dir, 'charpaths.json.xz')

pool_exclusions = {
        # Enemy-use, looks like (probably could just exclude the prefixes /Game/Enemies and
        # /Game/NonPlayerCharacters rather than hardcoding this...)  EDIT: Aha, we can't,
        # actually.  Atomic uses a /Game/Enemies pool for his drops.  (And a few others seem
        # to do so as well.
        '/Dandelion/Enemies/TraitorEddie/_Shared/_Design/Weapon/ItemPool_TraitorEddie',
        '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_AssaultRifles',
        '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_COVEnemyUse_HeavyWeapons',
        '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_Pistols',
        '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_Shotguns',
        '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_SMGs',
        '/Game/Enemies/Ape/_Unique/JungleMonarch/_Design/Character/ItemPool_ApeJungleMonarch_SG',
        '/Game/Enemies/Ape/_Unique/KingBobo/_Design/Weapon/ItemPool_ApeKingBobo_Club',
        '/Game/Enemies/Enforcer/_Shared/_Design/Weapon/ItemPool_CoVEnforcers_Shotguns',
        '/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/ItemPool_Enforcer_Bounty01_Weapon',
        '/Game/Enemies/Enforcer/Anointed/_Design/Weapons/ItemPool_Enforcer_Anointed_Gun',
        '/Game/Enemies/Goliath/_Unique/CageArena/_Design/Weapons/ItemPool_GoliathCageArea_Gun',
        '/Game/Enemies/Goon/_Shared/_Design/Weapons/ItemPool_Goon_AirGun',
        '/Game/Enemies/Mech/_Unique/EvilAI/_Design/Weapon/ItemPool_MechEvilAI_Gun',
        '/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Weapons/Gun/ItemPool_GiganticMech1_Gun',
        '/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Weapons/Launcher/ItemPool_GiganticMech_Launcher',
        '/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Weapon/ItemPool_Mech_TrialBoss_Launcher',
        '/Game/Enemies/Oversphere/_Shared/_Design/Weapon/ItemPool_Oversphere_Weapon_03',
        '/Game/Enemies/Punk_Female/_Unique/Bounty02/_Design/Character/ItemPool_PunkBounty02_Equipped',
        '/Game/Enemies/Punk_Female/_Unique/BrewHag/_Design/Weapon/ItemPool_PunkBrewHag_Weapon',
        '/Game/Enemies/Punk_Female/_Unique/SkagLady/_Design/Weapon/ItemPools/ItemPool_SkagLady_HeavyWeapons',
        '/Game/Enemies/Punk_Female/Badass/_Design/Weapon/ItemPools/ItemPool_BadassPunk_HeavyWeapons',
        '/Game/Enemies/Saurian/_Unique/TrialBoss/_Design/Weapon/ItemPool_Saurian_TrialBoss_Head_Launcher',
        '/Game/Enemies/Tink/Shotgun/_Design/ItemPools/ItemPool_TinkUse_Shotguns',
        '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_SG',
        '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_SM',
        '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_TrooperBadass',
        '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_TrooperBasic_SM',
        '/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/ItemPool_Trooper_Bounty01_Equipped',
        '/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Common',
        '/Game/NonPlayerCharacters/Aurelia/_TheBoss/_Design/Weapons/ItemPool_AureliaBoss_Equipped',
        '/Game/PatchDLC/Event2/Enemies/CartelBoss/Boss/_Design/Weapon/ItemPool_CartelBoss_Weapon',
        '/Game/PatchDLC/Event2/Enemies/Meat/Punk/RoasterLT/_Design/Character/ItemPool_Roaster_Equip',
        '/Game/PatchDLC/Event2/Enemies/Meat/Tink/TenderizerLt/_Design/Weapon/ItemPool_Tenderizer_SG',
        '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Weapons/RaidCannon/ItemPool_Gunner_RaidCannon',
        '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/UpperHalf/Weapon/ItemPool_UpperHalf_Gun',
        '/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossA/_Design/Weapons/ItemPool_MechRaidBossA_Gun',
        '/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossB/_Design/Weapons/ItemPool_MechRaidBossB_Gun',
        '/Geranium/Enemies/_Shared/_Design/ItemPools/ItemPool_GerCoVEnemyUse_Pistols',
        '/Geranium/Enemies/_Shared/_Design/ItemPools/ItemPool_GerCoVEnemyUse_Shotguns',
        '/Geranium/Enemies/_Shared/_Design/ItemPools/ItemPool_GerCoVEnemyUse_SniperRifles',
        '/Geranium/Enemies/Gyro/_Unique/Painless/_Design/ItemPools/ItemPool_GyroPainless_EquippedGun',
        '/Geranium/Enemies/LodgeBoss/_Design/Weapon/ItemPool_SploderBoss_Weapon',
        '/Hibiscus/Enemies/_Shared/_Design/ItemPools/ItemPool_Specter_PS_Use',
        '/Hibiscus/Enemies/_Shared/_Design/ItemPools/ItemPool_Zealots_EnemyUse_SMG_E_Shock_Only',
        '/Hibiscus/Enemies/FrostBiters/_Unique/_Design/Character/ItemPool_Spimmouth_EnemyUse_HW',
        '/Hibiscus/Enemies/Lunatic/_Shared/_Design/Weapon/ItemPool_Lunatics_Shotguns',
        '/Hibiscus/Enemies/Zealot/Pilfer/_Design/Weapon/ItemPool_Zealots_EnemyUse_SR_E_Pilfer',
        '/Hibiscus/NonPlayerCharacters/_Generic/Gideon/_Design/Character/ItemPool_EnemyUse_AS_Guideon',

        # Extra noise we don't care about
        '/Game/Enemies/Rakk/Queen/_Design/Character/ItemPool_RakkQueen_CashDrip',
        '/Game/Enemies/Rakk/Queen/_Design/Character/ItemPool_RakkQueen_CashExplosion',
        '/Game/Enemies/Rakk/Queen/_Design/Character/ItemPool_RakkQueen_CashTrickle',
        '/Dandelion/GameData/ItemPool/Ammo/ItemPool_JackBot_ExtraNeed_ExtraQuantity',
        '/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/ItemPool_KillaVolt_Loot_Incidental',
        '/Game/Enemies/FinalBoss/_Shared/_Design/LootPools/ItemPool_FinalBoss_Loot',
        '/Game/GameData/Loot/ItemPools/Ammo/ItemPool_Ammo_AssaulRifle',
        '/Game/GameData/Loot/ItemPools/Currency/ItemPool_Money',
        '/Game/GameData/Loot/ItemPools/Currency/ItemPool_Money_Normal',
        '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary',
        '/Game/GameData/Loot/ItemPools/ItemPool_NeedandGreed',
        '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Balance/ItemPool_Eridian_Fabricator',
        '/Game/Missions/Plot/EP01_ChildrenOfTheVault/ItemPool_Need_Prologue',
        '/Game/Missions/Plot/EP01_ChildrenOfTheVault/ItemPool_Prologue_Ammo',
        }

chars = [
        # Base Game
        ("Agonizer 9000", 'BPChar_Agonizer_9k'),
        ("AMBER LAMPS", 'BPChar_ServiceBot_LOOT'),
        ("Anointed Alpha", 'BPChar_AnointedJoe'),
        ("Anointed X-2", 'BPChar_AnointedX2'),
        ("Anointed X-3", 'BPChar_AnointedX3'),
        ("Anointed X-4", 'BPChar_PsychoAnointedX4'),
        ("Archer Rowe", 'BPChar_HeavyDinerBoss'),
        ("Artemis", 'BPChar_ApeBadass'),
        ("Aurelia", 'BPChar_AureliaBoss'),
        ("Azalea", 'BPChar_PunkBrewHag'),
        ("Big Donny", 'BPChar_TinkMotorcadeBigD'),
        ("Billy, the Anointed", 'BPChar_MansionBoss'),
        ("Bloated Rakk / Engorged Rakk", 'BPChar_RakkQueen'),
        ("Bloodshine", 'BPChar_PsychoBloodshine'),
        ("Buttmunch", 'BPChar_SkagButtmunch'),
        ("Captain Traunt", 'BPChar_Heavy_Traunt'),
        ("Chubby Skag", 'BPChar_SkagChubby'),
        ("Dinklebot", 'BPChar_OversphereRare01'),
        ("Dreg / Rage", 'BPChar_Rakk_Dragon'),
        ("Dumptruck", 'BPChar_Enforcer_BountyPrologue'),
        ("General Traunt", 'BPChar_HeavyDarkTraunt'),
        ("GenIVIV", 'BPChar_MechEvilAI'),
        ("Gigamind", 'BPChar_NogChipHolder'),
        ("Graveward", 'BPChar_EdenBoss'),
        ("Holder", 'BPChar_PrisonerHugs'),
        ("Holy Dumptruck", 'BPChar_Enforcer_BountyPrologue'),
        ("Katagawa Ball", 'BPChar_Oversphere_KatagawaSphere'),
        ("Katagawa Jr.", 'BPChar_KJR'),
        ("Killavolt", 'BPChar_EnforcerKillavolt'),
        ("King Bobo", 'BPChar_ApeKingBobo'),
        ("King Gnasher", 'BPChar_ApeJungleMonarch'),
        ("Lagromar", 'BPChar_TinkDemon'),
        ("Loot Tink", 'BPChar_TinkLoot'),
        ("Lt. Preston", 'BPChar_HeavyFootstepsOfGiants'),
        ("Max", 'BPChar_TrooperBounty03'),
        ("Mincemeat", 'BPChar_PsychoBadass'),
        ("Mouthpiece", 'BPChar_EnforcerSacrificeBoss'),
        ("Muldock, the Anointed", 'BPChar_EnforcerAnointed'),
        ("One Punch", 'BPChar_OnePunch'),
        ("Pain", 'BPChar_Terror'),
        ("Pillaging Maniac / Loot Psycho", 'BPChar_PsychoLoot'),
        ("Private Beans", 'BPChar_NogBeans'),
        ("Queen Ant Wanette", 'BPChar_SpiderantCakeRoyalty'),
        ("Rachael, the Anointed", 'BPChar_GoonAnointed'),
        ("Rampager", 'BPChar_Rampager'),
        ("Rax", 'BPChar_TrooperBounty02'),
        ("Rohner", 'BPChar_PunkMovieGoer'),
        ("Sheega", 'BPChar_PunkSkagLady'),
        ("Shiny Grog", 'BPChar_SaurianShiny'),
        ("Shiv", 'BPChar_PsychoBadassPrologue'),
        ("Terror", 'BPChar_Pain'),
        ("The Big-D (Big Donny's Turret)", 'BPChar_Tink_SentryRocketPodBigD'),
        ("The Tink-Train", 'BPChar_GoonMonsterTrucker'),
        ("Thieving Jabber", 'BPChar_ApeLoot'),
        ("Troy Calypso", 'BPChar_TroyBoss'),
        ("Trufflemunch", 'BPChar_SkagTrufflemunch'),
        ("Tumorhead", 'BPChar_PunkBadass_Tumorhead'),
        ("Turnkey Tim", 'BPChar_EnforcerTurnkey'),
        ("Tyreen the Destroyer", 'BPChar_FinalBoss'),
        ("Undertaker", 'BPChar_TinkUndertaker'),
        ("Vermilingua", 'BPChar_SkagAntEater'),
        ("Vice", 'BPChar_Rakk_DragonCryo'),
        ("Warden", 'BPChar_Goliath_CageArena'),

        # Zer0's Targets of Opportunity
        ("Atomic", 'BPChar_Trooper_Bounty01'),
        ("Baron Noggin", 'BPChar_Nog01_Bounty'),
        ("Crushjaw", 'BPChar_GoonBounty01'),
        ("DJ Deadsk4g", 'BPChar_Enforcer_Bounty02'),
        ("Handsome Jackie", 'BPChar_PunkBounty02'),
        ("Heckle", 'BPChar_Goliath_Bounty01'),
        ("Hot Karl", 'BPChar_Enforcer_Bounty01'),
        ("Judge Hightower", 'BPChar_AtlasSoldier_Bounty01'),
        ("Psychobillies - Billee", 'BPChar_Punk_Bounty01d'),
        ("Psychobillies - Billi", 'BPChar_Punk_Bounty01c'),
        ("Psychobillies - Billie", 'BPChar_Punk_Bounty01b'),
        ("Psychobillies - Billy", 'BPChar_Punk_Bounty01a'),
        ("Sky Bully", 'BPChar_Tink_Bounty01'),
        ("Sylestro", 'BPChar_Heavy_Bounty01'),

        # Hammerlock's Legendary Hunts
        ("Antalope", 'BPChar_Spiderant_Hunt01'),
        ("Blinding Banshee", 'BPChar_Nekrobug_Hunt01'),
        ("Chonk Stomp", 'BPChar_Saurian_Hunt01'),
        ("Chupacabratch", 'BPChar_Ratch_Hunt01'),
        ("Crawly, Cybil", 'BPChar_VarkidHunt02_LarvaA'),
        ("Crawly, Edie", 'BPChar_VarkidHunt02_LarvaB'),
        ("Crawly, Martha", 'BPChar_VarkidHunt02_LarvaC'),
        ("Crawly, Matty", 'BPChar_VarkidHunt02_LarvaD'),
        ("Jabbermogwai", 'BPChar_Ape_Hunt01'),
        ("Manvark", 'BPChar_VarkidHunt01'),
        ("Phoenix", 'BPChar_Rakk_Hunt01'),
        ("Skrakk", 'BPChar_Rakk_HuntSkrakk'),
        ("Swarm Host / Brood Mother / Vanda", 'BPChar_Nekrobug_HopperSwarm'),

        # Boss Rare Spawns
        ("Borman Nates", 'BPChar_PsychoRare02'),
        ("Captain Thunk", 'BPChar_TinkRare02'),
        ("Demoskaggon", 'BPChar_Skag_Rare01'),
        ("El Dragón Jr.", 'BPChar_Goliath_Rare03'),
        ("Force Trooper Citrine", 'BPChar_Trooper_Rare01b'),
        ("Force Trooper Onyx", 'BPChar_Trooper_Rare01a'),
        ("Force Trooper Ruby", 'BPChar_Trooper_Rare01c'),
        ("Force Trooper Sapphire", 'BPChar_Trooper_Rare01e'),
        ("Force Trooper Tourmaline", 'BPChar_Trooper_Rare01d'),
        ("I'm Rakkman", 'BPChar_Rakkman'),
        ("Indo Tyrant", 'BPChar_Saurian_Rare01'),
        ("Maxitrillion", 'BPChar_ServiceBot_Rare01'),
        ("Mother of Grogans", 'BPChar_PunkMotherOfDragons'),
        ("Princess Tarantella II", 'BPChar_SpiderantTarantella'),
        ("Red Jabber", 'BPChar_TinkRedJabber'),
        ("Road Dog", 'BPChar_Goliath_Rare02'),
        ("Sloth", 'BPChar_Goon_Rare01'),
        ("The Unstoppable", 'BPChar_Goliath_Rare01'),
        ("Urist McEnforcer", 'BPChar_EnforcerUrist'),
        ("Warty", 'BPChar_Tink_Rare01'),
        ("Wick", 'BPChar_PsychoRare03'),

        # Trials / Slaughters
        ("Arbalest of Discipline", 'BPChar_Mech_TrialBoss'),
        ("Blue Fire", 'BPChar_GiganticMech2'),
        ("Hag of Fervor", 'BPChar_Goon_TrialBoss'),
        ("Mr. Titan", 'BPChar_Goliath_SlaughterBoss'),
        ("Red Rain", 'BPChar_GiganticMech1'),
        ("Sera of Supremacy", 'BPChar_Guardian_TrialBoss'),
        ("Skag of Survival", 'BPChar_Skag_TrialBoss'),
        ("Tink of Cunning", 'BPChar_Tink_TrialBoss'),
        ("Tremendous Rex", 'BPChar_Saurian_SlaughterBoss'),
        ("Tyrant of Instinct", 'BPChar_Saurian_TrialBoss'),

        # Limited Time Events
        ("Captain Haunt", 'BPChar_HarvestBoss'),
        ("FISH SLAP!", 'BPChar_PsychoBadassTinyEvent2'),
        ("Franco Firewall", 'BPChar_CyberTrooperCapo'),
        ("Joey Ultraviolet", 'BPChar_CartelBoss'),
        ("Josie Byte", 'BPChar_PunkCyberLt'),
        ("Roaster", 'BPChar_Punk_Roaster'),
        ("The Tenderizer", 'BPChar_Tink_Tenderizer'),
        ("Tyrone Smallums", 'BPChar_TrooperBadassTinyEvent2'),

        # Maliwan Takedown
        ("Hildr", 'BPChar_MechRaidBossC'),
        ("Huskarl", 'BPChar_RaidBossMini'),
        ("Róta", 'BPChar_MechRaidBossB'),
        ("Sigrdrifa", 'BPChar_MechRaidBossA'),
        ("Valkyrie Squad", 'BPChar_MechRaidBossBar'),
        ("Wotan the Invincible", 'BPChar_BehemothRaid'),
        ("Wotan's Better Half", 'BPChar_UpperHalf'),
        ("Wotan's Brain", 'BPChar_SpiderBrain'),

        # Guardian Takedown
        ("Anathema the Relentless", 'BPChar_GuardianBruteMiniboss'),
        ("Scourge the Invincible Martyr", 'BPChar_GuardianBruteBoss'),

        # DLC1 (Moxxi's Heist of the Handsome Jackpot)
        ("DEGEN-3", 'BPChar_LoaderBadass_Venchy'),
        ("Evil St. Lawrence", 'BPChar_EnforcerBadass_Lawrence'),
        ("Fabricator", 'BPChar_FabrikatorBasic'),
        ("Freddie the Traitor", 'BPChar_TraitorEddie'),
        ("Gorgeous Armada", 'BPChar_TinkBadass_Giorgio'),
        ("Jackpot the Jack's Bot", 'BPChar_JackBot'),
        ("Junpai Goat Eater", 'BPChar_PunkBadass_Gaudy'),
        ("Loco Chantelle", 'BPChar_GoonBadass_Coco'),
        ("Scraptrap Prime", 'BPChar_ClaptrapQueen'),

        # DLC2 (Guns, Love, and Tentacles)
        ("Amach", 'BPChar_ZealotPilfer_Child_Rare'),
        ("DJ Spinsmouth", 'BPChar_Spinsmouth'),
        ("Eleanor and the Heart", 'BPChar_HeartBoss'),
        ("Empowered Grawn", 'BPChar_LunaticPossessed'),
        ("Empowered Scholar", 'BPChar_MinionPossessed'),
        ("Fungal Gorger", 'BPChar_Lost_Mush_Child'),
        ("Gideon", 'BPChar_Gideon'),
        ("Gmork", 'BPChar_Gmork_B_Wolf_Child'),
        ("Kratch", 'BPChar_SlugBadass_Kratch'),
        ("Kritchy", 'BPChar_Hib_Hunt_Kritchy'),
        ("Kukuwajack", 'BPChar_Hib_Hunt_Hampton'),
        ("Loot Skritaari", 'BPChar_MinionLoot'),
        ("Procurer", 'BPChar_Zealot_Badass_Procurer'),
        ("Shiverous the Unscathed", 'BPChar_Rare_Frost_Dragon'),
        ("Tom", 'BPChar_LostTwo_BigBro'),
        ("Vincent", 'BPChar_Vincent'),
        ("Voltborn", 'BPChar_ZealotNightmareShocker_Rare'),
        ("Wendigo", 'BPChar_Wendigo'),
        ("Xam", 'BPChar_LostTwo_ToughBro'),
        ("Yeti", 'BPChar_Yeti'),

        # DLC3 (Bounty of Blood)
        ("Abbadoxis", 'BPChar_GerSaurianGrogzilla'),
        ("Adelai Bronson", 'BPChar_GerSaurianHorsemen4'),
        ("Bellik Primis", 'BPChar_Biobeast_AlteredBeast'),
        ("Caber Dowd", 'BPChar_GerPunkLarry'),
        ("Dickon Goyle", 'BPChar_GerPunkGreg_Rakk'),
        ("Garriden Loch", 'BPChar_GerTinkProhibitor'),
        ("Haddon Marr", 'BPChar_GerEnforcerYarp'),
        ("Hydragoian", 'BPChar_Biobeast_CopyBeast'),
        ("Ipswitch Dunne (v1)", 'BPChar_GerEnforcerDispatcher'),
        ("Ipswitch Dunne (v2)", 'BPChar_GerSaurianDispatcher'),
        ("Jerrick Logan", 'BPChar_GerPsychoPhaserPete'),
        ("Kormash", 'BPChar_SploderBoss'),
        ("Lani Dixon", 'BPChar_GerPunkNumber'),
        ("Lasodactyl", 'BPChar_GerRakkLasodactyl'),
        ("Lectrikor", 'BPChar_Biobeast_PlasmaBeast'),
        ("Loot Rustler / Loot Poke", 'BPChar_GerTinkLoot'),
        ("Minosaur", 'BPChar_GerSaurianSaurtaur'),
        ("Pterodomini", 'BPChar_GerRakkRod'),
        ("Quartermaster", 'BPChar_Quartermaster_Tink'),
        ("Ruiner", 'BPChar_RuinerBoss'),
        ("Slithermaw", 'BPChar_GerRakkMother'),
        ("Vorducken", 'BPChar_GerSaurianDevourer_Pygmimus'),
        ("Waylon Hurd", 'BPChar_GerPsychoMoleMan'),
        ("Wrendon Esk", 'BPChar_GyroPainless'),
        ]

# Some enemies get an extra pool via a SpawnOptions object, which isn't really
# feasible to discover dynamically.  Just hardcode 'em!
spawnoptions_redirects = {
        'BPChar_ApeBadass': [
            '/Game/Enemies/_Spawning/Ape/_Unique/SpawnOptions_ApeArtemis_TheHangover',
            ],
        'BPChar_MansionBoss': [
            '/Game/Enemies/_Spawning/CotV/Goliaths/_Unique/SpawnOptions_GoliathAnointed_MansionFight',
            ],
        'BPChar_PsychoBadass': [
            '/Game/Enemies/_Spawning/CotV/Psychos/_Unique/SpawnOption_Mincemeat',
            ],
        'BPChar_EnforcerAnointed': [
            '/Game/NonPlayerCharacters/_Eden6/JakobsResistance/_Design/Spawning/SpawnOptions_AnointedEnforcer',
            ],
        'BPChar_NogBeans': [
            '/Game/Enemies/_Spawning/Maliwan/Nog/_Unique/SpawnOptions_NogBeans_Runnable',
            ],
        }

# And a few folks have some other pools that get involved, which'd be annoying to try
# and discover programmatically.  Hardcode these, too!
itempool_redirects = {
        'BPChar_OversphereRare01': [
            ('Loot-O-Gram Pool, when redeemed', '/Game/GameData/Loot/ItemPools/Unique/ItemPool_LootOGram_ConvertedToGuns'),
            ],
        'BPChar_Ape_Hunt01': [
            ('When killed with a fire weapon', '/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/ItemPool_Ape_Hunt01_FireDeath'),
            ],
        }

# Hardcoded notes
notes = {
        # Pain/Terror/A9K are a mess
        'BPChar_Terror': "See https://gist.github.com/ed93fcaf2926ffa5ac728f81c65ec4ad",
        'BPChar_Pain': "See https://gist.github.com/ed93fcaf2926ffa5ac728f81c65ec4ad",
        'BPChar_Agonizer_9k': "See https://gist.github.com/ed93fcaf2926ffa5ac728f81c65ec4ad",

        # I seem to use a couple different BPChar references in better loot while tweaking this one...
        'BPChar_MansionBoss': "Seems to maybe use BPChar_Goliath_Anointed somehow, my mod stuff references that as well",

        # Just wanted to make an annotation for Rachael
        'BPChar_GoonAnointed': "Uses a generic BPChar, but we seem to get the drops properly from 'em anyway",

        # Anointed X-3 inherits basically everything from Anointed X-2's BPChar
        'BPChar_AnointedX3': "Inherits practically everything (including drops) from X-2, so check that",
        }

# A set of bpchar names that we can test against, to see if the expansion object is
# setting chars that we're not looking for
full_bpchar_set = set([c[1].lower() for c in chars])

# Make sure our cache file dir exists
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir, exist_ok=True)

# Read from the cache if we have it
char_cache = {}
if os.path.exists(cache_file):
    with lzma.open(cache_file, 'rt', encoding='utf-8') as df:
        char_cache = json.load(df)

# Init data
data = BL3Data()
dw = DataWrapper()

class MyBVC(BVC):
    """
    A BVC object with a slight bit of alteration for our own purposes here
    """

    @staticmethod
    def from_data_struct(data_struct):
        # Calling a super staticmethod: https://stackoverflow.com/a/26807879/2013126
        bvc = super(MyBVC, MyBVC).from_data_struct(data_struct)
        return MyBVC(bvc=bvc.bvc,
                dtv=bvc.dtv,
                bva=bvc.bva,
                ai=bvc.ai,
                bvs=bvc.bvs,
                )

    def __str__(self):
        if self.dtv.table != 'None':
            base_val = '{}/{}/{}'.format(
                    self.dtv.table.split('/')[-1],
                    self.dtv.row,
                    self.dtv.value,
                    )
        elif self.ai != 'None':
            base_val = self.ai.split('/')[-1]
        elif self.bva != 'None':
            base_val = self.bva.split('/')[-1]
        else:
            base_val = str(self.bvc)
        if self.bvs == 1:
            return base_val
        else:
            return '{} x{}'.format(base_val, self.bvs)

class BalancedItem(object):
    """
    Wrapper class for a single BalancedItem
    """

    def __init__(self, data_struct):
        self.pool = None
        self.balance = None
        if 'export' not in data_struct['ItemPoolData']:
            self.pool = data_struct['ItemPoolData'][1]
        elif 'export' not in data_struct['ResolvedInventoryBalanceData']:
            self.balance = data_struct['ResolvedInventoryBalanceData'][1]
        else:
            self.balance = '(none)'
        self.weight = MyBVC.from_data_struct(data_struct['Weight'])

    def __str__(self):
        """
        Using a `dw` global here is pretty sketchy, but whatever.
        """
        global dw
        if self.pool is not None:
            label = 'Pool Redirect: {}'.format(self.pool)
        else:
            eng_name = dw.name_db.get(self.balance)
            if eng_name:
                label = '{} ({})'.format(eng_name, self.balance.split('/')[-1])
            else:
                label = self.balance
        return '{} (weight: {})'.format(label, self.weight)

class DropOnDeathAddition(object):
    """
    Wrapper for an addition to DropOnDeathItemPools
    """

    def __init__(self, data_struct, expansion_index):
        self.expansion_index = expansion_index
        self.pool = data_struct['ItemPool'][1]
        self.probability = MyBVC.from_data_struct(data_struct['PoolProbability'])
        self.num_times = MyBVC.from_data_struct(data_struct['NumberOfTimesToSelectFromThisPool'])

    def __str__(self):
        return 'idx {}: {} (prob: {}) (times: {})'.format(
                self.expansion_index,
                self.pool,
                self.probability,
                self.num_times,
                )

class PoolExpansion(object):
    """
    Wrapper class for a single PoolExpansion entry
    """

    def __init__(self, data, obj_path, expansion_index):
        self.data = data
        self.obj_path = obj_path
        self.expansion_index = expansion_index
        self.pool_to_expand = None
        self.expanded_items = []

        poolexp_data = data.get_data(obj_path)[0]
        if 'ItemPoolToExpand' in poolexp_data:
            self.pool_to_expand = poolexp_data['ItemPoolToExpand'][1]
            if 'BalancedItems' in poolexp_data and len(poolexp_data['BalancedItems']) > 0:
                for item in poolexp_data['BalancedItems']:
                    self.expanded_items.append(BalancedItem(item))
            else:
                print('WARNING: No items found in {}'.format(obj_path), file=sys.stderr)
        else:
            print('WARNING: No pool specified in {}'.format(obj_path), file=sys.stderr)

class Expansions(object):
    """
    Main wrapper class to hold expansion data
    """

    def __init__(self, data, obj_name, full_bpchar_set):
        self.data = data
        self.obj_name = obj_name

        # Which pools get expanded on a per-char basis
        self.char_pools_expanded = {}

        # Additions to a char's DropOnDeathItemPools
        self.char_dropondeath = {}

        # Get data
        self.obj_data = data.get_data(self.obj_name)[0]
        for idx, exp in enumerate(self.obj_data['CharacterExpansions']):
            exp_bpchar = exp['key'][:-2].lower()
            if exp_bpchar not in full_bpchar_set:
                print('WARNING: {} found in expansion object, but not being processed (index {})'.format(exp['key'], idx), file=sys.stderr)

            # ItemPoolExpansions
            for e in exp['value']['ItemPoolExpansions']:
                expansion_obj_name = e['asset_path_name'].split('.')[0]
                new_expansion = PoolExpansion(data, expansion_obj_name, idx)

                # This'll be helpful for lookups
                if exp_bpchar not in self.char_pools_expanded:
                    self.char_pools_expanded[exp_bpchar] = {}
                if new_expansion.pool_to_expand:
                    pool_to_expand_lower = new_expansion.pool_to_expand.lower()
                    if pool_to_expand_lower not in self.char_pools_expanded[exp_bpchar]:
                        self.char_pools_expanded[exp_bpchar][pool_to_expand_lower] = []
                    self.char_pools_expanded[exp_bpchar][pool_to_expand_lower].append(new_expansion)

            # DropOnDeathItemPools
            for p in exp['value']['DropOnDeathItemPools']:
                if exp_bpchar not in self.char_dropondeath:
                    self.char_dropondeath[exp_bpchar] = []
                self.char_dropondeath[exp_bpchar].append(DropOnDeathAddition(p, idx))

    def get_extra_dropondeath(self, charname):
        """
        Returns a list of extra DropOnDeathItemPool entries for the given `charname`
        """
        charname_lower = charname.lower()
        if charname_lower in self.char_dropondeath:
            return self.char_dropondeath[charname_lower]
        return None

    def get_pool_expansion(self, charname, pool_name):
        """
        Returns a list of additions to the given `pool_name`, for the given `charname`
        """
        charname_lower = charname.lower()
        pool_name_lower = pool_name.lower()
        if charname_lower in self.char_pools_expanded:
            if pool_name_lower in self.char_pools_expanded[charname_lower]:
                return self.char_pools_expanded[charname_lower][pool_name_lower]
        return None

# Grab info about our pool expansions
exps = Expansions(data, '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1', full_bpchar_set)

def report_pool(pool_name, exps, bpchar_name):
    """
    We repport on pool contents from a couple places and want it to be reported
    identically on both
    """
    pool = data.get_data(pool_name)
    if pool:
        if 'BalancedItems' in pool[0]:
            for item in pool[0]['BalancedItems']:
                bi = BalancedItem(item)
                print('   -> {}'.format(bi))
        else:
            print('  WARNING: pool is not an ordinary one...')
    else:
        print('  WARNING: pool is not serializable')
    pes = exps.get_pool_expansion(bpchar_name, pool_name)
    if pes:
        for pe in pes:
            print('   ++: idx {}, Additions from {}'.format(pe.expansion_index, pe.obj_path))
            if len(pe.expanded_items) > 0:
                for item in pe.expanded_items:
                    print('     -> {}'.format(item))
            else:
                print('     WARNING: Pool expanded but without any extra items')

# Loop through chars
cache_changed = False
for char_name, bpchar_name in chars:

    # First get the full path to the bpchar object
    if bpchar_name not in char_cache:
        for full_obj_name in data.find('', bpchar_name, exact=True):
            # Just blindly take the first result
            cache_changed = True
            char_cache[bpchar_name] = full_obj_name
            break
    if bpchar_name not in char_cache:
        raise Exception('{} not found?'.format(bpchar_name))
    bpchar_full = char_cache[bpchar_name]

    # Print out a header
    header = '{} ({})'.format(char_name, bpchar_name)
    print(header)
    print('-'*len(header))
    print(bpchar_full)

    # Print out hardcoded notes, if we have any
    if bpchar_name in notes:
        print('')
        print(' ** {}'.format(notes[bpchar_name]))

    # Get references from the bpchar, to find hardcoded itempools
    seen_dir_header = False
    for ref in data.get_refs_from(bpchar_full):
        ref_lower = ref.lower()
        if ref not in pool_exclusions and '/ItemPool_' in ref:
            if not seen_dir_header:
                seen_dir_header = True
                print('')
                print('Built-in ItemPools (need console to get rates):')
            print('')
            print(' - {}'.format(ref))
            report_pool(ref, exps, bpchar_name)

    # Extra DropOnDeathItemPools
    dods = exps.get_extra_dropondeath(bpchar_name)
    if dods:
        if len(dods) > 0:
            print('')
            print('Extra DropOnDeathItemPools:')
            for dod in dods:
                print('')
                print(' - {}'.format(dod))
                report_pool(dod.pool, exps, bpchar_name)
        else:
            print('')
            print('DropOnDeathItemPools expanded, but with no extra elements')

    # Redirect through a SpawnOptions object, if appropriate
    if bpchar_name in spawnoptions_redirects:
        for spawnoptions_name in spawnoptions_redirects[bpchar_name]:
            so_name_short = spawnoptions_name.split('/')[-1]
            so_data = data.get_exports(spawnoptions_name, 'SpawnFactory_OakAI')[0]
            if 'ItemPoolToDropOnDeath' in so_data:
                print('')
                print('Extra item pool via {}'.format(so_name_short))
                print(' - {}'.format(so_data['ItemPoolToDropOnDeath'][1]))
                report_pool(so_data['ItemPoolToDropOnDeath'][1], exps, bpchar_name)
            else:
                print('')
                print('ERROR: SpawnOptions {} found, but no extra pool defined'.format(so_name_short))

    # Aaand process any other itempool redirects that exist
    if bpchar_name in itempool_redirects:
        for (desc, new_pool) in itempool_redirects[bpchar_name]:
            print('')
            print('{}:'.format(desc))
            print(' - {}'.format(new_pool))
            report_pool(new_pool, exps, bpchar_name)

    print('')
    #break

# Write our cache
if cache_changed:
    print('Updating cache file at {}'.format(cache_file), file=sys.stderr)
    with lzma.open(cache_file, 'wt', encoding='utf-8') as df:
        json.dump(char_cache, df)

