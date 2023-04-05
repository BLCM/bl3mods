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
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('fragile_eridium_clusters.bl3hotfix',
        'Fragile Eridium Clusters',
        'Apocalyptech',
        [
            "Allows Eridium clusters (and jars) to be broken apart by gunfire or any",
            "other source of damage, instead of requiring the Eridian Resonator to be",
            "unlocked.  As such, allows the collection of Eridium from the environment",
            "to be done from the very start of the game, without any save editing.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='gameplay, qol',
        )

# These both basically just skip the check for /Game/GameData/DamageSources/DamageSource_Melee_Resonator

mod.comment('Clusters')
mod.bytecode_hotfix(Mod.LEVEL, 'MatchAll',
        '/Game/Lootables/Eridian/Rock_Formation_Pile/Shared/PD_Rock_Formation_Pile_Eridian_Parent',
        'BndEvt__OakDamage_K2Node_ComponentBoundEvent_4_TakeAnyPipelineDamageDelegate__DelegateSignature_PD_Rock_Formation_Pile_Eridian',
        139,
        48,
        165)
mod.newline()

mod.comment('Jars')
mod.bytecode_hotfix(Mod.LEVEL, 'MatchAll',
        '/Game/InteractiveObjects/ExplodingBarrels/Global/BP_ExplodingObject_EridiumJar',
        'Damaged',
        49,
        392,
        475)
mod.newline()

# So I'd looked into seeing if I could get this mod to allow "frozen" Anointed enemies to be
# broken up by arbitrary damage as well, and never got anywhere with it.  This bytecode on
# anointed Tinks seemed promising, except for the word "Friendly" in that export name, but
# it didn't actually work, and I noticed shortly after that this kind of bytecode doesn't
# seem to appear on any other anointed enemy.  Also, DamageSource_Melee_Resonator itself
# is basically not referenced anywhere usefully.  I did also look into various anointment-
# related objects under /Game/GameData/StatusEffects but couldn't do anything useful to 'em
# in there, either.  CE_AnointedFreezing had a handy-looking bInfiniteDuration=True but
# tweaking that didn't accomplish anything useful either.  Given the general lack of object
# references to this stuff hanging about, I kind of suspect that the anointment-freezing
# thing (and subsequent resonator-melee-to-destroy thing) is hardcoded in the EXE rather
# than in game objects.  Anyway, giving up on it for now -- perhaps someday!
if False:
    mod.comment('Anointed Enemies')
    mod.bytecode_hotfix(Mod.CHAR, 'BPChar_TinkAnointed',
            '/Game/Enemies/Tink/Anointed/_Design/Character/BPChar_TinkAnointed',
            'BndEvt__OakDamageComponent_K2Node_ComponentBoundEvent_0_HitByFriendlyDelegate__DelegateSignature_BPChar_TinkAnointed',
            31,
            3281,
            3373)
    mod.newline()

mod.close()

