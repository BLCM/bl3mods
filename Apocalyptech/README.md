My BL3 Mod Workspace
====================

## Recreations of 10-Year-Anniversary Events

- `2019-10-01_-_10-year-anniversary-event-1_-_bonus_boss_loot.txt` - This
  is the Week 1 event, as sent by GBX itself.
- `2019-10-08_-_10-year-anniversary-event-2_-_rare_spawn_hunt.txt` - This
  is the Week 2 event, as sent by GBX itself.
- `2019-10-15_-_10-year-anniversary-event-3_-_show_me_the_eridium.txt` - This
  is the Week 3 event, as sent by GBX itself, but with a few errors
  corrected.
- `2019-10-22_-_10-year-anniversary-event-4_-_mayhem_on_twitch.txt` - This
  is the Week 4 event, as sent by GBX itself.
- `better_bonus_boss_loot.txt` - This is a better (ie: OP and cheaty) version
  of the Week 1 event, which guarantees that all affected bosses will drop
  from their pools.
- `better_rare_spawn_hunt.txt` - This is a better (ie: OP and cheaty) version
  of the Week 2 event, which guarantees that all of the rare spawns will always
  drop their unique loot, and also removes the undocumented health buffs which
  are in the vanilla version.
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
  BL3 really needs much in the way of better loot.  Just sets the rarity
  weights to be improved, and increases Eridium and Cosmetic drop rates.
- `early_bloomer.txt` - Unlocks all weapon types, elements, manufacturers,
  etc, from the very beginning of the game.  Does *not* unlock COMs and
  Artifacts, since those are locked by storyline progression (eventually
  I'll figure that bit out).  Note that this doesn't unlock Anointed drops,
  that's one other thing I haven't figured out.
- `expanded_legendary_pools.txt` - Adds all unique items into the main
  legendary drop pools, not that BL3 needs bigger legendary pools.
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
- `maggie_super_buff.txt` - Cheat mod which gives the Maggie an absurd
  amount of damage.  Mostly just used for testing mods where I don't want
  to deal with enemies.
- `mayhem_1_better_loot.txt` - This was my first mod attempt, actually,
  and improves the quality of drops in Mayhem 1 (not that it really needed
  it).  As I say, not really useful at all, but I've kept it here for my
  own historical interest.

## Failed Attempts

These are some mod attempts that I've yet to actually get working at all.  So
don't look at these thinking that they're any good.  :)

- `always_visible_challenge_icons.txt` - Some attempts to make challenge icons
  (Claptrap salvages, Radios, etc) always appear on the map, regardless of if
  you've been close to them.
- `cdh.txt` - Just a quick attempt to see if `bDropOnDeath` still existed in
  item pools, even though it didn't look that it did.  Either it doesn't, or
  there's other problems with my attempts.  :)
- `faster_cost_spin.txt` - An attempt to get the cost spinner to resolve to
  the cost much more quickly, when mousing around items.  Not sure why this
  doesn't work, but I suspect that perhaps the object doesn't exist at the
  time that the hotfix executes?
- `movement_speed.txt` - An attempt to speed up character movement.  Didn't
  really expect this to work - I should give it another go.
- `no_delay_red_chests.txt` - An attempt to remove the 30-minute in-game
  delay between re-opening red chests.

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

For `hotfix_type` on either `reg_hotfix` or `table_hotfix`, you can use:

- `Mod.PATCH` - Will create a `SparkPatchEntry` hotfix
- `Mod.LEVEL`- Will create a `SparkLevelPatchEntry` hotfix
- `Mod.CHAR` - Will create a `SparkCharacterLoadedEntry` hotfix

Leave the `package` attribute as an empty string to leave that blank.
