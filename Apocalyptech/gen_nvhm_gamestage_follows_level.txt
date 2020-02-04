#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, LVL_TO_ENG

mod = Mod('nvhm_gamestage_follows_level.txt',
        'NVHM GameStage Follows Player Level',
        [
            "Makes Normal/NVHM mode always scale to your player level, like it",
            "does in TVHM or Mayhem mode.",
        ],
        'NVHMGameStage',
        )

for level in sorted(LVL_TO_ENG.keys()):
    mod.reg_hotfix(Mod.LEVEL, level,
            '/Game/GameData/Regions/RegionManagerData',
            'PlayThroughs.PlayThroughs[0].bGameStageTracksPlayerLevelAboveMinimum',
            'True')

mod.close()
