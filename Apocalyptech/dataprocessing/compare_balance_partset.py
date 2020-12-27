#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
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

import sys
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import BVC

# Just a util to get to the bottom of PartSet/Balance interactions once and for all, after
# the GBX addition of Action Skill Damage parts to COMs only happened in the PartSet
# objects.  Turns out that in nearly all cases, the Balances *can* be trusted, but if you
# want to be sure, you've gotta generate the runtimepartlist from the PartSets.  Alas!
# 
# Anyway, this util basically just loops through all gear (through DLC3) and compares the
# parts found in RuntimePartList in the Balance to the list you get by processing PartSets
# as the game (presumably) does.  This did uncover an interesting tidbit related to a
# couple of Artifact parts, in addition to the Action Skill Damage thing, but otherwise
# everything was fine.

# List of balance names
balances = []

# Data obj
data = BL3Data()

# Generic weapons first
for glob_pattern in [
        '/Game/Gear/Weapons/*/*/*Shared/_Design/*Balance*/Balance_*',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/*/_Design/*/*/*Balance*/Balance_*',
        ]:
    for obj_name in data.glob(glob_pattern):
        balances.append(obj_name)

# Now leg/unique weapons
balances.extend([
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/NineVolt/Balance/Balance_SM_DAHL_NineVolt',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/AAA/Balance/Balance_DAL_PS_AAA',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD',
        '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Alchemist/Balance/Balance_AR_TOR_Alchemist',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/AmberManagement/Balance/Balance_AR_TOR_AmberManagement',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Balance/Balance_SG_TED_Anarchy',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/AutoAime/Balance/Balance_SR_DAL_AutoAime',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Balance_PS_Tediore_BabyMaker',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/_Bangarang/Balance/Balance_PS_TED_Bangerang',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Barrage/Balance/Balance_DAL_AR_Barrage',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Decoupler/Balance/Balance_PS_MAL_Decoupler',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Bearcat/Balance/Balance_AR_TOR_Bearcat',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Balance/Balance_AR_JAK_Bekah',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Bitch/Balance/Balance_SM_HYP_Bitch',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/BiteSize/Balance/Balance_PS_JAK_BiteSize',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Balance/Balance_SG_TOR_Brewha',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Rose/Balance/Balance_PS_JAK_Rose',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Balance/Balance_PS_VLA_BoneShredder',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Boomer/Balance/Balance_SM_DAL_Boomer',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Trash/Balance/Balance_AR_COV_Trash',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Redistributor/Balance/Balance_SG_HYP_Redistributor',
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Balance/Balance_SR_DAL_BrashisDedication',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/BOTD/Balance/Balance_DAL_AR_BOTD',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Brightside/Balance/Balance_SG_TED_Brightside',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BubbleBlaster/Balance/Balance_PS_MAL_BubbleBlaster',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/Balance_PS_JAK_Buttplug',
        '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/Balance_ATL_AR_Carrier',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Antler/Balance/Balance_SG_MAL_ETech_Antler',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/CheapTips/Balance/Balance_SM_HYP_CheapTips',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Balrog/Balance/Balance_SG_Torgue_Balrog',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/CockyBastard/Balance/Balance_SR_JAK_CockyBastard',
        '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/Balance_VLA_SR_Prison',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ImaginaryNumber/Balance/Balance_MAL_SR_ImaginaryNumber',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Balance/Balance_SG_HYP_ConferenceCall',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ContainedExplosion/Balance/Balance_AR_TOR_Contained',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Craps/Balance/Balance_PS_TOR_Craps',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Creamer/Balance/Balance_HW_TOR_Creamer',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Balance/Balance_SM_HYP_Crossroad',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DNA/Balance/Balance_SM_MAL_DNA',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Dakota/Balance/Balance_SG_JAK_Dakota',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Balance/Balance_AR_VLA_Damn',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Balance/Balance_PS_JAK_Malevolent',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Balance/Balance_PS_TOR_Devestator',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Foursum/Balance/Balance_PS_TOR_4SUM',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Digby/Balance/Balance_DAL_AR_Digby',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/DowsingRod/Balance/Balance_AR_VLA_Dowsing',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Earworm/Balance/Balance_DAL_AR_Earworm',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Echo/Balance/Balance_PS_TOR_Echo',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Balance/Balance_SM_MAL_EmbersPurge',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/Balance_PS_COV_Chad',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Brick/Balance/Balance_SG_HYP_Brick',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Balance/Balance_AR_VLA_Faisor',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Fearmonger/Balance/Balance_SG_HYP_ETech_Fearmonger',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/Balance_SG_JAK_Fingerbiter',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Firecracker/Balance/Balance_SG_HYP_Firecracker',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Flakker/Balance/Balance_SG_Torgue_Flakker',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Flipper/Balance/Balance_SM_MAL_Flipper',
        '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Balance/Balance_HW_ATL_Freeman',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Frequency/Balance/Balance_SG_MAL_Frequency',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Balance/Balance_PS_MAL_FrozenDevil',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Gargoyle/Balance/Balance_PS_COV_Gargoyle',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Balance/Balance_AR_JAK_04_GatlingGun',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Balance/Balance_HW_TOR_BurgerCannon',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf',
        '/Game/PatchDLC/Takedown2/Gear/Weapons/Globetrotter/Balance/Balance_HW_COV_Globetrotter',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Balance/Balance_PS_MAL_GreaseTrap',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Balance/Balance_PS_TED_Gunerang',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Hail/Balance/Balance_DAL_AR_Hail',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/Balance_AR_JAK_HandOfGlory',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Handsome/Balance/Balance_SM_HYP_Handsome',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Balance/Balance_SR_JAK_Headsplosion',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/HeartBreaker/Balance/Balance_SG_HYP_HeartBreaker',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/HellFire/Balance/Balance_SM_DAHL_HellFire',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Balance/Balance_SG_JAK_Hellwalker',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Hive/Balance/Balance_HW_TOR_Hive',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Hornet/Balance/Balance_DAL_PS_Hornet',
        '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Balance/Balance_HW_COV_HotDrop',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Hydrafrost/Balance/Balance_PS_COV_Hydrafrost',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Balance/Balance_HW_VLA_IonCannon',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Balance/Balance_SM_MAL_IonLaser',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IcePick/Balance/Balance_PS_MAL_IcePick',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/CoolBeans/Balance/Balance_AR_JAK_CoolBeans',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IceBurger/Balance/Balance_SG_HYP_IceBurger',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Balance/Balance_PS_VLA_Infiniti',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider',
        '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Balance/Balance_HW_VLA_CloudBurst',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Kaleidoscope/Balance/Balance_DAL_PS_Kaleidoscope',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Kaos/Balance/Balance_DAL_AR_Kaos',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson',
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Balance/Balance_SR_DAL_WorldDestroyer',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/GodMother/Balance/Balance_PS_JAK_GodMother',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa',
        '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/L0V3M4CH1N3/Balance/Balance_SM_HYP_L0V3M4CH1N3',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Varlope/Balance/Balance_AR_TOR_Varlope',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/LaserSploder/Balance/Balance_AR_TOR_LaserSploder',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Balance/Balance_AR_JAK_LeadSprinkler',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Lasocannon/Balance/Balance_PS_VLA_Lasocannon',
        '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Balance/Balance_PS_ATL_Drill',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Balance/Balance_PS_COV_Legion',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LittleYeeti/Balance/Balance_PS_JAK_LittleYeeti',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Balance/Balance_SM_TED_NotAFlamethrower',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill_Legendary',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Balance/Balance_AR_VLA_LuciansCall',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Balance/Balance_PS_JAK_Lucky7',
        '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Balance/Balance_VLA_SR_Lyuda',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent',
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/MalaksBane/Balance/Balance_SR_DAL_ETech_MalaksBane',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/FriendZone/Balance/Balance_SG_TED_FriendZone',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Sheriff/Balance/Balance_PS_JAK_Sheriff',
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/MasterworkCrossbow/Balance/Balance_SR_HYP_Masterwork',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/MeltFacer/Balance/Balance_SG_HYP_MeltFacer',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Balance/Balance_SG_MAL_Mouthpiece2',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Miscreant/Balance/Balance_PS_VLA_Miscreant',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse',
        '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Balance/Balance_SR_JAK_Monocle',
        '/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Earthbound/Balance/Balance_SM_TED_Earthbound',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Balance/Balance_PS_ATL_DoubleTap',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Narp/Balance/Balance_SR_HYP_Narp',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/NeedleGun/Balance/Balance_SM_TED_NeedleGun',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Nemesis/Balance/Balance_DAL_PS_Nemesis',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Rakkman/Balance/Balance_DAL_PS_Rakkman',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Demoskag/Balance/Balance_SM_DAL_Demoskag',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Balance/Balance_SG_JAK_Nimble',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/PewPew/Balance/Balance_AR_COV_PewPew',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Nukem/Balance/Balance_HW_TOR_Nukem',
        '/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/ZeroForPlayer/Balance_SR_HYP_ZeroForPlayer',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Balance/Balance_ATL_AR_OPQ',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Troy/Balance/Balance_PS_TOR_Troy',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Balance/Balance_AR_VLA_Ogre',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Omniloader/Balance/Balance_DAL_PS_Omniloader',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/OnePunch/Balance/Balance_SG_JAK_OnePunch',
        '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/Balance_AR_JAK_PasRifle',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR',
        '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/Balance_PS_ATL_Warmonger',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Peashooter/Balance/Balance_PS_JAK_Peashooter',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Phebert/Balance/Balance_SG_HYP_Phebert',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Plague/Balance/Balance_HW_TOR_Plague',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Plumage/Balance/Balance_HW_ATL_Plumage',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Balance/Balance_SG_TED_Polybius',
        '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/Balance_HW_COV_PortaPooper',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/PredatoryLending/Balance/Balance_SM_HYP_PredatoryLending',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/Pricker/Balance/Balance_SM_HYP_Pricker',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Copybeast/Balance/Balance_SM_HYP_Copybeast',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Balance/Balance_PS_COV_PsychoStabber',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Rampager/Balance/Balance_HW_TOR_Rampager',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/QuickDraw/Balance/Balance_PS_JAK_QuickDraw',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/Balance_HW_TOR_RYNO',
        '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Balance/Balance_ATL_AR_RebelYell',
        '/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Fork/Balance/Balance_SM_HYP_Fork',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/RedLiner/Balance/Balance_SG_Torgue_RedLine',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Reflux/Balance/Balance_SG_HYP_Reflux',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Ripper/Balance/Balance_SM_DAL_Ripper',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/SpeakEasy/Balance/Balance_SG_JAK_SpeakEasy',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Balance_PS_JAK_SpyRevolver',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/RoisensThorns/Balance/Balance_PS_TOR_RoisensThorns',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Balance/Balance_AR_JAK_RowansCall',
        '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Balance/Balance_HW_ATL_RubysWrath',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Balance/Balance_SM_MAL_SFForce',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SacrificalLamb/Balance/Balance_SG_TED_SacrificialLamb',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/SandHawk/Balance/Balance_SR_DAL_SandHawk',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Satisfaction/Balance/Balance_HW_TOR_Satisfaction',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Balance/Balance_AR_COV_Sawbar',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Swarm/Balance/Balance_HW_TOR_Swarm',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Scoville/Balance/Balance_PS_TOR_Scoville',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Balance/Balance_PS_JAK_TheSeventhSense',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Shocker/Balance/Balance_SG_Torgue_ETech_Shocker',
        '/Game/PatchDLC/Steam/Gear/Weapons/SteamGun/Balance/Balance_SM_HYP_ShortStick_Legendary',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Balance/Balance_PS_COV_Skeksis',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Balance/Balance_SG_JAK_LGD_Sledge',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/SleepingGiant/Balance/Balance_SM_DAL_SleepingGiant',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/SlowHand/Balance/Balance_SG_HYP_SlowHand',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Balance/Balance_SM_TED_SpiderMind',
        '/Game/PatchDLC/Takedown2/Gear/Weapons/Smog/Balance/Balance_SM_HYP_Smog',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Soulrender/Balance/Balance_DAL_AR_Soulrender',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Shoveler/Balance/Balance_SG_Torgue_Shoveler',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Splinter/Balance/Balance_SG_JAK_Splinter',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/SniperRifles/Dahl/_Design/_Unique/Frostbolt/Balance/Balance_SR_DAL_ETech_Frostbolt',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/StarHelix/Balance/Balance_DAL_AR_StarHelix',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/StoneThrow/Balance/Balance_AR_JAK_Stonethrow',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Balance/Balance_AR_VLA_Sherdifier',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber',
        '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/TwitchPrime/Balance/Balance_SG_TED_Twitch',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Balance/Balance_SG_JAK_Unique_Wave',
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/Balance_SR_HYP_TwoTime',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Balance/Balance_SM_TED_TenGallon',
        '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BioBetsy/Balance/Balance_AR_COV_BioBetsy_Rad',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BioBetsy/Balance/Balance_AR_COV_BioBetsy_Shock',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Balance_AR_VLA_BigSucc',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/PrivateInvestigator/Balance/Balance_DAL_PS_PrivateInvestigator',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Balance/Balance_SM_TED_Beans',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheBoringGun/Balance/Balance_SG_TOR_Boring',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/TheButcher/Balance/Balance_SG_HYP_TheButcher',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/McSmugger/Balance/Balance_AR_JAK_McSmugger',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Balance/Balance_PS_JAK_MelsCompanion',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheCure/Balance/Balance_SG_JAK_TheCure',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Balance/Balance_AR_VLA_Dictator',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Balance/Balance_PS_JAK_TheDuc',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Balance/Balance_SG_JAK_Garcia',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Balance/Balance_SG_TED_Horizon',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Hunted/Balance/Balance_SR_JAK_Hunted',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Balance/Balance_SR_JAK_Hunter',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Huntress/Balance/Balance_SR_JAK_Huntress',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/Balance_PS_COV_Mouthpiece',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Fakobs/Balance/Balance_SG_JAK_Fakobs',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Thumper/Balance/Balance_SG_Torgue_Thumper',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists',
        '/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/Balance_AR_JAK_TraitorsDeath',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/TryBolt/Balance/Balance_AR_TOR_TryBolt',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Tunguska/Balance/Balance_HW_TOR_Tunguska',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Balance/Balance_PS_JAK_Unforgiven',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/UnkemptHarold/Balance/Balance_PS_TOR_UnkemptHarold',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Vanquisher/Balance/Balance_SM_DAHL_Vanquisher',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Balance/Balance_PS_JAK_WagonWheel',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Warlord/Balance/Balance_DAL_AR_Warlord',
        '/Game/PatchDLC/Takedown2/Gear/Weapons/WebSlinger/Balance/Balance_AR_VLA_WebSlinger',
        '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun',
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/Woodblocks/Balance/Balance_SR_HYP_Woodblocks',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/XZ/Balance/Balance_SM_HYP_XZ',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/YellowCake/Balance/Balance_HW_COV_ETech_YellowCake',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev',
        ])

