#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2022-2023 Christopher J. Kucera
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
import collections
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

# Args, why not.
parser = argparse.ArgumentParser(
        description="Generation script for the BL3 Force Enemy Spawns mod",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="""
            Note that this generation script makes full use of the BL3Data library,
            requiring access to both serialized data *and* the references database.
            See the BL3Data docs up in the python_mod_helpers directory for more
            information on all that.
            """,
        )
parser.add_argument('-f', '--force',
        type=str,
        dest='initial_search',
        default='/Game/Enemies/Tink/Anointed/_Design/Character/BPChar_TinkAnointed',
        #default='/Game/Enemies/Skag/Badass/_Design/Character/BPChar_SkagBadass',
        help="The BPChar or SpawnOption to force to spawn",
        )
parser.add_argument('-n', '--num-spawns',
        type=int,
        default=5,
        help="Number of spawns to allow from each SpawnOption",
        )
parser.add_argument('-m', '--max-recursion',
        type=int,
        default=20,
        help="""Maximum levels of recursion when processing SpawnOptions (the
            default should be far more than enough for all cases)""",
        )
args = parser.parse_args()
print(f'Generating mod for: {args.initial_search}')

# Start mod generation
initial_short = args.initial_search.rsplit('/', 1)[-1]
mod = Mod('force_enemy_spawns.bl3hotfix',
        f"Force Enemy Spawns: {initial_short}",
        'Apocalyptech',
        [
            "Resource mod which attemps to alter SpawnOptions objects so that wherever",
            "the configured character *can* spawn, they *will* spawn 100% of the time.",
            "",
            "Does not attempt to touch SpawnOptions objects which don't involve the",
            "specified char, since BL3/WL spawning points are often a bit touchy about",
            "which chars are allowed to spawn from them.",
            "",
            "The version stored on github is hardcoded to Anointed Tinks.  To make it",
            "operate on some other enemy, you'll have to edit the generation script",
            "and re-generate it.",
            "",
            "This mod was generated to force the following, where possible:",
            "",
            f"    {args.initial_search}",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='resource',
        )

data = BL3Data()

def get_indexes_from_spawn(data, spawn_name, obj_to_match):
    """
    Looks through the SpawnOptions object `spawn_name` looking for Options
    which spawn `obj_to_match`, which should be either a BPChar or SpawnOptions
    name.  It will return a 2-element tuple: the first element will be a list
    of Options indexes which matched on `obj_to_match`, and the second will
    be a list of indexes which did *not* match.

    Kind of a weird implementation, I know, but there it is.
    """
    our_indexes = []
    other_indexes = []
    so = data.get_data(spawn_name)
    for export in so:
        if export['export_type'] == 'SpawnOptionData':
            for idx, factory_ref in enumerate(export['Options']):
                if 'export' in factory_ref['Factory'] and factory_ref['Factory']['export'] != 0:
                    factory = so[factory_ref['Factory']['export']-1]
                    if factory['export_type'] == 'SpawnFactory_OakAI':
                        factory_actor = factory['AIActorClass']['asset_path_name'].rsplit('.', 1)[0]
                        if factory_actor == obj_to_match:
                            our_indexes.append(idx)
                        else:
                            other_indexes.append(idx)
                    elif factory['export_type'] == 'SpawnFactory_Container':
                        factory_options = factory['Options'][1]
                        if factory_options == obj_to_match:
                            our_indexes.append(idx)
                        else:
                            other_indexes.append(idx)
                    else:
                        raise RuntimeError('Unknown factory type "{}" in {}'.format(
                            factory['export_type'],
                            spawn_name,
                            ))
    return our_indexes, other_indexes

def ensure_spawn(mod, args, spawn_obj, our_indexes, other_indexes):
    """
    Given a `mod` object, CLI args `args`, a SpawnOptions object name
    `spawn_obj`, and two lists of indexes (`our_indexes` which is the
    list of indexes we want to ensure spawning, and `other_indexes`
    being the ones we want to suppress), write out the necessary
    hotfixes to make that happen.
    """
    zero = BVCF(bvc=0)
    mod.comment(spawn_obj)
    for to_set, indexes in [
            (1, our_indexes),
            (0, other_indexes),
            ]:
        for index in indexes:
            # I *think* we need to set ValueMode=Value in some situations, namely
            # when options redirect to other spawnoptions.  For instance, index 8
            # in SpawnOptions_CoVMix_Mansion1 redirects to SpawnOptions_CoVMix_MansionBadasses,
            # and the the ValueMode the weight on that one is AttributeInitializationData.
            # We're clearing out the AI in here, so I think that results in that
            # option never getting rolled.  I'm sure that can happen in other
            # circumstances as well.  The same attrs exist for the Alive struct, too,
            # but I assume we can leave that one alone
            mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                    spawn_obj,
                    f'Options.Options[{index}].WeightParam',
                    f"""
                    (
                        ValueType=Float,
                        DisabledValueModes=110,
                        ValueMode=Value,
                        Range=(Value={to_set},Variance=0),
                        AttributeInitializer=None,
                        AttributeData=None,
                        AttributeInitializationData={zero}
                    )
                    """,
                    )
            mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                    spawn_obj,
                    f'Options.Options[{index}].AliveLimitParam.Range',
                    f'(Value={args.num_spawns},Variance=0)',
                    )
            mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                    spawn_obj,
                    f'Options.Options[{index}].AliveLimit',
                    args.num_spawns,
                    )
            
            # Some things which didn't work
            if False:
                mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                        spawn_obj,
                        f'Options.Options[{index}].Probability',
                        '{}%'.format(to_set*100),
                        )
            if False:
                mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                        spawn_obj,
                        f'Options.Options[{index}].AliveLimitType',
                        'Spawner',
                        )
    mod.newline()

def process_refs(data, mod, args, seen_objects, search_name, level=0):
    """
    Main routine to try and enforce spawning throughojut the game.  Requires
    a data object `data`, a mod object `mod`, and CLI args `args`.  `seen_objects`
    is a set which keeps track of which SpawnOptions objects we've already
    processed, so we can avoid infinite loops, and `search_name` is the name
    we're trying to lock spawns to.  `level` is used to keep track of the recursion
    level, so we can fail out if need be, before Python does it for us.  (In
    practice, we'll basically never run into that since the game itself would be
    crashing if any circular dependencies existed.)

    This makes use of the references database to figure out what's pointing at
    `search_name`, and of course the serialized data to poke into the SpawnOptions
    to know what to do.
    """
    if level > args.max_recursion:
        # Prevent too much recursion; in practice we should never hit this with our
        # default of 20
        return
    if search_name in seen_objects:
        # Prevent infinite loops; in practice we should never hit this, 'cause the
        # game would be crashing if the data were set up that way.
        return
    seen_objects.add(search_name)
    for obj_ref in data.get_refs_to(search_name):
        if 'Spawn' in obj_ref:
            our_indexes, other_indexes = get_indexes_from_spawn(data, obj_ref, search_name)
            if len(other_indexes) == 0:
                # Sometimes we get a bpchar which *only* has a single ref in it, and it's meant
                # to be called from other spawnoptions.  Recurse in there!
                process_refs(data, mod, args, seen_objects, obj_ref, level)
            else:
                ensure_spawn(mod, args, obj_ref, our_indexes, other_indexes)
                process_refs(data, mod, args, seen_objects, obj_ref, level+1)

# Do the work!
seen_objects = set()
process_refs(data, mod, args, seen_objects, args.initial_search)

mod.close()
