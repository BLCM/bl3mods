#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021-2023 Christopher J. Kucera
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
import argparse
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, LVL_TO_ENG_LOWER

parser = argparse.ArgumentParser(
        description='Generates Mega TimeSaver XL',
        )
parser.add_argument('-v', '--verbose',
        action='store_true',
        help='Be verbose about what we\'re processing',
        )
args = parser.parse_args()
verbose = args.verbose

# There's a lot going on in this mod, but in general there's just a few classes
# of tweaks that I'm making.  This should cover like 95% of the mod.  Here's a
# brief summary:
#
#  - ParticleSystems
#    There's a few cases where a ParticleSystem might determine the timing of
#    something, and others where it just ends up looking weird if you don't
#    speed it up.  Digistruct effects tend to use these, and stuff like the
#    steam while Barista Bot pours coffee in Metridian Metroplex, or the liquid
#    pouring in the brewery in Cankerwood.  There's a lot of values which need
#    to be tweaked to speed up a ParticleSystem -- I've got that wrapped up in
#    a `scale_ps()` function.
#
#  - AnimSequences
#    These are little individual bits of animations, and if that's all you've
#    got to work with, they tend to require a number of tweaks inside them to
#    get the timing right.  I'm using an `AS()` class to wrap all that up.  There's
#    some weird interactions between the majority of the attrs and the
#    `SequenceLength` inside the AnimSequence which I've never figured out.  Some
#    AnimSequences end up glitching out if you scale SequenceLength along with
#    everything else, but others require you to scale it if you want the overall
#    timings to update properly.  Go figure.  The vehicle-related animations in
#    particular are very finnicky, and I've had to balance between an animation
#    which seems to freeze up versus having it *look* fine but leave the vehicle
#    uncontrollable for a bit afterwards.  Note that the AS class expects you to
#    fill in `scale` and `seqlen_scale` *after* instantiation, due to how we're
#    processing these.
#
#  - InteractiveObjects
#    Most of the stuff you interact with in the game is an InteractiveObject (IO),
#    sometimes prefixed by "Blueprint" (BPIO).  Speeding these up requires hitting
#    a lot of internal attrs (much like AnimSequences), but at least these don't
#    suffer from the same weird SequenceLength problems that AnimSequences do.  For
#    some objects, in addition to tweaking the "main" IO object itself, the
#    map-specific instances of the IO might also need some tweaking to account for the
#    reduced runtime.  So you'll see a bunch of level-specific object types have an
#    IO tweak and then also some custom map tweaks further down in the file.  Scaling
#    for these objects is helped out a bit by an `IO()` class, though the actual
#    scaling's done outside the class.
#
#  - GbxLevelSequenceActors
#    As a potential alternative to both AnimSequence and InteractiveObject tweaking,
#    the game sometimes uses sequences to kick off one or more of those, and there
#    may be a GbxLevelSequenceActor which kicks that off.  I didn't really discover
#    these until pretty late in the mod development, but when they're available,
#    they seem much more reliable (and simpler!) than editing AnimSequence and
#    InteractiveObject objects directly.  They've got a `SequencePlayer` sub-object
#    attached which has a very convenient `PlayRate` attr, so all I need to do is
#    set that and I'm golden.  I suspect there are quite a few AS/IO tweaks
#    that I'm doing which would be better done via this method.  (I'm pretty sure
#    there are plenty of AS/IO objects which don't live inside a sequence, so we'd
#    have to be doing some direct tweaks anyway, though.)
#
#  - Bytecode Tweaks
#    Finally, the other main class of tweaks in here is altering blueprint bytecode,
#    generally just to shorten `Delay` opcodes.  There's plenty of times where even
#    if you have all the AS/IO/whatever stuff sped up, you'll end up with blueprint-
#    enforced delays.  Tracking these down is a "fun" process sometimes; see my
#    UAssetAPI fork: https://github.com/apocalyptech/UAssetAPI/
#
# Other than all that, there's the usual amount of "custom" tweaking for other
# stuff, which should be pretty straightforward so long as you've got object
# serializations available.  Elevators all share a common set of attrs, as do the
# NPC walk/sprint speed stuff.  I've tried to keep things at least somewhat
# commented, so hopefully the comments here will help out if you're curious about
# something!

mod = Mod('mega_timesaver_xl.bl3hotfix',
        'Mega TimeSaver XL',
        'Apocalyptech',
        [
            "Speeds up nearly all the noticeably-slow interactive objects that you",
            "use throughout BL3.  This includes containers, doors, elevators,",
            "slot machines, vehicle entering/exiting, respawning, teleporting,",
            "using Eridian tools, Takedown countdowns, a ton of mission and level",
            "specific objects, and also speeds up a bunch of NPC walk/sprint",
            "speeds so you spend less time waiting for NPCs to move around.",
            "",
            "Note that this mod does NOT do any dialogue or mission skips -- all",
            "content in the game should still be available.",
            "",
            "See the README for some known quirks and bugs, and for a TODO list",
            "which may or may not ever get finished up.  Enjoy!",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol',
        quiet_streaming=True,
        )

###
### Some global scaling params follow.  For the *most* part, you can alter practically
### everything in the mod by altering these few variables, though there's some
### hardcoded stuff occasionally, and note that some timings are more fragile than
### others.  Some "complex" animations and sequences might be somewhat touchy about
### the precise timing, and I've done some manual tweaking to line things up in a few
### cases.  Nudging these global vars up or down could knock some of that out of
### alignment.  Vehicle animations in particular are already a bit weird and don't
### even work perfectly at 2x.  Dialogue skips probably become more likely as the
### scales goes up, too, particularly on the character movement scale.
###

# How much to improve speed
global_scale = 4

# ... but I want to do doors a *bit* more
door_scale = 5

# Character movement speed
global_char_scale = 1.4

# Vehicle-animation movement speed
global_vehicle_scale = 2

# Eridian tool speedups
global_eridian_scale = 2

# Minimum serialization version to allow.  Stock JWP doesn't serialize CurveFloats
# correctly, so the mod'll be invalid unless using apocalyptech's fork, of at least
# this version.  (Honestly we probably require more than v19 at this point -- I
# think there's some previously-unserializable objects we probably rely on now.
# Still, that should at least fail the generation instead of producing incorrect
# output, so we'll just leave it at v19 for now.)
min_apoc_jwp_version = 19

# Data obj
data = BL3Data()

def scale_ps(mod, data, hf_type, hf_target, ps_name, scale, notify=False):
    """
    Function to attempt to scale all components of a ParticleSystem object.
    At time of writing, this is hardly being used by anything -- I'd written
    it for Typhon's digistruct animation in Tazendeer Ruins, and it turns
    out that maybe we didn't even have to (the critical timing tweak looks
    like it was probably an ubergraph bytecode change to the call to his
    dialogue line).  Anyway, we've got a few other instances of editing
    ParticleSystems in here, which should maybe get ported over to using
    this, once I've got an opportunity to re-test 'em.

    `mod` and `data` should be the relevant Mod and BL3Data objects.

    `hf_type` and `hf_target` should be the initial hotfix params -- so far,
    we've only needed Mod.LEVEL for `hf_type`.

    `ps_name` is the path to the ParticleSystem object

    `scale` is the scale to use ("scale" is actually kind of a bad name here;
    we're actualy dividing, not multiplying)

    `notify` can be passed in to set the notify flag on the hotfixes, too,
    but so far that's never been necessary
    """
    done_work = False
    ps_obj = data.get_data(ps_name)
    for export in ps_obj:
        if export['export_type'] == 'ParticleSystem':
            for emitter_idx, emitter_obj in enumerate(export['Emitters']):
                emitter = ps_obj[emitter_obj['export']-1]
                for lod_idx, lod_obj in enumerate(emitter['LODLevels']):
                    lod = ps_obj[lod_obj['export']-1]
                    lod_attr = f'Emitters.Emitters[{emitter_idx}].Object..LODLevels.LODLevels[{lod_idx}].Object..'
                    if 'TypeDataModule' in lod:
                        tdm_obj = lod['TypeDataModule']
                        tdm = ps_obj[tdm_obj['export']-1]
                        if 'EmitterInfo' in tdm and 'MaxLifetime' in tdm['EmitterInfo']:
                            done_work = True
                            mod.reg_hotfix(hf_type, hf_target,
                                    ps_name,
                                    f'{lod_attr}TypeDataModule.Object..EmitterInfo.MaxLifetime',
                                    round(tdm['EmitterInfo']['MaxLifetime']/scale, 6),
                                    notify=notify,
                                    )
                    if 'RequiredModule' in lod:
                        reqmod_obj = lod['RequiredModule']
                        reqmod = ps_obj[reqmod_obj['export']-1]
                        reqmod_attr = f'{lod_attr}RequiredModule.Object..'
                        for attr in [
                                'EmitterDuration',
                                'EmitterDelay',
                                ]:
                            if attr in reqmod:
                                done_work = True
                                mod.reg_hotfix(hf_type, hf_target,
                                        ps_name,
                                        f'{reqmod_attr}{attr}',
                                        round(reqmod[attr]/scale, 6),
                                        notify=notify,
                                        )
                    for module_idx, module_obj in enumerate(lod['Modules']):
                        module = ps_obj[module_obj['export']-1]
                        module_attr = f'{lod_attr}Modules.Modules[0].Object..'
                        if 'Lifetime' in module:
                            for attr in ['MinValue', 'MaxValue']:
                                if attr in module['Lifetime']:
                                    done_work = True
                                    mod.reg_hotfix(hf_type, hf_target,
                                            ps_name,
                                            f'{module_attr}Lifetime.{attr}',
                                            round(module['Lifetime'][attr]/scale, 6),
                                            notify=notify,
                                            )
                            if 'Table' in module['Lifetime'] and 'Values' in module['Lifetime']['Table']:
                                for value_idx, value in enumerate(module['Lifetime']['Table']['Values']):
                                    done_work = True
                                    mod.reg_hotfix(hf_type, hf_target,
                                            ps_name,
                                            f'{module_attr}Lifetime.Table.Values.Values[{value_idx}]',
                                            round(value/scale, 6),
                                            notify=notify,
                                            )
                            if 'Distribution' in module['Lifetime']:
                                dist_obj = module['Lifetime']['Distribution']
                                dist = ps_obj[dist_obj['export']-1]
                                if 'Constant' in dist:
                                    done_work = True
                                    mod.reg_hotfix(hf_type, hf_target,
                                            ps_name,
                                            f'{module_attr}Lifetime.Distribution.Object..Constant',
                                            round(dist['Constant']/scale, 6),
                                            notify=notify,
                                            )

            break

    # Report if we didn't actually get any work
    if not done_work:
        print(f'WARNING: ParticleSystem had no edits: {ps_name}')

mod.header('Item Pickups')

# Defaults:
#  /Game/GameData/GameplayGlobals
#  - MassPickupMaxDelay: 0.075
#  - MassPickupMaxPullAmount: 6
#  - MassPickupMaxTotalDelay: 1.5
#  - MassPickupMinDelay: 0.06
#  - MassPickupRadius: 400
#  /Game/Pickups/_Shared/_Design/AutoLootContainerPickupFlyToSettings
#  - MaxLifetime: 2.5
#  - SpinSpeed: (pitch=0, yaw=200, roll=200)
#  - LinearSpeed: 750
#  - LinearAcceleration: 650

mod.comment('Mass Pickup Delay (honestly not sure if these have much, if any, effect)')
for var, value in [
        ('MassPickupMaxDelay', 0.075/3),
        ('MassPickupMaxTotalDelay', 1.5/3),
        ('MassPickupMinDelay', 0.06/3),
        ]:
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/GameplayGlobals',
            var,
            round(value, 6))
mod.newline()

mod.comment('Pickup flight speeds (likewise, I suspect many of these don\'t actually do much)')
mod.comment('The `AutoLootContainer` ones definitely do help, at least.')
for obj_name in [
        'AutoLootContainerPickupFlyToSettings',
        'ContainerEchoLogPickupFlyToSettings',
        'ContainerPickupFlyToSettings',
        'DroppedEchoLogPickupFlyToSettings',
        'DroppedPickupFlyToSettings',
        ]:
    full_obj_name = f'/Game/Pickups/_Shared/_Design/{obj_name}'
    obj_data = data.get_exports(full_obj_name, 'PickupFlyToData')[0]
    if 'LinearSpeed' in obj_data:
        speed = obj_data['LinearSpeed']
    else:
        # This seems to be the default
        speed = 1000
    mod.reg_hotfix(Mod.PATCH, '',
            full_obj_name,
            'LinearSpeed',
            speed*2)
    mod.reg_hotfix(Mod.PATCH, '',
            full_obj_name,
            'LinearAcceleration',
            obj_data['LinearAcceleration']*2)
mod.newline()

# Make Fast Travel + Teleport digistruct animations disappear
# (note that the death respawn is totally separate from this, and handled via
# some AnimSequence tweaks above)
mod.header('Fast Travel / Teleport Animation Disable')

# A bunch of silliness in here, when I was looking at bundling this separately
# as its own mod and was considering multiple versions.  In the end, this just
# hardcodes an effective disabling of the whole sequence, and I could omit
# various bits of math.  But whatever, the work is done -- leaving it as-is.
default_duration = 6.5
default_unlock = 5.5
default_teleport = 1.5
unlock_scale = default_unlock/default_duration
teleport_scale = default_teleport/default_duration

# 0.5 - Effectively disables it
# 2 - Quite short, but still gets a tiny bit of the tunnel
new_duration = 0.5

min_timers = min(default_teleport, new_duration)

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PlayerCharacters/_Shared/_Design/Travel/Action_TeleportEffects.Default__Action_TeleportEffects_C',
        'Duration',
        new_duration,
        )

# Adjust delay on unlocking resources (whatever that means; haven't figured out
# what's not available when "locked")
mod.bytecode_hotfix(Mod.PATCH, '',
        '/Game/PlayerCharacters/_Shared/_Design/Travel/Action_TeleportEffects',
        'ExecuteUbergraph_Action_TeleportEffects',
        1119,
        default_unlock,
        max(min_timers, round(new_duration*unlock_scale, 6)),
        )

# Adjust delay on actually teleporting
mod.bytecode_hotfix(Mod.PATCH, '',
        '/Game/PlayerCharacters/_Shared/_Design/Travel/Action_TeleportEffects',
        'ExecuteUbergraph_Action_TeleportEffects',
        391,
        default_teleport,
        max(min_timers, round(new_duration*teleport_scale, 6)),
        )

mod.newline()

# Photo Mode activation time
# I actually *don't* want to alter deactivation time, since Photo Mode can be used
# to pick up gear or hit buttons that you wouldn't otherwise be able to reach,
# while the camera's zooming back to your char.  That's even occasionally important
# with this mod active, such as getting to the Typhon Dead Drop in Meridian
# Outskirts without having to go all the way around the level.
mod.header('Photo Mode Activation Time')
mod.bytecode_hotfix(Mod.PATCH, '',
        '/Game/GameData/BP_PhotoModeController',
        'ExecuteUbergraph_BP_PhotoModeController',
        # 187 is the deactivation index (also default of 1.5)
        122,
        1.5,
        1.5/global_scale,
        )
mod.newline()

class AS():
    """
    Little wrapper class so that I can more easily loop over a bunch of AnimSequence
    objects which largely use the defaults but occasionally need to tweak some stuff.

    When I was pretty far along in this mod, I discovered that GbxLevelSequenceActor
    objects have a SequencePlayer sub-object with a PlayRate attr which often ends
    up producing better results than tweaking the AnimSequence timings themselves.
    I suspect that a lot of our AnimSequence tweaks that we do via this class would
    probably be better done via that method instead, though I definitely don't feel
    like having to re-test huge chunks of the game.  Also there probably *are*
    various circumstances where we'd need to tweak AnimSequences anyway, so I don't
    think this was wasted work.  Still, I suspect a bunch of bulk could be cut
    back into some simpler PlayRate adjustments if I were ever willing to take the
    time to do it.
    """

    def __init__(self, path, scale=None, seqlen_scale=None, extra_char=None, method=Mod.LEVEL, target=None):
        self.path = path
        self.scale = scale
        self.seqlen_scale = seqlen_scale
        self.extra_char = extra_char
        self.method = method
        self.target = target

    def _do_scale(self, mod, data, hf_trigger, hf_target):
        """
        Method to shorten animation sequences
        """

        # Serialize the data
        as_data = data.get_exports(self.path, 'AnimSequence')[0]

        # First the RateScale; happens regardless of AnimSequence contents
        mod.reg_hotfix(hf_trigger, hf_target,
                self.path,
                'RateScale',
                self.scale)

        # Now Notifies
        if 'Notifies' in as_data:
            for idx, notify in enumerate(as_data['Notifies']):
                # TODO: Should we also do `Duration`?  Few objects have that one...
                for var in ['SegmentBeginTime', 'SegmentLength', 'LinkValue']:
                    if var in notify and notify[var] != 0:
                        mod.reg_hotfix(hf_trigger, hf_target,
                                self.path,
                                'Notifies.Notifies[{}].{}'.format(idx, var),
                                round(notify[var]/self.scale, 6))

                # If we have targets inside EndLink, process that, too.  (So far, it doesn't
                # look like any animations we touch actually have anything here.)
                endlink = notify['EndLink']
                if 'export' not in endlink['LinkedMontage'] \
                        or endlink['LinkedMontage']['export'] != 0 \
                        or 'export' not in endlink['LinkedSequence'] \
                        or endlink['LinkedSequence']['export'] != 0:
                    for var in ['SegmentBeginTime', 'SegmentLength', 'LinkValue']:
                        if var in endlink and endlink[var] != 0:
                            mod.reg_hotfix(hf_trigger, hf_target,
                                    self.path,
                                    'Notifies.Notifies[{}].EndLink.{}'.format(idx, var),
                                    round(endlink[var]/self.scale, 6))

        # Finally: SequenceLength.  This one's a bit weird, which is why we're letting categories
        # decide if they want to use alt scalings.  For player animations for entering/leaving vehicles
        # (or for changing seats), if SequenceLength is scaled at the same scale as the rest of the
        # animations, the animation "freezes" before it's fully complete, and the player just jerks
        # to their final spot once the appropriate time has elapsed.  Contrariwise, if we *don't*
        # scale SequenceLength down, you end up with a period of time where you can't interact with
        # the vehicle at all, like driving, leaving, or changing seats again.  In the end, I settled
        # on just using the global vehicle scale for all categories here, but if I want to tweak
        # something in the future, at least it's easy enough to do so.
        if 'SequenceLength' in as_data:
            mod.reg_hotfix(hf_trigger, hf_target,
                    self.path,
                    'SequenceLength',
                    round(as_data['SequenceLength']/self.seqlen_scale, 6))

    def do_scale(self, mod, data):
        if self.target is None:
            if self.method == Mod.PATCH:
                target = ''
            elif self.method == Mod.LEVEL or self.method == Mod.CHAR:
                target = 'MatchAll'
            else:
                raise RuntimeError(f'Unknown method for AnimSequence patching: {self.method}')
        else:
            target = self.target
        self._do_scale(mod, data, self.method, target)
        if self.extra_char:
            self._do_scale(mod, data, Mod.CHAR, self.extra_char)

