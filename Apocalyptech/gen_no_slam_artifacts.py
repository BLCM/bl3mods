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

mod = Mod('no_slam_artifacts.txt',
        'No Slam-based Artifacts',
        [
            'Makes non-legendary/unique artifacts never have slam effects.',
            "Doesn't touch legendary/unique artifacts at all, so those can",
            'still spawn.',
        ])

def clear_part(mod, obj_name, part_idx):
    mod.reg_hotfix(Mod.PATCH, '',
            obj_name,
            'RuntimePartList.AllParts[{}].Weight'.format(part_idx),
            """
            (
                BaseValueConstant=0,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1
            )""")

# Loop!  Turns out the indexes are the same for each of these, but eh.
for (label, bal_name, indexes) in [
        ('Common', 'InvBalD_Artifact_01_Common', [
            1,  # Rear Ender
            6,  # Ice Spiker
            12, # Hot Drop
            13, # Mind Melt
            14, # Spark Plug
            15, # Toxic Revenger
            ]),
        ('Uncommon', 'InvBalD_Artifact_02_Uncommon', [
            1,  # Rear Ender
            6,  # Ice Spiker
            12, # Hot Drop
            13, # Mind Melt
            14, # Spark Plug
            15, # Toxic Revenger
            ]),
        ('Rare', 'InvBalD_Artifact_03_Rare', [
            1,  # Rear Ender
            6,  # Ice Spiker
            12, # Hot Drop
            13, # Mind Melt
            14, # Spark Plug
            15, # Toxic Revenger
            ]),
        ('VeryRare', 'InvBalD_Artifact_04_VeryRare', [
            1,  # Rear Ender
            6,  # Ice Spiker
            12, # Hot Drop
            13, # Mind Melt
            14, # Spark Plug
            15, # Toxic Revenger
            ]),
        ]:
    obj_name = '/Game/Gear/Artifacts/_Design/BalanceDefs/{}.{}'.format(bal_name, bal_name)
    mod.comment('{} Artifacts'.format(label))
    for index in indexes:
        clear_part(mod, obj_name, index)
    mod.newline()

mod.close()
