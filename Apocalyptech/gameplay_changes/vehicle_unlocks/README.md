Vehicle Unlocks
===============

This mod causes all enemy vehicle spawns to have the widest possible
range of parts available (including skins), right from the beginning
of the game.  Enemy vehicle spawns will also have an equal chance of
spawning each part, so no parts are more rare than others.  This is
intended to make collecting all the vehicle parts easier, and to make
the enemy vehicles quite a bit more colorful!

This does *not* interfere with the Ellie challenges to collect
specific vehicle parts -- even if you already have the parts unlocked,
you can still hijack the specific vehicles and turn them in to
complete the challenge.

There are three variants of the mod:

* [**Vehicle Unlocks**](https://github.com/BLCM/bl3mods/wiki/Vehicle%20Unlocks): Keeps maps locked to the vehicle types it could always
  spawn, so maps which only spawned Outrunners will continue to only
  spawn Outrunners (though you'll get all possible varieties of
  Outrunners)
* [**Vehicle Unlocks+**](https://github.com/BLCM/bl3mods/wiki/Vehicle%20Unlocks%2B): *Completely* unlocks vehicles, so every map which can
  spawn enemy vehicles will have a mix of Outrunners, Technicals,
  Cyclones, and Jetbeasts.  The spawners *do* retain a slight bias
  towards the original vehicle types, though.  This variant basically
  requires that you own DLC3 (Bounty of Blood).
* [**Vehicle Unlocks (Legacy)**](https://github.com/BLCM/bl3mods/wiki/Vehicle%20Unlocks%20%28Legacy%29): This is the pre-v2.0 version of the mod which was
  *not* able to alter wheel/chassis types, so for instance there was
  no level which would spawn a Zip Outrunner, or a Barbed Technical.
  The Standard/Plus versions *might* be a little unreliable in
  multiplayer, though, so if you play in MP and some enemy vehicles
  are invisible to guests, for instance, you might want to fall back
  to this version.

This mod also adds Monster Wheels to a few specific vehicles, though
there's not much reason to now that v2.0 adds in full chassis/wheel
randomization in levels:

* Clever Girl (Floodmoor Basin)
* Festive Flesh-Eater (Splinterlands)
* Skagzilla (The Droughts)
* The Legacy version also adds Monster Wheels to every Technical
  in Sandblast Scar

The Standard/Plus versions of the mod also add in some rare "stolen"
vehicle spawns, in some maps, which feature drivers/riders which
aren't ordinarily found on vehicles in the game.  Also, vehicles
with heavy armor are no longer labelled as "Heavy."  In lieu of that
(since heavy armor can pop up on any vehicle spawn now), some
vehicle spawns have a chance to spawn with Badass riders.

**Note:** Despite the word "unlock" in the mod title, note that this does
*not* automatically unlock vehicle parts in your own Catch-A-Ride menus.
You'll still have to hijack enemy vehicles and scan them in (or use a save
editor) to make the parts available to yourself.

**Multiplayer Note:** It's possible that the Standard/Plus versions
might behave a bit oddly in multiplayer -- guests might not be able to
see Jetbeasts in a level which doesn't ordinarily have them, for instance,
though in my (very limited) testing, subsequent Jetbeasts are often visible.
For best results, make sure that all connected players are running the same
mod.  If there's still unexpected behavior that you find unacceptable,
though, you may just have to drop back to the Legacy version.

Changelog
=========

Aug 28, 2022 *(no version number change)*
 * Updated "Vehicle Unlocks" and "Vehicle Unlocks+" to be regular files,
   instead of compressed, for OpenHotfixLoader compatibility.

Aug 1, 2022 *(no version number change)*
 * Updated to use [new metadata tags](https://github.com/apple1417/blcmm-parsing/tree/master/blimp)
   (no functionality change)

**v2.0.0** - October 11, 2021
 * Complete rewrite which allows us to spawn alternate wheel/chassis types
   in addition to randomizing the rest of the parts, and in fact allows us
   to add in whole vehicle types (like adding Jetbeasts to The Droughts,
   for instance).  Also:
   * Added jokey "stolen" vehicle spawns to some maps
   * Added badass enemy riders in lieu of dedicated "heavy armor" spawns
   * Standardized vehicle naming to omit team/faction, but always report
     chassis/wheel type.
 * Split into three variants:
   * "Vehicle Unlocks," which doesn't add new vehicle types to maps
   * "Vehicle Unlocks+," which *does* add new vehicle types to maps
   * "Vehicle Unlocks (Legacy)," which is just the old v1.0.1 version of the mod

Jun 16, 2021 *(no version number change)*
 * Added contact info to mod header
 * This is the last update for the "Legacy" version

**v1.0.1** - May 10, 2021
 * No functionality changes, just updating the README and in-mod
   description to be a bit more accurate.

**v1.0.0** - Sep 26, 2020
 * First versioned release
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

