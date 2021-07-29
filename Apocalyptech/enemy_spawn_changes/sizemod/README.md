Sizemod
=======

This is a collection of mod which attempts to scale all NPCs (enemies or
otherwise) by various factors, to make them very small, or very large.
This will almost certainly be game-breaking in some circumstances, so let
me know if anything really dire happens with any of these.

There are a number of options available:

* Tiny: 0.4x
* Smol: 0.7x
* Big: 2.0x
* Huge: 3.0x
* Giant: 5.0x

To use a custom value, edit the generation script to add more, and
re-run it.

Note that characters who are interacting with the environment in some way,
like typing on a console, or leaning up against a wall, will generally
be unaffected by this change, as the scene-based animation seems to override
the size scaling.

Changelog
=========

**v1.3.1** - Jun 16, 2021
 * Tweaked some scaling values due to data patches we must've missed with DLC6
 * Added contact info to mod header

**v1.3.0** - Apr 14, 2020
 * Updated with DLC6 BPChars
 * Correctly exclude FL4K's Loader Pet from alterations

**v1.2.0** - Nov 11, 2020
 * Updated with DLC5 BPChars

**v1.1.0** - Oct 3, 2020
 * Updated with DLC4 BPChars
 * Now takes into account any already-applied scaling on the models

**v1.0.0** - Sep 26, 2020
 * First versioned release
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

