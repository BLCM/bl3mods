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

loot_base = [
    #toptier
    "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson.Balance_SM_DAHL_Kaoson",
    "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner.Balance_HW_VLA_ETech_BackBurner",
    "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Reflux/Balance/Balance_SG_HYP_Reflux.Balance_SG_HYP_Reflux",
    "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Plague/Balance/Balance_HW_TOR_Plague.Balance_HW_TOR_Plague",
    "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch.Balance_AR_VLA_Monarch",
    "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/SandHawk/Balance/Balance_SR_DAL_SandHawk.Balance_SR_DAL_SandHawk",
    "/Game/PatchDLC/Takedown2/Gear/Weapons/Smog/Balance/Balance_SM_HYP_Smog.Balance_SM_HYP_Smog",
    "/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Balance/Balance_SG_JAK_Hellwalker.Balance_SG_JAK_Hellwalker",
    "/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Brick/Balance/Balance_SG_HYP_Brick.Balance_SG_HYP_Brick",
    "/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob.Balance_SG_Torgue_ETech_TheLob",
    "/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa.Balance_MAL_SR_Krakatoa",
    "/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Balance/Balance_SR_JAK_Headsplosion.Balance_SR_JAK_Headsplosion",
    "/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Balance/Balance_PS_COV_PsychoStabber.Balance_PS_COV_PsychoStabber",
    "/Game/PatchDLC/Event2/Gear/Weapon/_Unique/PewPew/Balance/Balance_AR_COV_PewPew.Balance_AR_COV_PewPew",
    "/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Balance/Balance_PS_MAL_GreaseTrap.Balance_PS_MAL_GreaseTrap",
    "/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Balance/Balance_ATL_AR_OPQ.Balance_ATL_AR_OPQ",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Lasocannon/Balance/Balance_PS_VLA_Lasocannon.Balance_PS_VLA_Lasocannon",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Flipper/Balance/Balance_SM_MAL_Flipper.Balance_SM_MAL_Flipper",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Gargoyle/Balance/Balance_PS_COV_Gargoyle.Balance_PS_COV_Gargoyle",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat.Balance_SR_JAK_UnseenThreat",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Balance/Balance_SG_TED_Anarchy.Balance_SG_TED_Anarchy",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Balance/Balance_PS_JAK_Lucky7.Balance_PS_JAK_Lucky7",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Balance/Balance_HW_VLA_IonCannon.Balance_HW_VLA_IonCannon",
    #all
    "/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon",
    "/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth",
    "/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom",
    "/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2",
    "/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5.Balance_SM_DAHL_CraderMP5",
    "/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju.Balance_DAL_AR_ETech_Juju",
    "/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman",
    "/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip.Balance_SG_MAL_DeathGrip",
    "/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev.Balance_AR_COV_Zheitsev",
    "/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute.Balance_PS_TED_Execute",
    "/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop.Balance_AR_TOR_Juliet_WorldDrop",
    "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DNA/Balance/Balance_SM_MAL_DNA.Balance_SM_MAL_DNA",
    "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Balance/Balance_PS_ATL_DoubleTap.Balance_PS_ATL_DoubleTap",
    "/Game/PatchDLC/Takedown2/Gear/Weapons/Globetrotter/Balance/Balance_HW_COV_Globetrotter.Balance_HW_COV_Globetrotter",
    "/Game/PatchDLC/Takedown2/Gear/Weapons/WebSlinger/Balance/Balance_AR_VLA_WebSlinger.Balance_AR_VLA_WebSlinger",
    "/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill.Balance_SM_MAL_CloudKill",
    "/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_VeryRare.Balance_SG_Torgue_ETech_VeryRare",
    #ars
    "/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Balance/Balance_AR_VLA_Dictator.Balance_AR_VLA_Dictator",
    "/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Balance/Balance_AR_VLA_Sherdifier.Balance_AR_VLA_Sherdifier",
    "/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR.Balance_AR_COV_KriegAR",
    "/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Warlord/Balance/Balance_DAL_AR_Warlord.Balance_DAL_AR_Warlord",
    "/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Barrage/Balance/Balance_DAL_AR_Barrage.Balance_DAL_AR_Barrage",
    "/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Balance/Balance_AR_VLA_Ogre.Balance_AR_VLA_Ogre",
    "/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle.Balance_AR_VLA_Sickle",
    "/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Bearcat/Balance/Balance_AR_TOR_Bearcat.Balance_AR_TOR_Bearcat",
    "/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/LaserSploder/Balance/Balance_AR_TOR_LaserSploder.Balance_AR_TOR_LaserSploder",
    "/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/TryBolt/Balance/Balance_AR_TOR_TryBolt.Balance_AR_TOR_TryBolt",
    "/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Balance/Balance_AR_JAK_04_GatlingGun.Balance_AR_JAK_04_GatlingGun",
    "/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Balance/Balance_AR_JAK_LeadSprinkler.Balance_AR_JAK_LeadSprinkler",
    "/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/BOTD/Balance/Balance_DAL_AR_BOTD.Balance_DAL_AR_BOTD",
    "/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/StarHelix/Balance/Balance_DAL_AR_StarHelix.Balance_DAL_AR_StarHelix",
    "/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Balance/Balance_AR_COV_Sawbar.Balance_AR_COV_Sawbar",
    "/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/Balance_ATL_AR_Carrier.Balance_ATL_AR_Carrier",
    "/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Balance/Balance_AR_VLA_Faisor.Balance_AR_VLA_Faisor",
    "/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Balance/Balance_AR_VLA_LuciansCall.Balance_AR_VLA_LuciansCall",
    "/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Balance/Balance_AR_JAK_RowansCall.Balance_AR_JAK_RowansCall",
    "/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Balance/Balance_AR_VLA_Damn.Balance_AR_VLA_Damn",
    "/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Kaos/Balance/Balance_DAL_AR_Kaos.Balance_DAL_AR_Kaos",
    "/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Alchemist/Balance/Balance_AR_TOR_Alchemist.Balance_AR_TOR_Alchemist",
    "/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Balance/Balance_ATL_AR_RebelYell.Balance_ATL_AR_RebelYell",
    #heavys
    "/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Swarm/Balance/Balance_HW_TOR_Swarm.Balance_HW_TOR_Swarm",
    "/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Tunguska/Balance/Balance_HW_TOR_Tunguska.Balance_HW_TOR_Tunguska",
    "/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Balance/Balance_HW_VLA_CloudBurst.Balance_HW_VLA_CloudBurst",
    "/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Balance/Balance_HW_ATL_RubysWrath.Balance_HW_ATL_RubysWrath",
    #pistols
    "/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent.Balance_PS_VLA_Magnificent",
    "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Balance/Balance_PS_JAK_TheDuc.Balance_PS_JAK_TheDuc",
    "/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Foursum/Balance/Balance_PS_TOR_4SUM.Balance_PS_TOR_4SUM",
    "/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Balance/Balance_PS_TOR_Devestator.Balance_PS_TOR_Devestator",
    "/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Echo/Balance/Balance_PS_TOR_Echo.Balance_PS_TOR_Echo",
    "/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Hornet/Balance/Balance_DAL_PS_Hornet.Balance_DAL_PS_Hornet",
    "/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Nemesis/Balance/Balance_DAL_PS_Nemesis.Balance_DAL_PS_Nemesis",
    "/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Balance/Balance_PS_COV_Legion.Balance_PS_COV_Legion",
    "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc.Balance_PS_JAK_Doc",
    "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie.Balance_PS_JAK_Maggie",
    "/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock.Balance_PS_MAL_Hellshock",
    "/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists.Balance_PS_MAL_ThunderballFists",
    "/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber.Balance_PS_MAL_Plumber",
    "/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Balance/Balance_PS_TED_Gunerang.Balance_PS_TED_Gunerang",
    "/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Balance_PS_Tediore_BabyMaker.Balance_PS_Tediore_BabyMaker",
    "/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Balance/Balance_PS_VLA_Infiniti.Balance_PS_VLA_Infiniti",
    "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Balance/Balance_PS_JAK_MelsCompanion.Balance_PS_JAK_MelsCompanion",
    "/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/AAA/Balance/Balance_DAL_PS_AAA.Balance_DAL_PS_AAA",
    "/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/_Bangarang/Balance/Balance_PS_TED_Bangerang.Balance_PS_TED_Bangerang",
    "/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/RoisensThorns/Balance/Balance_PS_TOR_RoisensThorns.Balance_PS_TOR_RoisensThorns",
    "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Balance/Balance_PS_JAK_Unforgiven.Balance_PS_JAK_Unforgiven",
    "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Balance/Balance_PS_JAK_WagonWheel.Balance_PS_JAK_WagonWheel",
    #shotguns
    "/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Balance/Balance_SG_JAK_Unique_Wave.Balance_SG_JAK_Unique_Wave",
    "/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/TheButcher/Balance/Balance_SG_HYP_TheButcher.Balance_SG_HYP_TheButcher",
    "/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Balance/Balance_SG_TED_Polybius.Balance_SG_TED_Polybius",
    "/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Redistributor/Balance/Balance_SG_HYP_Redistributor.Balance_SG_HYP_Redistributor",
    "/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Balance/Balance_SG_HYP_ConferenceCall.Balance_SG_HYP_ConferenceCall",
    "/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion.Balance_SG_MAL_Recursion",
    "/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp.Balance_SG_MAL_Wisp",
    "/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Flakker/Balance/Balance_SG_Torgue_Flakker.Balance_SG_Torgue_Flakker",
    "/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheBoringGun/Balance/Balance_SG_TOR_Boring.Balance_SG_TOR_Boring",
    "/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev.Balance_SG_MAL_Trev",
    #smg
    "/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman.Balance_SM_MAL_Cutsman",
    "/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/SleepingGiant/Balance/Balance_SM_DAL_SleepingGiant.Balance_SM_DAL_SleepingGiant",
    "/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Ripper/Balance/Balance_SM_DAL_Ripper.Balance_SM_DAL_Ripper",
    "/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Bitch/Balance/Balance_SM_HYP_Bitch.Balance_SM_HYP_Bitch",
    "/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/XZ/Balance/Balance_SM_HYP_XZ.Balance_SM_HYP_XZ",
    "/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin.Balance_SM_MAL_DestructoSpin",
    "/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted.Balance_SM_MAL_Devoted",
    "/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Balance/Balance_SM_TED_TenGallon.Balance_SM_TED_TenGallon",
    "/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Vanquisher/Balance/Balance_SM_DAHL_Vanquisher.Balance_SM_DAHL_Vanquisher",
    "/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Handsome/Balance/Balance_SM_HYP_Handsome.Balance_SM_HYP_Handsome",
    "/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Demoskag/Balance/Balance_SM_DAL_Demoskag.Balance_SM_DAL_Demoskag",
    "/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Balance/Balance_SM_HYP_Crossroad.Balance_SM_HYP_Crossroad",
    "/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Balance/Balance_SM_TED_NotAFlamethrower.Balance_SM_TED_NotAFlamethrower",
    #snipers
    "/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Balance/Balance_SR_JAK_Monocle.Balance_SR_JAK_Monocle",
    "/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD.Balance_MAL_SR_ASMD",
    "/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/Woodblocks/Balance/Balance_SR_HYP_Woodblocks.Balance_SR_HYP_Woodblocks",
    "/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/MalaksBane/Balance/Balance_SR_DAL_ETech_MalaksBane.Balance_SR_DAL_ETech_MalaksBane",
    "/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Balance/Balance_VLA_SR_Lyuda.Balance_VLA_SR_Lyuda",
    "/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm",
    "/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Hunted/Balance/Balance_SR_JAK_Hunted.Balance_SR_JAK_Hunted",
    #unique
    "/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/NineVolt/Balance/Balance_SM_DAHL_NineVolt.Balance_SM_DAHL_NineVolt",
    "/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror.Balance_HW_COV_Terror",
    "/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Balance/Balance_PS_VLA_BoneShredder.Balance_PS_VLA_BoneShredder",
    "/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Balance/Balance_HW_ATL_Freeman.Balance_HW_ATL_Freeman",
    "/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Hive/Balance/Balance_HW_TOR_Hive.Balance_HW_TOR_Hive",
    "/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Balance/Balance_SG_TED_Horizon.Balance_SG_TED_Horizon",
    "/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen.Balance_SR_JAK_IceQueen",
    "/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/Balance_PS_COV_Mouthpiece.Balance_PS_COV_Mouthpiece",
    "/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol.Balance_HW_VLA_Mongol",
    "/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Balance/Balance_SG_JAK_Nimble.Balance_SG_JAK_Nimble",
    "/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion.Balance_PS_COV_Contagion",
    "/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Phebert/Balance/Balance_SG_HYP_Phebert.Balance_SG_HYP_Phebert",
    "/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/PredatoryLending/Balance/Balance_SM_HYP_PredatoryLending.Balance_SM_HYP_PredatoryLending",
    "/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Rakkman/Balance/Balance_DAL_PS_Rakkman.Balance_DAL_PS_Rakkman",
    "/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/RedLiner/Balance/Balance_SG_Torgue_RedLine.Balance_SG_Torgue_RedLine",
    "/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre.Balance_PS_Tediore_Sabre",
    "/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek.Balance_SG_MAL_Shriek",
    "/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Balance/Balance_PS_COV_Skeksis.Balance_PS_COV_Skeksis",
    "/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Balance/Balance_SM_TED_SpiderMind.Balance_SM_TED_SpiderMind",
    "/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Thumper/Balance/Balance_SG_Torgue_Thumper.Balance_SG_Torgue_Thumper",
    "/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami.Balance_SM_MAL_Tsunami",
    "/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun.Balance_SM_MAL_westergun",
    "/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/Balance_HW_TOR_RYNO.Balance_HW_TOR_RYNO",
    #mission
    "/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech.Balance_PS_VLA_TheLeech",
    "/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Fork/Balance/Balance_SM_HYP_Fork.Balance_SM_HYP_Fork",
    "/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller.Balance_PS_MAL_Starkiller",
    "/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/Balance_VLA_SR_Prison.Balance_VLA_SR_Prison",
    "/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Omniloader/Balance/Balance_DAL_PS_Omniloader.Balance_DAL_PS_Omniloader",
    "/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/Balance_AR_JAK_TraitorsDeath.Balance_AR_JAK_TraitorsDeath",
    "/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/L0V3M4CH1N3/Balance/Balance_SM_HYP_L0V3M4CH1N3.Balance_SM_HYP_L0V3M4CH1N3",
    "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace.Balance_PS_JAK_AmazingGrace",
    "/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Balrog/Balance/Balance_SG_Torgue_Balrog.Balance_SG_Torgue_Balrog",
    "/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon.Balance_SM_MAL_Egon",
    "/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Balance/Balance_SR_DAL_WorldDestroyer.Balance_SR_DAL_WorldDestroyer",
    "/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/Balance_PS_COV_Chad.Balance_PS_COV_Chad",
    "/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Balance/Balance_HW_TOR_BurgerCannon.Balance_HW_TOR_BurgerCannon",
    "/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/Balance_SR_HYP_TwoTime.Balance_SR_HYP_TwoTime",
    "/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer.Balance_SM_MAL_Emporer",
    "/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Balance_AR_VLA_BigSucc.Balance_AR_VLA_BigSucc",
    "/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/Balance_SG_JAK_Fingerbiter.Balance_SG_JAK_Fingerbiter",
    "/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Balance/Balance_SR_DAL_BrashisDedication.Balance_SR_DAL_BrashisDedication",
    "/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/AmberManagement/Balance/Balance_AR_TOR_AmberManagement.Balance_AR_TOR_AmberManagement",
    "/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/Balance_AR_JAK_PasRifle.Balance_AR_JAK_PasRifle",
    "/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki.Balance_MAL_SR_Soleki",
    "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Balance/Balance_PS_JAK_Malevolent.Balance_PS_JAK_Malevolent",
    "/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/Balance_HW_COV_PortaPooper.Balance_HW_COV_PortaPooper",
    "/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/Balance_PS_ATL_Warmonger.Balance_PS_ATL_Warmonger",
    "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/Balance_PS_JAK_Buttplug.Balance_PS_JAK_Buttplug",
    "/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch.Balance_PS_MAL_SuckerPunch",
    "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TortureTruck/Balance_PS_JAK_TortureTruck.Balance_PS_JAK_TortureTruck",
    "/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Balance/Balance_SR_JAK_Hunter.Balance_SR_JAK_Hunter",
    "/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Balance/Balance_SG_TOR_Brewha.Balance_SG_TOR_Brewha",
    #one drop
    "/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Balance/Balance_AR_JAK_Bekah.Balance_AR_JAK_Bekah",
    "/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/Balance_AR_JAK_HandOfGlory,Balance_AR_JAK_HandOfGlory",
    #vday
    "/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim,Balance_SM_MAL_PolyAim",
    "/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite,Balance_SR_JAK_WeddingInvite",
    #BloodyH
    "/Game/PatchDLC/BloodyHarvest/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Fearmonger/Balance/Balance_SG_HYP_ETech_Fearmonger.Balance_SG_HYP_ETech_Fearmonger",
    "/Game/PatchDLC/BloodyHarvest/Gear/Weapons/SniperRifles/Dahl/_Design/_Unique/Frostbolt/Balance/Balance_SR_DAL_ETech_Frostbolt.Balance_SR_DAL_ETech_Frostbolt",
    #cartel
    "/Game/PatchDLC/Event2/Gear/Weapon/_Unique/YellowCake/Balance/Balance_HW_COV_ETech_YellowCake.Balance_HW_COV_ETech_YellowCake",
    "/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IceBurger/Balance/Balance_SG_HYP_IceBurger.Balance_SG_HYP_IceBurger",
    "/Game/PatchDLC/Event2/Gear/Weapon/_Unique/NeedleGun/Balance/Balance_SM_TED_NeedleGun.Balance_SM_TED_NeedleGun",

    #dlc1
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/AutoAime/Balance/Balance_SR_DAL_AutoAime.Balance_SR_DAL_AutoAime",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Boomer/Balance/Balance_SM_DAL_Boomer.Balance_SM_DAL_Boomer",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/CheapTips/Balance/Balance_SM_HYP_CheapTips.Balance_SM_HYP_CheapTips",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Craps/Balance/Balance_PS_TOR_Craps.Balance_PS_TOR_Craps",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Creamer/Balance/Balance_HW_TOR_Creamer.Balance_HW_TOR_Creamer",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/HeartBreaker/Balance/Balance_SG_HYP_HeartBreaker.Balance_SG_HYP_HeartBreaker",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Balance/Balance_SM_MAL_IonLaser.Balance_SM_MAL_IonLaser",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Nukem/Balance/Balance_HW_TOR_Nukem.Balance_HW_TOR_Nukem",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/SlowHand/Balance/Balance_SG_HYP_SlowHand.Balance_SG_HYP_SlowHand",
    #unique
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Balance/Balance_SM_MAL_EmbersPurge.Balance_SM_MAL_EmbersPurge",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Digby/Balance/Balance_DAL_AR_Digby.Balance_DAL_AR_Digby",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic,Balance_SM_HYP_JustCaustic",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/MeltFacer/Balance/BPInvPartSet_SG_HYP_MeltFacer.BPInvPartSet_SG_HYP_MeltFacer",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher.Balance_PS_JAK_RoboMasher",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Scoville/Balance/Balance_PS_TOR_Scoville.Balance_PS_TOR_Scoville",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Trash/Balance/Balance_AR_COV_Trash.Balance_AR_COV_Trash",
    "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Varlope/Balance/Balance_AR_TOR_Varlope.Balance_AR_TOR_Varlope",
    #dlc2
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider.Balance_SG_MAL_ETech_Insider",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian.Balance_SM_HYP_Oldridian",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal.Balance_AR_COV_Homicidal",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen.Balance_SG_TED_Omen",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing.Balance_SG_MAL_TheNothing",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Balance/Balance_PS_MAL_FrozenDevil.Balance_PS_MAL_FrozenDevil",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance.Balance_AR_JAK_Clairvoyance",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LittleYeeti/Balance/Balance_PS_JAK_LittleYeeti.Balance_PS_JAK_LittleYeeti",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Hydrafrost/Balance/Balance_PS_COV_Hydrafrost.Balance_PS_COV_Hydrafrost",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Kaleidoscope/Balance/Balance_DAL_PS_Kaleidoscope.Balance_DAL_PS_Kaleidoscope",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill_Legendary.Balance_PS_JAK_LoveDrill_Legendary",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant.Balance_AR_JAK_Mutant",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Balance/Balance_SM_MAL_SFForce.Balance_SM_MAL_SFForce",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Shocker/Balance/Balance_SG_Torgue_ETech_Shocker.Balance_SG_Torgue_ETech_Shocker",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Soulrender/Balance/Balance_DAL_AR_Soulrender.Balance_DAL_AR_Soulrender",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom.Balance_AR_COV_SparkyBoom",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/CockyBastard/Balance/Balance_SR_JAK_CockyBastard.Balance_SR_JAK_CockyBastard",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher.Balance_SR_JAK_Skullmasher",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/BiteSize/Balance/Balance_PS_JAK_BiteSize.Balance_PS_JAK_BiteSize",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Firecracker/Balance/Balance_SG_HYP_Firecracker.Balance_SG_HYP_Firecracker",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SacrificalLamb/Balance/Balance_SG_TED_SacrificialLamb.Balance_SG_TED_SacrificialLamb",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Balance/Balance_PS_JAK_SeventhSense.Balance_PS_JAK_SeventhSense",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheCure/Balance/Balance_SG_JAK_TheCure.Balance_SG_JAK_TheCure",
    "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Balance/Balance_PS_JAK_TheSeventhSense.Balance_PS_JAK_TheSeventhSense",
    #dlc3
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Copybeast/Balance/Balance_SM_HYP_Copybeast.Balance_SM_HYP_Copybeast",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ContainedExplosion/Balance/Balance_AR_TOR_Contained.Balance_AR_TOR_Contained",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/DowsingRod/Balance/Balance_AR_VLA_Dowsing.Balance_AR_VLA_Dowsing",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/PrivateInvestigator/Balance/Balance_DAL_PS_PrivateInvestigator.Balance_DAL_PS_PrivateInvestigator",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Plumage/Balance/Balance_HW_ATL_Plumage.Balance_HW_ATL_Plumage",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Satisfaction/Balance/Balance_HW_TOR_Satisfaction.Balance_HW_TOR_Satisfaction",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ImaginaryNumber/Balance/Balance_MAL_SR_ImaginaryNumber.Balance_MAL_SR_ImaginaryNumber",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Sheriff/Balance/Balance_PS_JAK_Sheriff.Balance_PS_JAK_Sheriff",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Decoupler/Balance/Balance_PS_MAL_Decoupler.Balance_PS_MAL_Decoupler",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/UnkemptHarold/Balance/Balance_PS_TOR_UnkemptHarold.Balance_PS_TOR_UnkemptHarold",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/SpeakEasy/Balance/Balance_SG_JAK_SpeakEasy.Balance_SG_JAK_SpeakEasy",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Frequency/Balance/Balance_SG_MAL_Frequency.Balance_SG_MAL_Frequency",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Brightside/Balance/Balance_SG_TED_Brightside.Balance_SG_TED_Brightside",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Shoveler/Balance/Balance_SG_Torgue_Shoveler.Balance_SG_Torgue_Shoveler",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Earthbound/Balance/Balance_SM_TED_Earthbound.Balance_SM_TED_Earthbound",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Antler/Balance/Balance_SG_MAL_ETech_Antler.Balance_SG_MAL_ETech_Antler",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BioBetsy/Balance/Balance_AR_COV_BioBetsy_Rad.Balance_AR_COV_BioBetsy_Rad",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BioBetsy/Balance/Balance_AR_COV_BioBetsy_Shock.Balance_AR_COV_BioBetsy_Shock",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BubbleBlaster/Balance/Balance_PS_MAL_BubbleBlaster.Balance_PS_MAL_BubbleBlaster",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/CoolBeans/Balance/Balance_AR_JAK_CoolBeans.Balance_AR_JAK_CoolBeans",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Dakota/Balance/Balance_SG_JAK_Dakota.Balance_SG_JAK_Dakota",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Fakobs/Balance/Balance_SG_JAK_Fakobs.Balance_SG_JAK_Fakobs",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/McSmugger/Balance/Balance_AR_JAK_McSmugger.Balance_AR_JAK_McSmugger",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Miscreant/Balance/Balance_PS_VLA_Miscreant.Balance_PS_VLA_Miscreant",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Narp/Balance/Balance_SR_HYP_Narp.Balance_SR_HYP_Narp",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Peashooter/Balance/Balance_PS_JAK_Peashooter.Balance_PS_JAK_Peashooter",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/QuickDraw/Balance/Balance_PS_JAK_QuickDraw.Balance_PS_JAK_QuickDraw",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Rose/Balance/Balance_PS_JAK_Rose.Balance_PS_JAK_Rose",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Splinter/Balance/Balance_SG_JAK_Splinter.Balance_SG_JAK_Splinter",
    "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/StoneThrow/Balance/Balance_AR_JAK_Stonethrow.Balance_AR_JAK_Stonethrow",
    #dlc4
    "/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Balance/Balance_SG_MAL_BlindBandit.Balance_SG_MAL_BlindBandit",
    "/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Convergence/Balance/Balance_SG_HYP_Convergence.Balance_SG_HYP_Convergence",
    "/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/LovableRogue/Balance/Balance_AR_TOR_LovableRogue.Balance_AR_TOR_LovableRogue",
    "/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/PAT_Mk3/Balance/Balance_SM_TED_PatMk3.Balance_SM_TED_PatMk3",
    "/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Voice/Balance/Balance_PS_TOR_Voice.Balance_PS_TOR_Voice",
    "/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/AshenBeast/Balance/Balance_SM_DAL_ETech_AshenBeast.Balance_SM_DAL_ETech_AshenBeast",
    "/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BanditLauncher/Balance/Balance_HW_COV_BanditLauncher.Balance_HW_COV_BanditLauncher",
    "/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Sawhorse/Balance/Balance_AR_COV_Sawhorse.Balance_AR_COV_Sawhorse",
    "/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Septimator/Balance/Balance_VLA_SR_Septimator.Balance_VLA_SR_Septimator",
]

