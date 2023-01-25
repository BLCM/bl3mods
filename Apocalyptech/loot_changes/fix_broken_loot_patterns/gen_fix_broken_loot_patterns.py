#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2023 Christopher J. Kucera
# <cj@apocalyptech.com>
# <https://apocalyptech.com/contact.php>
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
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('fix_broken_loot_patterns.bl3hotfix',
        'Fix Broken Loot Patterns',
        'Apocalyptech',
        [
            "A few enemies in the game drop at least part of their loot in a single",
            "tight point, making it impossible to sort through without picking some",
            "of it up first.  This mod fixes up those few cases so that the loot",
            "gets spread out in a more pleasing manner.",
            "",
            "This functionality is included in Better Loot as of v1.3.6, so there's",
            "no need to use this mod if you've got an up-to-date Better Loot.  (It",
            "won't hurt anything to have both enabled, though.)",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='bugfix',
        ss='https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/loot_changes/fix_broken_loot_patterns/mouthpiece.jpg',
        )

# Here we go!
for label, bpchar, new_time in [
        ('Mouthpiece',
            '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/Character/BPChar_EnforcerSacrificeBoss',
            1),
        ('Captain Traunt',
            '/Game/Enemies/Heavy/_Unique/Traunt/_Design/Character/BPChar_Heavy_Traunt',
            3),
        ('Loot Skrit / Loot Skritaari',
            '/Hibiscus/Enemies/Minion/Basic/_Design/Character/BPChar_MinionLoot',
            1),
        ]:
    bpchar_short = bpchar.rsplit('/', 1)[-1]
    mod.comment(label)
    mod.reg_hotfix(Mod.CHAR, bpchar_short,
            f'{bpchar}.{bpchar_short}_C:AIBalanceState_GEN_VARIABLE',
            'TimeToSpawnLootOver',
            new_time)
    mod.newline()

if False:
	# Guaranteed Loot Skrit on the one portal chest I'd been testing with.
	mod.reg_hotfix(Mod.LEVEL, 'Village_P',
	        '/Hibiscus/Maps/Village/Village_IOs.Village_IOs:PersistentLevel.BPIO_Hib_Lootable_PortalChest_2',
	        'MinionProbability',
	        100,
	        )

# And done.
mod.close()

