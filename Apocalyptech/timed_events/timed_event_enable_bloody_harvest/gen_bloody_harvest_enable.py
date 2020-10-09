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
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

heck = 'BloodyHarvest_P'
boss = 'BPChar_HarvestBoss'

# TODO: Once the event is over, keep an eye on the BH-related hotfixes from the
# pre-activation hotfix set: https://github.com/BLCM/bl3hotfixes/commit/8c6911ec1ad4c7446b416799ba7ba3fcf6215e90
# I suspect those changes will be made permanent, so I'm not including them
# now, but keep an eye on it...

class TierReward(object):

    def __init__(self, trinket, echo, skins, weapskin):
        self.trinket = trinket
        self.echo = echo
        self.skins = skins
        self.weapskin = weapskin

    def to_hotfix(self, mod):
        return """(
            (RewardWeaponTrinkets=({})),
            (RewardCustomizations=({})),
            (RewardCustomizations=({})),
            (RewardWeaponSkins=({}))
        )""".format(
                mod.get_full_cond(self.trinket, 'BP_BaseWeaponTrinketData_C'),
                mod.get_full_cond(self.echo, 'ECHOThemeCustomizationData'),
                ','.join([mod.get_full_cond(s, 'OakCustomizationData') for s in self.skins]),
                mod.get_full_cond(self.weapskin, 'BP_BaseWeaponSkinData_C'),
                )

