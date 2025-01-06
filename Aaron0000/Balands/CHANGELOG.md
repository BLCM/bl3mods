# DISCLAIMER: The numbers listed going from here down may not be 100% accurate in some cases. It may something like "Accuracy increased by 200%" but that doesn't mean it'll have an Accuracy of 200%+. Take the numbers with a grain of salt.

# CHANGELOG
------------------------------
1.6.7
-----
Fixed a typo in the change for the SNTNL Drone's search radius.

Fixed some inconsistencies between Mayhem 10 and 11's pet/vehicle damage.

1.6.6
-----
Made Hunter's eye mention that it is a Hunter skill.

Fixed the Kaoson still displaying accuracy and critical damage penalties on the weapon card.

Updated the Bounty Hunter class mod's description to be more accurate.

Updated Charged Relay's description to make it more clear that the Barrier must not be held in order to receive the bonuses.

1.6.5
-----
Seperated the Changelog from the Readme file and made it it's own file.

Fleshed out the descriptions for a lot of the Readme's weapon changes.

Fixed a typo in the Heavy Vehicle Armor stat changes.

Fixed an issue with Wildfire not being boosted to 10% chance correctly.

Made Full Can of Whoop Ass display the damage reduction it has.

Increased Auto Bear's self-destruct damage by 300%.

Increased Iron Bear's stomp damage (per level) by 250% (Basically meaning that low-level Iron Bear has the same stomp damage as before while high-level Iron Bear has stronger stomps.)

Added passive grenade regeneration to the Revengenader.

Added the Burning Summit as a drop to The Unstoppable to help mitigate the slog required to farm it.

1.6.4
-----
Adjusted the Loaded Dice to now actually affect the quality of loot obtained. White gear will be 50% less common, Green gear will be 30% less common, Purple gear will be twice as likely to drop, and Orange gear will be 30% more likely to drop.

Replaced the Luck stat on artifacts with Action Skill Duration since it did not actually work. Refrained from giving it the same treatment as the Loaded Dice due to issues with the calculation methods and leveling (kept producing too much purple gear if I tried to affect purple gear at all, and having it affect only white and green gear would be somewhat redundant in higher Mayhem levels where they already drop rarely.) The artifact prefix for Action Skill Cooldown is also changed to Refreshing while the Lucky prefix is changed to Long Lasting.

Fixed an issue with the Fire Rate/Reload generic anointment not reducing the time it takes to reload.

Fixed some issues with Red-Text Explainer involving the Pat SMGs and the Short Stick as well as the individual Red Text Explainer file not matching what was contained in the Complete file.

Adjusted the Devil's Foursum. Changed the damage type of the projectiles from shotgun to pistol, made the explosions no longer injure the user, and tightened the spread of the projectiles.

Significantly increased the damage of Baby Nukes. Unfortunately does not hold up in the later Mayhem Modes (Need to find a way to increase the damage of solely Baby Nukes without affecting other aspects of Moze/Iron Bear that use Action Skill Daamge.)

1.6.3
-----
(Attempted to) fix the Tr4iner class mod not activating upon every kill.

Added a replacer class mod for the Tr4iner since it seldom works and the effect is inconsequential. The replacer is called the "Fl4ktiv4tor":
	• It replaces the confusion ability with a 50% additive increase in Action Skill cooldown rate while heavily reducing the duration of most of Fl4k's Action Skills, intended to allow non-Rakk Attack Action Skills to activate certain anointments and skills more frequently.
	• Ferocity/Grim Harvest/Pack Tactics are swapped to Who Rescued Who/Rage and Recover/Head Count respectively.
	• Credit to tbj_quag for the idea.

Changed Moxxi's Endowment to now double all experience earned through combat (including boosts from other sources).

Removed the Naught replacer for Moxxi's Endowment from the main file and balancing file and included it as a seperate file in the newly added "Replacers" folder along with the Fl4ktiv4tor.

Fixed some loot drop issues with Gmork.

Fixed an incorrect reference for the Porcelain Pipe Bomb causing it to refer to the Red Queen for its damage. The actual damage number on the Pipebomb is unchanged.

Remade the previously made changes to the Sleeping Giant's post-reload buffs since it wasn't actually working. The post-reload damage buff is now 35%, the post-reload fire rate buff is now 35%, the post-reload critical damage buff is now 50%, and the previously attempted omni-buff chance change has been removed.

Changed Wooly Armor's 75% damage resistance into a 40% flat damage reduction.

Removed the "Nayhem" Mayhem modifier from the Balancing file. It can still be applied via the "Balands - Mayhem Mode Modifier Adjustments" file in the Quality of Life, Fixes, Etc. folder.

1.6.2
-----
Fixed a typo preventing the Semi-Auto mode of Auto/Single Dahl SMGs from receiving a damage buff.

1.6.1
-----
Fixed an issue for the "Less Extra Drops" files where a few enemies may not have been able to drop extra loot outside of Mayhem 10.

1.6.0
-----
Added a small chance for Manufacturer Rewards to deliver a (base game) Legendary item (Note for modders: Repurposes the unused Common manufacturer reward item pools for this.)

Tweaked how certain unique enemies dropped purple grenades to prevent ammo vending machines from having only a specific manufacturer of purple grenades on certain maps. (Note for modders: Repurposes an unused Pangolin grenade item pool for this.)

