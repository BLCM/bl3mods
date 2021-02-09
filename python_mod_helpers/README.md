Constructing Borderlands 3 Mods With Code
=========================================

Given the nature of BL3 modding at the moment, it's often easier to write
mods with the assistance of code, rather than trying to write hotfixes by
hand.  There are a couple of Python modules included here which can make
the process a bit easier.  You can find examples of these throughout
Apocalyptech's mod directory, since he wrote these modules and has used
them for nearly all mods in his dir.  Check out any of the `gen_*.py`
scripts in there.

The main one which is used to write out the mod files themselves is in
the `bl3hotfixmod` directory.  The easiest way to do it would be to copy
the `bl3hotfixmod` directory into the same dir that you'll be writing
the mod, but if you look at Apocalyptech's dirs, you'll see that that's
not what's been done there.  Instead, there's this statement near the top
of each of the `gen_*.py` files:

```python
import sys
sys.path.append('../../../python_mod_helpers')
```

The number of `..` entries you'd have to put in depends on how "far away"
your generation script is from this dir.  Alternatively, you could put in
an absolute path there, if you like.

Regardless of whether you're using that, you'd start off your mod like
so:

```python
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('filename_to_save.bl3hotfix',
        'Mod Title',
        'Author Name',
        [
            'Extra description lines to show in the header, if you want.',
            'You can leave this as an empty list.',
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='scaling',
        )
```

Most of that is probably self-explanatory, but I'll go through a couple of points:

If you're generating a mod which is really huge (such as SSpyR's runtime weapon/item
randomizer), you can have the helper generate a compressed version by appending
`.gz` to the filename.  In the example above, for instance, you could specify
`filename_to_save.bl3hotfix.gz` instead.

The `v=foo` line is completely optional, so don't worry about specifying a
version if you don't want (though it's good practice to put it in your file so that
people can compare to versions online, to know if they're out of date).

The `cats='scaling'` line is completely optional as well, and will be used to
categorize your mod into the Borderlands 3 ModCabinet, once that's active.

The `lic=Mod.CC_BY_SA_40` line is there so that an explicit license is attached
to your mod file.  It's not *required*, but I'd personally recommend you
license your mods, just so there's no ambiguity about how you want them used.
There's an open question as to whether or not licenses can even really apply to
this kind of modding, but I personally feel like the answer's a solid
"probably."

There are a bunch of Creative Commons licenses that the library supports, which I'll
list out here:

