Visible BPChar Names
====================

Updates Character (both NPC+Enemy) visible names to be the actual
BPChar name from the game data.  Useful for modders looking to make
sure they know exactly what BPChar is being used at any given time,
and completely useless for everyone else!

Note that the names displayed here may not be 100% accurate -- there's
some edge cases where I suspect the game could end up reporting a "base"
class name instead of the more-specific one.  There's also probably a
few cases where the game ends up using the usual names despite this mod.

Interestingly, many of the stationary NPCs found in the game (such as many
of the passengers in Sanctuary III) tend to *not* be BPChars, so they
aren't affected by this mod.  Those are InteractiveObjects instead,
typically.

This is also a pretty "heavy" mod -- there's over 500 `MatchAll`-based
hotfixes to try and catch all possible SpawnOptions objects (trying to
tailor hotfixes to only fire when required for all of those seemed
like a daunting task).  That doesn't seem to actually incur any
noticeable performance impact, at least, but something to maybe be
aware of.

[WL version can be found here.](https://github.com/BLCM/wlmods/wiki/Visible%20BPChar%20Names)

Changelog
=========

**v1.0.0** - Oct 11, 2022
 * Initial release
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

