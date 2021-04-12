#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Boss Rush 3000 Slaughter Generator
# Copyright (C) 2021 abram/skruntksrunt, altef-4, Christopher J. Kucera
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
import argparse
import sys
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod
import random
import math
import json

SEED=42
OUTPUT='boss_rush_3000.bl3hotfix'
DEFAULT_HEALTH=100
DEFAULT_DAMAGE=40
DEFAULT_TOUGH=0.2
MAX_MOBS=1000
BUFF_NAMES=[
    " the more difficult",
    " the roided",
    " the spectacular",
    " the slightly buffed",
    " the unnerfed",
    " the impermiable",
    " the kinda tankie",
    " the buff",
    " the tough",
    " the badder",
    ", a real baddie"
]
def parse_args():
    parser = argparse.ArgumentParser(description='Boss Rush 3000 Slaughter Generator')
    parser.add_argument('--seed', type=int, default=SEED, help='Seed of random number generator.')
    parser.add_argument('--json', type=str, default=None, help='JSON Input to specify each round (example-bpchar.json)')
    parser.add_argument('--time', action='store_true', default=False, help='Use time for a seed')
    parser.add_argument('--output', type=str, default=OUTPUT, help='Hotfix output file')
    parser.add_argument('--tough', type=float, default=DEFAULT_TOUGH, help='Proportion of tough mobs')
    parser.add_argument('--health', type=float, default=DEFAULT_HEALTH, help='Tough mob health multiplier')
    parser.add_argument('--damage', type=float, default=DEFAULT_DAMAGE, help='Tough mob damage multiplier')
    parser.add_argument('--maxmobs',type=int,default=MAX_MOBS, help='How many maximum different characters to load for the level')
    return parser.parse_args()

args = parse_args()
our_seed = int(args.seed)
if not args.time:
    random.seed(our_seed)

our_default_damage = float(args.damage)
our_default_health = float(args.health)
our_max_mobs = int(args.maxmobs)

# Mission Story
story = "Billie got her hands on the Katagawa's cloning machine and made a mess of the Slaughterstar 3000, filling it with Badasses and Saurians. Torgue wants you to go clean this mess up."

mod = Mod(args.output,
          'Boss Rush Slaughter 3000: Billy and the Clone-a-saurus',
          'skruntskrunt and altef_4',
          ['Turns maliwan slaughter star 3000',
           'into a boss rush slaughter 3000',
           story,
           "Based on altef_4's Hyperion Slaughter 3000"],
          lic=Mod.CC_BY_SA_40,
          v='0.9.3',
          cats='gameplay',
)

mod.comment( f'Seed for this generation (gen_boss_rush_3000.py): {our_seed}' )

for okey in ['Description','PreAcceptanceSummary','PostAcceptanceSummary']:
    for level in [Mod.EARLYLEVEL, Mod.LEVEL]:
        mod.reg_hotfix(level, 'MatchAll', '/Game/Missions/Side/Slaughters/TechSlaughter/Mission_TechSlaughter1.Default__Mission_TechSlaughter1_C',f'{okey}.FormatText',story)


from decimal import Decimal
# my imports
import boss
import mobnames


# what proportion of mobs to buff
toughen_mobs = float(args.tough)

#size mod
size_mod = True
#mob size
size = 1
#boss size
boss_size = '1.5,3.75'.split(',')
#mob speed
mob_speed = 1.5



ready_list = []
mesh_list = []
mission = []
move_list = []
item_pool_list = []


revert_enum = False
def rev(cnt, idx):
    if revert_enum:
        return cnt - idx - 1
    else:
        return idx

def enemy_icon(etype):
    return {
        'None': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/MinimapIcon_Enemy.MinimapIcon_Enemy'",
        'Normal': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/MinimapIcon_Pinging_Hostile.MinimapIcon_Pinging_Hostile'",
        'VeryGood': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/crewIcon_Hunt.crewIcon_Hunt'",
        'Badass': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/MinimapIcon_MiniBoss.MinimapIcon_MiniBoss'",
        'SuperBadass': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/MinimapIcon_Boss.MinimapIcon_Boss'",
        'UltimateBadass': "POISprite'/Game/UI/_Shared/InWorldAndMapIcons/MinimapIcon_Boss.MinimapIcon_Boss'",
    }.get(etype,'!ERR_etype.{}'.format(etype))
    

def get_bpchar(s):
    return s.split('/')[-1]

def print_and_comment(s):
    print(s)
    mod.comment(s)

chosen_mobs = set()
def gen_mod(so, scale, my_list):
    c = len(my_list)
    for idx, val in enumerate(my_list):
        if (isinstance(val[0],tuple) or isinstance(val[0],list)):
            # this means we're using (name,bpchar,balance,balancerow,extras)
            print_and_comment(f'Deploying {val[0][0]}')
            # new tuple of bpchar and prior spawn factory
            val = (val[0][1],val[1])
        else:
            print_and_comment(f'Deploying {val[0]}')
        if val == 'empty':
            continue
        var = val
        if len(var) < 2:
            print("Var < 2")
            print(var)
        assert len(var) >= 2
        obj = var[1].replace("_C'","")
        print_and_comment(f"{var},{obj},{val}")
        chosen_mobs.add(var[0])
        mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P', Mod.get_full(so), 'Options.Options[{}].Factory.Object..AIActorClass'.format(rev(c,idx)), "BlueprintGeneratedClass'{}.{}_C'".format(var[0],get_bpchar(var[0])))
        if obj not in ready_list:
            ready_list.append(obj)
            bpchar = var[0].replace("BlueprintGeneratedClass'","")
            last_bit = bpchar.split('/')[-1]
            # extend = eval(val+"(1)").replace('(x=','').replace('y=','').replace('z=','').replace(')','').split(',')
            # should extent be looked up from a table?
            extend = (70,70,119)
            scale = 1.0
            mod.reg_hotfix(Mod.LEVEL, 'TechSlaughter_P', Mod.get_full(so),
                'Options.Options[{}].Factory.Object..SpawnExtent'.format(rev(c,idx)),
                f'(X={scale * float(extend[0])},Y={scale * float(extend[1])},Z={scale * float(extend[2])})')
            mod.reg_hotfix(Mod.LEVEL, 'TechSlaughter_P', Mod.get_full(so),
                'Options.Options[{}].Factory.Object..SpawnOrigin'.format(rev(c,idx)),
                f'(X={1500},Y={0},Z={0})')# what if we change to X to 0 from 1500
            mod.reg_hotfix(Mod.LEVEL, 'TechSlaughter_P', Mod.get_full(so),
                'Options.Options[{}].Factory.Object..CollisionHandling'.format(rev(c,idx)),
                'AlwaysSpawn')
            mod.reg_hotfix(Mod.LEVEL, 'TechSlaughter_P', Mod.get_full(so),
                'Options.Options[{}].Factory.Object..bOverrideCollisionHandling'.format(rev(c,idx)),
                'True')
            mod.reg_hotfix(Mod.LEVEL, 'TechSlaughter_P', Mod.get_full(so),
                'Options.Options[{}].Factory.Object..SpawnDetails'.format(rev(c,idx)),
                '(Critical=AlwaysSpawn)')
            
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P', '{}:{}'.format(Mod.get_full(so),val[1]), 'TeamOverride', Mod.get_full_cond('/Game/Common/_Design/Teams/Team_Maliwan', 'Team'))



