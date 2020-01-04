## Deprecated Anniversary Event Mods

These are related to the 10-Year Anniversary events which took place shortly
after BL3's release.  With the November 21, 2019 patch (Mayhem 4 / Maliwan
Takedown), nearly all gear was given a dedicated source, which is slightly at
odds with the mods now found here.  Some bits of functionality from these have
been merged into Better Loot, though.

- `2019-10-01_-_10-year-anniversary-event-1_-_bonus_boss_loot.txt` - This
  is the Week 1 event, as sent by GBX itself.
- `better_bonus_boss_loot.txt` - This is a better (ie: OP and cheaty) version
  of the Week 1 event, which guarantees that all affected bosses will drop
  from their pools.
- `2019-10-08_-_10-year-anniversary-event-2_-_rare_spawn_hunt.txt` - This
  is the Week 2 event, as sent by GBX itself.
- `better_rare_spawn_hunt.txt` - This is a better (ie: OP and cheaty) version
  of the Week 2 event, which guarantees that all of the rare spawns will always
  drop their unique loot, and also removes the undocumented health buffs which
  are in the vanilla version.  Also theoretically makes any other rare spawn
  in the game which was *not* touched by this mod spawn with 100% frequency,
  though I'm not sure what else there is which might be affected by this.

## Deprecated/Testing Mods

- `mission_unlocks.txt` - This is actually partially successful; I can at
  least set mission reward pools here.  I'd hoped to also unlock Sanctuary
  with the first mission load, too, though, which didn't work.
- `datatable.txt` - Was used to test out how DataTable values interact with
  the rest of the BVC tuple - turns out that they probably override everything
  except for BVSC, which gets multiplied at the end as per usual.

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
- `movement_speed.txt` - An attempt to speed up character movement.  Didn't
  really expect this to work - I should give it another go.
- `no_delay_red_chests.txt` - An attempt to remove the 30-minute in-game
  delay between re-opening red chests.
- `bloody_harvest_challenges.txt` - An attempt to cheat the Bloody Harvest
  challenges to have lower target numbers.  Total fail!
- `guaranteed_badasses.txt` - A few little attempts to increase the number
  of Badasses.  Didn't do the trick, alas.
- `eridian_unlocks.txt` - Some attempts to unlock Eridian Resonator from the
  beginning of the game (would have gone on to the translator as well,
  had I figured this out)
- `torgue_full_auto.txt` - Tried to set Torgue ARs to full auto, but this
  didn't seem to do the trick (the version getting checked in actually tried
  to give them a 5-burst count).
- `golden_chest_costs_eridium.txt` - Just testing to see if I could get the
  Golden Chest to take Eridium instead.  Object/attr syntax is wrong somehow
  in here, and I don't really care enough to track it down.  Also the thing
  I'm trying to change might just be a visual thing anyway, so who knows.
- `better_vehicles.txt` - Was going to just be improving the hover mode for
  hover wheels, to be speedier all around.  The stuff I was trying wasn't
  working, though, so I've given up.  :)

