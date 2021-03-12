#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('no_marcus_character_intros.txt',
        'No Marcus Character Intros',
        'Apocalyptech',
        [
            "Doesn't work!  The object we need to modify gets loaded dynamically",
            "and I've never been able to figure out how to trigger a hotfix for",
            "that situation.",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol',
        )

for name, ts_idx in [
        ('Gunner', 2),
        ('Siren', 3),
        ('Beastmaster', 4),
        ('Operative', 5),
        ]:
    mod.comment(name)
    # Have never successfully doing a Package-based hotfix (and GBX has never used
    # it in their own hotfixes, alas)
    for pkg in [
            'DialogScript_RNR_Intro',
            '/Game/Dialog/Scripts/Scripted/DialogScript_RNR_Intro',
            ]:
        mod.reg_hotfix(Mod.PACKAGE, pkg,
                '/Game/Dialog/Scripts/Scripted/DialogScript_RNR_Intro',
                'TimeSlots.TimeSlots[{}].Object..Lines.Lines[0].Object..Performances'.format(ts_idx),
                '()')
        mod.reg_hotfix(Mod.PACKAGE, pkg,
                '/Game/Dialog/Scripts/Scripted/DialogScript_RNR_Intro',
                'TimeSlots.TimeSlots[{}].Object..DecisionTree.ResultBuckets.ResultBuckets[0].Results.Results[0].Line'.format(ts_idx),
                'None')
    mod.newline()

mod.close()
