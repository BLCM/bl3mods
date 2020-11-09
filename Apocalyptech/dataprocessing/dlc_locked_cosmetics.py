#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bl3data.bl3data import BL3Data

# Given a bunch of customizations, find out which ones are actually locked by some DLC info

custs = [
        '/Game/PatchDLC/Ixora/Gear/Weapons/WeaponTrinkets/_Design/WeaponTrinket_GearUp',
        '/Game/PatchDLC/Ixora/Customizations/ECHOTheme/ECHOTheme_50',
        '/Game/PatchDLC/Ixora/Customizations/ECHOTheme/ECHOTheme_52',
        '/Game/PatchDLC/Ixora/Customizations/ECHOTheme/ECHOTheme_57a',
        '/Game/PatchDLC/Ixora/Customizations/ECHOTheme/ECHOTheme_58',
        '/Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin51/CustomSkin_Beastmaster_51',
        '/Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin51/CustomSkin_Gunner_51',
        '/Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin51/CustomSkin_Operative_51',
        '/Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin51/CustomSkin_Siren_51',
        '/Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin62/CustomSkin_Beastmaster_62',
        '/Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin62/CustomSkin_Gunner_62',
        '/Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin62/CustomSkin_Operative_62',
        '/Game/PatchDLC/Ixora/PlayerCharacters/_Customizations/PlayerSkins/Skin62/CustomSkin_Siren_62',
        '/Game/PatchDLC/Ixora/PlayerCharacters/Beastmaster/Heads/DA_BMHead39',
        '/Game/PatchDLC/Ixora/PlayerCharacters/Gunner/Heads/DA_GNRHead39',
        '/Game/PatchDLC/Ixora/PlayerCharacters/Operative/Heads/DA_OPHead39',
        '/Game/PatchDLC/Ixora/PlayerCharacters/SirenBrawler/Heads/DA_SRNHead39',
        ]

data = BL3Data()

for cust in custs:
    obj_data = data.get_data(cust)
    for export in obj_data:
        if 'DlcInventorySetData' in export:
            print('{}: {}'.format(cust, export['DlcInventorySetData'][0]))
            break

