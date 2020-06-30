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

mod = Mod('hatsoff_weapon.txt',
        'Hats Off Weapon',
        'Apocalyptech',
        [
            "Just a joke mod.  During the intro to Bounty of Blood, a character named",
            "Old Pete starts making another character dance by shooting at his feet.",
            "This changes his Jakobs gun into the Backburner, instead, for a laugh.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Had a heck of a time finding the attribute to use here
mod.reg_hotfix(Mod.CHAR, 'BPChar_Hatsoff',
        '/Geranium/NonPlayerCharacters/GerNPC/HatsOff/_Design/Character/BPChar_Hatsoff.Default__BPChar_Hatsoff_C',
        'DefaultBalanceWeaponData',
        Mod.get_full_cond('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner', 'InventoryBalanceData'))

mod.close()
