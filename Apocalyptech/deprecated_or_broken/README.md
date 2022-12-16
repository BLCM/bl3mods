## Proofs of Concept

These are things that *work*, and I wanted to keep track of, but which
weren't actually intended to be mods themselves.

- `spawn_test.txt` - I just wanted to see if we could spawn enemy types in
  maps which don't ordinarily spawn them, and we can!  The test as-is is
  a bit broken and needs further development to be viable, but it worked
  well enough that I'm happy leaving it the way it is for now.
- `all_anointed.txt` - Just a test to turn all enemies (just in Covenant
   Pass) into Anointed.  Works fine, actually, but I have no plans to
   expand it beyond there.  There's a commented bit to turn all Covenant
   Pass enemies into Wotan instead, which is good for a laugh...
- `gun_randomizer.txt` - The file as-is just randomizes the barrel for
  the Cloud Kill SMG, and works pretty well, giving three random barrels
  to the gun.  No real plans to turn this into a real randomizer, just
  wanted to see if these kinds of shenanigans were possible.
  - As an aside, in order to survive a quit+reload, all of an item's
    parts have to come from the same "pool," which for weapons means
    a specific manufacturer+guntype.  So if you want gear that survives
    being put into a savegame, your options for randomization are
    somewhat limited.
- `mayhem_tweaks.txt` - Just playing around with the number and type of
  modifiers that get applied at various Mayhem levels, mostly just to
  verify that it could be done.  Works great!  I don't actually have any
  plans to do anything with 'em, though.
  - `mayhem_laffs.txt` - Mocking up a screenshot of a ridiuclous
    hypothetical Mayhem 20.  Bit o' fun is all.  (Though it does legit
    make Mayhem 10 into a nightmare.)
- `tiniest_tina.txt` - Made for a laugh after someone suggested online.
  Scales Tina down quite small, and renames her "Tiniest Tina."
- `hellwalker_to_purple_parts.txt` - Replaces the Hellwalker Balance/PartSet
  with the versions from a regular purple Jakobs shotgun.  Basically just
  wanted to see if the NamingStrategy object would still do the right thing,
  which it did.  This kind of thing could maybe turn into a mod of some
  sort eventually, though I have no immediate plans for it.
- `weapon_skin_swap.txt` - Makes the Ghoul Metal Grey user weapon skin actually
  use the Superstreamer's skin, if applied to a Tediore shotgun.  Just wanted
  to see if that was possible; no plans to turn it into a Real Mod.
- `achievement_shenanigans.txt` - I had the two co-op achievements left on
  Steam, and since I basically never do multiplayer, I decided to see if I could
  cheese 'em.  Turns out to be quite easy; just made them both depend on my
  SMG kill count, and set the target to one higher than that current stat from
  my save.  No plans to make this into a full mod, but if anyone else is
  interested, this is how you'd do it.
- `hatsoff_weapon.txt` - Just a joke mod.  During the intro to Bounty of Blood,
  a character named Old Pete starts making another character dance by shooting
  at his feet.  This changes his Jakobs gun into the Backburner, instead, for a
  laugh.
- `claptrap_gun.txt` - Makes the Smart-Gun XXL spawn Claptraps instead of
  spider turrets.  The Claptraps don't actually do anything interesting, though;
  they just stay in their spawned spot.  You can spawn other chars easily, of
  course, though enemies spawned this way will initially be on your team, and
  won't be able to harm you if they switch.  It's a bit weird.  Anyway, was kind
  of hoping to make a gun which would just generate more and more enemies
  against you, but the Team thing got in my way.  So a Claptrap gun it remains.
- `trivial_vc.txt` - Silly little mod to reduce the required quantity of Vault
  Card challenge targets to 1.  Don't really feel like officially making it a mod,
  but it *does* seem to work just fine.
- `droughts_eridium_moves.txt` - Similar to my mod-testing Droughts Chest Moves
  mod, this moves all small eridium piles in The Droughts to near the Highway Fast
  Travel location, and converts them all to the always-visible type.  Works fine,
  but it's pretty custom-purpose so it didn't seem worth making into an official
  mod, even as a "resource" type.
- `moodlock_*.txt` - Sets NPC dialogue "mood" to the specified value, which just
  affects their facial expressions.  I was hoping it would be more amusing than
  it is, but in the end it's kind of "meh," so I'm tossing it in here rather than
  doing a "real" release.
- `its_raining_skags.txt` - Repurposes the Eridium Cluster spawner in The
  Droughts to provide a rain of skags near the Highway fast travel.  I couldn't
  quite figure out having them *constantly* falling; they get to about 20 or
  so and then you need to kill one to get another to fall down.

## Deprecated/Testing Mods

- `mayhem_1_better_loot.txt` - This was my first mod attempt, actually,
  and improves the quality of drops in Mayhem 1 (not that it really needed
  it).  As I say, not really useful at all, but I've kept it here for my
  own historical interest.
