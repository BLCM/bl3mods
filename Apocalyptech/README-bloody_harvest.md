Farming Bloody Harvest Challenges
=================================

Cheater that I am, I was interested in figuring out a way to make getting
the Bloody Harvest challenges more quickly.  There are four challenge
rewards active during the event:

1. Weapon Trinket (at 4 challenge completions)
2. ECHO Skin (at 8 challenge completions)
3. Character Skin (at 12 challenge completions)
4. Weapon Skin (at 15 challenge completions)

Rewards 1, 2, and 4 only have to be redeemed once to get the reward
across all challenges, whereas 3 must be completed for every character,
since you only get the character skin unlock of the character who
unlocked it.

Many of the challenges are quite trivial -- you can get up to the
second reward unlock with very little effort, but a few of the other
ones are time-consuming.  So, how do we cheat?

The Easy Way: My "generate testing loot drops" mod
==================================================

I finally figured out how to add all customization types to loot pools, so
my loot drops script can generate all those items quite trivially.  If you
bring up the generation script, there's already a commented area which you
can uncomment to add the items to the drop pool.  For reference, though, here
are all the balances:

    /Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponTrinkets/_Shared/Trinket_League_BloodyHarvest_1.InvBal_Trinket_League_BloodyHarvest_1

    /Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_11.InvBal_ECHOTheme_11

    /Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_40.InvBal_CustomSkin_Beastmaster_40
    /Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_40.InvBal_CustomSkin_Gunner_40
    /Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_40.InvBal_CustomSkin_Operative_40
    /Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_40.InvBal_CustomSkin_Siren_40

    /Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01.InvBal_WeaponSkin_BloodyHarvest_01

Make sure they're in the list of balances to spawn, run the generation script,
add it into your `modlist.txt`, and then kill a few enemies to grab whatever
you're missing.

The Harder Way: Farming Bloody Harvest Efficiently
==================================================

This method actually just assumes that you're only going so far as
to get the character skins.  If you're trying to get the weapon
skin legitimately, I don't really know of any shortcuts for that
annoying 25-mission requirement.  Good luck with that!  But for
everything up to the character skins, read on:

Character Skins
---------------

To get to these, you'll have to get all but three challenges on four
characters.  The "hardest" ones (or at least the most time-consuming),
if you take into account my cheaty mods, are:

* Kill 500 Ghosts in Mayhem Mode
* Kill 150 Haunted Badasses
* Kill 20 Loot Ghosts
* Kill Captain Haunt 25 times

There's a number of ways you could theoretically go about making any
of those trivial:

* **Mod the target numbers to be lower** - I tried this and failed
  terribly.  You can check out my `bloody_harvest_challenges.txt` to
  see what I'd tried, but I couldn't get anywhere
* **Tie the target stats to something else** - When you do various
  things in the game, counters are incremented, and challenges will
  check versus those counters.  For instance I think the one for the
  Kill Captain Haunt 25 Times challenges uses something like `Kill_Haunt`,
  which theoretically goes up when you kill him.  If you could change
  the challenge to something like `Kill_Psychos` (or maybe change it
  so that killing a psycho increments `Kill_Haunt` instead), then
  that would trivialize many of these.  I looked into this a bit but
  I feel like I really need object dumps to know what to even try.
* For the Badass one specifically, **spawn more badasses**.  That would
  indeed be nice but I haven't been able to figure that out either.
* For the Loot Ghost one specifically, **spawn more loot ghosts**.
  As with Badasses, I just haven't been able to figure that out.

So, what we're left with is just making one of those as trivial as
possible, and it turns out that the "500 Ghosts in Mayhem Mode" is
about the best I can do at the moment.

So: The Method
--------------

Mods of mine that you'll want installed:

* `better_loot.txt` - Among other effects, this guarantees that all gear
  which *can* spawn with anointments does so.
* `better_rare_spawn_hunt.txt` - Not totally sure if this is required, but
  it'll make Rakkman, El Dragon Jr, Demoskaggon, and Borman Nates into
  guaranteed spawns, if they aren't already.
* `guaranteed_ghosts.txt` - Every enemy which can possibly be haunted
  will be haunted, and additionally every "haunted" urn and skull chest
  in the Heck Hole will spawn a ghost.  This helps the "500 Ghosts"
  challenge immensely.