def r_gun(_in_):
    return "(InventoryBalanceData={},ResolvedInventoryBalanceData=InventoryBalanceData'{}')".format(loot_base[_in_],loot_base[_in_])

loot_pool = [
        '/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPool_Mayhem2_Legendaries.ItemPool_Mayhem2_Legendaries',
        '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_COVEnemyUse_HeavyWeapons.ItemPool_COVEnemyUse_HeavyWeapons',
        '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary.ItemPool_Guns_Legendary',
        '/Game/GameData/Loot/ItemPools/Guns/ItemPool_AR_Shotgun_SMG_Legendary.ItemPool_AR_Shotgun_SMG_Legendary',
        '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Sniper_Heavy_Legendary.ItemPool_Sniper_Heavy_Legendary',
        '/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Legendary.ItemPool_AssaultRifles_Legendary',
        '/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Legendary.ItemPool_Heavy_Legendary',
        '/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary.ItemPool_Shotguns_Legendary',
        '/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Legendary.ItemPool_SMGs_Legendary'
        '/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary.ItemPool_SnipeRifles_Legendary',
        '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Legendary.ItemPool_Pistols_Legendary',
        '/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries.ItemPool_Mayhem4_Legendaries',
        '/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hib_SnipeRifles_Legendary.ItemPool_Hib_SnipeRifles_Legendary',
        '/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Guns_Legendary.ItemPool_Hibiscus_Guns_Legendary'
    ]

