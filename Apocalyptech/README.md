My BL3 Mod Workspace
====================

## Recreations of 10-Year-Anniversary Events

Check the `deprecated_or_broken` directory for some events which are
no longer found up here, because they don't play nicely with more
recent BL3 patches.

- `2019-10-15_-_10-year-anniversary-event-3_-_show_me_the_eridium.txt` - This
  is the Week 3 event, as sent by GBX itself, but with a few errors
  corrected.
- `2019-10-22_-_10-year-anniversary-event-4_-_mayhem_on_twitch.txt` - This
  is the Week 4 event, as sent by GBX itself.
- `better_rare_spawn_hunt_stripped.txt` - This is a stripped-down version of
  the Week 2 event which now *just* focuses on making sure that all rare
  spawns will spawn at 100% instead.  Also makes most of the vehicle rare
  spawns more common, with the exception of Skagzilla (though note that
  those just have an increased chance, not guaranteed).
- `better_eridium_event.txt` - This is a better (ie: OP and cheaty) version
  of the Week 3 event, which increases the Eridium drop rates even further,
  *vastly* reduces the customization costs at Earl's, and reduces the Eridium
  slot costs even further.
- `better_mayhem_on_twitch.txt` - This is a better (ie: OP and cheaty) version
  of the Week 4 event, which buffs up XP gains even more in Mayhem modes, and
  increases Anointed parts on drops even more (including in non-Mayhem).  All
  drops in Mayhem 3 should be Anointed.  This completely omits all of the
  Mayhem modifier statements and Twitch integration stuff from the vanilla
  Week 4 event, since I don't really care about those.

## BL3 versions of some of my BL2/TPS mods

- `better_loot.txt` - A *very* stripped-down version of Better Loot, not that
  BL3 really needs much in the way of better loot.  Does the following,
  currently:
  - Sets the rarity weights to be improved
  - Increases Eridium and Cosmetic drop rates.
  - Guarantees specific legendary drops from nearly all the bosses which
    have unique drops.  This has been updated for the Mayhem 4 / Maliwan
    Takedown patch, including all the new drops set up in that patch.
    Trials, Slaughters, and the Maliwan Takedown itself remain untested
    but everything else looks good
  - Unlocks Mayhem 4 drops for the named enemies as well.  Not sure if this
    unlocks world Mayhem 4 drops or not, but you can use `expanded_legendary_pools`
    for that.
- `early_bloomer.txt` - Unlocks all weapon types, elements, manufacturers,
  anointments, etc, from the very beginning of the game.  The main things I
  still haven't figured out is unlocking the Eridian Resonator and Translator,
  so those are still locked behind story progression.
- `expanded_legendary_pools.txt` - Adds all legendary/unique items into the main
  legendary drop pools, not that BL3 needs bigger legendary pools.  Includes
  all Bloody Harvest, Maliwan Takedown, Mayhem 4 items (which will drop
  regardless of Mayhem level, even in normal), and DLC1 items.
- `better_slots.txt` - Better results for slot machines.  A bit silly, but
  whatever.  Turns out there aren't any unique heads/skins/whatever to be
  had from them, so these just buff the gear.
- `testing_loot_drops.txt` - A version of my modder's-resource mod that I
  use for testing out things like Expanded Legendary Pools.  All Standard-drop
  enemies will drop five items from the specified pool.

## Other mods

- `cheaper_sdus.txt` - Vastly reduce the SDU costs.  Cheaty, of course!
- `cheaper_slots.txt` - Reduce the cash slots cost to 20%.  The eridium slot
  machine is untouched since I did that in my `better_eridium_event.txt`.
- `free_fabricator.txt` - This actually doesn't do what it *says* it does;
  it actually just spits out 10 Eridium bars, at a cost of 10 Eridium.
  Useful!  (Actually I suppose it *could* be useful to give Eridium to
  other co-op players.)
- `mayhem_1_better_loot.txt` - This was my first mod attempt, actually,
  and improves the quality of drops in Mayhem 1 (not that it really needed
  it).  As I say, not really useful at all, but I've kept it here for my
  own historical interest.
- `bloody_harvest_enable.txt`/`bloody_harvest_disable.txt` - These can be
  used to enable Bloody Harvest even after the event is over, or disable
  it prematurely.  The enabling script will also include the other balance
  hotfixes which were active during the last week(s) of the event, which
  includes health modifiers and other minor fixes.  These will almost
  certainly interfere with future events, if you happen to run 'em while
  they're active.
- `red_text_explainer.txt` - a BL3 version of Ezeith's BL2 mod.  Puts
  descriptions of weapon/grenade effects on the red text.  Shields, Artifacts,
  and COMs have been omitted since BL3 already lists those explicitly.
- `maliwan_charge_time.txt` - Improves the charge time of all Maliwan
  weapons except for Starkiller, Atomizers, and Melters, whose mechanism I
  haven't figured out how to tweak yet.  Pistols and SMGs get a 50%
  improvement, shotguns get 60%, and snipers will all be instant-fire.
