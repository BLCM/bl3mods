Timed Event Enable: Bloody Harvest
==================================

This is a mod which can be used to enable Bloody Harvest, after it's been
"officially" closed down by Gearbox.  You can use this to override a
currently-active event, as well.  Note that only *one* timed event is capable of
being fully-active at any time.  You can use my All Event Spawns Active mod so that
all three timed event world spawns occur, but only the active event's missions
and maps will be fully available.

This mod also includes the most recent hotfix tweaks that Gearbox was using by the
end of the event, which for Bloody Harvest is quite a bit - tweaks to Terror anoint
rates, Captain Haunt fixes, hecktoplasm quantity, and more.

My Expanded Event Spawns mod can be used to expand the areas in which event-specific
world spawn changes (haunted enemies, hearts, cartel operatives) can appear.  By
default, each event has a predefined list of areas in which its spawns can occur.

This mod comes in two variants, depending on which year you'd like to activate.
The only difference between the 2019 and 2020 versions are the rewards you get for
finishing challenges.  The 2019 event rewarded the following:

* At 4 Challenges: Shrunk 'n Dead Trinket
* At 8 Challenges: HECKO-3 ECHO Theme
* At 12 Challenges: If Spooks Could Kill Character Skin
* At 15 Challenges: Ghoul Metal Grey Weapon Skin

The 2020 event rewarded the following:

* At 4 Challenges: A Shrinking Feeling Trinket
* At 8 Challenges: Message from Beyond ECHO Theme
* At 12 Challenges: Haunted Look Character Skin
* At 15 Challenges: Porphyrophobia Weapon Skin

TODO
====

* A set of Terror-anointment and Bloody Harvest gear-related hotfixes were
  activated [shortly before Bloody Harvest 2020](https://github.com/BLCM/bl3hotfixes/commit/8c6911ec1ad4c7446b416799ba7ba3fcf6215e90).
  I assume those will be a permanent part of the game, but I want to check
  up on it once the event is over, in case I need to pull anything from
  there into here.

Changelog
=========

**v1.1.0** - Oct 8, 2020
 * Cleaned up the mod in various ways:
   * Now generated via my Python utilities.
   * Exclude some changes which have been integrated into the main game since
     last year.
   * Rearrange the remaining statements and label everything properly
   * Make use of the `MatchAll` character syntax to reduce hotfix count
 * Split mod into 2019 and 2020 versions, to provide access to the different
   challenge reward sets.
 * Also rearranged this directory structure slightly, so each Timed Event Enable
   mod lives in its own directory.

**v1.0.0** - Sep 26, 2020
 * First versioned release
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

