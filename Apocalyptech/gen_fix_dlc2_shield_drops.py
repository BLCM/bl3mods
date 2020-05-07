#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('fix_dlc2_shield_drops.txt',
        'Fix DLC2 Shield Drops',
        [
            "Most enemies in DLC2 (Guns, Love, and Tentacles) don't actually drop",
            "shields.  For standard enemies, they're in the pool list but with a",
            "zero weight.  For badasses, they're absent entirely from the pool",
            "list.  We're fixing the Standard ones, but not bothering with Badasses",
            "for now.",
        ])

mod.reg_hotfix(Mod.CHAR, 'MatchAll',
        '/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Hibiscus',
        'ItemPools.ItemPools[6].PoolProbability.BaseValueAttribute',
        Mod.get_full_cond('/Game/GameData/Loot/ItemPools/Attributes/Att_Shields_DropOdds', 'GbxAttributeData'))
mod.close()
