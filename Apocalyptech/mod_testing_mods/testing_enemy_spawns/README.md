Testing Enemy Spawns
====================

This mod isn't actually a general-purpose mod.  Rather, it's what I use to spawn
specific enemies into the game (for testing enemy behaviors or enemy-specific
mods, for instance).

To use this, you're meant to edit the generation file and alter the parameters to
suit what you want.  The checked-in version will set all spawns in Cathedral of the
Twin Gods to be Wotan, which probably isn't what you had in mind.

Cathedral of the Twin Gods is a nice level to work with, since the spawn points
are set up in a way which permits even "big" enemies like Wotan to show up -- most
levels only have spawns where the BPChars are coming out of buildings or dens in
the wall, etc, and the bigger enemies tend to either not spawn at all, or fall
through the geometry.  There's a bit of that in Cathedral as well, but bosses like
Wotan and Rampager will spawn in properly, so it seems like a good choice.  (Note
that Rampger will get locked up on its first immunity phase, though.)

Changelog
=========

Jun 16, 2021 *(no version number change)*
 * Added contact info to mod header

**v1.0.0** - Mar 22, 2021
 * Initial Release
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

