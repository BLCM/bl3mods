Fix Siren COM Blank Parts
=========================

Siren COMs have a peculiarity of their parts definition which means
that they can potentially spawn with one fewer part than they're
supposed to, or at least one fewer part than any other chars'
COMs have.  This is pretty rare, but it *is* something that's possible
in the data, so this mod just patches that up.

**Notes on Mod Compatibility:**

If using this mod along with World Drop Ixora COMs, make sure that this
mod is *before* World Drop Ixora COMs in your mod list.  The World Drop
Ixora COMs takes care of fixing the blank Siren COM parts for the COMs
that it touches, and this mod would disable the wrong part if run after
World Drop Ixora COMs.

Changelog
=========

**v1.1.1** - Jan 10, 2021
 * Fixed a bug that's been present since the June 25, 2020 BL3 patch
   which added Action Skill Damage as a possible COM part -- this mod
   had been zeroing out *that* part instead of the blank part.

**v1.1.0** - Sep 26, 2020
 * Updated for DLC4 Siren COM

**v1.0.0** - Sep 26, 2020
 * First versioned release
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

