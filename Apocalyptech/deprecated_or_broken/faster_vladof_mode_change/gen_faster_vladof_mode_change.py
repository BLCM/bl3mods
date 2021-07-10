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

import sys
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

#
# NOTE:
#
# These kinds of animations are *annoying*.  I cannot for the life of me get them to
# look right.  I ran into this with my Mega TimeSaver XL mod as well, specifically
# with the vehicle-related animations.  In short, in an AnimSequence:
#
#     RateScale <- Determines how fast the animation *visually* plays
#     SequenceLength <- Determines the total time length of the animation
#     Notifies <- Triggers events at various times, mostly sound effects and controller feedback
#
# So it seems easy enough.  If you *just* double the RateScale, the animation plays
# at 2x speed, but the game "waits" until the full SequenceLength has elapsed before
# letting you do anything else with the item in question.  So in this case, you'll
# visually get the mode change but you won't be able to fire until the SequenceLength
# is over.  (The animation actually ends up looking pretty weird towards the end, too.)
#
# If you *just* halve the SequenceLength but leave RateScale alone, the animation plays
# at ordinary speed and basically gets cut off halfway through, "jumping" to its end state.
#
# So, you'd think: just double the RateScale *and* halve the SequenceLength, right?  Wrong.
# The animation seems to, like, play at quad speed instead, and part of the animation gets
# cut off anyway, and it's just annoying AF.  For the vehicle animations in Mega Timesaver,
# I ended up settling on a state where the animation seems to "freeze" towards the end.
# For this one, I'm just not happy with any option, so it's going into my deprecated/broken
# pile for now.  I've tried various values inbetween 1 and 2 for the RateScale but it's
# just... annoying.  I dunno.
#
# So anyway, yeah.  This mod as-written contains various hardcoded scales in the method
# because I was trying out various combinations.  The Notifies stuff doesn't seem to really
# affect much of anything.  Here's the table of data that I'd been accumulating, with one
# particular Vladof AR:
#
#   RateScale   Notifies    EndLink     SequenceLength  Timing  Animation
#   ---------   --------    -------     --------------  ------  ---------
#   1           1           1           1               8.7     Perfectly Lined Up
#   2           1           1           1               8.7     Animation finishes halfway before you get control
#   1           1           1           2               4.2     Animation gets cut off halfway through
#   2           1           1           2               4.2     Animation finishes halfway before you get control
#   2           2           1           2               4.2     Animation finishes halfway before you get control
#   2           2           2           2               4.2     Animation finishes halfway before you get control
#   1           2           2           2               4.2     Animation gets cut off halfway through
#
# The timings (and notes) there aren't *super* accurate really, but they give you a feel for it.
# I'd been timing from when the mode-switch animation starts, to when the gun is capable of
# being fired next.  Timing was done on some video capture being played at 10% speed, to make
# stopwatching it a bit easier.  I didn't end up writing down my fractional RateScale notes,
# but none of them really looked great, IMO.
#
# Anyway, we'll see if I get back to it.

mod = Mod('faster_vladof_mode_change.txt',
        'Faster Vladof Mode Change',
        'Apocalyptech',
        [
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='gear-general, qol',
        )

data = BL3Data()

def do_anim_scale(obj_name, scale):

    global data

    hf_trigger = Mod.PATCH
    hf_target = ''

    scale = 2

    mod.reg_hotfix(hf_trigger, hf_target,
            obj_name,
            'RateScale',
            scale)

    scale = 2

    # Now we get into AnimSequence specifics.  This'll happen so long as there's
    # data which makes sense to alter (ie: non-`0` values)
    as_data = data.get_exports(obj_name, 'AnimSequence')[0]
    if 'Notifies' in as_data:
        for idx, notify in enumerate(as_data['Notifies']):
            for var in ['SegmentBeginTime', 'SegmentLength', 'LinkValue']:
                if var in notify and notify[var] != 0:
                    mod.reg_hotfix(hf_trigger, hf_target,
                            obj_name,
                            'Notifies.Notifies[{}].{}'.format(idx, var),
                            round(notify[var]/scale, 6))

            # If we have targets inside EndLink, process that, too.  (So far, it doesn't
            # look like any animations we touch actually have anything here.)
            endlink = notify['EndLink']
            #if 'export' not in endlink['LinkedMontage'] \
            #        or endlink['LinkedMontage']['export'] != 0 \
            #        or 'export' not in endlink['LinkedSequence'] \
            #        or endlink['LinkedSequence']['export'] != 0:
            for var in ['SegmentBeginTime', 'SegmentLength', 'LinkValue']:
                if var in endlink and endlink[var] != 0:
                    mod.reg_hotfix(hf_trigger, hf_target,
                            obj_name,
                            'Notifies.Notifies[{}].EndLink.{}'.format(idx, var),
                            round(endlink[var]/scale, 6))

    scale = 2

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
                obj_name,
                'SequenceLength',
                round(as_data['SequenceLength']/scale, 6))

