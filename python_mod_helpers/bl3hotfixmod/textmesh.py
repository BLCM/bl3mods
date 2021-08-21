#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# --
#
# The `rotate_points` function was written by StackOverflow user M Oehm,
# and is licensed under CC BY-SA 3.0 - https://creativecommons.org/licenses/by-sa/3.0/

import math
import enum
import statistics

class Point:
    """
    A somewhat badly-named class; is just a placement of a specific letter at an x,y,z
    coordinate, before any transforms (rotation, scaling, etc) have been performed.
    """

    def __init__(self, letter, x, y, z):
        self.letter = letter
        self.x = x
        self.y = y
        self.z = z

class LetterMIStatus:
    """
    Some status vars to keep track of, when applying global MIs to fonts.
    The `used` set keeps track of the (lowercased) map names in which this
    letter's been used already.  The `mi` dict keeps track of which MIs to
    apply in which levels -- the keys are the lowercased map names, and the
    values are the full path to the MIs in question.  The special-case `*`
    value can be used for the map name, to have the MI to apply to any
    map which isn't explicitly named.
    """

    def __init__(self):
        self.used = set()
        self.mi = {}

    def _is_level_used(self, level):
        """
        Returns `True` if we've been used on the specified `level` (which should be
        just the "final" end `*_P` level name.
        """
        return level.lower() in self.used

    def _set_level_used(self, level):
        """
        Sets ourselves to be in a "used" state on the given `level`.
        """
        self.used.add(level.lower())

class Letter:
    """
    Info about a single letter
    """

    def __init__(self, letter, width, height, origin_w, origin_h, mesh_override=None):
        """
        `letter` - The letter this object will represent
        `width` - The letter's width (in in-engine units, taken from the StaticMesh object)
        `height` - The letter's width (in in-engine units, taken from the StaticMesh object)
        `origin_w` - The letter's horizontal origin (in in-engine units, taken from the StaticMesh object)
        `origin_h` - The letter's vertical origin (in in-engine units, taken from the StaticMesh object)
        `mesh_override` - If not `None`, this is the string in the object name used to uniquely
            identify this letter.  Used in the Title Card font for things like punctuation.
        """
        self.letter = letter.upper()
        self.width = width
        self.height = height
        self.origin_w = origin_w
        self.origin_h = origin_h
        self.mesh_path = None
        self.mesh_override = mesh_override
        self.font = None

        # A couple computed params
        self.w_offset = (self.width/2)+self.origin_w
        self.h_offset = (self.height/2)+self.origin_h

        # Info used by MI-setting
        self.mistatus = {}

    def _finalize(self, font, pattern):
        """
        Once we're added into a Font, call this to finish setting up our data, such as linking
        back to the Font we belong to, and populating our full object path.
        """
        self.font = font
        if self.mesh_override:
            self.mesh_path = pattern.format(self.mesh_override)
        else:
            self.mesh_path = pattern.format(self.letter)

    def _ensure_mistatus(self, mod):
        """
        Makes sure that we have a LetterMIStatus object for the given mod.
        Returns the LetterMIStatus object, for convenience
        """
        if mod not in self.mistatus:
            self.mistatus[mod] = LetterMIStatus()
        return self.mistatus[mod]

    def _is_level_used(self, mod, level):
        """
        Returns `True` if we've been used in the active `mod`, on the specified
        `level` (which should be just the "final" end `*_P` level name.
        """
        mistatus = self._ensure_mistatus(mod)
        return mistatus._is_level_used(level)

    def _set_level_used(self, mod, level):
        """
        Sets ourselves to be in a "used" state in the active `mod`, on the given
        `level`.  If this is the first time we're being used, we will also create
        a hotfix using the Mod `mod` to set the MaterialInterface/MaterialInstance,
        if we have one defined for this level.
        """
        mistatus = self._ensure_mistatus(mod)
        level_lower = level.lower()
        if not self._is_level_used(mod, level):
            mistatus._set_level_used(level)
            if self.font.supports_mi:
                self._hotfix_level_mi(mod, level)

    def set_level_mi(self, mod, mi, level='*'):
        """
        Sets the MaterialInterface/MaterialInstance `mi` on ourselves, in the
        active `mod`, for the given `level`.  The special-case level `*` value
        can be used to have the MI apply to all levels.  If we have already been
        used in the specified level(s), will also create hotfixes for the given
        levels, using `mod`, to set the MIs.
        """
        if not self.font.supports_mi:
            print('WARNING: font {} does not support MaterialInterface/MaterialInstance coloration'.format(self.font.name))
            return
        mistatus = self._ensure_mistatus(mod)
        level_lower = level.lower()
        # Eh, don't bother checking for this, actually.  It seems to work just fine, and might
        # even happen on purpose if someone wants nearly all letters to be one color but
        # override on just a few.  Not worth complaining about.
        #if level_lower in mistatus.mi:
        #    if mistatus.mi[level_lower].lower() != mi.lower():
        #        print('WARNING: Changing {} {}\'s MI in {} from {} to {}'.format(
        #            self.font.name,
        #            self.letter,
        #            level,
        #            mistatus.mi[level_lower].split('/')[-1],
        #            mi.split('/')[-1],
        #            ))
        #        print('          This is unsupported and will result in undefined behavior!')
        mistatus.mi[level_lower] = mi
        if level == '*':
            # If we're setting a wildcard, loop through all levels in which we've been used...
            for used_level_lower in mistatus.used:
                # ... and if there is NOT a specific MI set up for that level, hotfix ours in.
                if used_level_lower not in mistatus.mi:
                    # Note that we aren't trying to use `MatchAll` here because then we'd have
                    # to be much more cautious about hotfix ordering
                    self._hotfix_level_mi(mod, used_level_lower)
        else:
            # If we're setting a specific level, and we've been used on this level, hotfix the MI
            if self._is_level_used(mod, level):
                self._hotfix_level_mi(mod, level)

    def _hotfix_level_mi(self, mod, level):
        """
        Given a Mod object `mod`, and a specific level `level`, hotfix our custom MI, if
        we have one set.  If a specific MI hasn't been set for `level`, we'll fall back
        to the wildcard (assuming that's present).
        """
        if not self.font.supports_mi:
            print('WARNING: font {} does not support MaterialInterface/MaterialInstance coloration'.format(self.font.name))
            return
        mistatus = self._ensure_mistatus(mod)
        level_lower = level.lower()
        if level_lower in mistatus.mi:
            mod.comment('bl3hotfixmod.textmesh - setting {}\'s {} in {} to use {}'.format(
                self.font.name,
                self.letter,
                level,
                mistatus.mi[level_lower].split('/')[-1]
                ))
            mod.reg_hotfix(mod.LEVEL, level,
                    self.mesh_path,
                    'StaticMaterials.StaticMaterials[0].MaterialInterface',
                    mod.get_full_cond(mistatus.mi[level_lower], 'MaterialInstanceConstant'))
        elif '*' in mistatus.mi:
            mod.comment('bl3hotfixmod.textmesh - setting {}\'s {} in {} (via wildcard) to use {}'.format(
                self.font.name,
                self.letter,
                level,
                mistatus.mi['*'].split('/')[-1]
                ))
            mod.reg_hotfix(mod.LEVEL, level,
                    self.mesh_path,
                    'StaticMaterials.StaticMaterials[0].MaterialInterface',
                    mod.get_full_cond(mistatus.mi['*'], 'MaterialInstanceConstant'))

