Mega TimeSaver XL
=================

This mod aims to speed up nearly all the noticeably-slow interactive
objects that you use throughout BL3.  It will eventually hope to encompass
basically the entire game, but **it is currently a work in progress!**
I've run up against some modding difficulties with the first complex-ish
mission-related animation in the game (scanning Vaugn's Wanted posters to
print statues during the "Golden Calves" mission in Ascension Bluff), and
it looks like it might take me some time to figure that out (and I don't
want to skip it just yet).

As such, this mod has not seen an awful lot of testing, so please let me
know if there's anything game-breaking or Obviously Wrong with this (like
if a too-fast animation ends up breaking mission progression somewhere).
Ordinarily I wouldn't release this until I'd had a chance to thoroughly
test it, but I think I'll be on that Golden Calves mission for awhile.

Currently, the mod affects the following:

* Lootable Containers
* Doors
* Vehicle interaction animations (hijacking, entering, leaving, changing seats)
* Catch-A-Ride Digistruct Speed
* Character Movement Speeds:
  * Claptrap
  * Lilith
* Eridian tools (Resonator, Analyzer)

Note that the vehicle animations in particular are a bit weird right now --
the animation gets "frozen" near the end for a bit.  I think that's something
that we can't do much about at the moment, though I'll be looking into it
more for the eventual 1.0 release.  Check the full README for known bugs and
my current TODO!

Known Bugs
==========

* Weapons on vehicles that you hijack seem to take a little bit to
  become active, possibly based on timing from the original hijack
  animations?  Vehicle movement, at least, is available right away,
  though steering is not.  Hrmph.
* The door you have to slide under to retrieve the umbrella for
  Claptrap in Bad Reception acts a bit weirdly, and is probably
  pretty easy to just run through now.

TODO
====

* Other character-speed improvements (Oletta comes to mind)
* Pretty much every mission-specific animation
* Elevators
* Lost Loot machine?
* I can speed up the slot machine animations easily, but they don't actually
  drop loot until after a set timer (synced with the sound effects).  Haven't
  been able to figure that out yet.
* Delay after breaking bone piles, trash cans, etc (basically pickups which
  aren't actually "connected" to a container)
  * Bone Piles
  * Trash Cans
  * Washing Machines
  * Cardboard Boxes
  * Some Mailbox drops
  * Some porta-potty drops
  * Eridian Crystals
* I feel like the Slam animation could use some work
* Entering/Exiting Iron Bear?
* Maybe have a real slight speedup on melee attacks?
* Level-loading (digistruct) animation/movie playback?
* Speed of camera that moves in/out of Photo Mode?

Changelog
=========

**v0.9.1** - May 10, 2021
 * Mod file was rebuilt using some updated backend infrastructure; no
   actual changes, but some values changed from integers to floats
   (`1000` -> `1000.0`, for instance)

**v0.9.0** - March 10, 2021
 * Initial beta release.  Incomplete, but should be handy regardless!
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

