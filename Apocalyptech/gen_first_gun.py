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

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, Pool

# The socket names can be found inside `Skeleton` objects, such as the one for this container:
#     /Game/Lootables/COV/Crate_Ammo/Model/Rig/SK_COV_Ammo_Box_Skeleton
# Fortunately, these are serializable with JWP
for filename, label, comments, attachments, set_gun in [
        ('full_loadout', 'Full Loadout',
            [
                "Updates the opening gun chest in Covenant Pass to include a full set of",
                "gear, including two pistols, shield, grenade, COM, and artifact.  (Obviously",
                "you'll need something like my Early Bloomer mod if you want to be able to",
                "use the COM/artifact.)",
            ],
            [
                ('TopLeft', '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Pistols_All'),
                ('TopMiddle', '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All'),
                ('TopRight', '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_All'),
                ('BottomLeft', '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods'),
                ('BottomMiddle', '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts'),
                ('BottomRight', '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Pistols_All'),
            ],
            False),
        ('testing_gear', 'Testing Gear',
            [
                "Updates the opening chest in Covenant Pass to contain my mod-testing gear,",
                "namely a Crader's EM-P5 and a Transformer.  Depending on circumstance, you",
                "might be more interested in my modtest_char_setup mod, which also does this",
                "(among other things).",
            ],
            [
                ('TopLeft', '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_FirstGun'),
                ('BottomRight', '/Game/Gear/Shields/_Design/_Uniques/Transformer/Balance/ItemPool_Shield_Recharger'),
            ],
            '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5'),
        ]:

    full_filename = 'first_gun_{}.txt'.format(filename)
    mod = Mod(full_filename,
            'First Gun Chest: {}'.format(label),
            'Apocalyptech',
            comments + [
                "",
                "Note that if the first thing you take out of the opening chest isn't a gun,",
                "you'll automatically receive a bonus gun from the FirstGun pool, in your",
                "inventory.",
                "",
                "Also updates the car-trunk chest which provides your second and third guns",
                "to pull from the main pistol pool rather than locked to white Jakobs+Dahl",
                "pistols.",
                ],
            lic=Mod.CC_BY_SA_40,
            )

    mod.comment('Update the chest LootDef')
    stanzas = []
    for (socket, pool) in attachments:
        stanzas.append("""(
                ItemPool=ItemPoolData'"{}"',
                AttachmentPointName={},
                Probability=(BaseValueConstant=1)
            )""".format(Mod.get_full_cond(pool), socket))
    # This does have to be EARLYLEVEL to work, btw.
    mod.reg_hotfix(Mod.EARLYLEVEL, 'Recruitment_P',
            '/Game/Missions/Plot/EP01_ChildrenOfTheVault/LootDef_Global_WhiteChest_ChildrenOfTheVault',
            'DefaultLoot.DefaultLoot[0].ItemAttachments',
            '({})'.format(','.join(stanzas)))
    mod.newline()

    # Also update the First Gun pool, if need be
    if set_gun:
        mod.comment('Update first-gun pool')

        mod.reg_hotfix(Mod.LEVEL, 'Recruitment_P',
                '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_FirstGun',
                'BalancedItems.BalancedItems[0].InventoryBalanceData',
                Mod.get_full_cond(set_gun))

        mod.reg_hotfix(Mod.LEVEL, 'Recruitment_P',
                '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_FirstGun',
                'BalancedItems.BalancedItems[0].ResolvedInventoryBalanceData',
                Mod.get_full_cond(set_gun, 'InventoryBalanceData'))

        mod.newline()

    # Now do the changes to the second-gun pool
    mod.comment('Update second-gun LootDef')
    for idx in [4, 5]:
        mod.reg_hotfix(Mod.EARLYLEVEL, 'Recruitment_P',
                '/Game/Missions/Plot/EP01_ChildrenOfTheVault/LootDef_Industrial_CarTrunk_Prologue',
                'DefaultLoot.DefaultLoot[0].ItemAttachments.ItemAttachments[{}].ItemPool'.format(idx),
                Mod.get_full('/Game/GameData/Loot/ItemPools/Guns/ItemPool_Pistols_All', 'ItemPoolData'))
    mod.newline()

    mod.close()
    print('Created {}'.format(full_filename))

