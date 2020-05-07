My BL3 Mod Workspace
====================

## Enemy / Spawn Changes

- `guaranteed_rare_spawns.txt` - Guarantees that all rare spawns will spawn
  at 100%, and that most vehicle rare spawns are much more common (about 10%
  per vehicle spawn, in the maps which have them).  The non-vehicle part is
  actually unnecessary for the base game now, since GBX made that change
  permanent on their end.  This does include DLC2 rare spawns, though, which
  are not currently at 100% in vanilla.  A few things which don't work:
  - Brood Mother, in Pyre of Stars, apparently spawns based partially on how
    many mobs you've killed outside her lair?  Maybe just the Varkids?
  - Skagzilla's spawnrate is unaffected.

## Cheat Type Mods

Obviously many of the other mods *not* in this section could easily be considered
cheat mods, too, but this is more a bin where I can stick cheaty things which
don't fit cleanly into the other categories, or are more overt about their
cheatiness.  (Better Loot probably belongs in here, but I've stuck it in
Gameplay Changes instead.)

- `movement_speed_cheats_reasonable.txt` and `movement_speed_cheats_extreme.txt` -
  Just what they sound like!  Move faster.  Also applies to Iron Bear and
  FL4K's pets.  Have not yet tested how this interacts crouching, FFYL,
  ladders, etc.
- `always_visible_challenge_icons.txt` - Makes challenge icons (Claptrap
  salvages, Radios, etc) always appear on the map, regardless of if you've
  been close to them.  Does the same for Eridian Writings.  Note that you
  will miss dialog if you use this -- when entering a new map, only one of
  the available challenge intros will be played.  Note that this currently
  only supports the base game and partially DLC2.  DLC1 challenges are
  omitted entirely because they act weirdly.  Known issues:
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
  - All DLC1 challenges are omitted
  - Gaige's Gift challenges from DLC2 are omitted 'cause they act weirdly
  - Some Eldritch Statue challenges from DLC2 don't seem to work.
- `more_visible_echo_logs.txt` - Makes ECHO Log loot bars (and any other
  item using that bar, such as mission items) much bigger.  Used to
  hopefully catch any ECHOs I may have missed after a few playthroughs.
- `better_mayhem_rewards.txt` - This buffs up XP gains even more in Mayhem
  modes, and increases Anointed parts on drops even more (including in
  non-Mayhem).  All drops in Mayhem 3 should be Anointed.  Mayhem drop rates
  are otherwise identical to the Farming Frenzy event rates, which might
  actually be permanent now?  **TODO:** I believe that this is still in use
  and works fine after the Mayhem 2.0 release, and they've simply changed
  the levels at which these variables get applied.  I should test that out
  to be sure, though.
- `first_gun_full_loadout` - Modifies the opening chest in Covenant Pass to
  contain two pistols, a shield, a grenade mod, a COM, and an artifact,  You'll
  need to be using Early Bloomer to make use of the COM and Artifact, of course.
- `mayhem2_decreased_enemy_scaling.txt` - I really dislike bullet-sponginess,
  and would rather just have fun with the various Mayhem 2.0 modifiers without
  having to worry about optimizing DPS.  This severely cuts back on enemy
  health/shield/armor buffs in all Mayhem 2.0 modes.  **TODO:** I *would*
  actually like to figure out how to nerf Mayhem-enhanced weapons so that they
  don't become super OP, but I haven't figured that out yet.  I may end up
  adjusting this to suit, if I'm finding things too easy.
- `mayhem2_modifier_nerfs.txt` - I enjoy the Mayhem 2.0 modifiers in general,
  but I'd wanted to nerf a few of 'em down a bit.  I don't think these nerfs
  dramatically change how you'd approach any given set of modifiers, but it
  should make the tougher ones a bit less deadly.

## Gameplay Changes

- `nvhm_gamestage_follows_level.txt` - Makes the game follow your
  character level in Normal/PT1/NVHM, as it does during TVHM and Mayhem.
- `fix_dlc2_shield_drops.txt` - Most enemies in DLC2 (Guns, Love, and Tentacles)
  won't actually drop shields.  This fixes standard enemies but doesn't
  currently bother with badasses.
- `better_loot.txt` - A somewhat stripped-down version of Better Loot, not that
  BL3 really needs much in the way of better loot.  Does the following,
  currently:
  - Sets the rarity weights to be improved
  - Increases Eridium drop rates and quantities.
  - Guarantees specific legendary drops from nearly all the bosses which
    have unique drops.  This has been updated through the Mayhem 2.0 update.
  - Unlocks Mayhem 4 drops for the named enemies as well.  Not sure if this
    unlocks world Mayhem 4 drops or not, but you can use `expanded_legendary_pools`
    for that.
