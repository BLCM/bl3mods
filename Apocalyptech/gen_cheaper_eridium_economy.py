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

mod = Mod('cheaper_eridium_economy.txt',
        'Cheaper Eridium Economy',
        [
            "Makes various aspects of the Eridium economy cheaper, which basically",
            "ends up breaking that whole economy given the scaling I've done here.",
            "",
            "Currently the affected areas are Earl's Customizations, and the Eridium",
            "slot machine.  Earl's Vault Veteran vending machine is untouched since",
            "I haven't yet figured out how to alter it.",
        ])

for label, row in [
        ('Trinkets', 'WeaponTrinket'),
        ('Weapon Skins', 'WeaponSkin'),
        ('Player Skins', 'PlayerSkin'),
        ('Player Heads', 'PlayerHead'),
        ('Emotes', 'PlayerEmote'),
        ('ECHO Skins', 'EchoSkin'),
        ('Room Decorations', 'RoomDecoration'),
        ]:
    mod.comment("Customization costs @ Earl's - {}".format(label))
    for col, new_value in [
            ('Common_2_01EACCE6461DA50C78B6068E8E1DB06E', 5),
            ('Uncommon_6_4FA7EB5D47E5DFC7534F7EB00CE20B93', 10),
            ('Rare_7_788B345F42F2ADF256A30DA0E9393428', 15),
            ('VeryRare_12_6B38338344254EA079EDBEBAB1E101D8', 20),
            ('Legendary_13_A5DA691D4B91DAD99EF799B758314307', 25),
            ]:
        mod.table_hotfix(Mod.PATCH, '',
                '/Game/GameData/Economy/Customizations/Table_CrazyEarlCustomizationCost',
                row,
                col,
                new_value)
    mod.newline()

# Original Week 3 event scaled this to 50%; I'm using 20%.
mod.comment('Eridium slot machine costs')
mod.reg_hotfix(Mod.LEVEL, 'Sanctuary3_P',
        '/Game/UI/InteractionPrompt/UIData_PlaySlotsEridium',
        'Cost.BaseValueScale',
        0.2)
mod.newline()

mod.close()
