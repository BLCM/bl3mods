#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
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

# Buncha classes to abstract everything for us.

class RewardSingle:

    def __init__(self, attr, class_type, obj_name):
        self.attr = attr
        self.class_type = class_type
        self.obj_name = obj_name

    def __str__(self):
        global mod
        return '({}={})'.format(
                self.attr,
                mod.get_full_cond(self.obj_name, self.class_type),
                )

class RewardList:

    def __init__(self, attr, class_type, *obj_names):
        self.attr = attr
        self.class_type = class_type
        self.obj_names = obj_names

    def __str__(self):
        global mod
        full_names = [mod.get_full_cond(n, self.class_type) for n in self.obj_names]
        return '({}=({}))'.format(
                self.attr,
                ','.join(full_names),
                )

class Trinkets(RewardList):

    def __init__(self, *obj_names):
        super().__init__('RewardWeaponTrinkets', 'BP_BaseWeaponTrinketData_C', *obj_names)

class Customizations(RewardList):

    def __init__(self, class_type, *obj_names):
        super().__init__('RewardCustomizations', class_type, *obj_names)

class EchoThemes(Customizations):

    def __init__(self, *obj_names):
        super().__init__('ECHOThemeCustomizationData', *obj_names)

class CharSkinsHeads(Customizations):

    def __init__(self, *obj_names):
        super().__init__('OakCustomizationData', *obj_names)

class WeaponSkins(RewardList):

    def __init__(self, *obj_names):
        super().__init__('RewardWeaponSkins', 'BP_BaseWeaponSkinData_C', *obj_names)

class ItemPool(RewardSingle):

    def __init__(self, obj_name):
        super().__init__('RewardItemPool', 'ItemPoolData', obj_name)

class Rewards(object):

    def __init__(self, rewards):
        self.rewards = rewards

    def __str__(self):
        return '({})'.format(','.join([str(r) for r in self.rewards]))

