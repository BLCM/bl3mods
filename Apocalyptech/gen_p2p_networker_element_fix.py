#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import collections
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('p2p_networker_element_fix.txt',
        'P2P Networker Element Fix',
        [
            "P2P Networker is an unfinished/unreleased gun that's still present in the",
            "BL3 data.  It's basically a more-powerful redistributor.  One thing broken",
            "about it is that it only has a primary element, but will still let you",
            "'switch' elements, which results in a message like 'GUN TEAM FIX NAME PLZ'",
            "in the game's UI.  Amusing as that is, this mod will add in a secondary",
            "element to the gun, so that it can be switched properly just like any other",
            "Maliwan weapon.",
        ])

# Some assumptions we can make, since we're just dealing with the one balance:
#  1) The "secondary element" part group is the only empty group in the list.
#  2) The weights of the elements should all just be 1 (since that's what the Primary element uses)
#  3) The BVC is the only part of the part weights that we have to worry about

p2p_bal = '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link'
part_type = 'BPInvPart_Maliwan_SMG_C'
extra_elements = [
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_01_Fire',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_02_Cryo',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_03_Shock',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_04_Radiation',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_05_Corrosive',
        ]

# Grab the data and start processing
data = BL3Data()
p2p_obj = data.get_exports(p2p_bal, 'InventoryBalanceData')[0]

# First the TOC
TocEntry = collections.namedtuple('TocEntry', ['StartIndex', 'NumParts'])
toc_vals = []
our_cat_idx = None
part_start_idx = None
for idx, toc in enumerate(p2p_obj['RuntimePartList']['PartTypeTOC']):
    if our_cat_idx is None:
        if toc['NumParts'] == 0:
            our_cat_idx = idx
            part_start_idx = toc_vals[-1].StartIndex + toc_vals[-1].NumParts
            toc_vals.append(TocEntry(part_start_idx, len(extra_elements)))
        else:
            toc_vals.append(TocEntry(toc['StartIndex'], toc['NumParts']))
    else:
        toc_vals.append(TocEntry(toc_vals[-1].StartIndex + toc_vals[-1].NumParts, toc['NumParts']))
if our_cat_idx is None:
    raise Exception('Did not find empty part category')

# Hotfix for TOC
mod.reg_hotfix(Mod.PATCH, '',
        p2p_bal,
        'RuntimePartList.PartTypeTOC',
        '({})'.format(','.join(['(StartIndex={},NumParts={})'.format(t.StartIndex, t.NumParts) for t in toc_vals])))

# Now the parts themselves, for the balance
Part = collections.namedtuple('Part', ['part_obj', 'weight'])
parts = []
for idx, part in enumerate(p2p_obj['RuntimePartList']['AllParts']):

    # Inject our elements if we've gotten to the right index
    if idx == part_start_idx:
        for element in extra_elements:
            parts.append(Part(element, 1))

    # Add in the part that we're actually on.
    if 'export' in part['PartData']:
        parts.append(Part('None', part['Weight']['BaseValueConstant']))
    else:
        parts.append(Part(part['PartData'][1], part['Weight']['BaseValueConstant']))

# Hotfix for partlist
mod.reg_hotfix(Mod.PATCH, '',
        p2p_bal,
        'RuntimePartList.AllParts',
        '({})'.format(','.join(
            ['(PartData={},Weight={})'.format(Mod.get_full_cond(p.part_obj, part_type), BVC(bvc=p.weight)) for p in parts])))

# Grab the PartSet name and ensure that the secondary element slot is enabled
partset_name = p2p_obj['PartSetData'][1]
mod.reg_hotfix(Mod.PATCH, '',
        partset_name,
        'ActorPartLists.ActorPartLists[{}].bEnabled'.format(our_cat_idx),
        'True')

mod.close()
