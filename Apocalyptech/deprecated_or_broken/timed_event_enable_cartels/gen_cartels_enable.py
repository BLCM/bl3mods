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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

class TierReward:

    def __init__(self, echo, trinket, deco, heads_or_weaponskin, skins):
        self.echo = echo
        self.trinket = trinket
        self.deco = deco
        self.heads_or_weaponskin = heads_or_weaponskin
        self.skins = skins

        # Bit of a silly hardcode here, but whatever.
        self.fourth_is_weaponskin = (type(heads_or_weaponskin) == str)

    def to_hotfix(self, mod):
        if self.fourth_is_weaponskin:
            fourth = '(RewardCustomizations=(),RewardWeaponSkins=({}))'.format(
                    mod.get_full_cond(self.heads_or_weaponskin, 'BP_BaseWeaponSkinData_C'),
                    )
        else:
            fourth = '(RewardCustomizations=({}),RewardWeaponSkins=())'.format(
                    ','.join([mod.get_full_cond(s, 'OakCustomizationData') for s in self.heads_or_weaponskin]),
                    )
        return """(
            (RewardCustomizations=({})),
            (RewardWeaponTrinkets=({})),
            (RewardItemPool={}),
            {},
            (RewardCustomizations=({}))
        )""".format(
                mod.get_full_cond(self.echo, 'ECHOThemeCustomizationData'),
                mod.get_full_cond(self.trinket, 'BP_BaseWeaponTrinketData_C'),
                mod.get_full_cond(self.deco, 'ItemPoolData'),
                fourth,
                ','.join([mod.get_full_cond(s, 'OakCustomizationData') for s in self.skins]),
                )

for instance, year, rewards in [
        (1, 2020, TierReward(
            '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_44',
            '/Game/PatchDLC/Event2/Gear/_Design/WeaponTrinkets/WeaponTrinket_Cartels_1',
            '/Game/PatchDLC/Event2/Pickups/RoomDecoration/ItemPool_CartelsRoomDeco',
            [
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_34',
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_34',
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_34',
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_34',
                ],
            [
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_47',
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_47',
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_47',
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_47',
                ],
            )),
        (2, 2021, TierReward(
            '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_40',
            '/Game/PatchDLC/Event2/Gear/_Design/WeaponTrinkets/WeaponTrinket_Cartels_2021',
            '/Game/PatchDLC/Event2/Pickups/RoomDecoration/ItemPool_CartelsRoomDeco_2021',
            '/Game/PatchDLC/Event2/Gear/_Design/WeaponSkins/WeaponSkin_Event2_2',
            [
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_48',
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_48',
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_48',
                '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_48',
                ],
            )),
        ]:

    mod = Mod('cartels_enable_{}.txt'.format(year),
            'Timed Event Enable: Revenge of the Cartels ({})'.format(year),
            'Apocalyptech',
            [
                "Enables the Revenge of the Cartels event.  Will interfere with any",
                "other event which happens to be running.  (Only one can be fully",
                "active at a time.)",
                "",
                "This version of the mod will enable the {} version of the event.".format(year),
                "The only difference between it and other years is the rewards you",
                "get for completing challenges, which is tracked separately",
                "between years.",
            ],
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.1.0',
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
            'OL_TheCartels')

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/Spawning/GlobalSpawnDLCData',
            'DLCs',
            """(
                (
                    Data=/Game/PatchDLC/Event2/GameData/SpawnDLCSCripts/SpawnDLC_Cartels.SpawnDLC_Cartels,
                    IsEnabled=(BaseValueConstant=1.000000)
                )
            )""")

    # The default here is apparently:
    #   SpawnOptionData'/Game/PatchDLC/BloodyHarvest/NonPlayerCharacters/LeagueNPC/_Design/Spawning/SpawnOptions_LeagueNPC_Season01.SpawnOptions_LeagueNPC_Season01'
    # Should maybe add that into our Bloody Harvest enabling thing
    mod.reg_hotfix(Mod.EARLYLEVEL, 'Sanctuary3_P',
            '/Game/Maps/Sanctuary3/Sanctuary3_Season.Sanctuary3_Season:PersistentLevel.OakMissionSpawner_1.SpawnerComponent.SpawnerStyle_SpawnerStyle_Single',
            'SpawnOptions',
            "SpawnOptionData'/Game/PatchDLC/Event2/NonPlayerCharacters/LeagueNPC/_Design/Spawning/SpawnOptions_LeagueNPC_Season02.SpawnOptions_LeagueNPC_Season02'")

    mod.newline()

    mod.comment('Main Menu')
    mod.table_hotfix(Mod.PATCH, '',
            '/Game/Common/_Design/Table_MicropatchSwitches',
            'MainMenuAltBackground',
            'Value',
            BVC(bvc=5))
    mod.newline()

    # Challenge Rewards!
    # This object *looks* like it's set up so that the rewards that are active depend on the current
    # LeagueInstance set above, but for Bloody Harvest 2020, that didn't seem to *actually* work.
    # I have not tested this on Broken Hearts or Cartels 2021, but I'm just assuming it's similarly
    # broken, so we're setting *both* instances to the same rewards, just like we do on my Bloody
    # Harvest Enable and Broken Hearts Enable mods.
    reward_str = rewards.to_hotfix(mod)
    mod.header('Hardcode Challenge Rewards')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PatchDLC/Event2/GameData/Challenges/EventChallenges/BP_Challenge_Cartels_00_MetaChallenge.Default__BP_Challenge_Cartels_00_MetaChallenge_C',
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

    # Bugfixes included with the rollout; stuff that was fixed after the data was
    # cooked, presumably.  As of the 2021 Cartels event, this hotfix is still live
    # in the official GBX hotfixes, btw.
    mod.header('Bugfixes')
    mod.reg_hotfix(Mod.LEVEL, 'Cartels_P',
            '/Game/PatchDLC/Event2/Maps/Cartels_Mission.Cartels_Mission:PersistentLevel.OakMissionWaypointBox_ACtivateStairSlide.CollisionComp',
            'RelativeScale3D',
            '(X=1.000000,Y=1.000000,Z=1.600000)')
    mod.newline()

    mod.close()

