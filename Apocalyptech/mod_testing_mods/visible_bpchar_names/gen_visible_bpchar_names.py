#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2022 Christopher J. Kucera
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
import collections
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod

# (These notes taken from the Wonderlands version of this mod, but should
# apply nearly entirely.)
#
# This turns out to be a harder problem than you might think, at least for
# this mod in particular (since we don't want any BPChars to share a name).
#
# There's a bunch of places where BPChars might get their displayed names from.
# At the top level there's the SpawnOptions objects, which can specify a name
# to override, and I believe that if specified, that'll override everything
# else.  That's *mostly* used to give unique names to otherwise-generic chars.
#
# Then the BPChar itself has a bunch of different attributes.  The "usual"
# one is found in the AIBalanceStateComponent subobject, in the PlayThroughs
# structure.  Then out on the main export, there's a bunch of potential attrs
# to supply alternate names in a variety of circumstances.  Then, finally,
# there's a TargetableComponent sub-object which is often used for NPC-type
# characters.
#
# For everything but the SpawnOptions name override, I don't really know
# which ones take precedence.  I suspect that it goes something like:
#
#    SpawnOptions -> PlayThroughs -> (various BPChar attrs) -> Targetable
#
# ... but that's kind of a guess.
#
# The next wrinkle with renaming these things is that most of those attributes
# work by referencing a GbxUIName object to provide the name, and those objects
# are pretty often shared between various BPChars.  This is most apparent during
# boss battles, which tend to have custom "Adds" which can be balanced
# independently of the main game, but which share the UIName of one of the main-
# game enemies.  (Though that's not the *only* example.)  So we can't just
# rename those UINames specifically, since we don't want those shared between
# BPChars.  I've also not had any luck creating new UIName objects with our
# sub-object creation methods, so that possibility is out.  (It *would* be nice
# to be able to do that -- could tailor the names to where they're found in the
# structure, for instance.  Ah well!)
#
# Fortunately, some of those places where names can be assigned *also* support
# setting names directly on the object, rather than redirecting to a UIName
# object.  Specifically, we can do that in the TargetableComponent sub-object,
# and the PlayThroughs struct in AIBalanceStateComponent.  For all the other
# places (SpawnOptions, random BPChar attrs, etc), we've got to just clear out
# the object reference entirely so that everything falls back to the other
# methods.
#
# So, good enough so far, but one final wrinkle: we've got to be careful about
# setting our names on "base" objects, and might have to worry about ordering
# in general.  As in any other UE game, objects have inheritance, and GBX makes
# use of that to group BPChars together.  For instance, most NPCs end up
# inheriting from BPChar_GenericNPC or BPChar_Generic_DAF, and operations done
# on those "base" objects can end up affecting objects which have been subclassed
# from those main ones.  On an early version of this mod, I'd noticed that
# Paladin Mike was showing up as one of those "generic" NPC BPChars instead of
# his specific one.  It turned out to be basically down to ordering -- the
# BPChar_PaladinMike naming tweak was happening first, but then later down the
# line one of the generic sets was happening, and I'm pretty sure that was
# overriding the earlier BPChar_PaladinMike statements, since the generic ones
# applied to his BPChar as well.
#
# So, I'd added in a couple of safeguards for that.  First, we loop through the
# references database and try to filter out any BPChars which aren't referenced
# by any Map or SpawnOptions object, and mark those as a char not to process.
# This ends up doing 95% of what we want -- all the various `*_Shared` BPChars
# end up getting excluded from that.  We've also got separate block/allow sets
# to tweak those results a bit -- there's a couple false positives, and also
# a couple false negatives.
#
# And finally, the other thing I did was add in dependency tracking between the
# BPChars.  Using the refs database again, the script makes sure that anything
# that appears to depend on another BPChar gets processed *after* that BPChar.
# So we loop through all the BPChars once to grab the data, then associate the
# objects based on parent/child relationships, and then write everything out in
# the "proper" order.
#
# It's entirely possible that even this isn't quite good enough.  I'm not sure
# how "deep" the object inheritance goes -- there might be a case where you've
# got one BPChar spawning in a map alongside a child BPChar, and it's possible
# that those statements might end up doing the wrong thing even with our ordering
# here.  Still, there's probably not much to be done about that, and the
# results seem quite good overall, regardless.  Just beware of potential wrong
# data being reported!