Reduced the chance of said enemies dropping a purple grenade from 50% (Road Dog)/ 75% (Tink Train, Lagromar, Crush Jaw, Blinding Banshee, Lt. Preston) to 20%/30% but added mayhem-scaled purple grenade drops in return.

Added elemental glows to the Corruption, Mutant, and Nukem to match their previously-changed elements.

Reduced the self-damage of the Pain is Power and Embrace the Pain by 50%.

Fixed Fast Hand(s)' presentation slightly.

1.5.9
-----
Added an item to the news section on the main menu to indicate Balands is active (Complete version and "Balance" files only.)

Fixed an issue with the S.F. Force again (accidentally deleted a previous portion of the fix at some point during a previous version.)

Reduced the strength of some of the animation speed increases in order to prevent items from spawning too low in relation to their container.

Removed "No More Loyalty Reward Notifications" from quality of life changes to re-enable loyalty rewards since it removed Loyalty Rewards to remove the notifications.

Replaced the unused manufacturer reward pools used for a few dedicated drops with other deprecated pools (Notes for Modders: replaced the previously used /Game/GameData/Loot/ItemPools/ManufacturerRewards/CoV/ItemPool_ManufacturerRewards_CoV_Common, /Game/GameData/Loot/ItemPools/ManufacturerRewards/CoV/ItemPool_ManufacturerRewards_Torgue_Common, and /Game/GameData/Loot/ItemPools/ManufacturerRewards/CoV/ItemPool_ManufacturerRewards_Tediore_Common with /Game/GameData/Loot/ItemPools/ItemPool_Creatures_Normal_DEPRECATED, /Game/GameData/Loot/ItemPools/ItemPool_Humans_Badass_DEPRECATED, and /Game/GameData/Loot/ItemPools/ItemPool_Humans_Normal_DEPRECATED)

Reduced Vehicle Mayhem Scaling by roughly 26%.

Lowered the variants of Jetbeasts' health closer to the health of the vehicles in the base game.

Vehicle weapons have been adjusted to be more on par with the default weapons instead of significantly worse for the most part (was unable to adjust the Jetbeast weapons).

Vehicle boosters have been diversified in terms of stats. Laser Wings/Jet Engine/Sonic Booster now have longer durations but slower recharge rates, while Firestarter/Toxic Booster/Thrust Turbine have lower boost duration but higher recharge rates and lower recharge delay.

Vehicle armor has been adjusted to actually have a downside instead of not actually reducing speed. It now increases Boost Consumption by 20%/30%/40% for Technicals/Outrunners/Cyclones and Jetbeasts respectively.

Added a file containing the previously mentioned vehicle changes to the "Individual Parts of Balands" folder.

1.5.8
-----
Fixed the "Complete Version" of Balands lacking the change that makes Boom Sickles spawn more often.

1.5.7
-----
Testing out taking some power from Violent Momentum and buffing some of Zane's other skills in return. Values are not final and are open to feedback (credit to Ancient_Rune for brainstorming these Zane changes.)

Changed Donnybrook's health regen from missing health to total health.

Increased Stiff Upper Lips' damage resistance to 10% per point and added Elemental Damage to the skill.

Increased Nerves of Steel's crit damage to 1.5% per point.

Increased Renegade's health regen to 1.5% per point.

Considerably reduced the gun damage curve on Violent Momentum for speeds past normal walking speed and made it stop counting as a kill skill (credit to Arin for the kill skill removal portion).

Fixed a typo in the Antifreeze's description.

Adjusted the weighting for health vials so that don't always drop from enemies even when you're at full health.

Added missing Red-Text Explainer to the Black Hole.

Updated the Void Rift's description.

Removed the Raging Bear changes that I left in the "Description Fixes" file by mistake.

Added the Weighted Ammo Drops to the "Qualifty-of-Life Adjustments" file.

1.5.6
-----
Renamed all of the files to automatically load in the correct order in OpenHotfixLoader instead of requiring the user to manually rename files (apologies, URL users.)

Added a file that allows you to lower the drop chance of Legendary gear from badass enemies, white/red chests, and vendors.

Added a file intended to be used with the previously mentioned file that reduces the amount of extra world drops added by the main Balands file or "Loot Adjustments" in the Trials, Circles of Slaughter, and Takedowns.

Added some variants of the "Dedicated Drop Source & Mayhem-Scaled Dedicated Drop Adjustments" files. One changes the amount of extra drops to only a single extra drop regardless of Mayhem level, another does the same but allows for the extra drops from the usual version if the drop source contains artifacts or class mods.

1.5.5
-----
Balands now has a collection of separate files apart from the original main file, for users to pick and choose what they prefer. This is largely divided into a file containing the balancing portion, and multiple files containing bugfixes, quality-of-life adjustments, and other miscellaneous options.

Removed the Smaller HUD and Animation-Speed-Up mods from the main Balands file and separated them into the previously mentioned individual files. Also added the Map Defogger from the Unofficial Community Patch as a separate file.

Removed the P.A.T. Mk. III from Spongeboss' dedicated drops since it has already been moved to General Blisterpus.

Made the Septimator and Septimator Prime's meteors' damage source be Sniper Rifle instead of Shotgun.

1.5.4
-----
Re-implemented the increased damage taken for player-controlled vehicles in Mayhem Mode. Player-controlled vehicles were taking too little damage relative to health. Open to suggestions on future changes for vehicles.

