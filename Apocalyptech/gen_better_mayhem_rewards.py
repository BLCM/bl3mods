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

mod = Mod('better_mayhem_rewards.txt',
        'Better Mayhem Rewards',
        [
            "Increases the XP gains you get in the various Mayhem modes, and increases",
            "the likelihood of Anointed drops.  Note that Better Loot makes anointments",
            "guaranteed, so if you're using both, be sure to put whichever behavior you",
            "want most *after* the other.",
        ])

# XP
mod.comment('XP Gains')
xp_scale = 2
for table, default_val in [
        ('/Game/GameData/Modifiers/DataTable_Mayhem_CoreMods_Easy', 2),
        ('/Game/GameData/Modifiers/DataTable_Mayhem_CoreMods_Medium', 5),
        ('/Game/GameData/Modifiers/DataTable_Mayhem_CoreMods_Hard', 9),
        ]:
    mod.table_hotfix(Mod.PATCH, '',
            table,
            'ExpGain_CombatOnly',
            'MinValue',
            default_val*xp_scale)
    mod.table_hotfix(Mod.PATCH, '',
            table,
            'ExpGain_CombatOnly',
            'MaxValue',
            default_val*xp_scale)
mod.newline()

# Anoint Chances
mod.comment('Anoint drop chances -- These are currently identical to what the Farming')
mod.comment('Frenzy event has set, apart from Mayhem 3+, which is set here to be')
mod.comment('guaranteed.  Possibly the Farming Frenzy rates are permanent?')
for (col, values) in [
        ('PlaythroughOne', (2.3, 1.5, 1, 0)),
        ('PlaythroughTwoAndBeyond', (2.3, 1.5, 1, 0))
        ]:
    for row, value in zip([
            'NoneChance',
            'NoneChance_Mayhem_01',
            'NoneChance_Mayhem_02',
            'NoneChance_Mayhem_03',
            ], values):
        mod.table_hotfix(Mod.PATCH, '',
                '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/DataTable_EndGame_DropChance',
                row,
                col,
                BVCF(bvc=value))

mod.close()
