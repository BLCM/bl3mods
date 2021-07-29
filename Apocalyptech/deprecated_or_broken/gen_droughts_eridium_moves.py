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
sys.path.append('../../python_mod_helpers')
sys.path.append('../dataprocessing/map_objects')
from mapobjlib.mapobjlib import MapObjects
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('droughts_eridium_moves.txt',
        'Droughts Eridium Moves',
        'Apocalyptech',
        [
            "Mod which moves all small Eridium piles in The Droughts into a line",
            "near the Highway Fast Travel point.  Also alters the Dens so that",
            "they can all spawn at once.",
            ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='resource',
        )

level = 'Prologue_P'

# Map Objects
mo = MapObjects()

objects = []
for level, object_path in mo.get_by_type('SpawnPoint_IO_C', level):
    if 'EridiumCrystal_Small' in object_path:
        objects.append(object_path)

#linestart = (48173, 27754, -3868)
#lineend = (47247, 26181, -3868)
linestart = (49283, 28145, -3815)
lineend = (45688, 24466, -3744)
#linestart = (49283, 28145, -3315)
#lineend = (45688, 24466, -3144)
delta_x = (lineend[0]-linestart[0])/(len(objects)-1)
delta_y = (lineend[1]-linestart[1])/(len(objects)-1)
delta_z = (lineend[2]-linestart[2])/(len(objects)-1)
cur_x, cur_y, cur_z = linestart

for obj_name in objects:

    mod.reg_hotfix(Mod.LEVEL, level,
            f'{obj_name}.SceneComp',
            'RelativeLocation',
            '(x={},y={},z={})'.format(
                round(cur_x, 1),
                round(cur_y, 1),
                round(cur_z, 1),
                ),
            notify=True)
    cur_x += delta_x
    cur_y += delta_y
    cur_z += delta_z

mod.newline()

mod.header('Trying to get more to spawn')

den_obj = '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.OakSpawner_EridiumCrystals.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den'

# Change the spawner to something that always shows up
spawner = '/Game/Lootables/Eridian/Rock_Formation_Pile/_Design/SpawnOption_EridianCrystal_Small'
#spawner = '/Game/Lootables/_Design/Data/Industrial/SpawnOptions_CoV_CardboardBox'
#spawner = '/Game/PatchDLC/Ixora/Lootables/_Design/Data/GearUp/SpawnOptions_VendingMachine_Weapons_GearUp'

# This one *must* be a non-Early level.  Using EARLY will make it not work.  Does not
# require notify.
#for hf_type in [Mod.LEVEL, Mod.EARLYLEVEL]:
for hf_type in [Mod.EARLYLEVEL]:
    mod.reg_hotfix(hf_type, 'Prologue_P',
            den_obj,
            'SpawnOptions',
            Mod.get_full_cond(spawner, 'SpawnOptionData'))

# Pick either of the next two

# This does need to be EARLYLEVEL
#mod.table_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
#        '/Game/Lootables/Eridian/Rock_Formation_Pile/_Design/Table_EridianCrystals',
#        'Zone',
#        'Small_7_3F0B239E4CEB2270736B28ABEF6D95EB',
#        9999999)

# These *do* need EARLYLEVEL but to *not* need notify
mod.reg_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
        den_obj,
        'NumActorsParam.AttributeInitializationData',
        '(BaseValueConstant=999999,BaseValueAttribute=None)')

mod.reg_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
        den_obj,
        'MaxAliveActorsWhenPassive.AttributeInitializationData.BaseValueConstant',
        999999)

mod.reg_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
        den_obj,
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueConstant',
        999999)

mod.close()