1.5.3
-----
Fixed Loco Chantelle not actually dropping Ember's Purge.

1.5.2
-----
Marginally increased the damage of Boomsday.

Fixed some incorrectly colored text in the description for Fast Hand(s).

Changed "multiplied by" for mayhem-damage scalars in Armored Infantry, Violent Momentum, Persistence Hunter, and Fast Hand(s) to "increased by" for clarity.

Fixed the Super Soldier still granting immunity.

Changed the Stop-Gap damage resistance to damage reduction.

Removed a duplicate line for Buttmunch's mayhem drops.

Added Mincemeat's dedicated drops to Buttmunch/Trufflemunch as mayhem-scaled drops due to being unable to apply it to Mincemeat directly.

1.5.1
-----
Fixed Boom. Enhance using the skill description for Cool Hand instead.

Fixed a typo preventing the Burn Both Ends skill description from being changed to match the actual effects.

Added Mayhem-scaled drops to Buttmunch after remembering it existed.

1.5.0
-----
Fixed the double barrel on the Shredifier not calculating damage appropiately (thanks to Lonemasterino for noticing this), changed the way the extra ammo cost is calculated on the Shredifier's double barrel to compensate for the loss in damage (an x2 Super Shredifier in double barrel mode will now only consume three ammo per shot).

1.4.9
-----
Re-added Mayhem scaling to vehicle damage. It increases by 65% per Mayhem level now.

Reduced the total health of Hemovorous' final form and Vermivorous by roughly 40%.

Reduced the total health of Captain Haunt by 50%, and his phylacteries by 80%.

Increased the damage of the Creeping Death by 12.5%, the magazine size by 2, and the fire rate by 40%.

Reduced the damage of the D.N.A's damage-over-time by 40%.

1.4.8
-----
Reduced the total health of Evil Brick, Evil Mordecai, Evil Lilith, Spongeboss, Locomobius, and Dr. Benedict by roughly 35% each.

Reduced the total health of the Seer by roughly 60%.

1.4.7
-----
Fixed From Rest's skill description not displaying the fire rate bonus.

Adjusted  Catharsis' description to no longer mention Action Skill cooldown since the cooldown was removed.

1.4.6
-----
Adjusted the Agonizer 9000's item drops. The Agonizer 1500 has been moved to a new item pool separate from the Agonizer 9000's regular dedicated item pools with a 50% chance to drop. The Crader MP-5 has been moved from the now-30%-chance-to-drop Damned/Loaded Dice/Crader's EM-P5/Backburner item pool to the Dictator/White Elephant item pool to further help reduce item pool bloat. (Note for modders; the Agonizer 1500 change modified the unused CoV white rarity gun pool for manufacturer rewards in order to produce a pool that only drops the Agonizer 1500 and nothing else.)

1.4.5
-----
Made it more likely for TK's Wave and the Tidal Wave to spawn with higher projectile counts.

1.4.4
-----
Made Trial bosses drop dedicated Class Mods for the player's current class more often (if they drop class mods for more than one class from their dedicated loot pool.)

Reduced Warty's mayhem scaled drops by half to account for his clone also being able to drop Warty's dedicated loot.

1.4.3
-----
Added Rachel the Anointed's item pool to Crushjaw as a separate drop in order to deal with not being able to directly adjust Rachel's pool. This newly-added item pool only activates during Mayhem mode and scales like most other Mayhem-scaled pools in this mod.

Added Muldock the Anointed's item pool to Turnkey Tim as a separate drop in order to deal with not being able to directly adjust Muldock's pool. This newly-added item pool only activates during Mayhem mode and scales like most other Mayhem-scaled pools in this mod. (Note for modders; this change modified the unused Tediore white rarity gun pool for manufacturer rewards in order to produce a pool that only drops the dedicated drops instead of mostly dropping regular gear)

Added Artemis' item pool to Indo Tyrant as a separate drop in order to deal with not being able to directly adjust Artemis' pool. This newly-added item pool only activates during Mayhem mode and scales like most other Mayhem-scaled pools in this mod. (Note for modders; this change modified the unused Torgue white rarity gun pool for manufacturer rewards in order to produce a pool that only drops the dedicated drops instead of mostly dropping regular gear)

Added the Brood Mother's item pool to Tyreen as a separate drop in order to deal with not being able to directly adjust Brood Mother's pool (without affecting certain enemies in the Cistern of Slaughter.) This newly-added item pool only activates during Mayhem mode and scales like most other Mayhem-scaled pools in this mod.

Fixed Explosive Punctuation not reducing Action Skill cooldown properly.

1.4.2
-----
Fixed the Trigger-Happy part boosting fire rate less than intended.

1.4.1
-----
Moved the purple Atlas grenade drop from General Traunt to Road Dog to prevent General Traunt/Blinding Banshee dropping the incorrect manufacturer of purple grenade assigned to them.

Made purple grenades always spawn with three parts.

Made regular Jakobs shotguns more likely to spawn with higher projectile counts.

Added the Mayhem 4 and Mayhem 6 exclusive gear to the regular legendary world drop pools (provided an appropriate Mayhem level is active.)

Added the Bekah, R.Y.N.A.H, Hunt(er), and Hunt(ress) to the regular legendary world drop pools.

