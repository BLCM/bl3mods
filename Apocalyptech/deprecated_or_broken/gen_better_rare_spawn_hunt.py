#!/usr/bin/env python
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

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('better_rare_spawn_hunt.txt',
        'Alteration of Week 2 Event',
        [
            'Totally-guaranteed drops, and remove health buffs of enemies.',
            '',
            'https://borderlands.com/en-US/news/2019-10-07-borderlands-3-rare-spawn-hunt/',
            'https://github.com/BLCM/bl3hotfixes/blob/master/gbx_info_archive/2019-10-07-anniversary_2.md',
        ])

# Make all rare spawns 100%
mod.comment('General level-based spawn rates (unchanged from stock GBX hotfixes, but for all levels)')
mod.comment("I'm not actually sure if the extra levels make any difference (it definitely shouldn't")
mod.comment('for stuff like the trials/slaughters, for instance), but eh.')
for level_name in [
        'AtlasHQ_P',
        'Beach_P',
        'BloodyHarvest_P',
        'COVSlaughter_P',
        'CityBoss_P',
        'CityVault_P',
        'City_P',
        'Convoy_P',
        'CreatureSlaughter_P',
        'Crypt_P',
        'DesertBoss_P',
        'Desert_P',
        'Desertvault_P',
        'Desolate_P',
        'FinalBoss_P',
        'Mansion_P',
        'MarshFields_P',
        'Mine_P',
        'Monastery_P',
        'MotorcadeFestival_P',
        'MotorcadeInterior_P',
        'Motorcade_P',
        'OrbitalPlatform_P',
        'Outskirts_P',
        'Prison_P',
        'Prologue_P',
        'ProvingGrounds_Trial1_P',
        'ProvingGrounds_Trial4_P',
        'ProvingGrounds_Trial5_P',
        'ProvingGrounds_Trial6_P',
        'ProvingGrounds_Trial7_P',
        'ProvingGrounds_Trial8_P',
        'Recruitment_P',
        'Sacrifice_P',
        'Sanctuary3_P',
        'TechSlaughter_P',
        'Towers_P',
        'Watership_P',
        'WetlandsBoss_P',
        'WetlandsVault_P',
        'Wetlands_P',
        ]:
    for row_name in [
            'Rare',
            'VeryRare',
            'SuperRare',
            ]:
        mod.table_hotfix(Mod.LEVEL, level_name,
                '/Game/GameData/Balance/RareSpawns/Table_Async_RareSpawnRarities.Table_Async_RareSpawnRarities',
                row_name,
                'Value',
                """(
                    BaseValueConstant=100.000000,
                    DataTableValue=(DataTable=None,RowName="",ValueName=""),
                    BaseValueAttribute=None,
                    AttributeInitializer=None,
                    BaseValueScale=1.000000
                )""")
mod.newline()

# Some individual spawn rates which apparently don't use those values above
mod.comment('Individual Spawn rates')
mod.reg_hotfix(Mod.LEVEL, 'Towers_P',
        '/Game/Maps/Zone_1/Towers/Towers_Combat.Towers_Combat:PersistentLevel.OakMissionRareSpawner_VicAndWarty',
        'PercentChanceToSpawn',
        """(
            BaseValueConstant=100.000000,
            DataTableValue=(DataTable=None,RowName="",ValueName=""),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1.000000
        )""")
mod.newline()

