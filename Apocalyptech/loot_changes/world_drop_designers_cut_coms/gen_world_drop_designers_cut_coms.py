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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, Balance

mod = Mod('world_drop_designers_cut_coms.bl3hotfix',
        'World Drop Designer\'s Cut COMs',
        'Apocalyptech',
        [
            "Adds in the white/green/blue/purple COMs available in the Designer's",
            "Cut DLC (DLC5/Ixora) data to the main world drop pools.  These COMs",
            "are available in the DLC5 game data but aren't actually available to",
            "drop anywhere ordinarily, for some reason.",
            "",
            "The COM names:",
            "",
            "    Beastmaster: Hellhound",
            "    Gunner: Guzzler",
            "    Operative: Bulldog",
            "    Siren: Ascetic",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='gear-com',
        ss=[
            'https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/loot_changes/world_drop_designers_cut_coms/com_beastmaster.png',
            'https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/loot_changes/world_drop_designers_cut_coms/com_gunner.png',
            'https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/loot_changes/world_drop_designers_cut_coms/com_operative.png',
            'https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/loot_changes/world_drop_designers_cut_coms/com_siren.png',
            ],
        )

# Original is misspelled "Acsetic"
mod.header('Fix Siren COM Name')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Ixora/Gear/_GearExtension/NamingStrategies/NamingStrategyExtension_Ixora_CM_Siren',
        'SingleNames.SingleNames[1].NamePart.Object..PartName',
        'Ascetic',
        )
mod.newline()

# Now the bulk of the mod
mod.header('Add in DLC5 COMs')
data = BL3Data()
for base_char, dlc5_dir, dlc5_char in [
        ('Beastmaster', 'BSM', 'BSM'),
        ('Gunner', 'GUN', 'GUN'),
        ('Operative', 'OPE', 'OPE'),
        ('Siren', 'SRN', 'SIR'),
        ]:

    for rarity in [
            '01_Common',
            '02_Uncommon',
            '03_Rare',
            '04_VeryRare',
            ]:

        print('Processing {} {}'.format(base_char, rarity))
        base_com_name = f'/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_{base_char}_{rarity}'
        dlc5_com_name = f'/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/{dlc5_dir}/PartSets/InvBalD_CM_Ixora_{dlc5_char}_{rarity}'

        base_com = Balance.from_data(data, base_com_name)
        dlc5_com = Balance.from_data(data, dlc5_com_name)

        # Grab the relevant "new" parts from the DLC5 COMs.  Namely, the main COM part,
        # and all the skill parts.  Obviously we're just hardcoding the indicies for
        # the various categories here.
        modtype_part = None
        skill_parts = []
        for idx, cat in enumerate(dlc5_com.categories):
            if idx == 1:
                assert(len(cat.partlist) == 1)
                modtype_part = cat.partlist[0].part_name
            elif idx == 5:
                for part in cat.partlist:
                    skill_parts.append(part.part_name)
        assert(modtype_part)
        assert(skill_parts)

        # Now add those in to the base-game COMs
        for idx, cat in enumerate(base_com.categories):
            if idx == 1:
                cat.add_part_name(modtype_part)
            elif idx == 3:
                # While we're in here, fix up the blank Primary part that Siren COMs can
                # spawn with.  The Fix Siren COM Blank Parts mod does this too, but since
                # we're changing the indexes, it won't actually know what to do with this.
                # So that mod should be run first, and then this mod will overwrite the
                # Balance completely.
                if base_char == 'Siren':
                    for part in cat.partlist:
                        if part.part_name == 'None':
                            part.weight = BVC(bvc=0)
            elif idx == 5:
                for part in skill_parts:
                    cat.add_part_name(part)

        # ... and now write out the hotfixes
        mod.comment('{} {}'.format(base_char, rarity))
        base_com.hotfix_balance_full(mod)
        mod.newline()

mod.close()
