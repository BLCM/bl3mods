#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('torgue_ar_full_auto.txt',
        'Torgue ARs: Full Auto',
        [
            "Makes Torgue ARs full auto, apart from a few legendary ones which specifically have",
            "burst-fire modes.  In general only 'generic' ARs needed fixing, apart from the",
            "Alchemist."
        ])

for obj_name in [
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/Part_AR_TOR_Barrel_01',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Barrel/Barrel_02/Part_AR_TOR_Barrel_02',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Barrel/Barrel_03/Part_AR_TOR_Barrel_03',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Alchemist/Parts/Part_AR_TOR_Barrel_Alchemist',
        ]:
    last_bit = obj_name.split('/')[-1]
    mod.reg_hotfix(Mod.PATCH, '',
            f'{obj_name}.{last_bit}:AspectList_WeaponUseModeAspectData.WeaponUseComponent_BPWeaponFireProjectileComponent_Torgue',
            'AutomaticBurstCount',
            '(Value=0,BaseValue=0)')

mod.close()
