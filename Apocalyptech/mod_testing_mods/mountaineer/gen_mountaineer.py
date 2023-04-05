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
import math
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('mountaineer.bl3hotfix',
        "Mountaineer",
        'Apocalyptech',
        [
            "Allows the player to walk up (nearly) vertical walls (though true",
            "90-degree walls or overhangs will still be impassable).  Note that",
            "there are definitely circumstances where you can get flung",
            "extremely high in the air while using this, and you run an increased",
            "chance of getting stuck somewhere in the level.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='cheat',
        )

# Default: 46
# Setting this all the way to 90 is *mostly* fine but increases the probability of weird
# edge cases; like on the path in The Droughts from Sanctuary's berth to Tannis's research
# area, there's an arm just floating up in the sky (out of view from the ground); with
# the value at 90, walking underneath that hand rockets the player up into the air,
# sometimes *super* high depending on the player speed at the time.  That kind of thing
# is still possible even at 89, but at least in those cases you've usually got a
# pretty obvious cause for it.
degree_to_set = 89

# Default: 45 for char, 50 for sliding
step_height = 400

for char, obj_name in [
        ('Beastmaster', '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPChar_Beastmaster.Default__BPChar_Beastmaster_C'),
        ('Gunner', '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/BPChar_Gunner.Default__BPChar_Gunner_C'),
        ('Operative', '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/BPChar_Operative.Default__BPChar_Operative_C'),
        ('Siren', '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/BPChar_Siren.Default__BPChar_Siren_C'),
        ]:

    mod.comment(char)

    # Default: 46
    mod.reg_hotfix(Mod.PATCH, '',
            obj_name,
            'OakCharacterMovement.Object..WalkableFloorAngle',
            degree_to_set)

    mod.reg_hotfix(Mod.PATCH, '',
            obj_name,
            'OakCharacterMovement.Object..WalkableFloorZ',
            '{:.6f}'.format(math.cos(math.radians(degree_to_set))))

    # Default: 45
    mod.reg_hotfix(Mod.PATCH, '',
            obj_name,
            'OakCharacterMovement.Object..MaxStepHeight',
            step_height)

    mod.newline()

# Default: 50
mod.comment('Sliding (global)')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PlayerCharacters/_Shared/_Design/Sliding/ControlledMove_Global_Sliding.Default__ControlledMove_Global_Sliding_C',
        'MaxStepHeight',
        step_height)
mod.newline()

mod.close()