_replace_enemy_uniq = set()
def replace_enemy(l):
    return replace_if_too_many([(boss.choose_random_slaughter_boss(),x[1]) for x in l], _replace_enemy_uniq)

def round1(end_boss=False):

    gen_mod('/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_1/SpawnOptions_KatagawaBallAdds_MeleeMix',
            size,replace_enemy([
                ("/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/BPChar_Enforcer_Bounty01", "Factory_SpawnFactory_OakAI"), # ??
                ("/Game/Enemies/ServiceBot/LOOT/_Design/Character/BPChar_ServiceBot_LOOT","Factory_SpawnFactory_OakAI_1"),
                ("/Game/Enemies/Skag/_Unique/Buttmunch/_Design/Character/BPChar_SkagButtmunch","Factory_SpawnFactory_OakAI_2"),
                ("/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue","Factory_SpawnFactory_OakAI_3"),
                ("/Game/Enemies/Heavy/_Unique/FootstepsOfGiants/_Design/Character/BPChar_HeavyFootstepsOfGiants","Factory_SpawnFactory_OakAI_4"),
                ("/Game/Enemies/Nog/_Unique/Beans/_Design/Character/BPChar_NogBeans","Factory_SpawnFactory_OakAI_5"),
            ]))


    #wave 1a
    # Junk loader is the test enemy that we know works
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1a_Trooper1',
             size,replace_enemy([
                 ("/Game/PatchDLC/Dandelion/Enemies/Loader/JUNK_Loaders/_Design/Character/BPChar_LoaderBasicJUNK","SpawnFactory_OakAI_2")
             ]))
    
    # After this point everything is random
    #wave 1b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1b_TrooperBscShtGn',
        size,replace_enemy([
            ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_2")
        ]))
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2a_Trooper',
        size,replace_enemy([
            ("BPChar_TrooperBadass_C_FIX","Factory_SpawnFactory_OakAI"),
            ("BPChar_TrooperShotgun_C_FIX","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMelee_C_FIX","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasic_C_FIX","SpawnFactory_OakAI_2"),
        ]))
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2b_TrprShtMleJtpk',
        size,replace_enemy([
            ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_3"),
        ]))
    #wave 3a
    pentulimatewavename='/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3a'
    pentulimatespawner="SpawnFactory_OakAI_0"
    penspawns = [f"SpawnFactory_OakAI_{i}" for i in range(5)]
    # what if we replace spawns?
    penspawns = ["Factory_SpawnFactory_OakAI" for i in range(5)]
    round3a = [
        ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_0"),
        ("BPChar_TrooperShotgun_C","SpawnFactory_OakAI_1"),
        ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_2"),
        ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_3"),
        ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_4"),
    ]
    penspawns = [x[1] for x in round3a]

    #wave 3b
    endwavename = '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3b'
    endspawner = "SpawnFactory_OakAI_0"
    #endspawns = [f"SpawnFactory_OakAI_{i}" for i in range(6)]
    #endspawns = ["Factory_SpawnFactory_OakAI" for i in range(5)]
    
    round3b = [
        ("BPChar_TrooperShotgun_C",endspawner),
        ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_1"),
        ("BPChar_TrooperBasic_C","SpawnFactory_OakAI_2"),
        ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_3"),
        ("BPChar_Heavy_Basic_C","SpawnFactory_OakAI_4"),
        ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_5"),
    ]
    endspawns = [x[1] for x in round3b]
    if end_boss:
        # was 132 for code
        gen_endboss(wave=pentulimatewavename,spawners=penspawns,wavecode=121)
        gen_endboss(wave=endwavename,spawners=endspawns,wavecode=121)
    else:
        # wave 3a
        gen_mod(pentulimatewavename,
                size,replace_enemy(round3a))
        # wave 3b
        gen_mod(endwavename,
                size,replace_enemy(round3b))
        
