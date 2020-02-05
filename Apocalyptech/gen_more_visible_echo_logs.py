#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('more_visible_echo_logs.txt',
        'More Visible ECHO Logs',
        [
            "Alters the loot bar for ECHO logs (and coincidentally mission-related pickups,",
            "and anything else using that smallish cyan bar) so that it's *much* taller and",
            "a bit wider, to be more easily visible from a distance.  Put this together",
            "because even after a few playthroughs I wasn't sure if I'd heard all the ECHOs",
            "yet, and these might help me suss a few more out.",
            "",
            "Technically this also lengthens the ammo/eridium/health/money/booster bars a bit,",
            "but only by a very small amount.",
        ],
        'VEchoLogs',
        )

# default: 85
height = 900
interactive_height = 200

# default = 2.25
width = 15

# This controls the interactive height of the beam
mod.comment('Interactive height')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Loot/RarityData/RarityData_00_Mission',
        'RarityLootBeamHeight',
        interactive_height)
mod.newline()

# These two statements define how big the main bar is, visually.
mod.comment('Visual size')
for (attr, value) in [
        ('Constant.Y', height),
        ('Constant.X', width),
        ]:
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Pickups/_Shared/Effects/Systems/PS_ConsumableLocatorStick.PS_ConsumableLocatorStick:ParticleModuleSize_0.DistributionVectorConstant_1',
            attr,
            value)
mod.newline()

# The "common" gear loot stick is nearly identical to the consumables one, which
# is what we're buffing up in this mod, so we'll reassign everything else which
# uses the now-huge one to the Common stick instead.  I'm leaving `RarityLootBeamHeight`
# alone for these, so that there's still at least *some* difference between 'em.
mod.comment('Reassign ammo/eridium/health/money/booster loot bars')
common_stick = Mod.get_full_cond('/Game/Pickups/_Shared/Effects/Systems/PS_ItemLocatorStick_Common', 'ParticleSystem')
for rd in [
        '/Game/GameData/Loot/RarityData/RarityData_00_Ammo',
        '/Game/GameData/Loot/RarityData/RarityData_00_Eridium',
        '/Game/GameData/Loot/RarityData/RarityData_00_Health',
        '/Game/GameData/Loot/RarityData/RarityData_00_Money',
        '/Game/GameData/Loot/RarityData/RarityData_00_ShieldBooster',
        ]:
    mod.reg_hotfix(Mod.PATCH, '',
            rd,
            'RarityLootBeamOverride',
            common_stick)
mod.newline()

# What follows is a bunch of other stuff I'm unsure about.  All these statements *work*
# in that they set the vars I'm intending them to, but they didn't actually alter the
# ingame stuff that I was looking to change.  So yeah: no idea what these actually do,
# but figured I'd leave 'em in here for posterity.
if False:

    for attr in [
            'StartSize.MaxValue',
            'StartSize.MinValueVec.Y',
            'StartSize.MaxValueVec.Y',
            ]:
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/Pickups/_Shared/Effects/Systems/PS_ConsumableLocatorStick.PS_ConsumableLocatorStick:ParticleModuleSize_0',
                attr,
                round(height/3, 6))

    for attr in [
            'StartSize.MinValueVec.X',
            'StartSize.MaxValueVec.X',
            ]:
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/Pickups/_Shared/Effects/Systems/PS_ConsumableLocatorStick.PS_ConsumableLocatorStick:ParticleModuleSize_0',
                attr,
                width)

    table_scale_h = 120/85
    table_scale_w = 3/2.25

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Pickups/_Shared/Effects/Systems/PS_ConsumableLocatorStick.PS_ConsumableLocatorStick:ParticleModuleSize_0',
            'StartSize.Table.Values.Values[0]',
            round(width*table_scale_w, 6))

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Pickups/_Shared/Effects/Systems/PS_ConsumableLocatorStick.PS_ConsumableLocatorStick:ParticleModuleSize_0',
            'StartSize.Table.Values.Values[1]',
            round(height*table_scale_h, 6))

    # Not sure if ParticleModuleSize_5 has anything to do with it...

    other_scale = 140/200

    for attr in [
            'StartSize.MaxValue',
            'StartSize.MinValueVec.X',
            'StartSize.MaxValueVec.X',
            ]:
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/Pickups/_Shared/Effects/Systems/PS_ConsumableLocatorStick.PS_ConsumableLocatorStick:ParticleModuleSize_5',
                attr,
                20)

    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/Pickups/_Shared/Effects/Systems/PS_ConsumableLocatorStick.PS_ConsumableLocatorStick:ParticleModuleSize_5',
            'StartSize.Table.Values.Values[0]',
            round(20*other_scale, 6))

mod.close()
