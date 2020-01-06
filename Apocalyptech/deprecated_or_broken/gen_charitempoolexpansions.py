#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('charitempoolexpansions.txt',
        'CharacterItemPoolExpansions altering tests...',
        [],
        'CIPE',
        )

# getall CharacterItemPoolExpansionData CharacterExpansions
#
# Testing this out on IndoTyrant, trying to get it to drop five legendary snipers.
#
# IndoTyrant is actually at index 58, but if we modify index 0 we can see the results right
# on the console, without having to dig into memory.  The problem I'm having is that every
# single one of these *only* sets the key.  The way they show up in a `getall` is:
#
#  CharacterExpansions = (("BPChar_AnointedJoe_C", (ItemPoolExpansions=(/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_AnointedJoe.ItemPoolExpansion_AnointedJoe))),...

# Whole lotta failed attempts follow...

#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
#        'CharacterExpansions[0]',
#        """(
#            "BPChar_Saurian_Rare01_C",
#            (
#                DropOnDeathItemPools=(
#                    (
#                        ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary.ItemPool_SnipeRifles_Legendary"',
#                        PoolProbability=(BaseValueConstant=1),
#                        NumberOfTimesToSelectFromThisPool=(BaseValueConstant=5)
#                    )
#                )
#            )
#        )""")

#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
#        'CharacterExpansions[0]',
#        """BPChar_Saurian_Rare01_C,
#            (
#                DropOnDeathItemPools=(
#                    (
#                        ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary.ItemPool_SnipeRifles_Legendary"',
#                        PoolProbability=(BaseValueConstant=1),
#                        NumberOfTimesToSelectFromThisPool=(BaseValueConstant=5)
#                    )
#                )
#            )""")

#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
#        'CharacterExpansions[0].key',
#        'BPChar_Saurian_Rare01_C')
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
#        'CharacterExpansions[0].value',
#        """(
#            DropOnDeathItemPools=(
#                (
#                    ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary.ItemPool_SnipeRifles_Legendary"',
#                    PoolProbability=(BaseValueConstant=1),
#                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=5)
#                )
#            )
#        )""")

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
        'CharacterExpansions[0][0]',
        'BPChar_Saurian_Rare01_C')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
        'CharacterExpansions[0][1]',
        """(
            ItemPoolExpansions=(),
            DropOnDeathItemPools=(
                (
                    ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary.ItemPool_SnipeRifles_Legendary"',
                    PoolProbability=(BaseValueConstant=1),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=5)
                )
            )
        )""")

#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
#        'CharacterExpansions[0]',
#        'BPChar_Saurian_Rare01_C')
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
#        'CharacterExpansions[1]',
#        # May as well see if the values show up after the keys, maybe?
#        #'CharacterExpansions[74]',
#        """(
#            ItemPoolExpansions=(),
#            DropOnDeathItemPools=(
#                (
#                    ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary.ItemPool_SnipeRifles_Legendary"',
#                    PoolProbability=(BaseValueConstant=1),
#                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=5)
#                )
#            )
#        )""")

#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
#        'CharacterExpansions[0]',
#        """(
#            key=BPChar_Saurian_Rare01_C,
#            value=(
#                DropOnDeathItemPools=(
#                    (
#                        ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary.ItemPool_SnipeRifles_Legendary"',
#                        PoolProbability=(BaseValueConstant=1),
#                        NumberOfTimesToSelectFromThisPool=(BaseValueConstant=5)
#                    )
#                )
#            )
#        )""")

mod.close()
