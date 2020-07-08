#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
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

import random
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('all_anointed.txt',
        'All Anointed',
        'Apocalyptech',
        [
            "Mostly just a joke mod, wanted to turn all enemies into Anointed.  This only",
            "does anything in Covenant Pass.  There's a commented bit at the bottom which",
            "will instead turn every enemy (besides Shiv) in Covenant Pass into Wotan, instead",
            "which is fun.  Unfortunately a few of them don't spawn (or maybe spawn but fall",
            "through the level geometry) in the second arena so you can't actually get to",
            "the Shiv fight with all-Wotans going on, or at least I couldn't on my one test.",
        ],
        lic=Mod.CC_BY_SA_40,
        )

data = BL3Data()

level = 'Recruitment_P'
anoint_punk = '/Game/Enemies/Punk_Female/Anointed/_Design/Character/BPChar_Punk_Anointed.BPChar_Punk_Anointed_C'
anoint_enforcer = '/Game/Enemies/Enforcer/Anointed/_Design/Character/BPChar_EnforcerAnointed.BPChar_EnforcerAnointed_C'
anoint_goliath = '/Game/Enemies/Goliath/Anointed/_Design/Character/BPChar_Goliath_Anointed.BPChar_Goliath_Anointed_C'
anoint_tink = '/Game/Enemies/Tink/Anointed/_Design/Character/BPChar_TinkAnointed.BPChar_TinkAnointed_C'
anoint_psycho = '/Game/Enemies/Psycho_Male/Anointed/_Design/Character/BPChar_PsychoAnointed.BPChar_PsychoAnointed_C'
anoint_goon = '/Game/Enemies/Goon/Anointed/_Design/Character/BPChar_GoonAnointed.BPChar_GoonAnointed_C'
anointeds = set([
    anoint_punk,
    anoint_enforcer,
    anoint_goliath,
    anoint_tink,
    anoint_psycho,
    anoint_goon,
    ])
anointed_mapping = {
        '/Game/Enemies/Psycho_Male/Basic/_Design/Character/BPChar_PsychoBasic.BPChar_PsychoBasic_C': anoint_psycho,
        '/Game/Enemies/Psycho_Male/_Unique/InfectedOnes/_Design/Character/BPChar_PsychoInfectedOnes.BPChar_PsychoInfectedOnes_C': anoint_psycho,
        '/Game/Enemies/Psycho_Male/_Unique/Prologue/_Design/Character/BPChar_PsychoPrologue.BPChar_PsychoPrologue_C': anoint_psycho,
        '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C': anoint_punk,
        '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadassArmored.BPChar_PunkBadassArmored_C': anoint_punk,
        '/Game/Enemies/Punk_Female/Basic/_Design/Character/BPChar_PunkBasic.BPChar_PunkBasic_C': anoint_punk,
        '/Game/Enemies/Punk_Female/_Unique/Prologue/_Design/Character/BPChar_PunkPrologue.BPChar_PunkPrologue_C': anoint_punk,
        '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C': anoint_tink,
        '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadassArmored.BPChar_TinkBadassArmored_C': anoint_tink,
        '/Game/Enemies/Tink/Basic/_Design/Character/BPChar_TinkBasic.BPChar_TinkBasic_C': anoint_tink,
        '/Game/Enemies/Tink/Loot/_Design/Character/BPChar_TinkLoot.BPChar_TinkLoot_C': anoint_tink,
        '/Game/Enemies/Tink/Shotgun/_Design/Character/BPChar_TinkShotgun.BPChar_TinkShotgun_C': anoint_tink,
        }

spawnoptions = set([
    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_Prologue',
    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_NoTinks_Prologue',
    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_PrologueBadass',
    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_Sacrifice',
    '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoV_Prologue_Recruitment',
    ])
seen = set()
added_more = True
while added_more:
    added_more = False

    for obj_name in list(spawnoptions):

        if obj_name not in seen:

            seen.add(obj_name)

            all_exports = data.get_data(obj_name)
            optiondata = data.get_exports(obj_name, 'SpawnOptionData')[0]

            for idx, option in enumerate(optiondata['Options']):
                export_idx = option['Factory']['export']
                factory = all_exports[export_idx-1]
                if 'AIActorClass' in factory:
                    orig_class = factory['AIActorClass']['asset_path_name']
                    if orig_class not in anointeds:
                        if orig_class in anointed_mapping:
                            mod.reg_hotfix(Mod.EARLYLEVEL, level,
                                    obj_name,
                                    'Options.Options[{}].Factory.Object..AIActorClass'.format(idx),
                                    # Bit of a laugh here; turn everything into Wotan, instead.
                                    #Mod.get_full_cond('/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/_Design/Character/BPChar_BehemothRaid.BPChar_BehemothRaid_C', 'BlueprintGeneratedClass'))
                                    Mod.get_full_cond(anointed_mapping[orig_class], 'BlueprintGeneratedClass'))
                        else:
                            print('Unknown class: {}'.format(orig_class))
                elif 'Options' in factory:
                    spawnoptions.add(factory['Options'][1])
                    added_more = True
                else:
                    raise Exception('bzort')

mod.close()
