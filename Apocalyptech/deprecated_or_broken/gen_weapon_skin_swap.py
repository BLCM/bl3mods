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

mod = Mod('weapon_skin_swap.txt',
        'Weapon Skin Swap',
        'Apocalyptech',
        [
            "Proof of concept - makes the Ghoul Metal Grey skin actually provide the",
            "Superstreamer skin, when applied to a Tediore shotgun.  Doesn't affect any",
            "other manufacturer/weapontype combination, though, since skins are particular",
            "like that.",
            "",
            "Mostly just wanted to see if it could be done; no plans to convert this",
            "into a Real Mod.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01',
        'Manufacturers.Manufacturers[4].WeaponTypes.WeaponTypes[2].Materials.Materials[0].Material',
        Mod.get_full_cond('/Game/PatchDLC/EventVDay/Gear/Weapon/Skins/MI_SG_TED_TwitchPrime'))

mod.close()
