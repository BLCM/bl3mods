#!/usr/bin/env python
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

# Given a balance, interactively choose parts to generate partlock mods.

import os
import sys
import colorama
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF, Balance, PartCategory, Part

_version = '1.1.0'

try:
    balance_name = sys.argv[1]
except IndexError:
    print('Specify a full Balance path as the argument to this script!')
    sys.exit(1)
bal_last = balance_name.split('/')[-1]
colorama.init(autoreset=True)

# TODO: these are all optimized for my usual black-text-on-white-bg terms
color_error = colorama.Fore.RED
color_choices = colorama.Fore.BLUE
color_choices_extra = colorama.Fore.BLUE + colorama.Style.DIM + colorama.Back.WHITE
color_commands = colorama.Fore.CYAN
color_actions = colorama.Fore.GREEN
color_relation = colorama.Fore.BLACK + colorama.Style.BRIGHT
color_partinfo = colorama.Fore.YELLOW + colorama.Style.DIM
color_header = colorama.Style.BRIGHT
color_reset = colorama.Style.RESET_ALL
color_never_spawn = colorama.Fore.RED
color_success = colorama.Fore.GREEN + colorama.Style.DIM

# Anointments which have been removed from the spawn pool, as of the 2020-07-23 update.
# The anointments still *exist*, but no new dropped gear will have them, because a
# hotfix has set their MinGameStage to 100.
disabled_anointments = {
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_AccuracyHandling/GPart_All_SkillEnd_AccuracyHandling',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_CritDamage/GPart_All_SkillEnd_CritDamage',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_FireRateReload/GPart_All_SkillEnd_FireRateReload',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_MoveSpeed/GPart_All_SkillEnd_MoveSpeed',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_ProjectileSpeed/GPart_All_SkillEnd_ProjectileSpeed',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NoAmmoConsumption/GPart_Gunner_NoAmmoConsumption',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_AccuracyCrit/GPart_Siren_Grasp_AccuracyCrit',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_DamageReduction/GPart_Siren_Slam_DamageReduction',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_ReturnDamage/GPart_Siren_Slam_ReturnDamage',
        '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_SlideRegenShields/GPart_All_SlideRegenShields',
        '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_CyberSpike/GPart_EG_Gen_SkillEnd_CyberSpike',
        '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_DamageMitigation/GPart_All_DamageMitigation',
        '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_ShockFeedback/GPart_All_ShockFeedback',
        '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillEnd_HealingPool/GPart_All_HealingPool',
        '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/AccuracyAndHandling/GPart_EG_WhileAirborn_AccuracyHandling',
        '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/CritDamage/GPart_EG_WhileAirborn_CritDamage',
        '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/Damage/GPart_EG_WhileAirborn_Damage',
        '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/FireRate/GPart_EG_WhileAirborn_FireRate',
        '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/AccuracyAndHandling/GPart_EG_WhileSliding_AccuracyHandling',
        '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/Damage/GPart_EG_WhileSliding_Damage',
        '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/FireRate/GPart_EG_WhileSliding_FireRate',
        }

class Relation:
    """
    Mostly just a glorified dict
    """

    def __init__(self, excluders, dependencies):
        self.excluders = excluders
        self.dependencies = dependencies

class CategoryInfo:
    """
    Mostly just a glorified dict
    """

    def __init__(self, data, bal, cat, start_part_idx, cat_idx=None, cat_name=None):
        self.bal = bal
        self.cat = cat
        self.cat_idx = cat_idx
        if cat_name is None:
            self.cat_name = self.compute_category_name(data)
        else:
            self.cat_name = cat_name
        self.start_part_idx = start_part_idx

    def compute_category_name(self, data):

        # No way to tell if there's no parts
        if len(self.cat.partlist) == 0:
            return '(no parts)'

        # Construct a default using the short name of the first real part,
        # if we can.  (If we don't find one, then there's no real parts
        # in here anyway.)
        default_label = None
        for part in self.cat.partlist:
            if part.short_name:
                default_label = part.short_name
                break
        if not default_label:
            return '(empty category)'

        # If we don't have a bal_name or cat_idx, just abort.  This
        # would only happen with our Anointment stuff anyway.
        if not self.bal.bal_name or self.cat_idx is None:
            return '(unknown)'

        # Make an attempt at figuring it out
        cat_name = data.get_parts_category_name(
                [p.part_name for p in self.cat.partlist],
                self.bal.bal_name,
                self.cat_idx,
                )
        if cat_name:
            return cat_name
        else:
            return default_label