- `Mod.CC_40` - [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- `Mod.CC_BY_ND_40` - [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/)
- `Mod.CC_BY_SA_40` - [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
- `Mod.CC_NC_40` - [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)
- `Mod.CC_BY_NC_ND_40` - [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- `Mod.CC_BY_NC_SA_40` - [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- `Mod.CC0` - [Creative Commons CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)
- `Mod.PUBLICDOMAIN` - [Public Domain (Creative Commons CC0 1.0 Universal (CC0 1.0))](https://creativecommons.org/publicdomain/zero/1.0/)

You can also specify any arbitrary string, if you want to use a license that's not
included in that list, such as:

    lic="Abandon all hope, ye who try to upload this mod anywhere",

Finally, there's a bunch of media data which can be added to the mod header,
which will be added to the ModCabinet wiki if specified.  Here's a mod
definition which includes all of them:

```python
mod = Mod('filename_to_save.bl3hotfix',
        'Mod Title',
        'Author Name',
        [
            'Extra description lines to show in the header',
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol',
        ss='https://i.imgur.com/ClUttYw.gif',
        videos='https://www.youtube.com/watch?v=JiEu23G4onM',
        nexus='https://www.nexusmods.com/borderlands3/mods/128',
        urls='https://borderlands.com/en-US/news/2020-09-10-borderlands-3-patch-hotfixes-sept-10/',
        )
```

`ss` is for screenshots (which will be inlined on the ModCabinet wiki page), `videos`
is for videos, `nexus` is for an alternate Nexus Mods link for this mod, and `urls`
is any other URL you might want to link to.  `ss`, `videos`, and `urls` can all be
lists rather than just strings, if you wanted to supply more than one.

Anyway, once you've got that mod header set up, you can use a few shortcuts to
build out the mod in your script:

```python
# Puts a newline in the mod (for readability purposes)
mod.newline()

# Puts a comment in the mod (again, for readability)
mod.comment('This is a comment line, will be prefixed by a #')

# Puts a much more obvious comment in the mod, using three hash marks
# with some "blank" comments above and below, to mark out main sections
mod.header('This is a mod header line')

# Same as above, but with a multiline header
mod.header_lines(['Line 1 of a header', 'Line 2 of a header'])

# Creates a regular hotfix
mod.reg_hotfix(hotfix_type, package,
    object_name,
    attribute_name,
    new_value)

# Creates a table-setting hotfix
mod.table_hotfix(hotfix_type, package,
    object_name,
    row_name,
    attribute_name,
    new_value)

# Closes out the mod properly
mod.close()
```

For both `reg_hotfix` and `table_hotfix`, you can include an optional `prev_val`
named argument, if you want to have a hotfix only trigger if the current value
matches.  (ie: a `set_cmp` in BLCMM parlance)

For `hotfix_type` on either `reg_hotfix` or `table_hotfix`, you can use:

- `Mod.PATCH` - Will create a `SparkPatchEntry` hotfix
- `Mod.LEVEL`- Will create a `SparkLevelPatchEntry` hotfix
- `Mod.EARLYLEVEL`- Will create a `SparkEarlyLevelPatchEntry` hotfix
- `Mod.CHAR` - Will create a `SparkCharacterLoadedEntry` hotfix
- `Mod.PACKAGE` - Will create a `SparkStreamedPackageEntry` hotfix
- `Mod.POST` - Will create a `SparkPostLoadedEntry` hotfix

Leave the `package` attribute as an empty string to leave that blank.  Note that
no official GBX hotfix has used `SparkStreamedPackageEntry` or
`SparkPostLoadedEntry` yet, and I've not yet been able to find a way to make use
of them (though I've only tried for `PACKAGE`, which I suspect might be required
to edit vehicle handling information).

The `bl3hotfixmod` package also includes a few convenience classes to help deal
with some commonly-used structures like `BaseValueConstant`-based stanzas and
`ItemPool` entries.  There's also a hash to turn level identifiers into their
English titles.  Look through the source for some more info on those, and grep
for their use in the mod-generation scripts for examples.

### Mesh Additions

The library now also supports [hotfix type 6](https://github.com/BLCM/BLCMods/wiki/Borderlands-3-Hotfixes#hotfix-type-6-spawnmesh),
which is what Gearbox uses to make map alterations using hotfixes.  The most
basic syntax for that is:

```python
mod.mesh_hotfix('/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_P',
        '/Engine/BasicShapes/Cube',
        (65800, -33128, -33000), 
        (0, 0, 0),
        (60, 60, 1))
```

You can alternatively use named parameters instead for `location`, `rotation`,
and `scale`.  If unspecified, they will default to `(0,0,0)` for location and
rotation, or `(1,1,1)` for scale.  You can also specify the `transparent`
argument if the added mesh should be invisible:

```python
mod.mesh_hotfix('/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_P',
        '/Engine/BasicShapes/Cube',
        location=(65800, -33128, -33000),
        scale=(60, 60, 1),
        transparent=True)
```

`mesh_hotfix` also supports an `early` parameter which you can set to `True`
to use a `SparkEarlyLevelPatchEntry` hotfix (instead of the default
`SparkLevelPatchEntry`).  So far it looks like that's probably not necessary,
but it's supported nonetheless.

Data Introspection
==================

This project also includes a `bl3data` project which can be used to simplify
programmatic access to BL3 data, so long as you have it set up properly.  There
are two data sources the package can draw from:

1. Extracted BL3 data, using the technique [described by the BLCMods wiki](https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data#extracting-raw-datafiles).
2. [The BL3 References database](http://apocalyptech.com/games/bl3-refs/) - the
   online version links to a MySQL/MariaDB database dump, which you'll have to
   import into your own MySQL/MariaDB database in order to use.  Alternatively,
   you can use [my refs-creation script](https://github.com/apocalyptech/bl3hotfixmodding/blob/master/dataprocessing/populate_refs_db.py)
   to generate the database from your already-extracted datafiles, though
   grabbing the provided SQL dump will almost certainly be quicker.

Of the two data sources, the first is required.  In order for `bl3data` to 
actually make use of the data, you also need to have a [JohnWickParse](https://github.com/SirWaddles/JohnWickParse)
binary available to do data serialization, and specifically you'll probably
want to use my own [indexed_arrays branch](https://github.com/apocalyptech/JohnWickParse/tree/indexed_arrays),
which includes some versioning information which `bl3data` uses to know if
it should re-serialize data.  You can use the main JWP project instead, but
the data library will re-serialize the data objects every time you run,
rather than intelligently using the previous data if possible.

The refs database is only needed if you want to use the `get_refs_to()` or
`get_refs_from()` methods, to look up references betwen objects.

As for usage, you'll probably find it most useful to just grep through this
project for examples.  The `dataprocessing` dir uses the library nearly everywhere,
and I've started using it for mod generation as well.  In short, though, here's
a couple of ways to use it:

```python
from bl3data.bl3data import BL3Data

data = BL3data()

poollist_name = '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss'

# boss_loot will contain a serialized version of the poollist.
# boss_loot[0] will contain the single export, of type `ItemPoolListData`
boss_loot = data.get_data(poollist_name)

# Loop through the pool list
for pool in boss_loot[0]['ItemPools']:
    print('Found item pool: {}'.format(pool['ItemPool'][1]))

# Get only `ItemPoolListData` exports specifically (in this case, no actual
# difference to just `get_data()`, `[0]` will still contain the single
# export)
boss_loot = data.get_exports(poollist_name, 'ItemPoolListData')

# Get export number 1 specifically (index `[0]`) -- the non-0-based-numbering
# is what's used by UE4 itself.  boss_loot[0] == listdata
listdata = data.get_export_idx(poollist_name, 1)

# Get references to the pool
object_names = data.get_refs_to(poollist_name)

# Get serialized objects which reference the pool
for object_name, data in data.get_refs_to_data(poollist_name):
    print('Found object: {}'.format(object_name))

# Find object names under `/Game/GameData/Loot` which start with `ItemPool_*`
object_names = list(data.find('/Game/GameData/Loot', 'ItemPool_'))
for object_name, data in data.find_data('/Game/GameData/Loot', 'ItemPool_'):
    print('Found object: {}'.format(object_name))

# Find objects by shell-like globs:
object_names = list(data.glob('/Game/GameData/Loot/ItemPools/Guns/*/ItemPool_*'))
for object_name, data in data.glob_data('/Game/GameData/Loot/ItemPools/Guns/*/ItemPool_*'):
    print('Found object: {}'.format(object_name))

# Look up data in a DataTable
cell = data.datatable_lookup(
        '/Game/GameData/Loot/ItemPools/Table_SimpleLootDropChances',
        'Eridium_Bar',
        'Drop_Chances_2_2811F91D40768DBD4FEBB791F8286836')

# Get the exact weight of a BaseValueConstant-based structure.
# Note that this will raise an Exception if it encounters data it doesn't
# understand yet, and right now it only supports very basic objects.  This
# will likely get better over time as I encounter more cases that I need
# to be able to process.
dumpster = data.get_data('/Game/GameData/Loot/ItemPools/ItemPool_Dumpster')[0]
for item in dumpster['BalancedItems']:
    print('Item weight: {}'.format(data.process_bvc_struct(item['Weight'])))
```

License
=======

Both bl3hotfixmod and bl3data are licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](COPYING.txt) for the full text of the license.

