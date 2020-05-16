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
from bl3hotfixmod.bl3hotfixmod import Mod, Balance, BVCF

mod = Mod('enable_pendant_of_terra.txt',
        'Enable Pendant of Terramorphous Artifact',
        'Apocalyptech',
        [
            "Pendant of Terramorphous is an Artifact which is in the BL3 data but",
            "was apparently cut sometime before release.  This sets it as a valid",
            "legendary Artifact drop.  It also increases the health regen rate from",
            "the 'default' (which is *extremely* weak, presumably before any balancing",
            "attempts had been made) to something which feels somewhat reasonable.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

art_bal_name = '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_05_Legendary'
cat_idx = 1
terra_part = '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Legendary/Misc/PendantOfTerramorphous/Artifact_Part_Ability_PendantOfTerramorphous'

# Add the part
mod.comment('Set as a valid drop')
data = BL3Data()
art_bal = Balance.from_data(data, art_bal_name)
cat = art_bal.categories[cat_idx]
if len(cat) != 14:
    raise Exception('Expected to find a category with fourteen parts!')
cat.add_part_name(terra_part, 1)
art_bal.hotfix_balance_full(mod)
mod.newline()

# Now buff up its health regen rate -- the default is really anemic (presumably it
# was scrapped before they got around to looking at balancing it).  Default value
# is `0.001`.
mod.comment('Buff health regen')
mod.table_hotfix(Mod.PATCH, '',
        '/Game/Gear/Artifacts/_Design/Balance/Table_Artifact_Abilities2',
        'LEGENDARY_BloodOfTerramorphous_HealthRegen',
        'Multiplier',
        BVCF(bvc=0.03))
mod.newline()

mod.close()