Changed the previously added increased chance of Legendary loot in certain endgame activities to allow more focused world-drops similarly to the "Loot the Universe" events. Non-Takedown activities have been changed from increasing all ten types of non-cosmetic Legendary loot (six weapon types, shields, grenades, class mods, and artifacts) to boosting a specific type of loot. For example, if previously a specific Circle of Slaughter boosted all ten types of legendary gear drops by 100% each, it would now boost one type of legendary gear by 1000% (unless the drop chance has been further changed).

Replaced the 375% higher chance of all legendary loot in Trial of Survival with an x37.5 higher chance of legendary pistols.

Replaced the 100% higher chance of all legendary loot in Trial of Fervor with an x10 higher chance of legendary heavy weapons.

Replaced the 375% higher chance of all legendary loot in Trial of Cunning with an x37.5 higher chance of legendary sniper rifles.

Replaced the 375% higher chance of all legendary loot in Trial of Supremacy with an x20 higher chance of legendary shotguns.

Replaced the 1500% higher chance of all legendary loot in Trial of Discipline with an x150 higher chance of legendary assault rifles.

Replaced the 375% higher chance of all legendary loot in Trial of Instinct with an x37.5 higher chance of legendary SMGs.

Replaced the 100% higher chance of all legendary loot in Cistern of Slaughter with an x10 higher chance of legendary grenades.

Replaced the 100% higher chance of all legendary loot in Slaughterstar 3000 with an x10 higher chance of legendary shields.

Replaced the 66% higher chance of all legendary loot in the Slaughter Shaft with an x3 higher chance of legendary artifacts and class mods each.

1.4.0
-----
Fixed the Trial bosses not dropping three legendary class mods.

Fixed the Anarchy not dropping from Kukuwajack.

1.3.9
-----
Fixed the Shlooter spawning with four passive parts instead of three.

1.3.8
-----
Changed Blitz' melee bonus to be applied before skill and gear bonuses, increase the distance by 37.5%, and tripled the movement speed of Blitz.

Made Hemovorous always drop three pieces of her non-Company Man dedicated loot. Company Man drops separately from her regular dedicated item pool.

1.3.7
-----
Added Burst Fire Delay to most things that affect fire rate. Delay is reduced for things that increase fire rate (meaning shorter intervals), and increased for things that reduce fire rate (meaning longer intervals)

Added Repair Time to most things that affected reload speed.

Fixed the status effect anointments for Zane and Amara not actually factoring in gear and skills, made all of the status effect anointments also increase cryo rate.

Reintroduced Mayhem Scaling for Slide Damage. It increase by 6% per Mayhem Level, may be further adjusted after receiving feedback.

Reintroduced Mayhem Scaling for Slam Damage. It increase by 10% per Mayhem Level, may be further adjusted after receiving feedback.

Reintroduced Mayhem Scaling for Shield Damage. It increase by 24% per Mayhem Level, may be further adjusted after receiving feedback.

Reduced Pet Damage Scaling to 55% per Mayhem level from 70%.

Increased Attack Command cooldown to 15 seconds from 12 seconds.

Reduced the increased Legendary world drop rate of all Trials excluding the Trial of Fervor by 25%.

Reduced the increased Legendary world drop rate of all Circles of Slaughter by 33%.

Reduced the increased Legendary world drop rate of Maliwan Takedown by 40%.

Added additional opportunities to find dedicated loot to most dedicated loot sources in an effort to reduce farming tedium. This opportunity is based on Mayhem level, growing by 10% in chance (adjusted if multiple enemies have the same dedicated drops such as the Power Troopers) and 0.3 drops for every Mayhem level. At Mayhem 4 you will have a 40% chance of an extra drop, at Mayhem 7 it will be two 70% chances, at at Mayhem 10 or 11 it will be three guaranteed dedicated drops. 

Enemies that did not receive Mayhem-scaled drops due to technical reasons; Rachel the Anointed, Artemis, Mincemeat, Muldock the Anointed, and the Brood Mother.

Enemies that did not receive Mayhem-scaled drops due to already having sufficient drops; Trial bosses, Raid bosses, and Anathema.

Made the Null Pointer, Boo, Cloud Kill, Vibra-Pulse, Digby's Smooth Tube, Just Kaus, Acid Burn, Double Downer, Cure, Initiative, Seventh Sense, (purple) Love Drill, Firecracker, Peashooter, Quickdraw, Chalice, Bubble Blaster, Vendetta, Icebreaker, Beast (both elements), Core Buster, Splinter, Dakota, Company Man (Gravekeeper), Mysterious Amulet have drop sources.

Added Blue Fire's drop pool to King Gnasher in replacement of his Westergun drop as a viable farming source for Blue Fire's loot.

Added Red Rain's drop pool to Rohner as a viable farming source for Red Rain's loot.

Moved the Pearl of Knowledge from Eleanor to Kratch.

Added the P.A.T. Mk. III to General Blisterpus.

Added chances to get legendary Fustercluck DLC items from Spongeboss (General Blisterpus has the mayhem-scaled P.A.T. Mk III drops.)

Lowered the drop chances of Gigamind, Rampager, Atomic, Sylestro, Kritchy, Amach, Wendigo, and Eleanor since certain previously added unique items no longer drop directly from their loot pools.

Reverted the drop chances for Adelai Bronson, Ipswitch Dunne, Lani Dixon, Haddon Marr, Lasodactyl, Lectrikor, and Bellik Primis back to normal after having made certain uniques no longer directly drop from their loot pools.

