#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('torgue_full_auto.txt',
        'pffff',
        [],
        'TorgueAuto',
        )

for barrel in ['01', '02', '03']:
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Barrel/Barrel_{}/Part_AR_TOR_Barrel_{}.Part_AR_TOR_Barrel_{}:WeaponUseModeAspectData_0.BPWeaponFireProjectileComponent_Torgue_C_0'.format(
                barrel, barrel, barrel,
                ),
            'AutomaticBurstCount',
            '(BaseValue=5)',
        )

    # This exists for Dahl, not sure if it'd even be valid in here.
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Barrel/Barrel_{}/Part_AR_TOR_Barrel_{}.Part_AR_TOR_Barrel_{}:WeaponUseModeAspectData_0.BPWeaponFireProjectileComponent_Torgue_C_0'.format(
                barrel, barrel, barrel,
                ),
            'bAutoBurst',
            'True',
        )

# Longshot, didn't work (based on another GBX hotfix)
#'/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Barrel/Barrel_{}/Part_AR_TOR_Barrel_{}.Part_AR_TOR_Barrel_{}:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Torgue'.format(
#'AspectList.AspectList[0].Object..WeaponUseComponent.Object..AutomaticBurstCount',

mod.close()
