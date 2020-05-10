#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('fewer_cartel_operatives.txt',
        'Revenge of the Cartels: Fewer Operatives',
        [
            "I enjoy having Cartel operatives pop up all over the place and",
            "provide a bit more chaos, but at their stock spawn rates, nearly",
            "every enemy encounter ends up as a total scrum.  When I'm not",
            "actively hunting them down for a Cartels mission, I'd like to",
            "ease off a bit without getting rid of them entirely.  So this",
            "just cuts their spawn probability in half.",
        ])

# Default value: 0.3
mod.table_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Event2/GameData/Balance/DataTable_Event02_Cartels',
        'OperativeSpawnChance',
        'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
        0.15)

mod.close()
