Warning
-------

This is all a bit weird, and I don't necessarily recommend it for public use,
though it's been working well enough for me.  This just exists basically due
to some limitations with our current object serialization abilities -- if those
ever get figured out, this may get a revamp into something a little more
reasonable (and will probably end up in my `bl3hotfixdata` library instead).

Anyway, I'm using it for a couple of mod-generation scripts, and you're free
to do the same, but keep in mind that this dir may change drastically at any
point, and I don't *fully* trust the data in here.

Overview
--------

This is a little SQLite database I put together to give me an easy way to
look up the names of map-based objects.  It's a bit hokey and I don't
fully trust it to Do The Right Thing in every circumstance, so I've not
bothered to integrate this into any existing frameworks, or to expand it
to do something more general-purpose.

Basically, it's just useful when you want to find all of a certain kind of
object in a certain map, across all of the map sub-objects.  For instance,
I wanted to get rid of the timer which prevents you from opening Red Chests
too closely together, and it seems to do so, I need to specifically alter
each chest -- I can't just alter some `Default__` parameters on the base
object.

So, I need to figure out all instances of `BPIO_Lootable_COV_RedCrate_C`
objects in any map which contains them.  That's kind of a pain ordinarily,
since those objects can be spread out over multiple `.umap` files in the
game data, and there's some map objects which (as of May 3, 2021) we still
can't serialize, so finding the full object names for all of them can't
be done that way.  (Once we *can* reliably serialize all map objects, this
project should really get a full rewrite to make use of that, and get rid
of a lot of the nonsense in here.)  A `getall` on the console would work,
but that would have to be run on every single map.

In the end, what I'm making use of is the object-name-dumping functionality
included in the [Universal Unreal Engine 4 Unlocker](https://framedsc.github.io/GeneralGuides/universal_ue4_consoleunlocker.htm),
which will output a couple of files containing object info when requested.
This, too, requires doing so manually on every single map, but I've already
gone ahead and done that for modding purposes a long time ago (and have
been updating my object-name dumps with every DLC release), so I've already
got that data handy.  I *am* also making use of a fully-extracted set of
BL3 data ([using these methods](https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data))
to determine the canonical sub-map names which exist for each map.

Doing this requires a little bit of piecing-together:

- The `ObjectsDump` files don't have the *complete* path to the objects;
  rather, they just start at the "last" component.  This is why we're
  looking into the extracted data, mostly, to get that path.  (You *can*
  get that info from the `NamesDump` file but IMO it's slightly hokier
  that way.
- UUU, at least in the versions that I'm using, often put the wrong number
  at the end for number-suffixed objects.  Specifically, they tend to
  be one too high.  So we've got to subtract one on any object which
  ends with `_N`
  - Note that *sometimes* this is not the case.  Some objects really do
    have a hardcoded number suffix which is stored differently than the
    other sort.  I'm pretty sure that for the level-specific paths that
    I'm interested in, that rarely if ever happens, though, so I'm not
    bothering to do anything about it.

So that's the general process: grab a list of all map sub-objects from the
extracted data filesystem, then loop through all the `ObjectsDump` files
looking for objects which match those sub-object names.  Shove that all
into a SQLite database, and Björn Stronginthearm's your uncle.

Running All This
----------------

This isn't really set up to be user-friendly, so expect to have to do your
own debugging.

**Step Zero:** [Extract all the BL3 data.](https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data)
Then use UUU to generate a `UE4Tools_NamesDump.txt` and `UE4Tools_ObjectsDump.txt`
file for every level you're interested in.  Follow their docs to do so.  The
`NamesDump` file isn't used at all at the moment, but it gets generated at the
same time.

- I also compress those files using [the xz util](https://tukaani.org/xz/) to turn
  the filename into `UE4Tools_ObjectsDump.txt.xz`, and take up far less space.  This
  is optional, but you'll have to edit the processing script otherwise.
- I have my dumps set up in the following data structure; if you deviate too far
  from this (different number of directory levels, etc), you'll have to tweak the
  script to suit:
  - `basegame` - Contains dirs `AtlasHQ_P` through `WetlandsVault_P`
  - `others` - Contains dirs `COVSlaughter_P` through `TechSlaughter_P` (includes Raids and Proving Grounds)
  - `events` - Contains dirs `BloodyHarvest_P` and `Cartels_P`
  - `dlc1` - Contains dirs `CasinoIntro_P` through `Trashtown_P`
  - `dlc2` - Contains dirs `Archive_P` through `Woods_P`
  - `dlc3` - Contains dirs `CraterBoss_P` through `Town_P`
  - `dlc4` - Contains dirs `Anger_P` through `Sanctum_P`
  - `dlc5` - Contains the single dir `FrostSite_P`
  - `dlc6` - Contains dirs `Cabin_P` through `SacrificeBoss_p`

**Step One:** Initialize the SQLite database.  I just do this from the CLI:

    sqlite3 map_objects.sqlite3 < schema.sql

**Step Two:** Alter `populate_map_objects.py` to suit, specifically the
"Constants" section near the top.

- `sqldb` is the name of the SQLite database
- `datadir` is the path to a fully-extracted BL3 data set
- `dumpsdir` is the path to a collection of dirs which contain the UUU dumps.
  If your directory structure isn't somewhat similar to the one above, you
  may have to tweak the script.

Some additional vars you probably shouldn't have to touch:

- `mapglobs` - Where to find map objects in the game data
- `blocklist` - Directories to ignore, inside those globs
- `dumpdir_blocklist` - Some dirs inside the dumps dir to ignore (I have some
  dumps for vehicle data in my dir)

**Step Three:** Run `populate_map_objects.py`.  That should do!

**Step Four:** Use SQLite to query the DB, or I've got an example lookup
script at `get_map_obj_type.py`.  For instance, to find all `BPIO_Lootable_COV_RedCrate_C`
objects, like I was interested in when I wrote all this, you could do:

    get_map_obj_type.py -c BPIO_Lootable_COV_RedCrate_C

... or to find *just* those objects inside `Prologue_P`:

    get_map_obj_type.py -c BPIO_Lootable_COV_RedCrate_C -m Prologue_P

Which would yield results like:

    /Game/Maps/Zone_0/Prologue/Prologue_Combat.Prologue_Combat:PersistentLevel.BPIO_Lootable_COV_RedCrate_114
    /Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BPIO_Lootable_COV_RedCrate_114
    /Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BPIO_Lootable_COV_RedCrate_1290

Library
-------

I've wrapped up access to the database in a very dumb little `mapobjlib`
library, which is what `get_map_obj_type.py` to access its data.  I'm also
going to be using that for a few mod-generation scripts.  If I ever make
this a bit more official, that'll probably want a rewrite.

Fin
---

That's it!  As I say, this isn't really intended to be user-friendly
'cause I'm not too sure about the overall data validity, or even this
current implementation.  Still, here it is!

