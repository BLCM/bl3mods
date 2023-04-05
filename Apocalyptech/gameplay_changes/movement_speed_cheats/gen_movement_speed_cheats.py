#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2021 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod

# See the current values:
#
# getall oakcharactermovementcomponent maxwalkspeed
# getall oakcharactermovementcomponent maxsprintspeed
#
# Player pawn itself, though we don't touch these (the 'max' values there seem to be enough)
#
# getall bpchar_player_c walkspeed_normal
# getall bpchar_player_c walkspeed_zerog

def do_move(mod, obj_name, var_name, val, base, multiplier):
    """
    I am about 95% certain that setting `Value` here doesn't do anything; that seems to be
    dynamically set by the engine and basically relates to the speed at which the BPChar
    is currently walking (or has most recently walked).  Doesn't seem to *always* correlate
    with what's going on in the game, but it definitely gets reset.  So `BaseValue` is
    almost certainly the only one which actually matters here.
    """
    new_val = int(val*multiplier)
    new_base = int(base*multiplier)
    mod.reg_hotfix(Mod.PATCH, '',
            '{}:CharMoveComp'.format(obj_name),
            var_name,
            '(Value={},BaseValue={})'.format(new_val, new_base))

def do_walk(mod, obj_name, val, base, multiplier):
    do_move(mod, obj_name, 'MaxWalkSpeed', val, base, multiplier)

def do_sprint(mod, obj_name, val, base, multiplier):
    do_move(mod, obj_name, 'MaxSprintSpeed', val, base, multiplier)

def do_crouch(mod, obj_name, val, base, multiplier):
    do_move(mod, obj_name, 'MaxWalkSpeedCrouched', val, base, multiplier)

def do_ladder_up(mod, obj_name, val, base, multiplier):
    do_move(mod, obj_name, 'MaxLadderAscendSpeed', val, base, multiplier)

def do_ladder_down(mod, obj_name, val, base, multiplier):
    do_move(mod, obj_name, 'MaxLadderDescendSpeed', val, base, multiplier)

def do_ffyl(mod, obj_name, val, base, multiplier):
    do_move(mod, obj_name, 'MaxInjuredSprintSpeed', val, base, multiplier)
    do_move(mod, obj_name, 'MaxWalkSpeedInjured', val, base, multiplier)

