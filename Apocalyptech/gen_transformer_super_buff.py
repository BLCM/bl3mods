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

mod = Mod('transformer_super_buff.txt',
        "Super buff for The Transformer.  Cheating!",
        [
            "Vastly buffs The Transformer, making you basically invulnerable",
            "when wearing it.",
            "",
            "Used by myself primarily just for mod testing purposes, for when I",
            "don't want to be bothered by actual combat.",
        ])

attr_effects = []
for (attr, mod_type, mod_val) in [

        # Stock values
        ('/Game/Gear/Shields/_Design/Naming/Att_Shield_IgnoreManufacturerName', 'OverrideBaseValue', 1),
        ('/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_ElementalResistance', 'OverrideBaseValue', 1.25),

        # Our buffs
        ('/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_Capacity', 'ScaleSimple', 10000),
        ('/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_RegenDelay', 'ScaleSimple', 0.0001),
        ('/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_RegenRate', 'ScaleSimple', 100000),

        ]:

    last_part = attr.split('/')[-1]
    full_attr = '{}.{}'.format(attr, last_part)
    
    attr_effects.append(f"""(
        AttributeToModify=GbxAttributeData'"{full_attr}"',
        ModifierType={mod_type},
        ModifierValue=(BaseValueConstant={mod_val})
    )""")

# Apply all our custom effects
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Gear/Shields/_Design/_Uniques/Transformer/Parts/Shield_Part_Aug_HYP_LGD_Transformer',
        'InventoryAttributeEffects',
        '({})'.format(','.join(attr_effects)),
        )

mod.close()
