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

import csv
import sys
from bl3data.bl3data import BL3Data

# This is all a bit hokey, but it seems to work in general.  Current error
# output, as of 2020-09-10 (note that it may be awhile before I can confirm
# some of the Alisma errors):
#
# WARNING: More than one bpchar redirect found for /Hibiscus/Enemies/Tentacle/Basic/_Design/Character/BPChar_TentacleBasic
# WARNING: More than one bpchar redirect found for /Hibiscus/Enemies/Zealot/Ghost/_Design/Character/BPChar_Zealot_Ghost_Invisible
# WARNING: More than one bpchar redirect found for /Hibiscus/Enemies/Vincent/_design/Character/BPChar_Vincent_Fake_Ghost
# WARNING: More than one bpchar redirect found for /Hibiscus/Enemies/Vincent/_design/Character/BPChar_Vincent_Fake_Ghost
# WARNING: More than one bpchar redirect found for /Hibiscus/Enemies/Vincent/_design/Character/BPChar_Vincent_Fake_Ghost
# ALERT: No names found, and not in our no-alert exception list: /Alisma/NonPlayerCharacters/GhostFather/BPChar_GhostKrieg_Father
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Mad_SpineTingler
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Mad_Rains
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Mad_BigAss
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Sane_SpineTingler
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Mad_ParadeHarpoon
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Sane_ParadeHarpoon
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Sane_ShadesOfTruth
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Sane_ExposureTherapy
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Sane_GoodbyeOldFriend
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Mad_ShadesOfTruth
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Sane_InkBlots
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Sane_Bell
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Mad_GoodbyeOldFriend
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Mad_InkBlots
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Sane_BlastRequests
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Mad_Bell
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Mad_ExposureTherapy
# WARNING: More than one bpchar redirect found for /Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Sane_BigAss
# ALERT: No names found, and not in our no-alert exception list: /Alisma/NonPlayerCharacters/GhostDaughter/BPChar_GhostKrieg_Daughter
# ALERT: No names found, and not in our no-alert exception list: /Alisma/NonPlayerCharacters/GhostMother/BPChar_GhostKrieg_Mother
# WARNING: More than one bpchar redirect found for /Alisma/Enemies/TrainBoss/_Shared/_Design/Character/BPChar_TrainBossVista
# WARNING: More than one bpchar redirect found for /Alisma/Enemies/zTBD_AliPunk/Badass/BPChar_AliPunkBadass
# WARNING: More than one bpchar redirect found for /Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Character/BPChar_Behemoth
# WARNING: More than one bpchar redirect found for /Game/PatchDLC/Event2/Enemies/Cyber/Trooper/Basic/_Design/Character/BPChar_TrooperBasicBossAddEvent2
# WARNING: More than one bpchar redirect found for /Game/PatchDLC/Event2/Enemies/Cyber/ServiceBots/Melee/BPChar_ServiceBot_MeleeBossAddEvent2
# WARNING: More than one bpchar redirect found for /Game/PatchDLC/Event2/Enemies/Cyber/ServiceBots/Melee/BPChar_ServiceBot_MeleeBossAddEvent2
# WARNING: DisplayName not found in /Game/Missions/Plot/MarshFields/UIName_MarshFields_BaseSpy
# WARNING: DisplayName not found in /Game/Missions/Plot/MarshFields/UIName_MarshFields_BaseSpy
# WARNING: DisplayName not found in /Game/Missions/Plot/MarshFields/UIName_MarshFields_BaseSpy
# WARNING: DisplayName not found in /Game/Missions/Plot/MarshFields/UIName_MarshFields_BaseSpy
# WARNING: More than one bpchar redirect found for /Game/Enemies/Ratch/_Unique/NoFeastBasic/_Design/Character/BPChar_RatchNoFeastBasic
# WARNING: More than one bpchar redirect found for /Game/Enemies/Ratch/_Unique/NoFeastPup/_Design/Character/BPChar_RatchNoFeastPup
# WARNING: More than one bpchar redirect found for /Game/Enemies/KatagawaJR/KJR/_Design/Character/BPChar_KJR
# WARNING: More than one bpchar redirect found for /Game/Enemies/KatagawaJR/KJR/_Design/Character/BPChar_KJR
# WARNING: More than one bpchar redirect found for /Game/Enemies/KatagawaJR/KJR/_Design/Character/BPChar_KJR
# WARNING: More than one bpchar redirect found for /Game/Enemies/KatagawaJR/KJR/_Design/Character/BPChar_KJR
# WARNING: More than one bpchar redirect found for /Game/Enemies/ServiceBot/_Unique/JanitorBot/_Design/Character/BPChar_ServiceBot_JanitorBot
# WARNING: More than one bpchar redirect found for /Game/Enemies/Psycho_Male/_Unique/Prologue/_Design/Character/BPChar_PsychoPrologue
#
# Output from here is live at https://docs.google.com/spreadsheets/d/1mJEohWGAvhdVxq55wACFZI0eqtsoUaTAZKMVj0AlgIk/edit?usp=sharing