# Now generic shields
glob_pattern = '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_*_*_*'
for obj_name in data.glob(glob_pattern):
    balances.append(obj_name)

# And named shields
balances.extend([
    '/Game/PatchDLC/Dandelion/Gear/Shield/Clover/Balance/InvBalD_Shield_Clover',
    '/Game/PatchDLC/Takedown2/Gear/Shields/Aesclepius/Balance/InvBalD_Shield_LGD_Aesclepius',
    '/Game/Gear/Shields/_Design/_Uniques/BackHam/Balance/InvBalD_Shield_BackHam',
    '/Game/Gear/Shields/_Design/_Uniques/Cyttorak/bALANCE/InvBalD_Shield_Cyttorak',
    '/Game/Gear/Shields/_Design/_Uniques/BigBoomBlaster/Balance/InvBalD_Shield_LGD_BigBoomBlaster',
    '/Game/Gear/Shields/_Design/_Uniques/BlackHole/Balance/InvBalD_Shield_LGD_BlackHole',
    '/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Balance/InvBalD_Shield_XPLootBooster',
    '/Game/PatchDLC/Dandelion/Gear/Shield/DoubleDowner/Balance/InvBalD_Shield_DoubleDowner',
    '/Game/PatchDLC/Dandelion/Gear/Shield/Ember/Balance/InvBalD_Shield_Ember',
    '/Game/PatchDLC/Event2/Gear/Shield/_Unique/Firewall/Balance/InvBalD_Shield_Legendary_Firewall',
    '/Game/Gear/Shields/_Design/_Uniques/FrontLoader/Balance/InvBalD_Shield_LGD_FrontLoader',
    '/Game/Gear/Shields/_Design/_Uniques/Aurelia/Balance/InvBalD_Shield_LGD_Aurelia',
    '/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart',
    '/Game/Gear/Shields/_Design/_Uniques/GoldenTouch/Balance/InvBalD_Shield_GoldenTouch',
    '/Game/Gear/Shields/_Design/_Uniques/Impaler/Balance/InvBalD_Shield_LGD_Impaler',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Initiative/Balance/InvBalD_Shield_Initiative',
    '/Game/Gear/Shields/_Design/_Uniques/LoopOf4N631/Balance/InvBalD_Shield_HYP_LoopOf4N631',
    '/Game/PatchDLC/Event2/Gear/Shield/_Unique/MEAT/Balance/InvBalD_Shield_Legendary_MEAT',
    '/Game/Gear/Shields/_Design/_Uniques/Dispensary/Balance/InvBalD_Shield_LGD_Dispensary',
    '/Game/Gear/Shields/_Design/_Uniques/BuriedAlive/Balance/InvBalD_Shield_BuriedAlive',
    '/Game/Gear/Shields/_Design/_Uniques/MessyBreakup/bALANCE/InvBalD_Shield_MessyBreakup',
    '/Game/Gear/Shields/_Design/_Uniques/MoxxisEmbrace/Balance/InvBalD_Shield_MoxxisEmbrace',
    '/Game/Gear/Shields/_Design/_Uniques/MrCaffeine/Balance/InvBalD_Shield_PAN_MrCaffeine',
    '/Game/Gear/Shields/_Design/_Uniques/NovaBurner/Balance/InvBalD_Shield_LGD_NovaBurner',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/OldGod/Balance/InvBalD_Shield_OldGod',
    '/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner',
    '/Game/Gear/Shields/_Design/_Uniques/Re-Charger/Balance/InvBalD_Shield_LGD_ReCharger',
    '/Game/Gear/Shields/_Design/_Uniques/Vamp/Balance/InvBalD_Shield_Legendary_Vamp',
    '/Game/Gear/Shields/_Design/_Uniques/Rectifier/Balance/InvBalD_Shield_LGD_Rectifier',
    '/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger',
    '/Game/Gear/Shields/_Design/_Uniques/SlideKick/Balance/InvBalD_Shield_LGD_SlideKick',
    '/Game/Gear/Shields/_Design/_Uniques/Radiate/Balance/InvBalD_Shield_LGD_Radiate',
    '/Game/Gear/Shields/_Design/_Uniques/Revengenader/Balance/InvBalD_Shield_LGD_Revengenader',
    '/Game/PatchDLC/Dandelion/Gear/Shield/Rico/Balance/InvBalD_Shield_Rico',
    '/Game/Gear/Shields/_Design/_Uniques/RoughRider/Balance/InvBalD_Shield_LGD_RoughRider',
    '/Game/PatchDLC/BloodyHarvest/Gear/Shields/_Design/_Unique/ScreamOfPain/Balance/InvBalD_Shield_ScreamOfTerror',
    '/Game/Gear/Shields/_Design/_Uniques/ShootingStar/Balance/InvBalD_Shield_LGD_ShootingStar',
    '/Game/PatchDLC/Takedown2/Gear/Shields/Stinger/Balance/InvBalD_Shield_LGD_Stinger',
    '/Game/Gear/Shields/_Design/_Uniques/StopGap/Balance/InvBalD_Shield_LGD_StopGap',
    '/Game/Gear/Shields/_Design/_Uniques/Transformer/Balance/InvBalD_Shield_LGD_Transformer',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Torch/Balance/InvBalD_Shield_Legendary_Torch',
    '/Game/Gear/Shields/_Design/_Uniques/Unpaler/Balance/InvBalD_Shield_LGD_Unpaler',
    '/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/VoidRift/Balance/InvBalD_Shield_LGD_VoidRift',
    '/Game/Gear/Shields/_Design/_Uniques/Ward/Balance/InvBalD_Shield_Ward',
    '/Game/PatchDLC/Event2/Gear/Shield/_Unique/Wattson/Balance/InvBalD_Shield_Legendary_Wattson',
    '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot',
    ])

