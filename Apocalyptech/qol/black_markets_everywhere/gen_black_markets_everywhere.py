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
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('black_markets_everywhere.bl3hotfix',
        'Black Markets Everywhere',
        'Apocalyptech',
        [
            "Sets all potential Black Market vending machine spawns to be active, and",
            "removes their respawn timer (which ordinarily prevents it from respawning",
            "for 30 minutes after being used).  Maps which can contain the machines",
            "all have 2-3 spawn locations for the machine.",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='maps, vendor',
        )

# Blarg.
data = BL3Data()
spawnoption = '/Game/PatchDLC/Ixora2/InteractiveObjects/GameSystemMachines/VendingMachine/_Shared/SpawnOption_BlackMarketVendingMachine'

# First, remove the respawn timer for these.  Yes, we actually do need a Char-based hotfix
# here -- it seems that the object doesn't exist early enough for Level hotfixes (Early or
# otherwise), but Char gets it fast enough.  Go figure!  Perhaps these `Default__` values
# apply even after the objects are instantiated?
mod.header('Remove Black Market Machine Respawn Timer')
mod.comment('Yes, we *do* need a Char-based hotfix here.  It\'s a thing.')
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
        '/Game/PatchDLC/Ixora2/InteractiveObjects/GameSystemMachines/VendingMachine/_Shared/BP_VendingMachine_BlackMarket.Default__BP_VendingMachine_BlackMarket_C',
        'PostUseRespawnDelaySeconds',
        0)
mod.newline()

# Now find everywhere the machine can spawn and enable each spawnpoint.
for mapobj_name in sorted(data.get_refs_to(spawnoption)):

    # I don't know that this is generally true for *all* maps in the game, but it's
    # at least true for the base-game maps which show up in here, so Good Enough.
    map_name, map_eng_name = Mod.get_level_info('{}_P'.format(mapobj_name.split('/')[-2]))
    mod.header(map_eng_name)

    # Inspect our object to find all OakSpawners we want to edit.
    mapobj_data = data.get_data(mapobj_name)
    for export in mapobj_data:
        if export['export_type'] == 'OakSpawner':
            oakspawner_export_idx = export['SpawnerComponent']['export']
            oakspawner_export = mapobj_data[oakspawner_export_idx-1]
            spawnerstyle_idx = oakspawner_export['SpawnerStyle']['export']
            spawnerstyle = mapobj_data[spawnerstyle_idx-1]
            if spawnerstyle['SpawnOptions'][1] == spawnoption:
                last_bit = mapobj_name.split('/')[-1]
                mod.reg_hotfix(Mod.LEVEL, map_name,
                        '{}.{}:PersistentLevel.{}.SpawnerComponent'.format(
                            mapobj_name,
                            last_bit,
                            export['_jwp_object_name'],
                            ),
                        'bEnabled',
                        'True',
                        notify=True)

    mod.newline()

mod.close()
