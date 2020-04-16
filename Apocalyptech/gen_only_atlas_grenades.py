#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, Pool

mod = Mod('only_atlas_grenades.txt',
        'Only Atlas Grenades',
        [
            "While doing a Zane runthrough, I only really wanted homing grenades,",
            "since I didn't have a lot of control over when exactly they were",
            "getting thrown out (or at least I didn't care enough to try and",
            "control for that).  So, I wanted only homing.  This does that!",
            "",
            "This does *not* affect legendary grenade drops, only the regular",
            "sort.",
        ],
        'OnlyAtlasGrenades',
        )

for pool_name in [
        'ItemPool_GrenadeMods_01_Common',
        'ItemPool_GrenadeMods_02_Uncommon',
        'ItemPool_GrenadeMods_03_Rare',
        'ItemPool_GrenadeMods_04_VeryRare',
        ]:
    for idx in range(1, 6):
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/GameData/Loot/ItemPools/GrenadeMods/{}'.format(pool_name),
                'BalancedItems.BalancedItems[{}].Weight'.format(idx),
                BVCF(bvc=0))

mod.close()
