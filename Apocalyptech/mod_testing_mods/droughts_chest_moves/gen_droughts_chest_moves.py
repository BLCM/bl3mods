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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('droughts_chest_moves.bl3hotfix',
        'Droughts Chest Moves',
        'Apocalyptech',
        [
            "Moves white+red chests in The Droughts to right near the Highway FT.",
            "Primarily just used for testing out my Red Chest Timer Reset and",
            "Reopenable Gear Chests mods, but also might be useful to other folks",
            "as an example of moving objects around a map.",
            ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='resource',
        )

level = 'Prologue_P'

for label, objects, linestart, lineend, (rot_p, rot_y, rot_r) in [
        ('Red Chests',
            [
                '/Game/Maps/Zone_0/Prologue/Prologue_Combat.Prologue_Combat:PersistentLevel.BPIO_Lootable_COV_RedCrate_114',
                '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BPIO_Lootable_COV_RedCrate_114',
                '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BPIO_Lootable_COV_RedCrate_1290',
                ],
            (49208, 25830, -3775),
            (49529, 26964, -3775),
            (180, 70, 90),
            ),
        ('White Chests',
            [
                '/Game/Maps/Zone_0/Prologue/Prologue_Combat.Prologue_Combat:PersistentLevel.BPIO_Lootable_Global_WhiteCrate_3',
                '/Game/Maps/Zone_0/Prologue/Prologue_Combat.Prologue_Combat:PersistentLevel.BPIO_Lootable_Global_WhiteCrate_396',
                '/Game/Maps/Zone_0/Prologue/Prologue_Combat.Prologue_Combat:PersistentLevel.BPIO_Lootable_Global_WhiteCrate_4',
                '/Game/Maps/Zone_0/Prologue/Prologue_Combat.Prologue_Combat:PersistentLevel.BPIO_Lootable_Global_WhiteCrate_8',
                '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BPIO_Lootable_Global_WhiteCrate_2',
                '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BPIO_Lootable_Global_WhiteCrate_3',
                '/Game/Maps/Zone_0/Prologue/Prologue_Terrain.Prologue_Terrain:PersistentLevel.BPIO_Lootable_Global_WhiteCrate_0',
                '/Game/Maps/Zone_0/Prologue/Prologue_Terrain.Prologue_Terrain:PersistentLevel.BPIO_Lootable_Global_WhiteCrate_2',
                ],
            (48173, 27754, -3768),
            (47247, 26181, -3768),
            (0, 240, 90),
            ),
        ]:

    mod.header(label)

    if len(objects) > 1:
        delta_x = (lineend[0]-linestart[0])/(len(objects)-1)
        delta_y = (lineend[1]-linestart[1])/(len(objects)-1)
        delta_z = (lineend[2]-linestart[2])/(len(objects)-1)
    else:
        delta_x = 0
        delta_y = 0
        delta_z = 0

    cur_x, cur_y, cur_z = linestart
    for obj_name in objects:
        mod.reg_hotfix(Mod.LEVEL, level,
                f'{obj_name}.Mesh_Chest1',
                'RelativeLocation',
                '(x={},y={},z={})'.format(
                    round(cur_x, 1),
                    round(cur_y, 1),
                    round(cur_z, 1),
                    ),
                notify=True)
        mod.reg_hotfix(Mod.LEVEL, level,
                f'{obj_name}.Mesh_Chest1',
                'RelativeRotation',
                f'(pitch={rot_p},yaw={rot_y},roll={rot_r})',
                notify=True)
        cur_x += delta_x
        cur_y += delta_y
        cur_z += delta_z

    mod.newline()

mod.close()