- `guaranteed_ghosts.txt` - All enemies should be ghosts, and all "haunted"
  Urns and skull boxes in the Heck Hole will spawn a ghost.  Extracted from
  an official GBX hotfix deployed on Oct 31, 2019 and then extented a bit.
  Requires that the Bloody Harvest event be active, presumably.
- `no_slam_artifacts.txt` - Makes it so that non-legendary/unique slam-based
  artifacts never drop.  Did this because I am self-evidentally never going
  to work slams into my ordinary BL3 combat, and this way there's less
  junk gear to dispose of immediately.  Perhaps someday GBX will overhaul
  how slamming works in BL3.
- `expanded_customization_pools.txt` - Adds in nearly all customizations to
  the relevant global-drop pools (the ones omitted are for preorders, deluxe
  editions, or other ones which give you the item automatically), and
  increases the customization drop rate.  Slot machine rewards are unaffected.
- `only_heads_and_skins.txt` - Since I recently figured out how to spawn
  customizations properly, I ended up completing my collection of all
  non-character skin/head customizations, so this little mod just makes
  it so that those are the only customizations that spawn (apart from
  dedicated spawns, of course).  Probably of little use to other people
  Not Me.
- `vehicle_unlocks.txt` - This unlocks most vehicle parts/skins as soon as
  the associated vehicle becomes available.  Note that wheel types aren't
  included here, since those are spawned a bit differently by the game, though
  I did make Technicals in Sandblast Scar have Monster Wheels, so that there's
  a source for those in-game.  Vehicles will pull from their full list of
  parts/skins when spawning (minus wheels), so variety is much increased, at
  the cost of stronger themeing per zone.
- `more_tracker_darts.txt` - I enjoy Atlas weapons, but I've found I basically
  never use them unless they've got the tracker darts part (as opposed to
  pucks or grenades).  So, I increased the weight of the tracker dart part,
  where possible, so that 75% of all Atlas equipment will have the darts.

## OP Gear Mods

- `maggie_super_buff.txt` - Cheat mod which gives the Maggie an absurd
  amount of damage.  Mostly just used for testing mods where I don't want
  to deal with enemies.  Also turns the Maggie into an Infinity -- doesn't
  consume ammo.
- `craders_emp5_super_buff.txt` - Cheat mod which gives Crader's EM-P5 an
  absurd amount of damage, infinite ammo, perfect accuracy/handling, increased
  fire rate, and improves the movement speed buff.  I just moved to this as
  my mod-testing gun instead of the Maggie because I still haven't figured out
  how to increase character movement speed in general, but the EM-P5 already
  has that effect built-in.
- `backham_super_buff.txt` - Cheat mod which makes the Back Ham practically
  invulnerable.  It reports a 100% damage reduction, though that's not
  entirely accurate; some damage can and will get through, but it'll be
  quite minor.  Damage reduction is applied regardless of the direction it
  came from, contrary to what the card reports.
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

## Deprecated / Broken Mods

Check the `deprecated_or_broken` dir for various mods which either don't
work at all, or don't make sense anymore given more recent patches to
BL3 itself.

Constructing Mods With Code
===========================

As I've done with BL2/TPS in the past, I tend to like writing mods with the
assistance of code, and I've started to do so here as well, for a few of
the mods I've worked on.  That's stored in the `bl3hotfixmod` directory.
You can check out any of the files named `gen_*.py` to take a look at how
it works, but it's pretty straightforward.  Start off the script with:

    from bl3hotfixmod.bl3hotfixmod import Mod

    mod = Mod('filename_to_save.txt',
            'Mod Title',
            [
                'Extra description lines to show in the header, if you want.',
                'You can leave this as an empty list.',
            ],
            'HotfixPrefix',
            )

Then you can use a few shortcuts to build out the mod:

    # Puts a newline in the mod (for readability purposes)
    mod.newline()

    # Puts a comment in the mod (again, for readability)
    mod.comment('This is a comment line, will be prefixed by a #')

    # Puts a much more obvious comment in the mod, using three hash marks
    # with some "blank" comments above and below, to mark out main sections
    mod.header('This is a mod header line')

    # Same as above, but with a multiline header
    mod.header_lines(['Line 1 of a header', 'Line 2 of a header'])

    # Creates a regular hotfix
    mod.reg_hotfix(hotfix_type, package,
        object_name,
        attribute_name,
        new_value)

    # Creates a table-setting hotfix
    mod.table_hotfix(hotfix_type, package,
        object_name,
        row_name,
        attribute_name,
        new_value)

    # Closes out the mod properly
    mod.close()

For both `reg_hotfix` and `table_hotfix`, you can include an optional `prev_val`
named argument, if you want to have a hotfix only trigger if the current value
matches.  (ie: a `set_cmp` in BLCMM parlance)

For `hotfix_type` on either `reg_hotfix` or `table_hotfix`, you can use:

- `Mod.PATCH` - Will create a `SparkPatchEntry` hotfix
- `Mod.LEVEL`- Will create a `SparkLevelPatchEntry` hotfix
- `Mod.CHAR` - Will create a `SparkCharacterLoadedEntry` hotfix

Leave the `package` attribute as an empty string to leave that blank.
