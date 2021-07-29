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
import enum
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, ItemPool

class Config:

    def __init__(self, filename, label, desc,
            weap_name,
            card_ammo, card_cost,
            itempool_reg, itempool_leg,
            itempool_reg_qty, itempool_leg_qty,
            firerate_reg, firerate_leg,
            label_reg, label_leg,
            reg_cost, leg_cost,
            video=None,
            ):
        self.filename = filename
        self.label = label
        self.desc = desc
        self.weap_name = weap_name
        self.card_ammo = card_ammo
        self.card_cost = card_cost
        self.itempool_reg = itempool_reg
        self.itempool_leg = itempool_leg
        self.itempool_reg_qty = itempool_reg_qty
        self.itempool_leg_qty = itempool_leg_qty
        self.firerate_reg = firerate_reg
        self.firerate_leg = firerate_leg
        self.label_reg = label_reg
        self.label_leg = label_leg
        self.reg_cost = reg_cost
        self.leg_cost = leg_cost
        self.video = video

###
### Rapid-fire config (also defines the "default" reward pools)
###

fab_default_reg = ItemPool('/Game/GameData/Loot/ItemPools/Fabricator/ItemPool_FabricatorGuns')
fab_default_reg.add_pool('/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Uncommon', BVC(bvc=90))
fab_default_reg.add_pool('/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Rare', BVC(bvc=8))
fab_default_reg.add_pool('/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_VeryRare', BVC(bvc=2))

fab_default_leg = ItemPool('/Game/GameData/Loot/ItemPools/Fabricator/ItemPool_FabricatorGuns_AltFire')
fab_default_leg.add_pool('/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary')
fab_default_leg.add_pool('/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards', BVC(bvc=0.25))

rapidfire = Config(filename='rapidfire',
        label='Rapid-Fire',
        desc=[
            "Converts the Fabricator's primary firing mode to full auto single-gun",
            "firing, and the legendary mode to a full auto shotgun-like blast.  The",
            "quantity of gear dropped on the legendary mode has been buffed up a bit",
            "as well, which is mildly cheaty.",
            ],

        weap_name='Vladof Fabricator',
        card_ammo='Shoots [skill]guns[/skill] instead of bullets!',
        card_cost='Requires [skill]1[/skill] Eridium per gun.',

        itempool_reg=fab_default_reg,
        itempool_reg_qty=BVCF(bvc=1),
        firerate_reg=6,
        reg_cost=1,
        label_reg='Gun Hose',

        itempool_leg=fab_default_leg,
        # Buffing this a bit, so we get at least 2
        itempool_leg_qty=BVCF(ai='/Game/GameData/Loot/ItemPools/Init_RandomLootCount_SomeMinOne', bvs=2),
        firerate_leg=0.75,
        leg_cost=250,
        label_leg='Legendary Blast',
        )

###
### Eridium config
###

eridium_reg = ItemPool('foo')
eridium_reg.add_pool('/Game/GameData/Loot/ItemPools/Eridium/ItemPool_Eridium_Single')

eridium_leg = ItemPool('foo')
eridium_leg.add_pool('/Game/GameData/Loot/ItemPools/Eridium/ItemPool_Eridium_Stack')

eridium_leg_stacks = 8
eridium = Config(filename='eridium',
        label='Eridium',
        desc=[
            "Converts the Fabricator's primary firing mode to full auto single Eridium",
            "bars, and the legendary mode to a full auto shotgun-like Eridium pile blast.",
            "This is a 1-to-1 cost-to-drop ratio, so no Eridium is lost.  This could",
            "theoretically be put to Actual Use by using it to trade Eridium to co-op",
            "partners easily.",
            ],
        video='https://www.youtube.com/watch?v=AYJYnaHxLOY',

        weap_name='Eridium Redistributor',
        card_ammo='Shoots [skill]Eridium[/skill] instead of bullets!',
        card_cost='Share with your friends and family!',

        itempool_reg=eridium_reg,
        itempool_reg_qty=BVCF(bvc=1),
        firerate_reg=6,
        reg_cost=1,
        label_reg='Eridium Hose',

        itempool_leg=eridium_leg,
        itempool_leg_qty=BVCF(bvc=eridium_leg_stacks),
        firerate_leg=1.5,
        leg_cost=eridium_leg_stacks*4,
        label_leg='Eridium Blast',
        )

###
### Fabricator Fabricator
###

replicator_pool = ItemPool('foo')
replicator_pool.add_pool('/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Balance/ItemPool_Eridian_Fabricator')

replicator = Config(filename='replicator',
        label='Replicator',
        desc=[
            "Converts the Fabricator to shoot out more Fabricators instead, at a",
            "cost of 1 Eridium per Fabricator.  Looking for the perfect Mercenary",
            "Day gift?  Look no further.",
            ],

        weap_name='Fabricator Fabricator',
        card_ammo='Shoots [skill]Fabricators[/skill] instead of bullets!',
        card_cost='Requires [skill]1[/skill] Eridium per Fabricator.',

        itempool_reg=replicator_pool,
        itempool_reg_qty=BVCF(bvc=1),
        firerate_reg=6,
        reg_cost=1,
        label_reg='Fabricator',

        itempool_leg=replicator_pool,
        itempool_leg_qty=BVCF(bvc=10),
        firerate_leg=0.75,
        leg_cost=10,
        label_leg='Fabricator Fabricator',
        )

###
### Now write the mods
###

base_obj = '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Parts/Part_Eridian_Fabricator'

