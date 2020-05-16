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

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, Pool

# Someone said it'd be fun to mock up a screenshot of some ludicrous
# "Mayhem 25" or whatever, and I thought that sounded amusing enough
# to dig into.  This isn't totally perfect; mayhems above 10 won't
# have any scaling info (no idea how to add rows to a DataTable, if
# it's even possible via hotfix), so to get a "complete" picture
# you've gotta take two screenshots and photoshop in the slider.
# Anyway, I was amused.

mod = Mod('mayhem_laffs.txt',
        'Mayhem lol',
        [
        ],
        )

EASY = '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_EAsy'
MED = '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Medium'
HARD = '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Hard'
VHARD = '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_VeryHard'

def patch_mayhem_level(level, mods):
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Mayhem2/OverrideModSet_Mayhem2',
            'PerLevelOverrides.PerLevelOverrides[{}].RandomModifierSlotsOverride'.format(level),
            '({})'.format(','.join(
                [Mod.get_full_cond(mod, 'MayhemModifierSlotDataAsset') for mod in mods]
                )))

for col_name in [
        'HealthSimpleScalar_42_0499AACF43FDF39B7084E2BB63E4BF68',
        'ShieldSimpleScalar_43_417C36C54DA2550A4CABC7B26A5E24A8',
        'ArmorSimpleScalar_44_BCAAA445479831C25B0D55AF294A15D6',
        ]:
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
            10,
            col_name,
            600)

for col_name in [
        'ExpGainScalar_39_2159F009466933AA733AE688E55B1B93',
        'CashScalar_22_B7B11DC94BBB45C94A96279146EC193E',
        ]:
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
            10,
            col_name,
            4)

mod.table_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
        10,
        'LootQuality_56_03E220E0495C6B37CD6C7195F5EA289B',
        55)

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Mayhem2/MayhemModeTwo',
        'MaxMayhemLevel',
        20)

patch_mayhem_level(9, [VHARD, VHARD, VHARD, VHARD])

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Mayhem2/ModifierSets/UI/Players/ModUiStat_Mayhem2_Players_CriticalFailure',
        'Text',
        '[IMPOSSIBLE] Time to Die')

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Mayhem2/ModifierSets/UI/Players/ModUiStat_Mayhem2_Players_CriticalFailure',
        'Description',
        'Enemies dealing health damage will immediately send you into Fight For Your Life.')

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_ElementalInfusion_All',
        'Text',
        '[IMPOSSIBLE] Iron Constitution')

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_ElementalInfusion_All',
        'Description',
        'Enemies have constant health regeneration.  Hope you have something that packs a punch...')

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_PriorityTarget',
        'Text',
        '[IMPOSSIBLE] Mirror Universe')

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_PriorityTarget',
        'Description',
        'Badass enemies spawn with a copy of your current gun and shield.')

mod.close()
