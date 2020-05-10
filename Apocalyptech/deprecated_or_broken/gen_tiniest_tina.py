#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, Pool

mod = Mod('tiniest_tina.txt',
        'Tiniest Tina',
        [
            "Scales down Tina a bunch, for a laff.  (Based entirely on the April Fool's",
            "thing from GBX, here -- not sure how many of the scaling vars *actually*",
            "need updating for this to work properly.  I'd think maybe just the first one?",
        ])

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