- `boss_drop_randomizer.txt` - Gets rid of all the specific boss drops,
  in favor of randomized loot.  After going through the game a few times
  with Better Loot I found myself using the same gear at various parts
  in the game, thanks to boss drops, so this'll keep me nicely randomized.
  I suspect I'm the only person in the world who'd want this, since I
  don't care about farming at all.  Basically intended to be used
  alongside my Expanded Legendary Pools mod, for best effect.
- `mission_reward_randomizer.txt` - Like the Boss Drop Randomizer, this
  randomizes all mission rewards to pull from the appropriate legendary
  pools instead of having fixed gear.  Customization rewards are
  left alone.  Recommended to be used with Expanded Legendary Pools.
- `dlc_loot_de-emphasizer.txt` - Both of the story DLCs so far (Moxxi's Heist
  and Marriage of Wainwright and Hammerlock) have had specific legendary drop
  pools which drop pretty frequently throughout their campaigns, so you see the
  same smallish pool of loot quire frequently (at least when using Better Loot
  or the like).  This largely takes away those specific drops in favor of
  the usual world drops.  Intended to be used alongside Expanded Legendary
  Pools.
- `vehicle_unlocks.txt` - This unlocks most vehicle parts/skins as soon as
  the associated vehicle becomes available.  Note that wheel types aren't
  included here, since those are spawned a bit differently by the game, though
  I did add Monster Wheels to a few specific vehicles: Clever Girl, Festive
  Flesh-Eater, Skagzilla, and any Technical in Sandblast Scar.  Vehicles will
  pull from their full list of parts/skins when spawning (minus wheels), so
  variety is much increased, at the cost of stronger themeing per zone.
- `mayhem2_no_drop_scaling.txt` - This nerfs the Mayhem 2.0 enhanced drop
  weighting so that Mayhem mode no longer provides any improved drops.  This
  is because in conjunction with Better Loot, it gets utterly absurd, and
  I'm honestly fine with the drops I get from Better Loot.  So, a rare
  example of a plain and simple nerf in one of my mods!

## Economy-related Mods

These are all quite cheaty.  Both cash and eridium-based economies basically
completely fall apart if you use all these, especially if Better Loot is also
being used, which gives you far more Eridium than usual.

- `cheaper_sdus.txt` - Vastly reduce the SDU costs.  Cheaty, of course!
- `cheaper_slots.txt` - Reduce the slot costs to 20% (both cash and eridium)
- `better_slots.txt` - Better results for slot machines.  A bit silly, but
  whatever.  Turns out there aren't any unique heads/skins/whatever to be
  had from them, so these just buff the gear.
- `cheaper_eridium_economy.txt` - Make Earl's cosmetics and Eridium slot
  costs cheaper.  Very cheaty.  (The eridium slot change is the same as in
  `cheaper_slots.txt`.)

## Gear Functionality Changes

- `red_text_explainer.txt` - a BL3 version of Ezeith's BL2 mod.  Puts
  descriptions of weapon/grenade effects on the red text.  Shields, Artifacts,
  and COMs have been omitted since BL3 already lists those explicitly.
- `maliwan_charge_time.txt` - Improves the charge time of all Maliwan
  weapons except for Starkiller, Ice Pick, D.N.A., Atomizers, and Melters,
  whose mechanism I haven't figured out how to tweak yet.  Pistols and
  SMGs get a 50% improvement, shotguns get 60%, and snipers will all be
  instant-fire.

## Partlocks / Part Changes

- `no_wasted_equipment.txt` - An improved version of my No Wasted COMs mod,
  this applies to COMs, Anointments, and Customizations as well.  Nicer than
  the BL2/TPS versions, since it should adjust properly even when players
  leave co-op, though note that it's completely untested in multiplayer.
- `early_bloomer.txt` - Unlocks all weapon types, elements, manufacturers,
  anointments, etc, from the very beginning of the game.  The main things I
  still haven't figured out is unlocking the Eridian Resonator and Translator,
  so those are still locked behind story progression.
