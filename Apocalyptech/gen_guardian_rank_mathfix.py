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

mod = Mod('guardian_rank_mathfix.txt',
        "Guardian Rank Math Fix",
        'Apocalyptech',
        [
            "Five Guardian Ranks scale up more slowly than the others - with just one",
            "point in them, they register at 0.99% as opposed to 1%, and at 40 points",
            "the difference has widened to 12.31% as opposed to 14.04%.  This mod sets",
            "them to scale at the same rate as the others.",
            "",
            "Now, it's worth noting that this change is only to a 'UIStat' object, and",
            "might possibly *only* affect the display of the numbers (so that with this",
            "mod enabled, the number is no longer accurate).  Or, possibly, the strength",
            "of the effect only depends on the number of points put into the stats, not",
            "the percent value, in which case this mod might be effectively nerfing the",
            "stat by making it approach its effective maximum more quickly.  Or,",
            "possibly the stat depends on the displayed percent, in which case this",
            "mod's a buff.",
            "",
            "So: this is either a buff, or a nerf, or does nothing but change a number",
            "in the UI.  Who can tell?  I suspect the latter.  Anyway, this evens the",
            "numbers out, whatever its other effects.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

for stat in [
        '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/UI/GuardianRank_UIStat_Accuracy',
        '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/UI/GuardianRank_UIStat_ActionSkillCooldown',
        '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/UI/GuardianRank_UIStat_GunRecoil',
        '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/UI/GuardianRank_UIStat_GunReloadSpeed',
        '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/UI/GuardianRank_UIStat_ShieldRechargeDelay',
        ]:

    mod.reg_hotfix(Mod.PATCH, '',
            stat,
            'bCalculateWithReductionMath',
            'False')

mod.close()