for config in [rapidfire, eridium, replicator]:

    full_desc = []
    full_desc.extend(config.desc)
    full_desc.extend([
        "",
        "The mod also improves the Fabricator's recoil quite a bit.",
        "Basically just intended as a joke -- enjoy!",
        ])

    mod = Mod(f'fabricator_{config.filename}.bl3hotfix',
            f'Fabricator: {config.label}',
            'Apocalyptech',
            full_desc,
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.0.0',
            cats='joke, gear-heavy',
            videos=config.video,
            )

    mod.header('Global Definitions')

    # A rather stupid way to make the Fabricator's primary firing mode free.  Was from my initial tests,
    # but this is harder to "undo," obvs.  Leaving this in here for... uh... reasons.
    #mod.reg_hotfix(Mod.PATCH, '',
    #        base_obj,
    #        'AspectList.AspectList[5]',
    #        'None')

    # Tighten up the gear-launch spread (didn't end up bothering with this; was primarily an artifact
    # from when I wanted to try and weaponize the gun pickups themselves).
    #mod.reg_hotfix(Mod.PATCH, '',
    #        '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Firing/FiringPattern_EridianFabricator',
    #        'Samples',
    #        """(
    #            StartRotation=(Pitch=0,Yaw=0,Roll=0),
    #            EndRotation=(Pitch=0,Yaw=0,Roll=0)
    #        )""")

    # Faster "projectiles" -- also a relic of my original desire to weaponize pickups
    #mod.reg_hotfix(Mod.PATCH, '',
    #        base_obj,
    #        'AspectList.AspectList[1].Object..WeaponUseComponent.Object..BaseProjectileSpeed',
    #        5000)

    # Weapon Name
    mod.comment('Weapon Name')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/WT_EridianFabricator',
            'InventoryName',
            config.weap_name)
    mod.newline()

    # Item Card
    mod.comment('Item Card')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Firing/UIStat_EridianFabricator_02',
            'FormatText',
            config.card_ammo)
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Firing/UIStat_EridianFabricator_03',
            'FormatText',
            config.card_cost)
    mod.newline()

    # Tamp down on the recoil
    mod.comment('Tamp down on recoil')
    mod.reg_hotfix(Mod.PATCH, '',
            base_obj,
            'AspectList.AspectList[7].Object..Component.Object..PatternHeightScale.BaseValue',
            0.5)
    mod.reg_hotfix(Mod.PATCH, '',
            base_obj,
            'AspectList.AspectList[7].Object..Component.Object..RecoilSpeed',
            6)
    mod.newline()

    ###
    ### "Regular" Fire -- full-auto AR-like
    ###

    mod.header('Regular Fire')

    # Label
    mod.comment('Mode Label')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/UIModeName_Fabricator_PrimaryFire',
            'Text',
            config.label_reg)
    mod.newline()

    # Just a single gun per slot
    mod.comment('One projectile per shot')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Att_FabricatorProjectilesPerShot',
            'ValueResolver.Object..Value.BaseValueConstant',
            1)
    mod.newline()

    # Shot cost
    mod.comment('Shot cost')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Att_FabricatorShotCost',
            'ValueResolver.Object..Value.BaseValueConstant',
            config.reg_cost)
    mod.newline()

    # Full auto!
    mod.comment('Full Auto')
    mod.reg_hotfix(Mod.PATCH, '',
            base_obj,
            'AspectList.AspectList[1].Object..WeaponUseComponent.Object..AutomaticBurstCount.BaseValue',
            0)
    mod.newline()

    mod.comment('Fire Rate')
    mod.reg_hotfix(Mod.PATCH, '',
            base_obj,
            'AspectList.AspectList[1].Object..WeaponUseComponent.Object..FireRate.BaseValue',
            config.firerate_reg)
    mod.newline()

    # Set firing itempools
    mod.comment('Setting the item pool')
    mod.reg_hotfix(Mod.PATCH, '',
            fab_default_reg.pool_name,
            'BalancedItems',
            str(config.itempool_reg))
    mod.reg_hotfix(Mod.PATCH, '',
            fab_default_reg.pool_name,
            'Quantity',
            config.itempool_reg_qty)
    mod.newline()

    ###
    ### "Legendary" Fire -- Making this into the shotgunny one
    ###

    mod.header('Legendary Fire')

    # Label
    mod.comment('Mode Label')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/UIModeName_Fabricator_AltFire',
            'Text',
            config.label_leg)
    mod.newline()

    # Full auto!
    mod.comment('Full Auto')
    mod.reg_hotfix(Mod.PATCH, '',
            base_obj,
            'AspectList.AspectList[2].Object..WeaponUseComponent.Object..AutomaticBurstCount.BaseValue',
            0)
    mod.newline()

    mod.comment('Fire Rate')
    mod.reg_hotfix(Mod.PATCH, '',
            base_obj,
            'AspectList.AspectList[2].Object..WeaponUseComponent.Object..FireRate.BaseValue',
            config.firerate_leg)
    mod.newline()

    mod.comment('Firing Cost')
    mod.reg_hotfix(Mod.PATCH, '',
            base_obj,
            'AspectList.AspectList[2].Object..WeaponUseComponent.Object..ShotAmmoCost.BaseValue',
            config.leg_cost)
    mod.reg_hotfix(Mod.PATCH, '',
            base_obj,
            'AspectList.AspectList[2].Object..WeaponUseComponent.Object..MinShotAmmoCost',
            config.leg_cost)
    mod.newline()

    mod.comment('Setting the item pool')
    mod.reg_hotfix(Mod.PATCH, '',
            fab_default_leg.pool_name,
            'BalancedItems',
            str(config.itempool_leg))
    mod.reg_hotfix(Mod.PATCH, '',
            fab_default_leg.pool_name,
            'Quantity',
            config.itempool_leg_qty)
    mod.newline()

    mod.close()

