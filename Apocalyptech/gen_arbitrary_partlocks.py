#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Given a balance, interactively choose parts to generate partlock mods.

import os
import sys
import colorama
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

balance_name = sys.argv[1]
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

class Relation(object):
    """
    Mostly just a glorified dict
    """

    def __init__(self, excluders, dependencies):
        self.excluders = excluders
        self.dependencies = dependencies

class Part(object):
    """
    Mostly just a glorified dict
    """

    def __init__(self, data, idx, part_obj=None, part_name=None):
        self.idx = idx
        if part_obj:
            if type(part_obj['PartData']) == dict:
                self.name = None
                self.short = '(no part)'
            else:
                self.name = part_obj['PartData'][1]
                self.short = self.name.split('/')[-1]
            try:
                self.weight = data.process_bvc_struct(part_obj['Weight'])
            except Exception:
                self.weight = -1
        else:
            self.name = part_name
            self.short = part_name.split('/')[-1]
            self.weight = -1

class CategoryInfo(object):
    """
    Mostly just a glorified dict
    """

    def __init__(self, data, apl, balance_name=None, cat_idx=None, cat_name=None, extra_parts=[]):
        self.data = data
        self.balance_name = balance_name
        self.cat_idx = cat_idx
        self.cat_name = cat_name
        if apl:
            self.multiple = apl['bCanSelectMultipleParts']
            self.use_weight = apl['bUseWeightWithMultiplePartSelection']
            if self.multiple:
                self.min_parts = apl['MultiplePartSelectionRange']['Min']
                self.max_parts = apl['MultiplePartSelectionRange']['Max']
            else:
                self.min_parts = 1
                self.max_parts = 1
            self.enabled = apl['bEnabled']
        else:
            # Basically just using this for anointments.
            self.multiple = False
            self.use_weight = True
            self.min_parts = 1
            self.max_parts = 1
            self.enabled = True
        self.parts = []
        self.parts_basic = []
        self.parts_extra = extra_parts
        self.bal_start = -1
        self.bal_end = -1

    def finish_parts(self):
        for part in self.parts_basic:
            self.parts.append((None, part))
        for (expansion, extra_parts) in self.parts_extra:
            for cur_idx, part_name in enumerate(extra_parts):
                self.parts.append((expansion, Part(self.data, cur_idx, part_name=part_name)))

    def set_bal_range(self, start, end):
        self.bal_start = start
        self.bal_end = end

    def add(self, part, part_idx):
        self.parts_basic.append(Part(self.data, part_idx, part_obj=part))

    def _compute_category_name(self):

        # No way to tell if there's no parts
        if len(self.parts) == 0:
            return '(no parts)'

        # Construct a default using the short name of the first real part,
        # if we can.  (If we don't find one, then there's no real parts
        # in here anyway.)
        default_label = None
        for (_, part) in self.parts:
            if part.name:
                default_label = part.short
                break
        if not default_label:
            return '(empty category)'

        # If we don't have a balance_name or cat_idx, just abort.  This
        # would only happen with our Anointment stuff anyway.
        if not self.balance_name or self.cat_idx is None:
            return '(unknown)'

        # Make an attempt at figuring it out
        cat_name = self.data.get_parts_category_name(
                [p[1].name for p in self.parts],
                self.balance_name,
                self.cat_idx,
                )
        if cat_name:
            return cat_name
        else:
            return default_label

    def compute_category_name(self):
        self.finish_parts()
        self.cat_name = self._compute_category_name()

class Action(object):
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
        return '{} {}'.format(self.text_short(), self.part[1].short)

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

# Grab the balance
data = BL3Data()
balance = data.get_data(balance_name)

# Get a list of extra anointments this item gets which isn't in the base balance
extra_anoints = data.get_extra_anoints(balance_name)

# Set up the struct we'll use to keep track of actions
actions = [{}]