def round2(end_boss=False):
    #ROUND 2 fix on 3a medic, basic, jetpack, badass

    #wave 1_0
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave1',
        size,replace_enemy([
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMelee_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpack_C","SpawnFactory_OakAI_3"),
            ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedic_C","SpawnFactory_OakAI_5"),
            ("BPChar_TrooperFlash_C","SpawnFactory_OakAI_6"),
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_7"),
        ]))
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2a',
        size,replace_enemy([
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMeleeDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpackDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_6"),
            ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2b',
        size,replace_enemy([
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMeleeDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_Heavy_Basic_C","SpawnFactory_OakAI_10"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpackDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_6"),
            ("BPChar_Heavy_Powerhouse_C","SpawnFactory_OakAI_8"),
            ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3a',
        size,replace_enemy([
            ("BPChar_TrooperShotgunDark_C_FIX","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMeleeDark_C_FIX","SpawnFactory_OakAI_1"),
            ("BPChar_HeavyGunner_C_FIX","SpawnFactory_OakAI_10"),
            ("BPChar_TrooperBasicDark_C_FIX","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpackDark_C_FIX","SpawnFactory_OakAI_3"),
            ("BPChar_TrooperBadass_C_FIX","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedicDark_C_FIX","SpawnFactory_OakAI_5"),
            ("BPChar_TrooperFlashDark_C_FIX","SpawnFactory_OakAI_6"),
        ]))
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3b',
        size,replace_enemy([
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperMeleeDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_10"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperJetpackDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_Heavy_Icebreaker_C","SpawnFactory_OakAI_4"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_6"),
            ("BPChar_Heavy_Acidrain_C","SpawnFactory_OakAI_7"),
            ("BPChar_TrooperBadass_C","SpawnFactory_OakAI_8"),
        ]))
    #wave 4a
    #wave 4b
    penendwavename = '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4a'
    endspawner = "SpawnFactory_OakAI_0"
    round4a = [
        ("BPChar_TrooperMeleeDark_C","SpawnFactory_OakAI_1"),
        ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_10"),
        ("BPChar_Heavy_Badass_C","SpawnFactory_OakAI_11"),
        ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
        ("BPChar_Heavy_Acidrain_C","SpawnFactory_OakAI_7"),
        ("BPChar_Heavy_Basic_C","SpawnFactory_OakAI_9"),
    ]
    round4b = [
        ("BPChar_TrooperBadass_C",endspawner),
        ("BPChar_HeavyGunner_C","SpawnFactory_OakAI_10"),
        ("BPChar_Heavy_Badass_C","SpawnFactory_OakAI_11"),
        ("BPChar_NogBasic_C","SpawnFactory_OakAI_12"),
        ("BPChar_Heavy_Icebreaker_C","SpawnFactory_OakAI_4"),
        ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_5"),
        ("BPChar_Heavy_Powerhouse_C","SpawnFactory_OakAI_8"),
    ]

    penspawns = [x[1] for x in round4a]
    endwavename='/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4b'
    # endspawns = ["Factory_SpawnFactory_OakAI" for i in range(7)]
    endspawns = [x[1] for x in round4b]
    if end_boss:
        gen_endboss(wave=penendwavename,spawners=penspawns,wavecode=242)
        gen_endboss(wave=endwavename,spawners=endspawns,wavecode=242)
    else:
    #wave 4a
        gen_mod(penendwavename,
                size,replace_enemy(round4a))
        gen_mod(endwavename,
                size,replace_enemy(round4b))

def round3(end_boss=False):
    #ROUND 3 FIX on 2a dark heavy, dogs, nogs
    
    #wave 1a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1a',
        size,replace_enemy([
            ("BPChar_TrooperFlashDark_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_16"),
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_3"),
        ]))
    #wave 1b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1b',
        size,replace_enemy([
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_19"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
            ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
        ]))
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2a',
        size,replace_enemy([
            ("BPChar_FrontrunnerBasic_C_FIX","Factory_SpawnFactory_OakAI"),
            ("BPChar_HeavyGunnerDark_C_FIX","SpawnFactory_OakAI_24"),
            ("BPChar_Heavy_PowerhouseDark_C_FIX","SpawnFactory_OakAI_25"),
            ("BPChar_NogBasic_C_FIX","SpawnFactory_OakAI_26"),
            ("BPChar_Heavy_BasicDark_C_FIX","SpawnFactory_OakAI_28"),
        ]))
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2b',
        size,replace_enemy([
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
            ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_29"),
        ]))
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3a',
        size,replace_enemy([
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
            ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
        ]))
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3b',
        size,replace_enemy([
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_NogBasic_C","SpawnFactory_OakAI_26"),
            ("BPChar_NogNinja_C","SpawnFactory_OakAI_27"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_29"),
        ]))
    #wave 4a
    endspawner='Factory_SpawnFactory_OakAI'
    round4a = [("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),]
    # what if we avoid that?
    round4a = [("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI_30"),]
    round4b = [
        ("BPChar_Oversphere_C",endspawner),
        ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_25"),
        ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
        ("BPChar_Oversphere_C","SpawnFactory_OakAI_3"),
        ("BPChar_NogBasicDark_C","SpawnFactory_OakAI_4"),
        ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
        ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
        ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_7"),
    ]
    # just least 3a 
    penendwavename='/Game/Enemies/_Spawning/Maliwan/Overspheres/Variants/SpawnOptions_Oversphere_RandomElement'
    pendspawners = ["Factory_SpawnFactory_OakAI"]
    penspawns = [x[1] for x in round4a]
    gen_mod(penendwavename,
            size,replace_enemy(round4a))
    
    #wave 4b
    endwavename='/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave4a'
    endspawners= [endspawner,"SpawnFactory_OakAI_25","SpawnFactory_OakAI_28","SpawnFactory_OakAI_3","SpawnFactory_OakAI_4","SpawnFactory_OakAI_5","SpawnFactory_OakAI_6","SpawnFactory_OakAI_7"]
    endspawns =  [x[1] for x in round4b]

    if end_boss:
        # 4a
        # gen_endboss(wave=penendwavename,spawners=penspawns,wavecode=341)
        # 4b
        # is 341 right?
        gen_endboss(wave=endwavename,spawners=endspawns,wavecode=341)
    else:
        gen_mod(endwavename,
            size,replace_enemy(round4b))

def round4(end_boss=False):
    #wave_1
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave1',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_NogBasicDark_C","SpawnFactory_OakAI_4"),
            ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
            ("BPChar_Oversphere_C","SpawnFactory_OakAI_7"),
        ]))
    #wave 2
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave2',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
            ("BPChar_NogBasicDark_C","SpawnFactory_OakAI_4"),
            ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
            ("BPChar_Oversphere_C","SpawnFactory_OakAI_7"),
            ("BPChar_OversphereDefender_C","SpawnFactory_OakAI_8"),
        ]))
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3a',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_28"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_NogBasicDark_C","SpawnFactory_OakAI_4"),
            ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
            ("BPChar_Oversphere_C","SpawnFactory_OakAI_7"),
            ("BPChar_OversphereDefender_C","SpawnFactory_OakAI_8"),
            ("BPChar_TrooperJetpackDark_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3b',
        size,replace_enemy([
            ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_OversphereHarbinger_C","SpawnFactory_OakAI_10"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_2"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_5"),
            ("BPChar_NogNogromancer_C","SpawnFactory_OakAI_6"),
            ("BPChar_Oversphere_C","SpawnFactory_OakAI_7"),
            ("BPChar_OversphereDefender_C","SpawnFactory_OakAI_8"),
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 4a
    #wave 4b
    penendwavename='/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4a'
    endwavename='/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4b'
    endspawner="Factory_SpawnFactory_OakAI"
    endspawners=[endspawner for i in range(8)]
    if end_boss:
        gen_endboss(wave=penendwavename,spawners=endspawners,wavecode=442)
        gen_endboss(wave=endwavename,   spawners=endspawners,wavecode=442)
    else:
        gen_mod(penendwavename,
                size,replace_enemy([
                    ("BPChar_Oversphere_C","Factory_SpawnFactory_OakAI"),
                    ("BPChar_Frontrunner_Badass_C_FIX","SpawnFactory_OakAI_0"),
                    ("BPChar_FrontrunnerJammer_C_FIX","SpawnFactory_OakAI_1"),
                    ("BPChar_OversphereDark_C","SpawnFactory_OakAI_11"),
                    ("BPChar_TrooperMedicDark_C_FIX","SpawnFactory_OakAI_15"),
                    ("BPChar_TrooperBasicDark_C_FIX","SpawnFactory_OakAI_16"),
                    ("BPChar_OversphereStinger_C","SpawnFactory_OakAI_17"),
                    ("BPChar_FrontrunnerStriker_C_FIX","SpawnFactory_OakAI_20"),
                ]))
        gen_mod(endwavename,
            size,replace_enemy([
                ("BPChar_Oversphere_C",endspawner),
                ("BPChar_OversphereDark_C","SpawnFactory_OakAI_11"),
                ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_18"),
                ("BPChar_Heavy_BasicDark_C","SpawnFactory_OakAI_22"),
                ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_23"),
                ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
                ("BPChar_OversphereStinger_C","SpawnFactory_OakAI_126"),
                ("BPChar_MechBasic_C","SpawnFactory_OakAI_27"),
                ("BPChar_NogNinjaDark_C","SpawnFactory_OakAI_30"),
            ]))

def round5():
    #ROUND 5 fix on 3a fix darc centurion, basic_mech
    
    #wave_1a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1a',
        size,replace_enemy([
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_10"),
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_TrooperShotgunDark_C","SpawnFactory_OakAI_12"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_13"),
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_15"),
            ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
        ]))
    #wave_1b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1b',
        size,replace_enemy([
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_10"),
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_TrooperMedicDark_C","SpawnFactory_OakAI_12"),
            ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_13"),
            ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
        ]))
    #wave 2a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2a',
        size,replace_enemy([
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_TrooperBasicDark_C","SpawnFactory_OakAI_12"),
            ("BPChar_TrooperFlashDark_C","SpawnFactory_OakAI_13"),
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
            ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_26"),
        ]))
    #wave 2b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2b',
        size,replace_enemy([
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
            ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_15"),
            ("BPChar_MechMGDark_C","SpawnFactory_OakAI_16"),
            ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
            ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_26"),
        ]))
    #wave 3a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3a',
        size,replace_enemy([
            ("BPChar_HeavyGunnerDark_C_FIX","SpawnFactory_OakAI_0"),
            ("BPChar_Heavy_BadassDark_C_FIX","SpawnFactory_OakAI_1"),
            ("BPChar_MechBasicDark_C_FIX","SpawnFactory_OakAI_11"),
            ("BPChar_MechChargerDark_C_FIX","SpawnFactory_OakAI_14"),
            ("BPChar_MechGrenadierDark_C_FIX","SpawnFactory_OakAI_15"),
            ("BPChar_MechMGDark_C_FIX","SpawnFactory_OakAI_16"),
            ("BPChar_FrontrunnerStriker_C_FIX","SpawnFactory_OakAI_2"),
            ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereHarbingerDark_C","SpawnFactory_OakAI_25"),
        ]))
    #wave 3b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3b',
        size,replace_enemy([
            ("BPChar_HeavyGunnerDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
            ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_15"),
            ("BPChar_MechMGDark_C","SpawnFactory_OakAI_16"),
            ("BPChar_FrontrunnerJammer_C","SpawnFactory_OakAI_2"),
            ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_24"),
            ("BPChar_OversphereDefenderDark_C","SpawnFactory_OakAI_26"),
            ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_3"),
            ("BPChar_OversphereStingerDark_C","SpawnFactory_OakAI_4"),
        ]))
    #wave 4a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4a',
        size,replace_enemy([
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_0"),
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_FrontrunnerStriker_C","SpawnFactory_OakAI_10"),
            ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_12"),
            ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_6"),
            ("BPChar_MechMGDark_C","SpawnFactory_OakAI_7"),
            ("BPChar_FrontrunnerBasic_C","SpawnFactory_OakAI_8"),
            ("BPChar_FrontrunnerJammer_C","SpawnFactory_OakAI_9"),
        ]))
    #wave 4b
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4b',
        size,replace_enemy([
            ("BPChar_MechBasicDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_MechChargerDark_C","SpawnFactory_OakAI_14"),
            ("BPChar_MechGrenadierDark_C","SpawnFactory_OakAI_15"),
            ("BPChar_MechMGDark_C","SpawnFactory_OakAI_16"),
            ("BPChar_FrontrunnerBasic_C","SpawnFactory_OakAI_2"),
            ("BPChar_FrontrunnerJammer_C","SpawnFactory_OakAI_3"),
            ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_4"),
            ("BPChar_FrontrunnerStriker_C","SpawnFactory_OakAI_5"),
        ]))
    #wave 5a
    gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave5',
        size,replace_enemy([
            ("BPChar_NogBadassDark_C","SpawnFactory_OakAI_1"),
            ("BPChar_TrooperBadassDark_C","SpawnFactory_OakAI_11"),
            ("BPChar_Heavy_PowerhouseDark_C","SpawnFactory_OakAI_12"),
            ("BPChar_Heavy_BadassDark_C","SpawnFactory_OakAI_13"),
            ("BPChar_Heavy_AcidrainDark_C","SpawnFactory_OakAI_14"),
            ("BPChar_Heavy_IcebreakerDark_C","SpawnFactory_OakAI_15"),
            ("BPChar_OversphereBadass_C","SpawnFactory_OakAI_2"),
            ("BPChar_MechMGDark_C","SpawnFactory_OakAI_3"),
            ("BPChar_Frontrunner_Badass_C","SpawnFactory_OakAI_5"),
        ]))
    #wave5b
    gen_mod('/Game/Enemies/_Spawning/ProvingGrounds/Trial7/SpawnOptions_PGTrial7_Maliwan_MechAdds',
        size,replace_enemy([
            ("BPChar_TrooperBasic_C","Factory_SpawnFactory_OakAI"),
            ("BPChar_TrooperMedic_C","Factory_SpawnFactory_OakAI_3"),
            ("BPChar_TrooperFlash_C","Factory_SpawnFactory_OakAI_4"),
        ]))
    # Let's try it without generating bosses
    # #BOSS 2
    # gen_mod('/Game/Enemies/_Spawning/Maliwan/Mechs/_Unique/SpawnOptions_Mech_TechSlaughterBoss2',
    #     float(boss_size[1]),[
    #         ("/Game/PatchDLC/Dandelion/Enemies/Fabrikator/Basic/_Design/Character/BPChar_FabrikatorBasic","Factory_SpawnFactory_OakAI"),
    #     ])
    # 
    # #BOSS 1 !bug here
    # gen_mod('/Game/Enemies/_Spawning/Maliwan/Mechs/_Unique/SpawnOptions_Mech_TechSlaughterBoss1',
    #     float(boss_size[0]),[
    #         ("/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Character/BPChar_Mech_TrialBoss","Factory_SpawnFactory_OakAI"),
    #     ])