# Vehicles!
#
# Command for these: find $(find . -name Vehicles -o -name Vehicle) -name "AS_*.uasset" | sort -i | cut -d. -f2 | grep -vE '(Idle|Flinch|Death|Land|Emperor)'
# ... though it's been trimmed quite heavily and reorganized quite a bit.
for vehicle_cat, hf_trigger, vehicle_scale, sequencelength_scale, animseqs in [
        ('Player Basic Interactions (always loaded objects)', Mod.PATCH, global_vehicle_scale, global_vehicle_scale, [
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/CraneConsole/AS_Console_Enter'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/CraneConsole/AS_Console_Exit'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/GunnersNest/AS_GunnersNest_Entry'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/GunnersNest/AS_GunnersNest_Exit'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Enter_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Enter_R'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Exit_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Exit_R'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Standing_Enter'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Standing_Exit'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Enter_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Enter_R'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Exit_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Exit_R'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_to_Turret'),
            #AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Enter_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Enter_R'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Exit'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_to_Driver'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Enter_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Enter_R'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Exit_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Exit_R'),
            #AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Enter_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Enter_R'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Exit'),
            #AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_FB'),
            #AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_LR'),
            #AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_UD'),
            #AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Shared/AS_Base_Pose'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_BL_Enter'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_BL_Exit'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_BR_Enter'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_BR_Exit'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_Enter'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_Exit'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_to_Turret'),
            #AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_Enter'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_Exit'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_to_Driver'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/CraneConsole/AS_Console_Enter'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/CraneConsole/AS_Console_Exit'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/GunnersNest/AS_GunnersNest_Entry'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/GunnersNest/AS_GunnersNest_Exit'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Enter_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Enter_R'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Exit_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Exit_R'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Standing_Enter'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Standing_Exit'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Enter_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Enter_R'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Exit_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Exit_R'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_to_Turret'),
            #AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Enter_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Enter_R'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Exit'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_to_Driver'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Enter_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Enter_R'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Exit_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Exit_R'),
            #AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Enter_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Enter_R'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Exit'),
            #AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_FB'),
            #AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_LR'),
            #AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_UD'),
            #AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Shared/AS_Base_Pose'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_BL_Enter'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_BL_Exit'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_BR_Enter'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_BR_Exit'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_Enter'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_Exit'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_to_Turret'),
            #AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_Enter'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_Exit'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_to_Driver'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/CraneConsole/AS_Console_Enter'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/CraneConsole/AS_Console_Exit'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/GunnersNest/AS_GunnersNest_Entry'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/GunnersNest/AS_GunnersNest_Exit'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Enter_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Enter_R'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Exit_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Exit_R'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Standing_Enter'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Standing_Exit'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Enter_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Enter_R'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Exit_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Exit_R'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_to_Turret'),
            #AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Enter_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Enter_R'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Exit'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_to_Driver'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Enter_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Enter_R'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Exit_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Exit_R'),
            #AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Enter_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Enter_R'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Exit'),
            #AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_FB'),
            #AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_LR'),
            #AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_UD'),
            #AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Shared/AS_Base_Pose'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_BL_Enter'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_BL_Exit'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_BR_Enter'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_BR_Exit'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_Enter'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_Exit'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_to_Turret'),
            #AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_Enter'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_Exit'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_to_Driver'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Crane/AS_Console_Enter'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Crane/AS_Console_Exit'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/GunnersNest/AS_GunnersNest_Entry'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/GunnersNest/AS_GunnersNest_Exit'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Enter_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Enter_R'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Exit_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Sitting_Exit_R'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Standing_Enter'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Standing_Exit'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Enter_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Enter_R'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Exit_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_Exit_R'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_to_Turret'),
            #AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Enter_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Enter_R'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_Exit'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Turret_to_Driver'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Enter_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Enter_R'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Exit_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_Exit_R'),
            #AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Revolver/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Enter_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Enter_R'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/RollerCoaster/AS_RollerCoaster_Exit'),
            #AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_FB'),
            #AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_LR'),
            #AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Shared/AS_ADD_UD'),
            #AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Shared/AS_Base_Pose'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_BL_Enter'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_BL_Exit'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_BR_Enter'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_BR_Exit'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_Enter'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_Exit'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_to_Turret'),
            #AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_TurnWheel_Backward'),
            #AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_Driver_TurnWheel'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_Enter'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_Exit'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_Turret_to_Driver'),
            ]),
        ('Player Basic Interactions (level-based objects)', Mod.LEVEL, global_vehicle_scale, global_vehicle_scale, [
            AS('/Dandelion/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Hyperhoop/AS_Hyperhoop_Enter'),
            AS('/Dandelion/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Hyperhoop/AS_Hyperhoop_Exit'),
            AS('/Dandelion/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Hyperhoop/AS_Hyperhoop_Enter'),
            AS('/Dandelion/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Hyperhoop/AS_Hyperhoop_Exit'),
            AS('/Dandelion/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Hyperhoop/AS_Hyperhoop_Enter'),
            AS('/Dandelion/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Hyperhoop/AS_Hyperhoop_Exit'),
            AS('/Dandelion/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicle/Hyperhoop/AS_Hyperhoop_Enter'),
            AS('/Dandelion/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicle/Hyperhoop/AS_Hyperhoop_Exit'),
            #AS('/Dandelion/Vehicles/Hyperloop/Animation/AS_Banking_Left'),
            #AS('/Dandelion/Vehicles/Hyperloop/Animation/AS_Banking_Right'),
            ]),
        ('Hijack Interactions - Player', Mod.PATCH, global_vehicle_scale, global_vehicle_scale, [
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Sitting_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Sitting_R'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Standing'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Hijack_Driver_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Hijack_Driver_R'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Hijack_Driver_to_Turret'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Revolver/AS_Hijack_Driver_L'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Revolver/AS_Hijack_Driver_R'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_Hijack_Driver_to_Turret'),
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/Vehicles/Technical/AS_Hijack_Driver'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Sitting_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Sitting_R'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Standing'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_HiJack_Driver_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_HiJack_Driver_R'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Hijack_Driver_to_Turret'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Revolver/AS_HiJack_Driver_L'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Revolver/AS_HiJack_Driver_R'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_Hijack_Driver_to_Turret'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/Vehicles/Technical/AS_HiJack_Driver'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Sitting_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Sitting_R'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Standing'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_HiJack_Driver_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Hijack_Driver_R'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Hijack_Driver_to_Turret'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Revolver/AS_Hijack_Driver_L'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Revolver/AS_Hijack_Driver_R'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_Hijack_Driver_to_Turret'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/Vehicles/Technical/AS_HiJack_Driver'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Sitting_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Sitting_R'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/MannedTurret/AS_Hijack_Standing'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_HiJack_Driver_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_HiJack_Driver_R'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Outrunner/AS_Hijack_Driver_to_Turret'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Revolver/AS_HiJack_Driver_L'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Revolver/AS_HiJack_Driver_R'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_Hijack_Driver_to_Turret'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/Vehicles/Technical/AS_HiJack_Driver'),
            ]),
        ('NPC Basic Interactions', Mod.CHAR, global_vehicle_scale, global_vehicle_scale, [
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Enter_L'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Enter_R'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Exit_L'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Exit_R'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Standing_Enter'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Standing_Exit'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_Driver_Enter_L'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_Driver_Enter_R'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_Driver_Exit_L'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_Driver_Exit_R'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_Driver_TurnWheel'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_LeapB_Attack'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_LeapB_Exit'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_LeapB_Unstable'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_LeapF_Attack'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_LeapF_Exit'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_LeapF_Unstable'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Enter_L'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Enter_R'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Exit'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Revolver/AS_Driver_Enter_L'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Revolver/AS_Driver_Enter_R'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Revolver/AS_Driver_Exit_L'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Revolver/AS_Driver_TurnWheel'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Shared/AS_ADD_FB'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Shared/AS_ADD_LR'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Shared/AS_ADD_UD'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Shared/AS_Base_Pose'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Shared/AS_VehicleLeap_Enter'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_BL_Enter'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_BL_Exit'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_BR_Enter'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_BR_Exit'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_Driver_Enter'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_Driver_Exit'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_Driver_TurnWheel'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_LeapFL_Attack'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_LeapFL_Exit'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_LeapFL_Unstable'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_LeapFR_Attack'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_LeapFR_Exit'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_LeapFR_Unstable'),
            #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_Turret_Enter'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_Turret_Exit'),
            #AS('/Game/Enemies/Punk_Male/_Shared/Animation/Vehicles/Technical/AS_BL_Enter'),
            AS('/Game/Enemies/Punk_Male/_Shared/Animation/Vehicles/Technical/AS_BL_Exit'),
            #AS('/Game/Enemies/Punk_Male/_Shared/Animation/Vehicles/Technical/AS_BR_Enter'),
            AS('/Game/Enemies/Punk_Male/_Shared/Animation/Vehicles/Technical/AS_BR_Exit'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Enter_L'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Enter_R'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Exit_L'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Exit_R'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Standing_Enter'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Standing_Exit'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_Driver_Enter_L'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_Driver_Enter_R'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_Driver_Exit_L'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_Driver_TurnWheel'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Enter_L'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Enter_R'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Exit'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Revolver/AS_Driver_Enter_L'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Revolver/AS_Driver_Enter_R'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Revolver/AS_Driver_Exit_L'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Revolver/AS_Driver_Exit_R'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Revolver/AS_Driver_TurnWheel'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Shared/AS_ADD_FB'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Shared/AS_ADD_LR'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Shared/AS_ADD_UD'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Shared/AS_Base_Pose'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_BL_Enter'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_BL_Exit'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_BR_Enter'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_BR_Exit'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_Driver_Enter'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_Driver_Exit'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_Driver_TurnWheel'),
            #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_Turret_Enter'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_Turret_Exit'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/MannedTurret/AS_Sitting_Enter_L'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/MannedTurret/AS_Sitting_Enter_R'),
            AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/MannedTurret/AS_Sitting_Exit_L'),
            AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/MannedTurret/AS_Sitting_Exit_R'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/MannedTurret/AS_Standing_Enter'),
            AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/MannedTurret/AS_Standing_Exit'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Shared/AS_ADD_FB'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Shared/AS_ADD_LR'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Shared/AS_ADD_UD'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Shared/AS_Base_Pose'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Technical/AS_BL_Enter'),
            AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Technical/AS_BL_Exit'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Technical/AS_BR_Enter'),
            AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Technical/AS_BR_Exit'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Technical/AS_Driver_Enter'),
            AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Technical/AS_Driver_Exit'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Technical/AS_Driver_TurnWheel'),
            #AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Technical/AS_Turret_Enter'),
            AS('/Game/NonPlayerCharacters/AtlasSoldier/Animation/Vehicles/Technical/AS_Turret_Exit'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Enter_L'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Enter_R'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Exit_L'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Exit_R'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/MannedTurret/AS_Standing_Enter'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/MannedTurret/AS_Standing_Exit'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Outrunner/AS_Driver_Enter_L'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Outrunner/AS_Driver_Enter_R'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Outrunner/AS_Driver_Exit_L'),
            #AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Outrunner/AS_Driver_TurnWheel'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Enter_L'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Enter_R'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Exit'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Revolver/AS_Driver_Enter_L'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Revolver/AS_Driver_Enter_R'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Revolver/AS_Driver_Exit_L'),
            #AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Revolver/AS_Driver_TurnWheel'),
            #AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Shared/AS_ADD_FB'),
            #AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Shared/AS_ADD_LR'),
            #AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Shared/AS_ADD_UD'),
            #AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Shared/AS_Base_Pose'),
            #AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_AllyDriver_Brace'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_AllyDriver_Enter'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_AllyDriver_Exit'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_BL_Enter'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_BL_Exit'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_BR_Enter'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_BR_Exit'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_Driver_Enter'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_Driver_Exit'),
            #AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_Driver_TurnWheel'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_Turret_Enter'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/AS_Turret_Exit'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/Passive/AS_BL_Enter'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/Passive/AS_BL_Exit'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/Passive/AS_BR_Enter'),
            AS('/Game/NonPlayerCharacters/_Generic/_Shared/Animation/Vehicles/Technical/Passive/AS_BR_Exit'),
            #AS('/Game/NonPlayerCharacters/Lilith/Animation/Vehicles/Revolver/AS_Driver_Enter_L'),
            #AS('/Game/NonPlayerCharacters/Lilith/Animation/Vehicles/Revolver/AS_Driver_Enter_R'),
            #AS('/Game/NonPlayerCharacters/Lilith/Animation/Vehicles/Revolver/AS_Driver_Exit_L'),
            #AS('/Game/NonPlayerCharacters/Lilith/Animation/Vehicles/Revolver/AS_Driver_TurnWheel'),
            #AS('/Game/NonPlayerCharacters/Lilith/Animation/Vehicles/Shared/AS_ADD_FB'),
            #AS('/Game/NonPlayerCharacters/Lilith/Animation/Vehicles/Shared/AS_ADD_LR'),
            #AS('/Game/NonPlayerCharacters/Lilith/Animation/Vehicles/Shared/AS_ADD_UD'),
            #AS('/Game/NonPlayerCharacters/Lilith/Animation/Vehicles/Shared/AS_Base_Pose'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Shared/AS_ADD_FB'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Shared/AS_ADD_LR'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Shared/AS_ADD_UD'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Shared/AS_AllyPassenger_BasePose'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_Attack'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_BackLeft_AO_CC'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_BackLeft_AO_CD'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_BackLeft_AO_CU'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_BackLeft_AO_LC'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_BackLeft_AO_LD'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_BackLeft_AO_LU'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_BackLeft_AO_RC'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_BackLeft_AO_RD'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_BackLeft_AO_RU'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_BackLeft_Attack'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_Brace'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_Charge_In'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_Enter'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_Exit'),
            #AS('/Game/NonPlayerCharacters/Maya/Animation/Vehicle/Technical/AS_AllyPassenger_Shield'),
            #AS('/Game/NonPlayerCharacters/Vaughn/Animation/Vehicles/Shared/AS_ADD_FB'),
            #AS('/Game/NonPlayerCharacters/Vaughn/Animation/Vehicles/Shared/AS_ADD_LR'),
            #AS('/Game/NonPlayerCharacters/Vaughn/Animation/Vehicles/Shared/AS_ADD_UD'),
            #AS('/Game/NonPlayerCharacters/Vaughn/Animation/Vehicles/Shared/AS_AllyPassenger_BasePose'),
            #AS('/Game/NonPlayerCharacters/Vaughn/Animation/Vehicles/Technical/AS_AllyDriver_Brace'),
            #AS('/Game/NonPlayerCharacters/Vaughn/Animation/Vehicles/Technical/AS_AllyDriver_Enter'),
            #AS('/Game/NonPlayerCharacters/Vaughn/Animation/Vehicles/Technical/AS_AllyDriver_Exit'),
            ]),
        ('Hijack Interactions - Enemies', Mod.CHAR, global_vehicle_scale, global_vehicle_scale, [
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Hijack_Sitting_L'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Hijack_Sitting_R'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Hijack_Standing'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_HiJack_Driver_L'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_HiJack_Driver_R'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_Hijack_Driver_to_Turret'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Revolver/AS_Hijack_Driver_L'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Revolver/AS_Hijack_Driver_R'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Shared/AS_HiJacked_Ejected'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_Hijack_Driver_to_Turret'),
            AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_Hijack_Driver'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Hijack_Sitting_L'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Hijack_Sitting_R'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Hijack_Standing'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_HiJack_Driver_L'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_HiJack_Driver_R'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_Hijack_Driver_to_Turret'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Revolver/AS_HiJack_Driver_L'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Revolver/AS_HiJack_Driver_R'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_Hijack_Driver_to_Turret'),
            AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_HiJack_Driver'),
            ]),
        #('Other (unused, currently)', Mod.LEVEL, global_vehicle_scale, global_vehicle_scale, [
        #    AS('/Game/Vehicles/Carnivora/Animation/AS_Entry_drop'),
        #    AS('/Game/Vehicles/Carnivora/Animation/AS_Entry_idle'),
        #    AS('/Game/Vehicles/Carnivora/Animation/AS_Magnet_Drop'),
        #    AS('/Game/Vehicles/Outrunner/Animation/AS_Outrunner_GearShift_Down'),
        #    AS('/Game/Vehicles/Outrunner/Animation/AS_Outrunner_GearShift_Up'),
        #    AS('/Game/Vehicles/Outrunner/Animation/AS_Vehicle_Spawn_DoorCargoSplit'),
        #    AS('/Game/Vehicles/Revolver/Animation/AS_Gunner_Enter_L'),
        #    AS('/Game/Vehicles/Revolver/Animation/AS_Gunner_Exit_L'),
        #    AS('/Game/Vehicles/Revolver/Animation/AS_Revolver_GearShift_Down'),
        #    AS('/Game/Vehicles/Revolver/Animation/AS_Revolver_GearShift_Up'),
        #    AS('/Game/Vehicles/Revolver/Animation/AS_Vehicle_Spawn_DoorCargoSplit'),
        #    AS('/Game/Vehicles/Technical/Animation/AS_Technical_BrakeBounce_B'),
        #    AS('/Game/Vehicles/Technical/Animation/AS_Technical_BrakeBounce_F'),
        #    AS('/Game/Vehicles/Technical/Animation/AS_Technical_GearShift_Down'),
        #    AS('/Game/Vehicles/Technical/Animation/AS_Technical_GearShift_Up'),
        #    AS('/Game/Vehicles/Technical/Animation/AS_Technical_Gunner_Driver_Enter'),
        #    AS('/Game/Vehicles/Technical/Animation/AS_Technical_Gunner_Driver_Exit'),
        #    AS('/Game/Vehicles/Technical/Animation/AS_Technical_Hit_HoodDown'),
        #    AS('/Game/Vehicles/Technical/Animation/AS_Vehicle_Spawn_DoorCargoSplit'),
        #    AS('/Game/Vehicles/Technical/Parts/JetBooster/AS_JetBooster_Anim'),
        #    AS('/Game/Vehicles/Technical/Parts/MeatGrinder/AS_Veh_Techincal_MeatGrinder'),
        #    AS('/Game/Vehicles/Technical/Parts/ToxicBooster/AS_Veh_Technical_ToxicBooster'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/BouncingLasers/AS_BouncingLasers_Shoot'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/Catapult/AS_Launch'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/Catapult_TireBombs/AS_Launch'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/DualFlakCanon/AS_Veh_Turret_DualFlakCanon_Shoot_Primary'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/HeavyMissile/AS_HeavyMissile_Shoot'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/MachineGun/AS_MachineGun_Shoot_Heavy'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/MachineGun/AS_MachineGun_Shoot'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/PulseRifle/Animation/AS_PulseRifle_DualTurrets_Deploy_In'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/PulseRifle/Animation/AS_PulseRifle_DualTurrets_Deploy_Out'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/PulseRifle/Animation/AS_PulseRifle_DualTurrets_Retracted'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/PulseRifle/Animation/AS_PulseRifle_Shoot'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/RodLauncher/AS_Veh_Turret_RodLauncher_Shoot_Primary'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/SawBlade/AS_Veh_Turret_SawBlade_Shoot_Primary'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/ShotgunMissile/AS_ShotgunMissile_Shoot'),
        #    AS('/Game/Vehicles/VehicleWeapons/_Shared/WeaponModels/SwarmerMissile/AS_SwarmerMissile_Shoot'),
        #    AS('/Geranium/NonPlayerCharacters/Dakota/Animation/Vehicles/JetBeast/AS_Driver_Exit_L'),
        #    AS('/Geranium/Vehicles/Horse/Animation/Cannon/AS_Fire'),
        #    AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Idle'),
        #    AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/MannedTurret/AS_Standing_Idle'),
        #    AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_LeapB_Idle'),
        #    AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_LeapF_Idle'),
        #    AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Idle'),
        #    #AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Shared/AS_ADD_Idle'),
        #    AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Shared/AS_VehicleLeap_Idle'),
        #    AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_LeapFL_Idle'),
        #    AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_LeapFR_Idle'),
        #    AS('/Game/Enemies/Psycho_Male/_Shared/Animation/Vehicles/Technical/AS_Turret_Idle'),
        #    AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Sitting_Idle'),
        #    AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/MannedTurret/AS_Standing_Idle'),
        #    AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Outrunner/AS_Turret_Idle'),
        #    #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Shared/AS_ADD_Idle'),
        #    #AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_BL_Idle'),
        #    AS('/Game/Enemies/Trooper/_Shared/Animation/Vehicles/Technical/AS_Turret_Idle'),
        #    ]),
        ]:

    mod.header('Vehicle Speedups: {}'.format(vehicle_cat))

    for animseq in animseqs:

        if verbose:
            print('Processing {}'.format(animseq.path))

        animseq.method = hf_trigger
        animseq.scale = vehicle_scale
        animseq.seqlen_scale = sequencelength_scale

        mod.comment(animseq.path)
        animseq.do_scale(mod, data)
        mod.newline()

# Default here is 2.36; not gonna bother dynamically reading it for a single object.
# This honestly doesn't really do much for you -- the vehicle is basically fully
# operable as soon as it starts, anyway.  Still, it makes things look a little
# snappier.
mod.header('Catch-A-Ride Digistruct Time')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
        '/Game/GameData/StatusEffects/CoordinatedEffects/Vehicles/BP_CE_Veh_Digistruct_In.Default__BP_CE_Veh_Digistruct_In_C',
        'Duration',
        0.5)
mod.newline()

# Vault Card Chest injection!  So: the Vault Card menu uses a custom red chest
# to do the animation, and the chest object in the UI structure also uses a custom
# opening animation.  Those objects don't ordinarily exist until the Vault Card
# menu has been opened, though, and they disappear once the menu is closed.  So,
# our hotfixes can't touch them unless we inject the chest into each map first.
# So that's what we're doing here!  One further wrinkle is that the "stock" custom
# red chest object doesn't actually use the animation that the menu-spawned chest
# uses, so we *also* have to force that reference to exist, so that we can hotfix
# the proper animation.  Just 395 hotfixes (including the actual animation-speedup
# ones) to get this working!  Totally worth it.
mod.header('Vault Card Chest Injection (needed in order to speed up their opening animation)')
for level_full in [
        '/Alisma/Maps/Anger/Anger_P',
        '/Alisma/Maps/Chase/Chase_P',
        '/Alisma/Maps/Eldorado/Eldorado_P',
        '/Alisma/Maps/Experiment/Experiment_P',
        '/Alisma/Maps/Sanctum/Sanctum_P',
        '/Dandelion/Maps/CasinoIntro/CasinoIntro_P',
        '/Dandelion/Maps/Core/Core_P',
        '/Dandelion/Maps/Impound/Impound_P',
        '/Dandelion/Maps/Strip/Strip_P',
        '/Dandelion/Maps/TowerLair/TowerLair_P',
        '/Dandelion/Maps/Trashtown/Trashtown_P',
        '/Game/Maps/ProvingGrounds/Trial1/ProvingGrounds_Trial1_P',
        '/Game/Maps/ProvingGrounds/Trial4/ProvingGrounds_Trial4_P',
        '/Game/Maps/ProvingGrounds/Trial5/ProvingGrounds_Trial5_P',
        '/Game/Maps/ProvingGrounds/Trial6/ProvingGrounds_Trial6_P',
        '/Game/Maps/ProvingGrounds/Trial7/ProvingGrounds_Trial7_P',
        '/Game/Maps/ProvingGrounds/Trial8/ProvingGrounds_Trial8_P',
        '/Game/Maps/Sanctuary3/Sanctuary3_P',
        '/Game/Maps/Slaughters/COVSlaughter/COVSlaughter_P',
        '/Game/Maps/Slaughters/CreatureSlaughter/CreatureSlaughter_P',
        '/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_P',
        '/Game/Maps/Zone_0/FinalBoss/FinalBoss_P',
        '/Game/Maps/Zone_0/Prologue/Prologue_P',
        '/Game/Maps/Zone_0/Recruitment/Recruitment_P',
        '/Game/Maps/Zone_0/Sacrifice/Sacrifice_P',
        '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_P',
        '/Game/Maps/Zone_1/City/City_P',
        '/Game/Maps/Zone_1/CityBoss/CityBoss_P',
        '/Game/Maps/Zone_1/CityVault/CityVault_P',
        '/Game/Maps/Zone_1/Monastery/Monastery_P',
        '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_P',
        '/Game/Maps/Zone_1/Outskirts/Outskirts_P',
        '/Game/Maps/Zone_1/Towers/Towers_P',
        '/Game/Maps/Zone_2/Mansion/Mansion_P',
        '/Game/Maps/Zone_2/MarshFields/MarshFields_P',
        '/Game/Maps/Zone_2/Prison/Prison_P',
        '/Game/Maps/Zone_2/Watership/Watership_P',
        '/Game/Maps/Zone_2/Wetlands/Wetlands_P',
        '/Game/Maps/Zone_2/WetlandsBoss/WetlandsBoss_P',
        '/Game/Maps/Zone_2/WetlandsVault/WetlandsVault_P',
        '/Game/Maps/Zone_3/Convoy/Convoy_P',
        '/Game/Maps/Zone_3/Desert/Desert_P',
        '/Game/Maps/Zone_3/DesertBoss/DesertBoss_P',
        '/Game/Maps/Zone_3/DesertVault/Desertvault_P',
        '/Game/Maps/Zone_3/Mine/Mine_P',
        '/Game/Maps/Zone_3/Motorcade/Motorcade_P',
        '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_P',
        '/Game/Maps/Zone_3/MotorcadeInterior/MotorcadeInterior_P',
        '/Game/Maps/Zone_4/Beach/Beach_P',
        # For some reason, injecting this chest in Crypt_P causes Tannis+Typhon to get
        # stuck right at the beginning of the map, after the first door opens.  No idea
        # why, though clearly the chest is stealing an event, or just getting in the
        # way of an event delivery.  Seriously bizarre.  I did try using a few other
        # red chest variants as well, and even a white chest, and all of them ended
        # up exhibiting the same behavior, too.
        #'/Game/Maps/Zone_4/Crypt/Crypt_P',
        '/Game/Maps/Zone_4/Desolate/Desolate_P',
        '/Game/PatchDLC/BloodyHarvest/Maps/Seasons/BloodyHarvest/BloodyHarvest_P',
        '/Game/PatchDLC/Event2/Maps/Cartels_P',
        '/Game/PatchDLC/Raid1/Maps/Raid/Raid_P',
        '/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_P',
        '/Geranium/Maps/CraterBoss/CraterBoss_P',
        '/Geranium/Maps/Facility/Facility_P',
        '/Geranium/Maps/Forest/Forest_P',
        '/Geranium/Maps/Frontier/Frontier_P',
        '/Geranium/Maps/Lodge/Lodge_P',
        '/Geranium/Maps/Town/Town_P',
        '/Hibiscus/Maps/Archive/Archive_P',
        '/Hibiscus/Maps/Bar/Bar_P',
        '/Hibiscus/Maps/Camp/Camp_P',
        '/Hibiscus/Maps/Lake/Lake_P',
        '/Hibiscus/Maps/Venue/Venue_P',
        '/Hibiscus/Maps/Village/Village_P',
        '/Hibiscus/Maps/Woods/Woods_P',
        '/Ixora/Maps/FrostSite/FrostSite_P',
        '/Ixora2/Maps/Boss/SacrificeBoss_p',
        '/Ixora2/Maps/Cabin/Cabin_P',
        '/Ixora2/Maps/Mystery/Nekro/NekroMystery_p',
        '/Ixora2/Maps/Mystery/Pandora/PandoraMystery_p',
        '/Ixora2/Maps/Noir/Noir_P',
        ]:
    level_short = level_full.rsplit('/', 1)[-1]
    level_label = LVL_TO_ENG_LOWER[level_short.lower()]
    mod.comment(level_label)
    chest_name = mod.streaming_hotfix(level_full,
            '/Game/PatchDLC/VaultCard/InteractiveObjects/BPIO_Lootable_VaultCard_RedCrate',
            location=(99999,99999,99999),
            )
    mod.reg_hotfix(Mod.LEVEL, level_short,
            chest_name,
            'OpeningInteractions.OpeningInteractions[0].TransitionAnimation',
            Mod.get_full_cond('/Game/PatchDLC/VaultCard/AS_Open_v2', 'AnimSequence'),
            )
    mod.newline()