class Action:
    """
    What we're going to do, modwise
    """

    (ALWAYS, NEVER) = range(2)

    def __init__(self, action, part, list_idx):
        self.action = action
        self.part = part
        self.list_idx = list_idx

    def text_short(self):
        if self.action == Action.ALWAYS:
            return 'Always spawn'
        else:
            return 'Never spawn'

    def text_long(self):
        return '{} {}'.format(self.text_short(), self.part.short_name)

class AnointPart(Part):
    """
    An ever-so-slightly fancier `bl3hotfixmod.Part` class which also contains
    information about which anointment object it comes from (will be the
    Balance itself, for anointments that are right on the balance).
    """

    def __init__(self, part_name, anoint_source, weight=1):
        super().__init__(part_name, weight=weight)
        self.anoint_source = anoint_source

def prompt():
    sys.stdout.write('> ')
    sys.stdout.flush()
    data = sys.stdin.readline().strip().lower()
    print('')
    return data

def error(msg):
    global color_error
    print('{}{}'.format(color_error, msg))
    print('')

def save_mod(save_filename):
    """
    Save out a mod file.  This actually relies on an awful lot of global variables.
    Apologies.
    """
    mod = Mod(save_filename,
            'Arbitrary Partlocks: {}'.format(bal_last),
            'Apocalyptech',
            [
                'Auto-generated partlocks, chosen with an interactive CLI app.',
            ],
            lic=Mod.CC_BY_SA_40,
            )

    for cat_idx, cat_actions in enumerate(actions):
        cur_cat = categories[cat_idx]
        always_vals = set()
        never_vals = set()
        for action in cat_actions.values():
            if action.action == Action.ALWAYS:
                always_vals.add(action.list_idx)
            else:
                never_vals.add(action.list_idx)

        # Now, loop through each category and assign new weights
        if len(always_vals) > 0 or len(never_vals) > 0:
            if cat_idx == 0:

                # We could try to generalize, but whatever.  Just process anoints separately
                cur_idx = 0
                if cur_cat.cat.partlist:
                    cur_source = cur_cat.cat.partlist[0].anoint_source
                for num, part in enumerate(cur_cat.cat.partlist):

                    # Reset our array index if needed
                    if part.anoint_source != cur_source:
                        cur_idx = 0
                        cur_source = part.anoint_source

                    # If we have any "always" entries, we effectively assume everything else
                    # is a "never", so we process a bit differently
                    if len(always_vals) > 0:
                        if num not in always_vals:
                            never_vals.add(num)

                    # Now write out
                    if part.anoint_source != balance_name:
                        extra_txt = ' (affects anything using this anoint)'
                        attr_ref = 'GenericParts.Parts'
                    else:
                        extra_txt = ''
                        attr_ref = 'RuntimeGenericPartList.PartList'
                    if num in always_vals:
                        mod.comment('Anointments: Always choose {}{}'.format(part.short_name, extra_txt))
                        mod.reg_hotfix(Mod.PATCH, '',
                                part.anoint_source,
                                '{}[{}].Weight'.format(attr_ref, cur_idx),
                                BVCF(bvc=1))
                        mod.newline()
                    elif num in never_vals:
                        mod.comment('Anointments: Never choose {}{}'.format(part.short_name, extra_txt))
                        mod.reg_hotfix(Mod.PATCH, '',
                                part.anoint_source,
                                '{}[{}].Weight'.format(attr_ref, cur_idx),
                                BVCF(bvc=0))
                        mod.newline()

                    # Increment our index
                    cur_idx += 1

            else:

                # Make sure this is set to use weights
                if not cur_cat.cat.use_weight_with_mult:
                    mod.comment('Category {}: Enable weight-based part picking'.format(cat_idx))
                    mod.reg_hotfix(Mod.PATCH, '',
                            balance.partset_name,
                            'ActorPartLists.ActorPartLists[{}].bUseWeightWithMultiplePartSelection'.format(cat_idx-1),
                            'True')
                    mod.newline()

                # Regular parts
                # TODO: If we ever get GPartExpansion objects which do more than add expansions,
                # well have to support it here, too.
                cur_idx = cur_cat.start_part_idx
                for num, part in enumerate(cur_cat.cat.partlist):

                    # If we have any "always" entries, we effectively assume everything else
                    # is a "never", so we process a bit differently
                    if len(always_vals) > 0:
                        if num not in always_vals:
                            never_vals.add(num)

                    # Now write out
                    if num in always_vals:
                        mod.comment('Category {}: Always choose {}'.format(cat_idx, part.short_name))
                        mod.reg_hotfix(Mod.PATCH, '',
                                balance_name,
                                'RuntimePartList.AllParts[{}].Weight'.format(cur_idx),
                                BVCF(bvc=1))
                        mod.newline()
                    elif num in never_vals:
                        mod.comment('Category {}: Never choose {}'.format(cat_idx, part.short_name))
                        mod.reg_hotfix(Mod.PATCH, '',
                                balance_name,
                                'RuntimePartList.AllParts[{}].Weight'.format(cur_idx),
                                BVCF(bvc=0))
                        mod.newline()

                    # Increment index
                    cur_idx += 1

    print('')
    print(color_success + '='*80)
    mod.close()
    print(color_success + '='*80)
    print(color_reset)
    input('Hit Enter to Continue...')
    print('')

