#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('cdh.txt',
        'Cold Dead Hands!',
        [
            'Not really, but wanted to test out if bDropOnDeath still exists',
            ],
        'CDH',
        )

for char in [
        'BPChar_PunkBasic',
        'BPChar_PunkBadass',
        'BPChar_PunkSniper',
        'BPChar_PunkShared',
        'BPChar_PunkAssaulter',
        'BPChar_PunkAnointed',
        'BPChar_Tink',
        ]:
    for pool in [
            'ItemPool_CoVEnemyUse_AssaultRifles',
            'ItemPool_COVEnemyUse_HeavyWeapons',
            'ItemPool_CoVEnemyUse_Pistols',
            'ItemPool_CoVEnemyUse_Shotguns',
            'ItemPool_CoVEnemyUse_SMGs',
            'ItemPool_CoVEnemyUse_SniperRifles',
            ]:
        for num in range(10):
            mod.reg_hotfix(Mod.CHAR, char,
                    '/Game/Enemies/_Shared/_Design/ItemPools/{}.{}'.format(pool, pool),
                    'BalancedItems[{}].bDropOnDeath'.format(num),
                    'True')

    mod.newline()

mod.close()
