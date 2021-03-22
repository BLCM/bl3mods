#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2021 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

import sys
import random
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod

### Config params
#level = 'MotorcadeFestival_P'
#spawnoptions = set([
#    # This actually isn't *every* spawn in Carnivora -- leaves out gameshow stuff, etc.
#    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeFestival_FullMix',
#    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeFestival_NoGoons',
#    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeInteriorAndFestival_TinksOnly',
#    '/Game/Enemies/_Spawning/CotV/Punks/Variants/SpawnOptions_PunkBasic',
#    ])
level = 'Desertvault_P'
spawnoptions = set([
    '/Game/Enemies/Goliath/_Shared/_Design/SpawnStyles/PortaPotty/SpawnOptions_GoliathBasic_Enraged_PortaPotty',
    '/Game/Enemies/_Spawning/CotV/Enforcers/_Unique/SpawnOptions_EnforcerAnointedDesertVault',
    '/Game/Enemies/_Spawning/CotV/Enforcers/Variants/SpawnOptions_EnforcerBadass',
    '/Game/Enemies/_Spawning/CotV/Enforcers/Variants/SpawnOptions_EnforcerBruiser',
    '/Game/Enemies/_Spawning/CotV/Goliaths/Variants/SpawnOptions_GoliathBadass',
    '/Game/Enemies/_Spawning/CotV/Goons/_Unique/SpawnOptions_GoonAnointedDesertVault',
    '/Game/Enemies/_Spawning/CotV/Goons/_Unique/SpawnOptions_Goon_Bounty01',
    '/Game/Enemies/_Spawning/CotV/Goons/Variants/SpawnOptions_GoonBadass',
    '/Game/Enemies/_Spawning/CotV/_Mixes/SpawnOptions_CotVAllSmalls',
    '/Game/Enemies/_Spawning/CotV/_Mixes/SpawnOptions_CotVPunksAndPsychos',
    '/Game/Enemies/_Spawning/CotV/_Mixes/SpawnOptions_CotVPunksAndPsychosAndTinks',
    '/Game/Enemies/_Spawning/CotV/_Mixes/SpawnOptions_CotvPunksAndTinks',
    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_City',
    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVault',
    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Mine/SpawnOptions_CotV_MineTinkMix',
    '/Game/Enemies/_Spawning/CotV/Psychos/_Mixes/SpawnOptions_PsychoMix',
    '/Game/Enemies/_Spawning/CotV/Psychos/_Unique/SpawnOptions_PsychoAnointedDesertVault',
    '/Game/Enemies/_Spawning/CotV/Psychos/Variants/SpawnOptions_PsychoAnointedMale',
    '/Game/Enemies/_Spawning/CotV/Psychos/Variants/SpawnOptions_PsychoBasic',
    '/Game/Enemies/_Spawning/CotV/Psychos/Variants/SpawnOptions_PsychoSuicideMale',
    '/Game/Enemies/_Spawning/CotV/Punks/_Mixes/SpawnOptions_PunkMix',
    '/Game/Enemies/_Spawning/CotV/Punks/Variants/SpawnOptions_PunkBasic',
    '/Game/Enemies/_Spawning/CotV/Tinks/Variants/SpawnOptions_TinkBadass',
    '/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Spawning/SpawnOptions_AtlasSoldierFodderMIx',
    ])

bpchar_to_spawn = '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/_Design/Character/BPChar_BehemothRaid'
#bpchar_to_spawn = '/Game/Enemies/PrometheaBoss/Rampager/_Design/Character/BPChar_Rampager'
#bpchar_to_spawn = '/Game/Enemies/Enforcer/Anointed/_Design/Character/BPChar_EnforcerAnointed'
#bpchar_to_spawn = '/Game/Enemies/Skag/Pup/_Design/Character/BPChar_SkagPup'
#bpchar_to_spawn = '/Game/Enemies/Ratch/_Unique/SpaceSlug/_Design/Character/BPChar_RatchSpaceSlug'

### Massage the bpchar into a full object reference
last_bit = bpchar_to_spawn.split('/')[-1]
bpchar_to_spawn_full = Mod.get_full_cond('{}.{}_C'.format(bpchar_to_spawn, last_bit), 'BlueprintGeneratedClass')

### Start the mod
mod = Mod('testing_enemy_spawns.bl3hotfix',
        'Testing Enemy Spawns',
        'Apocalyptech',
        [
            "Turns all spawns in {} into {}.".format(level, last_bit),
            "Update the generation script to suit!",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='resource',
        )

data = BL3Data()

seen = set()
added_more = True
while added_more:
    added_more = False

    for obj_name in sorted(list(spawnoptions)):

        if obj_name not in seen:

            print('Processing {}...'.format(obj_name))
            mod.comment(obj_name)
            seen.add(obj_name)

            all_exports = data.get_data(obj_name)
            optiondata = data.get_exports(obj_name, 'SpawnOptionData')[0]

            for idx, option in enumerate(optiondata['Options']):
                export_idx = option['Factory']['export']
                factory = all_exports[export_idx-1]
                if 'AIActorClass' in factory:
                    mod.reg_hotfix(Mod.EARLYLEVEL, level,
                            obj_name,
                            'Options.Options[{}].Factory.Object..AIActorClass'.format(idx),
                            bpchar_to_spawn_full)
                elif 'Options' in factory:
                    spawnoptions.add(factory['Options'][1])
                    added_more = True
                else:
                    raise Exception('bzort')

            mod.newline()

mod.close()

