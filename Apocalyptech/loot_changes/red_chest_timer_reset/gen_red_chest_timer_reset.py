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

# Map Objects
mo = MapObjects()

# Mod header
mod = Mod('red_chest_timer_reset.bl3hotfix',
        'Red Chest Timer Reset',
        'Apocalyptech',
        [
            "Prevents the game's red chests from remembering their opened state when",
            "quitting and restarting the game.  They will still have their usual timers",
            "while staying within the same game session, but a trip to the main menu",
            "will now let them be re-opened right away.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='chests',
        )

# Here we go!
for label, object_class in [
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
        mod.reg_hotfix(Mod.LEVEL, cur_level,
                object_path,
                'PersistenceData.bStoreInSaveGame',
                'False')

    mod.newline()

if False:
    # I could not for the life of me find a way to use the "base" object attributes
    # here to alter the in-game objects.  Could be it's just not possible, but of
    # course there could just as well be something I'm missing.  Anyway, this little
    # stanza represents what I'd tried, anyway.  It's my failures here which led to
    # the map_object weirdness above, in the end.  :D
    for chest_name in [
            '/Game/Lootables/_Design/Classes/CoV/BPIO_Lootable_COV_RedCrate',
            ]:

        last_bit = chest_name.split('/')[-1]
        for full_name in [
                # Really this is the one that should work
                '{}.Default__{}_C'.format(chest_name, last_bit),
                # These two are longshots for sure; would've been pretty surprised if they'd worked
                '{}.{}_C'.format(chest_name, last_bit),
                '{}_C.Default__{}_C'.format(chest_name, last_bit),
                ]:

            for method in [
                    Mod.LEVEL,
                    Mod.EARLYLEVEL,
                    ]:

                for notify in [
                        True,
                        False,
                        ]:

                    mod.reg_hotfix(method, 'MatchAll',
                            full_name,
                            'PersistenceData.bStoreInSaveGame',
                            'False',
                            notify=notify)

mod.close()
