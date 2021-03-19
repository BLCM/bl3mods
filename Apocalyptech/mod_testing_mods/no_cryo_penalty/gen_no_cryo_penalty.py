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
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('no_cryo_penalty.bl3hotfix',
        "No Cryo Penalty",
        'Apocalyptech',
        [
            "Gets rid of the movement penalty you'd otherwise suffer when a cryo",
            "effect is applied to your character, and allows sliding while frozen.",
            "This is obviously rather cheaty!",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.1.0',
        cats='cheat',
        )

# We could also just redefine the whole curve to only have a single point, but
# whatever.
mod.comment('Remove the speed debuff')
mod.reg_hotfix(Mod.PATCH, '',
		'/Game/GameData/StatusEffects/Cryo_PenaltyCurvePlayer',
		'FloatCurve.Keys.Keys[1].Value',
		1)
mod.reg_hotfix(Mod.PATCH, '',
		'/Game/GameData/StatusEffects/Cryo_PenaltyCurvePlayer',
		'FloatCurve.Keys.Keys[2].Value',
		1)
mod.newline()

# Now make it so we can slide while frozen, too
mod.comment('Allow sliding while frozen')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PlayerCharacters/_Shared/_Design/Sliding/ControlledMove_Global_Sliding.Default__ControlledMove_Global_Sliding_C',
        'bSpeedAffectedByCryo',
        'False')
mod.newline()

mod.close()
