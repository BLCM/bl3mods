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
import collections
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF, Balance

mod = Mod('fix_siren_com_blank_parts.bl3hotfix',
        'Fix Siren COM Blank Parts',
        'Apocalyptech',
        [
            "Siren COMs have a 'None' part in their PRIMARY part category, which",
            "means that those COMs might spawn with a missing part, compared to",
            "COMs from all other characters.  This will fix those so that the",
            "empty part can never be chosen.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.2.0',
        cats='gear-com, bugfix',
        )

data = BL3Data()

# I suppose that we could use data introspection to find the None parts -- we're
# even loading the balance to find the partset.  But whatever, I've already
# hardcoded the empty part indicies.
for bal_name in [

        # Base game COMs
        '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_01_Common',
        '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_02_Uncommon',
        '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_03_Rare',
        '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_04_VeryRare',
        '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_05_Legendary',

        # Trials Dedicated COM sources
        '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Breaker',
        '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Dragon',
        '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Elementalist',
        '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Nimbus',
        '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Phasezerker',

        # Maliwan Takedown COM
        '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_Raid1',

        # DLCs
        '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_DLC1',
        '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Hib',
        '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Alisma',
        '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/L01/InvBalD_CM_Ixora_SRN_L01',
        '/Game/PatchDLC/Ixora2/Gear/ClassMods/_Design/SRN/L01/InvBalD_CM_Ixora2_SRN_L01',
        ]:

    bal = Balance.from_data(data, bal_name)

    found_part = False
    part_idx = 0
    for cat in bal.categories:
        for part in cat.partlist:
            # Our PRIMARY part will always be category index 3
            if cat.index == 3 and part.part_name == 'None':
                # Set the weight of the `None` part to zero
                mod.reg_hotfix(Mod.PATCH, '',
                        bal_name,
                        'RuntimePartList.AllParts.AllParts[{}].Weight'.format(part_idx),
                        BVCF(bvc=0))

                # Make sure we're using weights
                mod.reg_hotfix(Mod.PATCH, '',
                        bal.partset_name,
                        'ActorPartLists.ActorPartLists[{}].bUseWeightWithMultiplePartSelection'.format(cat.index),
                        'True')

                # Break out of the loop
                found_part = True
                break
            part_idx += 1
        if found_part:
            break

mod.close()