mod = Mod('visible_bpchar_names.bl3hotfix',
        "Visible BPChar Names",
        'Apocalyptech',
        [
            "Updates Character (both NPC+Enemy) visible names to be the actual",
            "BPChar name from the game data.  Useful for modders looking to make",
            "sure they know exactly what BPChar is being used at any given time,",
            "and completely useless for everyone else!",
            "",
            "Note that results shouldn't be trusted 100%, but should be mostly",
            "pretty good.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='resource',
        ss='https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/mod_testing_mods/visible_bpchar_names/screenshot.png',
        )

data = BL3Data()

Statement = collections.namedtuple('Statement', [
    'obj_name',
    'attr',
    'value',
    ])

class BPChar:

    # Just some attribute names on the BPChar which we know about and are handling.
    # If any show up with "UIName" in the attr name which are *not* on this list,
    # the util will let us know about it.
    handled_uiname_attrs = {
            'CustomEvolve_PodUIName',
            'ElementToUINameMap',
            'ElementToUINameMap_PT2',
            'ElementToUINameMapPT2',
            'GoliathUINameList',
            'GoliathUINameList_PT2',
            'Possessed_UIName',
            'Revived_UIName_PT1',
            'Revived_UIName_PT2',
            'UIName',
            'UIName_PT1_LevelUp',
            'UIName_PT2_LevelUp',

            # We actually just ignore this one; only shows up in BPChar_VarkidShared
            # and is... weird.
            'EvolvingToPodUINameMap',
            }

    # We have some rudimentary detection below to try and figure out some BPChars
    # we *shouldn't* process because they're only used as parent classes for the "real"
    # BPChars.  These made it through that check, though, so we're hardcoding them.
    blocklist = {
            '/Alisma/NonPlayerCharacters/Krieg/_Design/Character/BPChar_Ali_Krieg_Shared',
            '/Game/Common/_Design/AI/Character/BPChar_AI',
            '/Game/Enemies/_Shared/_Design/BPChar_Enemy',
            '/Game/NonPlayerCharacters/_Generic/_Shared/_Design/Character/BPChar_GenericNPC',
            '/Game/NonPlayerCharacters/_Shared/_Design/BPChar_NonPlayerCharacter',
            '/Game/NonPlayerCharacters/_Shared/_Design/BPChar_NonPlayerCharacter_Combat',
            '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Character/BPChar_LoaderShared',
            }

    # Likewise, a few which are detected as should-not-process actually *should*.
    allowlist = {
            # Zane Digi-Clone
            '/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_Badass',
            '/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_Base',
            '/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_Normal',
            '/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_SuperBadass',
            '/Game/PlayerCharacters/Operative/DigiClone/_Design/Character/BPChar_DigiClone_UltimateSuperBadass',

            # Dakka Bear
            '/Game/PlayerCharacters/Gunner/_Shared/_Design/IronBear/BPChar_IronBear_DakkaBear',

            # Saurian riders in DLC3
            '/Geranium/Enemies/GerEnforcer/Rider/_Design/Character/BPChar_GerEnforcerRider',
            '/Geranium/Enemies/GerPunk_Female/Rider/_Design/Character/BPChar_GerPunkRider',
            '/Geranium/Enemies/GerSaurian/_Unique/Horsemen1/_Design/Rider/BPChar_GerTinkHorsemen1',
            '/Geranium/Enemies/GerSaurian/_Unique/Horsemen2/_Design/Rider/BPChar_GerEnforcerHorsemen2',
            '/Geranium/Enemies/GerSaurian/_Unique/Horsemen3/_Design/Rider/BPChar_GerPunkHorsemen3',
            '/Geranium/Enemies/GerSaurian/_Unique/Horsemen4/_Design/Rider/BPChar_GerPunkHorsemen4',
            '/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur_Punk',
            '/Geranium/Enemies/GerTink/Rider/_Design/Character/BPChar_GerTinkRider',
            }

    def __init__(self, name, bpchar, data):
        self.name = name
        self.short = self.name.rsplit('/')[-1]
        self.bpchar = bpchar
        self.statements = []
        self._initial_children = set()
        self.children = set()
        self.parents = set()
        self.do_process = False

        # Find dependencies, and make a note of if we're skipping this one.
        for ref in data.get_refs_to(self.name):
            if 'Spawn' in ref or 'Map' in ref:
                self.do_process = True
            if '/bpchar_' in ref.lower():
                self._initial_children.add(ref)
        if self.name in BPChar.blocklist:
            self.do_process = False
        elif self.name in BPChar.allowlist:
            self.do_process = True
        if not self.do_process:
            print(f'Skipping: {self.name}')
            return

        # Loop through and generate mod statements for this BPChar
        for export in self.bpchar:
            if export['export_type'].lower().startswith('bpchar') and export['_jwp_object_name'].startswith('Default__'):
                obj_name = '{}.{}'.format(self.name, export['_jwp_object_name'])

                # Check to see if there's any keys w/ UIName in the name that we haven't handled
                for key in export.keys():
                    if 'UIName' in key and key not in BPChar.handled_uiname_attrs:
                        print('{}: {}'.format(self.name, key))

                # Process TargetableComponent
                if 'TargetableComponent' in export \
                        and 'export' in export['TargetableComponent'] \
                        and export['TargetableComponent']['export'] != 0:
                    tc = self.bpchar[export['TargetableComponent']['export']-1]
                    self.statements.append(Statement(
                        obj_name,
                        'TargetableComponent.Object..TargetUIName',
                        'None'))
                    self.statements.append(Statement(
                        obj_name,
                        'TargetableComponent.Object..TargetName',
                        self.short))
                    # Should we just make everything targetable?  I think this would let
                    # us see the names of those little non-enemy crabs in some of the
                    # levels, for instance.  For now, I'm not doing it.
                    #self.statements.append(Statement(
                    #    obj_name,
                    #    'TargetableComponent.Object..bIsTargetable',
                    #    'True'))

                    # Some attrs we want to clear, if they exist
                    for to_empty in [
                            'ElementToUINameMap',
                            'ElementToUINameMap_PT2',
                            'ElementToUINameMapPT2',
                            'GoliathUINameList',
                            'GoliathUINameList_PT2',
                            ]:
                        if to_empty in export:
                            self.statements.append(Statement(
                                obj_name,
                                to_empty,
                                ''))

                    # Also some attrs to set to None, if they exist
                    # `UIName` only shows up in BPChar_SaurianForager.
                    for to_none in [
                            'CustomEvolve_PodUIName',
                            'Possessed_UIName',
                            'Revived_UIName_PT1',
                            'Revived_UIName_PT2',
                            'UIName',
                            'UIName_PT1_LevelUp',
                            'UIName_PT2_LevelUp',
                            ]:
                        if to_none in export:
                            self.statements.append(Statement(
                                obj_name,
                                to_none,
                                'None'))

                    # Custom processing for possessed Eridians; this doesn't tend
                    # to show up in the on-disk data for a lot of 'em
                    if 'Possessed_UIName' not in export and self.short.lower().startswith('bpchar_guardian'):
                        self.statements.append(Statement(
                            obj_name,
                            'Possessed_UIName',
                            'None'))

            # Process the AIBalanceStateComponent
            elif export['export_type'] == 'AIBalanceStateComponent':
                obj_name = '{}.{}_C:{}'.format(
                        self.name,
                        self.short,
                        export['_jwp_object_name'],
                        )
                if 'PlayThroughs' in export \
                        and type(export['PlayThroughs']) == list \
                        and len(export['PlayThroughs']) > 0:
                    for idx, pt in enumerate(export['PlayThroughs']):
                        self.statements.append(Statement(
                            obj_name,
                            f'PlayThroughs.PlayThroughs[{idx}].bOverrideUIDisplayName',
                            'False'))
                        self.statements.append(Statement(
                            obj_name,
                            f'PlayThroughs.PlayThroughs[{idx}].bOverrideDisplayName',
                            'True'))
                        self.statements.append(Statement(
                            obj_name,
                            f'PlayThroughs.PlayThroughs[{idx}].DisplayName',
                            self.short))

    def __lt__(self, other):
        return self.short.lower() < other.short.lower()

    def __str__(self):
        return self.short

    def finish(self, char_map):
        for child in self._initial_children:
            self.children.add(char_map[child])
            char_map[child].parents.add(self)

    def _write_statements(self, mod):
        for statement in self.statements:
            mod.reg_hotfix(Mod.CHAR, self.short,
                    statement.obj_name,
                    statement.attr,
                    statement.value)

    def write_to_mod(self, mod, written):
        if self in written:
            return
        written.add(self)
        for parent in sorted(self.parents):
            parent.write_to_mod(mod, written)
            #print(f'Processing {parent} before {self}')
        if self.do_process and self.statements:
            mod.comment(self.short)
            self._write_statements(mod)
            mod.newline()

# Load in data
bpchars = {}
skipped = set()
for bpchar_name, bpchar_obj in sorted(data.find_data('/', 'BPChar_')):
    bpchars[bpchar_name] = BPChar(bpchar_name, bpchar_obj, data)
for bpchar in bpchars.values():
    bpchar.finish(bpchars)
    if not bpchar.do_process:
        skipped.add(bpchar)

# Write out bpchars
written = set()
mod.header('BPChars')
for bpchar in sorted(bpchars.values()):
    bpchar.write_to_mod(mod, written)

# Since SpawnOptions only has UINameOverride and not NameOverride, we've gotta just
# clear all these out.
mod.header('Clear SpawnOptions Overrides')
mod.comment('This is annoyingly "heavy" since I don\'t have a good way to know when')
mod.comment('exactly all these SpawnOptions objects get loaded.  I\'d make do with just')
mod.comment('a MatchAll on LEVEL but I know of at least one SpawnOption object which')
mod.comment('gets loaded dynamically well through the level, so I\'m doing both...')
mod.newline()

so_objects = list(data.find_data('/', 'SpawnOption'))
so_objects.extend(list(data.find_data('/', 'Spawn_')))
for so_name, so in sorted(so_objects):
    so_short = so_name.rsplit('/', 1)[-1]
    for export in so:
        if export['export_type'].endswith('OakAI'):
            if 'AIActorClass' in export and 'asset_path_name' in export['AIActorClass']:
                if 'UINameOverride' in export and 'export' not in export['UINameOverride']:
                    obj_name = '{}.{}:{}'.format(
                            so_name,
                            so_short,
                            export['_jwp_object_name'],
                            )
                    for hf_type in [Mod.CHAR, Mod.LEVEL]:
                        mod.reg_hotfix(hf_type, 'MatchAll',
                                obj_name,
                                'UINameOverride',
                                'None')

mod.newline()

# Report on skipped BPChars at the end
mod.header('Skipped BPChars')
for skip in sorted(skipped, key=lambda s: s.name.lower()):
    mod.comment(skip.name)
mod.newline()

mod.close()