# These just need pool probabilities set
mod.comment("Loot drop chances, pt. 1 - test alterations; let's see how this goes!")
for (bpchar, obj_name, vanilla_event_scale) in [
        ('BPChar_EnforcerUrist', '/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/BPChar_EnforcerUrist.BPChar_EnforcerUrist_C:AIBalanceState_GEN_VARIABLE', 3),
        ('BPChar_Goliath_Rare01', '/Game/Enemies/Goliath/_Unique/Rare01/Character/BPChar_Goliath_Rare01.BPChar_Goliath_Rare01_C:AIBalanceState_GEN_VARIABLE', 3),
        ('BPChar_Goliath_Rare02', '/Game/Enemies/Goliath/_Unique/Rare02/_Design/Character/BPChar_Goliath_Rare02.BPChar_Goliath_Rare02_C:AIBalanceState_GEN_VARIABLE', 3),
        ('BPChar_Goliath_Rare03', '/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03.BPChar_Goliath_Rare03_C:AIBalanceState_GEN_VARIABLE', 3),
        ('BPChar_Goon_Rare01', '/Game/Enemies/Goon/_Unique/Rare01/_Design/Character/BPChar_Goon_Rare01.BPChar_Goon_Rare01_C:AIBalanceState_GEN_VARIABLE', 1.5),
        ('BPChar_PsychoRare02', '/Game/Enemies/Psycho_Male/_Unique/Rare02/_Design/Character/BPChar_PsychoRare02.BPChar_PsychoRare02_C:AIBalanceState_GEN_VARIABLE', 3),
        ('BPChar_PsychoRare03', '/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03.BPChar_PsychoRare03_C:AIBalanceState_GEN_VARIABLE', 1.5),
        ('BPChar_Rakkman', '/Game/Enemies/Psycho_Male/_Unique/Rakkman/_Design/Character/BPChar_Rakkman.BPChar_Rakkman_C:AIBalanceState_GEN_VARIABLE', 3),
        ('BPChar_ServiceBot_Rare01', '/Game/Enemies/ServiceBot/_Unique/Rare01/_Design/Character/BPChar_ServiceBot_Rare01.BPChar_ServiceBot_Rare01_C:AIBalanceState_GEN_VARIABLE', 3),
        ('BPChar_SpiderantTarantella', '/Game/Enemies/Spiderant/_Unique/Tarantella/_Design/Character/BPChar_SpiderantTarantella.BPChar_SpiderantTarantella_C:AIBalanceState_GEN_VARIABLE', 3),
        ]:
    # vanilla_event_scale isn't used, but it's what the vanilla Week 2 hotfixes used in BaseValueScale
    mod.reg_hotfix(Mod.CHAR, bpchar,
            obj_name,
            'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
            """(
                BaseValueConstant=100.000000,
                DataTableValue=(DataTable=None,RowName="",ValueName=""),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.000000
            )""")
mod.newline()

# These need some more specific alterations
mod.comment('Loot drop chances, pt. 2')
mod.reg_hotfix(Mod.CHAR, 'BPChar_PunkMotherOfDragons',
        '/Game/Enemies/Punk_Female/_Unique/MotherOfDragons/_Design/Character/BPChar_PunkMotherOfDragons.BPChar_PunkMotherOfDragons_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=((ItemPool=ItemPoolData'"/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_05_Legendary.ItemPool_Artifacts_05_Legendary"',PoolProbability=(BaseValueConstant=1.000000))),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear"')
        )""")
mod.reg_hotfix(Mod.CHAR, 'BPChar_Skag_Rare01',
        '/Game/Enemies/Skag/_Unique/Rare01/_Design/Character/BPChar_Skag_Rare01.BPChar_Skag_Rare01_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools.ItemPools',
        """((ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary.ItemPool_Shields_05_Legendary"',PoolProbability=(BaseValueConstant=1.000000)))""")
mod.reg_hotfix(Mod.CHAR, 'BPChar_TinkRedJabber',
        '/Game/Enemies/Tink/_Unique/RedJabber/_Design/Character/BPChar_TinkRedJabber.BPChar_TinkRedJabber_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=((ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary.ItemPool_GrenadeMods_05_Legendary"',PoolProbability=(BaseValueConstant=1.000000))),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_MiniBoss.ItemPoolList_MiniBoss"')
        )""")
mod.reg_hotfix(Mod.CHAR, 'BPChar_Trooper_Rare01a',
        '/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01a.BPChar_Trooper_Rare01a_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=((ItemPool=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster_05_Legendary.ItemPool_ClassMods_Beastmaster_05_Legendary"',PoolProbability=(BaseValueConstant=1.000000))),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear"')
        )""")
mod.reg_hotfix(Mod.CHAR, 'BPChar_Trooper_Rare01b',
        '/Game/Enemies/Trooper/_Unique/Rare01b/_Design/Character/BPChar_Trooper_Rare01b.BPChar_Trooper_Rare01b_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=((ItemPool=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner_05_Legendary.ItemPool_ClassMods_Gunner_05_Legendary"',PoolProbability=(BaseValueConstant=1.000000))),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear"')
        )""")
mod.reg_hotfix(Mod.CHAR, 'BPChar_Trooper_Rare01c',
        '/Game/Enemies/Trooper/_Unique/Rare01c/_Design/Character/BPChar_Trooper_Rare01c.BPChar_Trooper_Rare01c_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=((ItemPool=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative_05_Legendary.ItemPool_ClassMods_Operative_05_Legendary"',PoolProbability=(BaseValueConstant=1.000000))),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear"')
        )""")
