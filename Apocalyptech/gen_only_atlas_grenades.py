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

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF

mod = Mod('only_atlas_grenades.txt',
        'Only Atlas Grenades',
        'Apocalyptech',
        [
            "While doing a Zane runthrough, I only really wanted homing grenades,",
            "since I didn't have a lot of control over when exactly they were",
            "getting thrown out (or at least I didn't care enough to try and",
            "control for that).  So, I wanted only homing.  This does that!",
            "",
            "This does *not* affect legendary grenade drops, only the regular",
            "sort.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

for pool_name in [
        'ItemPool_GrenadeMods_01_Common',
        'ItemPool_GrenadeMods_02_Uncommon',
        'ItemPool_GrenadeMods_03_Rare',
        'ItemPool_GrenadeMods_04_VeryRare',
        ]:
    for idx in range(1, 6):
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/GameData/Loot/ItemPools/GrenadeMods/{}'.format(pool_name),
                'BalancedItems.BalancedItems[{}].Weight'.format(idx),
                BVCF(bvc=0))

mod.close()
