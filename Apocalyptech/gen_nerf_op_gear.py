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

# Purposefully not included in here:
#  - D.N.A. - Apparently generally considered not great, didn't even look at it.
#  - Iceburger - Ditto
#  - Multi-Tap - Base damage didn't seem out of whack, could be that its effects
#                make the on-card damage misleading, though.
#  - Pricker - If anything, needs a buff (not legendary, though, so unsurprising)
#  - Needle Gun - On the card, it's outclassed damagewise in the first place.
#                 Could be that the effects make up for it, but leaving for now.

mod = Mod('nerf_op_gear.txt',
        'Nerf OP Gear',
        'Apocalyptech',
        [
            "Nerfs some of the more egregiously-OP gear to be merely best-in-class.",
            "This is mostly meant to address weapons clearly intended for use in",
            "Mayhem 10, introduced by the Cartels/Mayhem 2.0 update, but also includes",
            "some other weapons such as the Krakatoa and Anarchy, etc.  This is",
            "intended for folks like myself who mostly disable Mayhem scaling, and",
            "don't want some guns absurdly outshining the rest.",
            "",
            "This only really addresses the 'base' damage scaling, and doesn't take",
            "any weapon behavior into consideration.",
            "",
            "This hasn't really seen any 'real' playtesting.  I've mostly just spawned",
            "a bunch of gear and fiddled with the numbers until the gear seems merely",
            "great instead of way OP.  Could be that I've gone too far (or not far enough)",
            "in some cases.  Launchers especially I don't really have a great feel for.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

readme_reports = []

# First up, one which doesn't fit the main pattern here.  Wedding Invitation's
# base damage isn't spectacular, but it's got a lot else going on.  Gonna try
# just nerfing the ricochet damage, which appears to be like 3x by default.
mod.header('Broken Hearts')
mod.comment('Wedding Invitation Ricochet Damage (default: 2.928)')
readme_reports.append('Wedding Invitation Ricochet Damage: `{}` -> `{}`'.format(2.928, 1))
mod.table_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/EventVDay/Gear/Weapon/DataTable_WeaponBalance_EventVDay',
        'WeddingInvitation',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        1)
mod.newline()

for cat_name, balance_obj, weapons in [
        ('Base Game Maliwan Snipers', '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_MAL', [
            # 4.25 is actually what GBX sets in a hotfix; the on-disk default is 1
            # At 2.5, a Storm's card can out-damage this, but I think it's probaby
            # acceptable.  Will have to see if it's all right while playing.
            ('Krakatoa', 'SR_Krakatoa', 4.25, 2.5),
            ]),
        ('DLC2 (Guns, Love, and Tentacles)', '/Game/PatchDLC/Hibiscus/Gear/Weapon/DataTable_WeaponBalance_Hibiscus', [
            # I almost feel like this could be nerfed even harder, but eh...
            ('Skullmasher', 'SR_Skullmasher', 0.5, 0.3),
            # This drops the base damage in half, but the gun gets something
            # like 1370% damage output at full stacks, so this'll honestly not
            # make much difference, and I'd sort of rather not drop the damage
            # any further.
            ('Anarchy', 'SG_Anarchy', 1, 0.4),
            ]),
        ('Cartels', '/Game/PatchDLC/Event2/Gear/Weapon/DataTable_WeaponBalance_Event2', [
            ('O.P.Q. System', 'OPQS', 1.8, 1),
            ('NoPewPew', 'PewPew', 1.1, 0.15),
            # TODO: GBX nerfed this officially, though by different means.  Should re-test Yellowcake.
            ('Yellowcake', 'YellowCake', 1.75, 1),
            ]),
        ('Mayhem 2.0', '/Game/PatchDLC/Mayhem2/Gear/Weapon/DataTable_WeaponBalance_Mayhem2', [
            ('The Monarch', 'AR_TheMonarch', 1.6, 0.7),
            ('Plaguebearer', 'HW_Plague', 1.1, 0.9),
            ('Backburner', 'HW_Backburner', 2, 1.7),
            # TODO: GBX nerfed Kaoson from 2.25 to 1.6, but also buffed most other legendary SMGs.
            # Should re-test all the SMGs in here to see how they fare now.
            ('Kaoson', 'Kaoson', 1.6, 1),
            ('Sand Hawk', 'SR_SandHawk', 1.5, 0.5),
            ('Reflux', 'SG_Reflux', 1.75, 1.5),
            ]),
        ]:
    mod.header(cat_name)
    for weap_label, row, default_scale, new_scale in sorted(weapons):
        mod.comment('{} (default: {})'.format(weap_label, default_scale))
        mod.table_hotfix(Mod.PATCH, '',
                balance_obj,
                row,
                'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
                new_scale)
        mod.newline()
        readme_reports.append('{}: `{}` -> `{}`'.format(weap_label, default_scale, new_scale))

mod.close()

print('Info for pasting into README:')
print('')
for line in sorted(readme_reports):
    print('  - {}'.format(line))
print('')
