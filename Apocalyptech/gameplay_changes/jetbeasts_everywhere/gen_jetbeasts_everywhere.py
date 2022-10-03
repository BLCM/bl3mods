#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021-2022 Christopher J. Kucera
# <cj@apocalyptech.com>
# <https://apocalyptech.com/contact.php>
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
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

# So we have the following constraints about Type-11 Hotfixes:
#
#   1) We can't inject any object which already exists in the map
#   1a) This applies for subclasses, too -- if an object inherits from
#       something else, and exists in the map already, you can't spawn
#       the "base" object either.
#   2) Newly-injected objects will always exist in `<levelname>_P`, as
#      oppposed to, say, `<levelname>_Combat` or `<levelname>_Dynamic`
#
# Additionally, for Catch-A-Ride objects, we have the following:
#
#   3) CAR Consoles can *only* attach to CAR Platforms which are in the
#      same level "namespace," for instance `<levelname>_P` versus
#      `<levelname>_Dynamic`.
#   4) Only about a third of the CAR objects in the game live in
#      `<levelname>_P`.
#
# So there's a lot of restrictions, but fortunately we have enough different
# objects that we can *generally* do what we need to do.  There are three
# different Console objects:
#
#     /Game/InteractiveObjects/GameSystemMachines/CatchARide/_Shared/Blueprints/BP_CatchARide_Console
#     /Geranium/InteractiveObjects/GameSystemMachines/CatchARide/_Shared/Blueprints/BP_CatchARide_Console_Ger
#     /Hibiscus/InteractiveObjects/Systems/CatchARide/_Design/BP_Hib_CatchARide_Console
#
# The Geranium and Hibiscus ones both inherit from the base-game one, so we
# can't inject base-game consoles on maps which have either of those.  The
# Hibiscus one has a MaterialOverride defined which makes it look subtly
# different (and more fitting for a snowy map).  All three can be configured
# to spawn either the base-game vehicles or Jetbeasts, using the RestrictionType
# attr on the console.
#
# There are two Platform objects:
#
#     /Game/InteractiveObjects/GameSystemMachines/CatchARide/_Shared/Blueprints/BP_CatchARide_Platform
#     /Hibiscus/InteractiveObjects/Systems/CatchARide/_Design/BP_Hib_CatchARide_Platform
#
# As you might expect, the Hibiscus one inherits from the base-game one.  The
# Hibiscus one also has a MaterialOverride defined which makes it look subtly
# different (and more fitting for a snowy map).
#
# So, for a console/platform group which lives in `<levelname>_P`, our job is
# easy:  We can just spawn whichever Console we need (which'll either be the
# Geranium or Hibiscus versions), hook it up to the existing platforms, and
# Björn Stronginthearm's your uncle.  This is what the Hook class does.
#
# For console/platform groups which do *not* live in `<levelname>_P`, we
# need to inject our own new Console/Platform pair, since there's no way to
# hook into the existing ones.  For everywhere except Skittermaw Basin, we
# can use the Hibiscus platforms, but due to constraint 1a, above, we're not
# able to use the base-game platforms, either.  So for Hibiscus, we're SOL.
#
# For maps that are *not* Skittermaw Basin, though, adding in new
# console/platform pairs is easy.  We can either put them alongside the
# existing ones (which is what the New class does), or do the nuclear option
# and move the existing ones out of the way and place our new ones exactly
# where the originals used to be (which is what the Replace class does).