# remove balconies
# OakSpawnPoint_12 is at -3796,3129,1496 (balconie)
# OakSpawnPoint_4 is at -175, 7028, -901

Tech_mission = '/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel'
DC = 'SpawnMesh_DoorCargo'
DS = 'SpawnMesh_DoorSmall'
SP = 'OakSpawnPoint'
safe_spawns = [ # altef-4 made this
        #RIGHT
        "{}_C'{}.{}_6'".format(DC,Tech_mission,DC),
        "{}_C'{}.{}_0'".format(DC,Tech_mission,DC),
        "{}_C'{}.{}_7'".format(DC,Tech_mission,DC),
        #"{}'{}.{}_12'".format(SP,Tech_mission,SP), # balconey?
        #"{}'{}.{}_15'".format(SP,Tech_mission,SP), # balconey?
        #"{}'{}.{}_39'".format(SP,Tech_mission,SP), # balconey?
        #LEFT
        "{}_C'{}.{}_5'".format(DC,Tech_mission,DC),
        #"{}'{}.{}_41'".format(SP,Tech_mission,SP),#LBalcon Right
        #"{}'{}.{}_20'".format(SP,Tech_mission,SP),#LBalcon Center
        #"{}'{}.{}_49'".format(SP,Tech_mission,SP),#LBalcon Left
        "{}_C'{}.{}_2'".format(DC,Tech_mission,DC),
        "{}_C'{}.{}_1'".format(DC,Tech_mission,DC),
        "{}_C'{}.{}_4'".format(DC,Tech_mission,DC),
        "{}_C'{}.{}_3'".format(DC,Tech_mission,DC),
        #"{}'{}.{}_8'".format(SP,Tech_mission,SP),#Lift
        "{}_C'{}.{}_3'".format(DC,Tech_mission,DC),
        #CENTER
        "{}'{}.{}_57'".format(SP,Tech_mission,SP),
        "{}_C'{}.{}_2'".format(DS,Tech_mission,DS),
        "{}_C'{}.{}_0'".format(DS,Tech_mission,DS),
        "{}_C'{}.{}_3'".format(DS,Tech_mission,DS),
        # "{}_C'{}.{}_4'".format(SP,Tech_mission,SP),#boss Mech_0 Right Lift
        # "{}_C'{}.{}_6'".format(SP,Tech_mission,SP),#boss Mech Left Lift Down
]
balconey_spawns = [
    "{}'{}.{}_12'".format(SP,Tech_mission,SP), # balconey?
    "{}'{}.{}_15'".format(SP,Tech_mission,SP), # balconey?
    "{}'{}.{}_39'".format(SP,Tech_mission,SP), # balconey?
    #LEFT
    "{}'{}.{}_41'".format(SP,Tech_mission,SP),#LBalcon Right
    "{}'{}.{}_20'".format(SP,Tech_mission,SP),#LBalcon Center
    "{}'{}.{}_49'".format(SP,Tech_mission,SP),#LBalcon Left
]



