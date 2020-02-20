#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('craders_emp5_super_buff.txt',
        "Super buff for Crader's EM-P5.  Cheating!",
        [
            "Vastly buffs Crader's EM-P5's damage, makes it not consume any ammo,",
            "gives it perfect accuracy+handling (though the in-game Handling stat",
            "won't say 100%), and improves its already-good fire rate",
            "",
            "Used by myself primarily just for mod testing purposes, for when I",
            "don't want to be bothered by actual combat.",
            "",
            "Note that any EM-P5 with the x2 Grip will consume 1 ammo (as opposed",
            "to its usual 2).  This mod prevents further x2 Grips from spawning.",
        ],
        'Craders',
        )

# The default Crader's barrel doesn't have *any* InventoryAttributeEffects, so these
# are all new.  Note that I'm not really sure which of these are *actually* providing
# what benefits; just basically throwing everything that seemed likely at it.  Could
# maybe have tried some more OverrideBaseValue instead of ScaleSimple, too...
attr_effects = []
for (attr, mod_type, mod_val) in [

        # Increased Damage
        ('/Game/GameData/Weapons/Att_Weapon_Damage', 'ScaleSimple', 6000),

        # Infinite ammo.
        ('/Game/GameData/Weapons/Att_Weapon_ShotAmmoCost', 'OverrideBaseValue', 0),

        # Fire Rate!  Already quite good, but what the hell.  Excess makes the heart grow fonder.
        ('/Game/GameData/Weapons/Att_Weapon_FireRate', 'ScaleSimple', 1.5),

        ###
        ### From here on our it's a bit more guessworky...
        ###

        # Better Accuracy
        ('/Game/GameData/Weapons/Att_Weapon_Spread', 'ScaleSimple', 0.001),

        # Better Impulse
        ('/Game/GameData/Weapons/Att_Weapon_AccuracyImpulse', 'ScaleSimple', 0.001),

        # Better Handling
        ('/Game/GameData/Weapons/Att_Weapon_SwayScale', 'ScaleSimple', 0.001),
        ('/Game/GameData/Weapons/Att_Weapon_SwayZoomScale', 'ScaleSimple', 0.001),

        # Better Recoil
        ('/Game/GameData/Weapons/Att_Weapon_RecoilHeightScale', 'ScaleSimple', 0.001),
        ('/Game/GameData/Weapons/Att_Weapon_RecoilWidthScale', 'ScaleSimple', 0.001),

        ]:

    last_part = attr.split('/')[-1]
    full_attr = '{}.{}'.format(attr, last_part)
    
    attr_effects.append(f"""(
        AttributeToModify=GbxAttributeData'"{full_attr}"',
        ModifierType={mod_type},
        ModifierValue=(BaseValueConstant={mod_val})
    )""")

# Apply all our custom effects
mod.comment('Custom Effects')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Parts/Part_SM_DAL_Barrel_CraderMP5',
        'InventoryAttributeEffects',
        '({})'.format(','.join(attr_effects)),
        )
mod.newline()

# Also buff movement speed increase.  Stock: 0.25
# No longer doing this, since I figured out a real movement speed mod.
#mod.table_hotfix(Mod.PATCH, '',
#        '/Game/PatchDLC/Raid1/Re-Engagement/Balance/DataTable_ReEngagement1_Weapons.DataTable_ReEngagement1_Weapons',
#        'CraderMP5',
#        'Custom_B_11_6D4E8C1140CC269ED614BC958ECB0E22',
#        0.75)

# Also, prevent the x2 Grip from spawning, since we'll start consuming ammo
# then.  We *could* probably just use a -1 Att_Weapon_ShotAmmoCost, which
# would make the thing actually regen ammo on non-x2 grips, but we'll just
# disallow it anyway.
mod.comment('Disallow x2 Grip from Spawning')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5',
        'RuntimePartList.AllParts.AllParts[24].Weight.BaseValueConstant',
        0)
mod.newline()

mod.close()