- `expanded_legendary_pools.txt` - Adds all legendary/unique items into the main
  legendary drop pools, not that BL3 needs bigger legendary pools.  Includes
  all items from:
  - Bloody Harvest
  - Broken Hearts
  - Revenge of the Cartels
  - Maliwan Takedown
  - Mayhem 4 items (which will drop regardless of Mayhem level, even in normal)
  - Mayhem 2.0 items (which will drop regardless of Mayhem level, even in normal)
  - DLC1 (Moxxi's Heist of the Handsome Jackpot)
  - DLC2 (Guns, Love, and Tentacles)
- `all_weapons_can_anoint.txt` - A number of weapons in the game can't
  ordinarily spawn with Anointments; this makes it so that they can.
- `more_tracker_darts.txt` - I enjoy Atlas weapons, but I've found I basically
  never use them unless they've got the tracker darts part (as opposed to
  pucks or grenades).  So, I increased the weight of the tracker dart part,
  where possible, so that 75% of all Atlas equipment will have the darts.
- `more_elemental_weapons.txt` - Increases the odds of guns having elements
  on them; by default it's more likely to have not.
- `no_projected_shields.txt` - Makes it so that shields never spawn with
  the "Projected" augmenation.  I've actually sort of made my peace with that
  aug, and don't immediately trash any shield with 'em anymore, but it's
  definitely my least favorite still, so away it goes!
- `no_slam_artifacts.txt` - Makes it so that non-legendary/unique slam-based
  artifacts never drop.  Did this because I am self-evidentally never going
  to work slams into my ordinary BL3 combat, and this way there's less
  junk gear to dispose of immediately.  Perhaps someday GBX will overhaul
  how slamming works in BL3.
- `only_atlas_grenades.txt` - Non-legendary/unique grenades should always be
  Atlas.  Using this on my Zane, where all I really wanted were homing
  grenades.
- `gen_arbitrary_partlocks.py` - This is actually just an interactive
  CLI-based mod-generation script which, when given an item/weapon balance as
  the one argument, will let you choose parts to either partlock or exclude
  entirely.  This could've theoretically been used to generate my No
  Projected Shields or No Slam Artifacts mods, though this script was written
  after those two.  Very much an oddity; I didn't even really have a use case
  for it when I wrote it.

## Customization Tweaks

- `expanded_customization_pools_*.txt` - Expands the world drop customization
  drop pool, flattens the pools (so each customization is as likely to drop
  as any other) and increases the customization drop rate.  All versions omit
  the customizations you get via preorders, deluxe editions, etc, since those
  drops aren't useful to anyone.  Slot machine rewards are unaffected.  Comes
  in three variants:
  - `all` - Apart from the exceptions above, all customizations will world
     drop.
  - `no_mission_rewards` - Excludes the customizations you get as mission
    rewards.
  - `no_mission_rewards_or_earl` - Excludes the customizations you get as
    mission rewards, and the ones which can be found in Earl's machine.
- `customization_unlocks.txt` - Removes the preorder/deluxe/superdeluxe
  requirements for the relevant cosmetic items.  This does *not* actually
  spawn them in your game; you'll have to edit either `expanded_customization_pools`
  or `testing_loot_drops` to drop/enable them, if you don't already have
  them.
- `only_heads_and_skins.txt` - Since I recently figured out how to spawn
  customizations properly, I ended up completing my collection of all
  non-character skin/head customizations, so this little mod just makes
  it so that those are the only customizations that spawn (apart from
  dedicated spawns, of course).  Probably of little use to other people
  Not Me.
