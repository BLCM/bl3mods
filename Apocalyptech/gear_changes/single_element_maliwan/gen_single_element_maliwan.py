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
from enum import Enum
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, Balance

mod = Mod('single_element_maliwan.bl3hotfix',
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
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.2.0',
        cats='gear-brand',
        )

# What, me overengineer a problem that could be solved quite simply with just a bit
# of hardcoding?  Pffffff....

class Weap(Enum):
    PS = 1
    SG = 2
    SM = 3
    SR = 4

class Element(Enum):
    FIRE = 1
    CRYO = 2
    SHOCK = 3
    RAD = 4
    CORR = 5

primary = {
        Weap.PS: {
            Element.FIRE: '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_PS_MAL_Elemental_Primary_Fire',
            Element.CRYO: '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_PS_MAL_Elemental_Primary_Cryo',
            Element.SHOCK: '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_PS_MAL_Elemental_Primary_Shock',
            Element.RAD: '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_PS_MAL_Elemental_Primary_Radiation',
            Element.CORR: '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_PS_MAL_Elemental_Primary_Corr',
            },
        Weap.SG: {
            Element.FIRE: '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SG_MAL_Elemental_Primary_Fire',
            Element.CRYO: '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SG_MAL_Elemental_Primary_Cryo',
            Element.SHOCK: '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SG_MAL_Elemental_Primary_Shock',
            Element.RAD: '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SG_MAL_Elemental_Primary_Radiation',
            Element.CORR: '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SG_MAL_Elemental_Primary_Corr',
            },
        Weap.SM: {
            Element.FIRE: '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SM_Mal_ElemPrimary_01_Fire',
            Element.CRYO: '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SM_Mal_ElemPrimary_02_Cryo',
            Element.SHOCK: '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SM_Mal_ElemPrimary_03_Shock',
            Element.RAD: '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SM_Mal_ElemPrimary_04_Radiation',
            Element.CORR: '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Primary/Part_SM_Mal_ElemPrimary_05_Corrosive',
            },
        Weap.SR: {
            Element.FIRE: '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Primary/Part_MAL_SR_Ele_Primary_Fire',
            Element.CRYO: '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Primary/Part_MAL_SR_Ele_Primary_Cryo',
            Element.SHOCK: '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Primary/Part_MAL_SR_Ele_Primary_Shock',
            Element.RAD: '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Primary/Part_MAL_SR_Ele_Primary_Radiation',
            Element.CORR: '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Primary/Part_MAL_SR_Ele_Primary_Corr',
            },
        }
secondary = {
        Weap.PS: {
            Element.FIRE: '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_PS_MAL_Elemental_Secondary_Fire',
            Element.CRYO: '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_PS_MAL_Elemental_Secondary_Cryo',
            Element.SHOCK: '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_PS_MAL_Elemental_Secondary_Shock',
            Element.RAD: '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_PS_MAL_Elemental_Secondary_Radiation',
            Element.CORR: '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_PS_MAL_Elemental_Secondary_Corr',
            },
        Weap.SG: {
            Element.FIRE: '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SG_MAL_Elemental_Secondary_Fire',
            Element.CRYO: '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SG_MAL_Elemental_Secondary_Cryo',
            Element.SHOCK: '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SG_MAL_Elemental_Secondary_Shock',
            Element.RAD: '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SG_MAL_Elemental_Secondary_Radiation',
            Element.CORR: '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SG_MAL_Elemental_Secondary_Corr',
            },
        Weap.SM: {
            Element.FIRE: '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_01_Fire',
            Element.CRYO: '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_02_Cryo',
            Element.SHOCK: '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_03_Shock',
            Element.RAD: '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_04_Radiation',
            Element.CORR: '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_05_Corrosive',
            },
        Weap.SR: {
            Element.FIRE: '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Secondary/Part_MAL_SR_Ele_Secondary_Fire',
            Element.CRYO: '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Secondary/Part_MAL_SR_Ele_Secondary_Cryo',
            Element.SHOCK: '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Secondary/Part_MAL_SR_Ele_Secondary_Shock',
            Element.RAD: '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Secondary/Part_MAL_SR_Ele_Secondary_Radiation',
            Element.CORR: '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Secondary/Part_MAL_SR_Ele_Secondary_Corr',
            },
        }
known_parts = {}
part_type = {}
for weap, elements in list(primary.items()) + list(secondary.items()):
    for element, partname in elements.items():
        known_parts[partname] = element
        part_type[partname] = weap

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
        #'/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/BinaryOperator/Balance/Balance_MAL_SR_BinaryOperator',
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
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Balance/Balance_SG_MAL_BlindBandit',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Balance/Balance_SG_MAL_BlindBandit_Epic',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/PlasmaCoil/Balance/Balance_SM_MAL_PlasmaCoil',
        ]:

    short_bal_name = bal_name.split('/')[-1]
    bal = Balance.from_data(data, bal_name)

    weap_type = None
    primary_cat = None
    primary_elements = set()
    secondary_cat = None
    secondary_elements = set()

    for cat in bal.categories:
        for part in cat.partlist:
            if 'Elemental_Primary' in part.part_name:
                weap_type = part_type[part.part_name]
                primary_elements.add(known_parts[part.part_name])
                primary_cat = cat
            elif 'Elemental_Secondary' in part.part_name:
                secondary_elements.add(known_parts[part.part_name])
                secondary_cat = cat

    mod.comment(short_bal_name)

    if primary_elements == secondary_elements:
        # Simple case - secondary elements are just a duplicate of the primary, so all
        # we're doing is disabling the secondary
        mod.reg_hotfix(Mod.PATCH, '',
                bal_name,
                'RuntimePartList.PartTypeTOC.PartTypeTOC[{}]'.format(secondary_cat.index),
                '(StartIndex=-1,NumParts=0)')
    else:
        # More complex: the elemental offerings are different.  Offer them all as equally-
        # likely options on the primary slot.
        full_elements = primary_elements | secondary_elements
        print(bal_name)
        print(' -> Folding into primary: {}'.format([e.name for e in full_elements]))
        print('')
        secondary_cat.disable()
        secondary_cat.clear()
        primary_cat.clear()
        for element in full_elements:
            primary_cat.add_part_name(primary[weap_type][element])
        bal.hotfix_full(mod)

    mod.newline()

mod.close()