boss_spawns = [
    "{}_C'{}.{}_4'".format(SP,Tech_mission,SP),#boss Mech_0 Right Lift
    "{}_C'{}.{}_6'".format(SP,Tech_mission,SP),#boss Mech Left Lift Down
]

safe_spawn_string = ",".join(safe_spawns)
# safe_spawn_string = ",".join(balconey_spawns)

missions = { # stolen from altef-4 gen_3000_Char_list.py
        111: "OakMissionSpawner_Round1Wave",
        112: "OakMissionSpawner_Round1Wave",
        121: "OakMissionSpawner_Round1Wave_0",
        122: "OakMissionSpawner_Round1Wave_0",
        123: "Round1Wave",
        131: "OakMissionSpawner_Round1Wave_5",
        211: "OakMissionSpawner_Round2Wave",
        132: "OakMissionSpawner_Round1Wave_5",
        221: "OakMissionSpawner_Round2Wave_1",
        222: "OakMissionSpawner_Round2Wave_1",
        231: "OakMissionSpawner_Round2Wave_2",
        232: "OakMissionSpawner_Round2Wave_2",
        233: "Round2Wave3Dropship",
        241: "OakMissionSpawner_Round2Wave_3",
        242: "OakMissionSpawner_Round2Wave_3",
        311: "OakMissionSpawner_Round3Wave",
        312: "OakMissionSpawner_Round3Wave",
        321: "OakMissionSpawner_Round3Wave_4",
        322: "OakMissionSpawner_Round3Wave_4",
        323: "Round3Wave2_BehindDropship",
        331: "OakMissionSpawner_Round3Wave_5",
        332: "OakMissionSpawner_Round3Wave_5",
        341: "OakMissionSpawner_Round3Wave_6",
        411: "OakMissionSpawner_Round4Wave",
        421: "OakMissionSpawner_Round4Wave_7",
        431: "OakMissionSpawner_Round4Wave_8",
        432: "OakMissionSpawner_Round4Wave_8",
        441: "OakMissionSpawner_Round4Wave_9",
        442: "OakMissionSpawner_Round4Wave_9",
        443: "Round4_Wave_5",
        511: "OakMissionSpawner_Round5Wave",
        512: "OakMissionSpawner_Round5Wave",
        521: "OakMissionSpawner_Round5Wave_0",
        522: "OakMissionSpawner_Round5Wave_0",
        531: "OakMissionSpawner_Round5Wave_10",
        532: "OakMissionSpawner_Round5Wave_10",
        533: "Round5Wave3_Dropship",
        541: "OakMissionSpawner_Round5Wave_11",
        542: "OakMissionSpawner_Round5Wave_11",
        551: "OakMissionSpawner_Round5Wave_12",
        552: "OakMissionSpawner_Round5Wave_12",
        561: "OakMissionSpawner_Round5Wave_13",
        562: "OakMissionSpawner_Round5Wave_13"
}