# Grab the PartSet, too
partset = data.get_data(balance[0]['PartSetData'][1])
categories = []
# We're putting anointments first
categories.append(CategoryInfo(data, None, cat_name='ANOINTMENTS', extra_parts=extra_anoints))
for cat_idx, part in enumerate(partset[0]['ActorPartLists']):
    categories.append(CategoryInfo(data, part, balance_name=balance_name, cat_idx=cat_idx))
    actions.append({})

# Now loop through the balance and get the partlists.  Process anointments first
if 'RuntimeGenericPartList' in balance[0]:
    for part_idx, part in enumerate(balance[0]['RuntimeGenericPartList']['PartList']):
        categories[0].add(part, part_idx)
    categories[0].finish_parts()
# And now regular parts
for toc_idx, toc in enumerate(balance[0]['RuntimePartList']['PartTypeTOC']):
    categories[toc_idx+1].set_bal_range(toc['StartIndex'], toc['StartIndex']+toc['NumParts'])
    for bal_idx in range(toc['StartIndex'], toc['StartIndex']+toc['NumParts']):
        categories[toc_idx+1].add(balance[0]['RuntimePartList']['AllParts'][bal_idx], bal_idx)
    categories[toc_idx+1].compute_category_name()

# Now start an interactive loop
part_cache = {}
cur_category = None
save_filename = None
while True:
    if cur_category is None:
        print('{}Choose Category for {}'.format(color_header, bal_last))
        print('')
        valid_cats = set()
        for idx, cat in enumerate(categories):
            if len(cat.parts) > 1:
                print('{}[{}] Category: {} ({} parts)'.format(
                    color_choices,
                    idx,
                    cat.cat_name,
                    len(cat.parts),
                    ))
                valid_cats.add(idx)
                for action in actions[idx].values():
                    print('{}  - {}'.format(color_actions, action.text_long()))
            elif len(cat.parts) == 1:
                print('[-] Single Choice: {}'.format(cat.cat_name))
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
            if save_filename == '':
                save_filename = None
            else:
                if os.path.exists(save_filename):
                    sys.stdout.write('{} already exists, overwrite [y/N]? '.format(save_filename))
                    sys.stdout.flush()
                    answer = sys.stdin.readline().strip()
                    if answer == 'y':
                        break
                    save_filename = None
                else:
                    break
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
        print('  {}Multiple Selection: {}'.format(color_partinfo, categories[cur_category].multiple))
        print('  {}Use Weights: {}'.format(color_partinfo, categories[cur_category].use_weight))
        print('  {}Number of Parts: {}-{}'.format(color_partinfo, categories[cur_category].min_parts, categories[cur_category].max_parts))
        print('')
        have_extras = False
        for idx, (partsource, part) in enumerate(categories[cur_category].parts):
            if idx in actions[cur_category]:
                action_txt = ' {}({})'.format(color_actions, actions[cur_category][idx].text_short())
            else:
                action_txt = ''
            if part.weight == -1:
                wt_txt = 'unknown weight'
            else:
                wt_txt = 'wt {}'.format(part.weight)
            if partsource:
                color = color_choices_extra
                have_extras = True
            else:
                color = color_choices
            print('{}{}: ({}) {}{}{}'.format(
                color,
                idx+1,
                wt_txt,
                part.short,
                color_reset,
                action_txt,
                ))
            # find excluders/depends
            if part.name is not None:
                if part.name not in part_cache:
                    excluders = set()
                    dependencies = set()
                    part_obj = data.get_data(part.name)
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
                    part_cache[part.name] = Relation(excluders, dependencies)
                rel = part_cache[part.name]
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
        print('{}[a<num>] Always spawn part'.format(color_commands))
        print('{}[n<num>] Never spawn part'.format(color_commands))
        print('{}[r<num>] Reset/remove action on part'.format(color_commands))
        choice = prompt()
        if choice == '':
            pass
        elif choice == 'q':
            cur_category = None
        else:
            first = choice[0]
            rest = choice[1:]
            if first == 'a' or first == 'n' or first == 'r':
                try:
                    num = int(rest)
                except ValueError as e:
                    error('Invalid number chosen')
                    continue
                if num > len(categories[cur_category].parts):
                    error('Chosen number is too large')
                elif num == 0:
                    error('Number must be at least 1')
                else:
                    if first == 'a':
                        actions[cur_category][num-1] = Action(Action.ALWAYS, categories[cur_category].parts[num-1], num-1)
                    elif first == 'n':
                        actions[cur_category][num-1] = Action(Action.NEVER, categories[cur_category].parts[num-1], num-1)
                    elif first == 'r':
                        if num-1 in actions[cur_category]:
                            del actions[cur_category][num-1]
                    else:
                        error('Invalid action specified')
            else:
                error('Invalid option chosen')