class Font:
    """
    Aggregate info about a specific Font
    """

    def __init__(self, name, obj_pattern, char_spacing, line_spacing, line_z_offset, supports_mi, letters):
        """
        `name` - English description of the font; only used in mod comments.
        `obj_pattern` - Format string to generate the StaticMesh object paths
        `char_spacing` - Extra spacing to put inbetween characters
        `line_spacing` - Extra spacing to put inbetween lines
        `line_z_offset` - How much we need to lower the text so that it's oriented properly
            along the Z axis, in units of line height.  This varies depending on the font.
            This could actually be programmatically determined from the Letter `origin_w`
            and `origin_h` values -- This value should be 1 when the origin values are
            approximately zero, and 2 when the origin values are approximately half the
            total letter height.
        `supports_mi` - `True` if this font supports setting coloration info via
            MaterialInterface/MaterialInstance objects, or `False` otherwise
        `letters` - A list of `Letter` objects belonging to this font.
        """
        self.name = name
        self.obj_pattern = obj_pattern
        self.char_spacing = char_spacing
        self.line_spacing = line_spacing
        self.line_z_offset = line_z_offset
        self.supports_mi = supports_mi
        self.letters = {}
        for letter in letters:
            letter._finalize(self, obj_pattern)
            self.letters[letter.letter] = letter

        # Compute the width of our "space" char, and also our character-derived line height.
        # We're going to omit any letters which have a mesh_override specified, since those
        # may be special chars like commas, periods, etc.
        relevant_chars = []
        for l in self.letters.values():
            if not l.mesh_override:
                relevant_chars.append(l)
        self.space_width = statistics.geometric_mean([l.width for l in relevant_chars])
        self.line_height = statistics.geometric_mean([l.height for l in relevant_chars])
        #print('Space width: {}'.format(self.space_width))
        #print('Line height: {}'.format(self.line_height))

    def get_line_width(self, text):
        """
        Given some `text`, compute how wide the line will be (including all our
        extra between-char spacing, etc)
        """
        total = 0
        first_in_sequence = True
        for letter in text:
            if letter.upper() in self.letters:
                total += self.letters[letter.upper()].width
                if first_in_sequence:
                    first_in_sequence = False
                else:
                    total += self.char_spacing
            else:
                total += self.space_width
                first_in_sequence = True
        return total

    def set_level_mi(self, mod, mi, level='*'):
        """
        Sets the MaterialInterface/MaterialInstance `mi` on all letters in this font,
        for the given `level`.  The wildcard `*` can be used for the level to indicate
        it should be active on all levels.  The active Mod object `mod` will be used
        to add in appropriate MI hotfixes for all letters which have already been
        used in the specified level(s).
        """
        if not self.supports_mi:
            print('WARNING: font {} does not support MaterialInterface/MaterialInstance coloration'.format(self.name))
            return
        for letter in self.letters.values():
            letter.set_level_mi(mod, mi, level)

