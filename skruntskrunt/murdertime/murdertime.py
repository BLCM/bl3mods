#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Murdercane Timer Generator
# Copyright (C) 2021 abram/skruntksrunt, Christopher J. Kucera
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

import json
import sys
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod
import random
sys.path.append('../boss-rush-slaughter')
sys.path.append('../bossrace')
import boss
import ixorabosses
import argparse
import pandas

OUTPUT='murdercanetimer.bl3hotfix'
BPCHAR=1
IXORA_MAP = 'FrostSite_P'
SEED=42 # 42
our_seed = SEED
version = '0.1.0'
title = 'MurdercaneTime'
MURDERCSV='murdertime.csv'

def parse_args():
    parser = argparse.ArgumentParser(description=f'{title}: MurderCane Time Change v{version}')
    parser.add_argument('--seed', type=int, default=SEED, help='Seed of random number generator.')
    parser.add_argument('--output', type=str, default=OUTPUT, help='Hotfix output file')
    parser.add_argument('--csv', type=str, default=MURDERCSV, help='Timing CSV File (index (0 to 5), stable (seconds), transition (seconds), radius (units))')
    return parser.parse_args()

args = parse_args()
our_seed = args.seed
if our_seed is None:
    our_seed = random.randint(0,2**32-1)
else:
    our_seed = int(our_seed)
random.seed(our_seed)

murdertime = pandas.read_csv(args.csv)

DFL_LEVEL=Mod.EARLYLEVEL
output_filename = args.output
new_title = f'{title}_{args.csv}'
mod = Mod(output_filename,
          new_title,
          'skruntskrunt',
          ["Change MurderCane Timing"],
          lic=Mod.CC_BY_SA_40,
          v=version,
          cats=['armsrace'],
)

mod.comment(f"Seed {our_seed}")
mod.comment(f"CSV  {args.csv}")
FROSTPATH="/Game/PatchDLC/Ixora/GameData/Mode/FrostSiteGearUpData.FrostSiteGearUpData"
STABLE="StableSeconds"
TRANSITION="TransitionSeconds"
RADIUS="Radius"
DEATHCIRCLE=['DeathCircleStages.DeathCircleStages[','].','.BaseValueConstant',]
MAXI= 5

# INDICES     = [     0,     1,     2,     3,    4,    5]
# STABLES     = [   180,   270,   240,   120,   60,    0]
# TRANSITIONS = [   150,   120,    90,    60,   30,   30]
# RADII       = [140000, 39000, 27500, 16000, 8000, 1900]


def deathcircle_template(index,arg):
    return f'DeathCircleStages.DeathCircleStages[{index}].{arg}.BaseValueConstant'


def deathcircle(mod,index=0,stable=180,transition=150,radius=140000):
    mod.reg_hotfix(Mod.EARLYLEVEL,
                   IXORA_MAP,
                   FROSTPATH,
                   deathcircle_template(index,STABLE),
                   stable
    )
    mod.reg_hotfix(Mod.EARLYLEVEL,
                   IXORA_MAP,
                   FROSTPATH,
                   deathcircle_template(index,TRANSITION),
                   transition
    )
    mod.reg_hotfix(Mod.EARLYLEVEL,
                   IXORA_MAP,
                   FROSTPATH,
                   deathcircle_template(index,RADIUS),
                   radius
    )

def generate_murdertime_mod(mod, murdertime):
    for i in range(MAXI+1):
        deathcircle(mod, index=i,
                    stable=murdertime["stable"][i],
                    transition=murdertime["transition"][i],
                    radius=murdertime["radius"][i])

generate_murdertime_mod(mod, murdertime)
