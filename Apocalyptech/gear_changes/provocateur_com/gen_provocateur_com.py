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
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF, ItemPool

mod = Mod('provocateur_com.bl3hotfix',
        'Provocateur COM (Unreleased Ixora Operative COM)',
        'Apocalyptech',
        [
            "The Designer's Cut DLC (Ixora) data included an unreleased/unfinished",
            "second Operative COM, to go along with the Spy COM.  With just a bit of",
            "tweaking, the unreleased mod can be fixed up to operate as-advertised",
            "on the COM text, so that's what this mod does.  The COM does not have a",
            "name defined anywhere in the game data, so this mod assigns it the name",
            "'Provocateur'.",
            "",
            "From the on-card COM description: \"Whenever Zane scores a Critical Hit",
            "he has a 10% chance to activate all kill skills twice.  Additionally, his",
            "kill skills last an additional 8 seconds.\"",
            "",
            "This mod makes use of a naming part taken from another unreleased bit of",
            "gear, the 'Portals and Shite,' a completely-unimplemented named Atlas",
            "AR which has nothing special about it apart from the name.  If any other",
            "mods end up using the Portals and Shite naming part as well, this mod",
            "won't be fully compatible with it.",
            "",
            "This mod also adds the Provocateur to the relevant drop pools, so it",
            "should be gettable from any source which would ordinarily drop the Spy.",
            "The probability of Spy was dropped a little bit to make room for the",
            "new COM, without diluting the rest of the pools too much (Spy and",
            "Provocateur are equally-likely drops).",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='gear-com',
        ss='https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/gear_changes/provocateur_com/screenshot.png',
        )

# Just for reference, the on-disk "vanilla" COM actually procs at 100% of crits, and
# applies the full Spy effect (extra duration, +10% effectiveness) as opposed to just
# the extra duration on the card.  Basically practically every part of the COM is pulling
# from the wrong values (mostly pointing back at Spy's vars/objects), so our work here
# is largely just redirecting those things back to the objects/vars actually associated
# with this COM.

# Buncha objects whose names get used more than once
cm_ability = '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/Ability_CM_Ixora_OPE_L02'
cm_ability_last = cm_ability.split('/')[-1]
cm_ability_def = '{}.Default__{}_C'.format(cm_ability, cm_ability_last)
title = '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Portal/Name_ATL_AR_Portals'
name_ext = '/Game/PatchDLC/Ixora/Gear/_GearExtension/NamingStrategies/NamingStrategyExtension_Ixora_CM_Operative'
table = '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/Table_CM_Ixora'
duration_effect = '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/StatusEffect_CM_Ixora_L02_OPE'
balance = '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/InvBalD_CM_Ixora_OPE_L02'
card_desc = '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/UIStat_CM_Ixora_OPE_L02_Description'

# Values we're going to set.
#
# Re: red text, I'm not super fond of just parroting Fight Club quotes out of context,
# but I had no other ideas, and this one comes from the same scene as the quote from
# the Spy mod, so it seemed fitting.
#
# Re: proc chance, the value in the on-disk datatable corresponding to chance is actually
# 50%, but that seems awfully high.  We're seeing it down to the 10% that the item card
# was reporting in its vanilla broken state.
com_name = 'Provocateur'
flavor = "First you have to know -- not fear -- know that someday you're gonna die."
proc_chance = 0.1
extra_time = 8

# Naming - we're reusing a naming object from the unreleased (and very uninteresting)
# Portals and Shite Atlas AR to do this, since this COM has no naming object of its
# own.

mod.header('Add a name to the COM')

mod.reg_hotfix(Mod.PATCH, '',
        title,
        'PartName',
        com_name,
        )

bits = []
for part, part_title in [
        ('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L01/Part_CM_Ixora_OPE_L01',
            'NamePart_InventoryNamePartData'),
        ('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/PartSets/ClassMod_Part_Mod_Operative_Ixora_01',
            'NamePart_InventoryNamePartData_1'),
        ('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/Skills/CM_Part_Skill_OPE_DLCSkill_12',
            'NamePart_InventoryNamePartData_2'),
        ('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/Part_CM_Ixora_OPE_L02',
            title),
        ]:
    if part_title.startswith('/'):
        title_ref = Mod.get_full_cond(part_title, 'InventoryNamePartData')
    else:
        title_ref = Mod.get_full_cond('{}:{}'.format(Mod.get_full_cond(name_ext), part_title), 'InventoryNamePartData')
    bits.append('(Part={},NamePart={})'.format(
        Mod.get_full_cond(part, 'BPInvPart_ClassMod_C'),
        title_ref,
        ))

mod.reg_hotfix(Mod.PATCH, '',
        name_ext,
        'SingleNames',
        '({})'.format(','.join(bits)),
        )

mod.newline()

# Red Text.

mod.header('Red Text')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/UIText_CM_Ixora_OPE_L02_RedText',
        'Text',
        '[flavor]{}[/flavor]'.format(flavor),
        )