# Direct animation speedups
mod.header('Simple Animation Speedups')
for cat_name, cat_scale, animseqs in [
        ('Containers', global_scale, [
            # Initial object list generated by:
            #     find $(find . -type d -name Lootables) -name "AS_*.uasset" | sort -i | cut -d. -f2 | grep -vE '(Idle|Flinch|_Closed|_Opened)'
            # ... while at the root of a data unpack
            AS('/Alisma/Lootables/Hyperion/AmmoCase/Animation/AS_Open_In'),
            AS('/Alisma/Lootables/Hyperion/LootCase/Animation/AS_Hyp_Misc2_Opening'),
            AS('/Alisma/Lootables/Hyperion/PortaPotty/Animation/AS_Open_IN_Poor'),
            AS('/Alisma/Lootables/Hyperion/PortaPotty/Animation/AS_Open_IN'),
            AS('/Alisma/Lootables/Hyperion/PortaPotty/Animation/AS_Open'),
            AS('/Alisma/Lootables/Hyperion/RedChest/Animation/AS_HypRedChest_Open'),
            AS('/Alisma/Lootables/Hyperion/SingleCase/Animation/AS_SingleCase_In'),
            AS('/Alisma/Lootables/Hyperion/WeaponBox/Animation/AS_HypWeaponLocker_Open'),
            AS('/Dandelion/LevelArt/Manufacturers/Hyperion/Props/SlotMachines/Animation/AS_PushButton_Open'),
            AS('/Dandelion/Lootables/Hyperion/AmmoCase/Animation/AS_Open_In'),
            # These four need a seqlen_scale of 1, otherwise you generally end up not actually seeing
            # at least one of the initial card draws.
            AS('/Dandelion/Lootables/Hyperion/BlackJackChest/Animation/AS_Open_Draw_card_01',
                seqlen_scale=1,
                ),
            AS('/Dandelion/Lootables/Hyperion/BlackJackChest/Animation/AS_Open_Draw_card_03',
                seqlen_scale=1,
                ),
            AS('/Dandelion/Lootables/Hyperion/BlackJackChest/Animation/AS_Open_Draw_card_04',
                seqlen_scale=1,
                ),
            AS('/Dandelion/Lootables/Hyperion/BlackJackChest/Animation/AS_Open_In',
                seqlen_scale=1,
                ),
            AS('/Dandelion/Lootables/Hyperion/LootCase/Animation/AS_Hyp_Misc2_Opening'),
            AS('/Dandelion/Lootables/Hyperion/PortaPotty/Animation/AS_Open_IN'),
            AS('/Dandelion/Lootables/Hyperion/RedChest/Animation/AS_HypRedChest_Open'),
            AS('/Dandelion/Lootables/Hyperion/SingleCase/Animation/AS_SingleCase_In'),
            AS('/Dandelion/Lootables/Hyperion/WeaponBox/Animation/AS_HypWeaponLocker_Open'),
            AS('/Game/Lootables/Atlas/Chest_Red/Animation/AS_Open'),
            AS('/Game/Lootables/Atlas/Crate_Ammo/Animation/AS_Open'),
            AS('/Game/Lootables/COV/Bandit_CardboardBox/Animation/AS_Open_Fast'),
            AS('/Game/Lootables/COV/Bandit_CardboardBox/Animation/AS_Open_Slow'),
            AS('/Game/Lootables/COV/Chest_Red/Animation/AS_Open_v1'),
            AS('/Game/Lootables/COV/Chest_White/Animations/AS_Open'),
            AS('/Game/Lootables/COV/Crate_Ammo/Animation/AS_Open_v1'),
            AS('/Game/Lootables/COV/Crate_OfferingBox/Animation/AS_Open_v1'),
            AS('/Game/Lootables/Eridian/Chest_Red/Animation/AS_Open'),
            AS('/Game/Lootables/Eridian/Chest_White/Animation/AS_Open'),
            AS('/Game/Lootables/Eridian/Crate_Ammo/Animation/AS_Open'),
            AS('/Game/Lootables/_Global/Chest_Gold/Animation/AS_Close'),
            AS('/Game/Lootables/_Global/Chest_Gold/Animation/AS_Open'),
            AS('/Game/Lootables/_Global/Chest_Trials/Animation/AS_Open'),
            AS('/Game/Lootables/_Global/Chest_Trials/Animation/AS_Open_v2'),
            AS('/Game/Lootables/_Global/Chest_Typhon/Animation/AS_Open',
                # Typhon Dead Drop doesn't seem to actually apply with just a Level hotfix.  I
                # suspect it gets loaded in too late, or something?  Anyway, applying a Char
                # hotfix instead seems to do the trick, so whatever.
                extra_char='MatchAll',
                ),
            AS('/Game/Lootables/_Global/Crate_Ammo/Animations/AS_Open'),
            AS('/Game/Lootables/_Global/Dumpster_Small/Animation/AS_Open'),
            AS('/Game/Lootables/_Global/Locker_Generic/Animation/AS_Open_Misnamed'),
            AS('/Game/Lootables/_Global/Locker_Generic/Animation/AS_Open',
                # This is necessary to get rid of a visual glitch (a not-fully-opened
                # locker) when picking up Ember's toolbox in Impound Deluxe, in Freddie's
                # hideout.  It looks like doing this doesn't negatively impact other
                # lockers throughout the game, though this means that locker-opening has
                # become the least-tested container in the game (I didn't make this
                # tweak until I was through with the primary mod-writing playthrough).
                # Still, I tested out the Sanctuary locker for The Kevin Konundrum,
                # and the Skywell-27 locker during Opposition Research, and those still
                # work fine too (in addition to a bunch of "regular" lockers I'd
                # tested), so I think we're good.  I suspect that we should probably
                # *default* to leaving the seqlen alone, rather than scaling it by
                # default and then specifying like this when we *don't* want it.
                # Still, that change would involve about a million times more re-testing
                # than I'm willing to do, so eh.
                seqlen_scale=1,
                ),
            AS('/Game/Lootables/Industrial/Cash_Register/Animation/AS_Open'),
            AS('/Game/Lootables/Industrial/Lock_Box/Animations/AS_Open'),
            AS('/Game/Lootables/Industrial/Machine_Washing/Animation/AS_Open'),
            AS('/Game/Lootables/Industrial/PortaPotty/Animation/AS_BlastOff'),
            AS('/Game/Lootables/Industrial/PortaPotty/Animation/AS_Open_v1'),
            AS('/Game/Lootables/Industrial/Refrigerator/Animation/AS_Open'),
            AS('/Game/Lootables/Industrial/Safe/Animation/AS_Open'),
            AS('/Game/Lootables/Industrial/Strong_Box/Animation/AS_Open'),
            AS('/Game/Lootables/Industrial/Toilet/Animations/AS_Open'),
            AS('/Game/Lootables/Industrial/Trunk_Car/Animation/AS_Open_Backfire'),
            AS('/Game/Lootables/Industrial/Trunk_Car/Animation/AS_Open'),
            AS('/Game/Lootables/Jakobs/Chest_Red/Animation/AS_Open'),
            AS('/Game/Lootables/Jakobs/Chest_White/Animation/AS_Open'),
            AS('/Game/Lootables/Jakobs/GunRack/Animation/AS_Open'),
            AS('/Game/Lootables/Jakobs/Lockbox/Animation/AS_Open'),
            AS('/Game/Lootables/Jakobs/MusicBox/Animation/AS_Open'),
            AS('/Game/Lootables/Maliwan/Ammo/Animation/AS_Open_v1'),
            AS('/Game/Lootables/Maliwan/Chest_Red/Animation/AS_Open'),
            AS('/Game/Lootables/Maliwan/Chest_White/Animation/AS_Open'),
            AS('/Game/Lootables/Mission_Specific/Rock_HideAKey/Animation/AS_Open'),
            AS('/Game/Lootables/Pandora/Mailbox/Animation/AS_Open_v1'),
            AS('/Game/Lootables/Pandora/Mailbox/Animation/AS_Open_v2'),
            AS('/Game/Lootables/Pandora/TrashCan/Model/Animation/AS_Open_v1'),
            AS('/Game/Lootables/Pandora/TrashCan/Model/Animation/AS_Open_v2'),
            # This one doesn't show up in the find command above...
            AS('/Game/Lootables/Pandora/TrashCan/Model/Animation/Open_v3'),
            AS('/Game/Lootables/Pandora/Varkid_Lootable/_Shared/Animation/AS_Open_Burst'),
            AS('/Game/Lootables/Pandora/Varkid_Lootable/_Shared/Animation/AS_Open'),
            AS('/Game/Lootables/Promethea/Cooler/Animation/AS_Open'),
            AS('/Game/Lootables/Promethea/Gashapon/Animations/AS_Open'),
            AS('/Game/Lootables/Promethea/Ratch_pile/Animation/Ratch_Pile_Large/AS_Open'),
            AS('/Game/Lootables/Promethea/Ratch_pile/Animation/Ratch_Pile_Large_Open/AS_Open'),
            AS('/Game/Lootables/Promethea/Ratch_pile/Animation/Ratch_Pile_Small/AS_Open'),
            AS('/Game/Lootables/Promethea/Ratch_pile/Animation/Ratch_Pile_Small_Open/AS_Open'),
            AS('/Game/Lootables/Promethea/Toilet/Animation/AS_Open_v1'),
            # Make this one not *quite* as fast as the rest.  Also requires the injection
            # above this, otherwise this object won't exist yet.
            AS('/Game/PatchDLC/VaultCard/AS_Open_v2',
                    scale=2,
                    seqlen_scale=2,
                    ),
            AS('/Geranium/Lootables/CashRegister/Animation/AS_Open'),
            AS('/Geranium/Lootables/Chest_DeadDrop/Model/Anims/AS_Open_Ger'),
            AS('/Geranium/Lootables/_Design/Classes/AS_Open_MoneyBack'),
            AS('/Geranium/Lootables/Machine_Washing/Animation/AS_Close'),
            AS('/Geranium/Lootables/Outhouse/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/Carcass/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/Cultists/AmmoCrate/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/Cultists/RedChest/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/Cultists/UniqueChest/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/Cultists/WhiteChest/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/FishingNet/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/FrostBiters/AmmoCrate/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/FrostBiters/RedChest/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/FrostBiters/TreasureBox/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/FrostBiters/WhiteChest/Animation/AS_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/SingingFish/Animation/AS_Sing_Sing'),
            AS('/Hibiscus/InteractiveObjects/Lootables/SingingFish/Animation/AS_Sing_Spit'),
            AS('/Hibiscus/InteractiveObjects/Lootables/SingleMushroom/AS_Mush_Open'),
            AS('/Hibiscus/InteractiveObjects/Lootables/TentacleToilet/Animation/AS_TentacleToilet_OpenAndDropWeapon'),
            ]),
        ('Doors', door_scale, [
            # Called by IO_Door_1000x600_SlideUp_Promethea_Vehicle2, the door to the hub area in City_P,
            # and also before the big pit in OrbitalPlatform_P (after the thruster).  We're doing some
            # custom sequence scaling here 'cause in OrbitalPlatform_P, if we leave the animsequence
            # scaling at the default, the door animation freezes *right* at the beginning and doesn't
            # open hardly at all.  Leaving the sequence scale at 1 lets that work fine though, and the
            # animation is still sped up, so that should do for now.  It does make me wonder if we maybe
            # shouldn't be touching that value *at all*, but I guess I'll leave it for now.
            AS('/Game/InteractiveObjects/Doors/Eden_6/Door_Eden6_VehicleSpawner/Animation/AS_VehicleDoor_Open',
                seqlen_scale=1,
                ),
            # Gate to the "back" half of the Homestead, in Splinterlands, during Part 2 of that questline
            AS('/Game/MapSpecific/Motorcade/SmallDoor/Animation/AS_Opening',
                target='Motorcade_P',
                # This one, too, needs a sequence scale of 1, otherwise the animation gets very janky.  Wonder
                # if *all* custom door-related ASes will end up needing this...
                seqlen_scale=1,
                ),
            # Nekrotafeyo-style door, first seen in Pyre of Stars but it's also in the Guardian Takedown.
            # See the IO_Door_Custom_Nekro_Crypt_Small bytecode fix below, too.
            AS('/Game/InteractiveObjects/MissionSpecificObjects/Desolate/DoorCrypt/_Shared/Model/SK_Desolate_CryptDoor_Anim',
                target='MatchAll',
                seqlen_scale=1,
                ),
            ]),
        ('Other Mission Animations', global_scale, [
            AS('/Game/MapSpecific/Motorcade/Crane/Animation/AS_Going_Down',
                target='Motorcade_P',
                # At global_scale, the crane descends faster than in-game gravity, which makes
                # the Golden Chariot a bit unpredictable.  So, cut down on the scale a bit.
                # (Even at this scale, it bounces around a bit, but seems more stable to me.)
                scale=global_scale/2,
                # Need to do this, otherwise the animation glitches out
                seqlen_scale=1,
                ),
            AS('/Game/InteractiveObjects/MissionSpecificObjects/Ep14_MinerDetails/Pipe_Destroyed/Animation/AS_Pipe_Destroyed',
                target='Mine_P',
                # a 2x speedup already looks a *bit* off; this animation really doesn't need
                # much in the way of speeding up.
                scale=global_scale/2,
                # Need to do this, otherwise the animation glitches out
                seqlen_scale=1,
                ),
            AS('/Game/InteractiveObjects/MissionSpecificObjects/Beach/Eridian_Bridge/_Shared/Animation/AS_Bridge_Going_up',
                target='Beach_P',
                scale=global_scale/2,
                # Honestly not sure if we *do* need seqlen_scale=1 here; I just stuck it in assuming it'd
                # be needed, given the other animations in this section.
                seqlen_scale=1,
                ),
            # So this *does* speed up the cocking animation for catapult 3, but there's a delay in
            # the bytecode which uses the SequenceLength of this sequence.  We need to keep the seqlen
            # at its default value or the animation glitches out, as with the other animations in
            # this section.  So, we can either speed up the animation and have an awkward silence until
            # the mission moves along, or just cope with the standard animation speed.
            #AS('/Alisma/InteractiveObjects/MissionSpecific/Plot/ALI_EP02/Catapult/Exports/AS_IO_Catapult_Cocking',
            #    target='Anger_P',
            #    scale=2,
            #    seqlen_scale=1,
            #    ),
            ]),
        # Doing this ends up screwing up the slots pretty thoroughly, actually -- the animation gets killed
        # pretty much immediately, so the rewards get stuck "inside" the machine until the 10-sec auto-drop
        # timer elapses.  Weird.  Anyway, the drawer animations aren't awful anyway, so just leave 'em.
        #('Slot Machine Components', global_scale, [
        #    '/Game/InteractiveObjects/GameSystemMachines/SlotMachine/Animation/AS_SlotMachine_Drawer_Close',
        #    '/Game/InteractiveObjects/GameSystemMachines/SlotMachine/Animation/AS_SlotMachine_Drawer_Open',
        #    '/Game/InteractiveObjects/GameSystemMachines/SlotMachine/Animation/AS_Slotmachine_Locker_Closing',
        #    '/Game/InteractiveObjects/GameSystemMachines/SlotMachine/Animation/AS_Slotmachine_Locker_Opening',
        #    ]),
        ('Character Death Respawns', global_scale, [
            # Turns out this affects the *entire* respawn sequence, including digistruct tunnel.
            # At our current rates, it ends up basically omitting the char-standing-up animation
            # entirely.  (And also the char doesn't end up facing the right way 'cause the camera
            # doesn't go through its motions.  Whatever.)
            AS('/Game/PlayerCharacters/Beastmaster/_Shared/Animation/Generic/FFYL/AS_Respawn_Kneel'),
            AS('/Game/PlayerCharacters/Gunner/_Shared/Animation/Generic/FFYL/AS_Respawn_Kneel'),
            AS('/Game/PlayerCharacters/Operative/_Shared/Animation/Generic/FFYL/AS_Respawn_Kneel'),
            AS('/Game/PlayerCharacters/SirenBrawler/_Shared/Animation/Generic/FFYL/AS_Respawn_Kneel'),
            ]),
        ('PC Animations', 2, [
            AS('/Game/PlayerCharacters/_Shared/Animation/Generic/UI/Echo/1st/AS_Echo_Cart_Pickup',
                # If we scale this up any more than this, the animation gets that freezing issue that
                # we see on the vehicle animations.  Would prefer avoiding that, in this case.
                scale=1.5,
                ),
            ]),
        ('NPC Animations', 2, [
            AS('/Game/NonPlayerCharacters/Ava/Animation/Missions/AS_MayaDeathReaction_Enter', target='CityBoss_P'),
            AS('/Game/NonPlayerCharacters/Ava/Animation/Missions/AS_MayaDeathReaction_Exit', target='CityBoss_P'),
            AS('/Game/Enemies/Saurian/_Shared/Animation/Missions/AS_FastDigging', target='Mansion_P'),
            ]),
        ('Diamond Armory', global_scale, [
            AS('/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/Animation/AS_Close', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/R_SideWall/AS_Wall_Opening', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/R_SideWall/AS_Wall_Locking', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/R_SideWall/AS_Wall_Opened_Idle', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/R_SideWall/AS_Wall_Locked_Idle', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/R_SideWall/AS_Wall_Closed_Idle', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/R_SideWall/AS_Wall_Closing', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/CenterWall/AS_Wall_Opening', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/CenterWall/AS_Wall_Locking', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/CenterWall/AS_Wall_Opened_Idle', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/CenterWall/AS_Wall_Locked_Idle', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/CenterWall/AS_Wall_Closed_Idle', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/CenterWall/AS_Wall_Closing', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/SideWall/AS_Wall_Opening', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/SideWall/AS_Wall_Locking', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/SideWall/AS_Wall_Opened_Idle', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/SideWall/AS_Wall_Locked_Idle', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/SideWall/AS_Wall_Closed_Idle', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondChest/Animations/SideWall/AS_Wall_Closing', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Animations/AS_Close', target='Sanctuary3_P'),
            AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Animations/AS_Open', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Animations/AS_Closed_Idle', target='Sanctuary3_P'),
            #AS('/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Animations/AS_Open_Idle', target='Sanctuary3_P'),
            ]),
        ]:

    mod.comment(cat_name)

    for animseq in animseqs:

        if animseq.scale is None:
            animseq.scale = cat_scale
        if animseq.seqlen_scale is None:
            animseq.seqlen_scale = animseq.scale

        animseq.do_scale(mod, data)

    mod.newline()

# Eridian tools should very arguably just be in the above section with all the other
# AnimSequence tweaks, but I think these pre-dated my fancier handling, and they seem
# to work fine.  I don't really feel like putting them in there and re-testing stuff,
# so I'm just pretending they're part of that main section with a comment rather than
# header, here.
mod.comment('Eridian Tools')
for anim_obj in [
        '/PlayerCharacters/_Shared/Animation/Skills/VaultRewards/1st/AS_Analyzer_Use',
        '/PlayerCharacters/_Shared/Animation/Skills/VaultRewards/1st/AS_Eridian_Melee_Small',
        '/PlayerCharacters/_Shared/Animation/Skills/VaultRewards/1st/Eridian_Analyzer/AS_Analyzer_Use',
        '/PlayerCharacters/Beastmaster/_Shared/Animation/Skills/VaultRewards/3rd/AS_Analyzer_Use',
        '/PlayerCharacters/Beastmaster/_Shared/Animation/Skills/VaultRewards/3rd/AS_Eridian_Melee_Small',
        '/PlayerCharacters/Gunner/_Shared/Animation/Skills/VaultRewards/3rd/AS_Analyzer_Use',
        '/PlayerCharacters/Gunner/_Shared/Animation/Skills/VaultRewards/3rd/AS_Eridian_Melee_Small',
        '/PlayerCharacters/Operative/_Shared/Animation/Skills/VaultRewards/3rd/AS_Analyzer_Use',
        '/PlayerCharacters/Operative/_Shared/Animation/Skills/VaultRewards/3rd/AS_Eridian_Melee_Small',
        '/PlayerCharacters/SirenBrawler/_Shared/Animation/Skills/VaultRewards/3rd/AS_Analyzer_Use',
        '/PlayerCharacters/SirenBrawler/_Shared/Animation/Skills/VaultRewards/3rd/AS_Eridian_Melee_Small',
        ]:

    mod.reg_hotfix(Mod.PATCH, '',
            anim_obj,
            'RateScale',
            global_eridian_scale)

mod.newline()

mod.header('Extra Container Tweaks')

# Maliwan Ammo Crate Digistructs
mod.comment('Maliwan Ammo Crate Digistructs')
# Honestly not sure what exactly this controls, though it's *not* anything to do with the animation trigger
mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
        '/Game/Lootables/_Design/Classes/Maliwan/BPIO_Lootable_Maliwan_AmmoCrate.BPIO_Lootable_Maliwan_AmmoCrate_C:Loot_GEN_VARIABLE',
        'AutoLootDelayOverride',
        0.8/global_scale)
# This is the delay for the "light burst" effect, and maybe when the digistruct animation
mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
        '/Game/GameData/Loot/CoordinatedEffects/BP_CE_Maliwan_Loot_Digistruct_In.Default__BP_CE_Maliwan_Loot_Digistruct_In_C',
        'ParticleEffects.ParticleEffects[0].StartTime',
        0.25/global_scale)
# *this* is what speeds up the actual digistruct animation on the individual items
mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
        '/Game/GameData/Loot/CoordinatedEffects/BP_CE_Maliwan_Loot_Digistruct_In.Default__BP_CE_Maliwan_Loot_Digistruct_In_C',
        'Duration',
        round(2.1/global_scale, 6))
mod.newline()

# Eridian ammo crate light-burst speedup
# This doesn't actually affect anything important, but the animation as-is makes the crate-opening
# *look* slower, so I'm tweaking it anyway.  Note that this doesn't really speed it up as much
# as it should; this ends up resulting in maybe a 2x speedup instead of our 4x intended.  So there's
# still something going on, but whatever, it's better.
mod.comment('Eridian Ammo Crate Light-Burst Speedup')
scale_ps(mod, data, Mod.LEVEL, 'MatchAll',
        '/Game/Lootables/Eridian/Chest_Red/Effects/Systems/PS_Eridian_Ammo_Chest_SinkNBurn',
        global_scale)
mod.newline()

# Industrial Dumpsters
mod.comment('Industrial Dumpster Loot Spawn')
mod.bytecode_hotfix(Mod.LEVEL, 'MatchAll',
        '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_Industrial_Dumpster',
        'ExecuteUbergraph_BPIO_Lootable_Industrial_Dumpster',
        243,
        0.8,
        0.8/global_scale,
        )
mod.newline()

# Xylourgos Portal Chests
# The speedup here is pretty slight; most of the delay is waiting for the various animations
# to finish up, even after being sped up by our other tweaks.
mod.comment('Xylourgos Portal Chest Loot Skrit Spawn Delay')
for index, delay in [
        # Slight delay before making the loot-vs-skrit decision (I think)
        (1938, 0.25),
        # Slight delay before spawning the skrit, if that's the choice that was made (I think)
        (1494, 1),
        ]:
    mod.bytecode_hotfix(Mod.LEVEL, 'MatchAll',
            '/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/Cultists/BPIO_Hib_Lootable_PortalChest',
            'ExecuteUbergraph_BPIO_Hib_Lootable_PortalChest',
            index,
            delay,
            0,
            )
mod.newline()

# TODO:
# So there's various objects in here where we're doing an IO() tweak in this section, but then
# down below we also do some tweaking to a Timeline object, specifically tweaking its Length
# attr, to match up with the freshly-scaled IO() bits.  Well, towards the tail end of this mod
# development, I noticed that those Timeline objects also have a `PlayRate` attr, which
# simplifies this whole process -- namely, you can leave this IO() bit out, leave the Timeline
# `Length` how it is, and *just* alter the `PlayRate`.  I suspect I may not have the energy
# to convert all the prior stuff to do it, so I think this new method is likely to only be
# used for some of DLC2 and then DLC3.  Still, it might be worth converting it at some point.
# (To be fair, *most* of the IOs in here make sense to keep as they are -- it's mostly just the
# mission-related objects in the "Other" section which ended up requiring map-specific tweaks.
# We wouldn't want to have to touch every single map door object to alter PlayRate, etc.  It
# should be mostly just the ones where I've noted that there's extra tweaks "below.")

class IO():
    """
    Convenience class to allow me to loop over a bunch of IO/BPIO objects which largely
    use the defaults but which occasionally need to override 'em.
    """

    def __init__(self, path, label=None,
            hf_type=Mod.LEVEL, level='MatchAll', notify=False,
            scale=None, timelinelength=True,
            timeline_skip_set=None,
            ):
        self.path = path
        self.last_bit = path.split('/')[-1]
        self.last_bit_c = f'{self.last_bit}_C'
        self.full_path = f'{self.path}.{self.last_bit_c}'
        if label is None:
            self.label = self.last_bit
        else:
            self.label = label
        self.hf_type = hf_type
        self.level = level
        self.notify = notify
        self.scale = scale

        # This is just used to suppress warnings we'd otherwise print, for objects
        # we know don't have this attr
        self.timelinelength = timelinelength

        # Any timelines to skip
        if timeline_skip_set is None:
            self.timeline_skip_set = set()
        else:
            self.timeline_skip_set = timeline_skip_set

