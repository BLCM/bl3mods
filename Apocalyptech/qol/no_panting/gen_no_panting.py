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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('no_panting.bl3hotfix',
        'No Panting',
        'Apocalyptech',
        [
            "Disables the 'tired' panting sound effect loop when you've been",
            "sprinting for awhile."
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol',
        )

for label, obj_name in [
        ('Gunner', 'Sounds_PL_Gunner'),
        ('Operative', 'Sounds_PL_Operative'),
        ('Siren', 'Sounds_PL_Siren'),
        ]:
    mod.comment(label)
    for attr in ['StartEvent', 'StopEvent']:
        mod.reg_hotfix(Mod.PATCH, '',
                f'/Game/PlayerCharacters/_Shared/_Design/Audio/{obj_name}',
                f'VocalLoops.VocalLoops.VocalLoops[1].{attr}',
                # lol
                #Mod.get_full_cond('/Game/Audio/Events/VO/VOBD/PL_Siren/WE_Oak_VOBD_PL_Siren_Pain_Fire_LP', 'WwiseEvent'))
                'None')
    mod.newline()

mod.close()