# Now loop through and generate a bunch of mods.
# NOTE: the way these are structured, it seems pretty trivial to alter the
# tier rewards at will, but practically it turns out to be not especially
# useful.  The most *interesting* thing you could do with the tier rewards
# is make everything use ItemPools, and it updates visually on the event
# window to look right.  However, the tier objects themselves seem
# hardcoded to only deliver ItemPool rewards properly when that tier was
# already set to be an ItemPool.  They'll claim that the item was delivered
# but nothing will show up in inventory.  Something in the ubergraph stuff,
# presumably.  So in the absence of that, all you can *really* do is
# shuffle around cosmetics, which has limited appeal.
for event_name, event_filename, challenge_obj, years in [
        ('Bloody Harvest', 'bloody_harvest',
            '/Game/PatchDLC/BloodyHarvest/GameData/Challenges/LeagueChallenges/Challenge_BloodyHarvest_00_MetaChallenge.Default__Challenge_BloodyHarvest_00_MetaChallenge_C',
            [
                (2019, False, Rewards([
                    Trinkets('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponTrinkets/_Shared/Trinket_League_BloodyHarvest_1'),
                    EchoThemes('/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_11'),
                    CharSkinsHeads(
                        '/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_40',
                        '/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_40',
                        '/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_40',
                        '/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_40',
                        ),
                    WeaponSkins('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01'),
                    ])),
                (2020, True, Rewards([
                    Trinkets('/Game/PatchDLC/Alisma/Gear/WeaponTrinkets/_Shared/Trinket_League_BloodyHarvest_2020'),
                    EchoThemes('/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_79'),
                    CharSkinsHeads(
                        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_63',
                        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_63',
                        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_63',
                        '/Game/PatchDLC/Alisma/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_63',
                        ),
                    WeaponSkins('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_02'),
                    ])),
                ]),
        ('Broken Hearts', 'broken_hearts',
            '/Game/PatchDLC/EventVDay/GameData/Challenges/BP_Challenge_ValentinesDayEvent_MetaChallenge.Default__BP_Challenge_ValentinesDayEvent_MetaChallenge_C',
            [
                (2020, False, Rewards([
                    EchoThemes('/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/ECHODevice/EchoTheme_Valentines_01'),
                    Trinkets('/Game/PatchDLC/EventVDay/Gear/Weapon/WeaponTrinkets/_Shared/Trinket_League_VDay_1'),
                    ItemPool('/Game/PatchDLC/EventVDay/GameData/Challenges/ChallengeRewards/ItemPool_VDay_Weapon_PolyAim'),
                    CharSkinsHeads(
                        '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Beastmaster_50',
                        '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Gunner_50',
                        '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Operative_50',
                        '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Siren_50',
                        ),
                    ItemPool('/Game/PatchDLC/EventVDay/GameData/Challenges/ChallengeRewards/ItemPool_VDay_Weapon_WeddingInvitation'),
                    ])),
                (2021, True, Rewards([
                    EchoThemes('/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/ECHODevice/EchoTheme_Valentines_02'),
                    Trinkets('/Game/PatchDLC/EventVDay/Gear/Weapon/WeaponTrinkets/_Shared/Trinket_League_VDay_2'),
                    ItemPool('/Game/PatchDLC/EventVDay/GameData/Challenges/ChallengeRewards/ItemPool_VDay_Weapon_PolyAim'),
                    CharSkinsHeads(
                        '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Beastmaster_65',
                        '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Gunner_65',
                        '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Operative_65',
                        '/Game/PatchDLC/EventVDay/PlayerCharacters/_Shared/CustomSkin_Siren_65',
                        ),
                    ItemPool('/Game/PatchDLC/EventVDay/GameData/Challenges/ChallengeRewards/ItemPool_VDay_Weapon_WeddingInvitation'),
                    ])),
                ]),
        ('Revenge of the Cartels', 'cartels',
            '/Game/PatchDLC/Event2/GameData/Challenges/EventChallenges/BP_Challenge_Cartels_00_MetaChallenge.Default__BP_Challenge_Cartels_00_MetaChallenge_C',
            [
                (2020, False, Rewards([
                    EchoThemes('/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_44'),
                    Trinkets('/Game/PatchDLC/Event2/Gear/_Design/WeaponTrinkets/WeaponTrinket_Cartels_1'),
                    ItemPool('/Game/PatchDLC/Event2/Pickups/RoomDecoration/ItemPool_CartelsRoomDeco'),
                    CharSkinsHeads(
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_34',
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_34',
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_34',
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_34',
                        ),
                    CharSkinsHeads(
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_47',
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_47',
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_47',
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_47',
                        ),
                    ])),
                (2021, True, Rewards([
                    EchoThemes('/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_40'),
                    Trinkets('/Game/PatchDLC/Event2/Gear/_Design/WeaponTrinkets/WeaponTrinket_Cartels_2021'),
                    ItemPool('/Game/PatchDLC/Event2/Pickups/RoomDecoration/ItemPool_CartelsRoomDeco_2021'),
                    WeaponSkins('/Game/PatchDLC/Event2/Gear/_Design/WeaponSkins/WeaponSkin_Event2_2'),
                    CharSkinsHeads(
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_48',
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_48',
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_48',
                        '/Game/PatchDLC/Event2/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_48',
                        ),
                    ])),
                ]),
        ]:

    for year, is_current, rewards in years:

        # Description
        desc = [
                "Sets the {} challenge rewards to the {} version".format(event_name, year),
                "of the event, for anyone who would prefer to work challenges",
                "rather than farming bosses.",
            ]
        if is_current:
            desc.extend([
                "",
                "Obviously this {} version is a bit pointless since it's the default".format(year),
                "reward set when not running mods, but this way you can flip back and",
                "forth without having to quit the game, I suppose.",
                ])

        # Start the mod
        mod = Mod('event_rewards_{}_{}.bl3hotfix'.format(event_filename, year),
                'Event Rewards: {} ({})'.format(event_name, year),
                'Apocalyptech',
                desc,
                contact='https://apocalyptech.com/contact.php',
                lic=Mod.CC_BY_SA_40,
                v='1.0.0',
                cats='event',
                )

        # So: the TierRewardsPerInstance attribute inside these MetaChallenge objects all have two
        # items in the list: one per year.  Even when the events had to be activated via hotfix
        # (during which time a `LeagueInstance` attr was set elsewhere), the event code would only
        # ever use the *last* entry, and certainly that's still what happens now that the events
        # can be toggled at will.  During the non-toggleable times, resetting this array to only
        # have a single element would result in crashes.  Anyway, we'll just set the last instance
        # and be done with it.
        mod.reg_hotfix(Mod.PATCH, '',
                challenge_obj,
                'TierRewardsPerInstance.TierRewardsPerInstance[1].TierRewards',
                rewards)
        mod.newline()

        # Close
        mod.close()

