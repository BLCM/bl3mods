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

from bl3hotfixmod.bl3hotfixmod import Mod, BVC

for label, scale, extra in [
        ('BL1', 1.045, ' (approximately; BL1 scaling is a bit weird)'),
        ('BL2', 1.13, ''),
        ('TPS', 1.1, ''),
        ]:

    full_filename = 'alternate_scaling_{}.txt'.format(label.lower())
    mod = Mod(full_filename,
            'Alternate Scaling: {}'.format(label),
            'Apocalyptech',
            [
                "Updates the universal scaling constant from BL3's default of 1.09 to match",
                "{}'s {}{}".format(label, scale, extra),
                "",
                "(NOTE: This is confirmed to affect gun damage, at least, but I have yet to",
                "test if it actually affects other stuff like enemies.)",
            ],
            lic=Mod.CC_BY_SA_40,
            )

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/Balance/HealthAndDamage/Att_UniversalBalanceScaler.Att_UniversalBalanceScaler:BP_ConstantValueResolver_C_0',
            'Value',
            BVC(bvc=scale))

    mod.close()
    print('Generated {}'.format(full_filename))