# Generic grenades
glob_pattern = '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_*_*_*'
for obj_name in data.glob(glob_pattern):
    balances.append(obj_name)

# Named grenades
balances.extend([
    '/Game/PatchDLC/Dandelion/Gear/Grenade/AcidBurn/Balance/InvBalD_GM_AcidBurn',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Summit/Balance/InvBalD_GM_Summit',
    '/Game/Gear/GrenadeMods/_Design/_Unique/JustDeserts/Balance/InvBalD_GM_JustDeserts',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Chupa/Balance/InvBalD_GM_Chupa',
    '/Game/PatchDLC/Geranium/Gear/Grenade/CoreBurst/Balance/InvBalD_GM_CoreBurst',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ButtStallion/Balance/InvBalD_GM_ButtStallion',
    '/Game/PatchDLC/Geranium/Gear/Grenade/SkagOil/Balance/InvBalD_GM_SkagOil',
    '/Game/Gear/GrenadeMods/_Design/_Unique/EchoV2/Balance/InvBalD_GM_EchoV2',
    '/Game/Gear/GrenadeMods/_Design/_Unique/EMP/Balance/InvBalD_GM_EMP',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Mogwai/Balance/InvBalD_GM_Mogwai',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Epicenter/Balance/InvBalD_GM_Epicenter',
    '/Game/Gear/GrenadeMods/_Design/_Unique/BirthdaySuprise/Balance/InvBalD_GM_BirthdaySuprise',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Balance/InvBalD_GM_TED_Fastball',
    '/Game/Gear/GrenadeMods/_Design/_Unique/FireStorm/Balance/InvBalD_GM_VLA_FireStorm',
    '/Game/PatchDLC/Event2/Gear/GrenadeMods/FishSlap/Balance/InvBalD_GM_FishSlap',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Mushroom/Balance/InvBalD_GM_Shroom',
    '/Game/PatchDLC/BloodyHarvest/Gear/GrenadeMods/_Design/_Unique/FontOfDarkness/Balance/InvBalD_GM_TOR_FontOfDarkness',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Seeker/Balance/InvBalD_GM_Seeker',
    '/Game/Gear/GrenadeMods/_Design/_Unique/HunterSeeker/Balance/InvBalD_GM_HunterSeeker',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Piss/Balance/InvBalD_GM_Piss',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Kryll/Balance/InvBalD_GM_Kryll',
    '/Game/PatchDLC/Takedown2/Gear/GrenadeMods/Lightspeed/Balance/InvBalD_GM_HYP_Lightspeed',
    '/Game/Gear/GrenadeMods/_Design/_Unique/MoxiesBosom/Balance/InvBalD_GM_PAN_MoxiesBosom',
    '/Game/Gear/GrenadeMods/_Design/_Unique/WizardOfNOG/Balance/InvBalD_GM_WizardOfNOG',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Nagate/Balance/InvBalD_GM_Nagate',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ToiletBombs/Balance/InvBalD_GM_TOR_ToiletBombs',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Quasar/Balance/InvBalD_GM_Quasar',
    '/Game/Gear/GrenadeMods/_Design/_Unique/RedQueen/Balance/InvBalD_GM_RedQueen',
    '/Game/Gear/GrenadeMods/_Design/_Unique/CashMoneyPreorder/Balance/InvBalD_GM_CashMoneyPreorder',
    '/Game/PatchDLC/Dandelion/Gear/Grenade/Slider/Balance/InvBalD_GM_TED_Slider',
    '/Game/Gear/GrenadeMods/_Design/_Unique/StormFront/Balance/InvBalD_GM_StormFront',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Surge/Balance/InvBalD_GM_Surge',
    '/Game/Gear/GrenadeMods/_Design/_Unique/HipHop/Balance/InvBalD_GM_TOR_HipHop',
    '/Game/Gear/GrenadeMods/_Design/_Unique/TranFusion/Balance/InvBalD_GM_TranFusion',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ToyGrenade/Balance/InvBalD_GM_ToyGrenade',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ObviousTrap/Balance/InvBalD_GM_ObviousTrap',
    '/Game/Gear/GrenadeMods/_Design/_Unique/WidowMaker/Balance/InvBalD_GM_WidowMaker',
    ])

