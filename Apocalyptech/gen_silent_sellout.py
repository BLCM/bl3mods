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

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('silent_sellout.txt',
        'Silent Sellout',
        'Apocalyptech',
        [
            "Removes the Tyreen-themed voice module from the Sellout",
        ],
        lic=Mod.CC_BY_SA_40,
        )
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/WeaponCustom/BPWeap_PS_MAL_SuckerPunch.BPWeap_PS_MAL_SuckerPunch_C:OakDialog_GEN_VARIABLE',
        'DialogScripts',
        '()')

mod.close()
