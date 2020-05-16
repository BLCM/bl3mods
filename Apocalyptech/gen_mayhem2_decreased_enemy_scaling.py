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

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('mayhem2_decreased_enemy_scaling.txt',
        'Mayhem 2.0: Decreased Enemy Scaling',
        'Apocalyptech',
        [
            "I'd like to play around with Mayhem modifiers, but the extra bullet-",
            "sponginess doesn't really do it for me.  This'll drop the enemy",
            "health/shield/armor scaling down pretty significantly.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

# TODO: Honestly I should really nerf the Mayhem gun parts themselves, too,
# 'cause they're gonna end up OP as hell.  Unfortunately the actual part
# objects only seem to really have scaling for cost and weapon score in them,
# and not the actual scaling.  Presumably that's built-in somehow to the
# OakWeaponMayhemPartData object type.

# Default scaling values:
#scaling = [2, 4, 6, 8, 15, 30, 50, 75, 100, 125]

# My original new values (hah, pathetic!)
#scaling = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]

# My most recent values (even more pathetic!)
scaling = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 4.5, 5, 5]

for mayhem_level_minus_one, scale_value in enumerate(scaling):
    mayhem_level = mayhem_level_minus_one + 1
    mod.comment('Mayhem {}'.format(mayhem_level))
    for col_name in [
            'HealthSimpleScalar_42_0499AACF43FDF39B7084E2BB63E4BF68',
            'ShieldSimpleScalar_43_417C36C54DA2550A4CABC7B26A5E24A8',
            'ArmorSimpleScalar_44_BCAAA445479831C25B0D55AF294A15D6',
            ]:
        mod.table_hotfix(Mod.PATCH, '',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                mayhem_level,
                col_name,
                scale_value)
    mod.newline()

mod.close()
