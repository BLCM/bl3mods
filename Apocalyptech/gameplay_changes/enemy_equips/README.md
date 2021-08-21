Enemy Equips
============

This is a collection of mods which alter the weapons that most enemies
in the game have equipped.  The default equip pools for most BL3 enemies
are custom-built Balances which the game's AI is presumably well-suited
to using.  These mods switch those over to using various of the world-drop
pools instead, so there *should* be a greater variety of weapons being
used by enemies, though in some cases, the enemies won't really know how
to use the gear effectively.  For instance, an enemy with a Cutsman
sounds like a dangerous proposition, but it seems that the AI has a bit
of trouble aiming properly with it.

Note that enemies which have custom equip weapons already have *not*
been touched by this.  For example, Holder (in The Anvil) is set to use
a Fingerbiter -- he'll continue to do so.  Some bosses have *very*
custom weapons defined, such as a lot of the Eridian enemies, etc, and
those are also left alone.  Melee-only enemies, of course, are also
excluded.  See below for a list of elemental-weapon-locked enemies
who are also excluded, just 'cause it seems like too much work to
support that at the moment.

There are currently five variants available:

1. **All World Drops** - This is my own preferred version to use, and
   sets most enemies to pull from the main weapon drop pool.  This will
   mean an increased number of enemies who are using sniper rifles and
   heavy weapons, so watch out for that!  When used in conjunction with
   a mod like Better Loot, this will probably result in a harder game,
   since the average enemy weapon stats will likely be higher.  In
   Normal at low levels, it might actually result in an easier game --
   using Early Bloomer along with this mod is recommended, if you're
   using it in the early game.  Note that enemies who were already set
   to use Heavy Weapons or Snipers will continue to be locked to those
   weapon types, and Shotgun Tinks will continue to always have shotguns.
2. **Typelocked World Drops** - This is similar to All World Drops,
   except that enemies will still always have the same type of weapon that
   they would have ordinarily.  So SMG-using enemies will always still
   have an SMG, etc.  The notes about Better Loot, Early Bloomer, and
   sniper/heavy/shotgun-tink enemies apply here as well.
3. **Legendaries (all)** - Enemies will use legendary weapons.  Intended
   mostly as a joke, but might be fun anyway.  Recommended to use along
   with my Expanded Legendary Pools mod, for maximum Fun.
4. **Legendaries (typelocked)** - Enemies will use legendary weapons, but
   will always have the same type of weapon that they would have ordinarily.
   SMG-using enemies will only have legendary SMGs, for instance.  Also
   recommended to be used along with Expanded Legendary Pools.
5. **All The Shoddy** - Everyone uses The Shoddy.  Want to have a pretty
   darn easy time?  This is the one for you.

There are a handful of characters throughout the game who are set to
use elemental-locked versions of weapons, and at the moment I have not
touched any of them.  So these enemies will continue to have their usual
equipped weapons:
* Desperado Rider / Outlaw Rider
* Ethereal Malech
* Festering Goliath
* Honcho Rider / Hoss Rider
* Malech
* Poke Rider / Rustler Rider
* Roaster
* Sheega
* The Tenderizer

TODO
====

* Expand to include those elemental-locked weapons
* Possibly expand to include specific-enemy-use bosses?
* Might be fun to set weapon-using bosses to use one of the weapons that
  they drop, like BL2/TPS's Cold Dead Hands does.  I sort of doubt I'll take
  the time to do that, though, since CDH doesn't seem possible currently.
* Since I mentioned it already: I'd love to turn this into a fully-fledged
  Cold Dead Hands for BL3.  I suspect that the only way that'll ever happen
  is if we get a fully-working SDK, though, and even then it might be a
  longshot.

Changelog
=========

**v1.0.0** - Jun 18, 2021
 * Initial Release
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

