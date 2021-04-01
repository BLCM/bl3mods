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
import random
import json
import boss
from boss import choose_random_slaughter_boss as random_boss
SEED = random.randint(0,2**31-1)
INPUT_FILE="example_bpchars.json"
OUTPUT_FILE="gen_bpchars_saurian.json"
OUTPUT_POOL_FILE="gen_bpchars_saurian.pool.json"

def parse_args():
    parser = argparse.ArgumentParser(description='Boss Rush 3000 Slaughter Generator')
    parser.add_argument('--input', type=str, default=INPUT_FILE,
                        help=f'Input template file')
    parser.add_argument('--seed', type=int, default=SEED, help='Seed of random number generator.')
    parser.add_argument('--json', type=str, default=OUTPUT_FILE, help='JSON Output File')
    parser.add_argument('--nomix', action='store_true', default=False, help="Don't use original hyperion slaughter shaft mix")
    return parser.parse_args()

args = parse_args()
data = json.load(open(args.input))
rounds = ["round1","round2","round3","round4","round5"]
# keep the original mix, or keep it super random
maintain_mix = not args.nomix
seed = int(args.seed)
output_filename = args.json
random.seed(seed)

def flatten(l):
    return [item for sl in l for item in sl]

def matching_bosses(substring, bosses=boss.safe_bosses):
    return [boss[1] for boss in bosses if substring in boss[0]]

def matching_bosses_exact(substring, bosses=boss.safe_bosses):
    return [boss[1] for boss in bosses if substring == boss[0]]

all_safe_bosses = [boss[1] for boss in boss.safe_bosses]

dinosaur_names = ['Minosaur','IndoTyrant','Tyrant of Instinct','Abbadoxis','Chonk Stomp','Ipswitch Dunne','Tremendous Rex']

# maybe GerSaurianHamatarus is bad?
# or SaurianLaser
more_saurians = [
    '/Geranium/Enemies/GerSaurian/HamtaurusBadass/_Design/Character/BPChar_GerSaurianHamtaurusBadass',
    '/Geranium/Enemies/GerSaurian/Hamtaurus/_Design/Character/BPChar_GerSaurianHamtaurus',
    '/Geranium/Enemies/GerSaurian/Tyrant/_Design/Character/BPChar_GerSaurianTyrant',
    '/Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_HamBadass',
    '/Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_Tyrant',
    '/Geranium/Enemies/GerSaurian/Predator/_Design/Character/BPChar_GerSaurianPredator',
    '/Game/Enemies/Saurian/_Unique/Laser/_Design/Character/BPChar_SaurianLaser',
    '/Game/Enemies/Saurian/_Unique/Queen/_Design/Character/BPChar_SaurianQueen',
    '/Game/Enemies/Saurian/_Unique/Shield/_Design/Character/BPChar_SaurianShield',
    '/Game/PatchDLC/Event2/Enemies/Tiny/Psycho/Badass/_Design/Character/BPChar_PsychoBadassTinyEvent2',
    '/Game/PatchDLC/Event2/Enemies/Cyber/Trooper/Capo/_Design/Character/BPChar_CyberTrooperCapo',
    '/Game/PatchDLC/Event2/Enemies/Cyber/Punk/TechLt/_Design/Character/BPChar_PunkCyberLt',
    '/Game/PatchDLC/Event2/Enemies/Meat/Punk/RoasterLT/_Design/Character/BPChar_Punk_Roaster',
    '/Game/PatchDLC/Event2/Enemies/Meat/Tink/TenderizerLt/_Design/Character/BPChar_Tink_Tenderizer',
    '/Game/PatchDLC/Event2/Enemies/Tiny/Trooper/Badass/_Design/Character/BPChar_TrooperBadassTinyEvent2',
]

dinosaurs = flatten([matching_bosses(x) for x in dinosaur_names]) + more_saurians
# override
#dinosaurs = ['/Game/Enemies/Saurian/_Unique/Laser/_Design/Character/BPChar_SaurianLaser']
#dinosaurs = [ '/Geranium/Enemies/GerSaurian/Hamtaurus/_Design/Character/BPChar_GerSaurianHamtaurus' ]

maliwan_names = [
    'Force Trooper',
    'Rax',
    'Beans',
    'Archer Rowe',
    'Atomic',
    'Sylestro'
]
maliwans = flatten([matching_bosses(x) for x in maliwan_names]) + matching_bosses_exact('Max')
bugs_names = ['Crawly','Wanette','Antalope','Princess Tarantella II',]
more_bugs = [
    '/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Badass/BPChar_VarkidHunt02_Badass',
    '/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Adult/BPChar_VarkidHunt02_AdultA',
    '/Game/Enemies/Varkid/_Unique/Hunt01/_Design/Character/BPChar_VarkidHunt01',
    '/Game/Enemies/Varkid/SuperBadass/_Design/Character/BPChar_VarkidSuperBadass',
    '/Game/Enemies/Varkid/Badass/_Design/Character/BPChar_VarkidBadass'
]
bugs = flatten([matching_bosses(x) for x in bugs_names]) + more_bugs