# Generic COMs
glob_pattern = '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_*_*_*'
for obj_name in data.glob(glob_pattern):
    balances.append(obj_name)

# Named COMs
balances.extend([
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_BountyHunter',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_CosmicStalker',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_DE4DEYE',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_FriendBot',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RakkCommander',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RedFang',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_BearTrooper',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_BlastMaster',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_BloodLetter',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_MindSweeper',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_Rocketeer',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_ColdWarrior',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_Executor',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_FireBrand',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_Infiltrator',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_Techspert',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Breaker',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Dragon',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Elementalist',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Nimbus',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Phasezerker',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_DLC1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Hib',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_DLC1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_Raid1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/GUN/InvBalD_CM_Gunner_Hib',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_DLC1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/OPE/InvBalD_CM_Operative_Hib',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_DLC1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_Raid1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Hib',
    ])

# Artifacts
balances.extend([
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_01_Common',
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_02_Uncommon',
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_03_Rare',
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_04_VeryRare',
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_05_Legendary',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/ElectricBanjo/Balance/InvBalD_Artifact_ElectricBanjo',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/Grave/Balance/InvBalD_Artifact_Grave',
    '/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/Lunacy/Balance/InvBalD_Artifact_Lunacy',
    '/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/PUK/Balance/InvBalD_Artifact_PUK',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/PhoenixTears/Balance/InvBalD_Artifact_PhoenixTears',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/RoadWarrior/Balance/InvBalD_Artifact_RoadWarrior',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/ElDragonJr/Balance/InvBalD_Artifact_ElDragonJr',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/VaultHunterRelic/Balance/InvBalD_Artifact_Relic',
    '/Game/PatchDLC/Geranium/Gear/Artifacts/_Design/_Unique/Vengeance/Balance/InvBalD_Artifact_Vengeance',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/CommanderPlanetoid/InvBalD_Artifact_CommanderPlanetoid',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/CosmicCrater/InvBalD_Artifact_CosmicCrater',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/Deathless/InvBalD_Artifact_Deathless',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/Salvo/InvBalD_Artifact_Salvo',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/LoadedDice/InvBalD_Artifact_LoadedDice',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/MoxxisEndowment/InvBalD_Artifact_MoxxisEndowment',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/OttoIdol/InvBalD_Artifact_OttoIdol',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/PullOutMethod/InvBalD_Artifact_PullOutMethod',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/RocketBoots/InvBalD_Artifact_RocketBoots',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/Safegaurd/InvBalD_Artifact_Safegaurd',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/SplatterGun/InvBalD_Artifact_SplatterGun',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/StaticTouch/InvBalD_Artifact_StaticTouch',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/VictoryRush/InvBalD_Artifact_VictoryRush',
    '/Game/PatchDLC/Raid1/Gear/Artifacts/WhiteElephant/InvBalD_Artifact_WhiteElephant',
    ])