- `customization_drops_*.txt` - Comes in three variants: `none`, `improved`, and
  `frequent`, and only affects the customization drop rate for "standard" enemies.
  The default is 0.5%; these mods change the rate to 0%, 3%, or 6%, respectively.
  `none` is useful if you already have all customizations and don't want to have
  them clogging up your Lost Loot machine.  `frequent` is useful for hunting down
  those last few you have yet to find (though even at 6% it'll probably take you
  ages to hunt them all down, if you're just relying on drops).

## Manufacturer Locks

- `manufacturer_lock_*.txt` - Where possible, locks weapon drops to only
  the specified manufacturer (except for boss/miniboss/rare-spawn drops,
  which are left totally alone).  This also only touches pools in which
  the manufacturer actually exists, so if you load in the Atlas lock mod,
  you'll still get the usual range of shotguns, SMGs, and sniper rifles,
  for instance.  There's also a few instances of manufacturer-specific
  loot pools which haven't been touched.  Custom combinations of locked
  gear can be generated from the commandline.

## Timed Event Mods

Note that only one timed event can be fully active at the same time, so
the event-enabling mods here will interfere with each other.  It *is*
possible to combine some of their effects -- for instance, it's possible
to have both haunted enemies and hearts at the same time.  I haven't
put together a mod to do that, though, 'cause it hardly seems worth it.

- `bloody_harvest_enable.txt` - This can be used to enable Bloody Harvest
  even after the event is over.  It also includes the other balance
  hotfixes which were active during the last week(s) of the event, which
  includes health modifiers and other minor fixes.
- `guaranteed_ghosts.txt` - All enemies should be ghosts, and all "haunted"
  Urns and skull boxes in the Heck Hole will spawn a ghost.  Extracted from
  an official GBX hotfix deployed on Oct 31, 2019 and then extented a bit.
  Requires that the Bloody Harvest event be active, presumably.
- `broken_hearts_enable.txt` - This can be used to enable the Broken Hearts
  event after it's officially closed down.  Includes some related balance
  changes which were active during the event.
- `cartels_enable.txt` - This can be used to enable the Revenge of the
  Cartels event after it's officially closed down.  This includes a bugfix
  which was hotfixed along with the event launch.

## Main Menu

- `main_menu_*.txt` - Just a simple tweak to set the main menu to any of
  the known visual changes.  Right now that is: normal, Halloween,
  Christmas, and Cartels.  No actual gameplay changes or anything, it's
  pretty silly.

## Mod-Testing Mods

A collection of mods which I use primarily just when testing out other
mods.

- `craders_emp5_super_buff.txt` - Cheat mod which gives Crader's EM-P5 an
  absurd amount of damage, infinite ammo, perfect accuracy/handling, and
  increased fire rate.  I started using this as my mod-testing gun to take
  advantage of its movement speed increase, though now that I've figured
  out how to do a proper movement speed mod, that effect isn't nearly as
  useful.  Still, it's a good testing gun anyway so I'll stick with it.
  Also prevents EM-P5 from spawning with the x2 grip, since that causes
  ammo consumption again.
- `transformer_super_buff.txt` - Cheat mod which makes the Transformer
  practically invulnerable.
- `modtest_char_setup.txt` - Used to create a max-level character, with
  max-level starting gear (Crader's EM-P5 and Transformer), right at the
  very beginning of the game.  See the mod comments for specific info.
- `first_gun_testing_gear.txt` - Modifies the opening chest in Covenant
  Pass to contain a Crader's EM-P5 and a Transformer.  Also improves the
  second-gun chest to not be rarity/manufacturer-locked.
- `testing_loot_drops.txt` - A version of my modder's-resource mod that I
  use for testing out things like Expanded Legendary Pools.  All Standard-drop
  enemies will drop five items from the specified pool.
- `fast_levelling_*.txt` - Used to level up a character real fast.  Comes
  in three variants.  "Insane" will give you nearly a whole level per
  kill when you're approaching lvl 50 (and probably more when on low level),
  "Fast" will be a little more sedate, for fine-tuning purposes, but will
  still be a *lot* faster than base game, and "Faster" is inbetween the two.

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

```python
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('filename_to_save.txt',
        'Mod Title',
        [
            'Extra description lines to show in the header, if you want.',
            'You can leave this as an empty list.',
        ],
        'HotfixPrefix',
        )
```

Then you can use a few shortcuts to build out the mod:

```python
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
```

For both `reg_hotfix` and `table_hotfix`, you can include an optional `prev_val`
named argument, if you want to have a hotfix only trigger if the current value
matches.  (ie: a `set_cmp` in BLCMM parlance)

For `hotfix_type` on either `reg_hotfix` or `table_hotfix`, you can use:

- `Mod.PATCH` - Will create a `SparkPatchEntry` hotfix
- `Mod.LEVEL`- Will create a `SparkLevelPatchEntry` hotfix
- `Mod.EARLYLEVEL`- Will create a `SparkEarlyLevelPatchEntry` hotfix
- `Mod.CHAR` - Will create a `SparkCharacterLoadedEntry` hotfix
- `Mod.PACKAGE` - Will create a `SparkStreamedPackageEntry` hotfix
- `Mod.POST` - Will create a `SparkPostLoadedEntry` hotfix

Leave the `package` attribute as an empty string to leave that blank.  Note that
no official GBX hotfix has used `SparkStreamedPackageEntry` or
`SparkPostLoadedEntry` yet, and I've not yet been able to find a way to make use
of them (though I've only tried for `PACKAGE`, which I suspect might be required
to edit vehicle handling information).

The `bl3hotfixmod` package also includes a few convenience classes to help deal
with some commonly-used structures like `BaseValueConstant`-based stanzas and
`ItemPool` entries.  There's also a hash to turn level identifiers into their
English titles.  Look through the source for some more info on those, and grep
for their use in the mod-generation scripts for examples.

Data Introspection
==================

This project also includes a `bl3data` project which can be used to simplify
programmatic access to BL3 data, so long as you have it set up properly.  There
are two data sources the package can draw from:

1. Extracted BL3 data, using the technique [described by the BLCMods wiki](https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data#extracting-raw-datafiles).
   This will require that you run the extra script linked to by that page, so
   that the object files exist in the same directory structure that they live
   at while in-engine.
2. [The BL3 References database](http://apocalyptech.com/games/bl3-refs/) - the
   online version links to a MySQL/MariaDB database dump, which you'll have to
   import into your own MySQL/MariaDB database in order to use.  Alternatively,
   you can use [my refs-creation script](https://github.com/apocalyptech/bl3hotfixmodding/blob/master/dataprocessing/populate_refs_db.py)
   to generate the database from your already-extracted datafiles, though
   grabbing the provided SQL dump will almost certainly be quicker.

Of the two data sources, the first is required.  In order for `bl3data` to 
actually make use of the data, you also need to have a [JohnWickParse](https://github.com/SirWaddles/JohnWickParse)
binary available to do data serialization, and specifically you'll probably
want to use my own [indexed_arrays branch](https://github.com/apocalyptech/JohnWickParse/tree/indexed_arrays),
which includes some versioning information which `bl3data` uses to know if
it should re-serialize data.  You can use the main JWP project instead, but
the data library will re-serialize the data objects every time you run,
rather than intelligently using the previous data if possible.

The refs database is only needed if you want to use the `get_refs_to()` or
`get_refs_from()` methods, to look up references betwen objects.

As for usage, you'll probably find it most useful to just grep through this
project for examples.  The `dataprocessing` dir uses the library nearly everywhere,
and I've started using it for mod generation as well.  In short, though, here's
a couple of ways to use it:

```python
from bl3data.bl3data import BL3Data

data = BL3data()

poollist_name = '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss'

# boss_loot will contain a serialized version of the poollist.
# boss_loot[0] will contain the single export, of type `ItemPoolListData`
boss_loot = data.get_data(poollist_name)

# Loop through the pool list
for pool in boss_loot[0]['ItemPools']:
    print('Found item pool: {}'.format(pool['ItemPool'][1]))

# Get only `ItemPoolListData` exports specifically (in this case, no actual
# difference to just `get_data()`, `[0]` will still contain the single
# export)
boss_loot = data.get_exports(poollist_name, 'ItemPoolListData')

# Get export number 1 specifically (index `[0]`) -- the non-0-based-numbering
# is what's used by UE4 itself.  boss_loot[0] == listdata
listdata = data.get_export_idx(poollist_name, 1)

# Get references to the pool
object_names = data.get_refs_to(poollist_name)

# Get serialized objects which reference the pool
for object_name, data in data.get_refs_to_data(poollist_name):
    print('Found object: {}'.format(object_name))

# Find object names under `/Game/GameData/Loot` which start with `ItemPool_*`
object_names = list(data.find('/Game/GameData/Loot', 'ItemPool_'))
for object_name, data in data.find_data('/Game/GameData/Loot', 'ItemPool_'):
    print('Found object: {}'.format(object_name))

# Find objects by shell-like globs:
object_names = list(data.glob('/Game/GameData/Loot/ItemPools/Guns/*/ItemPool_*'))
for object_name, data in data.glob_data('/Game/GameData/Loot/ItemPools/Guns/*/ItemPool_*'):
    print('Found object: {}'.format(object_name))

# Look up data in a DataTable
cell = data.datatable_lookup(
        '/Game/GameData/Loot/ItemPools/Table_SimpleLootDropChances',
        'Eridium_Bar',
        'Drop_Chances_2_2811F91D40768DBD4FEBB791F8286836')

# Get the exact weight of a BaseValueConstant-based structure.
# Note that this will raise an Exception if it encounters data it doesn't
# understand yet, and right now it only supports very basic objects.  This
# will likely get better over time as I encounter more cases that I need
# to be able to process.
dumpster = data.get_data('/Game/GameData/Loot/ItemPools/ItemPool_Dumpster')[0]
for item in dumpster['BalancedItems']:
    print('Item weight: {}'.format(data.process_bvc_struct(item['Weight'])))
```