# I don't know what should be round 4 final round
# removing round 4 didn't solve my problem
# perhaps too omega spawns are because round 3 is wrong?
final_round_spawns = set([missions[x] for x in [242,122,341]])
safe_missions = sorted(set(missions.values()).difference(final_round_spawns))
def gen_safe_spawns():
    mod.comment("Now we're going to remove the balconey as a spawn point")
    random_spawn = True
    full_Spawn_list = safe_spawn_string
    for m in safe_missions: #sorted(set(missions.values())):
        mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                    "{}.{}.SpawnerComponent".format(Tech_mission,m),
                    'SpawnPoints',
                    '({})'.format(full_Spawn_list),'',True)
        mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
                    'bRandomizeSpawnPoints',
                    random_spawn,"",True) # this was False
        for i in range(3):
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                "{}.{}.SpawnerComponent".format(Tech_mission,m),
                'SpawnPointGroups.SpawnPointGroups[{}].SpawnPoints'.format(i),
                '({})'.format(full_Spawn_list),'',True)
            mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
                'SpawnPointGroups.SpawnPointGroups[{}].bRandomize'.format(i),
                random_spawn,"",True)

def replace_if_too_many(wave, uniq_mobs, our_max_mobs=our_max_mobs):
    outwave = []
    for mob in wave:
        if len(uniq_mobs) > our_max_mobs:
            mob = (random.choice(sorted(list(uniq_mobs))),mob[1])
        else:
            if isinstance(mob[0],tuple) or isinstance(mob[0],list):
                uniq_mobs.add(mob[0][1]) # adds the bpchar path instead
            else:
                uniq_mobs.add(mob[0])
        outwave.append(mob)
    return outwave    
            
    
            
def gen_mod_from_data(data):
    mod.comment( f'Seed for this from json data: {data.get("seed","Seed not found")}' )
    rounds = ["round1","round2","round3","round4","round5"]
    uniq_mobs = set()
    for curr_round_name in rounds:
        curr_round = data[curr_round_name]
        waves = [x for x in curr_round.keys() if x[0] == '/']
        for wave_name in waves:
            wave = curr_round[wave_name]
            #gen_mod('/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4b',
            replace_if_too_many(wave, uniq_mobs)
            gen_mod(wave_name,size,wave)

def default_mod(end_boss=False):
    # [ ] round1?
    round1(end_boss=end_boss)
    # [ ] round2?
    # just override for now XXX
    # end_boss = False
    round2(end_boss=end_boss)
    # # [ ] round3?
    round3(end_boss=end_boss)
    # # [ ] round4?
    # disabling round4 end_boss for now
    round4(end_boss=end_boss)
    # # [ ] round5?
    round5()

def rename_mob(bpchar, newname):
    mod.comment(f"Rename {bpchar} to '{newname}'")
    attr = 'DisplayName'
    if not bpchar in mobnames.mobname_dict:
        mod.comment(f"WARNING: Cannot rename {bpchar} to '{newname}' as we are missing UIName")
        return
    uiname = mobnames.mobname_dict[bpchar]
    mod.reg_hotfix(mod.PATCH,'',
                   uiname,
                   attr,
                   newname)
    
def buff(boss_tuple,healthbuff=our_default_health,damagebuff=our_default_damage):
    my_boss = boss.mk_boss(*boss_tuple)
    # replace boss health with some multiplier
    my_boss['health'] = [healthbuff for h in my_boss['health']]
    my_boss['nloot'] = 0 # disable loot buffs
    my_boss['damage'] = damagebuff
    if my_boss['balance_table']:
        print_and_comment(f"Buffing: {my_boss['name']}")
        mod.raw_line(boss.buff_boss( my_boss ))
    rename_mob(my_boss["bpchar_path"],my_boss["name"]+random.choice(BUFF_NAMES))    
