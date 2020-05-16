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

mod = Mod('cdh.txt',
        'Cold Dead Hands!',
        [
            'Not really, but wanted to test out if bDropOnDeath still exists',
            ],
        )

for char in [
        'BPChar_PunkBasic',
        'BPChar_PunkBadass',
        'BPChar_PunkSniper',
        'BPChar_PunkShared',
        'BPChar_PunkAssaulter',
        'BPChar_PunkAnointed',
        'BPChar_Tink',
        ]:
    for pool in [
            'ItemPool_CoVEnemyUse_AssaultRifles',
            'ItemPool_COVEnemyUse_HeavyWeapons',
            'ItemPool_CoVEnemyUse_Pistols',
            'ItemPool_CoVEnemyUse_Shotguns',
            'ItemPool_CoVEnemyUse_SMGs',
            'ItemPool_CoVEnemyUse_SniperRifles',
            ]:
        for num in range(10):
            mod.reg_hotfix(Mod.CHAR, char,
                    '/Game/Enemies/_Shared/_Design/ItemPools/{}.{}'.format(pool, pool),
                    'BalancedItems[{}].bDropOnDeath'.format(num),
                    'True')

    mod.newline()

mod.close()