# We're actually generating two separate mods here, in the absence of
# something like BLCMM
for (label, suffix, multiplier, desc_override) in [
        ('Normal', 'normal', 1, [
            "Sets character (and pet, and Iron Bear) movement speed back to the defaults.",
            "Of use if you want to revert your movement speed after using one of the other",
            "movement speed mods, without having to quit the entire game to do so.",
            ]),
        ('Reasonable Improvements', 'reasonable', 1.5, None),
        ('Extreme Improvements', 'extreme', 2.25, None),
        ]:

    # Fill in our description
    if desc_override is None:
        mod_desc = [
                "Increases character (and pet, and Iron Bear) movement speed by {}x.".format(multiplier),
                "Includes improvements to FFYL, crouching, and ladder climbing.",
            ]
    else:
        mod_desc = desc_override

    # Mod header
    mod_filename = 'movement_speed_cheats_{}.bl3hotfix'.format(suffix)
    mod = Mod(mod_filename,
            'Movement Speed Cheats - {}'.format(label),
            'Apocalyptech',
            mod_desc,
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.1.0',
            cats='cheat',
            )

    # Player Chars
    mod.header('Player Characters')
    for (label, dirname, obj_name) in [
            ('Beastmaster', 'Beastmaster', '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPChar_Beastmaster.Default__BPChar_Beastmaster_C'),
            ('Gunner', 'Gunner', '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/BPChar_Gunner.Default__BPChar_Gunner_C'),
            ('Operative', 'Operative', '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/BPChar_Operative.Default__BPChar_Operative_C'),
            ('Siren', 'SirenBrawler', '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/BPChar_Siren.Default__BPChar_Siren_C'),
            ]:

        mod.comment(label)
        do_walk(mod, obj_name, 470, 470, multiplier)
        do_sprint(mod, obj_name, 720, 720, multiplier)
        do_crouch(mod, obj_name, 275, 275, multiplier)
        do_ffyl(mod, obj_name, 200, 200, multiplier)
        do_ladder_up(mod, obj_name, 200, 200, multiplier)
        do_ladder_down(mod, obj_name, 160, 160, multiplier)
        for anim, default_rate in [
                ('AS_Ladder_Enter', 1),
                ('AS_Ladder_Enter_Top', 1),
                ('AS_Ladder_Exit', 1),
                ('AS_Ladder_Exit_Top', 1),
                ]:
            mod.reg_hotfix(Mod.PATCH, '',
                    '/Game/PlayerCharacters/{}/_Shared/Animation/Generic/Ladders/3rd/{}'.format(dirname, anim),
                    'RateScale',
                    '{:g}'.format(default_rate*multiplier))
        mod.newline()

    # Ladder Animations
    mod.header('Generic Ladder Animations')
    for anim, default_rate in [
            ('AS_Ladder_Descend_Exit', 1),
            ('AS_Ladder_Enter', 1),
            ('AS_Ladder_Enter_Top', 1),
            ('AS_Ladder_Exit', 0.7),
            ('AS_Ladder_Exit_Top', 1),
            ]:
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/PlayerCharacters/_Shared/Animation/Generic/Ladders/1st/{}'.format(anim),
                'RateScale',
                '{:g}'.format(default_rate*multiplier))
    mod.newline()

    # Iron Bear
    mod.header('Iron Bear')
    mod.comment('Iron Bear')
    obj_name = '/Game/PlayerCharacters/Gunner/_Shared/_Design/IronBear/BPChar_IronBear.Default__BPChar_IronBear_C'
    do_walk(mod, obj_name, 456, 456, multiplier)
    do_sprint(mod, obj_name, 650, 650, multiplier)
    mod.newline()

    # Pets!
    mod.header('Pets')
    for (label, obj_name, walk_val, walk_base, sprint_val, sprint_base) in [
            ('Jabber - Basic',
                '/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/Character/BPChar_PetMonkey.Default__BPChar_PetMonkey_C',
                100, 500, 750, 750),
            ('Jabber - Beefcake',
                '/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/Character/BPChar_PetMonkey_Evo1_Beefcake.Default__BPChar_PetMonkey_Evo1_Beefcake_C',
                160, 800, 750, 750),
            ('Jabber - Gunslinger',
                '/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/Character/BPChar_PetMonkey_Evo2_Gunslinger.Default__BPChar_PetMonkey_Evo2_Gunslinger_C',
                100, 500, 750, 750),
            ('Spiderant - Basic',
                '/Game/PlayerCharacters/Beastmaster/Pet/Spiderant/_Design/Character/BPChar_PetSpiderant.Default__BPChar_PetSpiderant_C',
                140, 700, 900, 900),
            ('Spiderant - Fire',
                '/Game/PlayerCharacters/Beastmaster/Pet/Spiderant/_Design/Character/BPChar_PetSpiderant_Evo1_Fire.Default__BPChar_PetSpiderant_Evo1_Fire_C',
                140, 700, 900, 900),
            ('Spiderant - King',
                '/Game/PlayerCharacters/Beastmaster/Pet/Spiderant/_Design/Character/BPChar_PetSpiderant_Evo2_King.Default__BPChar_PetSpiderant_Evo2_King_C',
                140, 700, 900, 900),
            ('Skag - Basic',
                '/Game/PlayerCharacters/Beastmaster/Pet/Skag/_Design/Character/BPChar_PetSkag.Default__BPChar_PetSkag_C',
                168, 840, 900, 900),
            ('Skag - Horned',
                '/Game/PlayerCharacters/Beastmaster/Pet/Skag/_Design/Character/BPChar_PetSkag_Evo1_Horned.Default__BPChar_PetSkag_Evo1_Horned_C',
                # really weird walk val on this one
                67.2, 840, 900, 900),
            ('Skag - Eridian',
                '/Game/PlayerCharacters/Beastmaster/Pet/Skag/_Design/Character/BPChar_PetSkag_Evo2_Eridian.Default__BPChar_PetSkag_Evo2_Eridian_C',
                168, 840, 900, 900),
            ('Loader - BUL',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Pet/Loader/_Design/Character/BPChar_PetLoader_BUL.Default__BPChar_PetLoader_BUL_C',
                275, 600, 900, 900),
            ('Loader - ION',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Pet/Loader/_Design/Character/BPChar_PetLoader_ION.Default__BPChar_PetLoader_ION_C',
                240, 600, 900, 900),
            ('Loader - WAR',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Pet/Loader/_Design/Character/BPChar_PetLoader_WAR.Default__BPChar_PetLoader_WAR_C',
                300, 600, 900, 900),
            ]:

        mod.comment(label)
        do_walk(mod, obj_name, walk_val, walk_base, multiplier)
        do_sprint(mod, obj_name, sprint_val, sprint_base, multiplier)
        mod.newline()

    mod.close()