def toughen_up_mobs(toughen_mobs, chosen_mobs=chosen_mobs):
    # this is the proportion of tough mobs
    if toughen_mobs > 0.0:
        if toughen_mobs > 1.0:
            toughen_mobs /= 100.0;
    cmobs = sorted(list(chosen_mobs))
    n = len(cmobs)
    nmobs = min(round(n * toughen_mobs),n)
    tough_mobs = random.choices(cmobs, k=nmobs)
    boss_definitions = [x for x in [boss.find_boss(mob) for mob in tough_mobs] if not x is None]
    print_and_comment(f"{len(boss_definitions)/len(tough_mobs)} balance tables found")
    for our_boss in boss_definitions:
        buff(our_boss)

far_spawn = "far"
close_spawn = "close"
red_spawn = "red"
og_red_spawn = "og_red"
boss_spawns = {
    far_spawn:{
        "name":balconey_spawns[0],
        "location":(-2000.0,1000.0,1000.0),
        "myname":far_spawn,
    },
    close_spawn: {
        "name":balconey_spawns[3],
        # changed to 1000.0 for Y 1000.0 for Z
        # changed X to 3500 0 for Y 1000 for Z
        "location":(3500.0,0.0,1000.0),
        "myname":close_spawn,
    },
    red_spawn: {
        "name":boss_spawns[0],
        "location":(3500.0,0.0,1000.0),
        "myname":red_spawn,
    },
    og_red_spawn: {
        "name":boss_spawns[0],
        # OakSpawnPoint_4 is at -175, 7028, -901
        "location":(-175,7028,-901),
        "myname":og_red_spawn,
    },
}
OPTIONS=4
BPCHAR=1
katagawa = ("Katagawa Ball","/Game/Enemies/Oversphere/_Unique/KatagawaSphere/_Design/Character/BPChar_Oversphere_KatagawaSphere","/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique",
            "Oversphere_Katagawa",
            {"spawn":red_spawn}) #red spawn works # close does not
wotan = ("Wotan","/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/_Design/Character/BPChar_BehemothRaid",
         "/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth",
         "Behemoth_Raid",
         {"spawn":close_spawn}) # was red_spawn
omega = ("OmegaMantikore","/Game/Enemies/Nekrobug/_Unique/BetterTimes/_Design/Character/BPChar_Nekrobug_BetterTimes",
         "/Game/Enemies/Nekrobug/_Shared/_Design/Balance/Table_Balance_Nekrobug_Unique",
         "Nekrobug_BetterTimes",
         {"spawn":close_spawn})
graveward =("Graveward","/Game/Enemies/EdenBoss/_Shared/_Design/Character/BPChar_EdenBoss",
             "/Game/Enemies/EdenBoss/_Shared/_Design/Balance/Table_Balance_EdenBoss_PT1","EdenBoss",
            {"spawn":far_spawn}) # og_red_spawn in the right direction too far away # red_spawn right direction, too close
fabrikator = ("Fabrikator","/Game/PatchDLC/Dandelion/Enemies/Fabrikator/Basic/_Design/Character/BPChar_FabrikatorBasic",
              "/Game/PatchDLC/Dandelion/Enemies/Fabrikator/_Shared/_Design/Balance/Table_Balance_Fabrikator",
              "FabrikatorPT2",
              {"spawn":close_spawn})
benedict = ("Dr Benedict",
            '/Alisma/Enemies/DrBenedict/_Shared/_Design/Character/BPChar_DrBenedict',
            "/Alisma/Enemies/DrBenedict/_Shared/_Design/Balance/Table_Balance_DrBenedict_PT1",
            "Basic",
            {"spawn":close_spawn})
_close_spawn = {"spawn":close_spawn}
warden =    ('Warden','/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","CageArena",_close_spawn)
bellikprimis= ('Bellik Primis','/Geranium/Enemies/Biobeast/_Unique/AlteredBeast/_Design/Character/BPChar_Biobeast_AlteredBeast','/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique',"AlteredBeast",_close_spawn) # works
killavolt=('Killavolt (Kenneth)','/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique','Enforcer_KillaVolt',_close_spawn)

good_endbosses = [
    # fabrikator, # untested
    # graveward,
    omega,
    wotan,
    # benedict,
    bellikprimis,
    # katagawa,
]

def limit_wave_to_n(wave,n):
    ''' limits the number of entities in the wave to n '''
    mod.comment(f"limit_wave_to_n: Limit wave {wave} to {n}")
    path1=f'/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{wave}.SpawnerComponent'
    path2=f'/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{wave}.SpawnerComponent'
    obj1='SpawnerComponent.Object..SpawnerStyle.Object.Waves.Waves[0].SpawnerStyle.Object.NumActorsParam.AttributeInitializationData.BaseValueConstant'
    obj2='SpawnerComponent.Object..SpawnerStyle.Object.Waves.Waves[1].SpawnerStyle.Object.NumActorsParam.AttributeInitializationData.BaseValueConstant'
    obj3='SpawnerComponent.Object..SpawnerStyle.Object.NumActorsParam.AttributeInitializationData.BaseValueConstant'
    for t in [(path1,obj1),(path1,obj2),(path2,obj3)]:
        path,obj = t
        mod.reg_hotfix(
                    Mod.EARLYLEVEL, 
                    'TechSlaughter_P',
                    path,   
                    obj,
                    1,'',True)
        # we are trying to remove the initializer
        #      "NumActorsParam" : {
        # "AttributeInitializationData" : {
        #    "AttributeInitializer" : [
        #       "PCF_ScaleBy25PercentPerAdditionalPlayer_C",
        #       "/Game/GameData/Balance/PlayerCountFormulas/PCF_ScaleBy25PercentPerAdditionalPlayer"
        #    ],
        #    "BaseValueConstant" : 6
        # }
        mod.reg_hotfix(
                    Mod.EARLYLEVEL, 
                    'TechSlaughter_P',
                    path,   
                    obj.replace("BaseValueConstant","AttributeInitializer"),
                    'None','',True)

def generate_spawn( spawn_entry ):
    ''' generate a spawn by moving an existing one 
        spawn_entry is:
        {
          "name":"OriginalSpawnName", # the spawn name in the code
          "location":(x,y,z), # where to move it
          "myname":"what I call this spawn",
        }
        this will move OriginalSpawnName to location
    '''
    # make an entry
    spawnpoint = spawn_entry["name"]
    (x,y,z) = spawn_entry["location"]
    path =  spawnpoint.split("'")[1]
    mod.comment(f"generate_spawn: {spawn_entry.get('myname','')} {spawnpoint} moved to ({x},{y},{z})")
    for (obj,val) in [("RelativeLocation",f'(X={x},Y={y},Z={z})'),
                      ('bFilterByTag','None'),
                      ('SpawnAction','None'),
                      ('FilterMatchType','None'),
                      ('Tags','None'),
                      # # not sure we can rotate the spawn point
                      #('StretchyPoint',"(Rotation=(W=0.999,X=0,Y=0.0,Z=0.001))"),
                      #('StretchyPoint',"(Rotation=(W=0.707,X=0,Y=0.0,Z=0.707))"),
                      #('StretchyPoint',"(Rotation=(w=0.707,x=0,y=0.0,z=0.707))"),
    ]:
        mod.reg_hotfix(
            Mod.EARLYLEVEL, 'TechSlaughter_P',
            #f"{Tech_mission}.{wave}.SpawnerComponent",
            #f"/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{spawnpoint}.SpawnPointComponent",
            f"{path}.SpawnPointComponent",
            #"RelativeLocation",
            obj,
            val,'',True)

    
def set_wave_spawns_to( wave, spawns ):
    ''' set the spawns for this `wave` to `spawns`
        `spawns` is a list of spawn name strings
    '''
    # raise "Didn't finish set_wave_spawns_to"
    mod.comment(f"set_wave_spawns_to: Set {wave} to {spawns}")
    m = wave
    # SparkEarlyLevelPatchEntry,(1,1,1,TechSlaughter_P),/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.OakMissionSpawner_Round1Wave.SpawnerComponent,SpawnPoints,0,,(OakSpawnPoint_C'/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.OakSpawnPoint_4')
    spawn_list = ",".join(spawns)
    fspawn_list = f'({spawn_list})' #.format(spawn_list), 
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                "{}.{}.SpawnerComponent".format(Tech_mission,wave),
                'SpawnPoints',
                fspawn_list,'',True)
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
                'bRandomizeSpawnPoints',
                True,"",True) # this was False
    for i in range(3):
        mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
            "{}.{}.SpawnerComponent".format(Tech_mission,m),
            'SpawnPointGroups.SpawnPointGroups[{}].SpawnPoints'.format(i),
            fspawn_list,'',True)
        mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
            "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
            'SpawnPointGroups.SpawnPointGroups[{}].bRandomize'.format(i),
            True,"",True)