# It's tempting to try and limit some of these doors to the "obvious" particular level, but a lot
# of them end up getting used elsewhere anyway, like in Trials maps, or DLC6 levels.  We could
# probably programmatically guess at it, using the refs database, but that seems like too much work.
checked_ver = False
for category, cat_scale, io_objs in [
        ('Doors', door_scale, [
            # find $(find . -name Doors) -name "IO_*.uasset" | sort -i | cut -d. -f2 | grep -v Parent
            IO('/Alisma/InteractiveObjects/General/Doors/IO_Door_130x250_SlideLeft_Hyperion'),
            IO('/Alisma/InteractiveObjects/General/Doors/IO_Door_130x250_SlideUp_Prison'),
            IO('/Alisma/InteractiveObjects/General/Doors/IO_Door_400x400_SlideDown_Hyp'),
            IO('/Alisma/InteractiveObjects/General/Doors/IO_DoubleDoor_SlideUp_Hyp'),
            # This one's just part of a cutscene; stays open otherwise
            #IO('/Dandelion/InteractiveObjects/Doors/IO_Door_800x600_SlideUp_TrashTownMainEntry'),
            IO('/Dandelion/InteractiveObjects/Doors/IO_Door_Hyperion_DoubleGlass'),
            IO('/Dandelion/InteractiveObjects/Doors/IO_Door_Hyperion_Double'),
            IO('/Dandelion/InteractiveObjects/Doors/IO_Door_Hyperion_Single_TricksyNickLoot'),
            IO('/Dandelion/InteractiveObjects/Doors/IO_Door_Hyperion_Single'),
            # No timing parameters on these two
            #IO('/Dandelion/InteractiveObjects/Doors/PrizeDoors/IO_Door_Hyperion_Single_Prize'),
            #IO('/Dandelion/InteractiveObjects/Doors/PrizeDoors/IO_Switch_Hyp_Button_V1_Prize'),
            IO('/Dandelion/Missions/Plot/Ep01_MeetTimothy/IO_Door_TimothyHideout'),
            IO('/Game/InteractiveObjects/Doors/Atlas/_Design/IO_Door_130x250_Atlas_ShelfDoor'),
            IO('/Game/InteractiveObjects/Doors/Atlas/_Design/IO_Door_400x400_SlideLeftAndRight_AtlasHQ_Generic'),
            IO('/Game/InteractiveObjects/Doors/Atlas/_Design/IO_Door_AtlasHQ_Elevator_Exterior'),
            IO('/Game/InteractiveObjects/Doors/Atlas/_Design/IO_Door_AtlasHQ_Elevator_Interior_Short'),
            IO('/Game/InteractiveObjects/Doors/Atlas/_Design/IO_Door_AtlasHQ_Elevator_Interior_Tall'),
            # No timing parameters
            #IO('/Game/InteractiveObjects/Doors/City/_Design/IO_Door_1630x600_MeltHole_GiantDoor'),
            IO('/Game/InteractiveObjects/Doors/City/_Design/IO_Door_1630x600_SlideUp_GiantDoor'),
            IO('/Game/InteractiveObjects/Doors/CoV/_Design/IO_Door_CoV_SwingingGate_V1'),
            IO('/Game/InteractiveObjects/Doors/Default/1000x600/IO_Door_1000x600_SlideLeftAndRight'),
            IO('/Game/InteractiveObjects/Doors/Default/800x600/IO_Door_800x600_SlideUp'),
            IO('/Game/InteractiveObjects/Doors/Eden_6/_Design/IO_Door_130x250_Rotate_Watership'),
            IO('/Game/InteractiveObjects/Doors/Eden_6/_Design/IO_Door_400x400_SlideLeftAndRight_Eden6_Generic_IronBear'),
            IO('/Game/InteractiveObjects/Doors/Eden_6/_Design/IO_Door_Custom_Watership_RotateUp'),
            IO('/Game/InteractiveObjects/Doors/Eden_6/_Design/IO_Door_Marshfields_Custom_HiddenSpyDoor'),
            IO('/Game/InteractiveObjects/Doors/Eden_6/_Design/IO_Door_Watership_Custom_LabDoor',
                timelinelength=False,
                ),
            IO('/Game/InteractiveObjects/Doors/Eridian/_Design/IO_Door_1000x600_SlideLeftAndRight_Eridian_Generic'),
            IO('/Game/InteractiveObjects/Doors/Eridian/_Design/IO_Door_400x400_SlideUp_Eridian_Generic'),
            IO('/Game/InteractiveObjects/Doors/Eridian/_Design/IO_Door_Large_SlideUp_Eridian_Generic1'),
            IO('/Game/InteractiveObjects/Doors/Global/_Design/IO_Door_ScalableForcefield'),
            IO('/Game/InteractiveObjects/Doors/Industrial/_Design/IO_Door_1000x600_SlideUp_Industrial_Generic'),
            IO('/Game/InteractiveObjects/Doors/Industrial/_Design/IO_Door_400x400_SlideUp_Industrial_Generic'),
            IO('/Game/InteractiveObjects/Doors/Maliwan/_Design/IO_Door_Custom_Rotate_2Piece_Maliwan'),
            # No timing parameters for these two
            #IO('/Game/InteractiveObjects/Doors/Maliwan/_Design/IO_Door_Maliwan_Shield_Large'),
            #IO('/Game/InteractiveObjects/Doors/Maliwan/_Design/IO_Door_Maliwan_Shield'),
            IO('/Game/InteractiveObjects/Doors/Mansion/_Design/IO_Door_130x250_Rotate_Mansion_NoFrame'),
            IO('/Game/InteractiveObjects/Doors/Mansion/_Design/IO_Door_130x250_Rotate_Mansion'),
            IO('/Game/InteractiveObjects/Doors/Mansion/_Design/IO_Door_400x400_2Piece_Atrium_IronBearDoor'),
            IO('/Game/InteractiveObjects/Doors/Mansion/_Design/IO_Door_400x400_Rotate_2Piece_BustOpenMansionDoor'),
            IO('/Game/InteractiveObjects/Doors/Mansion/_Design/IO_Door_400x400_Rotate_2Piece_Generic_IronBearDoor'),
            IO('/Game/InteractiveObjects/Doors/Mansion/_Design/IO_Door_CustomSize_Rotate_2Piece_IronGate'),
            IO('/Game/InteractiveObjects/Doors/Mansion/_Design/IO_Door_Mansion_Bookcase_500x500_SlideRight'),
            # No timing parameters
            #IO('/Game/InteractiveObjects/Doors/Mine/_Design/IO_Door_400x400_SlideUp_MinerDetails_DestroyableDoor'),
            IO('/Game/InteractiveObjects/Doors/Monastery/_Design/IO_Door_130x250_SlideDown_Monastery'),
            IO('/Game/InteractiveObjects/Doors/Monastery/_Design/IO_Door_400x400_LeftAndRight_Monastery_1'),
            IO('/Game/InteractiveObjects/Doors/Monastery/_Design/IO_Door_400x400_LeftAndRight_Monastery_SpecialTitleCard'),
            # No timing parameters
            #IO('/Game/InteractiveObjects/Doors/Monastery/_Design/IO_Door_400x400_SlideUp_Monastery_TombDoor'),
            IO('/Game/InteractiveObjects/Doors/Monastery/_Design/IO_Door_800x600_SlideUp_Monastery_Courtyard'),
            IO('/Game/InteractiveObjects/Doors/Motorcade/_Design/IO_Door_130x250_Rotate_Motorcade_OrphanageDoor'),
            IO('/Game/InteractiveObjects/Doors/Motorcade/_Design/IO_Door_130x250_SlideUp_Motorcade_BanditHideoutDoor'),
            IO('/Game/InteractiveObjects/Doors/Motorcade/_Design/IO_Door_400x400_Motorcade_RotateUp'),
            IO('/Game/InteractiveObjects/Doors/Motorcade/_Design/IO_Door_800x600_Motorcade_Rotate'),
            IO('/Game/InteractiveObjects/Doors/Motorcade/_Design/IO_Door_800x600_SlideLeftAndRight_Motorcade_BarnDoor'),
            IO('/Game/InteractiveObjects/Doors/Motorcade/_Design/IO_Door_SkagFarm_400x400_RotateUp'),
            # Leave this one alone, doesn't ever impede movement.
            #IO('/Game/InteractiveObjects/Doors/Nekro/_Design/IO_Door_Custom_CloakedRock'),
            # No timing parameters for these two
            #IO('/Game/InteractiveObjects/Doors/Nekro/_Design/IO_Door_Custom_Nekro_Crypt_Small'),
            #IO('/Game/InteractiveObjects/Doors/Nekro/_Design/IO_Door_Custom_Nekro_Crypt'),
            IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_1000x600_SlideLeftAndRight_Pandora'),
            IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_1000x600_SlideUp_Pandora_Generic'),
            IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_130x250_Lynchwood_SlideLeft1'),
            IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_1630x1200_SlideUp_SecretGarageDoor'),
            IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_400x400_SlideUp_Pandora_Generic'),
            # No timing parameters
            #IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_CustomSize_Rotate_2Piece_CovRecruitmentDoor_Small'),
            IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_CustomSize_Rotate_2Piece_CovRecruitmentDoor'),
            # Only main TimelineLength found; skip it for now...
            #IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_CustomSize_Rotate_2Piece_MagnetDoor'),
            IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_CustomSize_RotateUp_Pandora_TunnelCap'),
            IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_CustomSize_SlideUp_Pandora_CarHook'),
            IO('/Game/InteractiveObjects/Doors/Pandora/_Design/IO_Door_Pandora_130x250_Rotate'),
            IO('/Game/InteractiveObjects/Doors/Prison/_Design/IO_Door_130x250_SlideUp_PrisonBars'),
            IO('/Game/InteractiveObjects/Doors/Prison/_Design/IO_Door_130x250_SlideUp_PrisonMetal'),
            IO('/Game/InteractiveObjects/Doors/Prison/_Design/IO_Door_400x400_SlideUpAndDown_Prison'),
            IO('/Game/InteractiveObjects/Doors/Prison/_Design/IO_Door_400x400_SlideUp_Prison'),
            IO('/Game/InteractiveObjects/Doors/Promethea/_Design/IO_Door_1000x600_SlideUp_Promethea_Generic'),
            # No timing parameters -- calls out to Door_Eden6_VehicleSpawner's AS_VehicleDoor_Open and handled above, though.
            #IO('/Game/InteractiveObjects/Doors/Promethea/_Design/IO_Door_1000x600_SlideUp_Promethea_Vehicle2'),
            IO('/Game/InteractiveObjects/Doors/Promethea/_Design/IO_Door_400x400_SlideUp_Promethea_Generic'),
            IO('/Game/InteractiveObjects/Doors/SpaceShips/_Design/IO_Door_130x250__SlideUp_Spaceships_Generic'),
            IO('/Game/InteractiveObjects/Doors/SpaceShips/_Design/IO_Door_400x400_SlideDown_Spaceships_Generic'),
            IO('/Game/InteractiveObjects/Doors/SpaceShips/_Design/IO_Door_400x400_SlideRight_Spaceships_Generi'),
            IO('/Game/InteractiveObjects/Doors/SpaceShips/_Design/IO_Door_400x400_SlideUp_Spaceships_Generic'),
            IO('/Game/PatchDLC/BloodyHarvest/InteractiveObjects/Doors/_Design/IO_Door_BloodyHarvest_Rotate_2Piece_IronGate'),
            # No timing parameters for these two
            #IO('/Game/PatchDLC/Event2/InteractiveObjects/Doors/_Design/IO_Door_400x400_Rotate_2Piece_Generic_IronBearDoor_Cartels'),
            #IO('/Game/PatchDLC/Event2/InteractiveObjects/Doors/_Design/IO_Door_CustomSize_Rotate_2Piece_IronGate_CartelsVar'),
            IO('/Game/PatchDLC/Ixora/InteractiveObjects/Doors/IO_Door_130x250_SlideUp_Motorcade_BanditHideoutDoor_GearUp'),
            IO('/Game/PatchDLC/Raid1/InteractiveObjects/Raid_MaliwanDoor/IO_Door_Raid02_Custom_SlideUp',
                    level='Raid_P',
                    ),
            # No timing parameters
            #IO('/Game/PatchDLC/Ixora/InteractiveObjects/Doors/IO_Door_400x400_SlideUp_Industrial_Generic_GearUp'),
            IO('/Geranium/InteractiveObjects/Doors/Facility/_Design/IO_Door_130x250_SlideUp_FacilityPlayerDoor1'),
            IO('/Geranium/InteractiveObjects/Doors/Facility/_Design/IO_Door_400x400_SlideLeftAndRight_FacilityIBDoor2'),
            IO('/Geranium/InteractiveObjects/Doors/Facility/_Design/IO_Door_400x400_SlideUp_FacilityIBDoor1'),
            IO('/Geranium/InteractiveObjects/Doors/Facility/_Design/IO_Door_800x600_SlideUpAndDown_FacilitySmallVehicleDoor2'),
            IO('/Geranium/InteractiveObjects/Doors/Facility/_Design/IO_Door_800x600_SlideUp_FacilitySmallVehicleDoor'),
            IO('/Geranium/InteractiveObjects/Doors/Facility/_Design/IO_Door_800x800_Rotate_IBArenaDoor'),
            # No timing parameters
            #IO('/Geranium/InteractiveObjects/Doors/Forest/_Design/IO_Door_Forest_TrainCrash'),
            IO('/Geranium/InteractiveObjects/Doors/Frontier/_Design/IO_Door_130x250_SlideUp_FrontierPlayerDoor'),
            IO('/Geranium/InteractiveObjects/Doors/Frontier/_Design/IO_Door_400x400_SlideLeftAndRight_FrontierIBDoor'),
            IO('/Geranium/InteractiveObjects/Doors/Frontier/_Design/IO_Door_400x400_VaultDoor'),
            IO('/Geranium/InteractiveObjects/Doors/IO_Door_130x250_SaloonDoor'),
            IO('/Geranium/InteractiveObjects/Doors/Lodge/_Design/IO_Door_400x400_Rotate_2Piece_Lodge_IronBear'),
            IO('/Geranium/InteractiveObjects/Doors/Lodge/_Design/IO_Door_Lodge_TreasureRoom'),
            # See also some tweaks, below
            IO('/Hibiscus/InteractiveObjects/MissionSpecific/Side/WhereIBelong/IO_MissionScripted_CageDoor'),
            IO('/Hibiscus/InteractiveObjects/Systems/Doors/_Design/Factory/IO_Hib_Door_800x600_Factory'),
            # No timing parameters for these two
            #IO('/Hibiscus/InteractiveObjects/Systems/Doors/_Design/MansionReskin/IO_Hib_Door2_400x400'),
            #IO('/Hibiscus/InteractiveObjects/Systems/Doors/_Design/MansionReskin/IO_Hib_Door_400x400'),
            # This one can't be serialized currently, for some reason.
            #IO('/Hibiscus/InteractiveObjects/Systems/Doors/_Design/MansionReskin/IO_Hib_Door_Bookcase'),
            # No timing parameters
            #IO('/Hibiscus/InteractiveObjects/Systems/Doors/_Design/MansionReskin/IO_Hib_DoorFrame_130x250'),
            IO('/Hibiscus/InteractiveObjects/Systems/Doors/_Design/Venue/IO_Hib_Door_Venue_BossGate',
                timelinelength=False,
                ),
            # No timing parameters
            #IO('/Hibiscus/InteractiveObjects/Systems/Doors/_Design/Village/IO_Hib_Door_130x250_Village'),
            IO('/Hibiscus/InteractiveObjects/Systems/Doors/_Design/Village/IO_Hib_Door_IronGate'),
            IO('/Hibiscus/InteractiveObjects/Systems/Doors/_Design/Woods/IO_Hib_Door_400x400_SlideDoor'),
            IO('/Hibiscus/InteractiveObjects/Systems/Doors/_Design/Woods/IO_Hib_Door_800x600_SlideDoor'),
            IO('/Ixora2/InteractiveObjects/Doors/IO_Door_400x400_SlideUp_Eridian_Generic'),
            # No timing parameters
            #IO('/Ixora2/InteractiveObjects/Doors/IO_Door_Custom_Eridian'),
            IO('/Ixora2/InteractiveObjects/Doors/IO_Door_SlideLeftAndRight_AlleyGate'),
            IO('/Ixora2/InteractiveObjects/MissionSpecific/04_Nekro/IO_Door_IXO_TombEntrance_SlideUp'),
            ]),
        ('Switches', global_scale, [
            # find $(find . -name Switches) -name "IO_*.uasset" | sort -i | cut -d. -f2
            IO('/Game/InteractiveObjects/Switches/Circuit_Breaker/_Design/IO_Switch_Circuit_Breaker_V1'),
            # No timing parameters
            #IO('/Game/InteractiveObjects/Switches/ControlPanel_Crane/_Design/IO_Switch_ControlPanel_Crane'),
            IO('/Game/InteractiveObjects/Switches/CoV/IO_Switch_CoV_SkullSwitch_V1'),
            IO('/Game/InteractiveObjects/Switches/CoV/Kitbash/_Design/IO_Switch_CoV_Kitbash_V1'),
            # No timing parameters
            #IO('/Game/InteractiveObjects/Switches/CoV/Target/IO_SwitchDamagable_CoV_TargetCeiling_V1'),
            IO('/Game/InteractiveObjects/Switches/CoV/Target/IO_SwitchDamagable_CoV_Target_V2'),
            IO('/Game/InteractiveObjects/Switches/Detonator/_Design/IO_Switch_Detonator_V1'),
            IO('/Game/InteractiveObjects/Switches/Eridian/_Design/IO_Switch_EridianSwitch_V1'),
            IO('/Game/InteractiveObjects/Switches/Industrial/Button/_Design/IO_Switch_GenericButton_V1'),
            # No timing parameters
            #IO('/Game/InteractiveObjects/Switches/Industrial/Keyboard/_Design/IO_Switch_Industrial_Keyboard_V1'),
            IO('/Game/InteractiveObjects/Switches/Lever/Design/IO_Switch_Industrial_FloorLever_V1'),
            IO('/Game/InteractiveObjects/Switches/Lever/Design/IO_Switch_Industrial_Prison'),
            IO('/Game/InteractiveObjects/Switches/Promethea/_Design/IO_Switch_Promethea_Generic_V1'),
            # No timing parameters
            #IO('/Game/InteractiveObjects/Switches/_Shared/_Design/IO_ChangeOfHeart_DoorbellButton'),
            IO('/Game/InteractiveObjects/Switches/Switch/Design/IO_Switch_IndustrialSwitch_V1'),
            IO('/Game/InteractiveObjects/Switches/WheelValve/Design/IO_Switch_Industrial_WheelValve_V1'),
            IO('/Game/PatchDLC/BloodyHarvest/InteractiveObjects/Switches/_Design/IO_Switch_SkullSwitch',
                level='BloodyHarvest_P',
                ),
            IO('/Game/InteractiveObjects/MissionUsable/_Design/MansionInvestigationObjects/IO_Switch_StatueButton',
                label="Hidden Statue Button in Jakobs Estate",
                level='Mansion_P',
                ),
            IO('/Game/PatchDLC/Event2/InteractiveObjects/CartelElevatorDoor/IO_Door_400x400_CartelElevatorDoor',
                label="Elevator doors in Villa Ultraviolet",
                level='Cartels_P',
                ),
            ]),
        ('More Containers', global_scale, [
            # This basically just speeds up the turn-to-green which allows it to be opened
            IO('/Game/Lootables/_Design/Classes/Eridian/BPIO_Lootable_Eridian_WhiteChestCrystal'),
            ]),
        ('Other Objects', global_scale, [
            # Both these slot machine objects need some other tweaks as well, done below.
            IO('/Game/InteractiveObjects/SlotMachine/_Shared/_Design/BPIO_SlotMachine',
                label='Base-Game Slot Machines',
                ),
            IO('/Dandelion/InteractiveObjects/PlayableSlotMachines/BPIO_SlotMachine_Dandelion_V1',
                label='DLC1 Slot Machines',
                ),
            # See also some tweaks below, re: Diamond Armory
            IO('/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/_Design/Chest/BPIO_DiamondChest',
                label='Diamond Armory Console',
                level='Sanctuary3_P',
                timeline_skip_set={
                    # This timeline controls the visible countdown (though not the *real* countdown).
                    # Letting it scale would end up with what looks like a very fast countdown.
                    'TimerTimeline_Template',
                    },
                ),
            IO('/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/_Design/Walls/BPIO_DiamondChestWall',
                label='Diamond Armory Walls',
                level='Sanctuary3_P',
                ),
            IO('/Game/InteractiveObjects/MissionScripted/_Design/IO_MissionScripted_StatueManufacturingMachine',
                label='Golden Calves Statue Scanner/Printer',
                level='Sacrifice_P',
                ),
            IO('/Game/InteractiveObjects/MissionUsable/_Design/IO_MissionUsable_SlidingDesk_Lamp',
                label="Rhys's Sliding Desk (Lamp)",
                level='AtlasHQ_P',
                ),
            IO('/Game/InteractiveObjects/MissionScripted/_Design/IO_MissionScripted_SlidingDesk',
                label="Rhys's Sliding Desk (Desk)",
                level='AtlasHQ_P',
                ),
            IO('/Game/InteractiveObjects/MissionUsable/_Design/MansionInvestigationObjects/IO_MissionUsable_ExplodingStatue',
                label="Exploding Busts in Jakobs Estate",
                level='Mansion_P',
                ),
            IO('/Game/InteractiveObjects/MissionUsable/_Design/MansionInvestigationObjects/IO_MissionUsable_SlidingPictureFrame',
                label="Sliding Pictures in Jakobs Estate",
                level='Mansion_P',
                ),
            IO('/Game/InteractiveObjects/MissionUsable/_Design/MansionInvestigationObjects/IO_MissionUsable_SpinningBookShelf',
                label="Rotating Bookshelves in Jakobs Estate",
                level='Mansion_P',
                ),
            IO('/Game/InteractiveObjects/MissionSpecificObjects/GrandTour/_Design/BP_IO_StageProp_UpDown',
                label="Stage Props in Jakobs Estate",
                level='Mansion_P',
                ),
            IO('/Game/InteractiveObjects/MissionUsable/_Design/IO_MissionUsable_AureliasSkeletons_MovableBed',
                label="Sliding Bed in 'Sacked' mission",
                level='Mansion_P',
                ),
            # To fully speed this up, we'd also need to adjust PS_Static_Scanned_Digistruct_Sweep timing,
            # which is used somewhere in Dandelion as well.  Maybe we'll want to do that eventually
            # anyway, in which case make sure to go back and test this.  Also might as well figure out
            # what the City_P use is, as well -- I'm guessing bringing the Ratch meat back to the Burger
            # joint?  At any rate, in MarshFields_P, the animation doesn't actually block you from
            # doing the Next Thing anyway, so eh.  See down below for another tweak I'd started on
            # before realizing it was silly.
            #IO('/Game/InteractiveObjects/MissionPlaceables/_Design/IO_MissionPlaceable_Static_Scanned',
            #    label="Rogues ID Scanner in Ambermire",
            #    # Looks like this actually shows up in City_P, in the Dynasty Diner quest.  I didn't
            #    # notice it then, so at least for now I'm only doing this in MarshField_P.
            #    level='MarshFields_P',
            #    ),
            IO('/Game/Missions/Plot/EP17_BigChase/BP_Ep17_CarGrinder',
                label='Splinterlands Car Grinder',
                level='Motorcade_P',
                ),
            IO('/Game/Missions/Side/Zone_3/Mine/GrowingPains/IO_MissionUsable_GrowingPains_PictureFrame',
                label="Handsome Jack Portrait in Konrad's Hold",
                level='Mine_P',
                ),
            # Also has some tweaks down below
            IO('/Game/InteractiveObjects/MissionScripted/_Design/IO_MissionScripted_EridianStatue',
                label="Eridian statues in Pyre of Stars",
                level='Crypt_P',
                ),
            # Also has some tweaks down below
            IO('/Game/InteractiveObjects/MissionScripted/_Design/IO_MissionScripted_EridianRaisingPlatform',
                label="Rising platforms in Pyre of Stars",
                level='Crypt_P',
                ),
            # Also has some tweaks down below
            IO('/Game/PatchDLC/Event2/InteractiveObjects/BookPuzzle/IO_Usable_KeypadBook',
                label="Book puzzle inputs in Villa Ultraviolet",
                level='Cartels_P',
                ),
            IO('/Game/PatchDLC/Event2/InteractiveObjects/BookPuzzle/IO_Door_SpinningBookShelf',
                label="Spinning bookshelf in Villa Ultraviolet",
                level='Cartels_P',
                ),
            # Also has some tweaks down below
            IO('/Game/PatchDLC/Event2/InteractiveObjects/CartelFountain/IO_MissionScripted_CartelFountain',
                label="Villa Ultraviolet descending fountain",
                level='Cartels_P',
                ),
            # Also has some AS() tweaks
            IO('/Dandelion/Lootables/_Design/Classes/Hyperion/BPIO_Lootable_BlackJackChest',
                label="Handsome Jackpot Blackjack Tables",
                ),
            # See also some tweaks below
            IO('/Hibiscus/InteractiveObjects/MissionSpecific/Side/WhereIBelong/IO_MissionScripted_CranePartDoor',
                label="Panel containing power coil in Call of the Deep",
                level='Lake_P',
                ),
            # See also some tweaks below
            IO('/Hibiscus/InteractiveObjects/MissionSpecific/Side/WhereIBelong/Placeables/IO_MissionPlaceable_BloodJar',
                label="Gythian blood jar in Call of the Deep",
                level='Lake_P',
                timelinelength=False,
                ),
            # See also some tweaks, below
            IO('/Hibiscus/InteractiveObjects/MissionSpecific/Side/PrivateEye/Painting/IO_Scripted_Private1_SecretWall',
                label="Secret wall in crypt, for Cold Case: Buried Questions",
                level='Village_P',
                ),
            IO('/Geranium/Maps/CraterBoss/Elevators/Elevator_CraterBoss_Gondola',
                label="Crater's Edge Gondola",
                level='CraterBoss_P',
                ),
            # See also some delay tweaks below
            IO('/Alisma/InteractiveObjects/MissionSpecific/Plot/ALI_EP02/Catapult/IO_MissionScripted_Ali_CatapultPivot',
                label="Castle Crimson catapult rotation",
                level='Anger_P',
                # This actually looks a little *too* fast with our default global_scale
                scale=2,
                ),
            # See also some delay tweaks below
            IO('/Alisma/InteractiveObjects/MissionSpecific/Side/InkBlots/IO_MissionScripted_BlotsPipes',
                label="Don't Call It A Rorschach Ink-Blot Pipes",
                level='Experiment_P',
                ),
            ]),
        ]:

    mod.header(f'InteractiveObject Speedups: {category}')

    for io_obj in io_objs:

        if verbose:
            print('Processing {}'.format(io_obj.path))

        if io_obj.scale is None:
            io_obj.scale = cat_scale

        mod.comment(io_obj.label)
        obj = data.get_data(io_obj.path)
        if not obj:
            print('WARNING - Could not be serialized: {}'.format(io_obj.path))
            continue

        if not checked_ver:
            if '_apoc_data_ver' not in obj[0] or obj[0]['_apoc_data_ver'] < min_apoc_jwp_version:
                raise RuntimeError('In order to generate a valid mod, you MUST use Apocalyptech\'s JWP fork which serializes to version {}'.format(min_apoc_jwp_version))
            checked_ver = True

        found_primary = False
        did_main = False
        did_curve = False
        for export in obj:
            if export['_jwp_object_name'] == io_obj.last_bit_c:
                found_primary = True
                if 'Timelines' in export:
                    for timeline_idx, timeline_ref in enumerate(export['Timelines']):
                        timeline_exp = timeline_ref['export']
                        timeline_name = timeline_ref['_jwp_export_dst_name']
                        if timeline_name in io_obj.timeline_skip_set:
                            if verbose:
                                print(f' - Skipping timeline {timeline_idx} ({timeline_name}, export {timeline_exp})')
                            continue
                        if verbose:
                            print(f' - Processing timeline {timeline_idx} ({timeline_name}, export {timeline_exp})')
                        if timeline_exp != 0:
                            timeline = obj[timeline_exp-1]

                            # This one's not actually required (and doesn't seem to do anything), but I feel weird *not* specifying it.
                            # NOTE: I *think* that when this attr doesn't show up, it's probably because
                            # there's a LengthMode=TL_TimelineLength in play, which you'll see in the
                            # map object itself, and the length ends up getting sort of computed?
                            # Anyway, in those instances I believe the TimelineLength *does* show up
                            # in this object if you query it, but the one you need to alter is the
                            # one from the map object.  So you'll want to `getall` on that TimelineComponent
                            # to ensure what it is and then do a tweak down below.  Fun!  You can see this
                            # on the IO_MissionPlaceable_BloodJar in Lake_P.
                            if 'TimelineLength' in timeline and timeline['TimelineLength'] != 0:
                                did_main = True
                                mod.reg_hotfix(io_obj.hf_type, io_obj.level,
                                        io_obj.full_path,
                                        f'Timelines.Timelines[{timeline_idx}].Object..TimelineLength',
                                        round(timeline['TimelineLength']/io_obj.scale, 6),
                                        notify=io_obj.notify,
                                        )

                            # Now process all our various curves
                            for trackname, curve_var in [
                                    ('EventTracks', 'CurveKeys'),
                                    ('FloatTracks', 'CurveFloat'),
                                    # I think VectorTracks is generally not needed; more used for
                                    # rotation+position info, perhaps?
                                    ('VectorTracks', 'CurveVector'),
                                    ]:
                                if trackname in timeline:
                                    if verbose:
                                        print('   - Processing {}'.format(trackname))
                                    for track_idx, track_ref in enumerate(timeline[trackname]):
                                        track_exp = track_ref[curve_var]['export']
                                        if verbose:
                                            print('     - On curve {} (export {})'.format(track_idx, track_exp))
                                        if track_exp != 0:
                                            curve = obj[track_exp-1]
                                            for inner_curve_var in ['FloatCurve', 'FloatCurves']:
                                                if inner_curve_var in curve:
                                                    for key_idx, key in enumerate(curve[inner_curve_var]['Keys']):
                                                        if key['time'] != 0:
                                                            did_curve = True
                                                            mod.reg_hotfix(io_obj.hf_type, io_obj.level,
                                                                    io_obj.full_path,
                                                                    f'Timelines.Timelines[{timeline_idx}].Object..{trackname}.{trackname}[{track_idx}].{curve_var}.Object..{inner_curve_var}.Keys.Keys[{key_idx}].Time',
                                                                    round(key['time']/io_obj.scale, 6),
                                                                    notify=io_obj.notify,
                                                                    )


        if not found_primary:
            raise RuntimeError('Could not find main export for {}'.format(io_obj.path))

        if not did_main and not did_curve:
            print('NOTICE - No timing parameters found for {}'.format(io_obj.path))
            mod.comment('(no timing parameters found to alter)')
        elif not did_main:
            # This honestly hardly matters; it doesn't look like this attr's really used
            # for much, anyway.
            if io_obj.timelinelength:
                print('NOTICE - No main TimelineLength found for {}'.format(io_obj.path))
        elif not did_curve:
            print('NOTICE - No curve timings found for {}'.format(io_obj.path))

        mod.newline()