nav_list = [
    '/Game/Common/_Design/AI/Navigation/AIPath_Default.AIPath_Default',
    '/Game/Enemies/ServiceBot/_Shared/_Design/Navigation/AIPath_ServiceBot.AIPath_ServiceBot',
    '/Game/Enemies/Mech/_Shared/_Design/Navigation/AIPath_Mech.AIPath_Mech',
    '/Game/Enemies/Rakk/_Shared/_Design/Navigation/AIPath_RakkFlightless.AIPath_RakkFlightless',
    '/Game/Enemies/Nog/_Shared/_Design/Navigation/AIPath_Nog.AIPath_Nog',
    '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Navigation/AIPath_WeeLoaderBadass.AIPath_WeeLoaderBadass'
]
htype_base = "'/Game/GameData/ResourcePools/"
htype = [
    "HealthTypeData=HealthTypeData{}HealthTypes/HealthType_Flesh.HealthType_Flesh'".format(htype_base),
    "HealthTypeData=HealthTypeData{}HealthTypes/HealthType_Armor.HealthType_Armor'".format(htype_base),
    "HealthTypeData=HealthTypeData{}HealthTypes/HealthType_Shield.HealthType_Shield'".format(htype_base),
    "HealthTypeData=HealthTypeData{}HealthTypes/HealthType_Flesh.HealthType_Flesh'".format(htype_base),
    "HealthTypeData=HealthTypeData{}HealthTypes/HealthType_Flesh.HealthType_Flesh'".format(htype_base)
]
hpool = [
    "HealthPoolData=GameResourcePoolData{}ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary'".format(htype_base),
    "HealthPoolData=GameResourcePoolData{}ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary'".format(htype_base),
    "HealthPoolData=GameResourcePoolData{}ResourcePool_AI_Health_03_Tertiary.ResourcePool_AI_Health_03_Tertiary'".format(htype_base),
    "HealthPoolData=GameResourcePoolData{}ResourcePool_AI_Health_04_Quaternary.ResourcePool_AI_Health_04_Quaternary'".format(htype_base),
    "HealthPoolData=GameResourcePoolData{}ResourcePool_AI_Health_05_Quinary.ResourcePool_AI_Health_05_Quinary'".format(htype_base)
]
def hfull(tin_,pin_,pct = 1.00000):
    return "({},{},bUseChanceToExist=True,ChanceToExist=(BaseValueConstant={}))".format(htype[tin_],hpool[pin_],pct)

               
