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
  - Brood Mother, in Pyre of Stars, looks like it's unaffected by this, alas.
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
  - Increases Eridium drop rates.
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
- `no_wasted_equipment.txt` - An improved version of my No Wasted COMs mod,
  this applies to COMs, Anointments, and Customizations as well.  Nicer than
  the BL2/TPS versions, since it should adjust properly even when players
  leave co-op, though note that it's completely untested in multiplayer.
- `movement_speed_cheats_reasonable.txt` and `movement_speed_cheats_extreme.txt` -
  Just what they sound like!  Move faster.  Also applies to Iron Bear and
  FL4K's pets.  Have not yet tested how this interacts crouching, FFYL,
  ladders, etc.
- `testing_loot_drops.txt` - A version of my modder's-resource mod that I
  use for testing out things like Expanded Legendary Pools.  All Standard-drop
  enemies will drop five items from the specified pool.

## Other mods

- `cheaper_sdus.txt` - Vastly reduce the SDU costs.  Cheaty, of course!
- `cheaper_slots.txt` - Reduce the cash slots cost to 20%.  The eridium slot
  machine is untouched since I did that in my `better_eridium_event.txt`.
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
- Some customization-related mods:
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
  - `customization_unlocks.txt` - Removes the preorder/deluxe/superdeluxe
    requirements for the relevant cosmetic items.  This does *not* actually
    spawn them in your game; you'll have to edit either `expanded_customization_pools`
    or `testing_loot_drops` to drop/enable them, if you don't already have
    them.
  - `customization_drops_*.txt` - Comes in three variants: `none`, `improved`, and
    `frequent`, and only affects the customization drop rate for "standard" enemies.
    The default is 0.5%; these mods change the rate to 0%, 3%, or 6%, respectively.
    `none` is useful if you already have all customizations and don't want to have
    them clogging up your Lost Loot machine.  `frequent` is useful for hunting down
    those last few you have yet to find (though even at 6% it'll probably take you
    ages to hunt them all down, if you're just relying on drops).
- `vehicle_unlocks.txt` - This unlocks most vehicle parts/skins as soon as
  the associated vehicle becomes available.  Note that wheel types aren't
  included here, since those are spawned a bit differently by the game, though
  I did add Monster Wheels to a few specific vehicles: Clever Girl, Festive
  Flesh-Eater, Skagzilla, and any Technical in Sandblast Scar.  Vehicles will
  pull from their full list of parts/skins when spawning (minus wheels), so
  variety is much increased, at the cost of stronger themeing per zone.
- `more_tracker_darts.txt` - I enjoy Atlas weapons, but I've found I basically
  never use them unless they've got the tracker darts part (as opposed to
  pucks or grenades).  So, I increased the weight of the tracker dart part,
  where possible, so that 75% of all Atlas equipment will have the darts.
- `always_visible_challenge_icons.txt` - Makes challenge icons (Claptrap
  salvages, Radios, etc) always appear on the map, regardless of if you've
  been close to them.  Does the same for Eridian Writings.  Note that you
  will miss dialog if you use this -- when entering a new map, only one of
  the available challenge intros will be played.  Note that this currently
  only supports the base game, not DLC1.  Known issues:
  - The third Typhon log in Meridian Outskirts
  - The Dead Claptrap in Neon Arterial might not show up immediately,
    though it does show up before there's been too much progression
    in the level.
  - A *bunch* of Legendary Hunts don't show up until you're right on
    top of them, for some reason.  Eden-6 and the second half of
    Pandora are especially finnicky about it for some reason:
    - Eden-6:
      - Floodmoor Basin
      - Anvil
      - Voracious Canopy
      - Ambermire
    - Pandora:
      - Devil's Razor
      - Splinterlands
      - Konrad's Hold
    - Nekrotafeyo:
      - The Pyre of Stars
  - The Target of Opportunity in Devil's Razor
  - Target of Opportunity in Cathedral of the Twin Gods
- `all_weapons_can_anoint.txt` - A number of weapons in the game can't
  ordinarily spawn with Anointments; this makes it so that they can.
- `eridian_unlocks.txt` - Aims to eventually unlock all eridian equipment
  from the beginning of the game, though currently all it does is the
  Resonator.
  - **NOTE:** This currently does have a couple weird side effects, namely:
    - Meleeing enemies will use the Resonator animation, though it
      continues to do damage as usual
    - You won't be able to attach the empty blood pack to Ace Baron, during
      the Meridian Outskirts mission "Healers and Dealers."
    - You won't be able to melee the varkid poop pile in Demon in the Dark,
      in Konrad's Hold
- `manufacturer_lock_*.txt` - Where possible, locks weapon drops to only
  the specified manufacturer (except for legendary/unique pools, which
  are left totally alone).  This also only touches pools in which the
  manufacturer actually exists, so if you load in the Atlas lock mod,
  you'll still get the usual range of shotguns, SMGs, and sniper rifles,
  for instance.  There's also a few instances of manufacturer-specific
  loot pools which haven't been touched.
- `always_scale_maliwan_takedown.txt` - Taken from the GBX event which
  set the Takedown to scale to the number of players.  This'll let you
  keep it that way forever, if you want.
- `first_gun_full_loadout.txt` - Modifies the opening chest in Covenant
  Pass, which ordinarily just gives you a white Vladof pistol, to give
  you two pistols, a grenade mod, a shield, a COM, and an Artifact.
  Obviously you'll need my Early Bloomer mod if you want to be able to
  use the COM and Artifact.  Also improves the second-gun chest to not
  be rarity/manufacturer-locked.
- `first_gun_testing_gear.txt` - Modifies the opening chest in Covenant
  Pass to contain a Crader's EM-P5 and a Transformer.  Also improves the
  second-gun chest to not be rarity/manufacturer-locked.

## OP Gear Mods

- `craders_emp5_super_buff.txt` - Cheat mod which gives Crader's EM-P5 an
  absurd amount of damage, infinite ammo, perfect accuracy/handling, and
  increased fire rate.  I started using this as my mod-testing gun to take
  advantage of its movement speed increase, though now that I've figured
  out how to do a proper movement speed mod, that effect isn't nearly as
  useful.  Still, it's a good testing gun anyway so I'll stick with it.
- `transformer_super_buff.txt` - Cheat mod which makes the Transformer
  practically invulnerable.

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