mod.reg_hotfix(Mod.CHAR, 'BPChar_Trooper_Rare01d',
        '/Game/Enemies/Trooper/_Unique/Rare01d/_Design/Character/BPChar_Trooper_Rare01d.BPChar_Trooper_Rare01d_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """(
            ItemPools=((ItemPool=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Siren_05_Legendary.ItemPool_ClassMods_Siren_05_Legendary"',PoolProbability=(BaseValueConstant=1.000000))),
            ItemPoolLists=(ItemPoolListData'"/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear"')
        )""")
mod.reg_hotfix(Mod.CHAR, 'BPChar_Trooper_Rare01e',
        '/Game/Enemies/Trooper/_Unique/Rare01e/_Design/Character/BPChar_Trooper_Rare01e.BPChar_Trooper_Rare01e_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """((ItemPool=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary.ItemPool_ClassMods_05_Legendary"',PoolProbability=(BaseValueConstant=1.000000)))""")
mod.reg_hotfix(Mod.CHAR, 'BPChar_Saurian_Rare01',
        '/Game/Enemies/Saurian/_Unique/Rare01/_Design/Character/BPChar_Saurian_Rare01.BPChar_Saurian_Rare01_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools.ItemPools',
        """(
            (
                ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/Currency/ItemPool_Money.ItemPool_Money"',
                NumberOfTimesToSelectFromThisPool=(
                    BaseValueConstant=0.000000,
                    AttributeInitializer=BlueprintGeneratedClass'"/Game/GameData/Loot/ItemPools/Init_RandomLootCount_Buttload.Init_RandomLootCount_Buttload_C"'
                )
            ),
            (
                ItemPool=ItemPoolData'"/Game/GameData/Loot/ItemPools/ItemPool_SkinsAndMisc.ItemPool_SkinsAndMisc"',
                PoolProbability=(BaseValueConstant=1.000000)
            )
        )""")
mod.newline()

# Not sure, fixing up some playthrough 1 drops for some chars...  These are unchanged from stock GBX hotfixes
# It seems like these should be related to the Mayhem/TVHM exclusions, but the object names in general don't
# make sense if interpreted that way...  Commenting for now.
#mod.reg_hotfix(Mod.CHAR, 'BPChar_EnforcerUrist',
#        '/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/BPChar_EnforcerUrist.BPChar_EnforcerUrist_C:AIBalanceState_GEN_VARIABLE',
#        'PlayThroughs.PlayThroughs[0].BalanceTableRow',
#        """(
#            DataTable=DataTable'"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique.Table_Enforcer_Balance_Unique"',
#            RowName="Enforcer_Bounty01_HotKarl"
#        )""")
#mod.reg_hotfix(Mod.CHAR, 'BPChar_Enforcer_Bounty02',
#        '/Game/Enemies/Enforcer/_Unique/Bounty02/_Design/Character/BPChar_Enforcer_Bounty02.BPChar_Enforcer_Bounty02_C:AIBalanceState_GEN_VARIABLE',
#        'PlayThroughs.PlayThroughs[0].BalanceTableRow',
#        """(
#            DataTable=DataTable'"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique.Table_Enforcer_Balance_Unique"',
#            RowName="Enforcer_Bounty01_HotKarl"
#        )""")
#mod.reg_hotfix(Mod.CHAR, 'BPChar_Nekrobug_Hunt01',
#        '/Game/Enemies/Nekrobug/_Unique/Hunt01/_Design/Character/BPChar_Nekrobug_Hunt01.BPChar_Nekrobug_Hunt01_C:AIBalanceState_GEN_VARIABLE',
#        'PlayThroughs.PlayThroughs[0].BalanceTableRow',
#        """(
#            DataTable=DataTable'"/Game/Enemies/Nekrobug/_Shared/_Design/Balance/Table_Balance_Nekrobug_Unique.Table_Balance_Nekrobug_Unique"',
#            RowName="Nekrobug__Nekrobug01_Hunt"
#        )""")

# Revert health multipliers
mod.comment('Revert health mutlipliers to standard levels (were buffed by GBX for the event)')
mod.comment('(These buffs were left in, even after the rest of the hotfix was taken out!)')
prim = 'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12'
sec = 'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49'
for (bpchar, obj_name, row_name, attr_name, scale) in [
        ('BPChar_Rakkman', '/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique.Table_Psycho_Balance_Unique', 'Rakkman', prim, 9),
        ('BPChar_Goliath_Rare03', '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique.Table_Balance_Goliath_Unique', 'Rare03', prim, 5),
        ('BPChar_OversphereRare01', '/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique.Table_Balance_Oversphere_Unique', 'Oversphere_Rare01', prim, 2),
        ('BPChar_Goliath_Rare02', '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique.Table_Balance_Goliath_Unique', 'Rare02', prim, 5),
        ('BPChar_Goliath_Rare02', '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique.Table_Balance_Goliath_Unique', 'Rare02', sec, 3),
        ('BPChar_PsychoRare03', '/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique.Table_Psycho_Balance_Unique', 'Rare03', prim, 5),
        ('BPChar_Tink_Rare01', '/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique.Table_Balance_Tink_Unique', 'Tink_Rare01', prim, 1),
        ('BPChar_Trooper_Rare01a', '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique.Table_Balance_Trooper_Unique', 'Trooper_Rare01a', prim, 6),
        ('BPChar_Trooper_Rare01b', '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique.Table_Balance_Trooper_Unique', 'Trooper_Rare01b', prim, 1.5),
        ('BPChar_Trooper_Rare01c', '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique.Table_Balance_Trooper_Unique', 'Trooper_Rare01c', prim, 3.5),
        ('BPChar_Trooper_Rare01d', '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique.Table_Balance_Trooper_Unique', 'Trooper_Rare01d', prim, 1.5),
        ('BPChar_Trooper_Rare01e', '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique.Table_Balance_Trooper_Unique', 'Trooper_Rare01e', prim, 1),
        ('BPChar_Skag_Rare01', '/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique.Table_Skag_Balance_Unique', 'DemoSkag', prim, 2.5),
        ('BPChar_Goliath_Rare01', '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique.Table_Balance_Goliath_Unique', 'Rare01', prim, 5),
        ('BPChar_Goliath_Rare01', '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique.Table_Balance_Goliath_Unique', 'Rare01', sec, 3),
        ('BPChar_TinkRare02', '/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique.Table_Balance_Tink_Unique', 'Tink_Rare02', prim, 8),
        ('BPChar_ServiceBot_Rare01', '/Game/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_ServiceBot_Unique.Table_Balance_ServiceBot_Unique', 'ServiceBot_ServiceBot01_Rare', prim, 5),
        ('BPChar_PsychoRare02', '/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique.Table_Psycho_Balance_Unique', 'Rare02', prim, 5),
        ('BPChar_PunkMotherOfDragons', '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique.Table_Balance_Punk_Unique', 'Punk_MotherOfDragons', prim, 8),
        ('BPChar_TinkRedJabber', '/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique.Table_Balance_Tink_Unique', 'Tink_RedJabber', prim, 10),
        ('BPChar_EnforcerUrist', '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique.Table_Enforcer_Balance_Unique', 'Enforcer_Bounty01_HotKarl', prim, 8),
        ('BPChar_Enforcer_BountyPrologue', '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique.Table_Enforcer_Balance_Unique', 'Enforcer_BountyPrologue', prim, 4),
        ('BPChar_PunkBounty02', '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique.Table_Balance_Punk_Unique', 'Punk_Bounty02', prim, 8),
        ('BPChar_Tink_Bounty01', '/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique.Table_Balance_Tink_Unique', 'Tink_Bounty01', prim, 1),
        ('BPChar_GoonBounty01', '/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique.Table_Balance_Goon_Unique', 'Goon_RoidRage', prim, 10),
        ('BPChar_Enforcer_Bounty01', '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique.Table_Enforcer_Balance_Unique', 'Enforcer_Bounty01_HotKarl', prim, 8),
        ('BPChar_Punk_Bounty01a', '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique.Table_Balance_Punk_Unique', 'Punk_Bounty02', prim, 8),
        ('BPChar_Punk_Bounty01b', '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique.Table_Balance_Punk_Unique', 'Punk_Bounty02', prim, 8),
        ('BPChar_Punk_Bounty01c', '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique.Table_Balance_Punk_Unique', 'Punk_Bounty02', prim, 8),
        ('BPChar_Punk_Bounty01d', '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique.Table_Balance_Punk_Unique', 'Punk_Bounty02', prim, 8),
        ('BPChar_Goliath_Bounty01', '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique.Table_Balance_Goliath_Unique', 'Bounty01', prim, 5),
        ('BPChar_Goliath_Bounty01', '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique.Table_Balance_Goliath_Unique', 'Bounty01', sec, 3),
        ('BPChar_Heavy_Bounty01', '/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique.Table_Balance_Heavy_Unique', 'Heavy_Bounty01', prim, 10),
        ('BPChar_Trooper_Bounty01', '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique.Table_Balance_Trooper_Unique', 'Trooper_Bounty01', prim, 4),
        ('BPChar_Enforcer_Bounty02', '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique.Table_Enforcer_Balance_Unique', 'Enforcer_Bounty01_HotKarl', prim, 8),
        ('BPChar_VarkidHunt02_AdultA', '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique.Table_Varkid_Balance_Unique', 'Hunt02_Adult', prim, 3),
        ('BPChar_VarkidHunt02_AdultB', '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique.Table_Varkid_Balance_Unique', 'Hunt02_Adult', prim, 3),
        ('BPChar_VarkidHunt02_LarvaA', '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique.Table_Varkid_Balance_Unique', 'Hunt02_Larva', prim, 0.5),
        ('BPChar_VarkidHunt02_LarvaB', '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique.Table_Varkid_Balance_Unique', 'Hunt02_Larva', prim, 0.5),
        ('BPChar_VarkidHunt02_LarvaC', '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique.Table_Varkid_Balance_Unique', 'Hunt02_Larva', prim, 0.5),
        ('BPChar_VarkidHunt02_LarvaD', '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique.Table_Varkid_Balance_Unique', 'Hunt02_Larva', prim, 0.5),
        ('BPChar_Ratch_Hunt01', '/Game/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_Ratch_Unique.Table_Balance_Ratch_Unique', 'Ratch_01Hunt', prim, 12),
        ('BPChar_Spiderant_Hunt01', '/Game/Enemies/Spiderant/_Shared/_Design/Balance/Table_Balance_Spiderant_Unique.Table_Balance_Spiderant_Unique', 'Spiderant_Hunt01', prim, 6),
        ('BPChar_Rakk_Hunt01', '/Game/Enemies/Rakk/_Shared/_Design/Balance/Table_Balance_Rakk_Unique.Table_Balance_Rakk_Unique', 'Rakk_Rakk01_Hunt', prim, 4),
        ('BPChar_VarkidHunt01', '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique.Table_Varkid_Balance_Unique', 'Hunt01', prim, 8),
        ('BPChar_VarkidHunt01_Tink', '/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique.Table_Varkid_Balance_Unique', 'Hunt01_Humanoid', prim, 8),
        ('BPChar_Rakk_HuntSkrakk', '/Game/Enemies/Rakk/_Shared/_Design/Balance/Table_Balance_Rakk_Unique.Table_Balance_Rakk_Unique', 'Rakk_Skrakk01_Hunt', prim, 10),
        ('BPChar_Ape_Hunt01', '/Game/Enemies/Ape/_Shared/_Design/Balance/Table_Balance_Ape_Unique.Table_Balance_Ape_Unique', 'Ape_Jabbermogwai', prim, 1.5),
        ('BPChar_Saurian_Hunt01', '/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique.Table_Balance_Saurian_Unique', 'Saurian_Saurian01_Hunt', prim, 15),
        ('BPChar_Nekrobug_HopperSwarm', '/Game/Enemies/Nekrobug/_Shared/_Design/Balance/Table_Balance_Nekrobug_Unique.Table_Balance_Nekrobug_Unique', 'Nekrobug_Broodmother', prim, 5),
        ('BPChar_Nekrobug_Hunt01', '/Game/Enemies/Nekrobug/_Shared/_Design/Balance/Table_Balance_Nekrobug_Unique.Table_Balance_Nekrobug_Unique', 'Nekrobug__Nekrobug01_Hunt', prim, 1.5),
        ('BPChar_OversphereRare01', '/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique.Table_Balance_Oversphere_Unique', 'Oversphere_Rare01', sec, 2),
        ]:
    mod.table_hotfix(Mod.CHAR, bpchar,
            obj_name,
            row_name,
            attr_name,
            scale)
mod.newline()

mod.close()
