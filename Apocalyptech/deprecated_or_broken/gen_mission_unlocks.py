#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('mission_unlocks.txt',
        'pffff',
        [],
        'MissionUnlocks',
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
