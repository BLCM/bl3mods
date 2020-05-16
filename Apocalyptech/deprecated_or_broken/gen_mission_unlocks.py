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

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('mission_unlocks.txt',
        'pffff',
        'Apocalyptech',
        [],
        lic=Mod.CC_BY_SA_40,
        )

# Set the item pool reward - this works!
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Default__Mission_Ep01_ChildrenOfTheVault_C:RewardData_OakMissionRewardData',
        'ItemPoolReward',
        'ItemPoolData\'"/Game/Missions/Plot/EP01_ChildrenOfTheVault/ItemPool_EP01ChildrenOfTheVault_MissionReward.ItemPool_EP01ChildrenOfTheVault_MissionReward"\'',
        #'ItemPoolData\'"/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary.ItemPool_ClassMods_05_Legendary"\'',
        )

# Testing seeing if I can unlock sanctuary right away. (doesn't seem to do the trick)
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Default__Mission_Ep01_ChildrenOfTheVault_C:RewardData_OakMissionRewardData',
        'Region',
        'RegionData\'"/Game/GameData/Regions/Zone0/Region_Sanctuary.Region_Sanctuary"\'',
        )

mod.close()
