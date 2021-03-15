Name: Raid on Bloodsun Canyon, Raid on VIP Tower, and Raid Bosses
=================================================================

* The Raid on Bloodsun Canyon: Fight all the named enemies in
  Bloosun Canyon who now have the strength of invincible raid boses.
* The Raid on VIP Tower: Fight all the named enemies in VIP tower
  who now have the strength of invincible raid boses. Except
  Freddie. Freddie is level 2 most of the time.

This mod attempts to make bosses tougher and makes boss fights
non-trivial. This mod is meant for Mayhem 10/11 Level 65 End Game
players and meant for COOP play against bosses who are spongier,
stronger, and drop a lot more loot. Bosses tend to drop a lot of their
dedicated loot pool making the long fight worthwhile as you can pick
up the annoint you were looking for.

Tougher Bosses include:
* Graveward
* Ruiner
* Troy
* Tyreen
* Captain Traunt 
* General Traunt 
* Rampager
* Power Rangers
* Trial bosses
* etc.

Balance help is appreciated. The underlying philosophy is that a big
spongey raid boss fight makes you deserving of dedicated drops.

Header
======
* Name: Raid on Bloodsun Canyon, Raid on VIP Tower, and Raid Bosses
* Version: 1.4.1
* Author: Abram/skruntskrunt,  Apocalyptech, EpicNNG, Grimm, and more
* Categories: enemy-drops, loot-system, mode-balance, enemy
* License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
* License URL: https://creativecommons.org/licenses/by-sa/4.0/


Changelog
=========
**v1.4.1** - 2021-03-15
 * Minor bug fix

**v1.4.0** - 2021-03-12
 * More automation, more bosses, better control of loot by style

**v1.3.0** - 2021-03-04
 * First versioned release
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

Development Home
================

This mod is being developed on the raid branch of:

https://github.com/abramhindle/bl3mods

You can get latest versions there. Pull requests, patches, and
feedback (as issues) are welcome.

Bug reporting
=============

Please report bugs to this repository on github: https://github.com/abramhindle/bl3mods

Dev Instructions
================

If you want to modify the software raid.py is the main generator of the hotfix.

* raid.py - main program
* raid.bl3hotfix.HEAD - header that is added to the head of raid.py output
* raid.bl3hotfix - generated via `python3 raid.py > raid.bl3hotfix`
* README.md - this readme
