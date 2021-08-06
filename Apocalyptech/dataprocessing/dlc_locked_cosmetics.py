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
        '/Game/PatchDLC/Event2/Gear/_Design/WeaponSkins/WeaponSkin_Event2_2',
        '/Game/PatchDLC/Event2/Gear/_Design/WeaponTrinkets/WeaponTrinket_Cartels_2021',
        '/Game/PatchDLC/Event2/Pickups/RoomDecoration/RoomDecoration_Event2_2',
        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_48',
        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_40',
        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_48',
        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_48',
        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_48',
        '/Game/PatchDLC/Ixora2/BodyMeshCustomization/Skins/CustomSkin_Beastmaster_54',
        '/Game/PatchDLC/Ixora2/BodyMeshCustomization/Skins/CustomSkin_Gunner_54',
        '/Game/PatchDLC/Ixora2/BodyMeshCustomization/Skins/CustomSkin_Operative_54',
        '/Game/PatchDLC/Ixora2/BodyMeshCustomization/Skins/CustomSkin_Siren_54',
        '/Game/PatchDLC/Ixora2/PlayerCharacters/_Shared/Skins/CustomSkin_Beastmaster_66',
        '/Game/PatchDLC/Ixora2/PlayerCharacters/_Shared/Skins/CustomSkin_Gunner_66',
        '/Game/PatchDLC/Ixora2/PlayerCharacters/_Shared/Skins/CustomSkin_Operative_66',
        '/Game/PatchDLC/Ixora2/PlayerCharacters/_Shared/Skins/CustomSkin_Siren_66',
        '/Game/PatchDLC/Ixora2/PlayerCharacters/Beastmaster/Heads/DA_BMHead45',
        '/Game/PatchDLC/Ixora2/PlayerCharacters/Gunner/Heads/DA_GNRHead45',
        '/Game/PatchDLC/Ixora2/PlayerCharacters/Operative/Heads/DA_OPHead45',
        '/Game/PatchDLC/Ixora2/PlayerCharacters/SirenBrawler/Heads/DA_SRNHead45',
        '/Game/PatchDLC/VaultCard/Customizations/EchoDevice/ECHOTheme_VC1_1',
        '/Game/PatchDLC/VaultCard/Customizations/EchoDevice/ECHOTheme_VC1_2',
        '/Game/PatchDLC/VaultCard/Customizations/EchoDevice/ECHOTheme_VC1_3',
        '/Game/PatchDLC/VaultCard/Customizations/EchoDevice/ECHOTheme_VC1_4',
        '/Game/PatchDLC/VaultCard/Customizations/Emotes/Beastmaster/CustomEmote_Beastmaster_VC1_1',
        '/Game/PatchDLC/VaultCard/Customizations/Emotes/Beastmaster/CustomEmote_Beastmaster_VC1_2',
        '/Game/PatchDLC/VaultCard/Customizations/Emotes/Gunner/CustomEmote_Gunner_VC1_1',
        '/Game/PatchDLC/VaultCard/Customizations/Emotes/Gunner/CustomEmote_Gunner_VC1_2',
        '/Game/PatchDLC/VaultCard/Customizations/Emotes/Operative/CustomEmote_Operative_VC1_1',
        '/Game/PatchDLC/VaultCard/Customizations/Emotes/Operative/CustomEmote_Operative_VC1_2',
        '/Game/PatchDLC/VaultCard/Customizations/Emotes/SirenBrawler/CustomEmote_Siren_VC1_1',
        '/Game/PatchDLC/VaultCard/Customizations/Emotes/SirenBrawler/CustomEmote_Siren_VC1_2',
        '/Game/PatchDLC/VaultCard/Customizations/RoomDeco/RoomDecoration_VC1_1',
        '/Game/PatchDLC/VaultCard/Customizations/RoomDeco/RoomDecoration_VC1_2',
        '/Game/PatchDLC/VaultCard/Customizations/RoomDeco/RoomDecoration_VC1_3',
        '/Game/PatchDLC/VaultCard/Customizations/WeaponSkin/WeaponSkin_VC1_1',
        '/Game/PatchDLC/VaultCard/Customizations/WeaponSkin/WeaponSkin_VC1_2',
        '/Game/PatchDLC/VaultCard/Customizations/WeaponSkin/WeaponSkin_VC1_3',
        '/Game/PatchDLC/VaultCard/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC1_1',
        '/Game/PatchDLC/VaultCard/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC1_2',
        '/Game/PatchDLC/VaultCard/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC1_3',
        '/Game/PatchDLC/VaultCard/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC1_4',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomHeads/CustomHead47/CustomHead_Beastmaster_47',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomHeads/CustomHead47/CustomHead_Gunner_47',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomHeads/CustomHead47/CustomHead_Operative_47',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomHeads/CustomHead47/CustomHead_Siren_47',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Beastmaster_67',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Beastmaster_68',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Beastmaster_69',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Beastmaster_70',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Gunner_67',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Gunner_68',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Gunner_69',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Gunner_70',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Operative_67',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Operative_68',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Operative_69',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Operative_70',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Siren_67',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Siren_68',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Siren_69',
        '/Game/PatchDLC/VaultCard/PlayerCharacters/_Shared/CustomSkin_Siren_70',
        '/Game/PatchDLC/VaultCard2/Customizations/EchoDevice/ECHOTheme_VC2_1',
        '/Game/PatchDLC/VaultCard2/Customizations/EchoDevice/ECHOTheme_VC2_2',
        '/Game/PatchDLC/VaultCard2/Customizations/EchoDevice/ECHOTheme_VC2_3',
        '/Game/PatchDLC/VaultCard2/Customizations/EchoDevice/ECHOTheme_VC2_4',
        '/Game/PatchDLC/VaultCard2/Customizations/EchoDevice/ECHOTheme_VC2_5',
        '/Game/PatchDLC/VaultCard2/Customizations/Emotes/Beastmaster/CustomEmote_Beastmaster_VC2_1',
        '/Game/PatchDLC/VaultCard2/Customizations/Emotes/Beastmaster/CustomEmote_Beastmaster_VC2_2',
        '/Game/PatchDLC/VaultCard2/Customizations/Emotes/Gunner/CustomEmote_Gunner_VC2_1',
        '/Game/PatchDLC/VaultCard2/Customizations/Emotes/Gunner/CustomEmote_Gunner_VC2_2',
        '/Game/PatchDLC/VaultCard2/Customizations/Emotes/Operative/CustomEmote_Operative_VC2_1',
        '/Game/PatchDLC/VaultCard2/Customizations/Emotes/Operative/CustomEmote_Operative_VC2_2',
        '/Game/PatchDLC/VaultCard2/Customizations/Emotes/Siren/CustomEmote_Siren_VC2_1',
        '/Game/PatchDLC/VaultCard2/Customizations/Emotes/Siren/CustomEmote_Siren_VC2_2',
        '/Game/PatchDLC/VaultCard2/Customizations/RoomDeco/RoomDecoration_VC2_1',
        '/Game/PatchDLC/VaultCard2/Customizations/RoomDeco/RoomDecoration_VC2_2',
        '/Game/PatchDLC/VaultCard2/Gear/_Design/WeaponSkins/WeaponSkin_VC2_1',
        '/Game/PatchDLC/VaultCard2/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC2_1',
        '/Game/PatchDLC/VaultCard2/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC2_2',
        '/Game/PatchDLC/VaultCard2/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC2_3',
        '/Game/PatchDLC/VaultCard2/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC2_4',
        '/Game/PatchDLC/VaultCard2/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC2_5',
        '/Game/PatchDLC/VaultCard2/Gear/WeaponTrinkets/_Design/WeaponTrinket_VC2_6',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Beastmaster_75',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Beastmaster_76',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Beastmaster_77',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Beastmaster_78',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Gunner_75',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Gunner_76',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Gunner_77',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Gunner_78',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Operative_75',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Operative_76',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Operative_77',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Operative_78',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Siren_75',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Siren_76',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Siren_77',
        '/Game/PatchDLC/VaultCard2/PlayerCharacters/_Shared/CustomSkin_Siren_78',
        ]

data = BL3Data()

for cust in custs:
    obj_data = data.get_data(cust)
    for export in obj_data:
        if 'DlcInventorySetData' in export:
            print('{}: {}'.format(cust, export['DlcInventorySetData'][0]))
            break

