#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Boss Race Generator
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
import sys
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod
import random
sys.path.append('../boss-rush-slaughter')
import boss
OUTPUT='bossrace.bl3hotfix'
BPCHAR=1
IXORA_MAP = 'FrostSite_P'
SEED=42
our_seed = SEED
if our_seed is not None:
    random.seed(our_seed)


mod = Mod(OUTPUT,
          'Boss Race',
          'skruntskrunt',
          ["Turns Arm's Race into a weird boss rush"],
          lic=Mod.CC_BY_SA_40,
          v='0.1.0',
          cats='gameplay',
)

# @piggy:~/projects/bl3data/extracted_new/frost-site/pp$ for file in `cat SpawnOptions`; do echo; bash json-of.sh $file | fgrep jwp_object_name | sed -e "s#^#'$file',#"; done | fgrep Factory | sed -e 's/"_jwp_object_name" : //'
raw_ixora_spawn_list = [
    #('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "Factory_SpawnFactory_OakAI",0),
    #('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "SpawnFactory_OakAI_1",1),
    #('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "SpawnFactory_OakAI_2",2),
    #('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider_Adds',      "SpawnFactory_OakAI_3",3),
    #('/Ixora/Enemies/_Spawning/GearUpBoss/SpawnOptions_FrontRider',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/CotV/Tink/SpawnOptions_MaliTinkSuicide_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/CotV/Psycho/SpawnOptions_PsychoBadass_GearUp',      "SpawnFactory_OakAI_0"),
    ('/Ixora/Enemies/_Spawning/CotV/Psycho/SpawnOptions_MaliPsychoBasic_GearUp',      "SpawnFactory_OakAI_0"),
    ('/Ixora/Enemies/_Spawning/CotV/Punk/SpawnOptions_PunkBasic_GearUp',      "SpawnFactory_OakAI_0"),
    ('/Ixora/Enemies/_Spawning/CotV/Punk/SpawnOptions_PunkBadass_GearUp',      "SpawnFactory_OakAI_0"),
    ('/Ixora/Enemies/_Spawning/CotV/Punk/SpawnOptions_PunkSniper_GearUp',      "SpawnFactory_OakAI_0"),
    ('/Ixora/Enemies/_Spawning/CotV/Punk/SpawnOptions_PunkShotgunner_GearUp',      "SpawnFactory_OakAI_0"),
    ('/Ixora/Enemies/_Spawning/CotV/Punk/SpawnOptions_PunkAssaulter_GearUp',      "SpawnFactory_OakAI_0"),
    ('/Ixora/Enemies/_Spawning/CotV/Enforcer/SpawnOptions_MaliEnforcerGun_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/CotV/Enforcer/SpawnOptions_Enforcer_Reaper',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Frontrunner/SpawnOptions_Frontrunner_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Frontrunner/SpawnOptions_Nullhound_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Frontrunner/SpawnOptions_Gunwolf_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Frontrunner/SpawnOptions_CoVFrontrunner_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperJetpack_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperShotgun_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperFlash_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperMelee_Random_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperBasic_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_CoVTrooper_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperMedic_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Trooper/SpawnOptions_TrooperBadass_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Nog/SpawnOptions_NogNinja_GearUp',      "SpawnFactory_OakAI_0"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Nog/SpawnOptions_NogBasic_GearUp',      "SpawnFactory_OakAI_0"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Oversphere/SpawnOptions_CoVOversphere_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyBasic_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyAcidrain_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyGunner_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyPowerhouse_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyBadass_Random_GearUp',      "Factory_SpawnFactory_OakAI",0),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyBadass_Random_GearUp',      "SpawnFactory_OakAI_0",1),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyBadass_Random_GearUp',      "SpawnFactory_OakAI_1",2),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyBadass_Random_GearUp',      "SpawnFactory_OakAI_2",3),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_CoVHeavy_GearUp',      "Factory_SpawnFactory_OakAI"),
    ('/Ixora/Enemies/_Spawning/Maliwan/Heavy/SpawnOptions_HeavyIcebreaker_GearUp',      "Factory_SpawnFactory_OakAI"),
    #('/Ixora/Enemies/_Spawning/Skags/SpawnOptions_SkagBadass',      "SpawnFactory_OakAI_0"),
    #('/Ixora/Enemies/_Spawning/Skags/SpawnOptions_SkagAdultsAndBarfers',      "SpawnFactory_OakAI_0"),
    #('/Ixora/Enemies/_Spawning/Skags/SpawnOptions_SkagAdultsAndBarfers',      "SpawnFactory_OakAI_2"),
    #('/Ixora/Enemies/GearUpBoss/Pet/_Design/Character/SpawnOptions_FrontRider_Pet',      "Factory_SpawnFactory_OakAI"),
    #('/Ixora/Enemies/GearUpBoss/Rider/_Design/Character/SpawnOptions_FrontRider_Rider',      "Factory_SpawnFactory_OakAI"),
    #('/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/SpawnOptions_FrontRider_Mount',      "Factory_SpawnFactory_OakAI"),
]
ixora_spawnoptions = dict()
for entry in  raw_ixora_spawn_list:
    row,factory = entry[0:2]
    l = ixora_spawnoptions.get(row,list())
    l.append(factory)
    ixora_spawnoptions[row]=l

def get_bpchar(s):
    return s.split('/')[-1]
    
for entry in raw_ixora_spawn_list:
    idx = 0
    if (len(entry) == 3):
        row, factory, idx = entry
    else:
        row,factory = entry
    so = row
    # 'Options.Options[{}].Factory.Object..AIActorClass'.format(rev(c,idx))
    mob = random.choice(boss.safe_bosses)
    bpchar = mob[BPCHAR]
    mod.comment(f"so:{row} factory:{factory} bpchar:{bpchar}")
    mod.reg_hotfix(Mod.EARLYLEVEL,
                   IXORA_MAP,
                   row,
                   #f'{row}.{factory}',
                   #f'{factory}.AIActorClass',
                   #'AIActorClass',
                   f'Options.Options[{idx}].Factory.Object..AIActorClass',
                   f"BlueprintGeneratedClass'{bpchar}.{get_bpchar(bpchar)}_C'",
    )

mod.close()