for instance, year, rewards in [
        (1, 2019, TierReward(
            trinket='/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponTrinkets/_Shared/Trinket_League_BloodyHarvest_1',
            echo='/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_11',
            skins=[
                '/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_40',
                '/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_40',
                '/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_40',
                '/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_40',
                ],
            weapskin='/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01',
            )),
        (2, 2020, TierReward(
            trinket='/Game/PatchDLC/Alisma/Gear/WeaponTrinkets/_Shared/Trinket_League_BloodyHarvest_2020',
            echo='/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_79',
            skins=[
                '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_63',
                '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_63',
                '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_63',
                '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_63',
                ],
            weapskin='/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_02',
            )),
        ]:

    mod = Mod('bloody_harvest_enable_{}.bl3hotfix'.format(year),
            'Timed Event Enable: Bloody Harvest ({})'.format(year),
            'Apocalyptech',
            [
                "Enables the Bloody Harvest event.  Will interfere with any other",
                "event which happens to be running.  (Only one can be fully",
                "active at a time.)",
                "",
                "Includes various balance changes and fixes which were active during",
                "the event, so you get as close to the \"live\" event experience as",
                "possible.",
                "",
                "This version of the mod will enable the {} version of the event.".format(year),
                "The only difference between it and other years is the rewards you",
                "get for completing challenges, which is tracked separately",
                "between years.",
            ],
            lic=Mod.CC_BY_SA_40,
            v='1.1.1',
            cats='event',
            )

    mod.header('Global activation switches')

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/GameplayGlobals',
            'ActiveLeague',
            'OL_BloodyHarvest')

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/GameplayGlobals',
            'LeagueInstance',
            instance)

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/Spawning/GlobalSpawnDLCData',
            'DLCs',
            """(
                (
                    Data=/Game/PatchDLC/BloodyHarvest/GameData/SpawnDLCScripts/SpawnDLC_BloodyHarvest.SpawnDLC_BloodyHarvest,
                    IsEnabled=(BaseValueConstant=1.000000)
                )
            )""")

    mod.newline()

    mod.comment('Activate main menu changes')
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/Common/_Design/Table_MicropatchSwitches',
            'MainMenuAltBackground',
            'Value',
            '(BaseValueConstant=3.000000)')
    mod.newline()

    # Challenge Rewards!
    # Challenge_BloodyHarvest_00_MetaChallenge really *looks* like it's set up so that the rewards
    # that are active depend on the current LeagueInstance set above, but they just don't seem to
    # be.  I've not been able to find a way to get it to use anything but LeagueInstance 2, and
    # the game is pretty fussy about the array -- any additions to the array end up just being
    # empty, and removing the second instance altogether crashes the game.  So, we're gonna do it
    # the stupid way and just set the rewards for *both* instances to the year we're looking for.
    # Really we'd only have to do it for instance 2, but eh...
    reward_str = rewards.to_hotfix(mod)
    mod.header('Hardcode Challenge Rewards')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/BloodyHarvest/GameData/Challenges/LeagueChallenges/Challenge_BloodyHarvest_00_MetaChallenge.Default__Challenge_BloodyHarvest_00_MetaChallenge_C',
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

    # Increased terror-anoint chances
    mod.header('Increased chance of Terror-anointment drops from various sources')

    for label, part, hf_type, hf_target in [
            ('Ghosts', 'Att_EndGamePartTerror_Multiplier_Ghost', Mod.LEVEL, 'MatchAll'),
            ('Bloody Harvest-specific Enemies', 'Att_EndGamePartTerror_Multiplier_BHEnemy', Mod.LEVEL, heck),
            ('Bloody Harvest Red Chests', 'Att_EndGamePartTerror_Multiplier_RedChest', Mod.LEVEL, heck),
            ('Captain Haunt', 'Att_EndGamePartTerror_Multiplier_Boss', Mod.CHAR, boss),
            ]:
        mod.comment(label)
        mod.reg_hotfix(hf_type, hf_target,
                f'/Game/PatchDLC/BloodyHarvest/Gear/_Design/_GearExtension/GParts/{part}.{part}:ValueResolver_ConstantAttributeValueResolver',
                'Value.BaseValueScale',
                10)
        mod.newline()

    # Captain Haunt!
    mod.header('Captain Haunt Tweaks')

    mod.comment('Increased drop rate')
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/BloodyHarvest/GameData/Balance/BloodyHarvest/DataTable_Season_Halloween',
            'HarvestBoss_LootDropChance',
            'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
            0.25)
    mod.newline()

    mod.comment('Increased health')
    mod.table_hotfix(Mod.CHAR, boss,
            '/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies',
            'Boss_Normal',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
            15)

    mod.table_hotfix(Mod.CHAR, boss,
            '/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies_PT2',
            'Boss_Normal',
            'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
            30)
    mod.newline()

    mod.comment('Drop from Boss pool, instead of Miniboss')
    mod.reg_hotfix(Mod.CHAR, boss,
            '/Game/PatchDLC/BloodyHarvest/Enemies/Heavy/_Unique/HarvestBoss/_Design/Character/BPChar_HarvestBoss.BPChar_HarvestBoss_C:AIBalanceState_GEN_VARIABLE',
            'DropOnDeathItemPools.ItemPoolLists.ItemPoolLists[0]',
            mod.get_full_cond('/Game/GameData/Loot/ItemPools/ItemPoolList_Boss', 'ItemPoolListData'))
    mod.newline()

    mod.comment('Audio fixes')
    mod.reg_hotfix(Mod.CHAR, boss,
            '/Game/PatchDLC/BloodyHarvest/Enemies/Heavy/_Unique/HarvestBoss/_Design/Character/BPChar_HarvestBoss.BPChar_HarvestBoss_C:DefaultAudioComponent_GEN_VARIABLE',
            'EmitterGain',
            10,
            notify=True)

    mod.reg_hotfix(Mod.CHAR, boss,
            '/Game/PatchDLC/BloodyHarvest/Enemies/Heavy/_Unique/HarvestBoss/_Design/Character/BPChar_HarvestBoss.BPChar_HarvestBoss_C:DefaultAudioComponent_GEN_VARIABLE',
            'RelativeScale3D',
            '(X=20.000000,Y=20.000000,Z=20.000000)',
            notify=True)

    mod.newline()

    mod.header('Other Tweaks/Fixes')

    # Some tweaks that I actually *don't* want in here
    if False:
        # These hotfixes reduced the frequency of Terror anoints outside of Heck Hole (introduced on Nov 7,")
        # and continued until the end of the event).  I suspect that anyone enabling this mod probably wants")
        # the full original Terror anoint drop rate, so I'm commenting these out.  I'm actually tempted to")
        # even *increase* the scaling a bit, but eh.")
        mod.comment('Reduce frequency of Terror anoints outside of Heck Hole')
        for att in [
                'Att_EndGame_GenericPartTerrorChance',
                'Att_EndGame_Gunner_PartTerrorChance',
                'Att_EndGame_Beastmaster_PartTerrorChance',
                'Att_EndGame_Operative_PartTerrorChance',
                'Att_EndGame_Siren_PartTerrorChance',
                ]:
            mod.reg_hotfix(Mod.PATCH, '',
                    f'/Game/PatchDLC/BloodyHarvest/Gear/_Design/_GearExtension/GParts/{att}.{att}:ValueResolver_SimpleMathValueResolver',
                    'ValueB.BaseValueScale',
                    0.1)
        mod.newline()

        # Likewise, this reduces the frequency of finding haunted enemies out in the overworld.
        # If you're using this mod, I suspect you're specifically *looking* for haunted enemies,
        # so I'm gonna keep them at the default value
        mod.comment('Reduce frequency of haunted enemies')
        for var, old_val, new_val in [
                ('ChanceToSpawnAsHaunted', 0.45, 0.35),
                ('ChanceToSpawnAsHaunted_Badass', 0.8, 0.6),
                ]:
            mod.table_hotfix(Mod.PATCH, '',
                    '/Game/PatchDLC/BloodyHarvest/GameData/Balance/BloodyHarvest/DataTable_Season_Halloween',
                    var,
                    'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
                    new_val)
        mod.newline()

    # Hecktoplasm drops
    mod.comment('Increase hecktoplasm drop quantities from ghosts')
    for pool, num_times in [
            ('ItemPoolList_Ghost_MissionItems_Normal', 3),
            ('ItemPoolList_Ghost_MissionItems_Badass', 3),
            ('ItemPoolList_Ghost_MissionItems_Loot', 5),
            ]:
        for idx in range(2):
            mod.reg_hotfix(Mod.CHAR, 'MatchAll',
                    '/Game/PatchDLC/BloodyHarvest/Missions/Side/Seasonal/BloodyHarvest_Intro/{}'.format(pool),
                    'ItemPools.ItemPools[{}].NumberOfTimesToSelectFromThisPool.BaseValueConstant'.format(idx),
                    num_times)
    mod.newline()

    # Loot Ghost drops
    mod.comment('Increase quantity of drops from Loot Ghosts, and make legendaries more likely')
    mod.reg_hotfix(Mod.CHAR, 'MatchAll',
            '/Game/PatchDLC/BloodyHarvest/Enemies/Ghost/_Shared/LootPool/ItemPool_BH_LootGhost',
            'Quantity',
            BVCF(bvc=7))
    mod.reg_hotfix(Mod.CHAR, 'MatchAll',
            '/Game/PatchDLC/BloodyHarvest/Enemies/Ghost/_Shared/LootPool/ItemPool_BH_LootGhost',
            'BalancedItems.BalancedItems[4].Weight.BaseValueConstant',
            0.032759)
    mod.newline()

    if False:
        # This is something related to twitch streaming integration.  I don't actually want
        # to include anything like that in mods, but figured I'd keep it here for reference.
        mod.reg_hotfix(Mod.LEVEL, heck,
                '/Game/GameData/Social/StreamingInteraction/Events/StreamingInteraction_Lootable_RedChest',
                'LootableFilterBalanceData.LootableFilterBalanceData[2]',
                mod.get_full_cond('/Game/Lootables/_Design/Data/Eridian/LootDef_Eridian_RedChest'))

    mod.close()

