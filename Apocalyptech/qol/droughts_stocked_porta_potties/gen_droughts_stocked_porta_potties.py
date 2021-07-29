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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('droughts_stocked_porta_potties.bl3hotfix',
        'Droughts Stocked Porta-Potties',
        'Apocalyptech',
        [
            "Various Porta-Potties throughout The Droughts ordinarily only provide",
            "ammo/money and the like, without any gear attachments.  This mod fixes",
            "them up so that they act like any other porta-potty in the game.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol, maps',
        ss=['https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/qol/droughts_stocked_porta_potties/screenshot.jpg'],
        )

lootdef = Mod.get_full_cond('/Game/Lootables/_Design/Data/Industrial/LootDef_Industrial_PortaPotty', 'LootableBalanceData')

for submap, index in [
        ('Dynamic', 61),
        ('Dynamic', 224),
        ('Dynamic', 740),
        ('Dynamic', 1044),
        ('Dynamic', 1844),
        ('Terrain', 0),
        ('Terrain', 61),
        ]:

    base_obj_name = f'/Game/Maps/Zone_0/Prologue/Prologue_{submap}.Prologue_{submap}:PersistentLevel.BPIO_Lootable_Industrial_PortaPotty_{index}'
    loot_obj_name = f'{base_obj_name}.Loot'

    mod.reg_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
            base_obj_name,
            'LootDefinition',
            lootdef)

    mod.reg_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
            loot_obj_name,
            'BalanceData',
            lootdef)

mod.close()
