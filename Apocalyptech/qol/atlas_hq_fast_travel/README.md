Atlas HQ Fast Travel
====================

This is a collection of mods which move the fast travel machine in Atlas HQ
to one of a few different locations, to avoid having to take a jog through
otherwise completely-empty areas of the level on your way to take on Power
Troopers or Katagawa Jr.  In all cases, it swaps out another New-U station
in place of the fast travel machine ordinarily in the bank, so your map
state will be remembered properly at the beginning of the level.

There's one bug with this that I still haven't been able to figure out: when
you first Fast Travel into the map from outside, you'll wind up in the
bank area as if the Fast Travel station was still there.  You can then do
a quick in-level Fast Travel to get where you want to be, at least.  Perhaps
eventually I'll figure out how to get around that problem.

Regardless, there are three variants:

* **Courtyard** - Moves the Fast Travel to the promenade level, just
  outside the entrance to the main Atlas HQ building.  The New-U machine
  which is ordinarily to the right when entering the building has been
  moved over to the bank.  That New-U spawns you pretty far away from the
  machine, when you resurrect -- nearly outside the bank, even.
* **Elevator Base** - Swaps with the New-U station at the base of the
  main Atlas HQ elevator.
* **Rhys' Office** - Swaps with the New-U station in Rhys' Office.

TODO
====

* Figure out that initial-fast-travelling-in issue.  I suspect the problem is
  that the player location probably gets set before any hotfixes run (even
  "early" level hotfixes), so this might not be fixable without something like
  an SDK.
* While *in* Atlas HQ itself, the FT icon doesn't show up on the map (though
  the proper area is highlighted when you choose it to Fast Travel).

Changelog
=========

Aug 1, 2022 *(no version number change)*
 * Updated to use [new metadata tags](https://github.com/apple1417/blcmm-parsing/tree/master/blimp)
   (no functionality change)

Jun 16, 2021 *(no version number change)*
 * Added contact info to mod header

**v1.0.1** - May 8, 2021
 * Move FT icon to the proper place when viewing the map from other
   locations (though the icon disappears when you're actually in Atlas
   HQ).
 * Also made a note about the initial-fast-travelling issue; apparently
   I'd not noticed that until now.  Perhaps the April patch changed
   something?  Unlikely; I probably just missed it.

**v1.0.0** - Mar 15, 2021
 * Initial release
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

