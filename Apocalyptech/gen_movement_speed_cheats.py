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

# We're actually generating two separate mods here, in the absence of
# something like BLCMM
for (label, suffix, multiplier) in [
        ('Reasonable Improvements', 'reasonable', 1.5),
        ('Extreme Improvements', 'extreme', 2.25),
        ]:

    # Mod header
    mod_filename = 'movement_speed_cheats_{}.txt'.format(suffix)
    mod = Mod(mod_filename,
            'Movement Speed Cheats - {}'.format(label),
            'Apocalyptech',
            [
                "Increases character (and pet, and Iron Bear) movement speed by {}x,".format(multiplier),
                "",
                "Not yet sure how this interacts with stuff like speed while crouching,",
                "FFYL, climbing ladders, etc.",
            ],
            lic=Mod.CC_BY_SA_40,
            )

    # Player Chars
    mod.header('Player Characters')
    for (label, obj_name) in [
            ('Beastmaster', '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPChar_Beastmaster.Default__BPChar_Beastmaster_C'),
            ('Gunner', '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/BPChar_Gunner.Default__BPChar_Gunner_C'),
            ('Operative', '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/BPChar_Operative.Default__BPChar_Operative_C'),
            ('Siren', '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/BPChar_Siren.Default__BPChar_Siren_C'),
            ]:

        mod.comment(label)
        do_walk(mod, obj_name, 470, 470, multiplier)
        do_sprint(mod, obj_name, 720, 720, multiplier)
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
            ]:

        mod.comment(label)
        do_walk(mod, obj_name, walk_val, walk_base, multiplier)
        do_sprint(mod, obj_name, sprint_val, sprint_base, multiplier)
        mod.newline()

    mod.close()
    print('Generated {}'.format(mod_filename))
