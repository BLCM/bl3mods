#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('maggie_super_buff.txt',
        'Super buff for Maggie.  Cheating!',
        [
            "Vastly buffs Maggie's damage, and makes it not consume any ammo.",
            "Used by myself primarily just for mod testing purposes, for when I don't",
            "want to be bothered by actual combat.  Originally used just to power",
            "through those interminable Slaughters, though.",
        ],
        'Maggie',
        )

# Original version of this mod just did the following, rather than editing the
# InventoryAttributeEffects directly:

#mod.table_hotfix(Mod.PATCH, '',
#        '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_JAK.DataTable_WeaponBalance_Unique_JAK',
#        'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
#        50)

attr_effects = []
for (attr, mod_type, mod_val) in [
        # Original: 0.35, after GBX nerf: 0.15
        ('/Game/GameData/Weapons/Att_Weapon_Damage', 'ScaleSimple', 50),

        # Stock
        ('/Game/GameData/Weapons/Att_Weapon_Spread', 'ScaleSimple', 3.5),

        # Stock (sort of doesn't matter w/ our infinite ammo thing, but whatever)
        ('/Game/GameData/Weapons/Att_Weapon_MaxLoadedAmmo', 'PreAdd', 4),

        # Stock
        ('/Game/GameData/Weapons/Att_Weapon_CustomSightColorScheme', 'OverrideBaseValue', 1),

        # New!  Infinite ammo.
        ('/Game/GameData/Weapons/Att_Weapon_ShotAmmoCost', 'OverrideBaseValue', 0),

        # Buff movement speed. - doesn't actually work; this needs to be specified as part of
        # an AttributeEffects structure, not InventoryAttributeEffects, which doesn't look like
        # it even exists in the usual Part structure.  Crader's EM-P5 has it specified in a
        # separate StatusEffect var.
        #('/Game/GameData/Attributes/Character/Att_GroundSpeedScale', 'Scale', 1.5),
        ]:

    last_part = attr.split('/')[-1]
    full_attr = '{}.{}'.format(attr, last_part)
    
    attr_effects.append(f"""(
        AttributeToModify=GbxAttributeData'"{full_attr}"',
        ModifierType={mod_type},
        ModifierValue=(BaseValueConstant={mod_val})
    )""")

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Parts/Part_PS_JAK_Barrel_Maggie.Part_PS_JAK_Barrel_Maggie',
        'InventoryAttributeEffects',
        '({})'.format(','.join(attr_effects)),
        )

mod.close()
