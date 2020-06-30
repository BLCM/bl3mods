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

mod = Mod('better_slots.txt',
        'Improved Slot Machine Chances',
        'Apocalyptech',
        [
            'Improved results for all slot machines -- will always get a reward, and',
            "never any loaded grenades.  Customizations won't drop too often, since",
            'they just just the same pools as the global customization drops.',
        ],
        lic=Mod.CC_BY_SA_40,
        )

weight_attr = 'Weight_2_352BDC9A4B7443F6DB3D9FA890CF4B0E'
for (label, obj_name, maps, results) in [
        ('Cash Trap!',
            '/Game/InteractiveObjects/SlotMachine/_Shared/_Design/Table_SlotMachinePrizes_ClapTrap.Table_SlotMachinePrizes_ClapTrap',
            [
                ('Sanctuary', 'Sanctuary3_P'),
                ('Atlas HQ', 'AtlasHQ_P'),
                ('Skywell-27', 'OrbitalPlatform_P'),
                ('The Lodge', 'Bar_P'),
            ],
            [
                ('Lose',               0),   # default: 25
                ('BOOM!',              0),   # default: 10
                ('ClassMod_Common',    0),   # default: 20
                ('ClassMod_Uncommon',  3),   # default: 13
                ('ClassMod_Rare',      9),   # default: 5
                ('ClassMod_VeryRare',  5),   # default: 2
                ('ClassMod_Legendary', 2),   # default: 0.5
                ('PlayerSkin',         5),   # default: 0.5
                ('RoomDecoration',     0.5), # default: 3
                ('PlayerHead',         0.5), # default: 5
                ('Eridium',            3),   # default: 1
                ('Cash',               3),   # default: 2
            ]),
        ("Tink's Hijinx",
            '/Game/InteractiveObjects/SlotMachine/_Shared/_Design/Table_SlotMachinePrizes_HiJinx.Table_SlotMachinePrizes_HiJinx',
            [
                ('Sanctuary', 'Sanctuary3_P'),
                ('Vestige', 'Town_P'),
            ],
            [
                ('Lose',                   0), # default: 25
                ('BOOM!',                  0), # default: 10
                ('ShieldOrGrenade_Common', 0), # default: 17.5
                ('Shield_Uncommon',        3), # default: 10
                ('Shield_Rare',            9), # default: 3
                ('Shield_VeryRare',        5), # default: 1.5
                ('Shield_Legendary',       2), # default: 0.25
                ('GrenadeMod_Uncommon',    3), # default: 10
                ('GrenadeMod_Rare',        9), # default: 3
                ('GrenadeMod_VeryRare',    5), # default: 1.5
                ('GrenadeMod_Legendary',   2), # default: 0.25
                ('Cash',                   3), # default: 3
            ]),
        ("Loot Boxer (and Moxxi's Heist machines)",
            '/Game/InteractiveObjects/SlotMachine/_Shared/_Design/Table_SlotMachinePrizes_LootBoxer.Table_SlotMachinePrizes_LootBoxer',
            [
                ('Sanctuary', 'Sanctuary3_P'),
                ('Jakobs Estate', 'Mansion_P'),
                ('Grand Opening', 'CasinoIntro_P'),
                ("Jack's Secret", 'Core_P'),
            ],
            [
                ('Lose',          0),   # default: 25
                ('BOOM!',         0),   # default: 10
                ('Gun_Common',    0),   # default: 20
                ('Gun_Uncommon',  3),   # default: 10
                ('Gun_Rare',      9),   # default: 3
                ('Gun_VeryRare',  5),   # default: 1.5
                ('Gun_Legendary', 2),   # default: 0.25
                ('WeaponSkin',    0.5), # default: 1
                ('WeaponTrinket', 0.5), # default: 3
                ('Eridium',       3),   # default: 1
                ('Cash',          3),   # default: 2
                ('Gun_ETech',     5),   # default: 0.25
            ]),
        ('Vault Line',
            '/Game/InteractiveObjects/SlotMachine/_Shared/_Design/Table_SlotMachinePrizes_VaultLine.Table_SlotMachinePrizes_VaultLine',
            [
                ('Sanctuary', 'Sanctuary3_P'),
                ('The Lodge', 'Bar_P'),
            ],
            [
                ('Lose',                 0), # default: 60
                ('Eridium',              5), # default: 18
                ('Gun_Rare',             4), # default: 4
                ('Gun_VeryRare',         9), # default: 2
                ('Gun_Legendary',        3), # default: 1
                ('Shield_Rare',          4), # default: 3
                ('Shield_VeryRare',      9), # default: 1.5
                ('Shield_Legendary',     3), # default: 0.5
                ('GrenadeMod_Rare',      4), # default: 3
                ('GrenadeMod_VeryRare',  9), # default: 1.5
                ('GrenadeMod_Legendary', 3), # default: 0.5
                ('Artifact',             9), # default: 5
            ]),
        ]:
    for (map_label, map_name) in maps:
        mod.comment('{} (in {})'.format(label, map_label))
        for (row_name, value) in results:
            mod.table_hotfix(Mod.LEVEL, map_name,
                    obj_name,
                    row_name,
                    weight_attr,
                    value)
        mod.newline()

mod.close()
