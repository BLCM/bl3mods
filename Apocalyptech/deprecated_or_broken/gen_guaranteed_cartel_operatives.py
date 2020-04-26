#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('guaranteed_cartel_operatives.txt',
        'Revenge of the Cartels: Guaranteed Operatives',
        [
            "All spawns which can generate operatives should do so.  This is",
            "actually a bit much, I stopped using it after a couple of tests.",
        ],
        'CartelGuar',
        )

mod.table_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Event2/GameData/Balance/DataTable_Event02_Cartels',
        'OperativeSpawnChance',
        'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
        1)

mod.close()
