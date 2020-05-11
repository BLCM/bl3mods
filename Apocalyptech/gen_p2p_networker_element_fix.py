#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import collections
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, Balance

mod = Mod('p2p_networker_element_fix.txt',
        'P2P Networker Element Fix',
        [
            "P2P Networker is an unfinished/unreleased gun that's still present in the",
            "BL3 data.  It's basically a more-powerful redistributor.  One thing broken",
            "about it is that it only has a primary element, but will still let you",
            "'switch' elements, which results in a message like 'GUN TEAM FIX NAME PLZ'",
            "in the game's UI.  Amusing as that is, this mod will add in a secondary",
            "element to the gun, so that it can be switched properly just like any other",
            "Maliwan weapon.",
        ])

# Some assumptions we can make, since we're just dealing with the one balance:
#  1) The "secondary element" part group is the only empty group in the list.
#  2) The weights of the elements should all just be 1 (since that's what the Primary element uses)

p2p_bal_name = '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link'
extra_elements = [
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_01_Fire',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_02_Cryo',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_03_Shock',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_04_Radiation',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_05_Corrosive',
        ]

# Add the parts
data = BL3Data()
p2p_bal = Balance.from_data(data, p2p_bal_name)
for cat in p2p_bal.categories:
    if len(cat) == 0:
        cat.enabled = True
        for element in extra_elements:
            cat.add_part_name(element, 1)
        break
p2p_bal.hotfix_full(mod)

mod.close()
