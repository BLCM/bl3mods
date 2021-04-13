Manufacturer Lock
=================

Where possible, locks weapon drops to only the specified manufacturer, apart from
specific boss/miniboss/rare-spawn drops, which are left totally alone.  There's
one mod here per manufacturer, so you can choose whichever one you like.

Note that the mods only touch pools in which the manufacturer actually exist, so
if you choose the Atlas lock mod, for instance, you'll still get the usual range
of shotguns, SMGs, and sniper rifles, since Atlas doesn't make those gun types.
You'd be limited to Atlas for Pistols, Heavy Weapons, and ARs, though.

You can generate your own custom combinations from the commandline by running
the generation script yourself.  For instance, if you wanted the game to only
drop Vladof or Dahl weapons for you, you could run:

    ./gen_manufacturer_lock.py dal vla

Which would generate a `manufacturer_lock_dal_vla.txt` file.  The manufacturer
abbreviations are:

* atl
* cov
* dal
* hyp
* jak
* mal
* ted
* tor
* vla

This mod has been updated as far as DLC6 (Director's Cut).

Changelog
=========

**v1.3.0** - Apr 11, 2020
 * Updated with DLC6 (Director's Cut), Vault Card 1, and related guns

**v1.2.0** - Nov 10, 2020
 * Updated with DLC5 (Designer's Cut) guns

**v1.1.0** - Sep 29, 2020
 * Updated with DLC4 guns

**v1.0.0** - Sep 26, 2020
 * First versioned release
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

