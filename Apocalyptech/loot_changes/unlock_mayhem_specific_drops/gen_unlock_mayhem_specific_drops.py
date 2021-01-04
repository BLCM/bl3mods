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

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, ItemPoolListEntry

mod = Mod('unlock_mayhem_specific_drops.bl3hotfix',
        'Unlock Mayhem-Specific Drops',
        'Apocalyptech',
        [
            "Removes the Mayhem level requirement for gear drops which ordinarily require",
            "either Mayhem 4 or Mayhem 6 to drop.  This functionality is included in",
            "Better Loot as well, so there's not much point in running both at the same time.",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='enemy-drops, loot-system',
        )

# Main Mayhem Unlocks
for mayhem_level, data in [
        (4, [
            ('Pain', 'BPChar_Terror', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Agonizer1500_Terror', 2, None),
            ('Rampager', 'BPChar_Rampager', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_Rampager_Gun', 0, None),
            ('Anointed X-2', 'BPChar_AnointedX2', 'Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AnointedX2', 0, None),
            ('Aurelia', 'BPChar_AureliaBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AureliaBoss', 0, None),
            ('Captain Traunt', 'BPChar_Heavy_Traunt', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CaptTraunt', 0, None),
            ('Mr. Titan', 'BPChar_Goliath_SlaughterBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/Itempool_CoVSlaughterBoss', 3, None),
            ('Troy Calypso', 'BPChar_TroyBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TroyDedicated', 0, None),
            ('Arbalest of Discipline', 'BPChar_Mech_TrialBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech', 1,
                '/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Operative'),
            ('Billy, the Anointed', 'BPChar_MansionBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_MansionBoss', 0,
                '/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Gunner'),
            ('Sylestro', 'BPChar_Heavy_Bounty01', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Sylvestro', 0,
                '/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Siren'),
            ('Tink of Cunning', 'BPChar_Tink_TrialBoss', '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink', 1,
                '/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Beastmaster'),
            ]),
        (6, [
            ('Captain Traunt', 'BPChar_Heavy_Traunt', '/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SMG_Legendary1', 0, None),
            ('GenIVIV', 'BPChar_MechEvilAI', '/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SG_Legendary', 0, None),
            ('General Traunt', 'BPChar_HeavyDarkTraunt', '/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SMG_Legendary2', 0, None),
            ('Katagawa Ball', 'BPChar_Oversphere_KatagawaSphere', '/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_PS_Legendary', 0, None),
            ('Katagawa Jr.', 'BPChar_KJR', '/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_SR_Legendary', 0, None),
            ('Killavolt', 'BPChar_EnforcerKillavolt', '/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_AR_Legendary', 0, None),
            ('Pain', 'BPChar_Terror', '/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_HW_Legendary1', 0, None),
            ('Warden', 'BPChar_Goliath_CageArena', '/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPoolExpansion_Mayhem2_HW_Legendary2', 0, None),
            ('Anathema the Relentless', 'BPChar_GuardianBruteMiniboss', '/Game/PatchDLC/Takedown2/GameData/Loot/ItemPool_TD2_Miniboss', 3, None),
            ('Scourge the Invincible Martyr', 'BPChar_GuardianBruteBoss', '/Game/PatchDLC/Takedown2/GameData/Loot/ItemPool_TD2_Boss', 4, None),
            ]),
        ]:
    mod.header('Main Mayhem {} Unlocks'.format(mayhem_level))
    for char_name, char_obj, exp_obj, idx, att in sorted(data):
        mod.comment(char_name)
        if att:
            value = Mod.get_full_cond(att, 'GbxAttributeData')
        else:
            value = 'None'
        mod.reg_hotfix(Mod.CHAR, char_obj,
                exp_obj,
                'BalancedItems.BalancedItems[{}].Weight.BaseValueAttribute'.format(idx),
                value)
        mod.newline()

# Now update the itempool itself
mod.header('Maliwan Takedown Mayhem 4 Unlocks (Wotan / Valkyrie Squad)')

mod.comment('M4 Legendaries Pool')
for idx in range(11):
    for char_name in [
            'BPChar_BehemothRaid',
            'BPChar_SpiderBrain',
            'BPChar_UpperHalf',
            'BPChar_MechRaidBossBar',
            ]:
        mod.reg_hotfix(Mod.CHAR, char_name,
                '/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries',
                'BalancedItems[{}].Weight.BaseValueAttribute'.format(idx),
                'None')
mod.newline()

# This pool just calls out to the M4 legendaries pool, but it does its own Mayhem
# check so we have to clear it here, too.
mod.comment('Wotan-specific drop pool')
for char_name in [
        'BPChar_BehemothRaid',
        'BPChar_SpiderBrain',
        'BPChar_UpperHalf',
        ]:
    # The on-disk version of `ItemPool_RaidBoss_Pool` has the M4 drops at index 8, but
    # a hotfix added in May 2020 shortened the pool so the M4 drops are at index 4.
    # Making this edit to index 4 won't hurt anything if run on a game that's not using
    # the GBX hotfixes, so we're doing both.
    for idx in [4, 8]:
        mod.reg_hotfix(Mod.CHAR, char_name,
                '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool',
                'BalancedItems[{}].Weight.BaseValueAttribute'.format(idx),
                'None')
mod.newline()

# This is the same story, but for Valkyrie Squad
mod.comment('Valkyrie Squad-specific drop pool')
mod.reg_hotfix(Mod.CHAR, 'BPChar_MechRaidBossBar',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool',
        'BalancedItems[4].Weight.BaseValueAttribute',
        'None')
mod.newline()

mod.header('Guardian Takedown Mayhem 6 Unlocks (Anathema / Scourge)')
for idx in range(8):
    for char_name in [
            'BPChar_GuardianBruteMiniboss',
            'BPChar_GuardianBruteBoss',
            ]:
        mod.reg_hotfix(Mod.CHAR, char_name,
                '/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPool_Mayhem2_Legendaries',
                'BalancedItems[{}].Weight.BaseValueAttribute'.format(idx),
                'None')
mod.newline()

mod.close()
