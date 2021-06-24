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

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

class TierReward(object):

    def __init__(self, echo, trinket, skins):
        self.echo = echo
        self.trinket = trinket
        self.skins = skins

    def to_hotfix(self, mod):
        return """(
            (RewardCustomizations=({})),
            (RewardWeaponTrinkets=({})),
            (RewardItemPool={}),
            (RewardCustomizations=({})),
            (RewardItemPool={})
        )""".format(
                mod.get_full_cond(self.echo, 'ECHOThemeCustomizationData'),
                mod.get_full_cond(self.trinket, 'BP_BaseWeaponTrinketData_C'),
                Mod.get_full_cond('/Game/PatchDLC/EventVDay/GameData/Challenges/ChallengeRewards/ItemPool_VDay_Weapon_PolyAim', 'ItemPoolData'),
                ','.join([mod.get_full_cond(s, 'OakCustomizationData') for s in self.skins]),
                Mod.get_full_cond('/Game/PatchDLC/EventVDay/GameData/Challenges/ChallengeRewards/ItemPool_VDay_Weapon_WeddingInvitation', 'ItemPoolData'),
                )

for instance, year, rewards in [
        (1, 2020, TierReward(
            echo='/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/ECHODevice/EchoTheme_Valentines_01',
            trinket='/Game/PatchDLC/EventVDay/Gear/Weapon/WeaponTrinkets/_Shared/Trinket_League_VDay_1',
            skins=[
                '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Beastmaster_50',
                '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Gunner_50',
                '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Operative_50',
                '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Siren_50',
                ],
            )),
        (2, 2021, TierReward(
            echo='/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/ECHODevice/EchoTheme_Valentines_02',
            trinket='/Game/PatchDLC/EventVDay/Gear/Weapon/WeaponTrinkets/_Shared/Trinket_League_VDay_2',
            skins=[
                '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Beastmaster_65',
                '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Gunner_65',
                '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Operative_65',
                '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Siren_65',
                ],
            )),
        ]:

    mod = Mod('broken_hearts_enable_{}.txt'.format(year),
            'Timed Event Enable: Broken Hearts ({})'.format(year),
            'Apocalyptech',
            [
                "Enables the Broken Hearts event.  Will interfere with any other event which",
                "happens to be running.  (Only one can be fully active at a time.)",
                "",
                "This version of the mod will enable the {} version of the event.".format(year),
                "The 2020 and 2021 versions are very similar but have a few differences",
                "between them.  Check the README for more info on that!",
            ],
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.1.1',
            cats='event',
            )

    mod.comment('Global activation switches')

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/GameplayGlobals',
            'LeagueInstance',
            instance)

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/GameplayGlobals',
            'ActiveLeague',
            'OL_ValentinesDay')

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/Spawning/GlobalSpawnDLCData',
            'DLCs',
            """(
                (
                    Data=/Game/PatchDLC/EventVDay/GameData/SpawnDLCScripts/SpawnDLC_VDay.SpawnDLC_VDay,
                    IsEnabled=(BaseValueConstant=1.000000)
                )
            )""")

    # The default here is apparently:
    #   SpawnOptionData'/Game/PatchDLC/BloodyHarvest/NonPlayerCharacters/LeagueNPC/_Design/Spawning/SpawnOptions_LeagueNPC_Season01.SpawnOptions_LeagueNPC_Season01'
    # Should maybe add that into our Bloody Harvest enabling thing
    mod.reg_hotfix(Mod.EARLYLEVEL, 'Sanctuary3_P',
            '/Game/Maps/Sanctuary3/Sanctuary3_Season.Sanctuary3_Season:PersistentLevel.OakMissionSpawner_1.SpawnerComponent.SpawnerStyle_SpawnerStyle_Single',
            'SpawnOptions',
            Mod.get_full_cond('/Game/PatchDLC/EventVDay/NonPlayerCharacters/LeagueNPC/_Design/Spawning/SpawnOptions_LeagueNPC_VDay', 'SpawnOptionData'))

    mod.newline()

    # Challenge Rewards!
    # This object *looks* like it's set up so that the rewards that are active depend on the current
    # LeagueInstance set above, but for Bloody Harvest 2020, that didn't seem to *actually* work.
    # I have not tested this on Broken Hearts 2021, but I'm just assuming it's similarly broken, so
    # we're setting *both* instances to the same rewards, just like we do on my Bloody Harvest
    # Enable mods.
    reward_str = rewards.to_hotfix(mod)
    mod.header('Hardcode Challenge Rewards')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/EventVDay/GameData/Challenges/BP_Challenge_ValentinesDayEvent_MetaChallenge.Default__BP_Challenge_ValentinesDayEvent_MetaChallenge_C',
            'TierRewardsPerInstance',
            f"""(
                (
                    LeagueInstance=1,
                    TierRewards={reward_str}
                ),
                (
                    LeagueInstance=2,
                    TierRewards={reward_str}
                )
            )""")
    mod.newline()

    # The 2020 and 2021 events ended up having a couple of different hotfixes each
    if year == 2020:

        # Balance changes - default here is 8500, apparently.  This never showed up
        # for the 2021 event.
        mod.comment('Balance Changes')
        mod.table_hotfix(Mod.CHAR, 'MatchAll',
                '/Game/PatchDLC/EventVDay/Enemies/Hearts/_Shared/Balance/Table_VDay_LootRarityBalance',
                'LootHeart',
                'LegendaryWeightModifier_18_B98DE11946C28DF64D94E197F7FED9BE',
                6500)
        mod.newline()

        # Reward scaling.  This *was* originally in the 2021 event, but was removed
        # before it was over
        mod.comment('Force Terminal Polyaimorous and Wedding Invitation to Level 65')
        for row in [
                'PolyAim',
                'WeddingInvitation',
                ]:
            mod.table_hotfix(Mod.PATCH, '',
                    '/Game/PatchDLC/EventVDay/Gear/Weapon/DataTable_WeaponBalance_EventVDay',
                    row,
                    'MinGameStage_5_E12DB0C74420238367FBC1A5221AFB84',
                    65)
        mod.newline()

    elif year == 2021:

        # This is pretty unimportant, but whatever
        mod.comment('Fix "final day" notification')
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/PatchDLC/EventVDay/GameData/ExpansionData_VDay',
                'LeagueFinalDay',
                25)
        mod.newline()

        # Terminal Polyaimorous and Wedding Invitation were added as Loot Heart drops instead
        # of just challenge rewards.  This actually differs from the 2021 event as it was,
        # 'cause they overwrote the entire pool.  With the Loot Heart rates as they were,
        # though, it was just nothing but TPs and WIs constantly, which felt like a bit much.
        # So, I'm actually nerfing that here (and omitting the Quantity tweak entirely).  The
        # stock 2021 BalancedItems hotfix did not have a `Weight` parameter for either gun.
        mod.comment('Set Terminal Polyaimorous and Wedding Invitation as Loot Heart drops')
        mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                '/Game/PatchDLC/EventVDay/Enemies/Hearts/_Shared/LootPool/ItemPool_VDay_LootHeart',
                'BalancedItems',
                """(
                    (
                        ItemPoolData=ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All.ItemPool_Guns_All"',
                        Weight=(BaseValueConstant=0.150000)
                    ),
                    (
                        ItemPoolData=ItemPoolData'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods.ItemPool_ClassMods"',
                        Weight=(
                            BaseValueConstant=0.000000,
                            BaseValueAttribute=GbxAttributeData'"/Game/GameData/Loot/ItemPools/Attributes/Att_ClassMods_DropOdds.Att_ClassMods_DropOdds"'
                        )
                    ),
                    (
                        ItemPoolData=ItemPoolData'"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All.ItemPool_Shields_All"',
                        Weight=(
                            BaseValueConstant=0.000000,
                            BaseValueAttribute=GbxAttributeData'"/Game/GameData/Loot/ItemPools/Attributes/Att_Shields_DropOdds.Att_Shields_DropOdds"'
                        )
                    ),
                    (
                        ItemPoolData=ItemPoolData'"/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts.ItemPool_Artifacts"',
                        Weight=(
                            BaseValueConstant=0.000000,
                            BaseValueAttribute=GbxAttributeData'"/Game/GameData/Loot/ItemPools/Attributes/Att_Artifact_DropOdds.Att_Artifact_DropOdds"'
                        )
                    ),
                    (
                        InventoryBalanceData=/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim.Balance_SM_MAL_PolyAim,
                        ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim.Balance_SM_MAL_PolyAim"',
                        Weight=(BaseValueConstant=0.04)
                    ),
                    (
                        InventoryBalanceData=/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite.Balance_SR_JAK_WeddingInvite,
                        ResolvedInventoryBalanceData=InventoryBalanceData'"/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite.Balance_SR_JAK_WeddingInvite"',
                        Weight=(BaseValueConstant=0.04)
                    )
                )""")
        #mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
        #        '/Game/PatchDLC/EventVDay/Enemies/Hearts/_Shared/LootPool/ItemPool_VDay_LootHeart',
        #        'Quantity.AttributeInitializer',
        #        'BlueprintGeneratedClass\'/Game/GameData/Loot/ItemPools/Init_RandomLootCount_SomeMinOne.Init_RandomLootCount_SomeMinOne_C\'"')

        # Presumably these two are related to the loot change, too.
        mod.raw_line('SparkLevelPatchEntry,(1,7,0,MatchAll),/Game/PatchDLC/EventVDay/GameData/SpawnDLCScripts/SpawnDLCSCript_VDay_Test.SpawnDLCSCript_VDay_Test_C,0,1,OnActorSpawned,1,3432,8:0.800000,8:0.680000')
        mod.raw_line('SparkLevelPatchEntry,(1,7,0,MatchAll),/Game/PatchDLC/EventVDay/GameData/SpawnDLCScripts/SpawnDLCSCript_VDay_Test.SpawnDLCSCript_VDay_Test_C,0,1,OnActorSpawned,1,3296,8:0.850000,8:0.680000')
        mod.newline()

    mod.close()