def spawn_conf(rnd,wave,ab,res):
    r = int('{}{}{}'.format(rnd,wave,ab))
    m_name = {
        111: "OakMissionSpawner_Round1Wave",
        112: "OakMissionSpawner_Round1Wave",
        121: "OakMissionSpawner_Round1Wave_0",
        122: "OakMissionSpawner_Round1Wave_0",
        123: "Round1Wave",
        131: "OakMissionSpawner_Round1Wave_5",
        132: "OakMissionSpawner_Round1Wave_5",
        211: "OakMissionSpawner_Round2Wave",
        221: "OakMissionSpawner_Round2Wave_1",
        222: "OakMissionSpawner_Round2Wave_1",
        231: "OakMissionSpawner_Round2Wave_2",
        232: "OakMissionSpawner_Round2Wave_2",
        233: "Round2Wave3Dropship",
        241: "OakMissionSpawner_Round2Wave_3",
        242: "OakMissionSpawner_Round2Wave_3",
        311: "OakMissionSpawner_Round3Wave",
        312: "OakMissionSpawner_Round3Wave",
        321: "OakMissionSpawner_Round3Wave_4",
        322: "OakMissionSpawner_Round3Wave_4",
        323: "Round3Wave2_BehindDropship",
        331: "OakMissionSpawner_Round3Wave_5",
        332: "OakMissionSpawner_Round3Wave_5",
        341: "OakMissionSpawner_Round3Wave_6",
        411: "OakMissionSpawner_Round4Wave",
        421: "OakMissionSpawner_Round4Wave_7",
        431: "OakMissionSpawner_Round4Wave_8",
        432: "OakMissionSpawner_Round4Wave_8",
        441: "OakMissionSpawner_Round4Wave_9",
        442: "OakMissionSpawner_Round4Wave_9",
        443: "Round4_Wave_5",
        511: "OakMissionSpawner_Round5Wave",
        512: "OakMissionSpawner_Round5Wave",
        521: "OakMissionSpawner_Round5Wave_0",
        522: "OakMissionSpawner_Round5Wave_0",
        531: "OakMissionSpawner_Round5Wave_10",
        532: "OakMissionSpawner_Round5Wave_10",
        533: "Round5Wave3_Dropship",
        541: "OakMissionSpawner_Round5Wave_11",
        542: "OakMissionSpawner_Round5Wave_11",
        551: "OakMissionSpawner_Round5Wave_12",
        552: "OakMissionSpawner_Round5Wave_12",
        561: "OakMissionSpawner_Round5Wave_13",
        562: "OakMissionSpawner_Round5Wave_13"
    }.get(r,'!m_name_{}'.format(r))
    m_spawn = {
        111: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1a_Trooper1',
        112: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1b_TrooperBscShtGn',
        121: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2a_Trooper',
        122: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2b_TrprShtMleJtpk',
        123: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2a_Trooper',
        131: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3a',
        132: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3b',
        211: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave1',
        221: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2a',
        222: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2b',
        231: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3a',
        232: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3b',
        233: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3a',
        241: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4a',
        242: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4b',
        311: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1a',
        312: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1b',
        321: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2a',
        322: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2b',
        323: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2a',
        331: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3a',
        332: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3b',
        341: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave4a',
        411: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave1',
        421: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave2',
        431: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3a',
        432: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3b',
        441: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4a',
        442: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4b',
        443: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4a',
        511: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1a',
        512: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1b',
        521: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2a',
        522: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2b',
        531: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3a',
        532: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3b',
        533: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3b',
        541: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4a',
        542: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4b',
        551: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave5',
        552: '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave5',
        561: '/Game/Enemies/_Spawning/ProvingGrounds/Trial7/SpawnOptions_PGTrial7_Maliwan_MechAdds',
        562: '/Game/Enemies/_Spawning/ProvingGrounds/Trial7/SpawnOptions_PGTrial7_Maliwan_MechAdds'
    }.get(r,'!m_spawn_{}'.format(r))
    m_mob = {
        111: 6.0,
        112: 6.0,
        121: 3.0,
        122: 8.0,
        123: 7.0,
        131: 4.0,
        132: 4.0,
        211: 5.0,
        221: 6.0,
        222: 6.0,
        231: 5.0,
        232: 6.0,
        233: 4.0,
        241: 6.0,
        242: 6.0,
        311: 6.0,
        312: 6.0,
        321: 6.0,
        322: 5.0,
        323: 7.0,
        331: 6.0,
        332: 8.0,
        341: 6.0,
        411: 6.0,
        421: 6.0,
        431: 6.0,
        432: 6.0,
        441: 6.0,
        442: 5.0,
        443: 7.0,
        511: 6.0,
        512: 6.0,
        521: 6.0,
        522: 6.0,
        531: 6.0,
        532: 5.0,
        533: 4.0,
        541: 6.0,
        542: 6.0,
        551: 6.0,
        552: 7.0,
        561: 6.0,
        562: 7.0
    }.get(r,'!m_mob_{}'.format(r))
    m_act = {
        111: 6.0,
        112: 6.0,
        121: 3.0,
        122: 8.0,
        131: 4.0,
        132: 4.0,
        211: 6.0,
        221: 6.0,
        222: 6.0,
        231: 5.0,
        232: 6.0,
        241: 6.0,
        242: 6.0,
        311: 6.0,
        312: 6.0,
        321: 6.0,
        322: 5.0,
        331: 6.0,
        332: 8.0,
        341: 6.0,
        411: 6.0,
        421: 6.0,
        431: 6.0,
        432: 6.0,
        441: 6.0,
        442: 8.0,
        511: 6.0,
        512: 6.0,
        521: 6.0,
        522: 6.0,
        531: 6.0,
        532: 5.0,
        541: 6.0,
        542: 6.0,
        551: 6.0,
        552: 7.0,
        561: 6.0,
        562: 7.0
    }.get(r,'!m_act_{}'.format(r))
    m_end = {
        111: 8.0,
        112: 8.0,
        121: 6.0,
        122: 12.0,
        131: 8.0,
        132: 8.0,
        211: 12.0,
        221: 6.0,
        222: 10.0,
        231: 8.0,
        232: 10.0,
        241: 12.0,
        242: 12.0,
        311: 12.0,
        312: 12.0,
        321: 12.0,
        322: 8.0,
        331: 10.0,
        332: 10.0,
        341: 10.0,
        411: 12.0,
        421: 12.0,
        431: 12.0,
        432: 12.0,
        441: 12.0,
        442: 10.0,
        511: 12.0,
        512: 12.0,
        521: 12.0,
        522: 12.0,
        531: 12.0,
        532: 8.0,
        541: 12.0,
        542: 12.0,
        551: 12.0,
        552: 15.0,
        561: 12.0,
        562: 15.0,
    }.get(r,'!m_end_{}'.format(r))

    return {
        'mission': m_name,
        'spawn': m_spawn,
        'alive_passive': m_act,
        'alive_end': m_end,
        'mobs': m_mob
    }.get(res,'!ERR_{}'.format(res))