data = BL3Data()

bpchar_redirect_excluders = {
        '/Game/PlayerCharacters/_Shared/_Design/Character/BPChar_Player',
        '/Game/NonPlayerCharacters/_Shared/_Design/BPChar_NonPlayerCharacter',
        '/Game/Common/_Design/AI/Character/BPChar_AI',
        '/Game/Enemies/_Shared/_Design/BPChar_Enemy',
        '/Game/NonPlayerCharacters/_Generic/_Shared/_Design/Character/BPChar_GenericNPC_Combat',
        '/Game/NonPlayerCharacters/_Shared/_Design/BPChar_NonPlayerCharacter_Combat',
        }

def get_bpchar_names(bpchar_name):
    global data
    global bpchar_redirect_excluders

    # Debug this?
    debug = False
    #if 'BPChar_ServiceBot_MeleeBossAddEvent2' in bpchar_name:
    #    debug = True

    # Names we've detected
    names = []

    # First get all UIName_* objects that are referenced directly
    uinames = []
    from_refs = data.get_refs_from(bpchar_name)
    for ref in from_refs:
        if 'uiname' in ref.lower():
            if debug:
                print('DBG: Got UIName: {}'.format(ref), file=sys.stderr)
            name_obj = data.get_data(ref)[0]
            names.append(name_obj['DisplayName']['string'])

    # Now get any names that might override that (in some cases
    # this seems to be the *only* path to get a UIName, in fact).
    # Some BPChar objects seem to serve as a "base" for other BPChar
    # objects, so if we don't find a name but there are other BPChars
    # which reference us, don't complain about it.
    has_bpchar_ref = False
    for ref in data.get_refs_to(bpchar_name):
        ref_lower = ref.lower()
        if 'spawnoptions_' in ref_lower:
            if debug:
                print('DBG: Got SpawnOptions: {}'.format(ref), file=sys.stderr)
            for so_ref in data.get_refs_from(ref):
                if 'uiname' in so_ref.lower():
                    # Hardcoded fixes here; numbered objects are often screwy w/ JWP
                    if ref.endswith('SpawnOptions_GerPunkSOS_Sales_1') and so_ref.endswith('UIName_GerPunkSOS_Sales'):
                        so_ref = '/Geranium/Enemies/GerPunk_Female/_Unique/SOS_Sales/_Design/Character/UIName_GerPunkSOS_Sales_1'
                    elif ref.endswith('SpawnOptions_GerPunkSOS_Sales_2') and so_ref.endswith('UIName_GerPunkSOS_Sales'):
                        so_ref = '/Geranium/Enemies/GerPunk_Female/_Unique/SOS_Sales/_Design/Character/UIName_GerPunkSOS_Sales_2'
                    elif ref.endswith('SpawnOptions_GerPunkSOS_Sales_3') and so_ref.endswith('UIName_GerPunkSOS_Sales'):
                        so_ref = '/Geranium/Enemies/GerPunk_Female/_Unique/SOS_Sales/_Design/Character/UIName_GerPunkSOS_Sales_3'
                    if debug:
                        print('DBG: Got UIName from SpawnOptions: {}'.format(so_ref), file=sys.stderr)
                    name_obj = data.get_data(so_ref)[0]
                    if 'DisplayName' in name_obj:
                        names.append(name_obj['DisplayName']['string'])
                    else:
                        print('WARNING: DisplayName not found in {}'.format(so_ref), file=sys.stderr)
        elif 'bpchar_' in ref_lower:
            if debug:
                print('DBG: Noticed BPChar reference', file=sys.stderr)
            has_bpchar_ref = True

    # If we have no names by now, see if we reference some other
    # BPChar object; could be that we're inheriting from someone else.
    # Only do this if we have a *single* reference
    if len(names) == 0:
        bpchar_redirect = None
        for ref in from_refs:
            if ref not in bpchar_redirect_excluders:
                if 'bpchar_' in ref.lower():
                    if bpchar_redirect:
                        print('WARNING: More than one bpchar redirect found for {}'.format(bpchar_name), file=sys.stderr)
                    else:
                        if debug:
                            print('DBG: Got BPChar reference: {}'.format(ref), file=sys.stderr)
                        bpchar_redirect = ref
        if bpchar_redirect:
            if 'BPChar_ServiceBot_MeleeEvent2' in bpchar_redirect:
                print('{} -> {}'.format(bpchar_name, bpchar_redirect), file=sys.stderr)
            (new_names, new_has_bpchar_ref) = get_bpchar_names(bpchar_redirect)
            if new_has_bpchar_ref:
                has_bpchar_ref = True
            names.extend(new_names)

    return (names, has_bpchar_ref)