def get_invbaldata(data, bal_name):
    bal_data = None
    bal_data_full = data.get_data(bal_name)
    for export in bal_data_full:
        if export['export_type'] == 'OakInventoryBalanceData':
            bal_data = export
            break
        elif export['export_type'] == 'InventoryBalanceData':
            bal_data = export
            break
    if bal_data is None:
        raise Exception('No valid invbaldata found for {}'.format(bal_name))
    return bal_data

(MODE_COMPLETE, MODE_ADDITIVE, MODE_SELECTIVE) = range(3)
ps_mode_mapping = {
        'EActorPartReplacementMode::Complete': MODE_COMPLETE,
        'EActorPartReplacementMode::Additive': MODE_ADDITIVE, # this is the default and will likely never actually show up in dumps
        'EActorPartReplacementMode::Selective': MODE_SELECTIVE,
        }
ps_mode_default = MODE_ADDITIVE

def get_cat_meta(category):
    """
    Used this to find out if the 
    """
    if category['bCanSelectMultipleParts']:
        return '{}-{}-{}-{}'.format(
                category['bCanSelectMultipleParts'],
                category['bUseWeightWithMultiplePartSelection'],
                category['MultiplePartSelectionRange']['Min'],
                category['MultiplePartSelectionRange']['Max'],
                )
    else:
        return 'false'

