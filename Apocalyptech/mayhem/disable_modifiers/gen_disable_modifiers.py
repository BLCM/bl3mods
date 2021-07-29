#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod

data = BL3Data()

for short_name, cat_name in [
        ('EAsy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
        ('VeryHard', 'Very Hard'),
        ]:

    cat_filename = cat_name.lower().replace(' ', '_')

    modset_obj_name = f'/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_{short_name}'
    modset_obj = data.get_export_idx(modset_obj_name, 1)

    #print(f'Processing {modset_obj_name}...')
    for idx, modset in enumerate(modset_obj['ModifierSets']):
        text_obj = data.get_export_idx(modset['UIStats'][0][1], 1)
        modifier_name = text_obj['Text']['string'].split('] ', 1)[1]
        modifier_name_lower = modifier_name.lower().replace(' ', '_')

        mod = Mod(f'disable_modifier_{cat_filename}_{modifier_name_lower}.bl3hotfix',
                f'Disable Mayhem Modifier ({cat_name}): {modifier_name}',
                'Apocalyptech',
                [
                    f"Disables the '{modifier_name}' {cat_name} mayhem modifier.",
                ],
                contact='https://apocalyptech.com/contact.php',
                lic=Mod.CC_BY_SA_40,
                v='1.0.0',
                cats='mayhem',
                )

        mod.reg_hotfix(Mod.PATCH, '',
                modset_obj_name,
                f'ModifierSets.ModifierSets[{idx}].Weight',
                0)

        mod.close()