Reverted the Seer's dedicated drop quantity back to normal as it interfered with the Mayhem-scaled drops that have been added.

Made Captain Haunt always drop three Bloody Harvest items.

Increased the odds of Loot Ghosts dropping Bloody Harvest loot.

Lowered the chance for additional drops on Joey Ultraviolet to 20%.

Lowered the world drop quantity of the Valkyries and made them always drop three pieces of dedicated loot.

Removed a portion of Scourge's money and eridium drops and replaced the eridium with a brick of 500 eridium to reduce the wait between the actual kill and main loot spawning.

Fixed Red Rain not dropping a 500-count eridium brick due to a previous update's changes.

Reduced Psychoreaver's health by roughly 40%.

Increased the damage of the Troubleshooter by 14%.

Reduced the damage of the Blade Fury's melee projectile by 25% and increased the bullet damage by 20%.

Reduced the recoil of Quasar (smgs), Polyaimorous, and Vibra-Pulse by 80%.

Increased the damage of the Devil's Foursum by 65%.

Increased the frequency of the Laser-Sploder's projectiles to 0.65 seconds from 0.85 seconds.

Reduced the vertical recoil of La Varlope by 35%.

Reduced the recoil of the Sickle by 15%.

Reduced the recoil of the Webslinger's primary firing mode by 20%.

Increased the damage of single-part and double-part novas to 50%/75% of a triple-part nova shield respectively.

Doubled the damage of the Stinger's novas (in-game description number doesn't change to reflect this.)

Reduced the cooldown of the Faulty Star's novas from 8 seconds to 2 seconds.

Reduced the Garcia's damage by 14%.

Reduced the Dakota's damage by 37.5%.

Reduced the D.N.A's damage by 50%.

Reverted the cooldown reduction on the Cmdl3t back to 6 seconds.

Adjusted the description of the Ice Spiker to mention that it counts as Amara's Action Skill damage.

Adjusted the description of the Bounty Hunter to be more accurate to the in-game effects.

1.3.6
-----
Increased the damage of the Elementalist's damage-over-time by 1750%.

Increased the radius of the Nuke grenade part from -10% per Nuke part to +23.45%.

Increased the suction radius of Singularity grenades by 80%.

Increased the suction radius of the Quasar by 47%.

1.3.5
-----
Fixed the MNTIS Cannon Damage anointment doing more damage than intended.

Adjusted the description of the Nimbus class mod to remove the damage number since it is useless and mention that the cloud inherits your weapon's damage-over-time damage value.

1.3.4
-----
Realized a less clunky way of applying Mayhem-scaled Action Skill damage to skills. It no longer renders action skill damage useless outside of Mayhem Mode or less effective than otherwise at lower Mayhem Levels. It has thus been moved to more commonly selected skills on each of the vault hunters (that have Action Skill damage scaling on a skill currently), and the percentages have been adjusted to have roughly the same damage before this update. 

Moved Zane's Action Skill Scaling to Violent Momentum. Action Skill Scaling is now 56.6% per point.

Moved Fl4k's Action Skill Scaling to Persistence Hunter. Action Skill Scaling is now 21.2% per point.

Moved Amara's Action Skill Scaling to Fast Hand(s). Action Skill Scaling is now 12% per point.

1.3.3
-----
Add "(Total)" in front of the Matched Set gun damage bonus to reduce confusion. The damage bonus doesn't display the damage increase per individual piece of matching gear, it displays the full bonus.

1.3.2
-----
Moved the Mayhem-scaled gun damage from Matched Set to Armored Infantry for two reasons. One, Armored Infantry is a more commonly selected skill and two, unlike the Mayhem-scaled Action Skill damage implemented on other characters this Mayhem-scaled gun damage does not penalize the user in any fashion so it being on a popular skill has no demerit.

Added a small (not Mayhem-scaled) gun damage bonus to Matched Set.

1.3.1
-----
Added Mayhem-scaled gun damage to Matched Set as a means of accomodating the loss of damage from Mayhem-scaled Skag Den/Big Surplus/Short Fuse. It does not increase in effectiveness based on how many items of a specific manufacturer you are wearing. It increases gun damage by 12% per Mayhem level and should be effective for 99% of guns.

Increased the effectiveness of Vampyr to 1% per point.

Increased the fire damage of Big Surplus to 10% per point.

Increased the fire damage of Cloud of Lead to 4% per point.

Reduced the fire damage of Fire in the Skag Den to 4% per point.

Reverted the damage bonus buff of Armored Infantry back to 3% per point, made it global damage instead of gun damage.

Made the damage bonus of Tenacious Defense global damage and made the damage bonus factor in skill and gear boosts.

Reduced the maximum damage bonus of Click, Click... to 50% and made it factor in skill and gear boosts.

Reduced the cooldown bonus of Explosive Punctuation to 5% from 8%, made the cooldown bonus factor in before skill and gear boosts, and added bonus movement speed.

Increased the amount of sniper rifle ammo given by SDUs by 3 additional ammo per SDU.

1.3.0
-----
Endgame activities (Trials, Circles of Slaughter, and Takedowns) have been given an increased chance to world-drop Legendary gear. For comparison's sake, "Loot the Universe" increased the chance of Legendary loot by 2000%.

Increased the amount of Legendary item drops in the Trial of Survival by 375%.

Increased the amount of Legendary item drops in the Trial of Fervor by 100%.

