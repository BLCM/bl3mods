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

mod = Mod('more_tracker_darts.txt',
        'More Tracker Darts',
        'Apocalyptech',
        [
            "I'm rather fond of Atlas weapons, but I've found that I pretty much",
            "never actually use them unless they have tracker darts (as opposed to",
            "pucks or grenades).  So, this mod increases the weight of the",
            "tracking dart option, so that I get those most of the time.  Tracker",
            "darts should spawn 75% of the time with this enabled.",
            "",
            "Note that most unique/legendary weapons have hardcoded or custom",
            "tracking parts -- for instance, Linc will always spawn with a tracker",
            "grenade.  Those have been left alone.  (Specifically: Rebel Yell,",
            "Freeman, Ruby's Wrath, Linc, Peacemonger, O.P.Q. System, Multi-tap,",
            "and Plumage.)",
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Default weight for all tracker delivery types is 1
new_weight = 6

# Rebel Yell, Freeman, Ruby's Wrath, Linc, and Peacemonger have custom/locked trackers
for (label, balance, bal_idx, partset, ps_pl_idx, part_idx) in [
        ('Common ARs',
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_01_Common', 18,
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/PartSets/PartSet_ATL_AR_01_Common', 4, 2),
        ('Uncommon ARs',
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_02_UnCommon', 18,
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/PartSets/PartSet_ATL_AR_02_UnCommon', 4, 2),
        ('Rare ARs',
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_03_Rare', 18,
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/PartSets/PartSet_ATL_AR_03_Rare', 4, 2),
        ('VeryRare ARs',
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_04_VeryRare', 18,
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/PartSets/PartSet_ATL_AR_04_VeryRare', 4, 2),
        ('Carrier',
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/Balance_ATL_AR_Carrier', 9,
            '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/PartSet_ATL_AR_Carrier', 4, 2),
        ('Common Heavy Weapons',
            '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_01_Common', 18,
            '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/PartSets/PartSet_ATL_HW_01_Common', 4, 2),
        ('Uncommon Heavy Weapons',
            '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_02_UnCommon', 18,
            '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/PartSets/PartSet_ATL_HW_02_UnCommon', 4, 2),
        ('Rare Heavy Weapons',
            '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_03_Rare', 18,
            '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/PartSets/PartSet_ATL_HW_03_Rare', 4, 2),
        ('VeryRare Heavy Weapons',
            '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_04_VeryRare', 18,
            '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/PartSets/PartSet_ATL_HW_04_VeryRare', 4, 2),
        ('Common Pistols',
            '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_01_Common', 24,
            '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/PartSets/PartSet_PS_ATL_01_Common', 6, 2),
        ('Uncommon Pistols',
            '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_02_UnCommon', 24,
            '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/PartSets/PartSet_PS_ATL_02_UnCommon', 6, 2),
        ('Rare Pistols',
            '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_03_Rare', 24,
            '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/PartSets/PartSet_PS_ATL_03_Rare', 6, 2),
        ('VeryRare Pistols',
            '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_04_VeryRare', 24,
            '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/PartSets/PartSet_PS_ATL_04_VeryRare', 6, 2),
        ]:

    mod.comment(label)

    balance_last = balance.split('/')[-1]
    balance_full = '{}.{}'.format(balance, balance_last)
    mod.reg_hotfix(Mod.PATCH, '',
            balance_full,
            'RuntimePartList.AllParts[{}].Weight.BaseValueConstant'.format(bal_idx),
            new_weight)

    # The parts list is duplicated, in a more clearly-delineated way, inside the PartSet
    # objects, but those don't seem to be actually used when dropping weapons.  Weird.
    #partset_last = partset.split('/')[-1]
    #partset_full = '{}.{}'.format(partset, partset_last)
    #mod.reg_hotfix(Mod.PATCH, '',
    #        partset_full,
    #        'ActorPartLists.ActorPartLists[{}].Parts[{}].Weight.BaseValueConstant'.format(ps_pl_idx, part_idx),
    #        new_weight)

    mod.newline()

mod.close()
