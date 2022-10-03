Jetbeasts (Almost) Everywhere
=============================

Gehenna's Jetbeast-production industry goes galactic!  Adds in new
Jetbeast Catch-A-Ride consoles wherever Catch-A-Rides are already found
throughout the game.  This mod also adds in "regular" Catch-A-Ride
consoles in The Blastplains, in case Jetbeasts aren't Your Thing.  This
mod unfortunately omits Skittermaw Basin -- due to some limitations of
the hotfixes we use, adding Jetbeasts in there appears to be impossible.

The new Catch-A-Ride consoles have often been placed in such a way
that it's pretty clear which one is the original and which one is the
addition, though in some cases it might not be obvious.  The Jetbeast spawners
have been set to use a slightly alternate texture (the one used in
DLC2/Hibiscus consoles) which makes them a little more washed-out looking.
This visual change has been applied to the consoles in The Blastplains,
as well.

**Compatibility Note:** This mod *requires* either OpenHotfixLoader or
B3HM v1.0.2 (or greater) to work properly.  Note that as of time of the
mod release, B3HM v1.0.2 has not yet been released, so OHL is the only
supported way to run the mod until then.

**Compatibility Note 2:** This mod will *not* be compatible with any other
mod which adds in Catch-A-Ride consoles/platforms to the same levels.

Bugs/TODO
=========

- Honestly the far *better* way to do this would be to figure out how to
  just get Jetbeasts to appear in the regular CAR consoles alongside the
  other vehicles, and vice-versa, and doing so would've been a hell of a lot
  less work, too.  Unfortunately I still have no idea how I'd go about that.
- When Jetbeasts spawn, they're not centered on the platforms.  (This is
  actually the case even for "vanilla" Jetbeast consoles on Gehenna).
  There's an attribute for positioning which can theoretically be set, but it
  looks like when there's more than one console attached to a platform, the
  positioning for the *first* one is the only one you can freely set.  The
  positioning on the second will apply so long as it's the same as the first,
  but I couldn't get them to be set independently.
- I'd love to be able to make the Jetbeast spawners more visually distinct.
  We're already applying the Hibiscus material override to them, which makes
  them a little whiter and more washed-out, but that's pretty subtle.  We
  could apply a more *obvious* material override, but since those aren't
  made for the CAR consoles, it'd almost certainly look weird and not fit
  in visually.  The other easiest thing would theoretically be to make them
  *smaller*, but the scaling parameters don't seem to like applying to CAR
  consoles for some reason.
- On levels with mission-specific vehicles (fuel truck in The Droughts,
  Project DD in Neon Arterial, Vaugn's Technical in Sandblast Scar), if the
  vehicle is destroyed, the map indicator of where to go to respawn the
  vehicle will point to the "old" Catch-A-Ride consoles (which are now far
  off-map), for cases where we've replaced the CAR system entirely.  You
  can still use any local CAR console to respawn the vehicle, though.

Changelog
=========

**v1.0.0** - Oct 2, 2022
 * Initial release

Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