Increased the amount of Legendary item drops in the Trial of Cunning by 375%.

Increased the amount of Legendary item drops in the Trial of Supremacy by 375%.

Increased the amount of Legendary item drops in the Trial of Discipline by 1500%. (The enemies here were particularly stingy with drops.)

Increased the amount of Legendary item drops in the Trial of Instinct by 375%.

Increased the amount of Legendary item drops in the Cistern of Slaughter by 100%.

Increased the amount of Legendary item drops in the Slaughter Shaft by 66%.

Increased the amount of Legendary item drops in Slaughterstar 3000 by 100%.

Increased the amount of Legendary item drops in the Maliwan Takedown by 300%.

Increased the amount of Legendary item drops in the Guardian Takedown by 800%.

Gave the singing fish found throughout the Guns, Love, and Tentacles DLC a small chance of producing a Fish Slap.

Improved the loot drops of Godliaths.

Fixed some typos in the loot changes for Anathema, Scourge, and Hemovorous. They should now drop more of their specific loot.

1.2.9
-----
Fixed the Star Helix not consuming two ammo per shot when a secondary firing mode is active.

1.2.8
-----
Exchanged the Ten Gallon in GenIVIV's loot pool with the Messy Breakup from Rax.

Made the Messy Breakup and Band of Sitorak always spawn with maximum parts. Messy Breakup additionally is now more likely to spawn in shock element compared to before.

Fixed the Rough Rider not always spawning with maximum parts.

Made the Hunter-Seeker, Hex, and Quasar more likely to spawn with extra parts.

Made the Hunter-Seeker, Hippity Hopper, Surge, and Lightspeed more likely to spawn in elemental versions.

1.2.7
-----
Fixed a typo in the adjustment for the Shlooter that is supposed to make it always spawn with three stat bonuses. It should now work properly.

1.2.6
-----
Updated the red-text explanation for the Crader's EMP-5 and Proprietary License slightly.

Adjusted the Aesclepius' status effect damage reduction to be far more effective and updated the description slightly.

Fixed the Polyaimorous' secondary firing mode not receiving proper damage bonuses.

1.2.5
-----
Reverted the damage buff on the Messy Breakup to prevent certain builds from violently destroying game content with an army of superpowered drones. Will see if the amount of drones active can be limited in the future.

1.2.4
-----
Fixed the Rakk Commander not actually increasing Rakk count by 3.

Fixed Torgue Cross-Promotion not boosting Splash Damage by 7% per point.

Made the Shlooter always spawn with maximum bonus stat parts after the first redemption.

Made the following grenades always spawn with maximum parts; Fish Slap, Firestorm, Tran-fusion, and Widowmaker.

Made the following grenades more likely to spawn with extra parts; Ghast Call, Ringer, and Epicenter.

Made the Widowmaker more likely to spawn with an element.

1.2.3
-----
Fixed some base weapon type and standard weapon barrel stat changes not applying to secondary firing modes.

Fixed the pet bonuses for Fl4k's Jabbers not displaying the increase in percentage they should display when Barbaric Yawp is invested into.

1.2.2
-----
Fixed the Spiderant Scorcher and Spiderant Countess not having all of their pet bonuses being displayed on the info card.

1.2.1
-----
Reduced the projectile speed of TK's Wave and the Tidal Wave. They're now 25% faster than TK's Wave would be in normal gameplay.

Increased the projectile damage of the Psycho Stabber.

Increased the melee damage of the Ionic Disruptor to 200%.

1.2.0
-----
Made the Company Man always spawn with three (non-manufacturer) passive stat bonuses.

1.1.9
-----
Added Action Skill damage Mayhem Scaling to a few skills for Zane, Fl4k, and Amara. Investing one point into these skills enables your Action Skill damage to scale with Mayhem levels. Be warned that if you have a point in one of these skills and don't have Mayhem mode activated, your Action Skills don't deal any damage due to how it calculates the damage. It was done this way to prevent Iron Bear and Iron Cub from destroying the universe, as well as being able to manually adjust the boost for each Vault Hunter. Mayhem 11 will end up having slightly more Action Skill damage bonus, but you can simply roll for four "Nay-hem" modifiers on Mayhem 10 if that bothers you.

Added Action Skill damage Mayhem Scaling to Praemunitas. It increases by 50% for every Mayhem level.

Added Action Skill damage Mayhem Scaling to Self-Repairing Systems. It increases by 25% for every Mayhem level.

Added Action Skill damage Mayhem Scaling to Root to Rise. It increases by 20% for every Mayhem level.

Added notes in the skill descriptions for the following skills/augments to indicate they receive Mayhem Scaling:  Best Served Cold, Binary System, Doppelbanger, Dominance, Success Imminent, Lethal Force Authorized, Remnant, Indiscriminate, Catharsis, Do Unto Others, Revelation, Unweave the Rainbow, Body and Mind, and Free the Soul.

Increased the Digi-Clone's damage by 15%.

Increased the damage of the SNTNL's machine gun, Bad Dose, and Static Field by 20%.

Increased the damage of Boomsday by 80%.

Increased the damage of Almighty Ordinance by 113%.

Increased the Digi-Clone's base health to 39% higher than normal game values.

Increased the base damage of Rakk Attack to 80% stronger than normal game values.

Increased the cooldown on Attack Commands to 12 seconds.

Increased the damage of Success Imminent by 150%.

