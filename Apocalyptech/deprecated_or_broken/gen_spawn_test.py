#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('spawn_test.txt',
        'Spawn Test',
        [],
        'SpawnTest',
        )

# This was a test to see if UE4's dynamic-object-loading thing would permit us to do
# map-merging stuff real trivially, like loading Nekrobugs into The Droughts just by
# referencing the relevant object in the SpawnOptions object.
#
# The status of this is a bit weird - about 50-75% of the Skag spawns in the map seem
# to stop working at all, while the remainder spawn *mostly* skags but occasionally
# a Nekrobug.  I wonder if something's calling out to that last SkagPup one, and that's
# the only definition that's *actually* working?
#
# Anyway, since I didn't actually have any mod plans for this, and just wanted to see
# if I could do it, I'm leaving it there.  I suspect that with some more investigation
# and trial-and-error, you'd be able to get any enemy to spawn anywhere.

for (so, count) in [
        ('/Game/Enemies/_Spawning/Skags/_Mixes/Zone0/SpawnOptions_PupsAndAdults', 2),
        ('/Game/Enemies/_Spawning/Skags/_Mixes/Zone0/SpawnOptions_SkagEarlyMix', 3),
        ('/Game/Enemies/_Spawning/Skags/Variants/SpawnOptions_SkagPup', 1),
        ]:
    for idx in range(count):
        mod.reg_hotfix(Mod.EARLYLEVEL, 'Prologue_P',
            Mod.get_full(so),
            'Options.Options[{}].Factory.Object..AIActorClass'.format(idx),
            "BlueprintGeneratedClass'/Game/Enemies/Nekrobug/Ground/_Design/Character/BPChar_Nekrobug_Ground.BPChar_Nekrobug_Ground_C'")
        mod.reg_hotfix(Mod.LEVEL, 'Prologue_P',
            Mod.get_full(so),
            'Options.Options[{}].Factory.Object..SpawnExtent'.format(idx),
            '(x=63,y=63,z=65)')
        mod.reg_hotfix(Mod.LEVEL, 'Prologue_P',
            Mod.get_full(so),
            'Options.Options[{}].Factory.Object..CachedTeam'.format(idx),
            "Team'/Game/Common/_Design/Teams/Team_Nekrobug.Team_Nekrobug'")

mod.close()
