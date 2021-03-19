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
OUTPUT_FILE="gen_bpchars.json"
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

previous = {}
def get_boss(spawn_name):
    """ cache spam names """
    if not maintain_mix:
        return random_boss()[1]
    if not spawn_name in previous:
        previous[spawn_name] = random_boss()[1]
    return previous[spawn_name]
    


for curr_round_name in rounds:
    curr_round = data[curr_round_name]
    waves = [x for x in curr_round.keys() if x[0] == '/']
    for wave_name in waves:
        wave = curr_round[wave_name]
        for spawn in wave:
            spawn_name = spawn[0]
            spawn[0] = get_boss(spawn_name)
 
data["seed"] = seed
json.dump(data,open(output_filename,"w"),indent=4)


