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

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF

mod = Mod('tiniest_tina.txt',
        'Tiniest Tina',
        'Apocalyptech',
        [
            "Scales down Tina a bunch, for a laff.  (Based entirely on the April Fool's",
            "thing from GBX, here -- not sure how many of the scaling vars *actually*",
            "need updating for this to work properly.  I'd think maybe just the first one?",
        ],
        lic=Mod.CC_BY_SA_40,
        )

reg_scale = 0.35
enraged_scale = 0.25

mod.reg_hotfix(Mod.CHAR, 'BPChar_TinyTina',
        '/Game/NonPlayerCharacters/TinyTina/_Design/Character/BPChar_TinyTina.Default__BPChar_TinyTina_C:CharacterMesh0',
        'RelativeScale3D',
        f'(X={reg_scale},Y={reg_scale},Z={reg_scale})')

mod.reg_hotfix(Mod.CHAR, 'BPChar_TinyTina',
        '/Game/NonPlayerCharacters/TinyTina/_Design/Character/BPChar_TinyTina.Default__BPChar_TinyTina_C',
        'PreEnragedActorScale',
        f'(X={reg_scale},Y={reg_scale},Z={reg_scale})')

mod.reg_hotfix(Mod.CHAR, 'BPChar_TinyTina',
        '/Game/NonPlayerCharacters/TinyTina/_Design/Character/BPChar_TinyTina.Default__BPChar_TinyTina_C',
        'EnragedActorScale',
        f'(X={enraged_scale},Y={enraged_scale},Z={enraged_scale})')

mod.reg_hotfix(Mod.CHAR, 'BPChar_TinyTina',
        '/Game/NonPlayerCharacters/TinyTina/_Design/Character/UIName_TinyTina',
        'DisplayName',
        'Tiniest Tina')

mod.close()
