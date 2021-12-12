Boss Guardian Takedown
==============

Replace mobs in Guardian Takedowns with named Badasses and
bosses.

We have 2 curated takedowns and a random takedown generator.

* `bosstakedown.skrunt1.bl3hotfix` a harder version of the guardian takedown meant to be somewhat relevantly themed to the Guardian Takedown. 
* `bosstakedown.skrunt2.bl3hotfix` DLC3 invades the Guardian Takedown, fight some saurians and cowboys.

Header
======

* Name: Boss Takedowns
* Version: 0.0.1
* Author: skruntskrunt
* Categories: gameplay, spawns, takedowns
* License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
* License URL: https://creativecommons.org/licenses/by-sa/4.0/
* Code License: GNU Public License Version 3

Changelog
=========

**v0.0.1** - 2021-12-11
 * skrunt1 creator mix 
 * Maliwan Takedowns don't work yet but CZ47 did such a great job so go play his mod.


Known Bugs
==========

Some mobs get stuck on the top of Nekro balls in the sky, look up there.

Please report bugs to this repository on github: https://github.com/abramhindle/bl3mods

Conflicts with Raid mod.

Sometimes spawns leak into basegame.

Licenses
========

All the mods in this repository are currently licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

References
==========

Inspiration from CZ47 Raid on Maliwan Takedown mod (totally jealous).

Thanks to Rockroze1, professor portal, philipambrose, ssucka,
government toast, QualityControl, and more for helping me test this.

Development Info
================

Check the `Makefile` for examples of how to generate the mod.
You can edit the spawnoptions json files to choose the mobs you want.

`bosstakedown.py` is relatively poorly written and poorly structured, but it generates the mod.

`make bosstakedown.666.bl3hotfix` will make a Guardian Takedown with random mobs chosen by seed 666.

`make skrunt` will make the currated mods from `skrunt/*.json`

Development Home
================

This mod is being developed on the `bosstakedown` branch of:

https://github.com/abramhindle/bl3mods

You can get latest versions there. Pull requests, patches, and
feedback (as issues) are welcome.

Bug reporting
=============

Please report bugs to this repository on github: https://github.com/abramhindle/bl3mods
