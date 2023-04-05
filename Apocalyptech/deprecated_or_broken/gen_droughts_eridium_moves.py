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
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('droughts_eridium_moves.txt',
        'Droughts Eridium Moves',
        'Apocalyptech',
        [
            "Mod which moves all small Eridium piles in The Droughts (and, now,",
            "Eschaton Row and Enoch's Grove) into a line near the Highway Fast",
            "Travel point (or for the others, near their only FT point).  Also",
            "Also alters the Dens so that they can all spawn at once, or at least",
            "have a nice solid line of them (the line in Enoch's Grove in",
            "particular isn't actually long enough to spawn all at the same time).",
            ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.1.0',
        cats='resource',
        )

data = BL3Data()
for level, den_obj, linestart, lineend, change_to in [
        ('Prologue_P',
            '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.OakSpawner_EridiumCrystals.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den',
            (49847, 28757, -3911),
            (44948, 23862, -3601),
            None,
            #'/Game/Lootables/Eridian/Rock_Formation_Pile/_Design/SpawnOption_EridianCrystal_Small',
            #'/Game/Lootables/_Design/Data/Industrial/SpawnOptions_CoV_CardboardBox',
            #'/Game/PatchDLC/Ixora/Lootables/_Design/Data/GearUp/SpawnOptions_VendingMachine_Weapons_GearUp',
            ),
        ('Noir_P',
            '/Ixora2/Maps/Noir/Noir_Combat.Noir_Combat:PersistentLevel.OakSpawner_EridiumCrystals.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den',
            (-15103, 5229, -875),
            (-15654, 9173, -875),
            None,
            ),
        ('Cabin_P',
            '/Ixora2/Maps/Cabin/Cabin_P.Cabin_P:PersistentLevel.OakSpawner_1.SpawnerComponent.SpawnerStyle_SpawnerStyle_Bunch',
            (9099, 20429, 29),
            (12109, 16399, 4),
            None,
            ),
        ]:

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
            delta_x = (lineend[0]-linestart[0])/(len(objects)-1)
            delta_y = (lineend[1]-linestart[1])/(len(objects)-1)
            delta_z = (lineend[2]-linestart[2])/(len(objects)-1)
            cur_x, cur_y, cur_z = linestart

            mod.comment('Moving objects around')

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

            if change_to is not None:
                # This one *must* be an Early-level hotfix.  Doesn't work otherwise.
                mod.comment('Updating spawner to {}'.format(change_to.split('/')[-1]))
                mod.reg_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
                        den_obj,
                        'SpawnOptions',
                        Mod.get_full_cond(change_to, 'SpawnOptionData'))
                mod.newline()

            mod.comment('Maxing spawn parameters')

            # Pick either of the next two

            # This does need to be EARLYLEVEL
            #mod.table_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
            #        '/Game/Lootables/Eridian/Rock_Formation_Pile/_Design/Table_EridianCrystals',
            #        'Zone',
            #        'Small_7_3F0B239E4CEB2270736B28ABEF6D95EB',
            #        9999999)

            # These *do* need EARLYLEVEL but to *not* need notify
            mod.reg_hotfix(Mod.EARLYLEVEL, level,
                    den_obj,
                    'NumActorsParam.AttributeInitializationData',
                    '(BaseValueConstant={},BaseValueAttribute=None,BaseValueScale=1)'.format(len(objects)))

            mod.reg_hotfix(Mod.EARLYLEVEL, level,
                    den_obj,
                    'MaxAliveActorsWhenPassive.AttributeInitializationData.BaseValueConstant',
                    len(objects))

            mod.reg_hotfix(Mod.EARLYLEVEL, level,
                    den_obj,
                    'MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueConstant',
                    len(objects))

            mod.newline()

            break

mod.close()

