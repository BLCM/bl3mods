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
from bl3hotfixmod.bl3hotfixmod import Mod, LVL_TO_ENG

mod = Mod('no_hidden_eridium.bl3hotfix',
        'No Hidden Eridium',
        'Apocalyptech',
        [
            "DLC6 (Director's Cut) added in the chance for eridium clusters and",
            "eridium jars to spawn in a 'spectral' variety which requires the",
            "player to have a Mysterious Amulet equipped to see.  The visual",
            "effect is neat, but this mod makes it so that all eridium cluster/jar",
            "spawns are ordinary, and don't require the Amulet to discover.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.1',
        cats='maps',
        )

# This is one easy way to accomplish it for every map before DLC6, but the Director's
# Cut maps have hardcoded spawns, so we may as well just do the other option anyway.
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/PatchDLC/Ixora2/GameData/DLCData/SpawnDLCExpansion_Ixora2_Eridium',
#        'GlobalReplacement',
#        '()')

mod.comment('Eridium Clusters')
for idx in [3, 4, 5]:
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Ixora2/Lootables/Eridium/SpawnOption_EridianCrystal_IxoraAndBase',
            f'Options.Options[{idx}].WeightParam.Range.Value',
            0)
mod.newline()

mod.comment('Eridium Jars')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Ixora2/Lootables/Eridium/SpawnOption_EridianJar_IxoraAndBase',
        'Options.Options[0].WeightParam.Range.Value',
        0)
mod.newline()

mod.close()