no_alert_exceptions = {
        # No idea, presumably related to all the random people who spawn in at the end of Joey Ultraviolet's fight
        '/Game/PatchDLC/Event2/Enemies/Cyber/Trooper/Basic/_Design/Character/BPChar_TrooperBasicBossAddEvent2',
        '/Game/PatchDLC/Event2/Enemies/Cyber/ServiceBots/Melee/BPChar_ServiceBot_MeleeBossAddEvent2',

        # No idea as well; there *is* a UIName object adjacent to the BPChar, but it's not referenced
        # by anything.  Says "Tito"...
        '/Game/NonPlayerCharacters/_Promethea/RatchGuy/_Design/Character/BPChar_RatchGuy',

        # Ehhh..
        '/Game/Enemies/Ratch/_Unique/NoFeastBasic/_Design/Character/BPChar_RatchNoFeastBasic',
        '/Game/Enemies/Ratch/_Unique/NoFeastPup/_Design/Character/BPChar_RatchNoFeastPup',
        }

# Process!
full_names = {}
for bpchar_name in data.find('', 'BPChar_'):

    # Hardcoded exclusions; not doing antyhing PC related
    if bpchar_name.startswith('/Game/PlayerCharacters/') or bpchar_name.startswith('/Game/OakTest/'):
        continue

    # Get names
    (names, has_bpchar_ref) = get_bpchar_names(bpchar_name)

    # And report-or-catalogue as-needed
    if len(names) == 0 and not has_bpchar_ref and bpchar_name not in no_alert_exceptions:
        print('ALERT: No names found, and not in our no-alert exception list: {}'.format(bpchar_name), file=sys.stderr)
    else:
        short_name = bpchar_name.split('/')[-1]
        if len(names) == 0:
            full_names[short_name] = ['(unknown)']
        else:
            full_names[short_name] = names

# Output!
writer = csv.writer(sys.stdout)
writer.writerow(['BPChar Name', 'Character Names'])
for k, v in sorted(full_names.items(), key=lambda t: t[0].lower()):
    writer.writerow([k, *v])

