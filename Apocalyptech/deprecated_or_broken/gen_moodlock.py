#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
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
import enum
sys.path.append('../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod

data = BL3Data()

class Mood(enum.Enum):
    """
    /Game/NonPlayerCharacters/_Shared/Animation/MoodActions/Action_Mood_*
    """
    Amazed='Amazed'
    Angry='Angry'
    Bored='Bored'
    Confused='Confused'
    Determined='Determined'
    Disgusted='Disgusted'
    Embarrased='Embarrased'
    Flirty='Flirty'
    GrossedOut='GrossedOut'
    Guilty='Guilty'
    Happy='Happy'
    Nervous='Nervous'
    Neutral='Neutral'
    Paranoid='Paranoid'
    Relaxed='Relaxed'
    Sad='Sad'
    Satisfied='Satisfied'
    Scared='Scared'
    Stressed='Stressed'
    Suffering='Suffering'
    Surprised='Surprised'
    Unimpressed='Unimpressed'

    def path(self):
        global mod
        return mod.get_full_cond('/Game/NonPlayerCharacters/_Shared/Animation/MoodActions/Action_Mood_{}.Action_Mood_{}_C'.format(self.value, self.value), 'BlueprintGeneratedClass')

for mood in Mood:

    mod = Mod('moodlock_{}.txt'.format(mood.value.lower()),
            'Moodlock: {}'.format(mood.value),
            'Apocalyptech',
            [
                "Sets NPC 'mood' during dialogue to '{}'.  This effect".format(mood.value),
                "is actually pretty subtle mostly, and I don't think it does",
                "anything during cutscenes.  Also, NPCs seem to revert to a",
                "neutral expression between lines anyway, even with the 'Neutral'",
                "mood updated.  Not really worth officially releasing, IMO.",
                ],
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.0.0b1',
            cats='joke',
            )

    # Update all moods to be the one that we want
    actions_obj = '/Game/NonPlayerCharacters/_Shared/Animation/MoodActions/NametagTable_MoodActions'
    obj = data.get_data(actions_obj)[0]
    for idx, mood_data in enumerate(obj['MoodData']):
        mod.reg_hotfix(Mod.PATCH, '',
                actions_obj,
                'MoodData.MoodData_Value[{}].Action'.format(idx),
                mood.path(),
                )

    # Original method; sets basically every single DialogScript line to
    # use the mood.  Generates a 28MB file.  Just keeping this around for
    # posterity; the other method is a lot better.
    if False:

        dialogscript_to_bpchar = {}
        for obj_name in data.find('', 'BPChar_'):
            short_name = obj_name.split('/')[-1]
            bpchar = data.get_data(obj_name)
            for export in bpchar:
                if export['export_type'] == 'BlueprintGeneratedClass' and export['_jwp_object_name'].startswith('BPChar_'):
                    if 'InheritableComponentHandler' in export:
                        ihc = bpchar[export['InheritableComponentHandler']['export']-1]
                        if 'Records' in ihc:
                            for record in ihc['Records']:
                                if record['ComponentClass'][0] == 'OakDialogComponent':
                                    ct = bpchar[record['ComponentTemplate']['export']-1]
                                    if 'DialogScripts' in ct:
                                        for ds in ct['DialogScripts']:
                                            if 'export' not in ds:
                                                ds_obj = ds[1]
                                                if ds_obj not in dialogscript_to_bpchar:
                                                    dialogscript_to_bpchar[ds_obj] = set([short_name])
                                                else:
                                                    dialogscript_to_bpchar[ds_obj].add(short_name)

        def process_dialogscript(mod, data, obj_name, mood, bpchars=None):
            mod.header(obj_name)
            fstring = 'TimeSlots.Timeslots[{}].Object..Lines.Lines[{}].Object..Performances.Performances[{}].Object..MoodName'
            obj = data.get_data(obj_name)
            for export in obj:
                if export['export_type'] == 'DialogScriptData':
                    if 'TimeSlots' in export:
                        for timeslot_idx, timeslot_ref in enumerate(export['TimeSlots']):
                            timeslot = obj[timeslot_ref['export']-1]
                            for line_idx, line_ref in enumerate(timeslot['Lines']):
                                line = obj[line_ref['export']-1]
                                for performance_idx, performance_ref in enumerate(line['Performances']):
                                    if bpchars is None:
                                        mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                                                obj_name,
                                                fstring.format(
                                                    timeslot_idx,
                                                    line_idx,
                                                    performance_idx,
                                                    ),
                                                mood,
                                                )
                                    else:
                                        for bpchar in sorted(bpchars):
                                            mod.reg_hotfix(Mod.CHAR, bpchar,
                                                    obj_name,
                                                    fstring.format(
                                                        timeslot_idx,
                                                        line_idx,
                                                        performance_idx,
                                                        ),
                                                    mood,
                                                    )
                    break

        for obj_name, bpchars in dialogscript_to_bpchar.items():
            process_dialogscript(mod, data, obj_name, mood, bpchars)

        for obj_name in data.find('', 'DialogScript_'):
            if obj_name not in dialogscript_to_bpchar:
                process_dialogscript(mod, data, obj_name, mood)

    mod.close()