mod.newline()

# Update the chance of proc'ing to 10%

mod.header('Tweak activation chance to match description')

mod.reg_hotfix(Mod.PATCH, '',
        cm_ability_def,
        'Chance.RowName',
        'OperativeL02',
        )

mod.table_hotfix(Mod.PATCH, '',
        table,
        'OperativeL02',
        'Value_B_5_AC44446B4200DFD2A654AC85CC59B4B0',
        proc_chance,
        )

mod.newline()

# Have the kill-skill duration boost use the "proper" variables, and fix the related
# datatable entry.

mod.header('Fix kill-skill duration boost')

mod.reg_hotfix(Mod.PATCH, '',
        cm_ability_def,
        'AbilityEffects.AbilityEffects[0].StatusEffectData',
        Mod.get_full_cond(duration_effect, 'StatusEffectData'),
        )

mod.table_hotfix(Mod.PATCH, '',
        table,
        'OperativeL02',
        'Value_A_2_4C4DFC67484D02BA3DBB029A999F015E',
        extra_time,
        )

mod.newline()

# Update card display attributes.  This isn't *really* necessary at the moment since the
# COM happens to display the correct values anyway, but if we ever change up the proc
# chance or extra duration, this'll ensure that the card continues to report the correct
# values.

mod.header('Ensure card reports correct values')

mod.reg_hotfix(Mod.PATCH, '',
        card_desc,
        'Attribute',
        Mod.get_full_cond('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/Att_CM_Ixora_OPE_L02_Chance', 'GbxAttributeData'),
        )

mod.reg_hotfix(Mod.PATCH, '',
        card_desc,
        'SupplementalStat.Object..Initializer.BaseValueAttribute',
        Mod.get_full_cond('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/Att_CM_Ixora_OPE_L02_Duration', 'GbxAttributeData'),
        )

mod.newline()

mod.comment('Also fix a minor grammatical error')
mod.reg_hotfix(Mod.PATCH, '',
        card_desc,
        'SupplementalStat.Object..FormatText',
        'Additionally, his kill skills last an additional [skillbold]$VALUE$ seconds[/skillbold].',
        )

mod.newline()

# Add to the drop pools

mod.header('Add to drop pools')

data = BL3Data()
for pool_name in [
        '/Game/PatchDLC/Ixora/GameData/Loot/ItemPools/Chest/Event/ItemPool_GearUp_Event_Industry_Legendary',
        '/Game/PatchDLC/Ixora/GameData/Loot/ItemPools/ItemPool_Ixora_All_Legendary',
        ]:
    short_name = pool_name.split('/')[-1]
    pool = ItemPool.from_data(data, pool_name)
    weight = None
    for drop in pool.balanceditems:
        if drop.balance_name and 'InvBalD_CM_Ixora_OPE_L01' in drop.balance_name:
            drop.weight.bvs /= 1.5
            weight = drop.weight
            break
    if not weight:
        raise Exception("Couldn't find Spy mod in {}".format(short_name))
    pool.add_balance(balance, weight)
    mod.comment(short_name)
    mod.reg_hotfix(Mod.LEVEL, 'FrostSite_P',
            pool_name,
            'BalancedItems',
            str(pool),
            )
    mod.newline()

mod.close()
