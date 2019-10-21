#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

def set_pool(mod, pool_to_set, balances):

    parts = []
    for bal in balances:
        part = '(InventoryBalanceData={},ResolvedInventoryBalanceData=InventoryBalanceData\'"{}"\',Weight=(BaseValueConstant=1))'.format(
                bal, bal,
                )
        parts.append(part)
    mod.reg_hotfix(Mod.PATCH, '',
            pool_to_set,
            'BalancedItems',
            '({})'.format(','.join(parts)))

mod = Mod('testing_loot_drops.txt',
        'Testing loot drops...',
        [],
        'Drops',
        )

pool_to_set = '/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary'
extra_pool_bit = 'ItemPool_SnipeRifles_Legendary'

balances = [
        #'/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Balance/Balance_PS_TOR_Devestator.Balance_PS_TOR_Devestator',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre.Balance_PS_Tediore_Sabre',
        ]

set_pool(mod, '{}.{}'.format(pool_to_set, extra_pool_bit), balances)

for char in [
        'BPChar_Ape',
        'BPChar_EnforcerShared',
        'BPChar_Frontrunner',
        'BPChar_Goon',
        'BPChar_GuardianShared',
        'BPChar_Heavy_Shared',
        'BPChar_Nekrobug_Shared',
        'BPChar_Nog',
        'BPChar_OversphereShared',
        'BPChar_PsychoShared',
        'BPChar_PunkShared',
        'BPChar_Rakk',
        'BPChar_Ratch',
        'BPChar_Saurian_Shared',
        'BPChar_ServiceBot',
        'BPChar_SkagShared',
        'BPChar_Spiderant',
        'BPChar_Tink',
        'BPChar_Tink_Turret',
        'BPChar_Trooper',
        'BPChar_VarkidShared',
        ]:

    mod.reg_hotfix(Mod.CHAR, char,
            '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear',
            'ItemPools[0].PoolProbability',
            """(
                BaseValueConstant=1.000000,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.000000
            )""")
    mod.reg_hotfix(Mod.CHAR, char,
            '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear',
            'ItemPools[0].ItemPool',
            'ItemPoolData\'"{}"\''.format(pool_to_set))
    mod.reg_hotfix(Mod.CHAR, char,
            '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear',
            'ItemPools[0].NumberOfTimesToSelectFromThisPool',
            """(
                BaseValueConstant=5.000000,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.000000
            )""")

mod.close()