###
### Finally the main interactive app can happen
###

# Little banner
banner_str = 'Starting gen_arbitrary_partlocks.py v{}'.format(_version)
print('')
print(color_header + '='*len(banner_str))
print('{}{}'.format(color_header, banner_str))
print(color_header + '='*len(banner_str))
print('')

# Grab the balance
data = BL3Data()
balance = Balance.from_data(data, balance_name)

# Flatten out the anointments found in the balance (for ease of display)
anointments_flattened = []
for anoint_path, anoints in balance.generics:
    for (part, weight) in anoints:
        anointments_flattened.append(AnointPart(part, anoint_path, weight))
        # I'd like to display '(no part)' rather than None for the short name
        if anointments_flattened[-1].short_name == 'None':
            anointments_flattened[-1].short_name = '(no part)'

# Set up the struct we'll use to keep track of actions (with an initial spot for anointment actions)
actions = [{}]

# Load our part categories into our wrapper CategoryInfo classes
categories = []
# Anointments first
categories.append(CategoryInfo(data, balance, PartCategory(partlist=anointments_flattened), 0, cat_name='ANOINTMENTS'))
# Now actual parts
start_idx = 0
for cat_idx, cat in enumerate(balance.categories):
    categories.append(CategoryInfo(data, balance, cat, start_idx, cat_idx=cat_idx))
    actions.append({})
    start_idx += len(cat.partlist)

    # I'd like to display '(no part)' rather than None for the short name
    for part in cat.partlist:
        if part.short_name == 'None':
            part.short_name = '(no part)'

