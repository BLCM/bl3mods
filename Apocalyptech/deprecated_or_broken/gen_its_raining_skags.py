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
sys.path.append('../../python_mod_helpers')
sys.path.append('../dataprocessing/map_objects')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('its_raining_skags.txt',
        "It's Raining Skags!",
        'Apocalyptech',
        [
            "They seem to crap out at 'round 20 active at any given time.  I didn't",
            "spend a *lot* of time looking around to see if I could get them to just",
            "keep on raining, but I didn't see anything obvious that I wasn't",
            "already doing.",
            ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        )

data = BL3Data()

level = 'Prologue_P'
den_obj = '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.OakSpawner_EridiumCrystals.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den'
coords_from = (43460, 20822)
coords_to = (47673, 26232)
coord_z = 0

# Pull apart our Den object
submap_first, obj_after = den_obj.split(':PersistentLevel.')
submap_base, submap_short = submap_first.rsplit('.', 1)
spawner_short = obj_after.split('.')[0]

# Grab map data
mod.header(f'Processing {spawner_short} objects in {submap_short}')
obj = data.get_data(submap_base)
for export in obj:
    if export['_jwp_object_name'] == spawner_short:
        sc = obj[export['SpawnerComponent']['export']-1]
        objects = []
        for sp in sc['SpawnPoints']:
            objects.append('{}:PersistentLevel.{}'.format(
                submap_first,
                sp['_jwp_export_dst_name'],
                ))

        # Calculate our deltas
        per_side = math.floor(math.sqrt(len(objects)))
        delta_x = (coords_to[0]-coords_from[0])/per_side
        delta_y = (coords_to[1]-coords_from[1])/per_side
        cur_x = coords_from[0]
        cur_y = coords_from[1]

        mod.comment('Moving objects around')
        for idx, obj_name in enumerate(objects):
            if idx != 0:
                if idx % per_side == 0:
                    cur_x = coords_from[0]
                    cur_y += delta_y
                else:
                    cur_x += delta_x

            mod.reg_hotfix(Mod.LEVEL, level,
                    f'{obj_name}.SceneComp',
                    'RelativeLocation',
                    '(x={},y={},z={})'.format(
                        round(cur_x, 1),
                        round(cur_y, 1),
                        round(coord_z, 1),
                        ),
                    notify=True)

        mod.newline()

        mod.comment('Skag Time')
        mod.reg_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
                den_obj,
                'SpawnOptions',
                Mod.get_full_cond('/Game/Enemies/_Spawning/Skags/_Mixes/SpawnOptions_SkagFullMix', 'SpawnOptionData'))
        mod.newline()

        mod.comment('Turn Skags to 11')

        mod.reg_hotfix(Mod.EARLYLEVEL, level,
                den_obj,
                'bInfinite',
                'True')

        mod.reg_hotfix(Mod.EARLYLEVEL, level,
                den_obj,
                'NumActorsParam.AttributeInitializationData',
                '(BaseValueConstant={},BaseValueAttribute=None,BaseValueScale=1)'.format(999999))

        mod.reg_hotfix(Mod.EARLYLEVEL, level,
                den_obj,
                'MaxAliveActorsWhenPassive.AttributeInitializationData.BaseValueConstant',
                999999)

        mod.reg_hotfix(Mod.EARLYLEVEL, level,
                den_obj,
                'MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueConstant',
                999999)

        mod.newline()

        break

mod.close()