# `getall Elevator`
mod.header('Elevators')
for label, level, obj_name, speed, travel_time in sorted([
        ('The Droughts - Taking Flight (Sanctuary III Drydock)', 'Prologue_P',
            '/Game/Maps/Zone_0/Prologue/Prologue_M_Ep04_EarnSpaceship.Prologue_M_Ep04_EarnSpaceship:PersistentLevel.Elevator_Ep04_Prologue',
            175, 10),
        ('Meridian Outskirts - Under Rax/Max Platform', 'Outskirts_P',
            '/Game/Maps/Zone_1/Outskirts/Outskirts_LowerSector.Outskirts_LowerSector:PersistentLevel.Elevator_UnderBridge_2',
            120, 10),
        ('Meridian Outskirts - Main upper/lower Elevator', 'Outskirts_P',
            '/Game/Maps/Zone_1/Outskirts/Outskirts_Mission.Outskirts_Mission:PersistentLevel.Elevator_Outskirts_Refugee',
            400, 10),
        ('Skywell-27 - Main Elevator', 'OrbitalPlatform_P',
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_Combat.OrbitalPlatform_Combat:PersistentLevel.Elevator_Cargo_OrbitalPlatform_2',
            2000, 10),
        # This one still feels a bit slow to me; I think it might not fully use these values?
        # But whatever, it's not slow enough for me to care enough to look into more.
        ('Skywell-27 - Boss Elevator', 'OrbitalPlatform_P',
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_Boss.OrbitalPlatform_Boss:PersistentLevel.Elevator_Cargo_OrbitalPlatform_2',
            200, 10),
        ('Atlas HQ - Main Office Elevator (initial trip up)', 'AtlasHQ_P',
            '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_M_EP06OfficeSpaceInvaders.AtlasHQ_M_EP06OfficeSpaceInvaders:PersistentLevel.Elevator_Ep06_AtlasHQ_V_2',
            250, 47),
        ('Atlas HQ - Smaller Elevator', 'AtlasHQ_P',
            '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_M_EP06OfficeSpaceInvaders.AtlasHQ_M_EP06OfficeSpaceInvaders:PersistentLevel.Elevator_Ep06_AtlasHQ_V_0',
            #250/2, 5*2),
            250, 5),
        ('Cistern of Slaughter', 'CreatureSlaughter_P',
            '/Game/Maps/Slaughters/CreatureSlaughter/CreatureSlaughter_P.CreatureSlaughter_P:PersistentLevel.Elevator_CreatureSlaughter',
            400, 10),
        ('Floodmoor Basin - Knotty Peak', 'Wetlands_P',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_Dynamic.Wetlands_Dynamic:PersistentLevel.Elevator_WetlandsLodge_3326',
            400, 10),
        # There's a lot of components in this one, and it's already pretty speedy, so I'm leaving it alone out of laziness.  Amusingly,
        # leaving it alone makes this one of the *slower* elevators in the game.
        #('Floodmoor Basin - Rocket Elevator', 'Wetlands_P',
        #    '/Game/Maps/Zone_2/Wetlands/Wetlands_M_DudeBro.Wetlands_M_DudeBro:PersistentLevel.Elevator_Rocket',
        #    900, 7),
        ('The Anvil - Sauce Room', 'Prison_P',
            '/Game/Maps/Zone_2/Prison/Prison_M_EP08PrisonBreak.Prison_M_EP08PrisonBreak:PersistentLevel.Elevator_PrisonArmory_1624',
            350, 10),
        ('Jakobs Estate', 'Mansion_P',
            '/Game/Maps/Zone_2/Mansion/Mansion_M_EP09GrandTour.Mansion_M_EP09GrandTour:PersistentLevel.Elevator_Ep09_Mansion_592',
            175, 20),
        ('Ambermire', 'MarshFields_P',
            '/Game/Maps/Zone_2/MarshFields/MarshFields_M_Ep12Marshfields.MarshFields_M_Ep12Marshfields:PersistentLevel.Elevator_Marshfields_WaterWheelStandin_4',
            500, 10),
        ("Carnivora - La Cage O' Tinks Entrance", 'MotorcadeFestival_P',
            '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_M_Plot.MotorcadeFestival_M_Plot:PersistentLevel.BP_Ep15_BigChase_FestivalElevator',
            120, 10),
        ("Carnivora - La Cage O' Tinks Exit", 'MotorcadeFestival_P',
            '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_M_Plot.MotorcadeFestival_M_Plot:PersistentLevel.BP_Ep15_BigChase_FestivalElevator_0',
            120, 10),
        ("Guts of Carnivora", 'MotorcadeInterior_P',
            '/Game/Maps/Zone_3/MotorcadeInterior/MotorcadeInterior_Plot.MotorcadeInterior_Plot:PersistentLevel.BP_CarnivorArena_Elevator_578',
            200, 10),
        ("Konrad's Hold", 'Mine_P',
            '/Game/Maps/Zone_3/Mine/Mine_Section2_Lobby.Mine_Section2_Lobby:PersistentLevel.Elevator_Ep14_Mine_NoName_3',
            5, 10),
        ("Slaughterstar 3000", 'TechSlaughter_P',
            '/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Geo.TechSlaughter_Geo:PersistentLevel.Elevator_TechSlaughter_2',
            500, 10),
        ("Tazendeer Ruins", 'Beach_P',
            '/Game/Maps/Zone_4/Beach/Beach_TempleFirstFloor.Beach_TempleFirstFloor:PersistentLevel.BP_EP18_Eridian_Elevator_0',
            2000, 10),
        ("Stormblind Complex", 'FrostSite_P',
            '/Ixora/Maps/FrostSite/FrostSite_Combat.FrostSite_Combat:PersistentLevel.Elevator_FrostSite_2',
            200, 10),
        ("Midnight's Cairn (Maliwan Takedown)", 'Raid_P',
            '/Game/PatchDLC/Raid1/Maps/Raid/Raid_M_RaidOnMaliwan.Raid_M_RaidOnMaliwan:PersistentLevel.Elevator_Raid__3',
            900, 10),
        ("Villa Ultraviolet", 'Cartels_P',
            '/Game/PatchDLC/Event2/Maps/Cartels_Combat.Cartels_Combat:PersistentLevel.Elevator_Cartels_5',
            95, 10),
        ("Grand Opening", 'CasinoIntro_P',
            '/Dandelion/Maps/CasinoIntro/CasinoIntro_GoldenBullion.CasinoIntro_GoldenBullion:PersistentLevel.Elevator_CasinoIntro_2',
            150, 10),
        ("Spendopticon", 'Strip_P',
            '/Dandelion/Maps/Strip/Strip_SM_RagingBot.Strip_SM_RagingBot:PersistentLevel.Elevator_RagingBot_Strip_2',
            350, 10),
        ("Jack's Secret", 'Core_P',
            '/Dandelion/Maps/Core/Core_Mission.Core_Mission:PersistentLevel.Elevator_Core_JackpotToCore_2',
            700, 20),
        ("VIP Tower", 'TowerLair_P',
            '/Dandelion/Maps/TowerLair/TowerLair_PM_TheHeist.TowerLair_PM_TheHeist:PersistentLevel.IO_Elevator_Heist_Tower_2',
            # Doing some extra scaling on this 'cause it's slooow.
            200*2, 40/2),
        ("Negul Neshai", 'Camp_P',
            '/Hibiscus/Maps/Camp/Camp_Plot_M.Camp_Plot_M:PersistentLevel.Elevator_Hib_DahlShip_2',
            200, 10),
        ("Heart's Desire", 'Venue_P',
            '/Hibiscus/Maps/Venue/Venue_IOs.Venue_IOs:PersistentLevel.Elevator_Hib_EleanorOffice_3',
            150, 10),
        ("Heart's Desire", 'Venue_P',
            '/Hibiscus/Maps/Venue/Venue_IOs.Venue_IOs:PersistentLevel.Elevator_PrisonArmory_4',
            200, 10),
        ("The Blastplains", 'Frontier_P',
            '/Geranium/Maps/Frontier/Frontier_M_MoneyBackGuarantee.Frontier_M_MoneyBackGuarantee:PersistentLevel.Elevator_MoneyBack_frontier_2',
            200, 10),
        ("Bloodsun Canyon - Presentation Room", 'Facility_P',
            '/Geranium/Maps/Facility/Facility_M_Plot.Facility_M_Plot:PersistentLevel.Elevator_ToLowerFacility_2',
            # This one's as slow as VIP Tower, but I'm sticking with our default scaling since
            # there's other sequences associated with it (the curtains + lights, specifically,
            # on the first trip down)
            400, 40),
        ("Bloodsun Canyon - Boss", 'Facility_P',
            '/Geranium/Maps/Facility/Facility_M_Plot.Facility_M_Plot:PersistentLevel.Elevator_Boss_2',
            200, 15),
        ("Crater's Edge Gondola", 'CraterBoss_P',
            '/Geranium/Maps/CraterBoss/CraterBoss_Boss.CraterBoss_Boss:PersistentLevel.Elevator_CraterBoss_Gondola_2',
            200, 50),
        ]):
    mod.comment(label)
    mod.reg_hotfix(Mod.EARLYLEVEL, level,
            obj_name,
            'ElevatorSpeed',
            speed*global_scale,
            )
    mod.reg_hotfix(Mod.EARLYLEVEL, level,
            obj_name,
            'ElevatorTravelTime',
            travel_time/global_scale,
            )
    if 'Elevator_Ep06_AtlasHQ_V_0' in obj_name:
        # For some reason, at our default speedup, this elevator often kills the player once
        # it gets to the bottom.  Setting killDelay to 0 seems to take care of that (as does
        # 1?  the default is 6).  No idea what that parameter actually does, but it's weird.
        # The `bCrushPlayers` seemed a likely culprit as well, but that doesn't seem to be
        # involved.
        mod.reg_hotfix(Mod.EARLYLEVEL, level,
                obj_name,
                'killDelay',
                0,
                )
    elif 'Elevator_CraterBoss_Gondola_2' in obj_name:
        # This one has an extra attr, just hardcode it stupidly in here.
        mod.reg_hotfix(Mod.EARLYLEVEL, level,
                obj_name,
                'TramTravelTime',
                43/global_scale,
                )
    mod.newline()

# Some elevators (okay, possibly just the ones in Atlas HQ) need some extra ubergraph love
# once the mission is done -- the tweak above only seems to apply on the very first trip up.
mod.header('Extra Elevator Tweaks')

# This is what speeds up the elevator for us on subsequent rides
mod.comment('Atlas HQ - Main Office Elevator (post-mission-activation)')
mod.bytecode_hotfix(Mod.LEVEL, 'AtlasHQ_P',
        '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_M_EP06OfficeSpaceInvaders',
        'ExecuteUbergraph_AtlasHQ_M_EP06OfficeSpaceInvaders',
        6427,
        25,
        25/global_scale)
mod.newline()

mod.comment("Stormblind Complex (Arm's Race) elevator activation delay")
mod.reg_hotfix(Mod.LEVEL, 'FrostSite_P',
        '/Ixora/Maps/FrostSite/FrostSite_Combat.FrostSite_Combat:PersistentLevel.Elevator_FrostSite_2',
        'SwitchDelayTime',
        0,
        )
mod.newline()

# Negul Neshai elevator timing; the elevator itself works just fine with the
# timing tweak above, but there's a mission objective on the elevator button
# whose activation is on a timer
mod.comment('Negul Neshai elevator-button timing')
mod.bytecode_hotfix(Mod.LEVEL, 'Camp_P',
        '/Game/PatchDLC/Hibiscus/Missions/Plot/EP05_DLC2',
        'ExecuteUbergraph_EP05_DLC2',
        34634,
        5,
        5/global_scale)
mod.newline()

# Bloodsun Canyon initial delay
mod.comment('Bloodsun Canyon presentation room - initial elevator delay')
mod.reg_hotfix(Mod.LEVEL, 'Facility_P',
        '/Geranium/Maps/Facility/Facility_M_Plot.Facility_M_Plot:PersistentLevel.Elevator_ToLowerFacility_2',
        'SwitchDelayTime',
        0)
mod.newline()

mod.comment('Bloodsun Canyon presentation room - light activation sequence')
mod.reg_hotfix(Mod.LEVEL, 'Facility_P',
        '/Geranium/Maps/Facility/Facility_M_Plot.Facility_M_Plot:PersistentLevel.SEQ_ElevatorMuralLights.AnimationPlayer',
        'PlaybackSettings.PlayRate',
        # The presentation room elevator takes 40 seconds by default, but is also delayed
        # by 6 seconds.  I suspect that this sequence is timed to coincide with that total
        # 46-second period, rather than just 40.  So, since we're getting rid of that
        # activation delay, if we want it to end at about the same time, we'd need to
        # scale the curtains+lights slightly differently.
        46/(40/global_scale),
        )
mod.newline()

# Turns out the Dandelion slots are identical, bytecodewise (at least for these two offsets)
mod.header('Slot Machine Tweaks')
for obj_name, export in [
        ('/Game/InteractiveObjects/SlotMachine/_Shared/_Design/BPIO_SlotMachine', 'ExecuteUbergraph_BPIO_SlotMachine'),
        ('/Dandelion/InteractiveObjects/PlayableSlotMachines/BPIO_SlotMachine_Dandelion_V1', 'ExecuteUbergraph_BPIO_SlotMachine_Dandelion_V1'),
        ]:
    mod.bytecode_hotfix(Mod.LEVEL, 'MatchAll',
            obj_name,
            export,
            1513,
            5,
            5/global_scale)
    mod.bytecode_hotfix(Mod.LEVEL, 'MatchAll',
            obj_name,
            export,
            2889,
            1,
            1/global_scale)
mod.newline()

# Lost Loot Machine
mod.header('Lost Loot Machine Gear-Spawning Delay')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
        '/Game/InteractiveObjects/GameSystemMachines/LostLootMachine/_Design/BP_LostLootMachine.BP_LostLootMachine_C:OakLostLoot_GEN_VARIABLE',
        'DelayBetweenSpawningItem',
        0.75/global_scale,
        )
mod.newline()

# Diamond Armory
# See also the IO() tweaks above
mod.header('Mission/Level Specific: Diamond Armory Timing Tweaks')
mod.comment('Event Delays')
for attr, default_val in [
        ('TimeToSpawnLootOver', 5),
        ('LootEnabledDelay', 9),
        ('MaxDeferredSpawnDelay', 2),
        ]:
    for obj_name in [
            'BPIO_DiamondChestWall_Shields',
            'BPIO_DiamondChestWall_Guns',
            'BPIO_DiamondChestWall_Grenades',
            ]:
        mod.reg_hotfix(Mod.LEVEL, 'Sanctuary3_P',
                f'/Game/PatchDLC/DiamondLootChest/Maps/Sanctuary3/Sanctuary3_DiamondChestRoom.Sanctuary3_DiamondChestRoom:PersistentLevel.{obj_name}.Loot',
                attr,
                default_val/global_scale,
                )
for attr, default_val in [
        ('SpawnChestLootDelay', 3),
        ]:
    for obj_name in [
            '/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/_Design/Chest/BPIO_DiamondChest.Default__BPIO_DiamondChest_C',
            '/Game/PatchDLC/DiamondLootChest/Maps/Sanctuary3/Sanctuary3_DiamondChestRoom.Sanctuary3_DiamondChestRoom:PersistentLevel.BPIO_DiamondChest_V_3',
            ]:
        mod.reg_hotfix(Mod.LEVEL, 'Sanctuary3_P',
                obj_name,
                attr,
                default_val/global_scale,
                )
mod.reg_hotfix(Mod.LEVEL, 'Sanctuary3_P',
        '/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/_Design/BP_CE_DiamondChest_Loot_Flash.Default__BP_CE_DiamondChest_Loot_Flash_C',
        'Duration',
        9/global_scale,
        )
# This is what determines how soon the last bit of gear spawns, on top of
# the armory console itself.  Keeping this more conservative so that it
# lines up a bit better with the golden particlesystem stuff.
mod.reg_hotfix(Mod.LEVEL, 'Sanctuary3_P',
        '/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/_Design/BP_CE_DiamondChest_Loot_Glimmer.Default__BP_CE_DiamondChest_Loot_Glimmer_C',
        'Duration',
        4.5/1.5,
        )
mod.newline()

mod.comment('Bytecode delay tweaks')
for obj_name, export_name, indexes in [
        ('/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/_Design/Walls/BPIO_DiamondChestWall',
            'ExecuteUbergraph_BPIO_DiamondChestWall',
            [
                (2457, 2, None),
                # Okay, so *this* is the timer for re-enabling the armory after an activation.
                # If it's scaled *too* much, one or more of the walls might not actually
                # populate the armory, which'll softlock it until the user quits + re-enters.
                # Looks like at the moment the most I can scale it by is 1.5x before we risk
                # screwing up the walls.  *Really* I'm guessing that what this means is that
                # I'm missing some scaling on something else -- will look around for that.
                (3310, 13.6, 1.5),
                (3435, 0.25, None),
                ]),
        ('/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/_Design/Chest/BPIO_DiamondChest',
            'ExecuteUbergraph_BPIO_DiamondChest',
            [
                (238, 1.4, None),
                (2248, 1, None),
                (2325, 0.2, None),
                ([5609, 5716], 1.5, None),
                (9273, 2, None),
                ]),
        ]:
    for index, default_val, bytecode_scale in indexes:
        if bytecode_scale is None:
            bytecode_scale = global_scale
        mod.bytecode_hotfix(Mod.LEVEL, 'Sanctuary3_P',
                obj_name,
                export_name,
                index,
                default_val,
                round(default_val/bytecode_scale, 6),
                )
mod.newline()

mod.comment('ParticleSystems')
for ps_name in [
        #'/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_Countdown',
        '/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_FloorRays',
        '/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_InitialOpen',
        '/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_ItemSparkle',
        '/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_LegendaryAttract',
        '/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_Room_CeilingRays',
        #'/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_Room_FloorVapor',
        #'/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_Room_FloorVapor_DiamondDust',
        '/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_Room_LaserShapes',
        #'/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_Room_SteamJet',
        #'/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_Room_WallVapor',
        #'/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_UsePrompt',
        '/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_WallDiamondDust_Burst',
        '/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_WallDiamondDust_Burst_Longer',
        '/Game/PatchDLC/DiamondLootChest/LevelArt/Environments/DiamondCrate/Effects/Systems/PS_DiamondCrate_WallRollDiamondDust',
        ]:
    scale_ps(mod, data, Mod.LEVEL, 'Sanctuary3_P', ps_name, global_scale)
mod.newline()

# Bad Reception door-timing fix
mod.header('Bad Reception umbrella garage door timing tweaks')
mod.reg_hotfix(Mod.LEVEL, 'Prologue_P',
        '/Game/Maps/Zone_0/Prologue/Prologue_M_BadReception.Prologue_M_BadReception:PersistentLevel.IO_Door_400x400_SlideUp_Pandora_Generic_2.Timeline_0_0',
        'TheTimeline.Length',
        # This seems about right -- running will still *just* block you, but
        # sliding works so long as it's timed right.
        round(3/3),
        )
mod.newline()

# Golden Calves Statue Scanner
mod.header('Mission/Level Specific: Custom Golden Calves Statue Scanner Tweaks')

mod.comment('Shorten scanner-light animation')
# TODO: Maybe convert this to `scale_ps()`?
mod.reg_hotfix(Mod.LEVEL, 'Sacrifice_P',
        '/Game/InteractiveObjects/MissionScripted/Effects/System/PS_Scanning_Machine',
        'Emitters.Emitters[0].Object..LODLevels.LODLevels[0].Object..RequiredModule.Object..EmitterDuration',
        12/global_scale)
mod.reg_hotfix(Mod.LEVEL, 'Sacrifice_P',
        '/Game/InteractiveObjects/MissionScripted/Effects/System/PS_Scanning_Machine',
        'Emitters.Emitters[0].Object..LODLevels.LODLevels[0].Object..Modules.Modules[1].Object..Lifetime.Distribution.Object..Constant',
        12/global_scale)
mod.newline()

mod.comment('Shorten delay between scanning + printing')
mod.reg_hotfix(Mod.LEVEL, 'Sacrifice_P',
        '/Game/Maps/Zone_0/Sacrifice/Sacrifice_M_GoldenCalves.Sacrifice_M_GoldenCalves:PersistentLevel.IO_MissionScripted_StatueManufacturingMachine_2.Scanning',
        'TheTimeline.Length',
        12/global_scale)
mod.reg_hotfix(Mod.LEVEL, 'Sacrifice_P',
        '/Game/Maps/Zone_0/Sacrifice/Sacrifice_M_GoldenCalves.Sacrifice_M_GoldenCalves:PersistentLevel.IO_MissionScripted_StatueManufacturingMachine_2.Scanning',
        'TheTimeline.Events.Events[0].Time',
        round(4.014948/global_scale, 6))
mod.newline()

# Not sure what most of this does, though at least one of them is an initial delay when
# you stick the posters in, before they start getting sucked into the machine.
mod.comment('Tweak a few shorter delays')
for index, cur_val in [
        (575, 0.2),
        (899, 2.0),
        # Honestly not sure if these two should be combined; not sure what they control and it's
        # not super obvious.
        (976, 1.0),
        (2539, 1.0),
        ]:
    mod.bytecode_hotfix(Mod.LEVEL, 'Sacrifice_P',
            '/Game/InteractiveObjects/MissionScripted/_Design/IO_MissionScripted_StatueManufacturingMachine',
            'ExecuteUbergraph_IO_MissionScripted_StatueManufacturingMachine',
            index,
            cur_val,
            round(cur_val/global_scale, 6))
mod.newline()

# This is all pretty stupid.  The pouring animation is hardcoded to 20 seconds; we chop
# six seconds off to get it down to 14.  That's the minimum we can do without causing
# the game to skip dialogue.
pour_duration = 14
mod.header('Mission/Level Specific: Coffee-pouring Animations during Rise and Grind')
# This one handles the visual fill-level on the side
# getall IO_MissionPlaceable_RiseAndGrind_3Thermos_C FillDuration
mod.reg_hotfix(Mod.LEVEL, 'City_P',
        '/Game/Maps/Zone_1/City/City_M_RiseAndGrind.City_M_RiseAndGrind:PersistentLevel.RiseAndGrind_Thermos',
        'FillDuration',
        pour_duration)
# Next two handle the actual pouring animation
# getall DistributionFloatConstant Constant name=RequiredDistributionSpawnRate outer=PS_CoffeePour_Stream
# TODO: Maybe convert this to `scale_ps()`?  This one's pretty custom-purpose, though, so maybe leave as-is.
mod.reg_hotfix(Mod.LEVEL, 'City_P',
        '/Game/Missions/Side/Zone_1/City/RiseAndGrind/Effects/Systems/PS_CoffeePour_Stream.PS_CoffeePour_Stream:ParticleModuleSpawn_1.RequiredDistributionSpawnRate',
        'Constant',
        pour_duration)
