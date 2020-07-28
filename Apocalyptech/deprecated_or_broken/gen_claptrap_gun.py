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

mod = Mod('claptrap_gun.txt',
        'Claptrap Gun',
        'Apocalyptech',
        [
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Enemy BPChars (like /Game/Enemies/Enforcer/Gun/_Design/Character/BPChar_EnforcerGun) will
# initially be non-hostile, but will turn against you once the spider-mind explosion happens.
# They won't be able to actually harm you, though.  (They *can* be damaged before the
# explosion, but that won't shift their allegiance.)

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Parts/Part_SM_TED_Barrel_SpiderMind.Part_SM_TED_Barrel_SpiderMind:TedioreWeaponAspectData_0.TedioreBehavior_TedioreBehavior_Sticky',
        'StuckAICharacter',
        Mod.get_full_cond('/Game/NonPlayerCharacters/Claptrap/_Design/Character/BpChar_Claptrap', 'BlueprintGeneratedClass'))

mod.close()