_endbosses = None

def gen_endboss(boss=None,wave=None,wavecode=None,spawners=["Factory_SpawnFactory_OakAI"]):
    global _endbosses
    mod.comment(f"gen_endboss({boss},{wave},{wavecode})")
    if wave is None or spawners is None:
        raise "Wave or spawner is not set in gen_endboss"
    my_boss = None
    if boss is None:
        if _endbosses is None or len(_endbosses) < 1: 
            # _endbosses= random.sample(good_endbosses,len(good_endbosses))
            _endbosses = good_endbosses.copy()
            random.shuffle(_endbosses)
        my_boss = _endbosses.pop()
    elif (isinstance(boss,tuple) or isinstance(boss,list)):
        # if the boss is a boss tuple just roll with it
        my_boss = boss
    else:
        candidate_boss = [x for x in good_endbosses if x[0] == boss or x[1] == boss]
        if len(candidate_boss) <= 1:
            raise f"Boss not found: {boss}"
        my_boss = candidate_boss[0]
    mod.comment(f"gen_endboss: spawning {my_boss}")
    # make sure the spawn exists
    our_spawn = boss_spawns[my_boss[OPTIONS]["spawn"]]
    generate_spawn( our_spawn )
    # short_wave = wave.split("_")[-1]
    short_wave = missions[wavecode]
    set_wave_spawns_to( short_wave, [our_spawn["name"]] )
    # replace that wave with only our boss
    mod.comment(f"gen_mod({wave},{size},{[ (my_boss[BPCHAR], sspawn) for sspawn in spawners ]})")
    gen_mod(wave,size,[ (my_boss[BPCHAR], sspawn) for sspawn in spawners])
    # limit wave spawn to only 1
    # disabled temporarily
    limit_wave_to_n(short_wave,1)
    # buff our boss
    #if buff is not None:
    buff(my_boss)
    

    
        
# generate safe spawns (remove balconies)    
gen_safe_spawns()

def force_boss_drop(b=graveward):
    gen_endboss(boss=b,wave='/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1a_Trooper1',wavecode=111,spawners=["Factory_SpawnFactory_OakAI" for i in range (6)])
    gen_endboss(boss=b,wave='/Game/Enemies/_Spawning/Maliwan/_Mixes/Zone_1/SpawnOptions_KatagawaBallAdds_MeleeMix',wavecode=111,spawners=["Factory_SpawnFactory_OakAI" for i in range (6)])

def debug_make_tiny_waves():
    # limit the missions to very few
    for r in [1,2,3]:
        for w in [1,2,3,4]:
            for a in [1,2]:
                k = 100*r + 10*w + a
                if k in missions:
                    limit_wave_to_n(missions[k],1)
    
# generate the mobs
if args.json is None:
    default_mod(end_boss=True)
    # force_boss_drop(b=graveward)
    # nothing:    
    # added for debug
    # limit_wave_to_n(missions[111],1) # only 1 the first wave
    # limit_wave_to_n(missions[112],6)
    # limit_wave_to_n(missions[121],1)
    # limit_wave_to_n(missions[122],9)
    # limit_wave_to_n(missions[123],1) # this seems to be the drop ship phase
    # limit_wave_to_n(missions[131],6)
    # limit_wave_to_n(missions[132],3)
    # debug_make_tiny_waves()
else:
    data =json.load(open(args.json))
    mod.comment(f"Based on {args.json}")
    gen_mod_from_data(data)

# buff some of them
if toughen_mobs > 0.0:
    toughen_up_mobs(toughen_mobs)

mod.close()
