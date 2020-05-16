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

from bl3hotfixmod.bl3hotfixmod import Mod, LVL_TO_ENG

# Note that so far (up through DLC2), all DLCs already have a MaxGameStage of 100
# in their RegionManagerData, so we've not had to worry about DLC level scaling.

mod = Mod('nvhm_gamestage_follows_level.txt',
        'NVHM GameStage Follows Player Level',
        'Apocalyptech',
        [
            "Makes Normal/NVHM mode always scale to your player level, like it",
            "does in TVHM or Mayhem mode.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

for level in sorted(LVL_TO_ENG.keys()):
    mod.reg_hotfix(Mod.LEVEL, level,
            '/Game/GameData/Regions/RegionManagerData',
            'PlayThroughs.PlayThroughs[0].bGameStageTracksPlayerLevelAboveMinimum',
            'True')

mod.close()