def BPChar_TrooperBasic_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderBasicJUNK.BPChar_LoaderBasicJUNK_C'",
        1: '(x=75,y=75,z=115)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_JNK,1.8,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperBasicDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/Basic/_Design/Character/BPChar_LoaderBasic.BPChar_LoaderBasic_C'",
        1: '(x=75,y=75,z=115)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_Gun,1.85,2.0,2.0,2.0,2.0,Normal,1.0',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperShotgun_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderSGT_JUNK.BPChar_LoaderSGT_JUNK_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1,Loader_SGT,2.3,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperShotgunDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/SGT/_Design/Character/BPChar_LoaderSGT.BPChar_LoaderSGT_C'",
        1: '(x=70,y=70,z=90)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_SGT,2.5,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperBadass_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderBadass_JUNK.BPChar_LoaderBadass_JUNK_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1,Loader_Badass,10.0,3.0,3.0,3.0,3.0,Badass,2.0',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperBadassDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/BrotherlyLove/_Design/Character/BPChar_SisterlyLove_DebtCollectorLoader.BPChar_SisterlyLove_DebtCollectorLoader_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,DebtCollector,13.0,1.0,1.0,1.0,1.0,SuperBadass,2.2',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperMelee_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderEXP_JUNK.BPChar_LoaderEXP_JUNK_C'",
        1: '(x=70,y=70,z=119)', 
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1,Loader_EXP,1.0,1.0,1.0,1.0,1.0,Normal,5.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperMeleeDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/EXP/_Design/Character/BPChar_LoaderEXP.BPChar_LoaderEXP_C'",
        1: '(x=40,y=40,z=120)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_EXP,1.1,1.0,1.0,1.0,1.0,Normal,7.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperJetpack_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/BL2_Loader/_Design/Character/BPChar_Loader_BL2.BPChar_Loader_BL2_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1,Loader_BL2,1.0,1.0,1.0,1.0,1.0,Normal,0.8',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperJetpackDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/AcidTrip/EarlyPrototypes/_Design/Character/BPChar_AcidTrip_EarlyPrototype.BPChar_AcidTrip_EarlyPrototype_C'",
        1: '(x=75,y=75,z=115)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,DebtCollector,15.0,3.0,3.0,3.0,3.0,SuperBadass,1.5',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_Basic_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/ElementalCryo/_Design/Character/BPChar_LoaderElementalCryo.BPChar_LoaderElementalCryo_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1,Loader_CRY,2.0,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_BasicDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/ElementalFire/_Design/Character/BPChar_LoaderElementalFire.BPChar_LoaderElementalFire_C'",
        1: '(x=90,y=90,z=110)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1,Loader_HOT,2.0,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_HeavyGunner_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/RPG/_Design/Character/BPChar_LoaderRPG.BPChar_LoaderRPG_C'",
        1: '(x=50,y=50,z=85)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1,Loader_RPG,2.0,1.0,1.0,1.0,1.0,Normal,0.8',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_HeavyGunnerDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/Badass/_Design/Character/BPChar_LoaderBadass.BPChar_LoaderBadass_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_Badass,14.5,3.0,3.0,3.0,3.0,Badass,1.8',
        3: 'twoguns', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperMedic_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Basic/_Design/Character/BPChar_SurveyorBasic.BPChar_SurveyorBasic_C'",
        1: '(x=34,y=34,z=88)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,SurveyorBasic_PT2,0.7,0.4,1.0,1.0,1.0,VeryGood,0.25',
        3: 'all',
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperMedicDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Badass/_Design/Character/BPChar_SurveyorBadass.BPChar_SurveyorBadass_C'",
        1: '(x=100,y=100,z=100)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,Surveyor_BadassPT2,1.4,1.0,1.0,1.0,1.0,Badass,0.5',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperFlash_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/RIOT/_Design/Character/BPChar_LoaderRIOT.BPChar_LoaderRIOT_C'",
        1: '(x=40,y=40,z=115)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1,Loader_RIOT,3.0,1.0,1.0,1.0,1.0,Normal,1.2',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperFlashDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/SVY/_Design/Character/BPChar_LoaderSVY.BPChar_LoaderSVY_C'",
        1: '(x=75,y=75,z=115)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_SVY,1.6,1.0,1.0,1.0,1.0,Normal,0.9',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_Powerhouse_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion.BPChar_VIPOnly_Dandelion_C'",
        1: '(x=45,y=45,z=110)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Dandellion,10.0,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_PowerhouseDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Petunia_FreddieBot/_Design/Character/BPChar_VIPOnly_Petunia.BPChar_VIPOnly_Petunia_C'",
        1: '(x=60,y=60,z=115)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Petunia,10.0,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_Icebreaker_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/Badass/_Design/Character/BPChar_LoaderBadass.BPChar_LoaderBadass_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_Badass,14.5,3.0,3.0,3.0,3.0,Badass,1.8',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_IcebreakerDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/Badass/_Design/Character/BPChar_LoaderBadass.BPChar_LoaderBadass_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_Badass,14.5,3.0,3.0,3.0,3.0,Badass,1.8',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_Acidrain_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/Badass/_Design/Character/BPChar_LoaderBadass.BPChar_LoaderBadass_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_Badass,14.5,3.0,3.0,3.0,3.0,Badass,1.8',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_AcidrainDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/AcidTrip/Facemelt/_Design/Character/BPChar_AcidTrip_Facemelt.BPChar_AcidTrip_Facemelt_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Facemelt,12.0,1.0,1.0,1.0,1.0,Badass,1.5',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_Badass_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/Badass/_Design/Character/BPChar_LoaderBadass.BPChar_LoaderBadass_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_Badass,14.5,3.0,3.0,3.0,3.0,Badass,1.8',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_BadassDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/AcidTrip/Facemelt/_Design/Character/BPChar_AcidTrip_Facemelt.BPChar_AcidTrip_Facemelt_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Facemelt,12.0,1.0,1.0,1.0,1.0,Badass,1.5',
        3: 'onegun', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_NogBasic_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBasic/_Design/Character/BPChar_WeeLoaderBasic.BPChar_WeeLoaderBasic_C'",
        1: '(x=25,y=25,z=50)',
        2: '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Balance/Table_Balance_WeeLoaderBadass_PT2,Basic,0.75,1.0,1.0,1.0,2.0,None,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_NogBasicDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBadass/_Design/Character/BPChar_WeeLoaderBadass.BPChar_WeeLoaderBadass_C'",
        1: '(x=25,y=25,z=50)',
        2: '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Balance/Table_Balance_WeeLoaderBadass_PT2,BadassWeePT2,5.5,1.0,1.0,1.0,1.0,SuperBadass,1.35',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_NogNinja_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBasic/_Design/Character/BPChar_WeeLoaderBasic.BPChar_WeeLoaderBasic_C'",
        1: '(x=25,y=25,z=50)',
        2: '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Balance/Table_Balance_WeeLoaderBadass_PT2,Basic,0.75,1.0,1.0,1.0,2.0,None,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_NogNinjaDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBadass/_Design/Character/BPChar_WeeLoaderBadass.BPChar_WeeLoaderBadass_C'",
        1: '(x=25,y=25,z=50)',
        2: '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Balance/Table_Balance_WeeLoaderBadass_PT2,BadassWeePT2,5.5,1.0,1.0,1.0,1.0,SuperBadass,1.35',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_NogBadassDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBadass/_Design/Character/BPChar_WeeLoaderBadass.BPChar_WeeLoaderBadass_C'",
        1: '(x=25,y=25,z=50)',
        2: '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Balance/Table_Balance_WeeLoaderBadass_PT2,BadassWeePT2,5.5,1.0,1.0,1.0,1.0,SuperBadass,1.35',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_NogNogromancer_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBasic/_Design/Character/BPChar_WeeLoaderBasic.BPChar_WeeLoaderBasic_C'",
        1: '(x=25,y=25,z=50)',
        2: '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Balance/Table_Balance_WeeLoaderBadass_PT2,Basic,0.75,1.0,1.0,1.0,2.0,None,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_FrontrunnerBasic_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/ServiceBot/Basic/_Design/character/BPChar_CasinoBot_Basic.BPChar_CasinoBot_Basic_C'",
        1: '(x=50,y=50,z=85)',
        2: '/Game/PatchDLC/Dandelion/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_CasinoBot,CasinoBot_Basic,1.1,1.0,1.0,2.0,2.0,Normal,0.25',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Frontrunner_Badass_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/ServiceBot/Bouncer/_Design/Character/BPChar_ServiceBot_Bouncer.BPChar_ServiceBot_Bouncer_C'",
        1: '(x=50,y=50,z=85)',
        2: '/Game/PatchDLC/Dandelion/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_CasinoBot,CasinoBot_Bouncer,1.1,1.0,1.0,2.0,2.0,Normal,0.45',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_FrontrunnerJammer_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/ServiceBot/Basic/_Design/character/BPChar_CasinoBot_Basic.BPChar_CasinoBot_Basic_C'",
        1: '(x=50,y=50,z=85)',
        2: '/Game/PatchDLC/Dandelion/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_CasinoBot,CasinoBot_Basic,1.5,1.5,2.0,3.0,3.0,Normal,1.45',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_FrontrunnerStriker_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/ServiceBot/Bouncer/_Design/Character/BPChar_ServiceBot_Bouncer.BPChar_ServiceBot_Bouncer_C'",
        1: '(x=50,y=50,z=85)',
        2: '/Game/PatchDLC/Dandelion/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_CasinoBot,CasinoBot_Bouncer,1.1,1.0,1.0,2.0,2.0,Normal,0.45',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Oversphere_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Basic/_Design/Character/BPChar_SurveyorBasic.BPChar_SurveyorBasic_C'",
        1: '(x=34,y=34,z=88)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,SurveyorBasic_PT2,0.7,0.4,1.0,1.0,1.0,VeryGood,0.25',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_OversphereDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Badass/_Design/Character/BPChar_SurveyorBadass.BPChar_SurveyorBadass_C'",
        1: '(x=100,y=100,z=100)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,Surveyor_BadassPT2,1.4,1.0,1.0,1.0,1.0,Badass,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_OversphereDefender_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Basic/_Design/Character/BPChar_SurveyorBasic.BPChar_SurveyorBasic_C'",
        1: '(x=34,y=34,z=88)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,SurveyorBasic_PT2,0.7,0.4,1.0,1.0,1.0,VeryGood,0.25',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_OversphereDefenderDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Badass/_Design/Character/BPChar_SurveyorBadass.BPChar_SurveyorBadass_C'",
        1: '(x=100,y=100,z=100)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,Surveyor_BadassPT2,1.4,1.0,1.0,1.0,1.0,Badass,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_OversphereHarbinger_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Basic/_Design/Character/BPChar_SurveyorBasic.BPChar_SurveyorBasic_C'",
        1: '(x=34,y=34,z=88)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,SurveyorBasic_PT2,0.7,0.4,1.0,1.0,1.0,VeryGood,0.25',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_OversphereHarbingerDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Badass/_Design/Character/BPChar_SurveyorBadass.BPChar_SurveyorBadass_C'",
        1: '(x=100,y=100,z=100)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,Surveyor_BadassPT2,1.4,1.0,1.0,1.0,1.0,Badass,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_OversphereStinger_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Basic/_Design/Character/BPChar_SurveyorBasic.BPChar_SurveyorBasic_C'",
        1: '(x=34,y=34,z=88)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,SurveyorBasic_PT2,0.7,0.4,1.0,1.0,1.0,VeryGood,0.25',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_OversphereStingerDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Badass/_Design/Character/BPChar_SurveyorBadass.BPChar_SurveyorBadass_C'",
        1: '(x=100,y=100,z=100)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,Surveyor_BadassPT2,1.4,1.0,1.0,1.0,1.0,Badass,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_OversphereBadass_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Surveyor/Badass/_Design/Character/BPChar_SurveyorBadass.BPChar_SurveyorBadass_C'",
        1: '(x=100,y=100,z=100)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Surveyor/_Shared/_Design/Balance/Table_Balance_Surveyor,Surveyor_BadassPT2,1.4,1.0,1.0,1.0,1.0,Badass,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_MechBasic_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Loader/Badass/_Design/Character/BPChar_LoaderBadass_Venchy.BPChar_LoaderBadass_Venchy_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT2,Loader_Badass,14.5,3.0,3.0,3.0,3.0,Badass,1.8',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_MechBasicDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/AcidTrip/Facemelt/_Design/Character/BPChar_AcidTrip_Facemelt.BPChar_AcidTrip_Facemelt_C'",
        1: '(x=80,y=80,z=119)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Facemelt,12.0,1.0,1.0,1.0,1.0,Badass,1.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_MechCharger_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion.BPChar_VIPOnly_Dandelion_C'",
        1: '(x=45,y=45,z=110)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Dandellion,10.0,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_MechGrenadier_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion.BPChar_VIPOnly_Dandelion_C'",
        1: '(x=45,y=45,z=110)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Dandellion,10.0,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_MechMG_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion.BPChar_VIPOnly_Dandelion_C'",
        1: '(x=45,y=45,z=110)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Dandellion,10.0,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

