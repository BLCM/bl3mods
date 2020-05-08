#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('disable_rogue_lite.txt',
        'Disable "Rogue Lite" Mayhem 2.0 Modifier',
        [
            "As the title says, makes it so 'Rogue Lite' will never show up",
            "as a Very Hard Mayhem 2.0 modifier.  I'd always reroll if I get",
            "that one, so this just saves me some keypresses.",
        ])

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_VeryHard',
        'ModifierSets.ModifierSets[1].Weight',
        0)

mod.close()
