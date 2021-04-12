Boss Rush: Billy and the Clone-a-saurus
=================================

So do you want get a boss rush?

Billy, one of the Billy sisters, was cheesed that vault hunters had
attacked her and her sisters. Billy broke into a stash of stolen
Maliwan equipment and found what Katagawa-Jr was using to produce his
clones. Billy had an idea, what if she cloned the Saurians of the
Borderlands and made theme park featuring them. Instantly she realized
that it was a dumb idea and questioned why anyone would entertain such
an idea. But could she use this cloning machine to clone Saurians and
other defeated Badasses to defeat the Vault Hunters once and for all?

This is a boss rush mod that can generate different configurations of
a boss rush. It is directly based on `altef_4`'s research and source
code. It shows none of the love and care and careful effort that
`altef_4` used. This is built in the style of Isaac of Binding Boss
Rush: just excessive and unfair. And that is the point. An insane boss
rush for OP Level 65 builds at Mayhem 10 or 11.

Thank you to the true hero: altef_4. His careful modding to produce
the Hyperion slaughter star 3000 allowed me to spend very little time
changing his mod.

You'll know the mod is loaded if the mission description of the
Slaughterstar 3000 mentions Billie.

Header
======
* Name: Boss Rush: Billy and the Clone-a-saurus
* Version: 0.9.1
* Author: Abram/skruntskrunt,  altef-4, Apocalyptech, Grimm, and more
* Categories: gameplay
* License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
* License URL: https://creativecommons.org/licenses/by-sa/4.0/
* Code License: GNU Public License Version 3

Changelog
=========

**v0.9.4** - 2021-04-11
 * Made round end bosses, every round has end bosses
 * Changing of names of tough monsters
 * Lots of bug fixing.
 * Massive debugging.

**v0.9.3** - 2021-03-21
 * Remove balconey spawns (reduces mission blocking bugs)
 * Add a description of the mod in the mission text
 * Reduce the total number of mobs to to avoid sound bugs (too many unique mobs, sound skips)
 * Toughen Mobs randomly (25% get buffed)
 * Add lots more variety of mobs

**v0.9.2** - 2021-03-28
 * Some bug fixes and added a mission description.
 
**v0.9.1** - 2021-03-22
 * Bug fixing and adding the ability to better control mob deployment via json definition files.

**v0.9** - 2021-03-18
 * First versioned release


Known Bugs
==========

This thing can cause crashes. Sometimes, somehow. It's not clear.

Stuck enemies: bring a void rift or a blackhole or a pull-out-method
in with you to yoink enemies out of the wall.

Enemies on top: Sometimes enemies cluster on the top rafters, bring a homing grenade.

Bad/Degenerate spawn: This is a hard problem sometimes enemies spawn
in a weird way and get stuck in walls. Rare but it happens.

Multiplayer: Sometimes it takes a while for your friends to load the
big bad bosses and so the bosses look like Maliwan troops but act
really rigid and strange with no animation. Just wait this one out.

Enemies that can cause trouble:
* Amach's witnesses like to float up to the top rafters, you can homing grenade them.
* Kukuajack produces gnats, they are hard to see, they float up.
* Sera's sometimes get stuck

Enemies I didn't enable because they were troublesome:
* Katagawa Jr. - just dies?
* Katagawa Ball - spawns randomly/inconsistently
* Skrakk - doesn't jump down
* Vice, Dreg, Petrodomini, Lasodactyl - for some reason flyers get stuck up top!
* Mouthpiece, gets stuck in an immunity phase
* Shiverous the Unscathed - gets stuck uptop
* Slittermaw, gets stuck
* Wrendon Esk, gets stuck

Licenses
========

All the mods in this repository are currently licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

References
==========

3000 Hyperion Slaughter by altef-4: https://github.com/BLCM/bl3mods/wiki/3000-hyperion-slaughter

Principal Skinner's great American Novel: Billy and the Cloneasaurus https://www.youtube.com/watch?v=ik0BPKM9WQg

Thanks to professor portal, rockroze1, helgenen, u4fun, governmentoast, and others for play testing.

Alternatives
============

You can try these premade hotfix mods with seeds. I like the saurian ones the best. You might need to download them and remove the `.txt` extension.

* https://raw.githubusercontent.com/BLCM/bl3mods/master/skruntskrunt/boss-rush-slaughter/boss_rush_3000.saurian.42.bl3hotifx.txt
* https://raw.githubusercontent.com/BLCM/bl3mods/master/skruntskrunt/boss-rush-slaughter/boss_rush_3000.42.bl3hotfix.txt
* https://raw.githubusercontent.com/BLCM/bl3mods/master/skruntskrunt/boss-rush-slaughter/boss_rush_3000.666.bl3hotfix.txt
* https://raw.githubusercontent.com/BLCM/bl3mods/master/skruntskrunt/boss-rush-slaughter/boss_rush_3000.bl3hotfix
* https://raw.githubusercontent.com/BLCM/bl3mods/master/skruntskrunt/boss-rush-slaughter/billy-and-the-cloneasaurus.bl3hotfix

See them at https://github.com/BLCM/bl3mods/tree/master/skruntskrunt/boss-rush-slaughter

Development Home
================

This mod is being developed on the `boss-rush` branch of:

https://github.com/abramhindle/bl3mods

You can get latest versions there. Pull requests, patches, and
feedback (as issues) are welcome.

Bug reporting
=============

Please report bugs to this repository on github: https://github.com/abramhindle/bl3mods


Dev Instructions
================

If you want to modify the software `gen_boss_rush_3000.py` is the main
generator of the hotfix. `boss.py` is full of boss definitions, and
`bpchar-gen.py` let's you just use json to define the menu for the
hyperion slaughter star.

* `gen_boss_rush_3000.py` - main program
* `boss_rush_3000.bl3hotfix` - generated via `python3 gen_boss_rush_3000.py`
* `bpchar-gen.py` - generate an reusable JSON file that you can edit to fine tune your boss rush.
* `README.md` - this readme
* `billy-and-the-cloneasaurus.bl3hotfix` - a very saurian themed generation of the boss rush
* `example_bpchars.json` - used as a template for generating these mods
* `boss_rush_3000.42.bl3hotfix` - boss rush with seed 42 (good dinos)
* `boss_rush_3000.666.bl3hotfix` - boss rush with seed 666 (General Traunt, lots of fun)
* `Makefile` - this describes the workflow to generate a mod. I usually just type
  `make boss_rush_3000.9999.bl3hotfix` where 9999 is the seed and it makes the mod for me.

How do you make `boss_rush_3000.42.bl3hotfix`?

```shell
python3 bpchar-gen.py --json gen_bpchars.42.json --seed 42
python3 gen_boss_rush_3000.py --json gen_bpchars.42.json --seed 42 --output boss_rush_3000.42.bl3hotfix
```

TODOs
=====

* [ ] Check Wotan spawn, to see if he can move if we use different spawns
* [ ] Get graveward to spawn properley (steal red rain's spawn and switch red rain's spawn?)
* [ ] Remove Boss Corpses
