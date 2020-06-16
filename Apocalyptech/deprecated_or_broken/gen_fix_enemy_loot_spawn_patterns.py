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

# So my *actual* goal here was to fix the Maliwan Slaughter bosses so they actually
# shoot their loot onto the main area properly, instead of just plopping them
# down where they were standing.  They're very time-consuming to get to, though, and
# Mouthpiece does the exact same thing with the majority of his loot, so I figured
# I'd try to get it working for him, first.
#
# Turns out I had no such luck; see the notes below.  Giving up for now.

mod = Mod('fix_enemy_loot_spawn_patterns.txt',
        'Fix Enemy Loot Spawn Patterns',
        'Apocalyptech',
        [
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Most enemies have "None" in here, but Mouthpiece had "Head".  Changing it didn't
# actually do anything notable, though.
#mod.reg_hotfix(Mod.CHAR, 'BPChar_EnforcerSacrificeBoss',
#        '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/Character/BPChar_EnforcerSacrificeBoss.BPChar_EnforcerSacrificeBoss_C:AIBalanceState_GEN_VARIABLE',
#        'DropLootSocketName',
#        'None')

# We'd almost certainly want to use something more like LootSpawnPattern_EnemyRing here,
# rather than StrongBackward, but I wanted something very visually distinct for testing.
# Anyway, the very first few bits of gear use whatever pattern's set here, but everything
# after just plops down as usual.  It's not even consistent as to what bits of gear get
# put in that initial burst -- it seems to *often* be generic loot, but I've had the
# unique drops in there as well, so who the heck knows.
mod.reg_hotfix(Mod.CHAR, 'BPChar_EnforcerSacrificeBoss',
        '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/Character/BPChar_EnforcerSacrificeBoss.BPChar_EnforcerSacrificeBoss_C:AIBalanceState_GEN_VARIABLE',
        'DropLootPattern',
        Mod.get_full_cond('/Game/GameData/Loot/SpawnPatterns/LootSpawnPattern_StrongBackward', 'LootSpawnPattern'))

mod.close()