def rotate_points(points, rot_y, rot_z, rot_x):
    """
    Given a list of `Point` objects (in `points`), rotate them around the origin
    by `rot_y`, `rot_z`, and `rot_x` degrees (specified in degrees, not radians).
    Since BL3 (and presumably UE4) considers positive X to be "forward", the order
    of arguments here evaluates to pitch/yaw/roll pretty nicely.

    This code licensed CC BY-SA 3.0 - https://creativecommons.org/licenses/by-sa/3.0/
    Written by StackOverflow user M Oehm at:
    https://stackoverflow.com/questions/34050929/3d-point-rotation-algorithm/34060479#34060479

    Adapted very slightly for my own purposes here.  It'd probably make sense to
    just add in a numpy dependency and use that; I assume that there's probably
    just a single function we could call, in there, to do all this.

    Not really intended to be used by users; just called from my own `inject_text`
    method.
    """
    rot_y = math.radians(rot_y)
    rot_x = math.radians(rot_x)
    rot_z = math.radians(rot_z)

    cosa = math.cos(rot_z)
    sina = math.sin(rot_z)

    cosb = math.cos(rot_y)
    sinb = math.sin(rot_y)

    cosc = math.cos(rot_x)
    sinc = math.sin(rot_x)

    axx = cosa*cosb
    axy = cosa*sinb*sinc - sina*cosc
    axz = cosa*sinb*cosc + sina*sinc

    ayx = sina*cosb
    ayy = sina*sinb*sinc + cosa*cosc
    ayz = sina*sinb*cosc - cosa*sinc

    azx = -sinb
    azy = cosb*sinc
    azz = cosb*cosc

    for point in points:
        px = point.x
        py = point.y
        pz = point.z

        yield (point,
                axx*px + axy*py + axz*pz,
                ayx*px + ayy*py + ayz*pz,
                azx*px + azy*py + azz*pz)

