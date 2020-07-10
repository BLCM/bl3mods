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

# Player characters (and related)
pcs = {
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPChar_Beastmaster',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPChar_StandIn_Beastmaster',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPChar_StandIn_Beastmaster_SkillScreen',
        '/Game/PlayerCharacters/Beastmaster/Pet/_Shared/_Design/Character/BPChar_Pet',
        '/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/Character/BPChar_PetMonkey',
        '/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/Character/BPChar_PetMonkey_Evo1_Beefcake',
        '/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/Character/BPChar_PetMonkey_Evo2_Gunslinger',
        '/Game/PlayerCharacters/Beastmaster/Pet/Skag/_Design/Character/BPChar_PetSkag',
        '/Game/PlayerCharacters/Beastmaster/Pet/Skag/_Design/Character/BPChar_PetSkag_Evo1_Horned',
        '/Game/PlayerCharacters/Beastmaster/Pet/Skag/_Design/Character/BPChar_PetSkag_Evo2_Eridian',
        '/Game/PlayerCharacters/Beastmaster/Pet/Spiderant/_Design/Character/BPChar_PetSpiderant',
        '/Game/PlayerCharacters/Beastmaster/Pet/Spiderant/_Design/Character/BPChar_PetSpiderant_Evo1_Fire',
        '/Game/PlayerCharacters/Beastmaster/Pet/Spiderant/_Design/Character/BPChar_PetSpiderant_Evo2_King',
        '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/BPChar_Gunner',
        '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/BPChar_StandIn_Gunner',
        '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/BPChar_StandIn_Gunner_SkillScreen',
        '/Game/PlayerCharacters/Gunner/_Shared/_Design/IronBear/BPChar_IronBear',
        '/Game/PlayerCharacters/Gunner/_Shared/_Design/IronBear/BPChar_IronBear_DakkaBear',
        '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/BPChar_Operative',
        '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/BPChar_StandIn_Operative',
        '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/BPChar_StandIn_Operative_SkillScreen',
        '/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_Badass',
        '/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_Base',
        '/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_Normal',
        '/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_SuperBadass',
        '/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_UltimateSuperBadass',
        '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/BPChar_Siren',
        '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/BPChar_StandIn_Siren',
        '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/BPChar_StandIn_Siren_SkillScreen',
        }

# Chars which have scaling limits (tuple: min, max)
scale_limits = {
        # A 2x+ Wendigo will fall through the floor and become unkillable, so we won't let
        # it grow.  (Presumably a *smaller* Wendigo would be okay though.)
        '/Hibiscus/Enemies/Wendigo/Design/Character/BPChar_Wendigo': (None, 1),
        }

# Generate sizes with: find . -name "BPChar_*.uasset" | cut -d. -f2 | sort -i
bpchars = []
with open('gen_sizemod_data.txt') as df:
    for line in df:
        obj_ref = line.strip()
        if obj_ref not in pcs:
            bpchars.append(obj_ref)

# Now generate
for label, scale in [
        ('Tiny', 0.4),
        ('Smol', 0.7),
        ('Big', 2.0),
        ('Huge', 3.0),
        ('Giant', 5.0),
        ]:

    filename_label = '{:0.1f}_{}.txt'.format(scale, label.lower())

    mod = Mod('sizemod_npc_{}'.format(filename_label),
            'Sizemod: NPC {}-lands ({}x)'.format(label, scale),
            'Apocalyptech',
            [
                "Scales NPC (enemies and otherwise) to {}x.  Keep in mind that this may".format(scale),
                "cause all manner of problems, and has not been thoroughly tested in any",
                "way.  Some characters (such as ones operating consoles in Sanctuary) will",
                "remain unscaled.  Let me know if anything really game-breaking happens!",
            ],
            lic=Mod.CC_BY_SA_40,
            )
    for bpchar in bpchars:

        # Check our scaling for min/max on a per-char basis
        this_scale = scale
        if bpchar in scale_limits:
            scale_min, scale_max = scale_limits[bpchar]
            if scale_max is not None and scale > scale_max:
                this_scale = scale_max
            elif scale_min is not None and scale < scale_min:
                this_scale = scale_min

        # Now do the hotfix
        last_bit = bpchar.split('/')[-1]
        mod.reg_hotfix(Mod.CHAR, last_bit,
                '{}.Default__{}_C:CharacterMesh0'.format(bpchar, last_bit),
                'RelativeScale3D',
                f'(X={this_scale},Y={this_scale},Z={this_scale})')
    mod.close()

    # Doesn't seem to work, will play around with it later.
    #mod = Mod('sizemod_player_{}'.format(filename_label),
    #        'Sizemod: Player {}-lands ({}x)'.format(label, scale),
    #        'Apocalyptech',
    #        [
    #        ],
    #        lic=Mod.CC_BY_SA_40,
    #        )
    #for bpchar in pcs:
    #    last_bit = bpchar.split('/')[-1]
    #    mod.reg_hotfix(Mod.CHAR, last_bit,
    #            '{}.Default__{}_C:CharacterMesh0'.format(bpchar, last_bit),
    #            'RelativeScale3D',
    #            f'(X={scale},Y={scale},Z={scale})')
    #mod.close()