# getall ParticleModuleRequired EmitterDuration name=ParticleModuleRequired_1 outer=PS_CoffeePour_Stream
mod.reg_hotfix(Mod.LEVEL, 'City_P',
        '/Game/Missions/Side/Zone_1/City/RiseAndGrind/Effects/Systems/PS_CoffeePour_Stream.PS_CoffeePour_Stream:ParticleModuleRequired_1',
        'EmitterDuration',
        pour_duration)
# *This* is the timer which activates the pickup and allows the mission to continue
mod.bytecode_hotfix(Mod.LEVEL, 'City_P',
        '/Game/Maps/Zone_1/City/City_M_RiseAndGrind',
        'ExecuteUbergraph_City_M_RiseAndGrind',
        6616,
        20,
        pour_duration)
mod.newline()

# The remaining speed improvements here would have to be done in relation to a
# `BPChar_GenericMonk` named "Brother Catus" spawning in to run over and open the
# door.  We could make him faster, but the bulk of the time is actually spent in
# the spawning animation, so walking/sprinting speed tweaks really don't help
# him much.  And also, since he's not actually an individual BPChar of his own,
# tweaking him would also tweak all other monks in the area, which I'd rather not
# do.  Anyway, these two tweaks improve the opening time pretty well anyway, so
# I'm content with that.  (Another thing to do would be to try and cut Catus out
# of the loop entirely, but I just don't care enough to try and do that without
# breaking the mission entirely.)
mod.header('Mission/Level Specific: Speed up second Athenas Bell of Peace door opening')
mod.bytecode_hotfix(Mod.LEVEL, 'Monastery_P',
        '/Game/Missions/Plot/Mission_Ep06_MeetMaya',
        'ExecuteUbergraph_Mission_Ep06_MeetMaya',
        39968,
        3,
        0)
mod.bytecode_hotfix(Mod.LEVEL, 'Monastery_P',
        '/Game/Maps/Zone_1/Monastery/Monastery_Mission_Ep06_MeetMaya',
        'ExecuteUbergraph_Monastery_Mission_Ep06_MeetMaya',
        49863,
        1,
        0)
mod.newline()

# Don't let Ava spend so long shocked at Maya's death
mod.header("Mission/Level Specific: Speed up Ava's shock-at-Maya's-death time")
mod.reg_hotfix(Mod.LEVEL, 'CityBoss_P',
        '/Game/NonPlayerCharacters/Ava/_Design/Actions/Action_Ava_Loop_Grieve.Default__Action_Ava_Loop_Grieve_C',
        'LoopTime.Range.Value',
        15/global_scale)
mod.bytecode_hotfix(Mod.LEVEL, 'CityBoss_P',
        '/Game/Maps/Zone_1/CityBoss/CityBoss_Mission',
        'ExecuteUbergraph_CityBoss_Mission',
        31722,
        15,
        15/global_scale)
mod.newline()

# Exploding Statues (in Jakobs Estate)
mod.header('Mission/Level Specific: Exploding Statue Tweaks')
for obj_name in [
        'Mansion_M_AureliasSkeletons.Mansion_M_AureliasSkeletons:PersistentLevel.IO_MissionUsable_ButtonStatue_2',
        'Mansion_M_EP09GrandTour.Mansion_M_EP09GrandTour:PersistentLevel.IO_MissionUsable_ExplodingStatue_3',
        'Mansion_M_EP09GrandTour.Mansion_M_EP09GrandTour:PersistentLevel.IO_MissionUsable_ExplodingStatue_1758',
        'Mansion_M_EP09GrandTour.Mansion_M_EP09GrandTour:PersistentLevel.IO_MissionUsable_ExplodingStatue_1388',
        'Mansion_P:PersistentLevel.IO_MissionUsable_ExplodingStatue_3',
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Mansion_P',
            f'/Game/Maps/Zone_2/Mansion/{obj_name}.RotateStatue',
            'TheTimeline.Length',
            1/global_scale,
            )
    mod.reg_hotfix(Mod.LEVEL, 'Mansion_P',
            f'/Game/Maps/Zone_2/Mansion/{obj_name}.BP_IO_LootSpawnComponent',
            'DelayBeforeSpawningLoot',
            1/global_scale,
            )
mod.newline()

# Sliding Paintings (in Jakobs Estate)
mod.header('Mission/Level Specific: Sliding Painting Tweaks')
for obj_name in [
        'Mansion_Library.Mansion_Library:PersistentLevel.IO_MissionUsable_SlidingPictureFrame_10',
        'Mansion_Library.Mansion_Library:PersistentLevel.IO_MissionUsable_SlidingPictureFrame_11',
        'Mansion_Library.Mansion_Library:PersistentLevel.IO_MissionUsable_SlidingPictureFrame_5',
        'Mansion_Library.Mansion_Library:PersistentLevel.IO_MissionUsable_SlidingPictureFrame_6',
        'Mansion_Library.Mansion_Library:PersistentLevel.IO_MissionUsable_SlidingPictureFrame_7',
        'Mansion_Library.Mansion_Library:PersistentLevel.IO_MissionUsable_SlidingPictureFrame_8',
        'Mansion_Library.Mansion_Library:PersistentLevel.IO_MissionUsable_SlidingPictureFrame_9',
        'Mansion_Theater.Mansion_Theater:PersistentLevel.IO_MissionUsable_SlidingPictureFrame_5',
        'Mansion_Theater.Mansion_Theater:PersistentLevel.IO_MissionUsable_SlidingPictureFrame_8',
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Mansion_P',
            f'/Game/Maps/Zone_2/Mansion/{obj_name}.MoveFrame',
            'TheTimeline.Length',
            1/global_scale,
            )
mod.newline()

# Jakobs Estate Stage Props
mod.header('Mission/Level Specific: Jakobs Estate Stage Prop Tweaks')
mansion_base = '/Game/Maps/Zone_2/Mansion/Mansion_M_EP09GrandTour.Mansion_M_EP09GrandTour:PersistentLevel'
for obj_name, delay in [
        ('IO_Switch_IndustrialSwitch_V_1142', 1.2),
        ('IO_Switch_IndustrialSwitch_V_2148', 1.2),
        ('IO_Switch_IndustrialSwitch_V_991', 2.2),
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Mansion_P',
            f'{mansion_base}.{obj_name}',
            'EndSwitchMovementDelay',
            round(delay/global_scale, 6),
            )
for obj_name, duration in [
        ('E11GrandTour_BackgroundProp', 2.5),
        ('E11GrandTour_LeftProp', 1.5),
        ('E11GrandTour_RightProp', 1.5),
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Mansion_P',
            f'{mansion_base}.{obj_name}',
            'DurationOfPropMovement',
            round(duration/global_scale, 6),
            )
    mod.reg_hotfix(Mod.LEVEL, 'Mansion_P',
            f'{mansion_base}.{obj_name}.Timeline_0',
            'TheTimeline.Length',
            round(1/global_scale, 6),
            )
    mod.reg_hotfix(Mod.LEVEL, 'Mansion_P',
            f'{mansion_base}.{obj_name}.Timeline_0',
            'TheTimeline.Events.Events[0].Time',
            round(0.5/global_scale, 6),
            )
mod.newline()

# Spinning Bookshelves
mod.header('Mission/Level Specific: Jakobs Estate Spinning Bookshelf Tweaks')
mod.reg_hotfix(Mod.LEVEL, 'Mansion_P',
        '/Game/Maps/Zone_2/Mansion/Mansion_P.Mansion_P:PersistentLevel.EasterEgg_SpiningBookshelf',
        'LootSpawnDelay',
        5/global_scale)
mod.newline()

# Sliding Bed in Sacked
mod.header('Mission/Level Specific: Sliding Bed in Sacked')
mod.reg_hotfix(Mod.LEVEL, 'Mansion_P',
        '/Game/Maps/Zone_2/Mansion/Mansion_M_AureliasSkeletons.Mansion_M_AureliasSkeletons:PersistentLevel.IO_MissionUsable_AureliasSkeletons_MovableBed_2.Move Bed',
        'TheTimeline.Length',
        2/global_scale)
mod.newline()

# Going Rogue ID Scanner
# (Honestly don't remember why this is commented out -- I think I remember that
# maybe it turns out to not matter at all?  Maybe the next sequence kicks off
# immediately even though the scanner is still going, or something.)
#mod.header('Mission/Level Specific: Going Rogue ID Scanner')
#mod.reg_hotfix(Mod.LEVEL, 'MarshFields_P',
#        '/Game/Maps/Zone_2/MarshFields/MarshFields_M_Ep12Marshfields.MarshFields_M_Ep12Marshfields:PersistentLevel.IO_MissionPlaceable_Static_Scanned_2.Timeline_0',
#        'TheTimeline.Length',
#        2/global_scale)
#mod.newline()

# Rumble in the Jungle Chasm-Jump Timer
mod.header('Mission/Level Specific: Rumble in the Jungle Chasm-Jump Timer')
mod.bytecode_hotfix(Mod.LEVEL, 'Watership_P',
        '/Game/Missions/Side/Zone_2/Watership/Mission_RumbleJungle',
        'ExecuteUbergraph_Mission_RumbleJungle',
        47567,
        30,
        5)
mod.newline()

# BALEX / EMS Bot door-opening scanning
mod.header('Mission/Level Specific: BALEX / EMS Bot door-opening scanning')
mod.reg_hotfix(Mod.LEVEL, 'Watership_P',
        '/Game/Missions/Side/Zone_2/Watership/RumbleJungle/Action_ServiceBot_Rumble_OpenDoor.Default__Action_ServiceBot_Rumble_OpenDoor_C',
        'PlayRate',
        1*global_scale)
mod.newline()

# Splinterlands Car Grinder
mod.header('Mission/Level Specific: Splinterlands Car Grinder Conveyor')
mod.reg_hotfix(Mod.LEVEL, 'Motorcade_P',
        '/Game/Maps/Zone_3/Motorcade/Motorcade_M_Plot.Motorcade_M_Plot:PersistentLevel.ConveyorDisplacementZone_GEN_VARIABLE_DisplacementZone_CAT_2260',
        'Speed',
        200*global_scale)
mod.newline()

# Splinterlands grinder magnet (not especially important but whatever)
mod.header('Mission/Level Specific: Splinterlands Car Grinder Magnet')
mod.reg_hotfix(Mod.LEVEL, 'Motorcade_P',
        f'/Game/Missions/Plot/EP17_BigChase/BP_Ep17_CarGrinder.BP_Ep17_CarGrinder_C:NODE_AddInterpToMovementComponent-3',
        'Duration',
        # This needs to be scaled back a little bit for... reasons?  Anyway, 2/3 seems
        # about right, so there we are.
        6/(global_scale*2/3),
        )
mod.newline()

# Eridian statue rotation in Tazendeer Ruins
mod.header('Mission/Level Specific: Eridian statue rotation in Tazendeer Ruins')
mod.reg_hotfix(Mod.EARLYLEVEL, 'Beach_P',
        '/Game/Maps/Zone_4/Beach/Beach_Plot_M.Beach_Plot_M:PersistentLevel.IO_BeachHead_EridianStatueMaliwan_0.RotatingMovement',
        'Duration',
        7/global_scale)
mod.reg_hotfix(Mod.LEVEL, 'Beach_P',
        '/Game/Maps/Zone_4/Beach/Beach_Plot_M.Beach_Plot_M:PersistentLevel.IO_BeachHead_EridianStatueMaliwan_0',
        'DelayBeforePlayingSequence',
        7/global_scale)
mod.newline()

# These two are so the ceiling portal opens up in time, instead of knocking
# the player off the elevator and to their death (lol)
mod.header('Mission/Level Specific: Tazendeer Ruins elevator ceiling door')
for obj_name in [
        'IO_Beachhead_ElevatorCeilingSceal_1',
        'IO_Beachhead_ElevatorCeilingSceal_4',
        ]:
    obj_name_full = f'/Game/Maps/Zone_4/Beach/Beach_Plot_M.Beach_Plot_M:PersistentLevel.{obj_name}'
    mod.reg_hotfix(Mod.LEVEL, 'Beach_P',
            obj_name_full,
            # Despite the word "speed" in here, this is actually a duration!
            'SlideSpeed',
            5/global_scale)
    mod.reg_hotfix(Mod.LEVEL, 'Beach_P',
            obj_name_full,
            'DelayBeforeStartAnim',
            3/global_scale)
mod.newline()

# There's a dialogue trigger at the top of the elevator which, at default speeds, is just about
# perfectly timed to kick off as soon as you get up there, but with any speedup at all, you arrive
# while Typhon's still talking on the way up, so the dialogue is skipped.  This tweak moves that
# trigger a little ways "forwards" towards where the bridge raises up out of the ground, so that
# the player could wait to finish the voice line before moving (though realistically, I'm not sure
# anyone who doesn't know about this would actually wait around).  We're also speeding up the
# bridge-raising animation here to account for the delayed trigger, since both that and the dialogue
# get triggered by the same event.  (See also the `AS_Bridge_Going_up` tweaks up in our main
# AnimSequence section.)
mod.header('Mission/Level Specific: Tazendeer Ruins post-elevator dialogue trigger and bridge-raising tweaks')
mod.reg_hotfix(Mod.LEVEL, 'Beach_P',
        '/Game/Maps/Zone_4/Beach/Beach_Plot_M.Beach_Plot_M:PersistentLevel.OakMissionWaypointBox_0.CollisionComp',
        'RelativeLocation',
        '(X=45044,Y=22996,Z=10648)',
        notify=True,
        )
for num, default in [
        (2, 4.2),
        (3, 3.8),
        (4, 3.0),
        (5, 3.4),
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Beach_P',
            f'/Game/Maps/Zone_4/Beach/Beach_TempleSecondFloor.Beach_TempleSecondFloor:PersistentLevel.IO_BeachHead_EridianBridge_{num}',
            'AnimationDelay',
            default/global_scale,
            )
mod.newline()

# Typhon digistruct in Tazendeer Ruins
mod.header('Mission/Level Specific: Typhon digistruct in Tazendeer Ruins')
mod.reg_hotfix(Mod.LEVEL, 'Beach_P',
        '/Game/Missions/Plot/EPXX_Beachhead/Effects/CoordinatedEffect/BP_CE_Typhon_Teleport.Default__BP_CE_Typhon_Teleport_C',
        'Duration',
        6/global_scale,
        )
# There's a lingering red glow which persists for the original 6-seconds-or-so.
# Not sure where that's coming from, but it doesn't seem important -- the final
# piece I was missing was the bytecode patch here, which happens inside a call
# to FinishSpeak.  Maybe we don't even *actually* need to speed up the
# ParticleSystem?
scale_ps(mod, data, Mod.LEVEL, 'Beach_P',
        '/Game/Missions/Plot/EPXX_Beachhead/Effects/Particles/PS_EP21_Typhon_Teleport',
        global_scale)
mod.bytecode_hotfix(Mod.LEVEL, 'Beach_P',
        '/Game/Missions/Plot/Mission_Ep21_Beachhead',
        'ExecuteUbergraph_Mission_Ep21_Beachhead',
        4145,
        5.6,
        round(5.6/global_scale, 6))
mod.newline()

# Initial door-opening triggers in Pyre of Stars
mod.header('Mission/Level Specific: Door-opening triggers in Pyre of Stars')
# kk, so the last arg to PlaySingleAnimation *is* a playrate arg.  This basically does the same
# thing as our AnimSequence tweaks to SK_Desolate_CryptDoor_Anim, above.  Sticking with the AS
# tweaks instead.
#mod.bytecode_hotfix(Mod.LEVEL, 'Crypt_P',
#        '/Game/InteractiveObjects/Doors/Nekro/_Design/IO_Door_Custom_Nekro_Crypt_Small',
#        'ExecuteUbergraph_IO_Door_Custom_Nekro_Crypt_Small',
#        296,
#        1,
#        global_scale)
mod.bytecode_hotfix(Mod.LEVEL, 'Crypt_P',
        '/Game/InteractiveObjects/Doors/Nekro/_Design/IO_Door_Custom_Nekro_Crypt_Small',
        'ExecuteUbergraph_IO_Door_Custom_Nekro_Crypt_Small',
        334,
        7,
        7/global_scale)
mod.newline()

# Eridian statue tweaks in Pyre of Stars
mod.header('Mission/Level Specific: Eridian statue tweaks in Pyre of Stars')

mod.comment('Timeline tweaks')
for num in [0, 2, 5, 8]:
    # See also: the IO_MissionScripted_EridianStatue tweaks above
    mod.reg_hotfix(Mod.LEVEL, 'Crypt_P',
            f'/Game/Maps/Zone_4/Crypt/Crypt_M_EP22TheMachine.Crypt_M_EP22TheMachine:PersistentLevel.IO_MissionScripted_EridianStatue_{num}',
            'TheTimeline.Length',
            6/global_scale,
            )
mod.newline()

mod.comment('Dialogue triggers')
mod.bytecode_hotfix(Mod.LEVEL, 'Crypt_P',
        '/Game/Missions/Plot/Mission_Ep22_TheMachine',
        'ExecuteUbergraph_Mission_Ep22_TheMachine',
        [38557, 25548],
        8,
        8/global_scale)
mod.bytecode_hotfix(Mod.LEVEL, 'Crypt_P',
        '/Game/Missions/Plot/Mission_Ep22_TheMachine',
        'ExecuteUbergraph_Mission_Ep22_TheMachine',
        3523,
        8.5,
        8.5/global_scale)
mod.newline()

# Rising platforms in Pyre of Stars
mod.header('Mission/Level Specific: Rising platforms in Pyre of Stars')

mod.comment('Timeline tweaks')
for num, delay in [
        (0, 1.5),
        (1, 2.5),
        (2, 3),
        (3, 0.5),
        (4, 1),
        ]:
    # See also: the IO_MissionScripted_EridianRaisingPlatform tweak above
    base_obj_name = f'/Game/Maps/Zone_4/Crypt/Crypt_M_EP22TheMachine.Crypt_M_EP22TheMachine:PersistentLevel.IO_MissionScripted_EridianRaisingPlatform_{num}'
    mod.reg_hotfix(Mod.LEVEL, 'Crypt_P',
            base_obj_name,
            'DelayBeforeStartingMovement',
            delay/global_scale)
    mod.reg_hotfix(Mod.LEVEL, 'Crypt_P',
            f'{base_obj_name}.MovePlatform',
            'TheTimeline.Length',
            1/global_scale)
mod.newline()

mod.comment('Action trigger for Typhon')
mod.bytecode_hotfix(Mod.LEVEL, 'Crypt_P',
        '/Game/Maps/Zone_4/Crypt/Crypt_M_EP22TheMachine',
        'ExecuteUbergraph_Crypt_M_EP22TheMachine',
        11737,
        6.5,
        6.5/global_scale)
mod.newline()

# Fire In The Sky rocket launch
mod.header('Mission/Level Specific: Fire In The Sky rocket launch')

mod.comment('Sparrow dialogue trigger')
mod.bytecode_hotfix(Mod.LEVEL, 'Beach_P',
        '/Game/Missions/Side/Zone_4/Desolate/Mission_BetterTimes',
        'ExecuteUbergraph_Mission_BetterTimes',
        22911,
        5,
        5/global_scale)
mod.newline()

mod.comment('Rocket Acceleration')
mod.reg_hotfix(Mod.LEVEL, 'Beach_P',
        '/Game/Maps/Zone_4/Beach/Beach_M_BetterTimes.Beach_M_BetterTimes:PersistentLevel.IO_MissionScripted_BetterTimes_Rocket.SplineFollower',
        'Acceleration',
        # Doing some guesstimation here
        round(0.025*global_scale*3, 6))
mod.newline()

mod.comment('Extra rocket effect trigger')
mod.bytecode_hotfix(Mod.LEVEL, 'Beach_P',
        '/Game/Missions/Side/Zone_4/Desolate/BetterTimes/IO_MissionScripted_BetterTimes_Rocket',
        'ExecuteUbergraph_IO_MissionScripted_BetterTimes_Rocket',
        2047,
        10,
        10/global_scale*1.5)
mod.newline()

mod.comment('Explosion trigger')
mod.bytecode_hotfix(Mod.LEVEL, 'Beach_P',
        '/Game/Missions/Side/Zone_4/Desolate/BetterTimes/IO_MissionScripted_BetterTimes_Rocket',
        'ExecuteUbergraph_IO_MissionScripted_BetterTimes_Rocket',
        479,
        30,
        30/global_scale*1.5)
mod.newline()

# Scryer's Crypt Door Phaselock-opening
mod.header("Mission/Level Specific: Scryer's Crypt Main Door")

mod.comment('Ava Phaselock animation')
mod.bytecode_hotfix(Mod.LEVEL, 'NekroMystery_p',
        '/Ixora2/Maps/Mystery/Nekro/NekroMystery_Mission',
        'ExecuteUbergraph_NekroMystery_Mission',
        53486,
        16,
        16/door_scale)
mod.newline()

mod.comment('Post-open delay')
mod.bytecode_hotfix(Mod.LEVEL, 'NekroMystery_p',
        '/Ixora2/Maps/Mystery/Nekro/NekroMystery_Mission',
        'ExecuteUbergraph_NekroMystery_Mission',
        55436,
        2.5,
        2.5/door_scale)
mod.newline()

# See also: IO_Door_IXO_TombEntrance_SlideUp speedups above
mod.comment('Actual door-opening timeline')
mod.reg_hotfix(Mod.LEVEL, 'NekroMystery_p',
        '/Ixora2/Maps/Mystery/Nekro/NekroMystery_Mission.NekroMystery_Mission:PersistentLevel.IO_Door_IXO_TombEntrance_SlideUp_2.Timeline_DoorOpening',
        'TheTimeline.Length',
        20/door_scale),
mod.newline()

# Arm's Race
mod.header("Mission/Level Specific: Remove Arm's Race Countdown")
mod.bytecode_hotfix(Mod.LEVEL, 'FrostSite_P',
        '/Game/PatchDLC/Ixora/Missions/Side/Mission_GearUp',
        'ExecuteUbergraph_Mission_GearUp',
        23316,
        10,
        0)
mod.bytecode_hotfix(Mod.LEVEL, 'FrostSite_P',
        '/Ixora/Maps/FrostSite/FrostSite_Mission',
        'ExecuteUbergraph_FrostSite_Mission',
        6200,
        10,
        0)
mod.newline()

# Maliwan Raid Start countdown
mod.header('Mission/Level Specific: Takedown at the Maliwan Blacksite start countdown')
mod.bytecode_hotfix(Mod.LEVEL, 'Raid_P',
        '/Game/PatchDLC/Raid1/Missions/Mission_Raid1',
        'ExecuteUbergraph_Mission_Raid1',
        13903,
        3,
        0)
mod.bytecode_hotfix(Mod.LEVEL, 'Raid_P',
        '/Game/PatchDLC/Raid1/Maps/Raid/Raid_M_RaidOnMaliwan',
        'ExecuteUbergraph_Raid_M_RaidOnMaliwan',
        2535,
        3,
        0)
mod.newline()

# Guardian Raid Start countdown
mod.header('Mission/Level Specific: Takedown at the Guardian Breach start countdown')
mod.bytecode_hotfix(Mod.LEVEL, 'GuardianTakedown_P',
        '/Game/PatchDLC/Takedown2/Missions/Side/Mission_Takedown2',
        'ExecuteUbergraph_Mission_Takedown2',
        8789,
        3,
        0)
mod.bytecode_hotfix(Mod.LEVEL, 'GuardianTakedown_P',
        '/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Mission',
        'ExecuteUbergraph_GuardianTakedown_Mission',
        1843,
        3,
        0)
mod.newline()

# Minos Prime initial crystals
mod.header('Mission/Level Specific: Initial Minos Prime Crystal Pads')
for obj_name in [
        'IO_Takedown2_GuardianPad_0',
        'IO_Takedown2_GuardianPad_3',
        ]:
    # These start at 47 and go up to 100, so 26 should complete them in ~2sec.
    mod.reg_hotfix(Mod.LEVEL, 'GuardianTakedown_P',
            f'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Mission.GuardianTakedown_Mission:PersistentLevel.{obj_name}',
            'ChargeIncreasePerSecond',
            # Default: 3
            26)
    mod.reg_hotfix(Mod.LEVEL, 'GuardianTakedown_P',
            f'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Mission.GuardianTakedown_Mission:PersistentLevel.{obj_name}',
            'ChargeDelayTime',
            # Default: 2
            0)
    mod.reg_hotfix(Mod.LEVEL, 'GuardianTakedown_P',
            f'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Mission.GuardianTakedown_Mission:PersistentLevel.{obj_name}',
            'AddMaxChargePerPlayer',
            # Default: 20
            0)
mod.newline()

# Villa Ultraviolet book puzzle triggers (see also the IO() tweaks above)
mod.header('Mission/Level Specific: Villa Ultraviolet book switches')
for num in [
        286,
        287,
        288,
        289,
        290,
        291,
        292,
        293,
        294,
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Cartels_P',
            f'/Game/PatchDLC/Event2/Maps/Cartels_Combat.Cartels_Combat:PersistentLevel.SM_Book__{num}.Timeline_Rotation_Book',
            'TheTimeline.Length',
            2/global_scale,
            )
mod.newline()