global_scale = 2
for label, weap_type_1st, weap_type_other, anim_scale, animations_both, animations_first in [
        ('Assault Rifles', 'Rifle/AssaultRifle', 'AssaultRifle', global_scale, [
            'AS_AR_VLA_Mode_Return_180_Auto',
            'AS_AR_VLA_Mode_Return_180',
            'AS_AR_VLA_Mode_Return_90_Auto',
            'AS_AR_VLA_Mode_Return_90',
            'AS_AR_VLA_Mode_Switch_180_Auto',
            'AS_AR_VLA_Mode_Switch_180',
            'AS_AR_VLA_Mode_Switch_90_Auto',
            'AS_AR_VLA_Mode_Switch_90',
            'AS_AR_VLA_Bipod_Out',
            'AS_AR_VLA_Bipod_Return',
            ], set([
            'AS_AR_VLA_Mode_Return_180_AutoE',
            'AS_AR_VLA_Mode_Return_90_AutoE',
            'AS_AR_VLA_Mode_Switch_180_AutoE',
            'AS_AR_VLA_Mode_Switch_90_AutoE',
            ])),
        ]:

    mod.header(label)
    animations_both.extend(list(animations_first))
    for anim_obj in animations_both:

        mod.comment(anim_obj)

        if anim_obj not in animations_first:
            do_anim_scale(f'/Game/PlayerCharacters/_Shared/WeaponAnimation/{weap_type_other}/Vladof/{anim_obj}', anim_scale)

        do_anim_scale(f'/Game/PlayerCharacters/_Shared/Animation/{weap_type_1st}/Vladof/1st/{anim_obj}', anim_scale)

        mod.newline()

    # ehhhhh
    # So if we ever do get around to making this into a fully-fledged (and workable) mod,
    # we may want to *start* with these Hold objects, walk through the Action objects, and
    # arrive at the actual animations from there, rather than hardcoding them in a list
    # like we're doing above.  Since I can't get these damned animations to look right,
    # though, for now it's being left here.
    #
    # Also: I would be surprised if these BlendInTime/DefaultBlendOutTime changes do anything.
    hold = data.get_data('/Game/PlayerCharacters/_Shared/_Design/WeaponHolds/AssaultRifle/WeaponHold_AR_VLA')[0]
    actions = set()
    for action in hold['WeaponActions']:
        if action['WeaponAction'] == 'EWAT_UseModeSwitch':
            for cwa in action['ConditionalWeaponActions']:
                for ca in cwa['ConditionalActions']:
                    actions.add(ca['Action'][1])
    for action_name in actions:
        last_bit = action_name.split('/')[-1]
        with_c = '{}_C'.format(last_bit)
        action = data.get_data(action_name)
        for export in action:
            if export['export_type'] == with_c:
                blend_in = export['BlendInTime']
                blend_out = export['DefaultBlendOutTime']
                mod.reg_hotfix(Mod.PATCH, '',
                        '{}.Default__{}'.format(action_name, with_c),
                        'BlendInTime',
                        blend_in/2)
                mod.reg_hotfix(Mod.PATCH, '',
                        '{}.Default__{}'.format(action_name, with_c),
                        'DefaultBlendOutTime',
                        blend_out/2)

mod.close()