for bal_name in balances:

    # Get parts from the balance
    bal_parts = []
    bal_data = get_invbaldata(data, bal_name)
    for part in bal_data['RuntimePartList']['AllParts']:
        if type(part['PartData']) == list:
            bal_parts.append((part['PartData'][1], data.process_bvc_struct(part['Weight'])))

    # Get a list of partset objects we'll loop through to fill in our partset-based parts list
    partset_names = []
    cur_bal_data = bal_data
    while True:
        partset_names.insert(0, cur_bal_data['PartSetData'][1])
        if 'BaseSelectionData' in cur_bal_data and type(cur_bal_data['BaseSelectionData']) == list:
            cur_bal_data = get_invbaldata(data, cur_bal_data['BaseSelectionData'][1])
        else:
            break
    
    # Printing out the partsets that we'll be looking at, for debugging
    #print(partset_names)

    # Now loop through the partset objects and grab parts by category.
    category_parts = []
    apl_metadata = {}
    for partset_name in partset_names:
        partset_data = data.get_data(partset_name)[0]

        # Figure out the mode of the partset APLs
        if 'ActorPartReplacementMode' in partset_data:
            partset_mode = ps_mode_mapping[partset_data['ActorPartReplacementMode']]
        else:
            partset_mode = ps_mode_default

        # Loop through APLs
        for idx, category in enumerate(partset_data['ActorPartLists']):
            if len(category_parts) < (idx+1):
                category_parts.append([])
                apl_metadata[idx] = None
            used = False

            # Behavior depends on what the mode is.  First up: Complete
            if partset_mode == MODE_COMPLETE:
                category_parts[idx] = []
                used = True
                if category['bEnabled']:
                    for part in category['Parts']:
                        if type(part['PartData']) == list:
                            category_parts[idx].append((part['PartData'][1], data.process_bvc_struct(part['Weight'])))

            # Next: Additive
            elif partset_mode == MODE_ADDITIVE:
                if category['bEnabled']:
                    used = True
                    for part in category['Parts']:
                        if type(part['PartData']) == list:
                            category_parts[idx].append((part['PartData'][1], data.process_bvc_struct(part['Weight'])))

            # Next: Selective
            elif partset_mode == MODE_SELECTIVE:
                if category['bEnabled']:
                    used = True
                    category_parts[idx] = []
                    for part in category['Parts']:
                        if type(part['PartData']) == list:
                            category_parts[idx].append((part['PartData'][1], data.process_bvc_struct(part['Weight'])))

            # Finally: wtf?  How did we get here.
            else:
                raise Exception('Unknown partset mode: {}'.format(partset_mode))

            # Store our metadata
            if used:
                apl_metadata[idx] = get_cat_meta(category)

    # Check to see if our top-level category metadata is different from the last time they were set
    # (It looks like the game always uses the "top-level" one for those params, which
    # is nice for me processing this stuff.  One simple test is the WTF shield, whose base
    # Anshin PartSet says that you can't have multiple augments (APL 3), but its top-level
    # WTF PartSet specifies a range of 2-2.)
    for idx, category in enumerate(partset_data['ActorPartLists']):
        if idx in apl_metadata and apl_metadata[idx] is not None:
            if apl_metadata[idx] != get_cat_meta(category):
                print('{}: Metadata mismatch on APL {}'.format(bal_name, idx))
                print(partset_names)
                print('  {} ->'.format(apl_metadata[idx]))
                print('  {}'.format(get_cat_meta(category)))

    # Now conglomerate all those categories into a single parts list
    partset_parts = []
    for cat_parts in category_parts:
        partset_parts.extend(cat_parts)

    # Now compare
    if bal_parts != partset_parts:

        # Okay, so we *expect* to have differences in our COMs, due to the new Action Skill Damage
        # parts.  If that's the *only* difference we find, don't bother complaining about it.
        bal_compare = set(bal_parts)
        partset_compare = set(partset_parts)
        differences = bal_compare ^ partset_compare

        found_non_asd = False
        for difference, weight in differences:
            if 'ActionSkillDamage' not in difference:
                # Okay, interesting, turns out there's Artifact_Part_Stats_FireDamage -> Artifact_Part_Stats_FireDamage_2 and 
                # Artifact_Part_Stats_CryoDamage -> Artifact_Part_Stats_CryoDamage_2 as well, two parts that I'd been thinking
                # were totally wrong during my data extraction for some time now.  These will be okay as well.
                if 'FireDamage' not in difference and 'CryoDamage' not in difference:
                    found_non_asd = True
                    break

        if found_non_asd:
            print('omg mismatch: {}'.format(bal_name))
            with open('balance.txt', 'w') as df:
                for part in bal_parts:
                    print(part, file=df)
            with open('partset.txt', 'w') as df:
                for part in partset_parts:
                    print(part, file=df)
            sys.exit(1)