mod = Mod('jetbeasts_everywhere.bl3hotfix',
        'Jetbeasts (Almost) Everywhere',
        'Apocalyptech',
        [
            "Adds in Jetbeast-spawning stations wherever Catch-A-Ride stations are",
            "found, throughout the game.  Also adds in regular-vehicle spawning",
            "stations in The Blastplains, to complement the Jetbeasts there.",
            "",
            "This unfortunately omits Skittermaw Basin, where due to some limitations",
            "of hotfixes, our methods here won't work.",
            "",
            "This mod requires either OpenHotfixLoader or B3HM v1.0.2 (or higher)",
            "to work properly.  Note that at time of release, B3HM v1.0.2 has not yet",
            "been released.  It will also be incompatible with any other mod which",
            "adds Catch-A-Ride consoles/platforms to the same map.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol, maps, vehicle',
        quiet_streaming=True,
        ss='https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/gameplay_changes/jetbeasts_everywhere/metroplex.png',
        )


class Config:
    """
    Configuration of our object types, depending on what DLC we're operating in.
    """

    # "New" coordinates specified in this mod were taken from apple1417's BL3TP
    # app, using a Siren.  The camera coords there are a bit too high, so we need
    # to lower our objects
    z_nudge_console = 90
    z_nudge_plat = 100

    def __init__(self, console_obj, console_replace_obj, plat_obj,
            set_replaced_console_enum=None,
            platform_mat_override=None,
            console_new_mat_override=None,
            console_replaced_mat_override=None,
            ):
        self.console_obj = console_obj
        self.console_replace_obj = console_replace_obj
        self.plat_obj = plat_obj
        self.set_replaced_console_enum = set_replaced_console_enum
        self.platform_mat_override = platform_mat_override
        self.console_new_mat_override = console_new_mat_override
        self.console_replaced_mat_override = console_replaced_mat_override


# Set our configuration per DLC
config_reg = Config(
    console_obj='/Geranium/InteractiveObjects/GameSystemMachines/CatchARide/_Shared/Blueprints/BP_CatchARide_Console_Ger',
    console_replace_obj='/Hibiscus/InteractiveObjects/Systems/CatchARide/_Design/BP_Hib_CatchARide_Console',
    plat_obj='/Hibiscus/InteractiveObjects/Systems/CatchARide/_Design/BP_Hib_CatchARide_Platform',
    console_new_mat_override='/Hibiscus/InteractiveObjects/Systems/CatchARide/MI_Hib_CAR_Station',
    )
# Unfortunately we actually *can't* do our stuff in DLC2, because the no-spawning-
# objects-which-are-already-in-the-map appears to apply to subobjects too.  Since
# the dlc2 map already contains Hib platforms (which inherit from base-game), we
# can't spawn any base-game platforms of our own.  QQ
#config_dlc2 = Config(
#    console_obj='/Geranium/InteractiveObjects/GameSystemMachines/CatchARide/_Shared/Blueprints/BP_CatchARide_Console_Ger',
#    console_replace_obj='/Game/InteractiveObjects/GameSystemMachines/CatchARide/_Shared/Blueprints/BP_CatchARide_Console',
#    plat_obj='/Game/InteractiveObjects/GameSystemMachines/CatchARide/_Shared/Blueprints/BP_CatchARide_Platform',
#    platform_mat_override='/Hibiscus/InteractiveObjects/Systems/CatchARide/MI_Hib_CAR_Platform',
#    console_new_mat_override='/Hibiscus/InteractiveObjects/Systems/CatchARide/MI_Hib_CAR_Station',
#    )
config_dlc3 = Config(
    #console_obj='/Game/InteractiveObjects/GameSystemMachines/CatchARide/_Shared/Blueprints/BP_CatchARide_Console',
    #console_replace_obj='/Game/InteractiveObjects/GameSystemMachines/CatchARide/_Shared/Blueprints/BP_CatchARide_Console',
    console_obj='/Hibiscus/InteractiveObjects/Systems/CatchARide/_Design/BP_Hib_CatchARide_Console',
    console_replace_obj='/Hibiscus/InteractiveObjects/Systems/CatchARide/_Design/BP_Hib_CatchARide_Console',
    set_replaced_console_enum='DLC3',
    plat_obj='/Hibiscus/InteractiveObjects/Systems/CatchARide/_Design/BP_Hib_CatchARide_Platform',
    console_replaced_mat_override='/Hibiscus/InteractiveObjects/Systems/CatchARide/MI_Hib_CAR_Station',
    )


class Coord:
    """
    A single "coordinate" (which actually consists of location, rotation, and scale)
    The individual modification types may not use all of these -- for instance, Hook
    only uses location and rotation.
    """

    def __init__(self, loc, rot, scale=(1,1,1)):
        self.loc = loc
        self.rot = rot
        self.scale = scale


class Modification:
    """
    Base modification class to provide some common functions
    """

    label = 'REPLACE ME'

    def __init__(self, desc, hook_console=None, hook_platform=None):
        self.desc = desc
        self.hook_console = hook_console
        self.hook_platform = hook_platform

    def set_plat_mat_override(self, mod, config, map_last, platform):
        if config.platform_mat_override:
            mat_val = mod.get_full_cond(config.platform_mat_override, 'MaterialInstanceConstant')
        else:
            mat_val = ''
        mod.reg_hotfix(Mod.LEVEL, map_last,
                '{}.PlatformMesh'.format(platform),
                'OverrideMaterials',
                '({})'.format(mat_val))

    def set_console_mat_override(self, mod, config, map_last, console, material):
        if material:
            mat_val = mod.get_full_cond(material, 'MaterialInstanceConstant')
        else:
            mat_val = 'None'
        # The Console_Proxy object we need isn't predictably named (or at least not
        # practically so), so we'll just abuse some .Object.. stuff to get there
        # instead.
        mod.reg_hotfix(Mod.LEVEL, map_last,
                console,
                'LocalProxies.LocalProxies[0].Object..SM_CatchARide_Console_V3.Object..OverrideMaterials.OverrideMaterials[0]',
                mat_val)

    #def add_new_console(self, mod, config, map_path, map_last, coords, scale_param=0.75):
    def add_new_console(self, mod, config, map_path, map_last, coords):
        """
        I'd really like for these new consoles to be a bit smaller than the "main" ones, just
        as a bit of visual indicator that they're the new ones, but I cannot for the life of
        me get it to work.  Setting the scaling parameter on the streaming_hotfix call *does*
        seem to resize the interactive elements of the CAR console (though they don't seem
        to line up the way I'd expect them to), but the console itself remains unchanged.

        There's access to a few more RelativeScale3D attrs via some objects off of the
        Console_Proxy (which we use to override the material, above), both under
        SM_CatchARide_Console_V3 and DefaultSceneRoot, but neither of those seem to have
        any impact either.  In all cases, the actual attrs do get updated properly, but the
        object just doesn't resize.  Basically all other objects that I've tried scaling
        on work fine, so I think it's something particular to the CAR consoles.
        """
        new_console = mod.streaming_hotfix(map_path,
                config.console_obj,
                location=(coords.loc[0], coords.loc[1], coords.loc[2]-config.z_nudge_console),
                rotation=coords.rot,
                #scale=(scale_param, scale_param, scale_param),
                )

        # Set its Material Override
        self.set_console_mat_override(mod, config, map_last, new_console, config.console_new_mat_override)

        # Return the new object name
        return new_console

class New(Modification):
    """
    A brand new Console + Platform pair.  Only one platform here!
    This is sort of deprecated in favor of Replace, below.  Note that
    this is currently hardcoded to set up the platform at 60% its usual
    size, since it's 1) often difficult to find space to put a new
    platform, and 2) I'd started out just using it for Jetbeasts, where
    it makes sense.  If I start using this elsewhere again, that scaling
    should probably be abstracted a bit so it doesn't look weird for
    "regular" vehicles.
    """

    label = 'New Console/Platform Pair'

    def __init__(self, desc, console, plat, hook_console=None, hook_platform=None):
        """
        `console` is a `Coord` object describing where to put the new console
        `plat` is a `Coord` object describing where to put the new platform
        """
        super().__init__(desc, hook_console, hook_platform)
        self.console = console
        self.plat = plat

    def process(self, map_path, map_base_path, map_last, config, mod):
        new_console = self.add_new_console(mod, config, map_path, map_last, self.console)
        new_plat = mod.streaming_hotfix(map_path,
                config.plat_obj,
                location=(self.plat.loc[0], self.plat.loc[1], self.plat.loc[2]-config.z_nudge_plat),
                rotation=self.plat.rot,
                scale=(.6, .6, .6))
        self.set_plat_mat_override(mod, config, map_last, new_plat)
        mod.reg_hotfix(Mod.LEVEL, map_last,
                new_console,
                'CatchARide_Platform1',
                mod.get_full_cond(new_plat, 'BP_CatchARide_Platform_C'))

        # Return the new console + platform names
        return ([new_console], [new_plat])


class Hook(Modification):
    """
    A new console which hooks into existing platforms.
    """

    label = 'Existing-Platform Hook'

    def __init__(self, desc, console, plat1, plat2=None, orig_console=None, hook_console=None, hook_platform=None):
        """
        `console` is a `Coord` object describing where to put our new console
        `plat1` and `plat2` are the "short" object names for the platforms we'll
            hook into, which we know are in `<mapname>_P` since otherwise we
            couldn't hook to them.  The full paths will be constructed during
            process() time, since we're passed the map path info at that time.
        `orig_console` is the "short" name of the existing CAR console.  If this
            is specified, then we'll make sure to enforce its material, even
            though we're otherwise leaving it alone.
        """
        super().__init__(desc, hook_console, hook_platform)
        self.console = console
        self.plat1 = plat1
        self.plat2 = plat2
        self.orig_console = orig_console

    def process(self, map_path, map_base_path, map_last, config, mod):
        new_console = self.add_new_console(mod, config, map_path, map_last, self.console)
        for plat_attr, plat_short in [
                ('CatchARide_Platform1', self.plat1),
                ('CatchARide_Platform2', self.plat2),
                ]:
            if plat_short:
                mod.reg_hotfix(Mod.LEVEL, map_last,
                        new_console,
                        plat_attr,
                        mod.get_full_cond('{}.{}:PersistentLevel.{}'.format(
                            map_path,
                            map_last,
                            plat_short,
                            ), 'BP_CatchARide_Platform_C'))

        # Also update the original console's material, if we've been told to.
        if self.orig_console:
            full_console = '{}.{}:PersistentLevel.{}'.format(
                    map_path,
                    map_last,
                    self.orig_console,
                    )
            self.set_console_mat_override(mod, config, map_last, full_console, config.console_replaced_mat_override)

        # Return our new console name
        return ([new_console], [])

class Replace(Modification):
    """
    Replacing an existing Console+Platforms setup with our own objects, so that
    we don't have to try and fit in a new platform somewhere.
    """

    label = 'Full Replacement + New Console'

    def __init__(self, desc, console, console_coord, console_new,
            plat1, plat1_coord,
            plat2=None, plat2_coord=None,
            hook_console=None, hook_platform=None):
        """
        `console` is the full object path to the existing console
        `console_coord` is a `Coord` object describing where that console used to be
        `console_new` is a `Coord` object decribing where our "new" console should be placed
        `plat1` and `plat2` are the "short" object names of the existing platforms, in the same
            level "namespace" as the console
        `plat1_coord` and `plat2_coord` are the `Coord` objects describing where the platforms
            used to be

        `plat2` and `plat2_coord` are optional
        """
        super().__init__(desc, hook_console, hook_platform)
        self.console = console
        self.console_coord = console_coord
        self.console_new = console_new
        self.plat1 = plat1
        self.plat1_coord = plat1_coord
        self.plat2 = plat2
        self.plat2_coord = plat2_coord

    def process(self, map_path, map_base_path, map_last, config, mod):

        # First move the old one super far away
        old_base_path = self.console.split(':PersistentLevel.', 1)[0]
        to_loop = [
                '{}.RootComponent'.format(self.console),
                '{}:PersistentLevel.{}.PlatformMesh'.format(old_base_path, self.plat1),
                ]
        if self.plat2:
            to_loop.append(('{}:PersistentLevel.{}.PlatformMesh'.format(old_base_path, self.plat2)))
        for obj_path in to_loop:
            # Platforms can be moved with regular LEVEL, but consoles seem to require EARLY.
            # Just use EARLY for all of 'em.
            mod.reg_hotfix(Mod.EARLYLEVEL, map_last,
                    obj_path,
                    'RelativeLocation',
                    '(X=-1000000,Y=-1000000,Z=-1000000)',
                    notify=True)

        # Now replace with our own console
        replaced_console = mod.streaming_hotfix(map_path,
                config.console_replace_obj,
                location=self.console_coord.loc,
                rotation=self.console_coord.rot,
                scale=self.console_coord.scale)
        self.set_console_mat_override(mod, config, map_last, replaced_console, config.console_replaced_mat_override)

        # ... and our *actual* "new" console
        new_console = self.add_new_console(mod, config, map_path, map_last, self.console_new)

        # And new platform(s)
        new_plats = []
        for coord in [self.plat1_coord, self.plat2_coord]:
            if coord:
                new_plats.append(mod.streaming_hotfix(map_path,
                    config.plat_obj,
                    location=coord.loc,
                    rotation=coord.rot,
                    scale=coord.scale))

        # If we need to change the RestrictionType on our replaced console,
        # do so now.
        if config.set_replaced_console_enum:
            mod.reg_hotfix(Mod.LEVEL, map_last,
                    replaced_console,
                    'RestrictionType',
                    config.set_replaced_console_enum)

        # Remnants of doing a joke where I flipped the platforms upside down.  lols, etc.
        # I can't get this method to work consistently on our second "new" console, for
        # whatever reason.  It did seem to work when I'd done the upside-down platform
        # thing.  Perhaps it only works on both if they're set to the same values...
        #mod.reg_hotfix(Mod.LEVEL, map_last,
        #        replaced_console,
        #        'DeploymentLocationOffset',
        #        '(X=0,Y=0,Z=-177)')

        # Hook the consoles up to our new platforms
        for idx, new_plat in enumerate(new_plats):
            full_ref = mod.get_full_cond(new_plat, 'BP_CatchARide_Platform_C')
            mod.reg_hotfix(Mod.LEVEL, map_last,
                    replaced_console,
                    'CatchARide_Platform{}'.format(idx+1),
                    full_ref)
            mod.reg_hotfix(Mod.LEVEL, map_last,
                    new_console,
                    'CatchARide_Platform{}'.format(idx+1),
                    full_ref)

            # Also set our platform override materials
            self.set_plat_mat_override(mod, config, map_last, new_plat)

        # Return the new console + platform names
        return ([replaced_console, new_console], new_plats)

###
### Class to assist with handling respawn stations
###

class Respawner:

    def __init__(self, label, map_base_path, map_last, spawner_name):
        self.label = label
        self.map_base_path = map_base_path
        self.map_last = map_last
        self.spawner_name = spawner_name
        self.consoles = []

respawners = [
        # Biofuel Rig
        Respawner("The Droughts", '/Game/Maps/Zone_0/Prologue', 'Prologue_P',
            'Prologue_M_Ep04_EarnSpaceship.Prologue_M_Ep04_EarnSpaceship:PersistentLevel.OakMissionVehicleSpawner_EllieBiofuelRig'),
        # Project DD
        Respawner("Neon Arterial", '/Game/Maps/Zone_1/CityVault', 'CityVault_P',
            'CityVault_M_LastStop.CityVault_M_LastStop:PersistentLevel.OakMissionVehicleSpawner_MayaTruck_Default'),
        # Prisa's Outrunner
        Respawner("Floodmoor Basin", '/Game/Maps/Zone_2/Wetlands', 'Wetlands_P',
            'Wetlands_M_DriveAwayThePain.Wetlands_M_DriveAwayThePain:PersistentLevel.OakMissionVehicleSpawner_DriveAwayThePain'),
        # Golden Chariot
        Respawner("Splinterlands", '/Game/Maps/Zone_3/Motorcade', 'Motorcade_P',
            'Motorcade_M_Plot.Motorcade_M_Plot:PersistentLevel.OakMissionVehicleSpawner_GoldenChariot'),
        # Vaughn's Technical
        Respawner("Sandblast Scar", '/Game/Maps/Zone_3/Convoy', 'Convoy_P',
            'Convoy_M_Plot.Convoy_M_Plot:PersistentLevel.OakMissionVehicleSpawner_Convoy'),
        ]

###
### Hooks - Extra processing that needs to be done for some consoles/platforms
###

def add_respawner_console(mod, config, map_path, map_base_path, map_last, new_console):
    global respawners
    for respawner in respawners:
        if map_base_path == respawner.map_base_path:
            respawner.consoles.append(new_console)
            return
    raise RuntimeError('No respawner found for: {}'.format(new_console))

def droughts_console_trigger_plot(mod, config, map_path, map_base_path, map_last, new_console):
    """
    Make sure that this console is usable to advance the first-vehicle plot.
    """
    mod.reg_hotfix(Mod.LEVEL, map_last,
            new_console,
            'PlayerBeginInteraction',
            '(Prologue_Dynamic_C_1.BndEvt__BP_CatchARide_Console_66_K2Node_ActorBoundEvent_24_PlayerBeginInteraction__DelegateSignature)')

def droughts_lock_before_ellie(mod, config, map_path, map_base_path, map_last, new_console):
    """
    Lock this CAR console until we've done the Ellie quest to unlock vehicles generally.

    I was originally thinking that these had a different lock timing than the others in
    the area (hence this function plus `droughts_lock_ellie_station` below), but honestly
    I could probably combine 'em into one without any loss/change of functionality.
    Still, I've already tested with this configuration, so changing it's more trouble
    than it's worth now.
    """
    mod.reg_hotfix(Mod.LEVEL, map_last,
            '{}.DefaultUsableComponent'.format(new_console),
            'EnabledCondition',
            mod.get_full_cond('/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_CatchARide_Console_Sacrifice.DefaultUsableComponent.EnabledCondition_MissionEnableConditionObjective', 'MissionEnableConditionObjective'))

    # Also let this console trigger the first-vehicle plot
    droughts_console_trigger_plot(mod, config, map_path, map_base_path, map_last, new_console)

def droughts_lock_ellie_station(mod, config, map_path, map_base_path, map_last, new_console):
    """
    Lock Ellie's CAR console until we're ready to do the first vehicle activation,
    and make sure it's hooked up to advance the plot mission

    I was originally thinking that these had a different lock timing than the others in
    the area (hence this function plus `droughts_lock_before_ellie` above), but honestly
    I could probably combine 'em into one without any loss/change of functionality.
    Still, I've already tested with this configuration, so changing it's more trouble
    than it's worth now.
    """

    # Disable until we're ready
    mod.reg_hotfix(Mod.LEVEL, map_last,
            '{}.DefaultUsableComponent'.format(new_console),
            'EnabledCondition',
            mod.get_full_cond('/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_CatchARide_Console_Ellies.DefaultUsableComponent.EnabledCondition_MissionEnableConditionObjective', 'MissionEnableConditionObjective'))

    # Also let this console trigger the first-vehicle plot
    droughts_console_trigger_plot(mod, config, map_path, map_base_path, map_last, new_console)

def droughts_platform(mod, config, map_path, map_base_path, map_last, new_platform):
    """
    Makes sure that the platforms in The Droughts can scan in the first
    stolen outrunner properly
    """
    mod.reg_hotfix(Mod.LEVEL, map_last,
            new_platform,
            'VehicleScanned',
            '(Prologue_Dynamic_C_1.BndEvt__BP_CatchARide_Platform_ElliesLeft_K2Node_ActorBoundEvent_4_VehicleScanned__DelegateSignature)')

def add_droughts_fuel_spawn(mod, config, map_path, map_base_path, map_last, new_console):
    """
    Make sure that this console can be used to respawn the fueling Technical, and
    also is locked until the appropriate point in the plot.
    """

    # Add as a valid respawner
    add_respawner_console(mod, config, map_path, map_base_path, map_last, new_console)

    # Adjust the usability to be locked where appropriate, too
    mod.reg_hotfix(Mod.LEVEL, map_last,
            '{}.DefaultUsableComponent'.format(new_console),
            'EnabledCondition',
            mod.get_full_cond('/Game/Maps/Zone_0/Prologue/Prologue_M_Ep04_EarnSpaceship.Prologue_M_Ep04_EarnSpaceship:PersistentLevel.BP_CatchARide_Console_OutsideShip.DefaultUsableComponent.MissionEnableConditionObjective_0', 'MissionEnableConditionObjective'))

    # Also let this console trigger the first-vehicle plot
    droughts_console_trigger_plot(mod, config, map_path, map_base_path, map_last, new_console)

def sanctuary_disable_spawned(mod, config, map_path, map_base_path, map_last, new_console):
    """
    Vehicles spawned in Sanctuary shouldn't actually be driveable
    """
    mod.reg_hotfix(Mod.LEVEL, map_last,
            new_console,
            'OnVehicleSpawned',
            '(Sanctuary3_P_C_0.OnVehicleSpawned_Event_0)')

def meridian_metroplex_gate_open(mod, config, map_path, map_base_path, map_last, new_console):
    """
    Make sure that spawning a vehicle from this station triggers the opening of the garage
    """
    mod.reg_hotfix(Mod.LEVEL, map_last,
            new_console,
            'OnVehicleSpawned',
            '(City_M_OvercomeHQBlockade_C_2.BndEvt__BP_CatchARide_Console_8_K2Node_ActorBoundEvent_0_OnVehicleSpawned__DelegateSignature)')

def blastplains_endgame_spawn(mod, config, map_path, map_base_path, map_last, new_console):
    """
    Make sure that spawning a vehicle from this station triggers the ride-to-Crater's-Edge
    """
    mod.reg_hotfix(Mod.LEVEL, map_last,
            new_console,
            'OnVehicleSpawned',
            '(cm_testFrontier_C_0.BndEvt__BP_CatchARide_Console_Ger_6_K2Node_ActorBoundEvent_0_OnVehicleSpawned__DelegateSignature)')

def desolation_power_on(mod, config, map_path, map_base_path, map_last, new_console):
    """
    Lock this console until the power gets turned on, as part of the first
    plot steps in the area.
    """
    mod.reg_hotfix(Mod.LEVEL, map_last,
            '{}.DefaultUsableComponent'.format(new_console),
            'EnabledCondition',
            mod.get_full_cond('/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_CatchARide_Console_Mission.DefaultUsableComponent.EnabledCondition_MissionEnableConditionObjective', 'MissionEnableConditionObjective'))

###
### Now get some work done!
###

for map_label, map_path, config, modifications in [

        ("The Droughts", '/Game/Maps/Zone_0/Prologue/Prologue_P', config_reg, [

            # We've got to do a fair bit of extra work here to make sure that the
            # consoles/platforms work properly for both the first-vehicle quest
            # and to respawn the fueling Technical.

            Replace("Outside Crimson Command",
                console='/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_CatchARide_Console_Recruitment',
                console_coord=Coord(loc=(-18917.982422, 14785.464844, 158.000168), rot=(0, 174.999908, 0)),
                console_new=Coord(loc=(-18318, 13487, 188), rot=(0, -90, 0)),
                plat1='BP_CatchARide_Platform_0',
                plat1_coord=Coord(loc=(-18483.882813, 14491.816406, 70.068481), rot=(0, 46.816319, 0)),
                plat2='BP_CatchARide_Platform_1089',
                plat2_coord=Coord(loc=(-17426.142578, 14065.506836, 70.068481), rot=(0, 46.816319, 0)),
                hook_console=droughts_lock_before_ellie,
                hook_platform=droughts_platform,
                ),

            Replace("Outside Ellie's",
                console='/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_CatchARide_Console_Ellies',
                console_coord=Coord(loc=(-15247.887695, 29855.195313, 332.650360), rot=(0, 77.892914, 0)),
                console_new=Coord(loc=(-15465, 28850, 423), rot=(0, -102.107086, 0)),
                plat1='BP_CatchARide_Platform_ElliesLeft_0',
                plat1_coord=Coord(loc=(-15842.166016, 29504.115234, 321.027130), rot=(0, -101.639511, 0)),
                plat2='BP_CatchARide_Platform_ElliesRight_1',
                plat2_coord=Coord(loc=(-14841.286133, 29299.837891, 320.013519), rot=(0, 258.360962, 0)),
                hook_console=droughts_lock_ellie_station,
                hook_platform=droughts_platform,
                ),

            Replace("Exit to Ascension Bluff",
                console='/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_CatchARide_Console_Sacrifice',
                console_coord=Coord(loc=(78674.523438, 54614.421875, -3154.181152), rot=(0, 183.532547, 0)),
                console_new=Coord(loc=(78766, 55638, -3056), rot=(0, 138.532547, 0)),
                plat1='BP_CatchARide_Platform_8',
                plat1_coord=Coord(loc=(79201.539063, 54879.988281, -3170), rot=(0, -90.000038, 0)),
                plat2='BP_CatchARide_Platform_9',
                plat2_coord=Coord(loc=(80192.500000, 54880, -3170), rot=(0, -90.000038, 0)),
                hook_console=droughts_lock_before_ellie,
                hook_platform=droughts_platform,
                ),

            Replace("Highway Fast Travel",
                console='/Game/Maps/Zone_0/Prologue/Prologue_M_Ep04_EarnSpaceship.Prologue_M_Ep04_EarnSpaceship:PersistentLevel.BP_CatchARide_Console_RestStop',
                console_coord=Coord(loc=(48143.566406, 22779.843750, -3885.288330), rot=(-6.726149, 163.662720, 1.716420)),
                console_new=Coord(loc=(48002, 21661, -3741), rot=(0, -151.33728, 0)),
                plat1='BP_CatchARide_Platform_2',
                plat1_coord=Coord(loc=(48781.031250, 22086.375000, -3877.631104), rot=(-0.048464, 162.308777, 0)),
                plat2='BP_CatchARide_Platform_140',
                plat2_coord=Coord(loc=(49039.128906, 22990.707031, -3874.513428), rot=(-0.285536, 164.855835, 0.540241)),
                hook_console=add_droughts_fuel_spawn,
                hook_platform=droughts_platform,
                ),

            Replace("Near exit to Devil's Razor",
                console='/Game/Maps/Zone_0/Prologue/Prologue_M_Ep04_EarnSpaceship.Prologue_M_Ep04_EarnSpaceship:PersistentLevel.BP_CatchARide_Console_Desert',
                console_coord=Coord(loc=(83352, 6544, -2905.500000), rot=(0, -49.637501, 0)),
                console_new=Coord(loc=(83046, 6378, -2704), rot=(0, -139.637501, 0)),
                plat1='BP_CatchARide_Platform_3',
                plat1_coord=Coord(loc=(82645, 7082, -2929), rot=(0, 0, 0)),
                plat2='BP_CatchARide_Platform_4',
                plat2_coord=Coord(loc=(82621, 8088, -2937), rot=(0, 0, 0)),
                hook_console=add_droughts_fuel_spawn,
                hook_platform=droughts_platform,
                ),

            Replace("West of Sanctuary Berth",
                console='/Game/Maps/Zone_0/Prologue/Prologue_M_Ep04_EarnSpaceship.Prologue_M_Ep04_EarnSpaceship:PersistentLevel.BP_CatchARide_Console_BelowShip',
                console_coord=Coord(loc=(22278.423828, 23791.894531, 4282.797852), rot=(0, 127.840416, 0)),
                console_new=Coord(loc=(22037, 21958, 4379), rot=(0, -167.159584, 0)),
                plat1='BP_CatchARide_Platform_5',
                plat1_coord=Coord(loc=(22781.148438, 23233.181641, 4252.668457), rot=(-1.776620, 355.656158, -0.374385)),
                # Interestingly, the second platform isn't actually hooked up, on the stock CAR console!
                plat2='BP_CatchARide_Platform_7',
                plat2_coord=Coord(loc=(22712.23, 22322.115, 4261.6895), rot=(-1.776620, 355.656158, 1.171227)),
                hook_console=add_droughts_fuel_spawn,
                hook_platform=droughts_platform,
                ),

            Replace("East of Sanctuary Berth",
                console='/Game/Maps/Zone_0/Prologue/Prologue_M_Ep04_EarnSpaceship.Prologue_M_Ep04_EarnSpaceship:PersistentLevel.BP_CatchARide_Console_OutsideShip',
                console_coord=Coord(loc=(19430.597656, 43101.695313, 4560), rot=(0, -47.563484, 0)),
                console_new=Coord(loc=(19383, 42558, 4658), rot=(0, 37.269554, 0)),
                plat1='BP_CatchARide_Platform_0',
                plat1_coord=Coord(loc=(18939.306641, 42931.300781, 4560), rot=(0, 82.730446, 0)),
                plat2='BP_CatchARide_Platform_1',
                plat2_coord=Coord(loc=(18027.310547, 43052.402344, 4560), rot=(0, 82.257034, 0)),
                hook_console=add_droughts_fuel_spawn,
                hook_platform=droughts_platform,
                ),

            ]),

        ("Ascension Bluff", '/Game/Maps/Zone_0/Sacrifice/Sacrifice_P', config_reg, [

            Replace("At entrance of level / exit to The Droughts",
                console='/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_CatchARide_Console_8',
                console_coord=Coord(loc=(50442.578125, -32399.447266, 13255.998047), rot=(0, 257.989105, 0)),
                console_new=Coord(loc=(52198, -31694, 13385), rot=(10, -12, 0)),
                plat1='BP_CatchARide_Platform_8',
                plat1_coord=Coord(loc=(50979.394531, -32050.617188, 13229.316406), rot=(0.000123, 140.893524, -0.000031)),
                plat2='BP_CatchARide_Platform_9',
                plat2_coord=Coord(loc=(51603.882813, -31282.394531, 13229.316406), rot=(0.000007, 140.893784, 0.000024)),
                ),

            Replace("Near Outrunner Hijack target outpost",
                console='/Game/Maps/Zone_0/Sacrifice/Sacrifice_Terrain.Sacrifice_Terrain:PersistentLevel.BP_CatchARide_Console_8',
                console_coord=Coord(loc=(48451.781250, 7815.903320, 10896), rot=(0, 429.374634, 0)),
                console_new=Coord(loc=(47256, 8305, 10972), rot=(0, 174.64386, 0)),
                plat1='BP_CatchARide_Platform_9',
                plat1_coord=Coord(loc=(47777.941406, 7908.291016, 10885), rot=(0.000041, 264.643860, 0.000020)),
                ),

            Replace("Near Bandit encampment",
                console='/Game/Maps/Zone_0/Sacrifice/Sacrifice_Terrain.Sacrifice_Terrain:PersistentLevel.BP_CatchARide_Console_0',
                console_coord=Coord(loc=(91402.500000, 12278.938477, 10078), rot=(0, 427.499481, 0)),
                console_new=Coord(loc=(91171, 12837, 10166), rot=(0, -22, 0)),
                plat1='BP_CatchARide_Platform_0',
                plat1_coord=Coord(loc=(90772.453125, 12033.593750, 10056.008789), rot=(0.000041, 292.768921, 0.000020)),
                ),

            Replace("Gateway to Holy Broadcast Center",
                console='/Game/Maps/Zone_0/Sacrifice/Sacrifice_Terrain.Sacrifice_Terrain:PersistentLevel.BP_CatchARide_Console_192',
                console_coord=Coord(loc=(70439.250000, 43618.105469, 11638), rot=(0, -126.563309, 0)),
                console_new=Coord(loc=(71167, 44603, 11729), rot=(0, 53.436691, 0)),
                plat1='BP_CatchARide_Platform_5809',
                plat1_coord=Coord(loc=(71264.796875, 43895.554688, 11619), rot=(0.000041, -126.293793, 0.000020)),
                plat2='BP_CatchARide_Platform_5808',
                plat2_coord=Coord(loc=(70466.867188, 44481.597656, 11619), rot=(0.000123, -126.294159, -0.000092)),
                ),

            ]),

        ("Sandblast Scar", '/Game/Maps/Zone_3/Convoy/Convoy_P', config_reg, [

            Replace("At level start",
                console='/Game/Maps/Zone_3/Convoy/Convoy_M_Plot.Convoy_M_Plot:PersistentLevel.BP_CatchARide_Console_START',
                console_coord=Coord(loc=(-86050.687500, 16312.919922, -2542.527832), rot=(0, -43.491669, 0)),
                console_new=Coord(loc=(-86584, 16813, -2452), rot=(0, 136.508331, 0)),
                plat1='BP_CatchARide_Platform_168',
                plat1_coord=Coord(loc=(-85881.968750, 17030.068359, -2545.958252), rot=(0, -44.111977, 0)),
                plat2='BP_CatchARide_Platform_4',
                plat2_coord=Coord(loc=(-86770.062500, 16105.588867, -2545.958252), rot=(0, -44.111977, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("Shortly after drop into canyon",
                console='/Game/Maps/Zone_3/Convoy/Convoy_M_Plot.Convoy_M_Plot:PersistentLevel.BP_CatchARide_Console_CAR',
                console_coord=Coord(loc=(-29846.091797, 22479.679688, -5090.051270), rot=(0, -89.999901, 0)),
                console_new=Coord(loc=(-29843, 23499, -5002), rot=(0, 90, 0)),
                plat1='BP_CatchARide_Platform',
                plat1_coord=Coord(loc=(-29348.283203, 22968.857422, -5094.676270), rot=(0, -89.999786, 0)),
                plat2='BP_CatchARide_Platform_72',
                plat2_coord=Coord(loc=(-30336.734375, 22963.857422, -5092.948730), rot=(0, -89.999756, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("After first dogleg / first encampment",
                console='/Game/Maps/Zone_3/Convoy/Convoy_M_Plot.Convoy_M_Plot:PersistentLevel.BP_CatchARide_Console_3',
                console_coord=Coord(loc=(12050.456055, 2189.174561, 560.348511), rot=(0, -176.977081, 0)),
                console_new=Coord(loc=(11964, 1044, 652), rot=(0, -86.977081, 0)),
                plat1='BP_CatchARide_Platform_2',
                plat1_coord=Coord(loc=(11431.149414, 1620.923340, 535.350403), rot=(0, -177.687988, 0)),
                plat2='BP_CatchARide_Platform_3',
                plat2_coord=Coord(loc=(11386.741211, 2686.579346, 535.350403), rot=(0, -176.977081, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("After first encampment ramp",
                console='/Game/Maps/Zone_3/Convoy/Convoy_M_Plot.Convoy_M_Plot:PersistentLevel.BP_CatchARide_Console_CAR_0',
                console_coord=Coord(loc=(32452.630859, 16532.500000, 4595), rot=(0, -120.000122, 0)),
                console_new=Coord(loc=(32187, 16881, 4678), rot=(0, 105, 0)),
                plat1='BP_CatchARide_Platform_81',
                plat1_coord=Coord(loc=(32653.134766, 15768.477539, 4581.827637), rot=(0, -118.297043, 0)),
                plat2='BP_CatchARide_Platform_90',
                plat2_coord=Coord(loc=(31696.082031, 16247.691406, 4581.827637), rot=(0, -115.444397, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("In Tunnel",
                console='/Game/Maps/Zone_3/Convoy/Convoy_M_Plot.Convoy_M_Plot:PersistentLevel.BP_CatchARide_Console_CAR_3',
                console_coord=Coord(loc=(69637.054688, -46207.046875, 7449.103516), rot=(0, -47.689529, 0)),
                console_new=Coord(loc=(68970, -45518, 7537), rot=(0, 132.310471, 0)),
                plat1='BP_CatchARide_Platform_99',
                plat1_coord=Coord(loc=(69667.484375, -45531.835938, 7440.857422), rot=(0, -45.946106, 0)),
                plat2='BP_CatchARide_Platform_108',
                plat2_coord=Coord(loc=(68960.648438, -46205.203125, 7440.856934), rot=(0, -45.960205, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("Cliffside Dogleg",
                console='/Game/Maps/Zone_3/Convoy/Convoy_M_Plot.Convoy_M_Plot:PersistentLevel.BP_CatchARide_Console_CAR_2',
                console_coord=Coord(loc=(88197.171875, -102635.906250, 13558.038086), rot=(0, 89.843521, 0)),
                console_new=Coord(loc=(87524, -102151, 13663), rot=(0, 44.843521, 0)),
                plat1='BP_CatchARide_Platform_126',
                plat1_coord=Coord(loc=(88688.492188, -103125.789063, 13525.613281), rot=(0, -89.999695, 0)),
                plat2='BP_CatchARide_Platform_117',
                plat2_coord=Coord(loc=(87717.882813, -103131.156250, 13530.362305), rot=(0, -89.999695, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("Before Main Encampment",
                console='/Game/Maps/Zone_3/Convoy/Convoy_M_Plot.Convoy_M_Plot:PersistentLevel.BP_CatchARide_Console_CAR_1',
                console_coord=Coord(loc=(60907.933594, -84954.820313, 19980), rot=(0, 44.716587, 0)),
                console_new=Coord(loc=(60221, -85665, 20092), rot=(0, 44.716587, 0)),
                plat1='BP_CatchARide_Platform_25',
                plat1_coord=Coord(loc=(60211.703125, -84953.562500, 19974.035156), rot=(0, 45.420197, 0)),
                plat2='BP_CatchARide_Platform_24',
                plat2_coord=Coord(loc=(60887.425781, -85675.718750, 19974.779297), rot=(0, 45.420197, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("Level End",
                console='/Game/Maps/Zone_3/Convoy/Convoy_M_Plot.Convoy_M_Plot:PersistentLevel.BP_CatchARide_Console_END',
                console_coord=Coord(loc=(86861.492188, -156675.750000, 18209.642578), rot=(0, 77.616112, 0)),
                console_new=Coord(loc=(86667, -157622, 18303), rot=(0, -102.383888, 0)),
                plat1='BP_CatchARide_Platform_0',
                plat1_coord=Coord(loc=(86276.273438, -157052.656250, 18195.423828), rot=(0, 78.319969, 0)),
                plat2='BP_CatchARide_Platform_1',
                plat2_coord=Coord(loc=(87235.843750, -157292.015625, 18196.167969), rot=(0, 78.319969, 0)),
                hook_console=add_respawner_console,
                ),

            ]),

        ("Devil's Razor", '/Game/Maps/Zone_3/Desert/Desert_P', config_reg, [

            Replace("Roland's Rest",
                console='/Game/Maps/Zone_3/Desert/Desert_POI_HubTown.Desert_POI_HubTown:PersistentLevel.BP_CatchARide_Console_8',
                console_coord=Coord(loc=(-11125.643555, -28666.228516, 3758.926025), rot=(0, -122.855423, 0)),
                console_new=Coord(loc=(-11089, -29289, 3846), rot=(0, -110, 0)),
                plat1='BP_CatchARide_Platform_9',
                plat1_coord=Coord(loc=(-11008.742188, -27553.095703, 3602.077637), rot=(0, 57.144623, 0)),
                plat2='BP_CatchARide_Platform_8',
                plat2_coord=Coord(loc=(-10130.604492, -28132.136719, 3602.077637), rot=(0, 57.144623, 0)),
                ),

            Replace("Near exit to Cathedral of the Twin Gods",
                console='/Game/Maps/Zone_3/Desert/Desert_POI_VaultEntrance.Desert_POI_VaultEntrance:PersistentLevel.BP_CatchARide_Console_290',
                console_coord=Coord(loc=(-11253.223633, 13585.142578, -50.998188), rot=(0, 102.407135, 0)),
                console_new=Coord(loc=(-10775, 13722, 41), rot=(0, 147.407135, 0)),
                plat1='BP_CatchARide_Platform_210',
                plat1_coord=Coord(loc=(-10609.001953, 12924.845703, -170.656982), rot=(0, -75.997948, 0)),
                plat2='BP_CatchARide_Platform_223',
                plat2_coord=Coord(loc=(-11550.184570, 12690.171875, -155.430725), rot=(0, -75.997948, 0)),
                ),

            Hook("Near ECHONet Hub 37",
                console=Coord(loc=(11759, -29311, 4015), rot=(0, -100, 0)),
                plat1='BP_CatchARide_Platform_2',
                plat2='BP_CatchARide_Platform_3'),

            Hook("Near the exit to Splinterlands and Sheega's place",
                console=Coord(loc=(41630, -11028, 5331), rot=(0, 76.863483, 0)),
                plat1='BP_CatchARide_Platform_29',
                plat2='BP_CatchARide_Platform_28'),

            Hook("Across from Boomtown",
                console=Coord(loc=(34105, 12259, 4943), rot=(0, 0, 0)),
                plat1='BP_CatchARide_Platform_27',
                plat2='BP_CatchARide_Platform_26'),

            Hook("Near the exit to The Droughts",
                console=Coord(loc=(12064, 25140, -88), rot=(0, 135, 0)),
                plat1='BP_CatchARide_Platform_31',
                plat2='BP_CatchARide_Platform_30'),

            Hook("Near the bridge to Hirschim/Grace's place, and Dental Dan's Mouth House",
                console=Coord(loc=(-1553, 36846, 457), rot=(0, -69, 0)),
                plat1='BP_CatchARide_Platform_25',
                plat2='BP_CatchARide_Platform_24'),

            Hook("Center of the map, ish, ner Antalope",
                console=Coord(loc=(6482, -5035, 77), rot=(0, 0, 0)),
                plat1='BP_CatchARide_Platform_1',
                plat2='BP_CatchARide_Platform_0'),

            ]),

        ("Cathedral of the Twin Gods", '/Game/Maps/Zone_3/DesertVault/Desertvault_P', config_reg, [

            Replace("Near Fast Travel / Entrance to Cathedral Itself",
                console='/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.BP_CatchARide_Console_3',
                console_coord=Coord(loc=(24239.160156, 12281.646484, 7547.016113), rot=(0, 0.000244, 0)),
                console_new=Coord(loc=(24794, 13384, 7618), rot=(5, 45, 0)),
                plat1='BP_CatchARide_Platform_6',
                plat1_coord=Coord(loc=(23826.220703, 12764.712891, 7552.276367), rot=(0, 0.000092, 0)),
                plat2='BP_CatchARide_Platform_7',
                plat2_coord=Coord(loc=(23826.033203, 11806.170898, 7553.959961), rot=(0, 0.000092, 0)),
                ),

            Replace("Before makeshift bridge (near Radio challenge)",
                console='/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.BP_CatchARide_Console_1',
                console_coord=Coord(loc=(-1958.780029, -7428.983887, 3222.500000), rot=(0, 1.250339, 0)),
                console_new=Coord(loc=(-2504, -6321, 3306), rot=(0, 91.250339, 0)),
                plat1='BP_CatchARide_Platform_4',
                plat1_coord=Coord(loc=(-2496.468018, -6867.816895, 3197.500000), rot=(0, 1.250161, 0)),
                plat2='BP_CatchARide_Platform_5',
                plat2_coord=Coord(loc=(-2450.109863, -7937.584473, 3197.500000), rot=(0, 1.250161, 0)),
                ),

            Replace("Overlooking Cathedral, near giant skeletons",
                console='/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.BP_CatchARide_Console_0',
                console_coord=Coord(loc=(-21021.310547, -37238.085938, 5937.253418), rot=(0, 223.048050, 0)),
                console_new=Coord(loc=(-22187, -37839, 6157), rot=(0, 178.04805, 0)),
                plat1='BP_CatchARide_Platform_0',
                plat1_coord=Coord(loc=(-21125.894531, -38158.140625, 5930.592773), rot=(0, 44.599590, 0)),
                plat2='BP_CatchARide_Platform_1',
                plat2_coord=Coord(loc=(-20378.199219, -38842.925781, 5931.592773), rot=(0, 46.199810, 0)),
                ),

            Replace("Level Entrance / Exit to Devil's Razor",
                console='/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.BP_CatchARide_Console_2',
                console_coord=Coord(loc=(-60349.851563, -6168.382324, 516.200562), rot=(0, -79.999596, 0)),
                console_new=Coord(loc=(-59338, -6162, 606), rot=(0, -35, 0)),
                plat1='BP_CatchARide_Platform_2',
                plat1_coord=Coord(loc=(-59935.980469, -5650.786133, 495.808502), rot=(0, -79.999863, 0)),
                plat2='BP_CatchARide_Platform_3',
                plat2_coord=Coord(loc=(-60903.058594, -5821.309570, 495.808502), rot=(0, -79.999863, 0)),
                ),

            ]),

        ("Splinterlands", '/Game/Maps/Zone_3/Motorcade/Motorcade_P', config_reg, [

            Replace("Near exit to Devil's Razor (Pitt's Stop)",
                console='/Game/Maps/Zone_3/Motorcade/Motorcade_Travel.Motorcade_Travel:PersistentLevel.BP_CatchARide_Console_Approach',
                console_coord=Coord(loc=(64866.714844, 105512.109375, 1730.595337), rot=(0, 60.747028, 0)),
                console_new=Coord(loc=(64497, 104876, 1825), rot=(0, -120, 0)),
                plat1='BP_CatchARide_Platform_40',
                plat1_coord=Coord(loc=(64175.441406, 105559.132813, 1725.350586), rot=(0, -120.951447, 0)),
                plat2='BP_CatchARide_Platform',
                plat2_coord=Coord(loc=(65273.402344, 104934.765625, 1721.714111), rot=(0, -119.801590, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("Around the corner from The Homestead (across from Carnivora exit)",
                console='/Game/Maps/Zone_3/Motorcade/Motorcade_Travel.Motorcade_Travel:PersistentLevel.BP_CatchARide_Console_Homestead',
                console_coord=Coord(loc=(43751.910156, 66973.640625, -870.514893), rot=(0, -153.000061, 0)),
                console_new=Coord(loc=(44471, 67347, -775), rot=(0, -153, 0)),
                plat1='BP_CatchARide_Platform_0',
                plat1_coord=Coord(loc=(43949.812500, 67682.992188, -870.705933), rot=(0, -153.825806, 0)),
                plat2='BP_CatchARide_Platform_1',
                plat2_coord=Coord(loc=(44439.750000, 66693.015625, -870.705933), rot=(0, -153.825928, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("Near exit to Carnivora",
                console='/Game/Maps/Zone_3/Motorcade/Motorcade_Travel.Motorcade_Travel:PersistentLevel.BP_CatchARide_Console_FestivalEntry',
                console_coord=Coord(loc=(18803.003906, 49375.855469, 100.414490), rot=(0, 55.519951, 0)),
                console_new=Coord(loc=(18265, 48518, 192), rot=(0, -124.480049, 0)),
                plat1='BP_CatchARide_Platform_42',
                plat1_coord=Coord(loc=(18975.111328, 48625.109375, 101.725388), rot=(0, 57.429695, 0)),
                plat2='BP_CatchARide_Platform_43',
                plat2_coord=Coord(loc=(18042.064453, 49217.562500, 101.725388), rot=(0, 57.429695, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("Below Legendary Phoenix spawnpoint",
                console='/Game/Maps/Zone_3/Motorcade/Motorcade_Travel.Motorcade_Travel:PersistentLevel.BP_CatchARide_Console_RaceTrack',
                console_coord=Coord(loc=(29594.429688, 106243.445313, -1617.271362), rot=(0, 192.689560, 0)),
                console_new=Coord(loc=(30634, 105389, -1525), rot=(0, -47.31044, 0)),
                plat1='BP_CatchARide_Platform_3',
                plat1_coord=Coord(loc=(30156.234375, 105888.398438, -1644.258423), rot=(0, -168.826248, 0)),
                plat2='BP_CatchARide_Platform_2',
                plat2_coord=Coord(loc=(29979.369141, 106768.226563, -1651.608032), rot=(0, -168.826248, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("High ridge (map midpoint)",
                console='/Game/Maps/Zone_3/Motorcade/Motorcade_Travel.Motorcade_Travel:PersistentLevel.BP_CatchARide_Console_Orphanage',
                console_coord=Coord(loc=(14370.710938, 82426.398438, 1516.019287), rot=(0, -128.391190, 0)),
                console_new=Coord(loc=(14036, 83610, 1624), rot=(0, 141.60881, 0)),
                plat1='BP_CatchARide_Platform_111',
                plat1_coord=Coord(loc=(15052.735352, 82486.757813, 1488.718140), rot=(0, -128.598145, 0)),
                plat2='BP_CatchARide_Platform_336',
                plat2_coord=Coord(loc=(14273.132813, 83108.281250, 1488.718140), rot=(0, -128.598145, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("Outside theme park / roller coaster",
                console='/Game/Maps/Zone_3/Motorcade/Motorcade_Travel.Motorcade_Travel:PersistentLevel.BP_CatchARide_Console_RollerCoaster',
                console_coord=Coord(loc=(-16245.121094, 100161.687500, -3770.058350), rot=(0.000007, -90, 0)),
                console_new=Coord(loc=(-17547, 100270, -3690), rot=(0, 180, 0)),
                plat1='BP_CatchARide_Platform_1864',
                plat1_coord=Coord(loc=(-16714, 100681, -3795.000244), rot=(0, -90, 0)),
                plat2='BP_CatchARide_Platform_1691',
                plat2_coord=Coord(loc=(-15764, 100681, -3795.000244), rot=(-0.000031, -90, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("Near gushing oil pipe and Princess Tarantella field",
                console='/Game/Maps/Zone_3/Motorcade/Motorcade_Travel.Motorcade_Travel:PersistentLevel.BP_CatchARide_Console_Greaseland',
                console_coord=Coord(loc=(-22280.017578, 78629.578125, -2965.172607), rot=(0.000007, 94.121971, 0)),
                console_new=Coord(loc=(-22310, 77324, -2879), rot=(0, -130.878029, 0)),
                plat1='BP_CatchARide_Platform_4',
                plat1_coord=Coord(loc=(-21775.027344, 78145.312500, -2992.046875), rot=(0, 94.121971, 0)),
                plat2='BP_CatchARide_Platform_5',
                plat2_coord=Coord(loc=(-22722.578125, 78077.007813, -2982.131592), rot=(-0.000031, 94.121971, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("At Chop Shop Fast Travel",
                console='/Game/Maps/Zone_3/Motorcade/Motorcade_Travel.Motorcade_Travel:PersistentLevel.BP_CatchARide_Console_Chopshop',
                console_coord=Coord(loc=(-58191.757813, 82182.453125, -2915.512207), rot=(-2.424973, -55.016891, -1.021819)),
                console_new=Coord(loc=(-58792, 83047, -2810), rot=(0, -55.016891, 0)),
                plat1='BP_CatchARide_Platform_45',
                plat1_coord=Coord(loc=(-58886.984375, 82300.468750, -2938.882080), rot=(0, -55, 0)),
                plat2='BP_CatchARide_Platform_44',
                plat2_coord=Coord(loc=(-58057.785156, 82863.460938, -2938.090088), rot=(0, -55, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("In Big Donny's Hideout",
                console='/Game/Maps/Zone_3/Motorcade/Motorcade_Travel.Motorcade_Travel:PersistentLevel.BP_CatchARide_Console_Tunnel',
                console_coord=Coord(loc=(-66270.695313, 93674.625000, -3746.495117), rot=(-0.258575, -45.001770, -0.117920)),
                console_new=Coord(loc=(-67039, 94356, -3621), rot=(0, -45, 0)),
                plat1='BP_CatchARide_Platform_67',
                plat1_coord=Coord(loc=(-66973.968750, 93716.664063, -3751.756836), rot=(-0.255005, -43.297058, 1.149907)),
                plat2='BP_CatchARide_Platform_65',
                plat2_coord=Coord(loc=(-66378.523438, 94393.312500, -3751.756836), rot=(-0.255005, -43.297058, 1.149907)),
                hook_console=add_respawner_console,
                ),

            ]),

        ("Carnivora", '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_P', config_reg, [

            Replace("Initial station at entrance",
                console='/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Chase.MotorcadeFestival_Chase:PersistentLevel.BP_CatchARide_Console_230',
                console_coord=Coord(loc=(-44402.453125, 38268.183594, 2158.889160), rot=(0, -240.990417, 0)),
                console_new=Coord(loc=(-43594, 40540, 2183), rot=(0, 84, 0)),
                plat1='BP_CatchARide_Platform_268',
                plat1_coord=Coord(loc=(-43765.046875, 39678.320313, 2130.458496), rot=(0, -3.002319, 0.128154)),
                plat2='BP_CatchARide_Platform_210',
                plat2_coord=Coord(loc=(-43812.804688, 38769.753906, 2130.458496), rot=(0, -2.994476, -0.139832)),
                ),

            Replace("Center of Map, to the South",
                console='/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Chase.MotorcadeFestival_Chase:PersistentLevel.BP_CatchARide_Console_49',
                console_coord=Coord(loc=(-60440, 7580, 2695), rot=(0, -75.000015, 0)),
                console_new=Coord(loc=(-60615, 8682, 2781), rot=(0, -65, 0)),
                plat1='BP_CatchARide_Platform_272',
                plat1_coord=Coord(loc=(-58941.281250, 8079.805664, 2703.574219), rot=(0, 90.000351, 0)),
                plat2='BP_CatchARide_Platform_271',
                plat2_coord=Coord(loc=(-59921.902344, 8079.817383, 2703.574951), rot=(0, 90.000351, 0)),
                ),

            Replace("Center of Map, to the North",
                console='/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Chase.MotorcadeFestival_Chase:PersistentLevel.BP_CatchARide_Console_52',
                console_coord=Coord(loc=(-26325, 8835, 2470), rot=(0, -89.999939, 0)),
                console_new=Coord(loc=(-26339, 10146, 2554), rot=(0, 90, 0)),
                plat1='BP_CatchARide_Platform_278',
                plat1_coord=Coord(loc=(-25850.710938, 9543.859375, 2466.404785), rot=(0, 90.000053, 0)),
                plat2='BP_CatchARide_Platform_277',
                plat2_coord=Coord(loc=(-26817.634766, 9543.863281, 2466.403809), rot=(0, 90.000053, 0)),
                ),

            Replace("Heading towards Rakkman's Hideout",
                console='/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Chase.MotorcadeFestival_Chase:PersistentLevel.BP_CatchARide_Console_50',
                console_coord=Coord(loc=(-86743.156250, -17189.480469, 2365), rot=(0, -52.447525, 0)),
                console_new=Coord(loc=(-86364, -16866, 2456), rot=(0, -52.447525, 0)),
                plat1='BP_CatchARide_Platform_274',
                plat1_coord=Coord(loc=(-86930.929688, -16590.689453, 2362.333984), rot=(0, 39.998615, 0)),
                plat2='BP_CatchARide_Platform_273',
                plat2_coord=Coord(loc=(-87580.367188, -15816.687500, 2362.333984), rot=(0, 39.998615, 0)),
                ),

            Replace("Near 'dogleg', closest to Carnivora's canonical resting point",
                console='/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Chase.MotorcadeFestival_Chase:PersistentLevel.BP_CatchARide_Console_48',
                console_coord=Coord(loc=(-40745.152344, -23125.302734, 2901.153076), rot=(8.921309, -331.555939, -5.680060)),
                console_new=Coord(loc=(-40514, -23405, 2994), rot=(5, 48.444, 0)),
                plat1='BP_CatchARide_Platform_270',
                plat1_coord=Coord(loc=(-41755.339844, -24190.037109, 2865.632324), rot=(0, -52.106056, 0)),
                plat2='BP_CatchARide_Platform_269',
                plat2_coord=Coord(loc=(-41002.738281, -23604.246094, 2867.116943), rot=(0, -52.106056, 0)),
                ),

            Replace("Northernmost Console",
                console='/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Chase.MotorcadeFestival_Chase:PersistentLevel.BP_CatchARide_Console_51',
                console_coord=Coord(loc=(-1420, -7141.396973, 2785), rot=(0, 179.999954, 0)),
                console_new=Coord(loc=(-343, -7149, 2893), rot=(0, 0, 0)),
                plat1='BP_CatchARide_Platform_276',
                plat1_coord=Coord(loc=(-922.887695, -7653.627441, 2785.154785), rot=(0, 0.000378, 0)),
                plat2='BP_CatchARide_Platform_275',
                plat2_coord=Coord(loc=(-922.889465, -6631.857422, 2785.154785), rot=(0, 0.000378, 0)),
                ),

            Replace("Near pipeline station",
                console='/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_Chase.MotorcadeFestival_Chase:PersistentLevel.BP_CatchARide_Console_0',
                console_coord=Coord(loc=(-12027.762695, -58421.542969, 2680), rot=(0, -89.999939, 0)),
                console_new=Coord(loc=(-10937, -57686, 2769), rot=(0, 0, 0)),
                plat1='BP_CatchARide_Platform_1',
                plat1_coord=Coord(loc=(-11532.598633, -57688.093750, 2678.124268), rot=(0, 90.000053, 0)),
                plat2='BP_CatchARide_Platform_0',
                plat2_coord=Coord(loc=(-12533.295898, -57688.097656, 2678.124268), rot=(0, 90.000053, 0)),
                ),

            ]),

        ("Meridian Outskirts", '/Game/Maps/Zone_1/Outskirts/Outskirts_P', config_reg, [

            Replace("First Catch-A-Ride system",
                console='/Game/Maps/Zone_1/Outskirts/Outskirts_M_OvercomeHQBlockade.Outskirts_M_OvercomeHQBlockade:PersistentLevel.BP_CatchARide_Console_498',
                console_coord=Coord(loc=(-69791.843750, -47855.414063, 1280.490601), rot=(0, 562.500122, 0)),
                console_new=Coord(loc=(-70098, -46791, 1371), rot=(0, 157.5, 0)),
                plat1='BP_CatchARide_Platform_17',
                plat1_coord=Coord(loc=(-69233.640625, -47124.804688, 1265.238892), rot=(0, 22.499969, 0)),
                plat2='BP_CatchARide_Platform_16',
                plat2_coord=Coord(loc=(-68888.476563, -47938.234375, 1265.238892), rot=(0, 22.499969, 0)),
                ),

            # Original console: BP_CatchARide_Console_0 (-46389.625000, -32581.312500, 1284.396729) r:(0, 183.446121, 0)
            Hook("Elevator ground floor, under broken bridge",
                console=Coord(loc=(-44669, -34281, 1371), rot=(0, -20, 0)),
                plat1='BP_CatchARide_Platform_1',
                plat2='BP_CatchARide_Platform_0',
                ),

            # Original console: BP_CatchARide_Console_3402 (-64331.089844, -22736.460938, 1307.986938) r:(-2.249443, -64.788216, 5.994318)
            Hook("Just around the corner from original entrance, across from bridge CAR",
                console=Coord(loc=(-65515, -21160, 1398), rot=(0, -20, 0)),
                plat1='BP_CatchARide_Platform_3404',
                plat2='BP_CatchARide_Platform_3405',
                ),

            Replace("Near road/vehicle exit to Meridian Metroplex (and Wizard of NOGs quest)",
                console='/Game/Maps/Zone_1/Outskirts/Outskirts_M_WizardOfNogs.Outskirts_M_WizardOfNogs:PersistentLevel.CatchARide_Console_WizardOfNog',
                console_coord=Coord(loc=(-16388.089844, -16242.651367, 3208.935303), rot=(0, 163.721817, -1.113806)),
                console_new=Coord(loc=(-15899, -16803, 3299), rot=(0, 50, 0)),
                plat1='BP_CatchARide_Platform_2602',
                plat1_coord=Coord(loc=(-15371.017578, -16443.156250, 3179.783447), rot=(0, 135.000259, 0)),
                plat2='BP_CatchARide_Platform_2603',
                plat2_coord=Coord(loc=(-14734.894531, -15812.353516, 3179.783447), rot=(0, 135.000259, 0)),
                ),

            # Original console: BP_CatchARide_Console_2 (-27394.162109, -41823.855469, 3190.081543) r:(0, -220.000153, 0)
            Hook("Entrance to refugee area",
                console=Coord(loc=(-26502, -43693, 3282), rot=(0, -90, 0)),
                plat1='BP_CatchARide_Platform_3',
                plat2='BP_CatchARide_Platform_2',
                ),

            ]),

        ("Meridian Metroplex", '/Game/Maps/Zone_1/City/City_P', config_reg, [

            Replace("At headquarters (Fast Travel)",
                console='/Game/Maps/Zone_1/City/City_M_OvercomeHQBlockade.City_M_OvercomeHQBlockade:PersistentLevel.BP_CatchARide_Console_8',
                console_coord=Coord(loc=(-31888.423828, -26813.353516, 4690.180664), rot=(0, -135, 0)),
                console_new=Coord(loc=(-32572, -25629, 4780), rot=(0, 180, 0)),
                plat1='BP_CatchARide_Platform_3',
                plat1_coord=Coord(loc=(-31766.224609, -26072.818359, 4666.068359), rot=(0, 0.000345, 0)),
                plat2='BP_CatchARide_Platform_2',
                plat2_coord=Coord(loc=(-31764.298828, -25169.015625, 4666.068359), rot=(0, 0.000345, 0)),
                hook_console=meridian_metroplex_gate_open,
                ),

            # Original console: BP_CatchARide_Console_0 (-12915.040039, -371.161743, 3645.281250) r:(0, -148.115250, 0)
            Hook("Past Rise and Grind, near Gigamind",
                console=Coord(loc=(-14815, -406, 3735), rot=(0, -58.11525, 0)),
                plat1='BP_CatchARide_Platform_0',
                plat2='BP_CatchARide_Platform_1',
                ),

            # Original console: BP_CatchARide_Console_2 (-6564.458984, -21549.431641, 4091.910645) r:(0, 208.721802, 0)
            Hook("Near exit to Lectra City",
                console=Coord(loc=(-5188, -20703, 4182), rot=(0, 180, 0)),
                plat1='BP_CatchARide_Platform_4',
                plat2='BP_CatchARide_Platform_5',
                ),

            # Original console: BP_CatchARide_Console_1 (7355.565430, -44107.449219, 4693.272949) r:(0, -202.499863, 0)
            Hook("Near entrance to Meridian Mercantile (down the street from Atlas HQ exit)",
                console=Coord(loc=(5963, -42722, 4780), rot=(0, -67.499863, 0)),
                plat1='BP_CatchARide_Platform_2',
                plat2='BP_CatchARide_Platform_3',
                ),

            # Original console: BP_CatchARide_Console_1499 (16192.142578, -19527.423828, 5396.564941) r:(0, -134.999939, 0)
            Hook("Near Atlas HQ exit",
                console=Coord(loc=(14250, -19474, 5503), rot=(0, -45, 0)),
                plat1='BP_CatchARide_Platform_1502',
                plat2='BP_CatchARide_Platform_1503', 
                ),

            ]),

        ("Neon Arterial", '/Game/Maps/Zone_1/CityVault/CityVault_P', config_reg, [

            Replace("Map Entrance",
                console='/Game/Maps/Zone_1/CityVault/CityVault_M_LastStop.CityVault_M_LastStop:PersistentLevel.BP_CatchARide_Console_START',
                console_coord=Coord(loc=(-47910, 178380, 5350), rot=(0, -169.999908, 0)),
                console_new=Coord(loc=(-47503, 179593, 5440), rot=(0, 100, 0)),
                plat1='BP_CatchARide_Platform_Start_0',
                plat1_coord=Coord(loc=(-47135.691406, 177992.531250, 5335.933594), rot=(-0.000829, -165.606750, -0.000566)),
                plat2='BP_CatchARide_Platform_Start',
                plat2_coord=Coord(loc=(-47385.691406, 179042.531250, 5339), rot=(-0.000829, -165.606750, -0.000566)),
                hook_console=add_respawner_console,
                ),

            Replace("First dogleg",
                console='/Game/Maps/Zone_1/CityVault/CityVault_M_LastStop.CityVault_M_LastStop:PersistentLevel.BP_CatchARide_Console_8',
                console_coord=Coord(loc=(-66687.695313, 135036.484375, 5364.359375), rot=(0, -80.312408, 0)),
                console_new=Coord(loc=(-65823, 136138, 5454), rot=(0, 15.678345, 0)),
                plat1='BP_CatchARide_Platform_14',
                plat1_coord=Coord(loc=(-66627.007813, 136260.718750, 5344.856445), rot=(0, -164.321655, 0)),
                plat2='BP_CatchARide_Platform_0',
                plat2_coord=Coord(loc=(-66444.710938, 135604.734375, 5344.856445), rot=(0, -164.321655, 0)),
                hook_console=add_respawner_console,
                ),

            Replace("At first door barrier",
                console='/Game/Maps/Zone_1/CityVault/CityVault_M_LastStop.CityVault_M_LastStop:PersistentLevel.BP_CatchARide_Console',
                console_coord=Coord(loc=(-63121.921875, 61878.132813, 4215.119141), rot=(-2.642592, 81.227577, 0.962614)),
                console_new=Coord(loc=(-61103, 61738, 4293), rot=(0, 95.771873, 0)),
                plat1='BP_CatchARide_Platform',
                plat1_coord=Coord(loc=(-61739.710938, 61359.082031, 4177.506836), rot=(-0.081416, 88.499725, 0.669265)),
                plat2='BP_CatchARide_Platform_24',
                plat2_coord=Coord(loc=(-62597.359375, 61403.207031, 4177.702148), rot=(-0.081416, 88.499725, 0.669265)),
                hook_console=add_respawner_console,
                ),

            Replace("Underneath first ramp to lower waterway",
                console='/Game/Maps/Zone_1/CityVault/CityVault_M_LastStop.CityVault_M_LastStop:PersistentLevel.BP_CatchARide_Console_35',
                console_coord=Coord(loc=(-18095.410156, 73522.718750, 1145.633057), rot=(0, -225.312546, 0)),
                console_new=Coord(loc=(-17984, 71530, 1215), rot=(0, 134.687454, 0)),
                plat1='BP_CatchARide_Platform_19',
                plat1_coord=Coord(loc=(-18779.460938, 73107.601563, 1110.355957), rot=(-0.000717, 0.006502, -0.000580)),
                plat2='BP_CatchARide_Platform_1',
                plat2_coord=Coord(loc=(-18779.460938, 72222.601563, 1110.355957), rot=(-0.000717, 0.006502, -0.000580)),
                hook_console=add_respawner_console,
                ),

            Replace("Last station, before big ramp to lowest waterway",
                console='/Game/Maps/Zone_1/CityVault/CityVault_M_LastStop.CityVault_M_LastStop:PersistentLevel.BP_CatchARide_Console_36',
                console_coord=Coord(loc=(16944.855469, 61019.757813, 1155.781372), rot=(0, -52.813229, 0)),
                console_new=Coord(loc=(15906, 62177, 1246), rot=(0, 90, 0)),
                plat1='BP_CatchARide_Platform_20',
                plat1_coord=Coord(loc=(16380.437500, 61389.253906, 1133.778931), rot=(0.000075, -89.988205, -0.000946)),
                plat2='BP_CatchARide_Platform_2',
                plat2_coord=Coord(loc=(15443.437500, 61389.253906, 1133.778931), rot=(0.000075, -89.988205, -0.000946)),
                hook_console=add_respawner_console,
                ),

            ]),

        ("Floodmoor Basin", '/Game/Maps/Zone_2/Wetlands/Wetlands_P', config_reg, [

            # Original console: BP_CatchARide_Console7 (-46987.519531, 27656.208984, 4511.528320) r:(0, -10.422604, 0)
            Hook("Near Drop Pod",
                console=Coord(loc=(-47680, 28418, 4582), rot=(0, 169.577396, 0)),
                plat1='BP_CatchARide_Platform7',
                ),

            Replace("Near Mudhaven, and Prisa's Garage",
                console='/Game/Maps/Zone_2/Wetlands/Wetlands_M_DriveAwayThePain.Wetlands_M_DriveAwayThePain:PersistentLevel.BP_CatchARide_Console_DriveAwayPain',
                console_coord=Coord(loc=(-28670.048828, 18110.751953, 1049), rot=(0, -158.108322, 0)),
                console_new=Coord(loc=(-29024, 19177, 1133), rot=(0, -158.108322, 0)),
                plat1='BP_CatchARide_Platform_68',
                plat1_coord=Coord(loc=(-28873.611328, 18622.812500, 1023.087402), rot=(0.830173, -160.706985, 0.000001)),
                hook_console=add_respawner_console,
                ),

            # Original console: BP_CatchARide_Console_7 (135, 37199, 1130) r:(0, -145.201843, 0)
            Hook("Midpoint of main basin, at base of giant tree root arch",
                console=Coord(loc=(-324, 37263, 1213), rot=(0, -55.201843, 0)),
                plat1='BP_CatchARide_Platform_2',
                ),

            # Original console: BP_CatchARide_Console5 (29344.335938, 45127.558594, 989.521851) r:(0, 39.348145, 0)
            Hook("Near exit to Voracious Canopy",
                console=Coord(loc=(29235, 45583, 1119), rot=(-15, -5.651855, 0)),
                plat1='BP_CatchARide_Platform5',
                ),

            Replace("At Lumberton Junction outpost (around the corner from Fort Sunshine)",
                console='/Game/Maps/Zone_2/Wetlands/Wetlands_Combat.Wetlands_Combat:PersistentLevel.BP_CatchARide_Console8',
                console_coord=Coord(loc=(28115, 20360, 2281), rot=(0, -135.633804, 0)),
                console_new=Coord(loc=(28781, 20190, 2378), rot=(0, -140.633804, 0)),
                plat1='BP_CatchARide_Platform8',
                plat1_coord=Coord(loc=(28231.468750, 19750.025391, 2239.870117), rot=(-0.596497, -134.799896, 0)),
                ),

            # Original console: BP_CatchARide_Console_3 (29686, 11288, 3300) r:(-5.382289, 128.421173, -1.399099)
            Hook("At Fort Sunshine",
                console=Coord(loc=(29340, 11296, 3430), rot=(-15, 73.42117300000001, -8)),
                plat1='BP_CatchARide_Platform_0',
                ),

            # Original console: BP_CatchARide_Console (-6337.822266, -9903.508789, 1150.780884) r:(0, 104.380722, 0)
            Hook("At bottom of dam (around the corner from the base of the Reliance elevator)",
                console=Coord(loc=(-6314, -9990, 1235), rot=(0, -75.619278, 0)),
                plat1='BP_CatchARide_Platform',
                ),

            # Original console: BP_CatchARide_Console_4 (-21732, 6639.999023, 5389) r:(-4.244194, -284.683990, -3.824315)
            Hook("Southern path from Reliance to Knotty Peak",
                console=Coord(loc=(-20896, 7420, 5421), rot=(4, 165.31601, -5)),
                plat1='BP_CatchARide_Platform_1',
                ),

            # Original console: BP_CatchARide_Console3 (16170.704102, 18679.240234, 8377.156250) r:(0, -179.124084, 0)
            Hook("Knotty Peak Garage (base of elevator)",
                console=Coord(loc=(15938, 18535, 8467), rot=(0, 90.875916, 0)),
                plat1='BP_CatchARide_Platform3',
                ),

            ## Original console: BP_CatchARide_Console_332 (-28526.726563, -13114.731445, 7128) r:(0, -284.955841, 0)
            Hook("Reliance",
                console=Coord(loc=(-28861, -12392, 7222), rot=(0, -14.955841, 0)),
                plat1='BP_CatchARide_Platform_420',
                ),

            # Original console: BP_CatchARide_Console_306 (-11104, -33339, 7334) r:(0, 178.040543, 0)
            Hook("Outside The Timbermills (where you ride the logs to Fort Sunshine)",
                console=Coord(loc=(-10621, -34460, 7560), rot=(0, 88.040543, 0)),
                plat1='BP_CatchARide_Platform_5',
                ),

            # Original console: BP_CatchARide_Console6 (37773, -10998, 8573) r:(0, -192.460739, 0)
            Hook("Near exit to The Anvil",
                #console=Coord(loc=(37686, -10736, 8674), rot=(0, -147.460739, 0)),
                console=Coord(loc=(37750, -10660, 8674), rot=(0, -147.460739, 0)),
                plat1='BP_CatchARide_Platform6',
                ),

            ]),

        ("Desolation's Edge", '/Game/Maps/Zone_4/Desolate/Desolate_P', config_reg, [

            Replace("Initial Station (which requires power-on)",
                console='/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_CatchARide_Console_Mission',
                console_coord=Coord(loc=(25395.646484, -46499.449219, 8494.558594), rot=(0, -90.000122, 0)),
                console_new=Coord(loc=(25398, -45913, 8582), rot=(0, 90, 0)),
                plat1='BP_CatchARide_Platform_0',
                plat1_coord=Coord(loc=(25894.091797, -46196.781250, 8481.400391), rot=(0, 89.736198, 0)),
                plat2='BP_CatchARide_Platform_1',
                plat2_coord=Coord(loc=(24903.191406, -46192.214844, 8481.400391), rot=(0, 89.736198, 0)),
                hook_console=desolation_power_on,
                ),

            Replace("Bottom of entry canyon, near Blinding Banshee lake",
                console='/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_CatchARide_Console_4',
                console_coord=Coord(loc=(37047.964844, -28109.371094, 918.398438), rot=(0, 279.815674, 0)),
                console_new=Coord(loc=(37256, -29102, 1008), rot=(0, 99.815674, 0)),
                plat1='BP_CatchARide_Platform_10',
                plat1_coord=Coord(loc=(37631.628906, -28497.433594, 905.057495), rot=(0, 101.016869, 0)),
                plat2='BP_CatchARide_Platform_11',
                plat2_coord=Coord(loc=(36664.062500, -28702.095703, 900.287476), rot=(0, 101.016869, 0)),
                ),

            Replace("Northwest corner of basin, near entrance to Clapslist mission area",
                console='/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_CatchARide_Console_2',
                console_coord=Coord(loc=(5901.309570, -24726.853516, 813.111877), rot=(0, -210.700592, 0)),
                console_new=Coord(loc=(6561, -25138, 916), rot=(0, -30, 0)),
                plat1='BP_CatchARide_Platform_6',
                plat1_coord=Coord(loc=(5998.379883, -25337.195313, 811.629456), rot=(0, -210.641754, 0)),
                plat2='BP_CatchARide_Platform_7',
                plat2_coord=Coord(loc=(6522.729492, -24544.906250, 811.629456), rot=(0, -210.641754, 0)),
                ),

            Replace("Northeast corner of basin, at Typhon's hideout",
                console='/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_CatchARide_Console_0',
                console_coord=Coord(loc=(5949.016602, -772.110352, -96.563232), rot=(0, -446.557068, 0)),
                console_new=Coord(loc=(4822, -738, -36), rot=(-10, -146.557068, 0)),
                plat1='BP_CatchARide_Platform_3',
                plat1_coord=Coord(loc=(6402.340332, -243.483307, -69.969841), rot=(-2.884506, -85.817146, 0.000003)),
                plat2='BP_CatchARide_Platform_2',
                plat2_coord=Coord(loc=(5414.054688, -315.728027, -69.967476), rot=(-2.884506, -85.817146, 0.000003)),
                ),

            Replace("Path to Tazendeer Ruins exit / General Traunt",
                console='/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_CatchARide_Console_3',
                console_coord=Coord(loc=(24799.550781, -12951.750977, 3995.512451), rot=(0, 180, 0)),
                console_new=Coord(loc=(25627, -12948, 4086), rot=(0, 0, 0)),
                plat1='BP_CatchARide_Platform_8',
                plat1_coord=Coord(loc=(25300.044922, -12456.316406, 3990), rot=(0, 180, 0)),
                plat2='BP_CatchARide_Platform_9',
                plat2_coord=Coord(loc=(25262.285156, -13445.152344, 3990), rot=(0, 180, 0)),
                ),

            Replace("Southwest corner of basin, near Twilight Arcade temple",
                console='/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_CatchARide_Console_6',
                console_coord=Coord(loc=(-21992.113281, -30261.078125, -506.874756), rot=(0, -350.619629, 0)),
                console_new=Coord(loc=(-22905, -30418, -412), rot=(0, -170.619629, 0)),
                plat1='BP_CatchARide_Platform_5',
                plat1_coord=Coord(loc=(-22526.601563, -29843.310547, -505.000702), rot=(0.929957, 9.186698, -0.560656)),
                plat2='BP_CatchARide_Platform_4',
                plat2_coord=Coord(loc=(-22370.671875, -30822.015625, -502.999237), rot=(0, 9.195935, 1.953013)),
                ),

            Replace("Southeast corner of basin, near initial Tazendeer Ruins attempt",
                console='/Game/Maps/Zone_4/Desolate/Desolate_Gameplay.Desolate_Gameplay:PersistentLevel.BP_CatchARide_Console_5',
                console_coord=Coord(loc=(-19328.552734, -11767.675781, -686.873779), rot=(0, -352.026398, 0)),
                console_new=Coord(loc=(-20171, -11894, -568), rot=(0, -172.026398, 0)),
                plat1='BP_CatchARide_Platform_12',
                plat1_coord=Coord(loc=(-19744.843750, -12327.465820, -690), rot=(0, 7.789122, 0)),
                plat2='BP_CatchARide_Platform_13',
                plat2_coord=Coord(loc=(-19876.677734, -11345.375000, -690), rot=(0, 7.788885, 0)),
                ),

            ]),

        ("Sanctuary", '/Game/Maps/Sanctuary3/Sanctuary3_P', config_reg, [

            # Original console: BP_CatchARide_Console_26 (13810, -1660, -2100) r:(0, 0, 0)
            Hook("Cargo Bay",
                console=Coord(loc=(13810, -1865, -2010), rot=(0, 0, 0)),
                plat1='BP_CatchARide_Platform_722',
                hook_console=sanctuary_disable_spawned,
                ),

            ]),

        #("Skittermaw Basin", '/Hibiscus/Maps/Lake/Lake_P', config_dlc2, []),

        ("Blastplains", '/Geranium/Maps/Frontier/Frontier_P', config_dlc3, [

            # Original console: BP_CatchARide_Console_Ger_6 (-64844.597656, 55906.023438, 8650) r:(0, -32.422150, 0)
            Hook("Near exit to Vestige (initial entry point)",
                console=Coord(loc=(-65852, 56588, 8740), rot=(0, -32.4, 0)),
                plat1='BP_CatchARide_Platform_0',
                plat2='BP_CatchARide_Platform_17',
                orig_console='BP_CatchARide_Console_Ger_6',
                hook_console=blastplains_endgame_spawn,
                ),

            # Original console: BP_CatchARide_Console_Ger_2 (-37559.113281, 49358.574219, 8607.960938) r:(0, -64.062531, 0)
            Hook("At exit of Hasty Retreat (around the corner from Vestige entrance)",
                console=Coord(loc=(-38501, 49125, 8705), rot=(0, -109.062531, 0)),
                plat1='BP_CatchARide_Platform',
                plat2='BP_CatchARide_Platform_3',
                orig_console='BP_CatchARide_Console_Ger_2',
                ),

            # Original console: BP_CatchARide_Console_Ger_10 (-14435.916016, 50526.929688, 7586.537109) r:(0, -90.000084, 0)
            Hook("Near exit to Bloodsun Canyon",
                console=Coord(loc=(-15611, 49271, 7663), rot=(0, 180, 0)),
                plat1='BP_CatchARide_Platform_4',
                plat2='BP_CatchARide_Platform_1',
                orig_console='BP_CatchARide_Console_Ger_10',
                ),

            # Original console: BP_CatchARide_Console_Ger_1 (4651.695801, 24025.958984, 8897.912109) r:(0, -559.687744, 0)
            Hook("Near exit to Obsidian Forest",
                console=Coord(loc=(4676, 24860, 9086), rot=(0, 70, 0)),
                plat1='BP_CatchARide_Platform_16',
                plat2='BP_CatchARide_Platform_15',
                orig_console='BP_CatchARide_Console_Ger_1',
                ),

            # Original console: BP_CatchARide_Console_Ger_14 (5676.428711, 13841.096680, 8440.460938) r:(0, -140.312714, 0)
            Hook("Near Saurdew Valley Ranch",
                console=Coord(loc=(4230, 14035, 8566), rot=(0, 130, 0)),
                plat1='BP_CatchARide_Platform_12',
                plat2='BP_CatchARide_Platform_11',
                orig_console='BP_CatchARide_Console_Ger_14',
                ),

            Replace("Outside Stickly's The Shoddy building",
                console='/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.BP_CatchARide_Console_Ger_0',
                console_coord=Coord(loc=(-9813.620117, 23161.726563, 8751.099609), rot=(0, -408.437622, 0)),
                console_new=Coord(loc=(-9129, 23902, 8872), rot=(0, 42, 0)),
                # We've manually rotated these platforms by 180deg, since the stock ones are facing
                # the wrong way.
                plat1='BP_CatchARide_Platform_13',
                plat1_coord=Coord(loc=(-8984.816406, 23100.056641, 8770.116211), rot=(0, -48.733368, 0)),
                plat2='BP_CatchARide_Platform_14',
                plat2_coord=Coord(loc=(-9827.779297, 22384.349609, 8761.375000), rot=(0, 128.749943, 0)),
                ),

            # Original console: BP_CatchARide_Console_Ger_9 (-29282.259766, 19853.400391, 8749.474609) r:(0, 171.562576, 0)
            Hook("Pump & Charge Fast Travel Station",
                console=Coord(loc=(-29402, 18783, 8843), rot=(0, -143.437424, 0)),
                plat1='BP_CatchARide_Platform_14',
                plat2='BP_CatchARide_Platform_13',
                orig_console='BP_CatchARide_Console_Ger_9',
                ),

            # Original console: BP_CatchARide_Console_Ger_13 (-34705, -5636, 7956) r:(0, -270.000305, 0)
            Hook("Near exit to Crater's Edge",
                console=Coord(loc=(-35671, -6901, 8062), rot=(0, -135, 0)),
                plat1='BP_CatchARide_Platform_10',
                plat2='BP_CatchARide_Platform_9',
                orig_console='BP_CatchARide_Console_Ger_13',
                ),

            Replace("Near Frack Mesa Extraction (around the corner from Crater's Edge exit)",
                console='/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.BP_CatchARide_Console_Ger_10',
                console_coord=Coord(loc=(-23415.140625, 7372.931641, 9308), rot=(0, -270.937561, 0)),
                console_new=Coord(loc=(-23382, 6290, 9398), rot=(0, 89.062439, 0)),
                plat1='BP_CatchARide_Platform_4',
                plat1_coord=Coord(loc=(-22871.818359, 6826.662109, 9293.000977), rot=(0, -268.420990, 0)),
                plat2='BP_CatchARide_Platform_1',
                plat2_coord=Coord(loc=(-23937.560547, 6826.954102, 9291.609375), rot=(0, 89.062454, 0)),
                ),

            # Original console: BP_CatchARide_Console_Ger_11 (-4445.105469, -4181.778320, 9398) r:(0, 74.374748, 0)
            Hook("Near exit to Ashfall Peaks",
                console=Coord(loc=(-3242, -4002, 9431), rot=(0, -15.625252, 0)),
                plat1='BP_CatchARide_Platform_6',
                plat2='BP_CatchARide_Platform_5',
                orig_console='BP_CatchARide_Console_Ger_11',
                ),

            # Original console: BP_CatchARide_Console_Ger_12 (-11689.300781, -1925.080322, 11125) r:(0, -133.437729, 0)
            Hook("Fort Kickwater",
                console=Coord(loc=(-12785, -1895, 11191), rot=(0, -153.437729, 0)),
                plat1='BP_CatchARide_Platform_8',
                plat2='BP_CatchARide_Platform_7',
                orig_console='BP_CatchARide_Console_Ger_12',
                ),

            ]),
        ]:

    # A header for the map
    mod.header(map_label)

    # Pull apart our map path a bit
    map_base_path, map_last = map_path.rsplit('/', 1)

    # Do all our work
    for idx, modification in enumerate(modifications):
        mod.comment('CAR System #{} - {}: {}'.format(idx+1, modification.desc, modification.label))
        new_consoles, new_platforms = modification.process(map_path, map_base_path, map_last, config, mod)
        if modification.hook_console or modification.hook_platform:
            mod.comment('Processing extra behaviors/effects for spawned objects')
        if modification.hook_console:
            for new_console in new_consoles:
                modification.hook_console(mod, config, map_path, map_base_path, map_last, new_console)
        if modification.hook_platform:
            for new_platform in new_platforms:
                modification.hook_platform(mod, config, map_path, map_base_path, map_last, new_platform)
        mod.newline()

# Some extra mission-vehicle-spawn objects we've got to fix up
mod.header('Mission Vehicle Respawners')

for respawner in respawners:
    mod.comment(respawner.label)
    # Technically we should maybe use the fully-correct object type here, but
    # just using the base class BP_CatchARide_Console_C seems to work just fine.
    mod.reg_hotfix(Mod.LEVEL, respawner.map_last,
            '{}/{}'.format(respawner.map_base_path, respawner.spawner_name),
            'ConsoleAllowToRespawn',
            '({})'.format(','.join([
                mod.get_full_cond(c, 'BP_CatchARide_Console_C') for c in respawner.consoles
                ])))
    mod.newline()

# Moving a chest out of the way
mod.header('Moving Objects out of the Way')

mod.comment('Floodmoor Basin')
mod.reg_hotfix(Mod.LEVEL, 'Wetlands_P',
        '/Game/Maps/Zone_2/Wetlands/Wetlands_P.Wetlands_P:PersistentLevel.BPIO_Lootable_COV_AmmoCrate_17.Mesh_Chest1',
        'RelativeLocation',
        '(X=-27855,Y=-12622,Z=7128)',
        notify=True)
mod.reg_hotfix(Mod.LEVEL, 'Wetlands_P',
        '/Game/Maps/Zone_2/Wetlands/Wetlands_P.Wetlands_P:PersistentLevel.BPIO_Lootable_COV_AmmoCrate_17.Mesh_Chest1',
        'RelativeRotation',
        '(Pitch=0,Yaw=-155.11581,Roll=0)',
        notify=True)
mod.newline()

mod.close()