* `maggie_super_buff.txt` / `westergun_super_buff.txt` / `stalker_super_buff.txt` -
  These trivialize the actual combat.  I use Maggie for general combat,
  Westergun when going for the cryo-kills-in-Heck-Hole challenge, and
  Stalker for taking down Haunt.  Note that for the "kill Haunt with a
  Bloody Harvest gun" challenge, you can technically use anything with
  a Bloody Harvest anointment on it; I hadn't realized that when
  initially choosing a loadout, so you may not need that.
* `gen_testing_loot_drops.py` - You'll use this to trivially spawn the
  specific cheat-buffed equipment you'll be using (namely: Maggie,
  Westergun, Stalker).
* If you want, I've also got buffs for the Whispering Ice grenade
  and the Snowdrift artifact, in case you wanted to use those for the
  cryo-kill challenge as well.

So, take a character, load `testing_loot_drops.txt` after generating it
with the loot you want, and go grab enough gear for your four chars.
Make sure your Westergun is ice, if you're using that.  Ideally only
pick up gear which has Bloody Harvest anointments on them.  You may want
to quit the game and come back in *without* using `testing_loot_drops.txt`
so your drops aren't completely boring from here on out.

Now, for each character:

1. Equip your loot.  If you're using the recommended Maggie/Westergun/Stalker
   combo and you made sure they have terror anoints, you've now completed
   the "equip three BH items at once" and "loot a BH legendary" challenges.
2. Talk to Maurice to start the quest
3. Make sure Mayhem Mode is active (level doesn't really matter, though I'd
   been doing it on Mayhem 3)
4. Head to Carnivora first, tear through everything with your Maggie, and
   pick up every instance of BH-anointed drops along the way.  You'll
   eventually have to drop a few bits of gear to make enough room to
   unlock the "loot 50 pieces of BH gear" challenge, which you should
   achieve by the time you get to the Tink dancehall.
5. Once out in the main Carnivora area, head over to Rakkman and kill him.
6. Then kill the other three haunted targets: El Dragon Jr (just to the
   left a bit at Jakobs Estate on Eden-6), Demoskaggon (a short vehicle
   ride over the ramp and to the left a bit in The Droughts on Pandora),
   and Borman Nates (around the corner to the left in Meridian Outskirts
   on Promethea, up on the elevated platform which spans the canal).
7. Head back to Maurice, enter Heck Hole.  Switch to your ice Westergun,
   and then "farm" the first area, right up to the skull puzzle, where
   you would ordinarily jump down into the blood lake.  When you get to
   the skull puzzle the first time, complete it quick so you don't
   forget.  Quit out to the main menu and hop back in *before* jumping
   down to the blood lake.
8. It'll probably take you 4 times to complete the "kill 100 haunted
   enemies in Heck Hole with ice" - you seem to get about 27 or so kills
   per run.  (Your Ghost Kill count will be racking up *much* higher,
   especially if you're opening skull chests and destroying haunted
   urns, which I'd recommend doing.)
9. Once you've gotten that, I'd recommend switching back over to the
   Maggie and going through a few more times to clean up the "kill 500
   ghosts in mayhem mode" challenge, since this initial area in Heck
   Hole seems to be the ideal place to spawn ghosts.  It's better than
   Trials, in my limited testing, mostly because you also get the
   guaranteed ghosts from urns and skull boxes.  I estimate you'll be
   doing a total of 6-7 runs through that initial bit to get you at
   least very close to the 500-ghost limit, including the runs where
   you were working on the cryo-kill challenge.
10. Once you're at 500 ghosts killed (or within 25 or so), jump down
    to the blood lake and complete the level.  If you've got a
    Terror-anointed Maggie you can probably just use that for the
    whole fight.  If not, you may as well use it for the first two
    phases and then switch to your Stalker for the last.  Killing
    Haunt with a BH gun should get you your 12th challenge, to
    unlock the skin.

So yeah, at that point the remaining challenges you've *not* done are
the 150 haunted badasses, 20 loot ghosts, and 25 Captain Haunt kills.
Whatever, you've already cheated your way to the weapon skin.

I didn't time it out explicitly, but I believe the process above takes
less than an hour per char, which feels like a pretty vast improvement
on doing it vanilla.  Still nowhere near as good as just spawning the
items directly with `gen_testing_loot_drops.py`, but if you don't mind
the Bloody Harvest combat then it's hardly a chore.