- `mission_unlocks.txt` - This is actually partially successful; I can at
  least set mission reward pools here.  I'd hoped to also unlock Sanctuary
  with the first mission load, too, though, which didn't work.
- `datatable.txt` - Was used to test out how DataTable values interact with
  the rest of the BVC tuple - turns out that they probably override everything
  except for BVSC, which gets multiplied at the end as per usual.
- `always_scale_maliwan_takedown.txt` - Taken from the GBX event which
  set the Takedown to scale to the number of players.  This'll let you
  keep it that way forever, if you want.  Turns out that GBX decided
  to make that change permanent, so there's no real need for this one
  anymore.
- `bloody_harvest_disable.txt` - This can be used to disable Bloody
  Harvest prematurely.  It worked fine during the original event, but it's
  a bit pointless now because GBX added in an in-game toggle for that kind
  of event.  Still, keeping it around for awhile.
- `eridian_unlocks.txt` - Aims to eventually unlock all eridian equipment
  from the beginning of the game, though currently all it does is the
  Resonator.  Unlocking the Analyzer seems to be trickier, and the fact
  that there's some actual savegame editing which can unlock this gear
  properly, without any fuss, I'm moving the mod into this deprecated
  section.  Also, if I ever do figure out more, I'm almost certainly going
  to just fold it into Early Bloomer rather than release as a separate
  mod (which is, in fact, what I did with the Resonator).
- `guaranteed_cartel_operatives.txt` - Ups the probability of Cartel operatives
  (during the Revenge of the Cartels event) from 30% to 100%.  Works fine, but
  it's a bit much.  Never used it outside of a couple tests.
- `mayhem_level_cheats` - Some old Mayhem Mode cheats that I was using for
  quite awhile; namely restricting enemy scaling to 2x and forcing specific
  modifier configs for each level.  Since releasing my Mayhem Mode Configurator,
  though, this mod's kind of obsolete, and I grew to not really want this
  exact config anyway.  So, moving this over here as a deprecated mod.

I had a collection of timed-event-enabling mods publicly available prior to
the availability of B3HM as a modding tool.  Gearbox asked us to not do mods
which enabled those events, though, since they were still using them as
marketing tools, so we removed 'em from the repo.  As of the patch on June
24, 2021, though, GBX has added the ability to enable them at will directly
from the main menu (which I'd been expecting them to do eventually - yay!).
Anyway, I'm moving these mods back in here just for my own historical
packrattery, but they're not really useful anymore (and are possibly/probably
not even functional, given the new event framework).

- `timed_event_enable_bloody_harvest` - The event-enabler mod for 2019+2020 Bloody Harvests
- `timed_event_enable_broken_hearts` - The event-enabler mod for 2020+2021 Broken Heartses
- `timed_event_enable_cartels` - The event-enabler mod for 2020+2021 Cartelses

These mods were used for awhile for testing, and a few for doing some
Bloody Harvest farming, but they're basically now obsolete (or at least
I'll probably not use them again) with my Crader EM-P5 and Back Ham setup:

- `maggie_super_buff.txt` - Cheat mod which gives the Maggie an absurd
  amount of damage.  Mostly just used for testing mods where I don't want
  to deal with enemies.  Also turns the Maggie into an Infinity -- doesn't
  consume ammo.
- `backham_super_buff.txt` - Cheat mod which makes the Back Ham practically
  invulnerable.  It reports a 100% damage reduction, though that's not
  entirely accurate; some damage can and will get through, but it'll be
  quite minor.  Damage reduction is applied regardless of the direction it
  came from, contrary to what the card reports.  I was quite happy with
  this shield, but the 40% reflect chance often made it difficult to
  manage enemy damage when I was trying to test gear functionality, etc,
  so I switched to the Transformer instead.
- Bloody Harvest-related buffs (for getting the cryo challenge specifically
  done as easily as possible)
  - `stalker_super_buff.txt` - Used to take down Captain Haunt pretty
    quickly for the Haunt-specific challenge.  May as well use the Maggie
    buff until the final phase.
  - `westergun_super_buff.txt` - Probably the easiest way to get the cryo
    challenge.  Should tear through practically anything.  A few Mayhem
    3 modifiers stacked together can make it a bit less effective but it'll
    still perform extremely well.
  - `snowdrift_super_buff.txt` - Ended up not using it really, but it
    technically worked for the cryo challenge.
  - `whispering_ice_slight_buff.txt` - Compared to the other OP mods in
    this section, the buff is pretty slight here, but it's still more
    powerful than usual.  Went a bit overboard with the radius on the
    grenade; you'll probably get hit by it yourself occasionally.
- `hardcode_mayhem2_drops.txt` - On release, Mayhem 2.0 broke a lot of world
  drops, which was fixed in a hotfix a week later.  This mod fixed them up
  in the meantime.