# Villa Ultraviolet fountain (see also the IO() tweaks above)
mod.header('Mission/Level Specific: Villa Ultraviolet fountain')
tl_name = '/Game/PatchDLC/Event2/Maps/Cartels_Mission.Cartels_Mission:PersistentLevel.IO_MissionScripted_CartelFountain.Timeline_MoveFountain'
mod.reg_hotfix(Mod.LEVEL, 'Cartels_P',
        tl_name,
        'TheTimeline.Length',
        16/global_scale,
        )
for idx, default in enumerate([
        0,
        2.9,
        6.5,
        13.5,
        15.0,
        ]):
    if default != 0:
        mod.reg_hotfix(Mod.LEVEL, 'Cartels_P',
                tl_name,
                f'TheTimeline.Events.Events[{idx}].Time',
                round(default/global_scale, 6),
                )
mod.newline()

# Spendopticon Hyperway Speedups
mod.header('Mission/Level Specific: Spendopticon Hyperway Speedups')
hl_obj = '/Dandelion/MapSpecific/Strip/HyperHoop/BP_HyperHoop_VNat'
hl_obj_def = f'{hl_obj}.Default__BP_HyperHoop_VNat_C'
hl_spline_obj = f'{hl_obj_def}:HyperHoop_SplineFollowerComponent'

# I think it's the first bytecode hotfix that has the most effect here; the other
# three below it didn't seem to actually do much on their own?  It's possible we
# could trim down these hotfixes by quite a bit, but I'm a bit sick of testing it
# out so I'm leaving it as-is.
mod.comment('Digistruct-In Animations')
hyperway_in_scale=2
mod.bytecode_hotfix(Mod.LEVEL, 'Strip_P',
        hl_obj,
        'ExecuteUbergraph_BP_HyperHoop_VNat',
        1378,
        2.85,
        2.85/hyperway_in_scale,
        )
mod.bytecode_hotfix(Mod.LEVEL, 'Strip_P',
        hl_obj,
        'ExecuteUbergraph_BP_HyperHoop_VNat',
        1265,
        3,
        3/hyperway_in_scale,
        )
mod.reg_hotfix(Mod.LEVEL, 'Strip_P',
        '/Dandelion/MapSpecific/Strip/HyperHoop/BP_CE_Hyperhoop_Digistruct_In.Default__BP_CE_Hyperhoop_Digistruct_In_C',
        'Duration',
        3/hyperway_in_scale)
scale_ps(mod, data, Mod.LEVEL, 'Strip_P',
        '/Dandelion/MapSpecific/Strip/HyperHoop/Effects/Particles/PS_Hyperhoop_Spawn',
        global_scale)
mod.newline()

# So the arrival dialogue is triggered by the deceleration, and gets cut off
# once the player-exit animation is finished.  There may be some bytecodey
# things we could do to allow the dialogue to continue after that point, but
# it seemed more straightforward to just push back the deceleration trigger.
# We're setting the Min/Max speed to equal, so that trigger *only* really
# affects the dialogue.  This timing is basically perfect for English dialogue
# to the both districts.  The Vice district lines can get away with 52000, but
# one Market line needs slightly more time.  Note that the *starting* dialogue
# can sometimes get a bit lost as you zip away, for the longer dialogues.
mod.comment('Travel Parameters')
mod.reg_hotfix(Mod.LEVEL, 'Strip_P',
        hl_obj_def,
        'DistanceFromEndDecelerate',
        # default: 8000
        54000)
mod.reg_hotfix(Mod.LEVEL, 'Strip_P',
        hl_obj_def,
        'DelayBeforeMove',
        # default: 0.25
        0.4)
mod.reg_hotfix(Mod.LEVEL, 'Strip_P',
        hl_obj_def,
        'DelayBeforeExitAnim',
        # default: 1.25
        0.25)
hl_speed_scale=1.7
for attr, default in [
        ('MaxSpeed', 5000),
        #('MinSpeed', 500),
        ('MinSpeed', 5000),
        #('Acceleration', 300),
        ('TurnRate', 150),
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Strip_P',
            hl_spline_obj,
            attr,
            default*hl_speed_scale,
            )
mod.newline()

# This totally wasn't worth the effort it took to track down; in the end the biggest
# win was updating that TheTimeline attr, though the bytecode tweak technically
# shaves a second off the response time as well.
mod.header('Mission/Level Specific: BUD Bot rescue-response delay')
mod.reg_hotfix(Mod.LEVEL, 'Impound_P',
        '/Dandelion/Maps/Impound/Impound_Mission.Impound_Mission:PersistentLevel.IO_Door_Hyperion_Single_6.Alpha',
        'TheTimeline.Length',
        2.5/door_scale,
        )
mod.bytecode_hotfix(Mod.LEVEL, 'Impound_P',
        '/Game/PatchDLC/Dandelion/Missions/Plot/Mission_DLC1_Ep03_Impound',
        'ExecuteUbergraph_Mission_DLC1_Ep03_Impound',
        4757,
        1,
        0)
mod.newline()

# This was an interesting one.  There's an AS_Impound_Bridge object which we could do
# our usual Stuff to, but doing so makes the bridge-extension animation freak the hell
# out and seemingly never stop.  I tried various things related to that but never got
# it to work.  Then in the SEQ object itself there's some PlayRate stuff where the
# AS is linked-to, but it looks like we may not be able to get at it with hotfixes (or
# at least I couldn't figure it out, and they don't show up in obj dump or via PythonSDK's
# dumper -- it's got similar shenanigans to the Raid1 itempool expansion stuff.  Those
# were in a "PrecompiledEvaluationTemplate" attr, though, and the name makes me think
# that we probably couldn't get at them even if we had the syntax right.)  I did find that
# the SEQ object itself has a `PlaybackSettings` attr, on which we can set a PlayRate, but
# doing that doesn't affect anything, but I also found that `AnimationPlayer` sub-obj,
# which has its *own* `PlaybackSettings` attr, and that, finally did the trick.  So, good
# times!  Pretty simple in the end, but this was the first time we'd run into it.
mod.header("Mission/Level Specific: Freddie's makeshift bridge back to his lair")
mod.reg_hotfix(Mod.LEVEL, 'Impound_P',
        '/Dandelion/Maps/Impound/Impound_Mission.Impound_Mission:PersistentLevel.SEQ_Ep03_Impound_BridgeToHangar.AnimationPlayer',
        'PlaybackSettings.PlayRate',
        global_scale,
        )
mod.newline()

# Setting Default__ works but doesn't actually end up applying on the "real" object
# (regardless of Earlylevel/notify/etc).  Really there's no point in us setting
# Default__ in here, since setting the instantiated one *does* do the trick, but
# it seems a bit wrong to *not* do Default__.  So I'm doing both.  Myeh.
mod.header('Mission/Level Specific: Key To Happiness timer in The Compactor')
for obj_name in [
        '/Dandelion/Maps/Trashtown/Trashtown_M_Plot.Default__Trashtown_M_Plot_C',
        '/Dandelion/Maps/Trashtown/Trashtown_M_Plot.Trashtown_M_Plot:PersistentLevel.Trashtown_M_Plot_C_0',
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Trashtown_P',
            obj_name,
            'HappinessTestDelayTime',
            # Default: 15
            2,
            )
mod.newline()

# Opening the door to VIP Tower
mod.header('Mission/Level Specific: Ultra-Thermite Opening Door to VIP Tower')
mod.reg_hotfix(Mod.LEVEL, 'Strip_P',
        '/Dandelion/Maps/Strip/Strip_PM_TheHeist.Strip_PM_TheHeist:PersistentLevel.GbxLevelSequenceActor_ThermiteFlare.AnimationPlayer',
        'PlaybackSettings.PlayRate',
        global_scale,
        )
mod.reg_hotfix(Mod.LEVEL, 'Strip_P',
        '/Dandelion/Maps/Strip/Strip_PM_TheHeist.Strip_PM_TheHeist:PersistentLevel.GbxLevelSequenceActor_ThermiteDoorOpen.AnimationPlayer',
        'PlaybackSettings.PlayRate',
        2,
        )
mod.newline()

# Lots of closely-associated Call of the Deep tweaks, in Skittermaw Basin
mod.header('Mission/Level Specific: Call of the Deep Tweaks, in Skittermaw Basin')

# Power coil panel in Call of the Deep
mod.comment('Power Coil panel - acquiring the coil')
mod.reg_hotfix(Mod.LEVEL, 'Lake_P',
        '/Hibiscus/Maps/Lake/Lake_S_WhereIBelong.Lake_S_WhereIBelong:PersistentLevel.IO_MissionScripted_CranePartDoor_Excavation.Rotate',
        'TheTimeline.Length',
        0.75/global_scale,
        )
mod.newline()

mod.comment('Power coil panel - installing at crane')
mod.reg_hotfix(Mod.LEVEL, 'Lake_P',
        '/Hibiscus/Maps/Lake/Lake_S_WhereIBelong.Lake_S_WhereIBelong:PersistentLevel.IO_MissionScripted_CranePartDoor_Crane.Rotate',
        'TheTimeline.Length',
        0.75/global_scale,
        )
mod.newline()

# Slapping in the getall here 'cause I always have to reconstruct the buggers every time:
# getall gbxlevelsequenceplayer PlaybackSettings name=AnimationPlayer outer=GbxLevelSequenceActor_Crane_MoveCageToPlatform
mod.comment('Initial crane placement')
mod.reg_hotfix(Mod.LEVEL, 'Lake_P',
        '/Hibiscus/Maps/Lake/Lake_S_WhereIBelong.Lake_S_WhereIBelong:PersistentLevel.GbxLevelSequenceActor_Crane_MoveCageToPlatform.AnimationPlayer',
        'PlaybackSettings.PlayRate',
        global_scale,
        )
mod.newline()

# Gythian Blood Jar fill-up
mod.comment('Gythian Blood Jar Fill-Up')
mod.reg_hotfix(Mod.LEVEL, 'Lake_P',
        '/Hibiscus/Maps/Lake/Lake_S_WhereIBelong.Lake_S_WhereIBelong:PersistentLevel.IO_MissionPlaceable_BloodJarToFill.Timeline_0',
        'TheTimeline.Length',
        5/global_scale,
        )
mod.newline()

mod.comment('Cage door Opening/closing')
mod.reg_hotfix(Mod.LEVEL, 'Lake_P',
        '/Hibiscus/Maps/Lake/Lake_S_WhereIBelong.Lake_S_WhereIBelong:PersistentLevel.IO_MissionScripted_CageDoor_2.Raise',
        'TheTimeline.Length',
        1.5/door_scale,
        )
mod.newline()

# There's also Seq_WhereIBelong_CraneMoveCageIntoWater involved, but I'm leaving
# that one because there's associated dialogue which takes basically the whole time.
mod.comment('Post-mission Crane Raising')
mod.reg_hotfix(Mod.LEVEL, 'Lake_P',
        '/Hibiscus/Maps/Lake/Lake_S_WhereIBelong.Lake_S_WhereIBelong:PersistentLevel.GbxLevelSequenceActor_Crane_LiftCageOutOfWater.AnimationPlayer',
        'PlaybackSettings.PlayRate',
        global_scale,
        )
mod.newline()

# DJ Midnight Dark Mix mission-close delay
mod.header('Mission/Level Specific: DJ Midnight Dark Mix Mission-Close Delay')
mod.bytecode_hotfix(Mod.LEVEL, 'Bar_P',
        '/Hibiscus/Maps/Bar/Bar_Side_M_SinisterSounds',
        'ExecuteUbergraph_Bar_Side_M_SinisterSounds',
        2518,
        20,
        # It's tempting to make this even shorter, but I'd like to have a
        # bit more of DJ Midnight's Dark Mix animation before having her
        # revert back to the usual.
        20/global_scale)
mod.newline()

# Cold Case: Buried Questions
mod.header('Mission/Level Specific: Cold Case: Buried Questions speedups')

mod.comment('Crypt opening')
mod.reg_hotfix(Mod.LEVEL, 'Village_P',
        '/Hibiscus/Maps/Village/Village_Side_M_PrivateEye01.Village_Side_M_PrivateEye01:PersistentLevel.GbxLevelSequenceActor_OpenCryptDoor.AnimationPlayer',
        'PlaybackSettings.PlayRate',
        0.25*door_scale,
        )
mod.newline()

# See also the tweaks in the IO() section
mod.comment('Secret Wall')
mod.reg_hotfix(Mod.LEVEL, 'Village_P',
        '/Hibiscus/Maps/Village/Village_Side_M_PrivateEye01.Village_Side_M_PrivateEye01:PersistentLevel.IO_Scripted_PrivateEye_SecretWall_5.Wall Opening animation',
        'TheTimeline.Length',
        7/global_scale,
        )

mod.newline()

# Brewery equipment in The Cankerwood.
mod.header('Mission/Level Specific: Cankerwood Brewery Equipment')

mod.comment('Nozzle Animations')
# Not actually making use of duration here, since we're now altering PlayRate instead of Length.  Keeping
# those values in here just in case I ever change my mind, though, since I'd already put 'em in.
for timeline, duration in [
        ('Sender Pipe Movement', 1.6),
        ('RefillContainer', 0.6),
        ('Pouring', 3),
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Woods_P',
            f'/Hibiscus/Maps/Woods/Woods_Plot_M.Woods_Plot_M:PersistentLevel.BPIO_Hib_EP04_BaitPuzzle_Sender_2.{timeline}',
            'TheTimeline.PlayRate',
            global_scale,
            )
mod.newline()

mod.comment('Receptacle Animations')
# Not actually making use of duration here, since we're now altering PlayRate instead of Length.  Keeping
# those values in here just in case I ever change my mind, though, since I'd already put 'em in.
for receiver_num in [2, 3, 4]:
    for timeline, duration in [
            ('FillReceiver', 1.6),
            ('EmptyReceiver', 0.6),
            ]:
        mod.reg_hotfix(Mod.LEVEL, 'Woods_P',
                f'/Hibiscus/Maps/Woods/Woods_Plot_M.Woods_Plot_M:PersistentLevel.BPIO_Hib_EP04_BaitPuzzle_Receiver_{receiver_num}.{timeline}',
                'TheTimeline.PlayRate',
                global_scale,
                )
mod.newline()

mod.comment('Pouring ParticleSystem')
scale_ps(mod, data, Mod.LEVEL, 'Woods_P',
        '/Hibiscus/InteractiveObjects/MissionSpecific/Plot/EP04/BaitPuzzle/Assets/PS_Hib_BaitPuzzle_PourLiquid',
        global_scale)
mod.newline()

mod.comment('Pouring Timings')
for index, delay in [
        # Initial pour timing, up to ValidateRecipe
        (1064, 1.2),
        # End of pour timing
        (734, 1.0),
        # Button-re-enable timing, among others
        (83, 1.5),
        ]:
    mod.bytecode_hotfix(Mod.LEVEL, 'Woods_P',
            '/Hibiscus/InteractiveObjects/MissionSpecific/Plot/EP04/BaitPuzzle/BPIO_Hib_EP04_BaitPuzzleManager',
            'ExecuteUbergraph_BPIO_Hib_EP04_BaitPuzzleManager',
            index,
            delay,
            delay/global_scale,
            )
mod.newline()

# These aren't as clean as I'd like -- like the one that you hit takes a little longer to re-active
# than the other one, so if you want to move left twice (for instance) there's a slightly longer
# delay than there really should be.  I don't see any obvious way to fix that, though, and it's not
# awful, so not much to do but cope!
mod.comment('Button-unlock delays')
mod.bytecode_hotfix(Mod.LEVEL, 'Woods_P',
        '/Hibiscus/InteractiveObjects/MissionSpecific/Plot/EP04/BaitPuzzle/BPIO_Hib_EP04_BaitPuzzleManager',
        'ExecuteUbergraph_BPIO_Hib_EP04_BaitPuzzleManager',
        [1179, 1602],
        2,
        2/global_scale,
        )
mod.newline()

# This one's not really necessary -- you can pick up the jug as soon as the animation starts.  But,
# whatever, we're doing everything else here so why not?
mod.comment('Pedestal Raising')
mod.reg_hotfix(Mod.LEVEL, 'Woods_P',
        '/Hibiscus/Maps/Woods/Woods_Plot_M.Woods_Plot_M:PersistentLevel.BPIO_Hib_EP04_BaitContainer_2.Movement',
        'TheTimeline.PlayRate',
        global_scale,
        )
mod.newline()

# Heart's Desire hidden-elevator desk drawers
mod.comment("Heart's Destire hidden-elevator desk drawers")
for num in [6, 7, 8, 9]:
    mod.reg_hotfix(Mod.LEVEL, 'Venue_P',
            f'/Hibiscus/Maps/Venue/Venue_IOs.Venue_IOs:PersistentLevel.BPIO_Hib_EP06_DeskDrawer_{num}.DrawerMovement',
            'TheTimeline.PlayRate',
            global_scale)
mod.newline()

# Money Back Guarantee artillery cannon
mod.header('Mission/Level Specific: Artillery cannon for Money Back Guarantee, in The Blastplains')
mod.reg_hotfix(Mod.LEVEL, 'Frontier_P',
        '/Geranium/Maps/Frontier/Frontier_M_MoneyBackGuarantee.Frontier_M_MoneyBackGuarantee:PersistentLevel.SEQ_Frontier_ArtilleryCannon_2.AnimationPlayer',
        'PlaybackSettings.PlayRate',
        global_scale,
        )
mod.reg_hotfix(Mod.LEVEL, 'Frontier_P',
        '/Geranium/Maps/Frontier/Frontier_M_MoneyBackGuarantee.Frontier_M_MoneyBackGuarantee:PersistentLevel.IO_MissionUsable_ArtilleryCannon_2',
        'DelayBeforePlayingSequence',
        1/global_scale,
        )
mod.newline()

# Various Oletta tweaks.  I'm using notify=True for most of these, and I'm not sure if
# it's actually required in all cases (or at all) - I'd just used it by default since
# many other RelativeLocation tweaks tend to need it.
mod.header('Mission/Level Specific: Various Oletta / Lost and Found tweaks')

# AINodes that Oletta will follow.  In the vanilla data, she hangs around at
# the first node after picking up the quest.  Then when you talk to her, she
# proceeds through the second and third (and beyond to a few more).  What I'm
# doing here, instead, is extending her post-spawn node traversal to include
# that second node, since she runs to those.  Then talking to her will kick off
# at that third node, instead of the second.  She ends up teleporting a bit to
# the second node; I haven't figured that one out yet.  Unfortunately we can't
# *just* go to the second node because she ends up teleporting the *entire*
# way there.
oletta_first_node_comp = '/Geranium/Maps/Forest/Forest_M_AnimalControl.Forest_M_AnimalControl:PersistentLevel.AINode_3.AINodeComponent'
oletta_second_node = '/Geranium/Maps/Forest/Forest_M_AnimalControl.Forest_M_AnimalControl:PersistentLevel.AINode_1'
oletta_second_node_comp = f'{oletta_second_node}.AINodeComponent'
oletta_third_node = '/Geranium/Maps/Forest/Forest_M_AnimalControl.Forest_M_AnimalControl:PersistentLevel.AINode_2'

# Also shuffling the nodes around a bit.  The first node is moving to the
# previous location of the second node, and the second is moving out onto
# the "bridge"
oletta_first_node_coords = '(X=-4007.6667,Y=-5736.0737,Z=1459.2206)'
oletta_second_node_coords = '(X=-3404,Y=-6601,Z=1625)'

# Tighten up some dialogue delays to make it fit more nicely on the way to her lab.
mod.comment('Intro dialogue delay tweaks')
for index, cur_delay in [
        ([25040, 1171], 2),
        (826, 3),
        ]:
    mod.bytecode_hotfix(Mod.LEVEL, 'Forest_P',
            '/Game/PatchDLC/Geranium/Missions/Plot/Mission_Ep03_ObsidianForest',
            'ExecuteUbergraph_Mission_Ep03_ObsidianForest',
            index,
            cur_delay,
            0.5)
mod.newline()

mod.comment("Move Oletta's initial Lost and Found waiting point")
mod.reg_hotfix(Mod.LEVEL, 'Forest_P',
        oletta_first_node_comp,
        'RelativeLocation',
        oletta_first_node_coords,
        notify=True,
        )
mod.newline()

mod.comment("Give Oletta's Lost and Found waiting point a further navigation node")
# Link Oletta's standing point to AINode_1 (usually a part of the
# next sequence after you've said hello to her)
mod.reg_hotfix(Mod.LEVEL, 'Forest_P',
        oletta_first_node_comp,
        'LinksTo',
        """
        (
            (
                Weight=1,
                PrevWeight=0,
                Actor={}
            )
        )
        """.format(Mod.get_full_cond(oletta_second_node, 'AINode')),
        notify=True,
        )
# Cut off AINode_1's link
mod.reg_hotfix(Mod.LEVEL, 'Forest_P',
        oletta_second_node_comp,
        'LinksTo',
        '',
        notify=True,
        )
mod.newline()

mod.comment('Extend second navigation node onto bridge')
# Move AINode_1 further out onto the bridge
mod.reg_hotfix(Mod.LEVEL, 'Forest_P',
        oletta_second_node_comp,
        'RelativeLocation',
        oletta_second_node_coords,
        notify=True,
        )
# ... and tighten up its arrival threshhold
mod.reg_hotfix(Mod.LEVEL, 'Forest_P',
        oletta_second_node_comp,
        'ArrivalThreshold',
        '20',
        notify=True,
        )
mod.newline()

# Move the "Meet Oletta" activation sphere near her new starting point, too
mod.comment('Relocate "Talk to Oletta" activation sphere to second navigation node')
mod.reg_hotfix(Mod.LEVEL, 'Forest_P',
        '/Geranium/Maps/Forest/Forest_M_AnimalControl.Forest_M_AnimalControl:PersistentLevel.OakMissionWaypoint_MeetGranny.CollisionComp',
        'RelativeLocation',
        oletta_second_node_coords,
        notify=True,
        )
mod.newline()

mod.comment('Redirect post-"Talk to Oletta" navigation node to the next step')
# Redirect the start of her mission dialogue to the next node along
mod.reg_hotfix(Mod.LEVEL, 'Forest_P',
        '/Geranium/Maps/Forest/Forest_M_AnimalControl.Forest_M_AnimalControl:PersistentLevel.Forest_M_AnimalControl_C_1',
        'AINode_1_ExecuteUbergraph_Forest_M_AnimalControl_RefProperty',
        Mod.get_full_cond(oletta_third_node, 'AINode'),
        notify=True,
        )
mod.newline()

# More dialogue delay tweaks
mod.header('Mission/Level Specific: Quick and the Quickerer Dialogue Delay Tweaks')
mod.bytecode_hotfix(Mod.LEVEL, 'Town_P',
        '/Game/PatchDLC/Geranium/Missions/Side/Mission_Dueling',
        'ExecuteUbergraph_Mission_Dueling',
        8312,
        4,
        0.5,
        )
mod.newline()

# Crater's Edge narration delay
mod.header("Mission/Level Specific: Crater's Edge gondola narration delay")
mod.bytecode_hotfix(Mod.LEVEL, 'CraterBoss_P',
        '/Game/PatchDLC/Geranium/Missions/Plot/Mission_Ep05_Crater',
        'ExecuteUbergraph_Mission_Ep05_Crater',
        19592,
        14,
        0.5)
mod.newline()

# Castle Crimson catapult tweaks
mod.header('Mission/Level Specific: Castle Crimson catapult tweaks')

mod.comment('Pivot Times')
for suffix in [
        '',
        '_0',
        '_1',
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Anger_P',
            f'/Alisma/Maps/Anger/Anger_M_Plot.Anger_M_Plot:PersistentLevel.IO_Ali_CatapultPivot{suffix}',
            'RotateTime',
            3/2)
mod.newline()

mod.comment('Catapult dialogue delay')
mod.bytecode_hotfix(Mod.LEVEL, 'Anger_P',
        '/Game/PatchDLC/Alisma/Missions/Plot/ALI_EP02',
        'ExecuteUbergraph_ALI_EP02',
        27530,
        2,
        0)
mod.bytecode_hotfix(Mod.LEVEL, 'Anger_P',
        '/Game/PatchDLC/Alisma/Missions/Plot/ALI_EP02',
        'ExecuteUbergraph_ALI_EP02',
        29617,
        3,
        0)
mod.newline()

# P.A.T. firing delay
mod.header('Mission/Level Specific: P.A.T. firing delay')
mod.bytecode_hotfix(Mod.LEVEL, 'Anger_P',
        '/Alisma/Maps/Anger/Anger_SM_AllShapesAndCalibers',
        'ExecuteUbergraph_Anger_SM_AllShapesAndCalibers',
        988,
        4,
        0)
mod.newline()

# Ink Blots
mod.header("Mission/Level Specific: Don't Call It A Rorschach Ink-Blot Pipes")
for num in [
        2,
        5,
        9,
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Experiment_P',
            f'/Alisma/Maps/Experiment/Experiment_SM_InkBlots.Experiment_SM_InkBlots:PersistentLevel.IO_MissionScripted_BlotsPipes_{num}.Timeline_RorchaschPuddle',
            'TheTimeline.Length',
            3/global_scale,
            )
mod.newline()

# Honestly not sure yet if I want to put this in here, but I'm doing it for now...
# Can split it out later if I want.
mod.header('NPC Walking Speeds')

