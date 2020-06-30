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

from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, Balance

mod = Mod('single_element_maliwan.txt',
        'Single-Element Maliwan',
        'Apocalyptech',
        [
            "Removes the second element on all Maliwan guns which ordinarily have it.",
            "Special effects on guns like D.N.A. are unaffected.  Note that you will",
            "still be able to hit the change-element key, but the element will remain",
            "the same, and you'll get a silly little 'Please Fix Label' message where",
            "the element name usually is.",
            "",
            "No more blinky inventory screens which make you wonder what happened to that",
            "fire weapon you were just looking at!  At the expense of gear versatility,",
            "of course.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

data = BL3Data()
for bal_name in [
        # Pistols
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_01_Common',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_02_UnCommon',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_03_Rare',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_04_VeryRare',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_Rare',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_VeryRare',

        # Shotguns
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_01_Common',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_02_Uncommon',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_03_Rare',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_04_VeryRare',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Maliwan/Balance/Balance_SG_MAL_ETech_Rare',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Maliwan/Balance/Balance_SG_MAL_ETech_VeryRare',

        # SMGs
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_01_Common',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_02_Uncommon',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_03_Rare',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_04_VeryRare',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Maliwan/Balance/Balance_SM_MAL_ETech_Rare',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Maliwan/Balance/Balance_SM_MAL_ETech_VeryRare',

        # Sniper Rifles
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_01_Common',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_02_UnCommon',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_03_Rare',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_04_VeryRare',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Maliwan/Balance/Balance_SR_MAL_ETech_Rare',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Maliwan/Balance/Balance_SR_MAL_ETech_VeryRare',

        # Uniques/Legendaries
        # This list is trimmed to exclude weapons which already don't have a second element.
        #
        # Some other purposeful exclusions:
        #  - Vault Hero.  Now it *does* do something special!
        #  - A few guns whose special ability is sort of tied to having two elements:
        #    - Destructo Spinner
        #    - Hellshock
        #    - SF Force
        #
        # Current up through 2020-06-11 (Guardian Takedown).

        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Balance/Balance_SG_MAL_Mouthpiece2',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Balance/Balance_SM_MAL_EmbersPurge',
        #'/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Balance/Balance_PS_MAL_GreaseTrap',
        #'/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BubbleBlaster/Balance/Balance_PS_MAL_BubbleBlaster',
        #'/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Balance/Balance_PS_MAL_FrozenDevil',
        #'/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Balance/Balance_SM_MAL_SFForce',
        #'/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DNA/Balance/Balance_SM_MAL_DNA',
        #'/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link',
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Balance/Balance_SM_MAL_IonLaser',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IcePick/Balance/Balance_PS_MAL_IcePick',
        '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Antler/Balance/Balance_SG_MAL_ETech_Antler',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Decoupler/Balance/Balance_PS_MAL_Decoupler',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Flipper/Balance/Balance_SM_MAL_Flipper',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Frequency/Balance/Balance_SG_MAL_Frequency',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ImaginaryNumber/Balance/Balance_MAL_SR_ImaginaryNumber',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing',
        '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth',
        ]:
    short_bal_name = bal_name.split('/')[-1]
    bal = Balance.from_data(data, bal_name)
    found_secondary_elem = False
    for cat in bal.categories:
        for part in cat.partlist:
            if 'Elemental_Secondary' in part.part_name:
                found_secondary_elem = True
                break
        if found_secondary_elem:
            # We *could* wipe out the partlist in this category and use the built-in
            # hotfix functionality in the `Balance` object, but that would generate a
            # gigantic hotfix, when all we really need to do is tweak one element in
            # the balance's TOC.  Note that `bEnabled` in the PartSet's ActorPartLists
            # array does *not* actually do anything.
            mod.comment(short_bal_name)
            mod.reg_hotfix(Mod.PATCH, '',
                    bal_name,
                    'RuntimePartList.PartTypeTOC.PartTypeTOC[{}]'.format(cat.index),
                    '(StartIndex=-1,NumParts=0)')
            mod.newline()
            break
    if not found_secondary_elem:
        print('NOTE: No secondary element for {}'.format(short_bal_name))

mod.close()