Increased the base health of Fl4k's pets by 40%.

Tripled the base damage of Fl4k's pets.

Doubled the base damage of the Jabber pets' weapons.

Re-enabled Pet Damage Scaling in Mayhem Mode and added the Mayhem Level multiplier to the pet descriptions, at +70% per Mayhem Level.

Reverted previous damage buffs to the Great Horn Skag and Eridian Skag Attack Commands.

Reduced the damage of the Gunslinger Jabber's Attack Command by 30%.

Reduced the damage of the WAR Loader's Attack Command by 20%.

Increased the base damage of Phasecast to 150% stronger than normal game values.

Increased the base damage of Reverbration to 79% stronger than normal game values.

Increased the base damage of Deliverance to 145% stronger than normal game values.

Increased the base damage of Tandava to 154% stronger than normal game values.

Increased the base damage of Phaseslam, Fracture, and Downfall to 215% stronger than normal game values.

Increased the base damage of Phaseflare to 51% stronger than normal game values.

Increased the base damage of Glow Up to 55% stronger than normal game values.

Increased the base damage of Shooting Star to 91% stronger than normal game values.

Increased the base damage of Light Fantastic to 47% stronger than normal game values.

Reduced the damage of Body and Mind to 50%.

Increased the damage of Free the Soul to 7 times higher than normal game values.

Heavily reduced the health scaling for enemies in Arms Race.

Reduced the damage of Diadems in Scourge the Invincible's fight by 75%.

Fixed Dahl SMGs not receiving a damage bonus in semi-automatic firing mode.

Reduced the fire rate of burst-fire mode on Dahl SMGs to compensate for the increase base fire rate on Dahl SMGs. 

Increased the melee damage bonus of the Psycho Stabber to 250%.

Increased the melee damage bonus of the Ripper to 200%.

Made the description on the Anarchy more accurate.

Reduced the damage of the Blade Fury's bullet damage by 25%, reset the projectile's melee damage to original values.

Removed the increased animation speed for the animation of exiting a vehicle as the driver to prevent running over yourself with your own car.

Reduced the O.P.Q-System's fire rate by 56%.

Made the following shields always spawn with maximum parts; Beskar, Snowshoe, Gas Mask, Infernal Wish, Old God, Recharge-Berner, Re-Volter, Red Card Recharger, Rico, Rough Rider, Super Soldier (but not the first time you redeem one), Torch, Version 0.m.

Made the Rough Rider no longer spawn with "none" parts.

Reduced the maximum bonus of the Flesh Melter's corrosive damage bonus. Now reaches 25% at level 72.

Reduced the Phasecast damage anointment to 75%.

Reduced the Phaseslam damage anointment to 100%.

Reduced the Phaseflare damage anointment to 75%.

Increased the Terror Cryo damage anointment to 50%.

1.1.8
-----
Experimenting with increasing the damage on Action Skill and pets. Not confident with releasing them in their current state however.

Changed Monkey Do's amp damage to say 86% instead of 81%.

Fixed a typo preventing the Butcher from doing damage.

Fixed an issue with the MNTIS damage anointment doing double the listed damage.

Increased Face-puncher damage to slightly above game-launch levels.

Removed the damage penalty on the Unleash the Dragon.

Increased Armored Infantry's damage bonus to 5% per point.

Increased Torgue Cross-Promotion's splash damage bonus to 7% per point.

Increased Scrappy's damage bonus to 7% per point.

Increased the radius of the Stinger's novas by roughly 43%.

Increased the Dowsing Rod's damage by 15%.

Increased the Faisor's damage by 15%

Increased the Flipper's damage by 35%.

Increased the Prompt Critical's damage by 25%.

Increased the Unkempt Harold's damage by 10%.

Increased the Ogre's damage by 10%.

Reduced the base damage of the Guardian 4N631 by 30% and increased the special effect to 120% maximum.

Reduced the damage on the Ember's Purge by 9%, increased the damage of the puddle from 33% to 50%.

Reduced Body and Mind damage by 25%.

Reduced the Reflux' damage by 25% and reverted the ammo cost back to one.

Reduced the Sand Hawk's damage by 37.5%.

Reduced the critical hit damage bonus on the Executor to 50%.

Added action skill damage to Synchronicity.

Added a small accuracy and handling bonus to Boom. Enhance.

Made Violent Momentum display the Slide Damage bonus.

Adjusted the Naught. The instant recharge has been reduced to a 75% recharge delay reduction, and a 50% recharge rate penalty has been added. This has been done to prevent issues with certain shields such as the Mana Well.

1.1.7
-----
Removed the Monarch's increased bipod-mode movement speed penalty to prevent issues with the movement penalty sticking around after switching weapons.

Reduced Cold Bore's bonus cryo damage to 10% per point.

Fixed the Crader EMP-5 doing a lot more damage than intended.

Increased the damage of the Butcher by 41%.

Increased the Fade Away damage anointment to 40% and adjusted the text on the Gravity Snare damage anointment to 40%. The Snare anointment uses the Fade Away damage anointment for the damage value and I have yet to figure out how to fix it.

Adjusted the Gamma Burst radiation damage anointment's description to be more accurate.

Tripled the speed of the Web Slinger's projectiles. Fixed the Web Slinger underbarrel having two projectiles instead of one and increased the damage of the underbarrel to 50 from 20.

Made the Ward always spawn with maximum Roid parts.