# Now start an interactive loop
part_cache = {}
cur_category = None
show_dependencies = True
while True:
    if cur_category is None:
        print('{}Choose Category for {}'.format(color_header, bal_last))
        print('')
        valid_cats = set()
        for idx, cat in enumerate(categories):
            if len(cat.cat.partlist) > 1:
                if cat.cat.num_min != cat.cat.num_max:
                    part_range = '{}-{}'.format(cat.cat.num_min, cat.cat.num_max)
                else:
                    part_range = cat.cat.num_min
                print('{}[{}] Category: {} ({} parts, select {})'.format(
                    color_choices,
                    idx,
                    cat.cat_name,
                    len(cat.cat.partlist),
                    part_range,
                    ))
                valid_cats.add(idx)
                for action in actions[idx].values():
                    print('{}  - {}'.format(color_actions, action.text_long()))
            elif len(cat.cat.partlist) == 1:
                print('[-] Single Choice: {} ({})'.format(cat.cat_name, cat.cat.partlist[0].short_name))
            else:
                if idx == 0:
                    print('[-] (no anointments)')
                else:
                    print('[-] (empty category)')
        print('')
        can_save = any([len(a) > 0 for a in actions])
        if can_save:
            print('{}[s] Save'.format(color_commands))
        print('{}[q] Quit'.format(color_commands))
        choice = prompt()
        if choice == '':
            pass
        elif choice == 's' and can_save:
            sys.stdout.write('Enter filename> ')
            sys.stdout.flush()
            save_filename = sys.stdin.readline().strip()
            if save_filename != '':
                do_save = False
                if os.path.exists(save_filename):
                    sys.stdout.write('{} already exists, overwrite [y/N]? '.format(save_filename))
                    sys.stdout.flush()
                    answer = sys.stdin.readline().strip()
                    if answer == 'y':
                        do_save = True
                else:
                    do_save = True
                if do_save:
                    save_mod(save_filename)
        elif choice == 'q':
            break
        else:
            try:
                num_choice = int(choice)
            except ValueError as e:
                error('Unknown input')
                continue
            if num_choice not in valid_cats:
                error('Unknown category')
            else:
                cur_category = num_choice
    else:
        print('{}Category {}'.format(color_header, categories[cur_category].cat_name))
        print('  {}Multiple Selection: {}'.format(color_partinfo, categories[cur_category].cat.select_multiple))
        print('  {}Use Weights: {}'.format(color_partinfo, categories[cur_category].cat.use_weight_with_mult))
        print('  {}Number of Parts: {}-{}'.format(color_partinfo, categories[cur_category].cat.num_min, categories[cur_category].cat.num_max))
        print('')
        have_extras = False
        for idx, part in enumerate(categories[cur_category].cat.partlist):

            # What weight to report (if any)
            if part.weight == -1:
                wt_txt = 'unknown weight'
            else:
                try:
                    wt_txt = 'wt {}'.format(data.process_bvc(part.weight))
                except:
                    wt_txt = ''
            if wt_txt != '':
                wt_txt = '({}) '.format(wt_txt)

            # Alternate color if we're an anoint coming from an anoint-expansion obj
            color = color_choices
            if type(part) == AnointPart and part.anoint_source != categories[cur_category].bal.bal_name:
                color = color_choices_extra
                have_extras = True

            # Report on anointments which will never spawn if GBX hotfixes are loaded
            if part.part_name in disabled_anointments:
                extra_txt = ' {}(WILL NEVER SPAWN W/ GBX HOTFIXES)'.format(color_never_spawn)
            else:
                extra_txt = ''

            # Report if there's an action we're going to take on this part
            if idx in actions[cur_category]:
                action_txt = ' {}({})'.format(color_actions, actions[cur_category][idx].text_short())
            else:
                action_txt = ''

            print('{}{}: {}{}{}{}{}'.format(
                color,
                idx+1,
                wt_txt,
                part.short_name,
                extra_txt,
                color_reset,
                action_txt,
                ))
            # find excluders/depends
            if show_dependencies and part.part_name is not None and part.part_name != 'None':
                if part.part_name not in part_cache:
                    excluders = set()
                    dependencies = set()
                    part_obj = data.get_data(part.part_name)
                    for export in part_obj:
                        if export['export_type'].startswith('BPInvPart_'):
                            if 'Excluders' in export:
                                for excl in export['Excluders']:
                                    # This happens in at least /Game/Gear/Shields/_Design/PartSets/Part_Augment/Safespace/Part_Shield_Aug_Knockback
                                    # Basically it seems to reference *itself* somehow?  Whatever, going to assume it's just not there.
                                    if 'export' not in excl:
                                        excluders.add(excl[1].split('/')[-1])
                            if 'Dependencies' in export:
                                for dep in export['Dependencies']:
                                    dependencies.add(dep[1].split('/')[-1])
                            break
                    part_cache[part.part_name] = Relation(excluders, dependencies)
                rel = part_cache[part.part_name]
                for excl in rel.excluders:
                    print('{}  - Excluder: {}'.format(color_relation, excl))
                for dep in rel.dependencies:
                    print('{}  - Dependency: {}'.format(color_relation, dep))
        if have_extras:
            print('')
            print('{}Alternate-color choices are in expansion objects; changes will affect'.format(color_choices_extra))
            print('{}all balances which utilize these parts.  This applies to the "always"'.format(color_choices_extra))
            print('{}choices as well, which can completely block the expanded ones.'.format(color_choices_extra))
        print('')
        print('{}[q] Back'.format(color_commands))
        if show_dependencies:
            dep_action = 'off'
        else:
            dep_action = 'on'
        print('{}[d] Toggle dependency/excluder display {}'.format(color_commands, dep_action))
        print('{}[a<num>] Always spawn part'.format(color_commands))
        print('{}[n<num>] Never spawn part'.format(color_commands))
        print('{}[r<num>] Reset/remove action on part'.format(color_commands))
        print('{}<num> can be a list separated by commas, and can include a range with a dash'.format(color_commands))
        choice = prompt()
        if choice == '':
            pass
        elif choice == 'q':
            cur_category = None
        elif choice == 'd':
            show_dependencies = not show_dependencies
        else:
            first = choice[0]
            rest = choice[1:]
            if first == 'a' or first == 'n' or first == 'r':

                # Get a list of numbers to process.  We can specify multiple values by
                # delimiting with commas, and specify ranges with dashes (open-ended
                # ranges are *not* allowed though)
                errors = False
                nums_to_process = []
                comma_parts = [p.strip() for p in rest.split(',')]
                for comma_part in comma_parts:
                    if '-' in comma_part:
                        range_parts = [p.strip() for p in comma_part.split('-')]
                        if len(range_parts) != 2:
                            error('Unknown number range: {}'.format(comma_part))
                            errors = True
                        try:
                            start_num = int(range_parts[0])
                            end_num = int(range_parts[1])
                            if end_num > start_num:
                                nums_to_process.extend(list(range(start_num, end_num+1)))
                            else:
                                error('Invalid range specified: {}'.format(comma_part))
                        except ValueError as e:
                            error('Invalid number in range: {}'.format(comma_part))
                            errors = True
                    else:
                        try:
                            num = int(comma_part)
                            nums_to_process.append(num)
                        except ValueError as e:
                            error('Invalid number chosen: {}'.format(comma_part))
                            errors = True

                # Make sure that all our specified numbers are valid
                for num in nums_to_process:
                    if num > len(categories[cur_category].cat.partlist):
                        error('Number "{}" is too large'.format(num))
                        errors = True
                    elif num < 1:
                        error('Number must be at least 1 (specified {})'.format(num))
                        errors = True

                # Now actually do what we've been told
                if not errors:
                    for num in nums_to_process:
                        if first == 'a':
                            actions[cur_category][num-1] = Action(Action.ALWAYS, categories[cur_category].cat.partlist[num-1], num-1)
                        elif first == 'n':
                            actions[cur_category][num-1] = Action(Action.NEVER, categories[cur_category].cat.partlist[num-1], num-1)
                        elif first == 'r':
                            if num-1 in actions[cur_category]:
                                del actions[cur_category][num-1]
                        else:
                            error('Invalid action specified')
            else:
                error('Invalid option chosen')