def BPChar_MechChargerDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion.BPChar_VIPOnly_Dandelion_C'",
        1: '(x=45,y=45,z=110)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Dandellion,10.0,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_MechGrenadierDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Petunia_FreddieBot/_Design/Character/BPChar_VIPOnly_Petunia.BPChar_VIPOnly_Petunia_C'",
        1: '(x=60,y=60,z=115)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Petunia,10.0,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_MechMGDark_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion.BPChar_VIPOnly_Dandelion_C'",
        1: '(x=45,y=45,z=110)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques,Dandellion,10.0,1.0,1.0,1.0,1.0,Normal,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
#DropShip fixes

#round1
def BPChar_TrooperBadass_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass_Looter.BPChar_EnforcerBadass_Looter_C'",
        1: '(x=50,y=50,z=105)',
        2: '/Dandelion/Enemies/Looters/Enforcer/_Shared/_Design/Balance/Table_Enforcer_BalanceLooters,Enforcer_Badass,5.5,2.0,4.0,4.0,4.0,Badass,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperShotgun_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Punk/Shotgunner/_Design/Character/BPChar_PunkShotgunner_Looter.BPChar_PunkShotgunner_Looter_C'",
        1: '(x=34,y=34,z=85)',
        2: '/Dandelion/Enemies/Looters/Punk/_Shared/_Design/Balance/Table_Balance_PunkLooters,Punk_Shotgunner,1.0,1.0,1.0,1.0,1.0,None,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperMelee_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Psycho/Basic/_Design/Character/BPChar_PsychoBasic_Looter.BPChar_PsychoBasic_Looter_C'",
        1: '(x=34,y=34,z=88)',
        2: '/Dandelion/Enemies/Looters/Psycho/_Shared/_Design/Balance/Table_PsychoLooters_Balance,Psycho_BasicLooter,1.0,1.0,1.0,1.0,1.0,Normal,0.33',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperBasic_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Enforcer/Bruiser/_Design/Character/BPChar_EnforcerBruiser_Looter.BPChar_EnforcerBruiser_Looter_C'",
        1: '(x=50,y=50,z=100)',
        2: '/Dandelion/Enemies/Looters/Enforcer/_Shared/_Design/Balance/Table_Enforcer_BalanceLooters,Enforcer_Gun,3.0,1.5,3.5,3.5,3.5,None,0.4',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

