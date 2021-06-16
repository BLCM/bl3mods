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

import os
import sys
sys.path.append('../../../python_mod_helpers')
sys.path.append('../../dataprocessing/map_objects')
from mapobjlib.mapobjlib import MapObjects
from bl3hotfixmod.bl3hotfixmod import Mod, LVL_TO_ENG_LOWER

# As with my Red Chest Timer Reset mod, it seems like we should be able to use
# some `Default__*` type objects to set these params on a per-class basis,
# rather than having to touch each map object specifically, but I wasn't able
# to find a way to do that.

# Map Objects
mo = MapObjects()

# Mod header
mod = Mod('reopenable_gear_chests.bl3hotfix',
        'Reopenable Gear Chests',
        'Apocalyptech',
        [
            "Prevents red and white chests throughout the game from remembering their",
            "opened state between level loads, so they can be re-openable without",
            "having to go out to the main menu (or waiting for the timers to elapse).",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='chests',
        )

# Here we go!
for label, object_class in [
        # White Chests
        ('Cartels White Chests', 'BPIO_Lootable_Jakobs_WhiteChest_Cartels'),
        ('Cultist White Chests', 'BPIO_Hib_Lootable_Cultist_WhiteChest'), # Hibiscus
        # This container doesn't seem to "take" our hotfixes -- values remain unchanged -- but,
        # they seem to automatically reactivate anyway, so it doesn't appear necessary. 
        #('Eridian Crystal-Encrusted White Chests', 'BPIO_Lootable_Eridian_WhiteChestCrystal'),
        ('Eridian White Chests', 'BPIO_Lootable_Eridian_WhiteChest'),
        ('Frostbiters White Chests', 'BPIO_Hib_Lootable_FrostBiters_WhiteChest'), # Hibiscus
        ('Jakobs White Chests', 'BPIO_Lootable_Jakobs_WhiteChest'),
        ('Maliwan White Chests', 'BPIO_Lootable_Maliwan_WhiteChest'),
        ('Standard White Chests', 'BPIO_Lootable_Global_WhiteCrate'),

        # Red Chests
        ('Alisma Hyperion Red Chests', 'BPIO_Ali_Lootable_Hyperion_RedChest'), # Alisma
        ('Atlas Red Chests', 'BPIO_Lootable_Atlas_RedChest'),
        ('CoV Red Chests', 'BPIO_Lootable_COV_RedCrate'),
        ('Cultist Red Chests', 'BPIO_Hib_Lootable_Cultist_RedChest'), # Hibiscus
        ('Eridian Red Chests', 'BPIO_Lootable_Eridian_RedChest'),
        ('Frostbiters Red Chests', 'BPIO_Hib_Lootable_FrostBiters_RedChest'), # Hibiscus
        ('Hyperion Red Chests', 'BPIO_Lootable_Hyperion_RedChest'), # Dandelion
        ('Jakobs Red Chests', 'BPIO_Lootable_Jakobs_RedChest'),
        ('Maliwan Red Chests', 'BPIO_Lootable_Maliwan_RedChest'),
        ('Portal Red Chests', 'BPIO_Hib_Lootable_PortalChest'), # Hibiscus
        ]:

    object_class = f'{object_class}_C'
    print(f'Processing {object_class}...')
    mod.header(f'{label} ({object_class})')

    cur_level = None
    for level, object_path in mo.get_by_type(object_class):

        # Mini-header if we're processing a new level
        if level != cur_level:
            if cur_level is not None:
                mod.newline()
            mod.comment(LVL_TO_ENG_LOWER[level.lower()])
            cur_level = level

        # Hotfixes
        # Turns out this boolean is more for remembering which items are attached
        # to the container; to get the reopening behavior we need the ResetDelay
        # stuff, instead.
        #mod.reg_hotfix(Mod.LEVEL, cur_level,
        #        object_path,
        #        'bMaintainStateAcrossMapLoads',
        #        'False')
        mod.reg_hotfix(Mod.LEVEL, cur_level,
                object_path,
                'PersistenceData.ResetDelay',
                0)

    mod.newline()

mod.close()
