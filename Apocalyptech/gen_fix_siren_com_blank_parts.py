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

import collections
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('fix_siren_com_blank_parts.txt',
        'Fix Siren COM Blank Parts',
        'Apocalyptech',
        [
            "Siren COMs have a 'None' part in their PRIMARY part category, which",
            "means that those COMs might spawn with a missing part, compared to",
            "COMs from all other characters.  This will fix those so that the",
            "empty part can never be chosen.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

data = BL3Data()

# I suppose that we could use data introspection to find the None parts -- we're
# even loading the balance to find the partset.  But whatever, I've already
# hardcoded the empty part indicies.
for bal_name, part_idx in [

        # Base game COMs
        ('/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_01_Common', 81),
        ('/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_02_Uncommon', 81),
        ('/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_03_Rare', 81),
        ('/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_04_VeryRare', 81),
        ('/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_05_Legendary', 76),

        # Trials Dedicated COM sources
        ('/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Breaker', 72),
        ('/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Dragon', 72),
        ('/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Elementalist', 72),
        ('/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Nimbus', 72),
        ('/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Phasezerker', 72),

        # Maliwan Takedown COM
        ('/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_Raid1', 72),

        # DLCs
        ('/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_DLC1', 72),
        ('/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Hib', 72),
        ]:

    # Set the `None` weight to zero
    mod.reg_hotfix(Mod.PATCH, '',
            bal_name,
            'RuntimePartList.AllParts.AllParts[{}].Weight'.format(part_idx),
            BVCF(bvc=0))

    # Find the category index and partset name to make sure that it's using the weight.
    bal_obj = data.get_data(bal_name)[0]
    partset_name = bal_obj['PartSetData'][1]
    cat_idx = 0
    for idx, toc in enumerate(bal_obj['RuntimePartList']['PartTypeTOC']):
        if toc['StartIndex'] > part_idx:
            break
        if toc['NumParts'] > 0:
            cat_idx = idx

    # Now do those updates
    mod.reg_hotfix(Mod.PATCH, '',
            partset_name,
            'ActorPartLists.ActorPartLists[{}].bUseWeightWithMultiplePartSelection'.format(cat_idx),
            'True')

mod.close()
