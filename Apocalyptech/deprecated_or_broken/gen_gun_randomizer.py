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

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('gun_randomizer.txt',
        'Gun Randomizer (proof of concept)',
        [
            "Proof of concept for a gun randomizer.  In this state it's ony",
            "randomizing the barrel (oh, and element, I suppose) of the Cloud",
            "Kill SMG, to give it three random barrels from all other base-game",
            "uniques/legendaries.  Seems to work great, though the weapons",
            "don't survive a save/reload.  So clearly there's *some* sanity",
            "checking going on.",
            "",
            "Don't really have any plans to turn this into a full mod, just",
            "wanted to see if it'd work.",
        ])

parts = [
        (False, [
            # Body
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Body/Part_SM_MAL_Body',
            ]),
        (False, [
            # Body Variants
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Body/Part_SM_MAL_Body_A',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Body/Part_SM_MAL_Body_B',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Body/Part_SM_MAL_Body_C',
            ]),
        (True, [
            # Barrel

            # Just Maliwan SMG barrels
            #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Parts/Part_SM_MAL_Barrel_CloudKill',
            #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Parts/Part_SM_MAL_Barrel_Crit',
            #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Parts/Part_SM_MAL_Barrel_Cutsman',
            #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Part/Part_SM_MAL_Barrel_DestructoSpin',
            #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Parts/Part_SM_MAL_Barrel_Devoted',
            #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Parts/Part_SM_MAL_Barrel_Egon',
            #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Parts/Part_SM_MAL_Barrel_Emporer',
            #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Parts/Part_SM_MAL_Barrel_Tsunami',
            #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Parts/Part_SM_MAL_Barrel_VibraPulse',
            #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Parts/Part_SM_MAL_Barrel_westergun',

            # Some shotgun barrels, for the heck of it
            #'/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Brick/Parts/Part_SG_Hyp_Barrel_Brick',
            #'/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Parts/Part_SG_Hyp_Barrel_ConferenceCall',
            #'/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Phebert/Parts/Part_SG_Hyp_Barrel_Phebert',
            #'/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Redistributor/Parts/Part_SG_Hyp_Barrel_Redistributor',
            #'/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/TheButcher/Parts/Part_SG_Hyp_Barrel_TheButcher',

            # All base-game unique/legendary barrels
            '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/MasterworkCrossbow/Parts/Part_SR_HYP_Barrel_Masterwork',
            '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/Woodblocks/Parts/Part_SR_HYP_Barrel_Woodblocks',
            '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Parts/Part_SR_VLA_Barrel_Prison',
            '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Parts/Part_SR_VLA_Barrel_Lyuda',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Parts/Part_MAL_SR_Barrel_Soleki',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Parts/Part_MAL_SR_Barrel_FireStorm',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Parts/Part_MAL_SR_Barrel_Storm',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Barrel_ASMD',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Parts/Part_MAL_SR_Barrel_Krakatoa',
            '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Parts/Part_SR_DAL_Barrel_WorldDestroyer',
            '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Parts/Part_SR_DAL_Barrel_BrashisDedication',
            '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Parts/Part_SR_JAK_Barrel_Monocle',
            '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Hunted/Part_SR_JAK_Barrel_Hunted',
            '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Huntress/Part_SR_JAK_Barrel_Huntress',
            '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Parts/Part_SR_JAK_Barrel_Hunter',
            '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Parts/Part_PS_VLA_Barrel_BoneShredder',
            '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Parts/Part_PS_VLA_Barrel_Infiniti',
            '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Parts/Part_PS_VLA_Barrel_Magnificent',
            '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Parts/Part_PS_COV_Barrel_Chad',
            '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Parts/Part_PS_COV_Barrel_Mouthpiece',
            '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Parts/Part_PS_COV_Barrel_Legion',
            '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Parts/Part_PS_COV_Barrel_PsychoStabber',
            '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Parts/Part_PS_COV_Barrel_Contagion',
            '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Parts/Part_PS_COV_Barrel_Skeksis',
            '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Parts/Part_PS_ATL_Barrel_Drill',
            '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Parts/Part_PS_ATL_Barrel_Warmonger',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Parts/Part_PS_MAL_Barrel_Plumber',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Parts/Part_PS_MAL_Barrel_HellShock',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/_AI/TrooperBadass/Part_PS_MAL_Barrel_AI_TrooperBadass',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Parts/Part_PS_MAL_Barrel_ThunderballFists',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Parts/Part_PS_MAL_Barrel_SuckerPunch',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Parts/Part_PS_MAL_Barrel_HyperHydrator',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Parts/Part_PS_MAL_Barrel_Starkiller',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Troy/Parts/Part_PS_TOR_Barrel_Troy',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Parts/Part_PS_TOR_Barrel_Nurf',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Foursum/Parts/Part_PS_TOR_Barrel_Sight_4SUM',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Foursum/Parts/Part_PS_TOR_Barrel_4SUM',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/RoisensThorns/Parts/Part_PS_TOR_Barrel_RoisensThorns',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Echo/Parts/Part_PS_TOR_Barrel_Echo',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Echo/Parts/Part_PS_TOR_Barrel_Mod_Breeder',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Barrel_Heckle',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Parts/Part_PS_TOR_Barrel_Devestator',
            '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Rakkman/Parts/Part_Dal_PS_Barrel_Rakkman',
            '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Hornet/Parts/Part_Dal_PS_Barrel_Hornet',
            '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Nemesis/Parts/Part_Dal_PS_Barrel_Nemesis',
            '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Omniloader/Parts/Part_Dal_PS_Barrel_Omniloader',
            '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Parts/Part_PS_TED_Barrel_Sabre',
            '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Parts/Part_PS_TED_Barrel_BabyMaker',
            '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Parts/Part_PS_TED_Barrel_Gunerang',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Parts/Part_PS_JAK_Barrel_WagonWheel',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AureliaBackup/Parts/Part_PS_JAK_Barrel_AureliaPistol',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Parts/Part_PS_JAK_Barrel_Buttplug',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Part_PS_JAK_Barrel_SpyRevolver',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Parts/Part_PS_JAK_Barrel_Malevolent',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Parts/Part_PS_JAK_Barrel_Unforgiven',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Parts/Part_PS_JAK_Barrel_TheDuc',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/GodMother/Parts/Part_PS_JAK_Barrel_GodMother',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Parts/Part_PS_JAK_Barrel_MelsCompanion',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Parts/Part_PS_JAK_Barrel_Maggie',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Parts/Part_PS_JAK_Barrel_AmazingGrace',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Parts/Part_PS_JAK_Barrel_Doc',
            '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/PredatoryLending/Parts/Part_SM_HYP_Barrel_PredatoryLending',
            '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Handsome/Parts/Part_SM_HYP_Barrel_Handsome',
            '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/L0V3M4CH1N3/Parts/Part_SM_HYP_Barrel_L0V3M4CH1N3',
            '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Bitch/Parts/Part_SM_HYP_Barrel_Bitch',
            '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Parts/Part_SM_HYP_Barrel_Crossroad',
            '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/XZ/Parts/Part_SM_HYP_Barrel_XZ',
            '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Fork/Parts/Part_SM_HYP_Barrel_Fork',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Parts/Part_SM_MAL_Barrel_Crit',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Parts/Part_SM_MAL_Barrel_Cutsman',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Parts/Part_SM_MAL_Barrel_VibraPulse',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Parts/Part_SM_MAL_Barrel_CloudKill',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Parts/Part_SM_MAL_Barrel_Egon',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Parts/Part_SM_MAL_Barrel_Emporer',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Parts/Part_SM_MAL_Barrel_Tsunami',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Parts/Part_SM_MAL_Barrel_westergun',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Part/Part_SM_MAL_Barrel_DestructoSpin',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Parts/Part_SM_MAL_Barrel_Devoted',
            '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Ripper/Parts/Part_SM_DAL_Barrel_Ripper',
            '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/SleepingGiant/Parts/Part_SM_DAL_Barrel_SleepingGiant',
            '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/RockNRoll_Intro/Part_SM_DAL_Barrel_RockNRoll',
            '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Demoskag/Parts/Part_SM_DAL_Barrel_Demoskag',
            '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/HellFire/Parts/Part_SM_DAL_Barrel_HellFire',
            '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Vanquisher/Parts/Part_SM_DAL_Barrel_Vanquisher',
            '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/NineVolt/Parts/Part_SM_DAL_Barrel_NineVolt',
            '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Parts/Part_SM_TED_Barrel_Beans',
            '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Parts/Part_SM_TED_Barrel_NotAFlamethrower',
            '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Parts/Part_SM_TED_Barrel_SpiderMind',
            '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Parts/Part_SM_TED_Barrel_TenGallon',
            '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/TheButcher/Parts/Part_SG_Hyp_Barrel_TheButcher',
            '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Redistributor/Parts/Part_SG_Hyp_Barrel_Redistributor',
            '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Parts/Part_SG_Hyp_Barrel_ConferenceCall',
            '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Brick/Parts/Part_SG_Hyp_Barrel_Brick',
            '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Phebert/Parts/Part_SG_Hyp_Barrel_Phebert',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Parts/Part_SG_MAL_Barrel_Mouthpiece2',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Parts/Part_SG_MAL_Barrel_Recursion',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Parts/Part_SG_MAL_Barrel_Wisp',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Parts/Part_SG_MAL_Barrel_Shriek',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Parts/Part_SG_MAL_Barrel_Trev',
            '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Parts/Part_SG_Torgue_Barrel_Brewha',
            '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/RedLiner/Parts/Part_SG_Torgue_Barrel_Redline',
            '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Flakker/Parts/Part_SG_Torgue_Barrel_Flakker',
            '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheBoringGun/Parts/Part_SG_TOR_Barrel_Boring',
            '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Thumper/Parts/Part_SG_Torgue_Barrel_Thumper',
            '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Balrog/Parts/Part_SG_Torgue_Barrel_Balrog',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Parts/Part_SG_TED_Barrel_Sludge',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Parts/Part_SG_TED_Barrel_Horizon',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Parts/Part_SG_TED_Barrel_Polybius',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/FriendZone/Parts/Part_SG_TED_Barrel_FriendZone',
            '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Parts/Part_SG_JAK_Barrel_TidalWave',
            '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Parts/Part_SG_JAK_Barrel_TKWave',
            '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Parts/Part_SG_JAK_Barrel_Sledge',
            '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Parts/Part_SG_JAK_Barrel_Mod_Sledge',
            '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Parts/Part_SG_JAK_Barrel_Hellwalker',
            '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Parts/Part_SG_JAK_Barrel_Nimble',
            '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Parts/Part_SG_JAK_Barrel_Garcia',
            '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/OnePunch/Parts/Part_SG_JAK_Barrel_OnePunch',
            '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Parts/Part_AR_VLA_Barrel_LuciansCall',
            '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Parts/Part_AR_VLA_Barrel_Shredifier',
            '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Parts/Part_AR_VLA_Barrel_Damn',
            '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Parts/Part_AR_VLA_Barrel_Ogre',
            '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Parts/Part_AR_VLA_Barrel_Faisor',
            '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Parts/Part_AR_VLA_Barrel_Dictator',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Parts/Part_AR_COV_Barrel_Sawbar',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/FireRate/Part_AR_COV_Barrel_HeatFirerate',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Damage/Part_AR_COV_Barrel_HeatDamage',
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Portal/Parts/Part_AR_ATL_Barrel_Portals',
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Parts/Part_AR_ATL_Barrel_RebelYell',
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Parts/Part_AR_ATL_Barrel_Carrier',
            '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Alchemist/Parts/Part_AR_TOR_Barrel_Alchemist',
            '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/WardenWeapon/Part_AR_TOR_Barrel_Warden',
            '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/LaserSploder/Parts/Part_AR_TOR_Barrel_LaserSploder',
            '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Bearcat/Parts/Part_AR_TOR_Barrel_Bearcat',
            '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/TryBolt/Parts/Part_AR_TOR_Barrel_TryBolt',
            '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Warlord/Parts/Part_DAL_AR_Barrel_Warlord',
            '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Kaos/Parts/Part_DAL_AR_Barrel_Kaos',
            '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Earworm/Parts/Part_DAL_AR_Barrel_Earworm',
            '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/StarHelix/Parts/Part_DAL_AR_Barrel_StarHelix',
            '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Hail/Parts/Part_DAL_AR_Barrel_Hail',
            '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Barrage/Parts/Part_DAL_AR_Barrel_Barrage',
            '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Parts/Part_AR_JAK_Barrel_GatlingGun',
            '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Parts/Part_AR_JAK_Barrel_LeadSprinkler',
            '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Parts/Part_AR_JAK_Barrel_RowansCall',
            '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Parts/Part_AR_JAK_Barrel_HandOfGlory',
            '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Parts/Part_AR_JAK_Barrel_TraitorsDeath',
            '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Parts/Part_AR_JAK_Barrel_PasRifle',
            '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Parts/Part_AR_JAK_Barrel_Bekah',
            '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Parts/Part_ATL_Barrel_Freeman',
            '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Parts/Part_ATL_Barrel_RubysWrath',
            '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Parts/Part_HW_VLA_Barrel_Mongol',
            '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Parts/Part_HW_VLA_Barrel_CloudBurst',
            '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Parts/Part_HW_COV_Barrel_HotDrop',
            '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Part/Part_HW_COV_Barrel_PortaPooper',
            '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Parts/Part_HW_COV_Barrel_Terror',
            '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Parts/Part_HW_TOR_Barrel_BurgerCannon',
            '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Parts/Part_HW_TOR_Barrel_RYNO',
            '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Tunguska/Parts/Part_HW_TOR_Barrel_Tunguska',
            '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Rampager/Parts/Part_HW_TOR_Barrel_Rampager',
            '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Swarm/Parts/Part_HW_TOR_Barrel_Swarm',
            '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Hive/Parts/Part_HW_TOR_Barrel_Hive',
            ]),
        (False, [
            # Barrel Variants
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SM_MAL_Barrel_01_A',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SM_MAL_Barrel_01_B',
            ]),
        (False, [
            # Scope
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Scope/Part_SM_MAL_Scope_01',
            ]),
        (False, [
            # Mag
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Mag/Part_SM_MAL_Mag_01',
            ]),
        (False, [
            # Grip
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Grip/Part_SM_MAL_Grip_03',
            ]),
        (False, [
            # Unknown
            ]),
        (False, [
            # Stock
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Stock/Part_SM_MAL_Stock_01',
            ]),
        (False, [
            # Element
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SM_Mal_ElemPrimary_01_Fire',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SM_Mal_ElemPrimary_02_Cryo',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SM_Mal_ElemPrimary_03_Shock',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SM_Mal_ElemPrimary_04_Radiation',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SM_Mal_ElemPrimary_05_Corrosive',
            ]),
        (False, [
            # Unknown
            ]),
        (False, [
            # Material
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Parts/Part_SM_MAL_Material_CloudKill',
            ]),
        ]

