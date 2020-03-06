#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF
from bl3data.bl3data import BL3Data

bl3data = BL3Data()
mod = Mod('no_projected_shields.txt',
        'No Projected Shields',
        [
            'Makes shields never spawn with the "projected" effect',
        ],
        'NoProjected',
        )

sections = {}
def do_start(mod, section_name):
    global sections
    if section_name not in sections:
        sections[section_name] = True
        mod.comment(section_name)

def do_end(mod, section_name):
    global sections
    if section_name in sections:
        mod.newline()

# We need to check PartSets for bUseWeightWithMultiplePartSelection, and possibly
# they might be referenced in more than one place?  So we'll keep track of which
# ones we've touched already
partset_seen = set()

# Grab all references to the aug and clear 'em out
aug_name = '/Game/Gear/Shields/_Design/PartSets/Part_Augment/ProjectedShield/Part_Shield_Aug_Projected'
obj_names = bl3data.get_refs_to(aug_name)
for obj_name in sorted(obj_names):

    last_component = obj_name.split('/')[-1]

    if 'Naming' in obj_name:
        continue

    elif 'InvBalD' in obj_name:
        # Should just have a single export
        data = bl3data.get_data(obj_name)
        if len(data) != 1:
            raise Exception('InvBalD with an unknown export count ({}): {}'.format(len(data), obj_name))

        # Map a part index to what'll be an ActorPartList in the PartSet
        part_idx_to_apl_idx = {}
        for (apl_idx, toc) in enumerate(data[0]['RuntimePartList']['PartTypeTOC']):
            if toc['NumParts'] > 0 and toc['StartIndex'] >= 0:
                for part_idx in range(toc['StartIndex'], toc['StartIndex']+toc['NumParts']):
                    part_idx_to_apl_idx[part_idx] = apl_idx

        # Now loop through parts
        apl_idxes_to_check = set()
        for (part_idx, part) in enumerate(data[0]['RuntimePartList']['AllParts']):
            if part['PartData'][1] == aug_name:
                do_start(mod, last_component)
                mod.reg_hotfix(Mod.PATCH, '',
                        obj_name,
                        'RuntimePartList.AllParts.AllParts[{}].Weight'.format(part_idx),
                        BVCF(bvc=0))
                apl_idxes_to_check.add(part_idx_to_apl_idx[part_idx])
        do_end(mod, last_component)

        # Check the PartSet for weighting, if we haven't already
        if len(apl_idxes_to_check) > 0:
            partset_name = data[0]['PartSetData'][1]
            partset_cat = '{} Weighting'.format(partset_name.split('/')[-1])
            if partset_name not in partset_seen:
                partset_seen.add(partset_name)
                partset_data = bl3data.get_data(partset_name)
                if len(partset_data) != 1:
                    raise Exception('PartSet with an unknown export count ({}): {}'.format(len(partset_data), partset_name))
                for apl_idx in sorted(apl_idxes_to_check):
                    if not partset_data[0]['ActorPartLists'][apl_idx]['bUseWeightWithMultiplePartSelection']:
                        do_start(mod, partset_cat)
                        mod.reg_hotfix(Mod.PATCH, '',
                                partset_name,
                                'ActorPartLists.ActorPartLists[{}].bUseWeightWithMultiplePartSelection'.format(apl_idx),
                                'True')
                do_end(mod, partset_cat)

    elif 'PartSet' in obj_name:
        # Should just have a single export
        # Not actually sure if the weights here are actually used; I suspect it's just the Balance.
        # The bUseWeightWithMultiplePartSelection attr *is* used, though we don't actually catch
        # any of those here; all the InvBalD's above have already linked through to 'em.
        data = bl3data.get_data(obj_name)
        if len(data) != 1:
            raise Exception('PartSet with an unknown export count ({}): {}'.format(len(data), obj_name))
        for (apl_idx, apl) in enumerate(data[0]['ActorPartLists']):
            had_aug = False
            for (part_idx, part) in enumerate(apl['Parts']):
                if part['PartData'][1] == aug_name:
                    had_aug = True
                    do_start(mod, last_component)
                    mod.reg_hotfix(Mod.PATCH, '',
                            obj_name,
                            'ActorPartLists.ActorPartLists[{}].Parts.Parts[{}].Weight'.format(apl_idx, part_idx),
                            BVCF(bvc=0))
            if obj_name not in partset_seen and had_aug and not apl['bUseWeightWithMultiplePartSelection']:
                partset_seen.add(obj_name)
                mod.reg_hotfix(Mod.PATCH, '',
                        obj_name,
                        'ActorPartLists.ActorPartLists[{}].bUseWeightWithMultiplePartSelection'.format(apl_idx),
                        'True')
        do_end(mod, last_component)

    else:
        raise Exception('Unknown object: {}'.format(obj_name))

mod.close()
