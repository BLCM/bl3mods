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
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_63',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_63',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_63',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_63',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/_Shared/CustomSkin_Beastmaster_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/_Shared/CustomSkin_Gunner_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/_Shared/CustomSkin_Operative__DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/_Shared/CustomSkin_Siren__DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/_Shared/CustomHead_Beastmaster_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/_Shared/CustomHead_Gunner_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/_Shared/CustomHead_Operative_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/_Shared/CustomHead_Siren_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/RoomDeco/RoomDeco_DLC4_01_Orbs',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/RoomDeco/RoomDeco_DLC4_02_Trophy',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/RoomDeco/RoomDeco_DLC4_03_Axe',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/RoomDeco/RoomDeco_DLC4_04_Moon',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/RoomDeco/RoomDeco_DLC4_05_Mask',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Emotes/Beastmaster/CustomEmote_Beastmaster_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Emotes/Beastmaster/CustomEmote_Beastmaster_DLC4_02',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Emotes/Gunner/CustomEmote_Gunner_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Emotes/Gunner/CustomEmote_Gunner_DLC4_02',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Emotes/Operative/CustomEmote_Operative_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Emotes/Operative/CustomEmote_Operative_DLC4_02',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Emotes/SirenBrawler/CustomEmote_Siren_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Emotes/SirenBrawler/CustomEmote_Siren_DLC4_02',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_79',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_DLC4_01',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_DLC4_02',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_DLC4_03',
        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_DLC4_04',
        '/Game/PatchDLC/Alisma/Gear/WeaponTrinkets/Trinket_DLC4_Trinket_01',
        '/Game/PatchDLC/Alisma/Gear/WeaponTrinkets/Trinket_DLC4_Trinket_02',
        ]

data = BL3Data()

for cust in custs:
    obj_data = data.get_data(cust)
    for export in obj_data:
        if 'DlcInventorySetData' in export:
            print('{}: {}'.format(cust, export['DlcInventorySetData'][0]))
            break