# Saving down here
if save_filename:
    mod = Mod(save_filename,
            'Arbitrary Partlocks: {}'.format(bal_last),
            [
                'Auto-generated partlocks, chosen with an interactive CLI app.',
            ],
            'ArbPL{}'.format(bal_last.replace('_', '')))

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
                for num, (partsource, part) in enumerate(cur_cat.parts):

                    # If we have any "always" entries, we effectively assume everything else
                    # is a "never", so we process a bit differently
                    if len(always_vals) > 0:
                        if num not in always_vals:
                            never_vals.add(num)

                    # Now write out
                    if num in always_vals:
                        if partsource:
                            mod.comment('Anointments: Always choose {} (affects anything using this anoint)'.format(part.short))
                            mod.reg_hotfix(Mod.PATCH, '',
                                    partsource,
                                    'GenericParts.Parts[{}].Weight'.format(part.idx),
                                    BVCF(bvc=1))
                            mod.newline()
                        else:
                            mod.comment('Anointments: Always choose {}'.format(part.short))
                            mod.reg_hotfix(Mod.PATCH, '',
                                    balance_name,
                                    'RuntimeGenericPartList.PartList[{}].Weight'.format(part.idx),
                                    BVCF(bvc=1))
                            mod.newline()
                    elif num in never_vals:
                        if partsource:
                            mod.comment('Anointments: Never choose {} (affects anything using this anoint)'.format(part.short))
                            mod.reg_hotfix(Mod.PATCH, '',
                                    partsource,
                                    'GenericParts.Parts[{}].Weight'.format(part.idx),
                                    BVCF(bvc=0))
                            mod.newline()
                        else:
                            mod.comment('Anointments: Never choose {}'.format(part.short))
                            mod.reg_hotfix(Mod.PATCH, '',
                                    balance_name,
                                    'RuntimeGenericPartList.PartList[{}].Weight'.format(part.idx),
                                    BVCF(bvc=0))
                            mod.newline()

            else:

                # Regular parts
                # TODO: If we ever get GPartExpansion objects which do more than add expansions,
                # well have to support it here, too.
                for num, (partsource, part) in enumerate(cur_cat.parts):

                    # If we have any "always" entries, we effectively assume everything else
                    # is a "never", so we process a bit differently
                    if len(always_vals) > 0:
                        if num not in always_vals:
                            never_vals.add(num)

                    # Now write out
                    if num in always_vals:
                        mod.comment('Category {}: Always choose {}'.format(cat_idx+1, part.short))
                        mod.reg_hotfix(Mod.PATCH, '',
                                balance_name,
                                'RuntimePartList.AllParts[{}].Weight'.format(part.idx),
                                BVCF(bvc=1))
                        mod.newline()
                    elif num in never_vals:
                        mod.comment('Category {}: Never choose {}'.format(cat_idx+1, part.short))
                        mod.reg_hotfix(Mod.PATCH, '',
                                balance_name,
                                'RuntimePartList.AllParts[{}].Weight'.format(part.idx),
                                BVCF(bvc=0))
                        mod.newline()

    mod.close()