newbosses = """/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_PsychoShark
/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_DoubleDownDomina
/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_GorgeousRoger
/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_BomberGary
/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_MachineGunMikey
/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_Yvan
/Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part3/_Design/Character/BPChar_DoItForDigby_SteelDragon
/Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part2/Character/BPChar_DoItForDigby_BloodBucket
/Dandelion/Enemies/Looters/_Unique/MeetTimothy/_Design/Character/BPChar_MeetTimothy_ThirdRail
/Dandelion/Enemies/Looters/_Unique/GreatEscape/_Design/Character/BPChar_GreatEscape_Rudy
/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_TinkBadass_Giorgio
/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_EnforcerBadass_Lawrence
/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_GoonBadass_Coco
/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_PunkBadass_Gaudy
/Dandelion/Enemies/Looters/_Unique/RegainingOnesFeet/_Design/Character/BPChar_RegainingFeet_GoldenBullion
/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeJacket
/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeSlacks
/Dandelion/Enemies/Looters/_Unique/ThePlan/_Design/Character/BPChar_ThePlan_TricksyNick
/Dandelion/Enemies/Looters/_Unique/OneMansTrash/_Design/Character/BPChar_OneMansTrash_TonyBordel
/Dandelion/Enemies/ServiceBot/Unique_Janitor/_Design/Character/BPChar_CasinoBot_BigJanitor
/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion
/Dandelion/Enemies/Loader/_Unique/VIPOnly/Petunia_FreddieBot/_Design/Character/BPChar_VIPOnly_Petunia
/Dandelion/Enemies/Loader/_Unique/AcidTrip/EarlyPrototypes/_Design/Character/BPChar_AcidTrip_EarlyPrototype
/Dandelion/Enemies/Loader/_Unique/AcidTrip/Facemelt/_Design/Character/BPChar_AcidTrip_Facemelt
/Dandelion/Enemies/Loader/_Unique/Impound/_Design/Character/BPChar_BudLoader
/Dandelion/Enemies/Loader/_Unique/BrotherlyLove/_Design/Character/BPChar_SisterlyLove_DebtCollectorLoader
/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/BPChar_FrontRider_Mount
/Alisma/Enemies/DrBenedict/_Shared/_Design/Character/BPChar_DrBenedict
/Ixora/Enemies/CotV/Enforcer/Reaper/_Design/Character/BPChar_Enforcer_Reaper
/Alisma/Enemies/AliEnforcer/_Unique/GeneralBlisterPuss/BPChar_GeneralBlisterPuss
/Alisma/Enemies/AliEnforcer/_Unique/TheBlackRook/BPChar_AliEnforcer_TheBlackRook
/Alisma/Enemies/BulletRider/_Unique/AP/_Design/Character/BPChar_BulletRider_AP
/Alisma/Enemies/_Unique/SpongeBoss/_Design/Character/BPChar_SpongeBoss
/Alisma/Enemies/Constructor/_Unique/SecuritySergeant/_Design/Character/BPChar_Constructor_SecuritySergeant
/Alisma/Enemies/Constructor/_Unique/SecurityChief/_Design/Character/BPChar_Constructor_SecurityChief
/Alisma/Enemies/AliPsycho/_Unique/TheBlackKing/_Design/Character/BPChar_AliPsycho_TheBlackKing
/Alisma/Enemies/HyperionPunk/_Unique/TheWarden/_Design/Character/BPChar_HyperionPunk_TheWarden""".split("\n")

allbosses = newbosses + all_safe_bosses

previous = {}

pools = {
    'round1':flatten([
        allbosses,
        dinosaurs
    ]),
    'round2':flatten([
        allbosses,
        bugs,
    ]),
    'round3':flatten([
        matching_bosses('Wick'),
        matching_bosses('Warty'),
        matching_bosses('DEGEN-3'),
        matching_bosses('Yeti'),
        allbosses,
        dinosaurs

    ]),
    'round4':flatten([
        matching_bosses('Traunt'),
        matching_bosses('Warden'),
        bugs,
    ]),
    'round5':flatten([
        allbosses,
        matching_bosses('Traunt'),
        matching_bosses('Warden'),
        matching_bosses('Killavolt'),
        dinosaurs
    ]),
}

json.dump(pools,open(OUTPUT_POOL_FILE,"w"),indent=4)


def get_boss_from_pool(spawn_name,round_pool):
    """ cache spam names """
    if not maintain_mix:
        return random.choice(round_pool)
    if not spawn_name in previous:
        previous[spawn_name] = random.choice(round_pool)
    return previous[spawn_name]



def get_boss(spawn_name,round_name, wave_name):
    """ cache spam names """
    return get_boss_from_pool(spawn_name,pools[round_name])


for curr_round_name in rounds:
    curr_round = data[curr_round_name]
    waves = [x for x in curr_round.keys() if x[0] == '/']
    for wave_name in waves:
        wave = curr_round[wave_name]
        for spawn in wave:
            spawn_name = spawn[0]
            spawn[0] = get_boss(spawn_name,curr_round_name,wave_name)
 
data["seed"] = seed
json.dump(data,open(output_filename,"w"),indent=4)


