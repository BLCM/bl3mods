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

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('skill_tree_shenanigans.txt',
        'Skill Tree Shenanigans',
        'Apocalyptech',
        [
        ],
        lic=Mod.CC_BY_SA_40,
        )

rgba = (.899, .012, .899, 1)

# Color alterations; only affects the individual skill icons themselves
for varname in [
        'FrameColorHeader',
        'FrameColorBackground',
        'IconColor',
        'IconBackgroundColor',
        ]:

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'BranchColorInfo.{}'.format(varname),
            '(r={},g={},b={},a={})'.format(*rgba))

# Skills
root_to_rise = '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl.AbilityTree_Siren_Brawl:Tiers_OakPlayerAbilityTreeTierData_0.Items_OakPlayerAbilityTreeItemData_Ability'
personal_space = '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl.AbilityTree_Siren_Brawl:Tiers_OakPlayerAbilityTreeTierData_0.Items_OakPlayerAbilityTreeItemData_Ability_0'
clarity = '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl.AbilityTree_Siren_Brawl:Tiers_OakPlayerAbilityTreeTierData_0.Items_OakPlayerAbilityTreeItemData_Ability_2'
one_with_nature = '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl.AbilityTree_Siren_Brawl:Tiers_OakPlayerAbilityTreeTierData_3.Items_OakPlayerAbilityTreeItemData_Ability_0'

# Augments
blight_tiger = '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl.AbilityTree_Siren_Brawl:Tiers_OakPlayerAbilityTreeTierData_1.OakPlayerAbilityTreeItemData_ActionAbilityAugment_2'
downfall = '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl.AbilityTree_Siren_Brawl:Tiers_OakPlayerAbilityTreeTierData_3.OakPlayerAbilityTreeItemData_ActionAbilityAugment_0'

# Take 1!  *Sort of* works but not really well enough to do anything with.  Skills moved beneath
# their default space seem to not work at all -- saying you need to get to level 2 to enable them.
# Skills moved *above* visually show as being available when they'd be available in their ordinary
# spot, but aren't actually clickable until you get to their new tier.  So, a bit weird all around.
if False:

    # Was just trying this out to see if it happens to make the skills work totally properly after being
    # moved.  Spoiler: it did not, so reverted back to the default notify, which is False
    notify=False

    # Swap Root To Rise (tier 1) with One With Nature (tier 4)
    if False:
        # Setting just a single element in `Items`
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
                'Tiers.Tiers[1].Object..Items.Items[0]',
                Mod.get_full_cond(one_with_nature, 'OakPlayerAbilityTreeItemData_Ability'),
                notify=notify)

        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
                'Tiers.Tiers[4].Object..Items.Items[0]',
                Mod.get_full_cond(root_to_rise, 'OakPlayerAbilityTreeItemData_Ability'),
                notify=notify)
    if True:
        # Setting the entire `Items` array
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
                'Tiers.Tiers[1].Object..Items',
                '({})'.format(','.join([
                    Mod.get_full_cond(one_with_nature, 'OakPlayerAbilityTreeItemData_Ability'),
                    Mod.get_full_cond(personal_space, 'OakPlayerAbilityTreeItemData_Ability'),
                    Mod.get_full_cond(clarity, 'OakPlayerAbilityTreeItemData_Ability'),
                    ])),
                notify=notify)

        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
                'Tiers.Tiers[4].Object..Items',
                '({})'.format(','.join([
                    Mod.get_full_cond(root_to_rise, 'OakPlayerAbilityTreeItemData_Ability'),
                    ])),
                notify=notify)

    # Fix display columns (we *could*, of course, use our fancy object-chaining syntax as we did with the
    # previous statements, to get to these objects, but I feel it's clearer if we go after them directly,
    # instead).
    mod.reg_hotfix(Mod.PATCH, '',
            one_with_nature,
            'LayoutInfo',
            'Left')

    mod.reg_hotfix(Mod.PATCH, '',
            root_to_rise,
            'LayoutInfo',
            'Center')

    # Try swapping frame names?
    # (nah, as expected that mostly just changes the icons)
    #mod.reg_hotfix(Mod.PATCH, '',
    #        one_with_nature,
    #        'ItemFrameName',
    #        'rootsToRise')
    #mod.reg_hotfix(Mod.PATCH, '',
    #        root_to_rise,
    #        'ItemFrameName',
    #        'powerSiphon')

    # Allow One With Nature to go up to 11
    #mod.reg_hotfix(Mod.PATCH, '',
    #        one_with_nature,
    #        'MaxPoints',
    #        5)

    # Unlock skills @ level 1?
    # (potentially might do something with a fresh char, maybe.  Has no effect on an existing one though)
    #mod.reg_hotfix(Mod.PATCH, '',
    #        '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren',
    #        'GradePointsToUnlockFirstTier',
    #        2)

    # Move Downfall (tier 4) to Tier 1
    mod.reg_hotfix(Mod.PATCH, '',
            'Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'Tiers.Tiers[4].Object..WingItems',
            '()',
            notify=notify)

    mod.reg_hotfix(Mod.PATCH, '',
            'Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'Tiers.Tiers[1].Object..WingItems',
            '({})'.format(Mod.get_full_cond(downfall, 'OakPlayerAbilityTreeItemData_ActionAbilityAugment')),
            notify=notify)

# Take 2; this method would require than any randomized skills at least retain the structure
# of the original tree, in order to keep working.  This has the advantage of fully working,
# though.
if True:

    # Swap Root To Rise (tier 1) with One With Nature (tier 4)
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'Tiers.Tiers[1].Object..Items.Items[0].Object..AbilityClass',
            Mod.get_full_cond('/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/OneWithNature/PassiveSkill_Siren_OneWithNature.PassiveSkill_Siren_OneWithNature_C', 'BlueprintGeneratedClass'))
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'Tiers.Tiers[1].Object..Items.Items[0].Object..ItemFrameName',
            'powerSiphon')

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'Tiers.Tiers[4].Object..Items.Items[0].Object..AbilityClass',
            Mod.get_full_cond('/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/RootToRise/PassiveSkill_Siren_RootToRise.PassiveSkill_Siren_RootToRise_C', 'BlueprintGeneratedClass'))
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'Tiers.Tiers[4].Object..Items.Items[0].Object..ItemFrameName',
            'rootsToRise')

    # Newly-placed One With Nature goes to 11?
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'Tiers.Tiers[1].Object..Items.Items[0].Object..MaxPoints',
            11)

mod.close()
