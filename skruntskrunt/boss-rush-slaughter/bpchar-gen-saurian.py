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
    # '/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Badass/BPChar_VarkidHunt02_Badass',
    # '/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Adult/BPChar_VarkidHunt02_AdultA',
    # '/Game/Enemies/Varkid/_Unique/Hunt01/_Design/Character/BPChar_VarkidHunt01',
    '/Game/Enemies/Varkid/SuperBadass/_Design/Character/BPChar_VarkidSuperBadass',
    '/Game/Enemies/Varkid/Badass/_Design/Character/BPChar_VarkidBadass'
]
bugs = flatten([matching_bosses(x) for x in bugs_names]) + more_bugs

previous = {}

pools = {
    'round1':flatten([
        matching_bosses('Pyschobillies'),
        matching_bosses('Force Trooper'),
        dinosaurs
    ]),
    'round2':flatten([
        matching_bosses('Pyschobillies'),
        maliwans,
        bugs,
    ]),
    'round3':flatten([
        matching_bosses('Wick'),
        matching_bosses('Warty'),
        matching_bosses('DEGEN-3'),
        matching_bosses('Yeti'),
        maliwans,
        dinosaurs

    ]),
    'round4':flatten([
        matching_bosses('Pyschobillies'),
        matching_bosses('Traunt'),
        matching_bosses('Warden'),
        maliwans,
        bugs,
    ]),
    'round5':flatten([
        matching_bosses('Pyschobillies'),
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