class TextMesh:
    """
    Main class intended as the user-level API.  Mostly just doing this to avoid
    "from foo import *" type situations, or having to type out tons of stuff in
    the import statement.

    Methods/vars provided here:

        `inject_text` - The main method to add a block of StaticMesh text to
            a map.  See the docstrings for what the args mean

        `Align`/`VAlign` - A couple enums used to pass in alignment info to
            `inject_text`, if you want to use alignments other than center/middle.

        `inject_compass` - Given some world coordinates, inject some floating
            text which serves as a compass to let you know what the axes look like.

    Fonts provided (pass these in to `inject_text`):

        `yellowblocks` - Yellow block text, such as seen on the gateway to Ellie's
            scrapyard when you first head to unlock Outrunners in The Droughts.
            Only has letters!  No numbers or punctuation.  These meshes do have
            collision information, so they are climbable and will stop NPC/Player
            movement.

        `titlecard` - Used for the character title cards which introduce the main
            NPCs and Bosses, based on the Countach font.  These meshes don't have
            any collision info, so anything can just walk right through.  This font
            is missing the letter "Q", but does include some numbers (1, 5, and 8
            are missing from those, though).  Also includes some punctuation:
            & ( ) . , !

        `titlecard2` - Another font used in character title cards, this time based
            on the font Posterama.  Like `titlecard`, these meshes don't have
            collision info.  This font set is quite limited, and only contains the
            following 14 letters: A, B, C, E, G, H, I, L, M, N, R, T, V, Y

        `zero` - An *extremely* limited font which only contains the four letters
            Z, E, R, and O.  Despite the object paths implying that this is used
            in title cards, this is *not* the font used for Zer0's name on his
            card, unless they've been stretched out and altered for display
            purposes (the "O" does *not* have the slash through it, either).
    """

    class Align(enum.Enum):
        """
        Enum to describe horizontal alignments
        """
        CENTER = 1
        LEFT = 2
        RIGHT = 3

        def __str__(self):
            return self.name.capitalize()

    class VAlign(enum.Enum):
        """
        Enum to describe vertical alignments
        """
        MIDDLE = 1
        TOP = 2
        BOTTOM = 3

        def __str__(self):
            return self.name.capitalize()

    # Font 1: Yellow block text
    yellowblocks = Font('Yellow Blocks', '/Game/LevelArt/Environments/_Global/Letters/Meshes/SM_Letter_{}',
            char_spacing=5,
            line_spacing=9,
            line_z_offset=2,
            supports_mi=False,
            letters=[
                # Values here are the y + z values in the StaticMesh objects, under ExtendedBounds.(BoxExtent|Origin)
                Letter('A', 51.408050, 99.852646, -25.698353, 49.926346),
                Letter('B', 52.664890, 99.974990, -22.635244, 49.980854),
                Letter('C', 50.975678, 102.010380, -25.486248, 49.984303),
                Letter('D', 48.666516, 99.960006, -24.333258, 49.980003),
                Letter('E', 36.435250, 103.467292, -16.705948, 51.733660),
                Letter('F', 33.876038, 104.168952, -16.721985, 52.084476),
                Letter('G', 48.960976, 104.936120, -24.480488, 49.964710),
                Letter('H', 55.768120, 107.433930, -26.116295, 51.949196),
                Letter('I', 23.795388, 100.061988, -10.601769, 50.031006),
                Letter('J', 51.924220, 105.250610, -21.417486, 49.102474),
                Letter('K', 57.960086, 100.061988, -22.741297, 50.031000),
                Letter('L', 34.975926, 100.062004, -16.361795, 50.031000),
                Letter('M', 73.586944, 103.600472, -35.025703, 50.032330),
                Letter('N', 52.365070, 99.142944, -24.007483, 49.571472),
                Letter('O', 52.158554, 101.402400, -25.558758, 49.972797),
                Letter('P', 53.232220, 108.187960, -24.848257, 52.326210),
                Letter('Q', 57.132748, 118.236428, -27.558954, 42.869305),
                Letter('R', 52.631380, 103.394776, -24.901249, 50.282400),
                Letter('S', 54.432938, 101.428560, -23.022789, 49.959710),
                Letter('T', 43.706780, 102.300270, -10.469986, 51.150116),
                Letter('U', 53.523464, 103.754616, -24.488916, 49.547970),
                Letter('V', 52.194954, 100.016388, -11.717011, 50.008180),
                Letter('W', 86.998986, 105.262116, -25.749828, 50.992580),
                Letter('X', 51.986862, 104.227776, -23.439910, 48.738735),
                Letter('Y', 53.430030, 103.986366, -8.987263, 51.993183),
                Letter('Z', 43.618886, 102.788440, -19.835200, 49.980003),
                ])

    # Font 2: Title Card Text, based on Countach
    titlecard = Font('Character Title Card', '/Game/Cinematics/Props/Characters_TitleCard/Model/Meshes/Countach/SM_Cinematic_Letter_Countach_{}',
            char_spacing=3,
            line_spacing=11,
            line_z_offset=1,
            supports_mi=True,
            letters=[
                # Values here are the y + z values in the StaticMesh objects, under ExtendedBounds.(BoxExtent|Origin)
                Letter('0', 39.453506, 62.659370, -0.000008, 0.000008),
                Letter('2', 41.084824, 62.659378, -0.000015, 0.000010),
                Letter('3', 39.453506, 62.659370, -0.000008, 0.000006),
                Letter('4', 37.000000, 62.659374, 0.000015, 0.000004),
                Letter('6', 39.453496, 62.659378, 0.000017, 0.000006),
                Letter('7', 39.932800, 62.659370, 0.000000, 0.000002),
                Letter('9', 39.453520, 62.659378, -0.000015, 0.000004),
                # Shifted manually by -5
                Letter('A', 36.193756, 62.659378, -0.000015-5, 0.000006),
                Letter('&', 38.790206, 62.659378, 0.000000, 0.000006, 'Ampersand'),
                Letter('B', 41.084870, 62.659370, 0.000015, 0.000004),
                Letter(')', 25.657814, 71.154694, 0.000000, -0.000004, 'BracketClose'),
                Letter('(', 25.799206, 71.154694, -0.000006, -0.000004, 'BracketOpen'),
                Letter('C', 39.453492, 62.659374, 0.000000, 0.000004),
                Letter(',', 14.103134, 19.923439, -0.000015, 0.000000, 'Comma'),
                Letter('D', 41.084840, 62.659378, 0.000000, 0.000004),
                Letter('E', 38.190644, 62.659370, 0.000015, 0.000002),
                Letter('!', 21.028130, 62.659378, -0.000004, 0.000006, 'ExclamationMark'),
                Letter('F', 38.190644, 62.659370, 0.000015, 0.000002),
                Letter('G', 39.453492, 62.659374, 0.000000, -0.000006),
                Letter('H', 42.651550, 62.659378, 0.000000, -0.000004),
                Letter('I', 26.635926, 62.659370, 0.000000, -0.000006),
                Letter('J', 32.029694, 62.659374, -0.000015, -0.000002),
                Letter('K', 44.903138, 62.659374, 0.000038, -0.000002),
                # Shifted manually by -5
                Letter('L', 28.207824, 62.659378, -0.000031-5, 0.000000),
                Letter('M', 54.460938, 62.659374, -0.000002, -0.000002),
                Letter('N', 42.651550, 62.659374, -0.000002, -0.000002),
                Letter('O', 39.453496, 62.659378, -0.000002, -0.000002),
                # Shifted manually by -3
                Letter('P', 41.084816, 62.659370, 0.000011-3, -0.000004),
                Letter('.', 11.554688, 9.473438, -0.000008, -0.000007, 'Period'),
                # Shifted manually by -3
                Letter('R', 41.084808, 62.659378, 0.000015-3, -0.000004),
                Letter('S', 39.453506, 62.659378, 0.000038, -0.000004),
                Letter('T', 34.026550, 62.659370, -0.000031, -0.000008),
                Letter('U', 40.595276, 62.659374, -0.000031, -0.000006),
                # Shifted manually by +2
                Letter('V', 36.278076, 62.659378, 0.000000+2, -0.000006),
                Letter('W', 53.482788, 62.659374, 0.000000, -0.000008),
                Letter('X', 45.667176, 62.659374, 0.000031, -0.000008),
                # Shifted manually by +4
                Letter('Y', 36.278076, 62.659378, -0.000061+4, -0.000008),
                Letter('Z', 42.607850, 62.659370, 0.000031, -0.000010),
                ])

    # Font 3: Another partial title-card font, based on Posterama
    titlecard2 = Font('Partial Title Card', '/Game/Cinematics/Props/Characters_TitleCard/Model/Meshes/Posterama/SM_Cinematic_Letter_Posterama_{}',
            char_spacing=6,
            line_spacing=11,
            line_z_offset=1,
            supports_mi=True,
            letters=[
                # Values here are the y + z values in the StaticMesh objects, under ExtendedBounds.(BoxExtent|Origin)
                Letter('A', 50.266052, 51.800004, 0.000031, 0.000004),
                Letter('B', 36.351014, 51.000000, -0.000031, 0.000000),
                Letter('C', 45.640840, 52.526300, 0.000015, 0.000002),
                Letter('E', 30.795350, 50.973346, 0.000000, -0.000006),
                Letter('G', 46.011506, 52.600000, -0.000015, -0.000002),
                Letter('H', 40.404694, 50.946502, -0.000015, 0.000006),
                Letter('I', 7.279694, 50.946434, -0.000015, 0.000002),
                Letter('L', 31.201516, 50.973220, -0.000019, 0.000008),
                Letter('M', 48.776550, 51.737374, -0.000031, -0.000006),
                Letter('N', 41.349976, 52.522712, 0.000000, 0.000004),
                Letter('R', 39.425126, 51.000000, -0.000038, 0.000000),
                Letter('T', 39.543762, 50.973214, 0.000000, -0.000006),
                Letter('V', 50.606140, 51.980200, 0.000000, 0.000002),
                Letter('Y', 44.103028, 51.000000, 0.000000, 0.000000),
                ])

    # Font 4: Another partial title-card font
    zero = Font('Zer0', '/Game/Cinematics/Props/Characters_TitleCard/Model/Meshes/SM_Cinematic_Letter_{}',
            char_spacing=3,
            line_spacing=11,
            line_z_offset=2,
            supports_mi=True,
            letters=[
                # Values here are the y + z values in the StaticMesh objects, under ExtendedBounds.(BoxExtent|Origin)
                Letter('E', 17.600000, 65.100000, -8.799998, 32.550000),
                Letter('O', 21.000000, 66.900000, -10.500004, 32.550000),
                Letter('R', 21.500000, 65.366580, -10.750002, 32.683285),
                Letter('Z', 22.634376, 65.100000, -11.317188, 32.550000),
                ])

    # Font X: A complete set of digits
    # Not gonna bother with these, actually:
    #   1) It's just that weird writing style that they made up for Promethea signs
    #   2) They're gigantic
    #   3) They're visually oriented around the Y axis rather than X, so we'd have to
    #      make our processing more generic, and I don't feel like doing that at
    #      the moment
    #   4) They're also untextured, just having a grey checkerboard pattern on 'em
    #digits = Font('Promethea Digits', '/Game/LevelArt/Environments/Promethea/Props/Screens/Model/Meshes/SM_HologramLetters_Letter{}',
    #        char_spacing=3,
    #        line_spacing=11,
    #        line_z_offset=1,
    #        supports_mi=True,
    #        letters=[
    #            # Values here are the y + z values in the StaticMesh objects, under ExtendedBounds.(BoxExtent|Origin)
    #            Letter('0', 360.000000, 1867.844600, 0.000000, 0.000000),
    #            Letter('1', 360.000000, 1873.114800, 0.000000, -0.000061),
    #            Letter('2', 360.000000, 1792.121800, 0.000000, 0.000000),
    #            Letter('3', 360.000000, 1871.175800, 0.000000, 0.000061),
    #            Letter('4', 360.000000, 1900.519200, 0.000000, 0.000000),
    #            Letter('5', 360.000000, 1862.805200, 0.000000, 0.000000),
    #            Letter('6', 360.000000, 1865.222200, 0.000000, 0.000000),
    #            Letter('7', 360.000000, 1869.637400, 0.000000, 0.000000),
    #            Letter('8', 360.000000, 1610.808000, 0.000000, 0.000061),
    #            Letter('9', 360.000000, 1870.806800, 0.000000, 0.000000),
    #            ])

    # Font X: Borderlands Title (used in fake-out cinematic after Pandora Vault)
    # Not keeping this one:
    #   1) As above, they're oriented around the Y axis rather than X
    #   2) The numbers look weird anyway
    #   3) The letters seem to glitch out a bit depending on what angle you're looking at, too.
    #title = Font('Borderlands Title', '/Game/Cinematics/Props/Logo/Model/Meshes/SM_BL_{}',
    #        char_spacing=3,
    #        line_spacing=11,
    #        line_z_offset=2,
    #        supports_mi=False,
    #        letters=[
    #            # Values here are the y + z values in the StaticMesh objects, under ExtendedBounds.(BoxExtent|Origin)
    #            Letter('1', 21.250012, 68.606020, 0.000000, 34.387500),
    #            Letter('2', 21.250012, 69.082276, 0.000001, 34.387510),
    #            Letter('3', 21.250012, 69.405000, 0.000000, 34.387500),
    #            Letter('4', 21.250012, 68.670000, 0.000000, 34.387500),
    #            Letter('A', 21.250008, 39.240000, 0.000001, 19.620000),
    #            Letter('B', 21.250006, 39.240000, 0.000001, 19.620000),
    #            Letter('D', 21.250006, 39.240000, 0.000001, 19.620000),
    #            Letter('E', 21.250006, 39.240000, 0.000001, 19.620000),
    #            Letter('L', 21.250006, 39.240000, 0.000001, 19.620000),
    #            Letter('N', 21.250008, 39.240000, 0.000001, 19.620000),
    #            Letter('O', 21.250006, 39.780002, 0.000001, 19.590002),
    #            Letter('R', 21.250006, 39.240000, 0.000001, 19.620000),
    #            Letter('S', 21.250006, 39.780002, 0.000001, 19.590002),
    #            Letter('X', 21.250008, 39.780002, 0.000001, 19.590002, 'Borderlands'),
    #            Letter('Y', 21.250006, 39.240000, 0.000001, 19.620000, 'D2'),
    #            Letter('Z', 21.250006, 39.240000, 0.000001, 19.620000, 'R2'),
    #            ])

    @staticmethod
    def inject_text(mod,
            level,
            origin,
            text,
            font=yellowblocks,
            rotation=(0,0,0),
            scale=1,
            align=Align.CENTER,
            valign=VAlign.MIDDLE,
            quiet=False,
            ):
        """
        Injects the specified text into a level by creating StaticMesh
        objects for each letter in the text.  Makes use of our new method
        for enabling arbitrary StaticMesh objects in any level, to have the
        widest possible range of alphabet meshes to do so.

        Positional arguments (all required):

        `mod` - The active Mod object in which to add our hotfixes

        `level` - The level to add the text to; should be the full path of the
            `*_P` level reference (don't bother with `*_Dynamic` or `*_Combat`, etc)

        `origin` - An x,y,z tuple describing where to put the text

        `text` - A string or list of strings describing the text to inject into
            the level.

        And then optional arguments:

        `font` - The Font object to use, which will determine which StaticMeshes
            to reference.  Defaults to our `yellowblocks` font.

        `rotation` - a pitch,yaw,roll tuple describing any rotations on the text,
            specified in degrees (not radians).  You may need to do some
            experimentation to figure out which ones are appropriate.  Positive X
            is considered "forward."

        `scale` - An integer describing the scale.  This does not currently
            support scaling axes individually.

        `align` - Horizontal alignment of the text.  This will also impact how
            the text attaches to its `origin`, and how `rotation` affects the
            text: right-aligned text will have its right side at the `origin`
            point, and rotate around that, whereas left-aligned text will
            have its left side at the `origin`.  Centered text will center
            itself on `origin`.  Values are: `Align.CENTER` (the default),
            `Align.LEFT`, and `Align.RIGHT`.

        `valign` - Vertical alignment of the text.  This only really impacts
            how the text attaches to `origin`, and how `rotation` affects the
            text, much like `align`.  Values are: `VAlign.MIDDLE` (the default), 
            `VAlign.TOP`, and `VAlign.BOTTOM`.

        `quiet` - By default,  this method will also inject some comments before
            the hotfixes, to describe the text that's being hotfixed into the
            mod.  Use Set this to `True` to prevent those comments.
        """

        # Support passing in either a string or list of strings
        if type(text) == str:
            text = [text]

        # Report on what we're doing, assuming we've not been told to shut up
        if not quiet:
            last_bit = level.split('/')[-1]
            mod.comment(f'Injecting text in {last_bit}:')
            mod.comment(f'- Font: {font.name}')
            mod.comment(f'- Alignment: {align}, {valign}')
            mod.comment(f'- Origin: {origin}')
            if rotation != (0, 0, 0):
                mod.comment(f'- Rotation: {rotation}')
            if scale != 1:
                mod.comment(f'- Scale: {scale}')
            mod.comment('- Text:')
            for line in text:
                mod.comment(f'>    {line}')
            mod.newline()

        # Calculate the total size (non-transformed) of the text block
        total_height = (len(text)*font.line_height) + ((len(text)-1)*font.line_spacing)
        total_width = max([font.get_line_width(l) for l in text])

        # Figure out where to center our text, based on alignment
        if align == TextMesh.Align.LEFT:
            start_y = 0
        elif align == TextMesh.Align.RIGHT:
            start_y = total_width
        else:
            start_y = total_width/2

        if valign == TextMesh.VAlign.TOP:
            start_z = -(font.line_height*font.line_z_offset)
        elif valign == TextMesh.VAlign.BOTTOM:
            start_z = total_height-(font.line_height*font.line_z_offset)
        else:
            start_z = (total_height/2)-(font.line_height*font.line_z_offset)

        start = (0, start_y, start_z)

        # Loop through and set up our non-transformed initial state
        points = []
        cur_x, cur_y, cur_z = start
        for line in text:
            line_width = font.get_line_width(line)

            # Align text properly
            if align == TextMesh.Align.LEFT:
                offset = 0
            elif align == TextMesh.Align.RIGHT:
                offset = total_width-line_width
            else:
                offset = (total_width-line_width)/2

            cur_y = start[1] - offset
            first_in_sequence = True
            for letter in line:
                if letter.upper() in font.letters:
                    if first_in_sequence:
                        first_in_sequence = False
                    else:
                        cur_y -= font.char_spacing
                    letter_obj = font.letters[letter.upper()]
                    points.append(Point(letter_obj, cur_x, cur_y-letter_obj.w_offset, cur_z+letter_obj.h_offset))
                    cur_y -= letter_obj.width
                else:
                    cur_y -= font.space_width
                    first_in_sequence = True
            cur_z -= font.line_height
            cur_z -= font.line_spacing

        # Finally, rotate, scale, and move to the correct location
        for point, rotated_x, rotated_y, rotated_z in rotate_points(points, *rotation):
            # TODO: it'd be fun to have a `wobble` parameter, or the like, which the
            # user could specify to have the letters randomly tilt around a little bit.
            # Would want to use a normal distribution for the randomness, which'd mean
            # either introducing a numpy dependency or implementing my own.  Don't feel
            # like doing either at the moment, so ehh.
            mod.mesh_hotfix(level,
                    point.letter.mesh_path,
                    location=(
                        (rotated_x*scale)+origin[0],
                        (rotated_y*scale)+origin[1],
                        (rotated_z*scale)+origin[2],
                        ),
                    rotation=(
                        -rotation[0],
                        rotation[1],
                        -rotation[2],
                        ),
                    scale=(scale, scale, scale),
                    ensure=True,
                    )
            point.letter._set_level_used(mod, level.split('/')[-1])

        # If we're not quiet, make sure we end with a newline
        if not quiet:
            mod.newline()

    @staticmethod
    def inject_compass(mod, level, origin, quiet=False):
        """
        Given a point `origin` within `level`, injects a "compass" around that point,
        to easily show the player which direction the axes go in.  Will put the necessary
        hotfixes into the active Mod object `mod`.  The text identifiers will be
        "POS X", "NEG X", "POS Y", "NEG Y", "POS Z", and "NEG Z" (if the `origin` point
        is taken from a character's position while they're on the ground, the "NEG Z"
        label will end up under the ground).  If `quiet` is set to `True`, it will be
        passed along to `inject_text` to prevent descriptive comments from being added
        to the mod file.
        """

        distance = 250
        for text, rel_pos, rotation in [
                ('POS X', (distance, 0, 0), (0, 90, 0)),
                ('NEG X', (-distance, 0, 0), (0, -90, 0)),
                ('POS Y', (0, distance, 0), (0, 180, 0)),
                ('NEG Y', (0, -distance, 0), (0, 0, 0)),
                ('POS Z', (0, 0, distance), (0, 0, -90)),
                ('NEG Z', (0, 0, -distance), (0, 0, 90)),
                ]:

            TextMesh.inject_text(mod, level,
                    (origin[0]+rel_pos[0], origin[1]+rel_pos[1], origin[2]+rel_pos[2]),
                    text,
                    rotation=rotation,
                    font=TextMesh.titlecard,
                    quiet=quiet,
                    )

    @staticmethod
    def inject_point_grid(mod, level, origin, size,
            increment=1000,
            label_rotation=(0,45,0),
            label_scale=1,
            ):
        """
        Injects a "point grid" into the given `mod` file, labelling world positions
        with a small red sphere at the specified intervals in x, y, and z directions.
        Given the limitations of the available character set, the digits 1, 5, and 8
        will be replaced with "i", "s", and "b", respectively.  Also, since we don't
        have a dash symbol, negative numbers will be prefixed with an exclamation
        point instead.

        `level` - The full path of the level in which to inject the grid
        `origin` - The point of origin at which to start the grid, as (x, y, z)
        `size` - A tuple describing the size of the grid, as (size_x, size_y, size_z).
            The sizes *can* be negative to go backwards along an axis instead of
            forwards
        `increment` - How often to draw a point (applies to all axes)
        `label_rotation` - Rotation for label, defaults to (0, 45, 0)
        `label_scale` - Scale for text coordinate labels, defaults to 1
        """

        start_x, max_x = sorted([origin[0], origin[0]+size[0]])
        start_y, max_y = sorted([origin[1], origin[1]+size[1]])
        start_z, max_z = sorted([origin[2], origin[2]+size[2]])

        cur_x = start_x
        while cur_x <= max_x:
            cur_y = start_y
            while cur_y <= max_y:
                cur_z = start_z
                while cur_z <= max_z:
                    mod.mesh_hotfix(level,
                            '/GbxSharedBlockoutAssets/IOMission/IOMissionSphere/Model/Mesh/SM_IO_Mission_Sphere',
                            (cur_x, cur_y, cur_z),
                            ensure=True)
                    coord_text = '({}, {}, {})'.format(int(cur_x), int(cur_y), int(cur_z))
                    coord_text = coord_text.replace('1', 'i').replace('5', 's').replace('8', 'B').replace('-', '!')
                    TextMesh.inject_text(mod,
                            level,
                            (cur_x, cur_y, cur_z),
                            coord_text.split(' '),
                            rotation=label_rotation,
                            scale=label_scale,
                            align=TextMesh.Align.LEFT,
                            font=TextMesh.titlecard,
                            )
                    cur_z += increment
                cur_y += increment
            cur_x += increment