toc = []
full_partlist = []
cur_part_idx = 0
for apl_idx, (editing, partlist) in enumerate(parts):
    if len(partlist) > 0:
        toc.append((cur_part_idx, len(partlist)))
    else:
        toc.append((-1, 0))
    full_partlist.extend(partlist)
    cur_part_idx += len(partlist)

    # Set the partlist
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/InvPartSet_SM_MAL_CloudKill',
            'ActorPartLists[{}].Parts'.format(apl_idx),
            '({})'.format(','.join([
                '(PartData={})'.format(Mod.get_full_cond(part)) for part in partlist
                ])))

    # And do our custom stuff if we're supposed to
    if editing:
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/InvPartSet_SM_MAL_CloudKill',
                'ActorPartLists[{}].bCanSelectMultipleParts'.format(apl_idx),
                'True')
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/InvPartSet_SM_MAL_CloudKill',
                'ActorPartLists[{}].MultiplePartSelectionRange'.format(apl_idx),
                '(Min=3,Max=3)')

# Set the balance partlist
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill',
        'RuntimePartList.AllParts',
        '({})'.format(','.join([
            '(PartData={})'.format(Mod.get_full_cond(part)) for part in full_partlist
            ])))

# Put in our fixed TOC
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill',
        'RuntimePartList.PartTypeTOC',
        '({})'.format(','.join([
            '(StartIndex={},NumParts={})'.format(idx, num) for idx, num in toc
            ])))

mod.close()