def BPChar_TrooperBadass_C_FIX_(_in_):
    return {
        0: "BlueprintGeneratedClass'/Alisma/Enemies/HyperionEnforcer/Badass/_Design/Character/BPChar_HyperionEnforcerBadass.BPChar_HyperionEnforcerBadass_C'",
        1: '(x=50,y=50,z=105)',
        2: '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance,Enforcer_Badass,5.5,2.0,4.0,4.0,4.0,Badass,0.4',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperShotgun_C_FIX_(_in_):
    return {
        0: "BlueprintGeneratedClass'/Alisma/Enemies/HyperionEnforcer/Gun/_Design/Character/BPChar_HyperionEnforcerGun.BPChar_HyperionEnforcerGun_C'",
        1: '(x=50,y=50,z=100)',
        2: '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance,Enforcer_Gun,3.0,1.5,3.5,3.5,3.5,None,0.4',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperMelee_C_FIX_(_in_):
    return {
        0: "BlueprintGeneratedClass'/Alisma/Enemies/HyperionEnforcer/Melee/_Design/Character/BPChar_HyperionEnforcerMelee.BPChar_HyperionEnforcerMelee_C'",
        1: '(x=50,y=50,z=100)',
        2: '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance,Enforcer_Melee,2.5,1.0,2.5,2.5,2.5,None,0.33',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperBasic_C_FIX_(_in_):
    return {
        0: "BlueprintGeneratedClass'/Alisma/Enemies/HyperionEnforcer/Basic/_Design/Character/BPChar_HyperionEnforcerBasic.BPChar_HyperionEnforcerBasic_C'",
        1: '(x=50,y=50,z=100)',
        2: '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance,Enforcer_Shield,2.5,1.0,2.5,2.5,2.5,None,0.33',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

#round2
def BPChar_TrooperMeleeDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Punk/Shotgunner/_Design/Character/BPChar_PunkShotgunner_Looter.BPChar_PunkShotgunner_Looter_C'",
        1: '(x=34,y=34,z=85)',
        2: '/Dandelion/Enemies/Looters/Punk/_Shared/_Design/Balance/Table_Balance_PunkLooters,Punk_Shotgunner,1.0,1.0,1.0,1.0,1.0,None,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_HeavyGunner_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Psycho/Basic/_Design/Character/BPChar_PsychoBasic_Looter.BPChar_PsychoBasic_Looter_C'",
        1: '(x=34,y=34,z=88)',
        2: '/Dandelion/Enemies/Looters/Psycho/_Shared/_Design/Balance/Table_PsychoLooters_Balance,Psycho_BasicLooter,1.0,1.0,1.0,1.0,1.0,Normal,0.33',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperBasicDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Punk/Badass/_Design/Character/BPChar_PunkBadass_Looter.BPChar_PunkBadass_Looter_C'",
        1: '(x=34,y=34,z=100)',
        2: '/Dandelion/Enemies/Looters/Punk/_Shared/_Design/Balance/Table_Balance_PunkLooters,Punk_Badass,5.5,1.0,1.0,1.0,1.0,Badass,2.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperJetpackDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Goliath/Basic/_Design/Character/BPChar_GoliathBasic_Looter.BPChar_GoliathBasic_Looter_C'",
        1: '(x=64,y=64,z=120)',
        2: '/Dandelion/Enemies/Looters/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Looter,Basic,5.0,2.5,3.0,3.0,3.0,None,0.4',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperMedicDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Goon/Basic/_Design/Character/BPChar_GoonBasic_looter.BPChar_GoonBasic_Looter_C'",
        1: '(x=75,y=75,z=125)',
        2: '/Dandelion/Enemies/Looters/Goon/_Shared/_Design/Balance/Table_Balance_GoonLooter,Goon_BasicLooter,5.0,1.0,1.0,1.0,1.0,VeryGood,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperFlashDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Psycho/Basic/_Design/Character/BPChar_PsychoBasic_Looter.BPChar_PsychoBasic_Looter_C'",
        1: '(x=34,y=34,z=88)',
        2: '/Dandelion/Enemies/Looters/Psycho/_Shared/_Design/Balance/Table_PsychoLooters_Balance,Psycho_BasicLooter,1.0,1.0,1.0,1.0,1.0,Normal,0.33',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_TrooperShotgunDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Tink/Shotgun/_Design/Character/BPChar_TinkShotgun_Looter.BPChar_TinkShotgun_Looter_C'",
        1: '(x=34,y=34,z=60)',
        2: '/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters,Tink_Shotgun,1.0,1.0,1.0,1.0,1.0,None,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

#ROUND3
def BPChar_FrontrunnerBasic_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Tink/Badass/_Design/Character/BPChar_TinkBadass_Looter.BPChar_TinkBadass_Looter_C'",
        1: '(x=34,y=34,z=65)',
        2: '/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters,Tink_Badass,6.0,2.0,2.0,1.0,1.0,Badass,0.7',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_HeavyGunnerDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Tink/Shotgun/_Design/Character/BPChar_TinkShotgun_Looter.BPChar_TinkShotgun_Looter_C'",
        1: '(x=34,y=34,z=60)',
        2: '/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters,Tink_Shotgun,1.0,1.0,1.0,1.0,1.0,None,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_PowerhouseDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Punk/Badass/_Design/Character/BPChar_PunkBadass_Looter.BPChar_PunkBadass_Looter_C'",
        1: '(x=34,y=34,z=100)',
        2: '/Dandelion/Enemies/Looters/Punk/_Shared/_Design/Balance/Table_Balance_PunkLooters,Punk_Badass,5.5,1.0,1.0,1.0,1.0,Badass,2.0',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_NogBasic_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Tink/Shotgun/_Design/Character/BPChar_TinkShotgun_Looter.BPChar_TinkShotgun_Looter_C'",
        1: '(x=34,y=34,z=60)',
        2: '/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters,Tink_Shotgun,1.0,1.0,1.0,1.0,1.0,None,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_BasicDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Goliath/Basic/_Design/Character/BPChar_GoliathBasic_Looter.BPChar_GoliathBasic_Looter_C'",
        1: '(x=64,y=64,z=120)',
        2: '/Dandelion/Enemies/Looters/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Looter,Basic,5.0,2.5,3.0,3.0,3.0,None,0.4',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_Heavy_BadassDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Goliath/Midget/_Design/Character/BPChar_GoliathMidget_Looter.BPChar_GoliathMidget_Looter_C'",
        1: '(x=45,y=45,z=72)',
        2: '/Dandelion/Enemies/Looters/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Looter,Midget,4.5,1.9,3.0,3.0,3.0,None,0.4',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

#ROUND4
def BPChar_Frontrunner_Badass_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Tink/Badass/_Design/Character/BPChar_TinkBadass_Looter.BPChar_TinkBadass_Looter_C'",
        1: '(x=34,y=34,z=65)',
        2: '/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters,Tink_Badass,6.0,2.0,2.0,1.0,1.0,Badass,0.7',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_FrontrunnerJammer_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Goliath/Midget/_Design/Character/BPChar_GoliathMidget_Looter.BPChar_GoliathMidget_Looter_C'",
        1: '(x=45,y=45,z=72)',
        2: '/Dandelion/Enemies/Looters/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Looter,Midget,4.5,1.9,3.0,3.0,3.0,None,0.4',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

#ROUND5
def BPChar_MechBasicDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Goliath/Badass/_Design/Character/BPChar_GoliathBadass_Looter.BPChar_GoliathBadass_Looter_C'",
        1: '(x=64,y=64,z=120)',
        2: '/Dandelion/Enemies/Looters/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Looter,Badass,8.0,4.0,4.0,4.0,4.0,Badass,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_MechChargerDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Tink/Badass/_Design/Character/BPChar_TinkBadass_Looter.BPChar_TinkBadass_Looter_C'",
        1: '(x=34,y=34,z=65)',
        2: '/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters,Tink_Badass,6.0,2.0,2.0,1.0,1.0,Badass,0.7',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_MechGrenadierDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Tink/Shotgun/_Design/Character/BPChar_TinkShotgun_Looter.BPChar_TinkShotgun_Looter_C'",
        1: '(x=34,y=34,z=60)',
        2: '/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters,Tink_Shotgun,1.0,1.0,1.0,1.0,1.0,None,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_MechMGDark_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Tink/Badass/_Design/Character/BPChar_TinkBadass_Looter.BPChar_TinkBadass_Looter_C'",
        1: '(x=34,y=34,z=65)',
        2: '/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters,Tink_Badass,6.0,2.0,2.0,1.0,1.0,Badass,0.7',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def BPChar_FrontrunnerStriker_C_FIX(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Looters/Punk/ArmoredVIP/_Design/Character/BPChar_PunkArmored_LooterVIP.BPChar_PunkArmored_LooterVIP_C'",
        1: '(x=34,y=34,z=100)',
        2: '/Dandelion/Enemies/Looters/Punk/_Shared/_Design/Balance/Table_Balance_PunkLooters,Punk_PrettyBoy,2.5,2.0,1.5,1.0,1.0,VeryGood,0.7',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")


def WORK1(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBadass/_Design/Character/BPChar_WeeLoaderBadass.BPChar_WeeLoaderBadass_C'",
        1: '(x=25,y=25,z=50)',
        2: '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Balance/Table_Balance_WeeLoaderBadass_PT2,BadassWeePT2,5.5,1.0,1.0,1.0,1.0,SuperBadass,1.35',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

def WORK2(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Claptrap/Swarm/_Design/Character/BPChar_ClaptrapSwarm.BPChar_ClaptrapSwarm_C'",
        1: '(x=50,y=50,z=65)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Claptrap/_Shared/_Design/Balance/Table_Balance_Claptrap_PT1,Feral_PT2,1.0,0.7,1.0,1.0,1.0,VeryGood,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

def WORK3(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Claptrap/Claptrap_Queen/_Design/Character/BPChar_ClaptrapQueen.BPChar_ClaptrapQueen_C'",
        1: '(x=90,y=90,z=90)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Claptrap/_Shared/_Design/Balance/Table_Balance_Claptrap_PT1,Queen_PT2,45.0,1.0,1.0,1.0,1.0,VeryGood,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[1], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def WORK4(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Character/BPChar_WeeLoaderShared.BPChar_WeeLoaderShared_C'",
        1: '(x=25,y=25,z=50)',
        2: '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Balance/Table_Balance_WeeLoaderBadass_PT2,Basic,0.75,1.0,1.0,1.0,2.0,None,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: "AnimBlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/Animation/BPAnim_WeeLoader.BPAnim_WeeLoader_C'", # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def WORK4_(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/WeeLoader/WeeLoaderBasic/_Design/Character/BPChar_WeeLoaderBasic.BPChar_WeeLoaderBasic_C'",
        1: '(x=25,y=25,z=50)',
        2: '/Game/PatchDLC/Dandelion/Enemies/WeeLoader/_Shared/_Design/Balance/Table_Balance_WeeLoaderBadass_PT2,Basic,0.75,1.0,1.0,1.0,2.0,None,0.5',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

def NWORK5(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/Mimic/Basic/_Design/Character/BPChar_MimicBasic.BPChar_MimicBasic_C'",
        1: '(x=80,y=80,z=120)',
        2: '/Dandelion/Enemies/Mimic/_Shared/_Design/Balance/Table_Balance_Mimic,Mimic_PT2,1.2,0.9,1.0,1.0,1.0,Badass,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

def WORK7(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Character/BPChar_GiganticMech1.BPChar_GiganticMech1_C'",
        1: '(x=1200,y=1200,z=1500)',
        2: '/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique,Mech_TechSlaughterBoss1,1.2,0.9,1.0,1.0,1.0,Badass,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 10.0, #Original 3D char scale
        6: "AnimBlueprintGeneratedClass'/Game/Enemies/Mech/_Shared/Animation/BPAnim_Mech.BPAnim_Mech_C'",  
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def WORK71(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Character/BPChar_GiganticMech2.BPChar_GiganticMech2_C'",
        1: '(x=1200,y=1200,z=1500)',
        2: '/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique,Mech_TechSlaughterBoss2,1.2,0.9,1.0,1.0,1.0,Badass,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 10.0, #Original 3D char scale
        6: "AnimBlueprintGeneratedClass'/Game/Enemies/Mech/_Shared/Animation/BPAnim_Mech.BPAnim_Mech_C'",  
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def WORK6(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/Enemies/Varkid/_Unique/BossFodder/_Design/Character/BPChar_VarkidBossFodder.BPChar_VarkidBossFodder_C'",
        1: '(x=60,y=60,z=70)',
        2: '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique,BossFodder,1.2,0.9,1.0,1.0,1.0,Badass,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

def WORK8(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_Base.BPChar_DigiClone_Base_C'",
        1: '(x=80,y=80,z=120)',
        2: '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique,BossFodder,1.2,0.9,1.0,1.0,1.0,Badass,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def WORK9(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_Badass.BPChar_DigiClone_Badass_C'",
        1: '(x=80,y=80,z=120)',
        2: '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique,BossFodder,1.2,0.9,1.0,1.0,1.0,Badass,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def WORK10(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_Normal.BPChar_DigiClone_Normal_C'",
        1: '(x=80,y=80,z=120)',
        2: '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique,BossFodder,1.2,0.9,1.0,1.0,1.0,Badass,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def WORK11(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_SuperBadass.BPChar_DigiClone_SuperBadass_C'",
        1: '(x=80,y=80,z=120)',
        2: '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique,BossFodder,1.2,0.9,1.0,1.0,1.0,Badass,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
def WORK12(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_UltimateSuperBadass.BPChar_DigiClone_UltimateSuperBadass_C'",
        1: '(x=80,y=80,z=120)',
        2: '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique,BossFodder,1.2,0.9,1.0,1.0,1.0,Badass,1.0',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

def BPChar_GiganticMech1_C___(_in_):
    return {
        0: "BlueprintGeneratedClass'/Dandelion/Enemies/JackBot/_Shared/_Design/Character/BPChar_JackBot.BPChar_JackBot_C'",
        1: '(x=175,y=175,z=175)',
        2: '/Dandelion/Enemies/JackBot/_Shared/_Design/Balance/Table_Balance_JackBot_PT2,Basic,10.0,10.0,1.0,1.0,1.0,UltimateBadass,1.25',
        3: 'melee', #melee, onegun, twoguns
        4: nav_list[0], #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")

def BPChar_GiganticMech1_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Character/BPChar_Mech_TrialBoss.BPChar_Mech_TrialBoss_C'",
        1: '(x=100,y=100,z=175)',
        2: '/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique,Mech_TrialBoss,7.0,1.0,1.0,1.0,1.0,Badass,1.25',
        3: 'melee', #melee, onegun, twoguns
        4: '',
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: True,# Is BOSS
    }.get(_in_, "!ERROR!")

def BPChar_GiganticMech2_C(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Fabrikator/Basic/_Design/Character/BPChar_FabrikatorBasic.BPChar_FabrikatorBasic_C'",
        1: '(x=150,y=150,z=400)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Fabrikator/_Shared/_Design/Balance/Table_Balance_Fabrikator,FabrikatorPT2,150.0,50.0,25.0,1.0,1.0,SuperBadass,1.25',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: True,# Is BOSS
    }.get(_in_, "!ERROR!")

def BPChar_GiganticMech1_C_(_in_):
    return {
        0: "BlueprintGeneratedClass'/Game/PatchDLC/Dandelion/Enemies/Constructor/Basic/_Design/Character/BPChar_ConstructorBasic.BPChar_ConstructorBasic_C'",
        1: '(x=175,y=175,z=175)',
        2: '/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor,BasicPT2,120.0,80.0,35.0,5.0,5.0,SuperBadass,1.25',
        3: 'melee', #melee, onegun, twoguns
        4: '', #override navigation
        5: 1.0, #Original 3D char scale
        6: '', # Apply AnimationClass 
        7: False,# Is BOSS
    }.get(_in_, "!ERROR!")
    
