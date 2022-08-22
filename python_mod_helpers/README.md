Constructing Borderlands 3 Mods With Code
=========================================

* [Overview](#overview)
  * [Bytecode Alterations](#bytecode-alterations)
  * [Mesh Additions](#mesh-additions)
  * [StaticMesh Text Blocks](#staticmesh-text-blocks)
  * [Blueprint Streaming](#blueprint-streaming)
* [Data Introspection](#data-introspection)
* [Hotfix Generator](#hotfix-generator)
* [License](#license)

Overview
--------

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
        contact='https://apocalyptech.com/contact.php',
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

The `contact=foo` line is completely optional, and is just used if you want to
give users a way to contact you about your mods.  You can actually use any of
three variables here: `contact`, `contact_email`, and/or `contact_discord`.  Keep
in mind that this information will be public, so only put info in here if you're
okay with that.

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
        homepage='https://your-cool-mod.biz/',
        ss='https://i.imgur.com/ClUttYw.gif',
        videos='https://www.youtube.com/watch?v=JiEu23G4onM',
        nexus='https://www.nexusmods.com/borderlands3/mods/128',
        urls='https://borderlands.com/en-US/news/2020-09-10-borderlands-3-patch-hotfixes-sept-10/',
        )
```

`homepage` is there in case your mod has an official homepage.  `ss` is for
screenshots (which will be inlined on the ModCabinet wiki page), `videos`
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

### Bytecode Alterations

The library supports [hotfix type 7](https://github.com/BLCM/BLCMods/wiki/Borderlands-3-Hotfixes#hotfix-type-7-blueprint-bytecode),
which is used to alter the Blueprint Bytecode which provides some of the fancier
behaviors in objects.  This isn't as straightforward as some of the other modding
we do, and requires some different tools to use effectively.  The tools we usually
use to look at Borderlands data (JohnWickParse and FModel) don't output anything
about bytecode.  The project that we're using to look into the bytecode is
[UAssetGUI/UAssetAPI](https://github.com/atenfyr/UAssetGUI).  When serializing
the data, it will give you "indexes" in the JSON which correspond to the values
you need to use in these types of hotfixes.

If UAssetGUI isn't showing you the exact index that you need (or if you wanted to
doublecheck the indexes yourself), [UAssetAPI's `KismetSerializer.cs` source](https://github.com/atenfyr/UAssetAPI/blob/master/UAssetAPI/Kismet/KismetSerializer.cs)
is what you'd want to look at -- specifically the `SerializeExpression` method.
Keep track of changes to the `index` variable (keeping in mind that recursive
calls to `SerializeExpression` may do their own `index` increments) to keep track
of the "current" index as you walk through the serialization.

The syntax for specifying these types hotfixes is pretty straightforward:

```python
mod.bytecode_hotfix(Mod.PATCH, '',
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/AntGreatBow/Ability_AntGreatBow'
        'ExecuteUbergraph_Ability_AntGreatBow',
        194,
        0,
        2)
```

The first few arguments should be familiar by now -- the fourth is the name
of the export containing the function you're trying to alter.  The fifth argument
is the index that you're altering, as found via UAssetGUI (or other methods, if
they exist).  Then the final two arguments are the current/previous/"from" value,
and the new/"to" value.  Unlike other hotfix types, the previous value *must* be
specified, so this hotfix type cannot do "blind" changes like other hotfix types
can.

One unique behavior in `bytecode_hotfix` is how it handles the object name.  If
given a "bare" name, like above (without a `.SecondPart` in the object name),
rather than converting it to just the usual "full" form, it'll additionally add
a `_C` at the end of the name.  So the code above would generate a hotfix whose
full object name comes out as:

    /Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/AntGreatBow/Ability_AntGreatBow.Ability_AntGreatBow_C

It seems that doing so is pretty likely to be the correct behavior in all cases,
so feel free to give that a try.  As with other hotfix types, if you pass in
an object name which already contains a `.`, it'll leave it alone, so if there are
cases where `_C` isn't an appropriate suffix, you can specify the correct values
yourself.

This hotfix type supports specifying multiple indexes, when making the same change
more than once within a single function.  This may be required in some cases --
the bytecode hotfix processing seems to be a little picky sometimes.  To do this,
you can pass a list in for the index, rather than a single number:

```python
mod.bytecode_hotfix(Mod.PATCH, '',
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/AntGreatBow/Ability_AntGreatBow'
        'ExecuteUbergraph_Ability_AntGreatBow',
        [194, 318],
        0,
        2)
```

### Mesh Additions

The library supports [hotfix type 6](https://github.com/BLCM/BLCMods/wiki/Borderlands-3-Hotfixes#hotfix-type-6-spawnmesh),
which is what Gearbox uses to add in "static" map elements.  The most
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

By default, you can only make use of StaticMeshes which are already available
in the level, while using this hotfix type.  One way around this is to use
*another* hotfix first, to create a reference to a new StaticMesh.  Thanks to
the dynamic object-loading capabilities of UE4, this will let you use the
new mesh in one of these hotfixes.  The `mesh_hotfix` method supports
doing this transparently behind-the-scenes, so long as you add the parameter
`ensure=True`, such as this statement which adds the DLC1 Neon Peach mesh
into The Droughts (near the Highway fast travel):

```python
mod.mesh_hotfix('/Game/Maps/Zone_0/Prologue/Prologue_P',
        '/Dandelion/LevelArt/Manufacturers/Hyperion/Props/Casino/NeonSigns/Model/Meshes/SM_Hyp_Neon_Peach',
        location=(45949, 21627, -3720),
        ensure=True,
        )
```

When using `ensure=True`, the library will use the Eridian Resonator object to
swap in the requested meshes, and then swap it back to the "stock" Resonator
object when the mod is closed.  By default, the library will add in comments
along with these mesh-swapping hotfixes, so it's obvious where it's put things
in automatically.  If you prefer not to see these comments, pass in
`quiet_meshes=True` to your initial `Mod()` object creation.

### StaticMesh Text Blocks

The game data includes two sets of StaticMesh letters, which can be used as
"fonts" to write out text blocks in the game world.  This would be incredibly
cumbersome to do by hand, even with the `mesh_hotfix` method, so a separate
library is available to make it much easier.  See [README-textmesh.md](README-textmesh.md)
for documentation on using this library.

![StaticMesh Text Example](screenshots/textmesh_example.jpg)

### Blueprint Streaming

The library supports [hotfix type 11](https://github.com/BLCM/BLCMods/wiki/Borderlands-3-Hotfixes#hotfix-type-11-stream-blueprint),
which can be used to add in interactive elements to maps, such as vending
machines, quick change stations, and more.  (This is in contrast to mesh/type-6
hotfixes which can only add in "static" elements.)  This has a ton of caveats,
so definitely read through this whole section to know what you can and can't
do with this hotfix type.

The basic syntax looks like this, which adds in a Crazy Earl vending machine
near the "Highway" fast travel in The Droughts:

```python
mod.streaming_hotfix('/Game/Maps/Zone_0/Prologue/Prologue_P',
        '/Game/InteractiveObjects/GameSystemMachines/VendingMachine/_Shared/Blueprints/BP_VendingMachine_CrazyEarl',
        location=(46488, 22942, -3879),
        )
```

`rotation` and `scale` parameters can also be added, though `scale` hasn't
been very well tested.  `rotation` defaults to `(0,0,0)`, and `scale` defaults
to `(1,1,1)`:

```python
mod.streaming_hotfix('/Game/Maps/Zone_0/Prologue/Prologue_P',
        '/Game/InteractiveObjects/GameSystemMachines/VendingMachine/_Shared/Blueprints/BP_VendingMachine_CrazyEarl',
        location=(46488, 22942, -3879),
        rotation=(0, 180, 0),
        scale=(1.2, 1.2, 1.2),
        )
```

There are a few caveats with using this type of hotfix.  Unfortunately,
Gearbox's implementation of this hotfix type is somewhat broken, to the extent
that they have never successfully used it themselves in the live hotfixes.  The
hotfix includes parameters for location, rotation, and scale (like our
`streaming_hotfix` function), but the game totally ignores them, and instead
spawns the object right at location `(0,0,0)` with the default rotation and
scale.  So mods which want to use this type of hotfix need to "manually" do
the repositioning themselves.

The `streaming_hotfix` function takes care of this for you automatically.  For
instance, the first example above generates the following in your mod file:

    SparkEarlyLevelPatchEntry,(1,11,0,Prologue_P),/Game/Maps/Zone_0/Prologue,/Game/InteractiveObjects/GameSystemMachines/VendingMachine/_Shared/Blueprints,BP_VendingMachine_CrazyEarl,80,"0.000000,0.000000,0.000000|0.000000,0.000000,0.000000|1.000000,1.000000,1.000000"
    # Doing repositioning for BP_VendingMachine_CrazyEarl_C_0 in Prologue_P
    SparkEarlyLevelPatchEntry,(1,1,1,Prologue_P),/Game/Maps/Zone_0/Prologue/Prologue_P.Prologue_P:PersistentLevel.BP_VendingMachine_CrazyEarl_C_0.RootComponent,RelativeLocation,0,,(X=46488.000000,Y=22942.000000,Z=-3879.000000)
    SparkEarlyLevelPatchEntry,(1,1,1,Prologue_P),/Game/Maps/Zone_0/Prologue/Prologue_P.Prologue_P:PersistentLevel.BP_VendingMachine_CrazyEarl_C_0.RootComponent,RelativeRotation,0,,(Pitch=0.000000,Yaw=0.000000,Roll=0.000000)
    SparkEarlyLevelPatchEntry,(1,1,1,Prologue_P),/Game/Maps/Zone_0/Prologue/Prologue_P.Prologue_P:PersistentLevel.BP_VendingMachine_CrazyEarl_C_0.RootComponent,RelativeScale3D,0,,(X=1.000000,Y=1.000000,Z=1.000000)

Note the initial type-11 hotfix followed by three positioning hotfixes.  It
also includes a comment about doing the positioning -- you can disable that
by passing `quiet_streaming=True` to the initial `Mod` constructor.

One further wrinkle here is that we have to know what sub-object to use to
reposition the object.  In the example above, that sub-object is `RootComponent`,
but it varies by type.  The library has a mapping for a number of objects
(check the `_StreamingBlueprintHelper` class to see the list for yourself), but
if you try to inject an object the helper doesn't know about, it will raise
a RuntimeError.  To specify the subobject name yourself, in these cases, use
the `positioning_obj` parameter to `streaming_hotfix`.  For instance, using
the initial example:

```python
mod.streaming_hotfix('/Game/Maps/Zone_0/Prologue/Prologue_P',
        '/Game/InteractiveObjects/GameSystemMachines/VendingMachine/_Shared/Blueprints/BP_VendingMachine_CrazyEarl',
        location=(46488, 22942, -3879),
        positioning_obj='RootComponent',
        )
```

If you do discover some mappings which are not in the library yet, please feel
free to send them along so they can get added to the library!  If you're not sure
what object name to try, `RootComponent` is a decent first guess, but if that
doesn't work, you'll have to dig into object serializations to figure out what
name to use.

Another thing to note is that the object names we use for positioning start with
an suffix of `_0` for the first one added, and go up by one for each of the same
type of object added to the map.  This library keeps track of which indexes to use
when doing the auto-positioning hotfixes.  If more than one mod tries to add the same
type of object to the same map, though, the mods will have no way of knowing what the
proper index is.  So, effectively, two mods won't be able to add the same object
type to the same map, using our current methods.

One *other* thing to note is that this hotfix type *cannot* be used to add objects
to a map which already contains that object type.  So if a map already has ammo
vending machines, for instance, you won't be able to add more ammo vending machines.

The final thing to note with this hotfix type is that it *requires* at least B3HM
v1.0.2 to work properly.  The type-11/streaming hotfix itself seems to require some
time to fully load into the level, when processing hotfixes, and if the repositioning
hotfixes happen too soon after the streaming hotfix, the object won't exist yet to
be repositioned.  So, a delay has to be injected inbetween the streaming hotfix
and the repositioning hotfix, and B3HM is the only reasonable place where this can
be accomplished.  So, mods using this type of hotfix *must* use at least v1.0.2 of
B3HM to work properly.  (The Linux mitmproxy-based `hfinject.py` also supports
injecting these delay statements properly.)

Data Introspection
==================

This project also includes a `bl3data` project which can be used to simplify
programmatic access to BL3 data, so long as you have it set up properly.  There
are two data sources the package can draw from:

1. Extracted BL3 data, using the technique [described by the BLCMods wiki](https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data#extracting-raw-datafiles).
2. [The BL3 References database](http://apocalyptech.com/games/bl3-refs/) - 
   simply download the SQLite version of the database and unzip it somewhere
   on your hard drive.  A MySQL/MariaDB dump is also available, or you could
   use [my refs-creation script](https://github.com/apocalyptech/bl3hotfixmodding/blob/master/dataprocessing/populate_refs_db.py)
   to generate the database from your already-extracted datafiles, though
   grabbing the provided SQL dump will almost certainly be quicker.

Of the two data sources, the first is required.  In order for `bl3data` to 
actually make use of the data, you also need to have a
[JohnWickParse](https://github.com/apocalyptech/JohnWickParse/releases)
binary available to do data serialization (the version linked to here is my
own fork which is optimized for BL3 usage).

The refs database is only needed if you want to use the `get_refs_to()` or
`get_refs_from()` methods, to look up references betwen objects.

When you first run any methods using `bl3data`, the app will create a config file
for you and tell you the path name.  You'll need to fill in the information
requested in the `filesystem` section to use `bl3data`.  The `database` section
is where you can specify the optional path to the SQLite references database.

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

Hotfix Generator
================

Hotfix Generator, in the `hotfixgenerator` dir, is an in-progress app by
[Trevor Troxel](https://github.com/TrevorSTroxel) which aims to streamline
the process of writing BL3 hotfix mods.  Check out its directory for more
information.

License
=======

As of 2021-08-15, Both bl3hotfixmod and bl3data are licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).
Prior to that date, they were licensed under [GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](COPYING.txt) for the full text of the license.