Made the Trial bosses drop three legendary class mods when they would normally drop one.

1.1.6
-----
Added in the smaller HUD from the Unofficial Community Patch and added a separate version of Balands to Github/Nexus that does not include the smaller HUD.

Increased Fire in the Skag Den's fire damage to 5% per point.

Increased the duration of the Phasecast-Weapon Damage anointment to 10 seconds.

Added a 50% bonus to slide damage to the Vanquisher.

Updated a few more Red-Text descriptors.

1.1.5
-----
Improved the rate of experience gain in Mayhem Mode by 1.5 times (50% higher) for each Mayhem level.

1.1.4
-----
Fixed the Action Skill End Badass/Boss Damage anointment having more damage than intended.

Updated Juliet's Dazzle description slightly to mention that the projectiles penetrate and ricochet.

1.1.3
-----
Adjusted some Red-Text Explainer descriptions for accuracy and removed redundant explanations for gear that already included a description on the card.

Adjusted Bloom, Frequency, Robin's Call, and Unseen Threat descriptions slightly.

Removed the ricochet text on the Stonethrower.

Replaced Forge with Redistribution on the Green Monster, restored the unlisted splash effect and updated item description to be more accurate. Turns out that giving items like the Sand Hawk excessive ammo regen without a timer isn't very healthy for balance.

Fixed the Good Juju's secondary firing mode dealing less damage than it should.

1.1.2
-----
Updated to include Unofficial Community Patch version 1.0.1.

Added the newest version of Apocalyptech's Red Text Explainer.

Fixed an issue with the Kill-o'-the-Wisp where the ammo cost was connected to the damage table instead of the actual damage attribute. Increased the Wisp's damage by 25% and fixed the Wisp's ammo cost to be 3.

Fixed Vosk's Deathgrip's description to say it is four seconds instead of six.

Made the Spade fully-automatic and reduced the fire rate by 50%.

Removed the increased weighting on legendary class mod drops from Jack-Bot since class mods now more heavily favor dropping for your current Vault Hunter due to UCP implementation.

1.1.1
-----
Implemented most features from the Unofficial Community Patch (for Borderlands 3) other than Red-Text Explainer and Smaller HUD that weren't already included in Balands. This means you do not need to run the Unofficial Community Patch at the same time as Balands.

Slightly adjusted the duration of the following anointments: Clone-Swap weapon damage, Phasecast weapon damage, and Attack Command movement.

Removed Legendary gear (that isn't a quest reward) from Earl's Black Market and replaced the Item of the Day with a guaranteed Alien-Barrel weapon due to Legendary gear being too cheap in the beginning of a playthrough. This change will hopefully be reverted in a future update after adjusting the prices in Earl's vendor.

Buffed the damage of the Kyb's Worth by 35%.

1.1.0
-----
Reverted the Body and Mind changes.

Reverted the replacement of Violent Tapestry to Alacrity on the Stone.

Added splash notes to Tandava, Fist Over Matter, Fracture, Downfall, Glow Up, Shooting Star, and Light Fantastic.

Reduced Fracture cooldown to 22 seconds.

Made the lifesteal anoint actually display 1.5% instead of rounding up to 2%.

Reverted Devil's Foursum projectile speed increase and lowered splash radius to 245 from 275.

Increased Downfall's flight speed by 25%.

1.0.9
-----
Fixed the Health Regen anointment using the incorrect item to get the percentage displayed for how much health-per-second is regained, and buffed the value to 8% per second.

1.0.8
-----
Replaced the grenade capacity on "Why Can't I Carry All These Grenades" with grenade regeneration.

Increased the DE4DEYE's high-health damage bonus to 50%.

Increased the low-health threshold of the Low-Health damage anointment to 50%, lowered the damage bonus to 60%.

1.0.7
-----
Reverted most of the changes to the Flakker's explosions. It now shoots out slightly further away while accelerating slightly slower than normal. Damage has also been adjusted slightly.

1.0.6
-----
Fixed The Iron Bank and Praemunitus not decreasing the heat rate of COV weapons and made them display the heat reduction on the skill card.

Made Deep Well display the heat reduction on the skill card.

1.0.5
-----
Adjusted Forceful Expression's description to be more accurate to its actual effects.

Halved Do Harm and Violent Tapestry's maximum stacks to 50 and doubled the efficiency of each stack.

Increased Clear the Mind's duration to 12 seconds.

Garcia - Increased damage by 24%, lowered ammo cost to 1, increased projectile count by 2, improved accuracy spread by 25%, reduced vertical recoil by 40%, and increased fire rate by 60%.

1.0.4
-----
Fixed the Action Skill End Elemental Damage anointments' damage percentages in the anointment text not changing to the correct number of 20% (courtesy of ZetaDaemon.)

1.0.3
-----
Restored Best Served Cold's cooldown back to three seconds to prevent possible nova-spam issues when using the Seein' Dead (that and the reduction didn't seem to work in the first place). Increased the nova damage to five times what it would be normally.

1.0.2
-----
Changed the rarity of the Hunt(er), Hunt(ress), Hunt(ed), and Revengenador to Legendary to help prevent them from being overlooked when they randomly drop.

1.0.1
-----
Increased the odds of Evil Lilith dropping her specific drops to 60% to compensate for her obnoxiously long immunity phase.

Adjusted the description of the Guardian 4N631 slightly.
