#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('eridian_unlocks.txt',
        'Eridian Artifact Unlocker',
        [
            "This is the start of a mod which aims to eventually unlock the",
            "fancy Eridian tech to be available at the start of the game, namely:",
            "",
            "  - Resonator (breaks Eridian crystals)",
            "  - Analyzer (reads Eridian Writings)",
            "  - Mayhem Interface (mayhem mode)",
            "",
            "The Artifactor, which unlocks your artifact slot, is already unlocked",
            "by my Early Bloomer mod.  The Fabricator (the gun gun) doesn't",
            "interest me, so I'm real unlikely to bother looking into unlocking",
            "that one.",
            "",
            "At the moment, only the Resonator is unlocked.  I've partially figured",
            "out unlocking the Analyzer, though it behaves pretty weirdly so it's",
            "not in here yet.",
        ])

# Resonator unlock.  Kind of stupid, really, but it works great!
mod.comment('Always allow Resonator')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator',
        'OverrideCondition.Object..Conditions',
        """(
            Condition_CompareDistance_C'/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator:OverrideCondition_GbxCondition_List:Conditions_Condition_CompareDistance'
        )""")
mod.newline()

mod.close()
