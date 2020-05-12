#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('stronger_snipers.txt',
        'Stronger Snipers',
        [
            "This buffs up sniper rifles by a bit, with a bit of base-damage increase, and",
            "some crit bonus damage as well (which is expanded even more for Jakobs snipers).",
            "This may need some tweaking after more playtesting.",
            "",
            "At current values, the blue Jakobs sniper I was testing with was affected like so:",
            "",
            "   On-Card Damage: 4159 -> 4852",
            "   Non-Crit on Dummy: 4770 -> 5566",
            "   Crit on Dummy: 12k -> 18k",
        ])

# All Sniper Manufacturers
mod.comment('All Sniper Rifles')
for col, value in [
        # Default: 1.2
        ('CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C', 1.4),
        # Default: 1.8
        ('DamageScale_36_150C89A04BB4FCF0061CAC86E39E1A39', 2.1),
        ]:
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Base_Data',
            'SniperRifle',
            col,
            value)
mod.newline()

# Specific Jakobs buffs
mod.comment('Jakobs-Specific Buffs')
for row, col, value in [
        # Default values here: 1
        ('JAK_Barrel_01', 'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C', 1.1),
        ('JAK_Barrel_02', 'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C', 1.1),
        ('JAK_Barrel_03', 'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C', 1.1),
        ]:
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/DataTable_Weapon_SR_Barrel_Init',
            row,
            col,
            value)
mod.newline()

mod.close()
