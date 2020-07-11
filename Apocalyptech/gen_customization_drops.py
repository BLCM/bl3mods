#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF

for (label, filename, rate, desc) in [
        ('None', 'none', 0, [
            "This removes the customization drops entirely from enemy drop pools.  It doesn't",
            "touch any specific customization drop that might exist for a particular enemy,",
            "but should get rid of nearly all world drops.  It's mostly just for if you've",
            "already got all the customizations and don't want them cluttering up your Lost",
            "Loot machine.",
            "",
            "This additionally tries to remove cosmetics from containers in the game,",
            "though that's not received much testing.",
            ]),
        ('Improved', 'improved', 0.03, [
            "This improves the customization drop rate from 0.5% to 3%, for most enemy",
            "drops.  Specific customization drops from a particular enemy haven't been",
            "touched.",
            ]),
        ('Frequent', 'frequent', 0.06, [
            "This improves the customization drop rate from 0.5% to 6%, for most enemy",
            "drops.  Specific customization drops from a particular enemy haven't been",
            "touched.",
            ]),
        ('Constant', 'constant', 0.12, [
            "This improves the customization drop rate from 0.5% to 12%, for most enemy",
            "drops.  Specific customization drops from a particular enemy haven't been",
            "touched.",
            "",
            "This will seriously interfere with your Lost Loot machine, so only really",
            "recommended if you're chasing down those last few customizations.",
            ]),
        ]:

    full_filename = 'customization_drops_{}.txt'.format(filename)

    mod = Mod(full_filename,
            'Standard Enemy Customization Drop Rate: {}'.format(label),
            'Apocalyptech',
            desc,
            lic=Mod.CC_BY_SA_40,
            )

    mod.header('Set cosmetics drop chance to {}'.format(rate))
    for pool, index in [
            ('/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear', 9),
            ('/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear', 9),
            ('/Game/GameData/Loot/ItemPools/ItemPoolList_AnointedEnemyGunsGear', 7),
            ('/Game/GameData/Loot/ItemPools/ItemPoolList_Boss', 6),
            ('/Game/GameData/Loot/ItemPools/ItemPoolList_MiniBoss', 6),
            ('/Game/GameData/Loot/ItemPools/ItemPoolList_VaultBossEnemy', 6),
            ('/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPoolList_StandardEnemyGunsandGearLoader', 9),
            ('/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPoolList_BadassEnemyGunsGearLoader1', 9),
            ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Dandelion', 9),
            ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_BadassEnemyGunsGear_Dandelion', 9),
            ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_Boss_Dandelion', 6),
            ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_MiniBoss_Dandelion', 6),
            ('/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/ItemPoolList_Constructor', 6),
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Hibiscus', 9),
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_BadassEnemyGunsGear_Hibiscus', 9),
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_Boss_Hibiscus', 6),
            ('/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_MiniBoss_Hibiscus', 6),
            ('/Game/PatchDLC/Geranium/GameData/Loot/EnemyPools/ItemPoolList_BadassEnemyGunsGear_Geranium', 9),
            ('/Game/PatchDLC/Geranium/GameData/Loot/EnemyPools/ItemPoolList_Boss_Geranium', 6),
            ('/Game/PatchDLC/Geranium/GameData/Loot/EnemyPools/ItemPoolList_MiniBoss_Geranium', 6),
            ('/Game/PatchDLC/Geranium/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Geranium', 9),
            ]:

        # Defaults vary depending on pool; for base-game it's 0.5%.
        # Tends to be higher for DLCs, I believe.
        mod.reg_hotfix(Mod.CHAR, 'MatchAll',
                pool,
                'ItemPools[{}].PoolProbability'.format(index),
                BVCF(bvc=rate))

    mod.newline()

    # Some extra things to do if we're disabling entirely.
    if rate == 0:

        # TODO: Still getting some cosmetic drops in DLC2, maybe from badasses?

        mod.header('Remove cosmetics from containers')

        mod.comment('Regular container ItemPools')
        for pool, index in [
                ('/Game/GameData/Loot/ItemPools/ItemPool_ChestFlaps', 5),
                ('/Game/GameData/Loot/ItemPools/ItemPool_RedChestFlaps', 4),
                ('/Game/GameData/Loot/ItemPools/ItemPool_Shields_Skins_Artifacts_GrenadeMods_ClassMods_Deco', 4),
                ('/Game/GameData/Loot/ItemPools/ItemPool_Shields_Skins_Artifacts_GrenadeMods_ClassMods_Deco', 5),
                ('/Game/GameData/Loot/ItemPools/ItemPool_Shields_Skins_Artifacts_GrenadeMods_ClassMods_Deco', 6),
                ('/Game/GameData/Loot/ItemPools/ItemPool_Shields_Skins_Artifacts_GrenadeMods_ClassMods_Deco', 7),
                ]:
            mod.reg_hotfix(Mod.PATCH, '',
                    pool,
                    'BalancedItems.BalancedItems[{}].Weight.BaseValueScale'.format(index),
                    rate)
        mod.newline()

        mod.comment('Container LootDef Configurations')
        for lootdef, configidx in [
                ('/Hibiscus/InteractiveObjects/Lootables/_Design/Data/BalanceData/LootDef_FishNet', 1),
                ]:
            mod.reg_hotfix(Mod.EARLYLEVEL, 'MatchAll',
                    lootdef,
                    'DefaultLoot.DefaultLoot[{}].Weight.BaseValueScale'.format(configidx),
                    rate)
        mod.newline()

        mod.comment('Container LootDef Contents')
        for lootdef, configidx, inneridxes in [
                ('/Game/Lootables/_Design/Data/Industrial/LootDef_Industrial_Refrigerator', 4, [8, 9]),
                ('/Game/PatchDLC/Geranium/Lootables/_Design/Data/Jakobs/LootDef_GER_Industrial_Refrigerator', 4, [8, 9]),
                ]:
            for inneridx in inneridxes:
                mod.reg_hotfix(Mod.EARLYLEVEL, 'MatchAll',
                        lootdef,
                        'DefaultLoot.DefaultLoot[{}].ItemAttachments.ItemAttachments[{}].Probability.BaseValueScale'.format(
                            configidx,
                            inneridx,
                            ),
                        rate)
        mod.newline()

    mod.close()