class Char():
    """
    Convenience class for looping over a bunch of BPChar objects for speed improvements.
    At the moment there's not really much of a reason to do this instead of just looping
    over a list of tuples, but we're doing other classes like this anyway (IO and AS),
    so I may as well do this too.
    """

    def __init__(self, name, path, scale, sprint_scale=None, force_have_slowdown=False):
        self.name = name
        self.path = path
        self.last_bit = path.split('/')[-1]
        self.default_name = f'Default__{self.last_bit}_C'
        self.default_name_lower = self.default_name.lower()
        self.full_path = f'{self.path}.{self.default_name}'
        self.scale = scale
        self.force_have_slowdown = force_have_slowdown
        if sprint_scale is None:
            self.sprint_scale = scale
        else:
            self.sprint_scale = sprint_scale

    def __lt__(self, other):
        return self.name.casefold() < other.name.casefold()

for char in sorted([
        Char('Claptrap',
            '/Game/NonPlayerCharacters/Claptrap/_Design/Character/BpChar_Claptrap',
            global_char_scale,
            ),
        # At our default scale, DLC6 Claptrap actually cuts off some dialogue.  (It's
        # pretty slight, but still.)  Honestly his speed isn't awful anyway, but eh.
        # (He actually has a line get cut off at one point even at the default speeds.)
        Char('Claptrap (DLC6)',
            '/Ixora2/NonPlayerCharacters/Claptrap/_Design/Character/BPChar_Claptrap_IXO',
            1.2,
            ),
        Char('Ellie',
            '/Game/NonPlayerCharacters/Ellie/_Design/Character/BPChar_Ellie',
            global_char_scale,
            ),
        Char('Lilith',
            '/Game/NonPlayerCharacters/Lilith/_Design/Character/BPChar_Lilith',
            global_char_scale,
            ),
        Char('Ace Baron (Healers and Dealers)',
            '/Game/NonPlayerCharacters/_Promethea/MedicalAssistant/_Design/Character/BPChar_MedicalAssistant',
            global_char_scale,
            ),
        # Vic's got a long way to run -- really bump this one up
        Char('Vic (Head Case)',
            '/Game/NonPlayerCharacters/_Pandora/HeadCaseGirl/_Design/Character/BPChar_HeadCaseGirl',
            3,
            ),
        # Maya's mostly fine, but there's a couple of cases where it'd be nice if she were a bit faster
        Char('Maya',
            '/Game/NonPlayerCharacters/Maya/_Design/Character/BPChar_Maya',
            global_char_scale,
            ),
        # Ava's honestly not too bad, but she's got a long run back from the graveyard
        Char('Ava',
            '/Game/NonPlayerCharacters/Ava/_Design/Character/BPChar_Ava',
            global_char_scale,
            ),
        # ... her DLC6 char does have a tendency to get stuck on stuff, may as well buff her there, too.
        Char('Ava (DLC6)',
            '/Ixora2/NonPlayerCharacters/Ava/_Design/Character/BPChar_Ava_IXO',
            global_char_scale,
            ),
        # This one's a bit silly 'cause he walks all of like three feet, but whatever.
        Char('Liam (Atlas HQ Security Guard)',
            '/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSecurityGuard',
            global_char_scale,
            ),
        Char('Glenn the Ratch',
            '/Game/NonPlayerCharacters/_Promethea/TalkingRatch/_Design/Character/BPChar_TalkingRatch',
            global_char_scale,
            ),
        Char('Terry the Ratch',
            '/Game/NonPlayerCharacters/_Promethea/TalkingRatch/_Design/Character/BPChar_GoodRatch',
            global_char_scale,
            ),
        # Not sure if this is really necessary, but he *can* lag behind in The Anvil.
        Char('Brick',
            '/Game/NonPlayerCharacters/Brick/_Design/Character/BPChar_Brick',
            global_char_scale,
            ),
        # Also not sure how necessary this is; at the moment this hardly improves anything; just her
        # saunter over to construct the bomb, in Anvil.
        Char('Tina',
            '/Game/NonPlayerCharacters/TinyTina/_Design/Character/BPChar_TinyTina',
            global_char_scale,
            ),
        Char('Failurebot',
            '/Game/NonPlayerCharacters/_Eden6/MrInterpolator/_Design/Character/BPChar_MrInterpolator',
            global_char_scale,
            ),
        # Clay is actually fine for most of his interactions in the main game, but he can lag behind
        # on the way to Blackbarrel Cellars
        Char('Clay',
            '/Game/NonPlayerCharacters/Clay/_Design/Character/BPChar_Clay',
            global_char_scale,
            ),
        Char('Clay (DLC6)',
            '/Ixora2/NonPlayerCharacters/Clay/_Design/Character/BPChar_Clay_IXO',
            global_char_scale,
            ),
        # He's not bad in Desolation's Edge, but there's a bit of following in Tazendeer Ruins which
        # could benefit from a speedup, as well as quite a bit in Pyre of Stars.
        Char('Typhon',
            '/Game/NonPlayerCharacters/Typhon/_Design/Character/BPChar_Typhon',
            global_char_scale,
            ),
        # Tannis is honestly fine; you can end up waiting on her a bit in Pyre of Stars, but mostly
        # just if you're doing the kind of mod-testing that this mod encourages.  So, leaving her as-is.
        # (also, in Pyre of Stars, her default speed is about as fast as Typhon's boosted speed, and
        # they tend to run together)
        #Char('Tannis',
        #    '/Game/NonPlayerCharacters/Tannis/_Design/Character/BPChar_Tannis',
        #    global_char_scale,
        #    ),
        Char('VIP Valet / Dealer Bot / Upgraded Dealer Bot',
            '/Game/PatchDLC/Dandelion/Enemies/ServiceBot/Croupier/_Design/Character/BPChar_ServiceBot_Croupier',
            # Not sure if this comes into play at any point beyond the very first door-opening
            # bot, but its default speed is sloooow.  Bumping this up a bit more than our
            # standard rate.  (I think it must be artificially slowed down in bytecode or
            # something, since the actual numbers seem just like most other chars.  Regardless,
            # tweaking these values *does* seem to make that initial door-opening walk quicker,
            # so whatever.)
            global_char_scale*1.5,
            ),
        Char('Timothy Lawrence',
            '/Dandelion/NonPlayerCharacters/Timothy/_Design/Character/BPChar_Timothy',
            global_char_scale,
            # doesn't show up in the serialization but it's there in-game  (setting this
            # doesn't really seem to make much difference, though, alas)
            force_have_slowdown=True,
            ),
        Char('Digby Vermouth',
            '/Dandelion/NonPlayerCharacters/_SideMissions/Digby/_Design/Character/BPChar_Digby',
            global_char_scale,
            ),
        # Honestly Bureaucracy Bot's "premium" speed isn't awful, given the short distance, but
        # bumping it up anyway.
        Char('Bureaucracy Bot (Form Bot)',
            '/Dandelion/Enemies/ServiceBot/ImpoundFeeBot/BPChar_ImpoundFormBot',
            global_char_scale,
            ),
        # Not terrible by default either, given the short distance.
        Char('BUD Bot',
            '/Dandelion/Enemies/Loader/_Unique/Impound/_Design/Character/BPChar_BudLoader',
            global_char_scale,
            ),
        Char('Joy',
            '/Dandelion/NonPlayerCharacters/_SideMissions/Joy/_Design/Character/BPChar_Joy',
            global_char_scale,
            ),
        # Gaige is mostly fine throughout the game, but it's a longish way to Heart's Desire
        # at the end of the DLC, so bumping her up a bit.  Deathtrap's sprint speed is
        # already quite good.
        Char('Gaige',
            '/Hibiscus/NonPlayerCharacters/Gaige/_Design/Character/BPChar_Hib_Gaige',
            global_char_scale,
            ),
        Char('McSmugger',
            '/Geranium/NonPlayerCharacters/GerNPC/McSmugger/_Design/Character/BPChar_McSmugger',
            global_char_scale,
            ),
        # Oletta's actually a tough one to speed up without unintended side effects!  There are
        # four interactions specifically which can cause problems:
        #
        #   1) The initial jaunt over to the lab
        #   2) Heading over to the Traitorweed-testing area
        #   3) Unlocking the door to the rest of the map, and journey back to her starting point
        #   4) Her walk across the rooftops at the beginning of Lost and Found
        #
        # (Her journey back from the lab to have you release the Menta Gnats isn't problematic
        # because the timers on that seem to be entirely dialogue-dependent.)
        #
        # Number 4 in particular *really* needs speeding up, but if we bump up her walking speed
        # too much, all sorts of weirdness can start happening with all the others, so we've got
        # to remain somewhat conservative.  What I'm doing with number 4 is moving some of the
        # AINodes around so that she's got less distance to cover (she runs to the initial
        # waiting point, so this speeds things up nicely).  That and a few other minor
        # tweaks gets all four cases working pretty well.  Oletta *does* do a little bit of
        # teleporting when getting into position for Lost and Found, still, but IMO that's a
        # perfectly fine tradeoff.
        Char('Oletta',
            '/Geranium/NonPlayerCharacters/Granny/_Design/Character/BPChar_Granny',
            global_char_scale,
            ),
        Char('Slim',
            '/Geranium/NonPlayerCharacters/GerNPC/Dueler/_Design/Character/BPChar_Dueler',
            global_char_scale,
            ),
        Char('Drunk William',
            '/Geranium/NonPlayerCharacters/GerNPC/DuelOpponent/_Design/Character/BPChar_DuelOpponent',
            global_char_scale,
            ),
        Char('P.A.T.',
            '/Alisma/NonPlayerCharacters/PAT/_Design/Character/BPChar_PAT',
            global_char_scale,
            ),
        ]):

    found_main = False
    char_data = data.get_data(char.path)
    speed_walk = None
    speed_sprint = None
    have_slowdown = False
    for export in char_data:
        if export['_jwp_object_name'].lower() == char.default_name_lower:
            found_main = True
            if 'OakCharacterMovement' in export:
                if export['OakCharacterMovement']['export'] != 0:
                    move_export = char_data[export['OakCharacterMovement']['export']-1]
                    if 'MaxWalkSpeed' in move_export:
                        speed_walk = move_export['MaxWalkSpeed']['BaseValue']
                    else:
                        # The default
                        speed_walk = 600
                    if 'MaxSprintSpeed' in move_export:
                        speed_sprint = move_export['MaxSprintSpeed']['BaseValue']
                    else:
                        # The default
                        speed_sprint = 900
                    if char.force_have_slowdown \
                            or 'NavSlowdownOptions' in move_export and 'SlowdownSpeed' in move_export['NavSlowdownOptions']:
                        have_slowdown = True
                else:
                    raise RuntimeError('Could not find OakCharacterMovement export in {}'.format(char.path))
            else:
                raise RuntimeError('Could not find OakCharacterMovement in {}'.format(char.path))
            break
    if not found_main:
        raise RuntimeError('Could not find {} in {}'.format(char.default_name, char.path))

    mod.comment(char.name)
    mod.reg_hotfix(Mod.CHAR, char.last_bit,
            char.full_path,
            'OakCharacterMovement.Object..MaxWalkSpeed',
            '(Value={},BaseValue={})'.format(
                round(speed_walk*char.scale, 6),
                round(speed_walk*char.scale, 6),
                ),
            )
    # NOTE: After spending quite a bit of time getting Oletta sorted out, I'm pretty sure
    # that MaxSprintSpeed isn't actually used by NPCs.  I'm pretty sure that the stances
    # used to control NPC speeds just take the walk speed and scale it where appropriate.
    # I think that MaxWalkSpeed itself might even be scaled down a bit for the usual NPC
    # "Walk" stance.
    mod.reg_hotfix(Mod.CHAR, char.last_bit,
            char.full_path,
            'OakCharacterMovement.Object..MaxSprintSpeed',
            '(Value={},BaseValue={})'.format(
                round(speed_sprint*char.sprint_scale, 6),
                round(speed_sprint*char.sprint_scale, 6),
                ),
            )
    if have_slowdown:
        mod.reg_hotfix(Mod.CHAR, char.last_bit,
                char.full_path,
                'OakCharacterMovement.Object..NavSlowdownOptions.bSlowdownNearGoal',
                'False',
                )
        mod.reg_hotfix(Mod.CHAR, char.last_bit,
                char.full_path,
                'OakCharacterMovement.Object..NavSlowdownOptions.SlowdownSpeed.Value',
                1,
                )
    mod.newline()

###
### Various disabled things follow!  These are either bits which *work* but which I
### decided not to do for various reasons, or attempts which just outright failed.
###

# Bomb-conveyor during Capture The Frag
if False:
    # All of this actually works quite well, but the bomb can end up clipping through
    # other conveyor items, which looks weird, and also has a tendency to skip
    # dialogue.  So, whatever, let's just Not Do It.
    bomb_scale = 2
    mod.header('Capture the Frag bomb conveyor')
    mod.reg_hotfix(Mod.LEVEL, 'Wetlands_P',
            '/Game/Maps/Zone_2/Wetlands/Wetlands_M_SpecialDelivery.Wetlands_M_SpecialDelivery:PersistentLevel.BP_TransporterSystem_SpecialDelivery.TransporterTrack1',
            'CarryingSpeed',
            750*bomb_scale)
    # Timing for the bomb breaking down
    for index, from_val in [
            (2598, 25),
            ([4031, 14233], 18),
            (5122, 16),
            (10904, 24),
            (15721, 22),
            ]:
        mod.bytecode_hotfix(Mod.LEVEL, 'Wetlands_P',
                '/Game/Missions/Side/Zone_2/Wetlands/Mission_SpecialDelivery',
                'ExecuteUbergraph_Mission_SpecialDelivery',
                index,
                from_val,
                from_val/bomb_scale,
                )
    mod.newline()

# Peace Bells (or whatever) in Athenas.  Not actually doing this because the speed
# isn't too bad already, and the events they trigger actually happen immediately
# when you "use" them, anyway.  The Ubergraphs sometimes put in some artificial
# delays to make it seem like stuff's happening after, like with the door opening
# I tweaked, above, but it's not actually tied in with this.
if False:

    # Up in the main IO/BPIO section, this speeds up the striker itself...
    #('Large Bells in Athenas', 'Monastery_P', '/Game/InteractiveObjects/BonshuBell/Global/IO_MissionUsable_BonshuBell'),

    # ... and this next bit makes the bell ringing trigger at the right time
    mod.header('Large Bells on Athenas')
    bell_scale=5
    for obj_name in [
            '/Game/Maps/Zone_1/Monastery/Monastery_Mission_MonkMission.Monastery_Mission_MonkMission:PersistentLevel.IO_MissionUsable_BonshuBell_1',
            '/Game/Maps/Zone_1/Monastery/Monastery_Mission_Ep06_MeetMaya.Monastery_Mission_Ep06_MeetMaya:PersistentLevel.IO_MissionUsable_BonshuBell_0',
            '/Game/Maps/Zone_1/Monastery/Monastery_Mission_Ep06_MeetMaya.Monastery_Mission_Ep06_MeetMaya:PersistentLevel.IO_MissionUsable_BonshuBell_1',
            '/Game/Maps/Zone_1/Monastery/Monastery_Mission_Ep06_MeetMaya.Monastery_Mission_Ep06_MeetMaya:PersistentLevel.IO_MissionUsable_BonshuBell_4227',
            ]:
        for subobj in [
                'BellRinging',
                'StrikeBell',
                ]:
            full_obj = f'{obj_name}.{subobj}'
            mod.reg_hotfix(Mod.LEVEL, 'Monastery_P',
                    full_obj,
                    'TheTimeline.Length',
                    4/bell_scale,
                    )
            if subobj == 'StrikeBell':
                mod.reg_hotfix(Mod.LEVEL, 'Monastery_P',
                        full_obj,
                        'TheTimeline.Events.Events[0].Time',
                        1/bell_scale,
                        )
        #mod.reg_hotfix(Mod.LEVEL, 'Monastery_P',
        #        obj_name,
        #        'TheTimeline.PlayRate',
        #        bell_scale,
        #        )
    mod.newline()

# Some attempts to make loot-spewing pickups (bone piles, trash cans, etc) pick up more quickly.
# No luck yet!
if False:

    # The default for this attr (found in droppedinventoryitempickup objects) is 1.  I suspect this
    # *might* be something we could go for?  It feels like these items start auto-picking-up after
    # about 1sec.  I assume that the var means something like "if the item hasn't had a collision after
    # this many seconds, stop applying physics" or somesuch, at which point they're pick-upable.
    # I could be wrong about that, though.  At any rate, this statement looks okay to me but it never
    # seems to change the reported `getall` values.  Could be this is dynamically assigned or something.
    for hftype in [Mod.LEVEL, Mod.EARLYLEVEL]:
        for notify in [True, False]:
            mod.reg_hotfix(hftype, 'MatchAll',
                    '/Game/Pickups/_Shared/_Design/BP_OakConsumableItemPickup.Default__BP_OakConsumableItemPickup_C',
                    'NextImpactTimeThreshold',
                    0.1,
                    notify=notify)

    # So after some more experimentation, I think that the basic issue is that loot
    # doesn't get auto-picked-up until it's no longer being affected by physics.  The
    # engine just waits for them to get "settled" and *then* adds them into whatever
    # structure controls "these are the things you can auto-pick-up."  So in the end,
    # it's sort of the `ShouldAttachLoot` boolean which determines how quickly things
    # like ammo/health/money will get auto-picked up.  The `bSimulatePhysicsAfterOpening`
    # boolean is actually for the container itself, not the loot -- think of the way
    # cardboard boxes get physicsy after they've been opened.  I figured I'd try
    # turning that off too, anyway, just so any loot-attachment didn't get screwed
    # up.
    #
    # Anyway, first attempt: altering the Default__ object.  This just doesn't work;
    # the attrs never get updated on the map objects.  I think it's 'cause the map
    # objects are sort of hardcoded with the defaults already.
    for hf_type in [Mod.EARLYLEVEL, Mod.LEVEL]:
        for notify in [True, False]:
            mod.reg_hotfix(hf_type, 'Towers_P',
                    '/Game/Lootables/_Design/Classes/CoV/BPIO_Lootable_COV_CardboardBox.Default__BPIO_Lootable_COV_CardboardBox_C',
                    'bSimulatePhysicsAfterOpening',
                    'False',
                    notify=notify)
            mod.reg_hotfix(hf_type, 'Towers_P',
                    '/Game/Lootables/_Design/Classes/CoV/BPIO_Lootable_COV_CardboardBox.Default__BPIO_Lootable_COV_CardboardBox_C',
                    'ShouldAttachLoot',
                    'True',
                    notify=notify)

    # ... aaand testing this out by hitting each individual map object.  This *does*
    # work!  The cardboard boxes don't get physics after opening, the loot gets
    # "attached" inside, and money/health/ammo will get immediately auto-picked-up.
    # In the end I wouldn't be willing to do this, though, 'cause I kind of like
    # the default dispersal method (and it might end up weird for stuff like guns),
    # and also because I'd have to touch literally every single relevant object in
    # the game to do it this way.  Eesh.
    #
    # Anyway, the only other alternative here would be to see if there's *some* way
    # to tell the engine to auto-pick-up items even if they're being acted on by
    # physics.  It's possible that there's a boolean somewhere which'd do that (or
    # maybe some ubergraph stuff?) but I haven't found it yet, and don't really care
    # to work hard enough to find it.  I assume that that behavior isn't default
    # For A Reason -- like maybe it's very "expensive" in the engine to keep updating
    # those locations in realtime, in whatever structure controls auto-pick-up.
    # Anyway, for now I'm definitely giving up on it.
    for map_name in [
            '/Game/Maps/Zone_1/Towers/Towers_P',
            '/Game/Maps/Zone_1/Towers/Towers_Combat',
            '/Game/Maps/Zone_1/Towers/Towers_Light',
            ]:
        map_data = data.get_data(map_name)
        map_last = map_name.rsplit('/', 1)[-1]
        for export in map_data:
            if export['export_type'] == 'BPIO_Lootable_COV_CardboardBox_C':
                export_name = export['_jwp_object_name']
                obj_full = f'{map_name}.{map_last}:PersistentLevel.{export_name}'
                mod.reg_hotfix(Mod.EARLYLEVEL, 'Towers_P',
                        obj_full,
                        'bSimulatePhysicsAfterOpening',
                        'False',
                        notify=True)
                mod.reg_hotfix(Mod.EARLYLEVEL, 'Towers_P',
                        obj_full,
                        'ShouldAttachLoot',
                        'True',
                        notify=True)

# While working on speedups for Oletta, there was one annoying sequence at the
# beginning of the Lost and Found mission where her stance was unavoidably locked
# to "Walk" instead of sprint, and she had a *long* way to go, requiring a pretty
# hefty Walk-speed buff to make it reasonable.  Unfortunately, it seems that NPCs
# might not actually use MaxSprintSpeed -- it seems that the game probably just
# scales up MaxWalkSpeed instead, which led to pretty absurd behavior elsewhere in
# Oletta's movements.
#
# So, one thing I'd been doing for awhile was to convert as many of her Run stances
# to Walk, to attempt to compensate for this.  The one place I was aware of where
# this was more-or-less *necessary*, to avoid skipping dialogue, was her initial
# jaunt over to the lab, to charge up the core sample to activate the Menta Gnats.
#
# I'd ended up trying it on *all* the stance parameters that I could find, in the
# end, because her sprint speed was hilariously out of place otherwise, but all of
# this combined ended up causing some really bizarre behavior.  On the way to the
# test area (where you first use Traitorweed), she ends up teleporting a bit, and
# the dialogue triggers are a bit weird.  Then afterwards she seems to say some
# dialogue *early* and open the door to the rest of the level from a distance.
#
# In the end, what I did instead of this was move her navigation AINodes around a
# bit -- she runs from her spawnpoint to the dedicated spot -- and bringing her
# walk speed buff down to our usual levels, and that turned out to be a much better
# solution overall.  Still, leaving this in here in case I want to take another
# look at it.
if False:
    mod.comment('Oletta: Walk instead of Run')
    mod.bytecode_hotfix(Mod.LEVEL, 'Forest_P',
            '/Geranium/Maps/Forest/Forest_M_Ep03_Forest',
            'ExecuteUbergraph_Forest_M_Ep03_Forest',
            # This is the index we *need* to do, to not skip dialogue, btw.  The rest are
            # just because her Run speed looks ridiculous with our enhanced scaling.
            3176,
            #[237, 1352, 3176, 6172, 6692],
            '/Game/NonPlayerCharacters/_Shared/_Design/StanceData/StanceData_NPC_Passive_Run.StanceData_NPC_Passive_Run',
            '/Game/NonPlayerCharacters/_Shared/_Design/StanceData/StanceData_NPC_Passive_Walk.StanceData_NPC_Passive_Walk',
            )
    mod.newline()

# I'd like to speed up the Lost Loot machine's open/close animation, but it acts... *weird*.
# It really should just be our usual IO() shenanigans like so:
#
#     IO('/Game/InteractiveObjects/GameSystemMachines/LostLootMachine/_Design/BP_LostLootMachine',
#         label='Lost Loot Machines',
#         ),
#
# ... but the two relevant FloatCurve objects don't update properly.  It's quite weird; on-disk
# they look like this, which is what the IO() processing has always expected (trimmed down to
# just the relevant info):
#
#     {
#       "export_type": "CurveVector",
#       "_jwp_export_idx": 36,
#       "_jwp_is_asset": false,
#       "_jwp_object_name": "CurveVector_2",
#       "FloatCurves": {
#         "Keys": [
#           { "time": 0.0, "value": -50.0 },
#           { "time": 1.5, "value": 0.0 }
#         ]
#       }
#     }
#
# But via a `getall` on the console, the `FloatCurves` attr shows up as an array (also trimmed
# down to just the relevant info):
#
#     >>> getall CurveVector FloatCurves name=CurveVector_2 outer=BP_LostLootMachine_C <<<
#     0) CurveVector /Game/InteractiveObjects/GameSystemMachines/LostLootMachine/_Design/BP_LostLootMachine.BP_LostLootMachine_C:CurveVector_2.FloatCurves =
#             0: ()
#             1: ()
#             2: (Keys=((Value=-50.000000),(Time=1.500000)))
#
# Below is basically just two attempts to try and alter the `Time` values by going after that
# weird in-engine structure instead, but these don't work any better than the IO() processing
# does.  The attr just never updates.
#
# Anyway, without having these Time attrs update, the Lost Loot open/close animation glitches
# out (when spewing loot, the door remains mostly-closed, and afterwards the door switches to
# being mostly-open).  In the end, I'm just going to leave the open/close animations at the
# default values.  We *are* updating the loot-spew delay, so that bit happens much more quickly.
if False:
    # Test 1
    lost_loot_obj = '/Game/InteractiveObjects/GameSystemMachines/LostLootMachine/_Design/BP_LostLootMachine.BP_LostLootMachine_C'
    for curve_idx, default_val in [
            (0, 1.2),
            (2, 1.5),
            ]:
        mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                f'{lost_loot_obj}:CurveVector_{curve_idx}',
                'FloatCurves.FloatCurves[2].Keys.Keys[1].Time',
                default_val/global_scale,
                )

    # Test 2
    mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
            lost_loot_obj,
            'Timelines.Timelines[0].Object..VectorTracks.VectorTracks[0].CurveVector.Object..FloatCurves.FloatCurves[2].Keys.Keys[1].Time',
            1.2/global_scale,
            )
    mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
            lost_loot_obj,
            'Timelines.Timelines[1].Object..VectorTracks.VectorTracks[0].CurveVector.Object..FloatCurves.FloatCurves[2].Keys.Keys[1].Time',
            1.5/global_scale,
            )

mod.close()