## Failed Attempts

These are some mod attempts that I've yet to actually get working at all.  So
don't look at these thinking that they're any good.  :)

- `cdh.txt` - Just a quick attempt to see if `bDropOnDeath` still existed in
  item pools, even though it didn't look that it did.  Either it doesn't, or
  there's other problems with my attempts.  :)
- `faster_cost_spin.txt` - An attempt to get the cost spinner to resolve to
  the cost much more quickly, when mousing around items.  Not sure why this
  doesn't work, but I suspect that perhaps the object doesn't exist at the
  time that the hotfix executes?
- `no_delay_red_chests.txt` - An attempt to remove the 30-minute in-game
  delay between re-opening red chests.
- `bloody_harvest_challenges.txt` - An attempt to cheat the Bloody Harvest
  challenges to have lower target numbers.  Total fail!
- `guaranteed_badasses.txt` - A few little attempts to increase the number
  of Badasses.  Didn't do the trick, alas.
- `eridian_unlocks_full.txt` - A work-in-progress; the non-`full` version
  contains what I've got working so far (which is just the Resonator unlock).
  This has the start of Analyzer/Translator too, though it acts a bit weird.
- `golden_chest_costs_eridium.txt` - Just testing to see if I could get the
  Golden Chest to take Eridium instead.  Object/attr syntax is wrong somehow
  in here, and I don't really care enough to track it down.  Also the thing
  I'm trying to change might just be a visual thing anyway, so who knows.
- `better_vehicles.txt` - Was going to just be improving the hover mode for
  hover wheels, to be speedier all around.  The stuff I was trying wasn't
  working, though, so I've given up.  :)
- `deluxe_badass_combustor_unlock.txt` - Attempts to have the Deluxe Badass
  Combustor do its effects beyond level 10.  The object we need to modify is
  dead simple, but damned if I could get it to change.  Another time.
- `expanded_pt1_scaling.txt` - An attempt to allow all Normal/PT1/NVHM
  missions to have no max-level cap, which would have two effects: 1)
  Splinterlands and Carnivora would no longer suddenly be a cakewalk, and
  2) the game would scale all the way to 50, most likely, before the end
  of the campaign.  In the end, this approach didn't work, though.  Use
  `nvhm_gamestage_follows_level.txt` out in the main dir for a more
  nuclear option which happens to work.
- `longer_auto_pickup.txt` - There was a likely-looking var in `GameplayGlobals`
  which looked like it probably controlled the auto-item-pickup radius.
  This changes the value properly, but either it doesn't do what I thought
  it did, or something else also needs to change in order for it to work.
- `fix_enemy_loot_spawn_patterns.txt` - I wanted to fix the loot drop pattern
  for the Maliwan Slaughter bosses, but started with Mouthpiece instead, since
  he's many orders of magnitude easier to get to.  Anyway, no dice.
- `gen_faster_npcs.py` - DLC3 added a few NPCs who walk reaaal slowly, and I
  wanted to see if I could speed them up.  Started with Oletta (intending to
  test around the Lost and Found mission), but didn't get anywhere -- I think
  I have the right attribute to go after, but I haven't been able to figure out
  a correct hotfix syntax, so I don't know if that's right.  Anyway, giving
  up for now.
- `get_skill_tree_shenanigans.py` - This is actually partially working; was just
  playing with shuffling skills around, namely swapping Amara's Root to Rise
  with One With Nature.  My "preferred" method, which gives the most flexibility
  (can totally rearrange skill trees) doesn't work well enough to be generally
  useful -- skills lower than they "should" be won't be selectable ever, and
  skills higher than they "should" be have incorrect visual notifications.  The
  second method I tried does work, but would require that you keep the same
  "structure" as the vanilla tree.  You could swap skills around all you like
  (while making sure that the max-points and icon vars are moved too) but you
  wouldn't be able to rearrange the tree at will.
- `no_marcus_character_intros.txt` - An attempt to turn off the Marcus voiceovers
  as you cycle through your savegames (and presumably while selecting a new
  character).  As with my Better Vehicles attempt, though, the relevant objects
  get loaded dynamically and I've never figured out how to trigger a hotfix for
  that.
- `faster_vladof_mode_change` - This is sort of only half-failed...  Getting the
  mode-switch animations to complete faster is pretty easy, but I cannot for the
  life of me get the animations to *look* decent, and it bothers me enough that
  I'm not willing to "officially" release this thing.  Essentially the same problem
  that I have with the vehicle animations in my Mega Timesaver XL mod.  Pffffff.
- `always_visible_guardian_takedown_platforms` - Basically what it says: trying
  to make the platforms in Guardian Takedown visible all the time, instead of just
  some of the time.

Licenses
========

All Apocalyptech's code in here is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../COPYING.txt) for the full text of the license.

All Apocalyptech's mods in this repository are currently licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

