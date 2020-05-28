#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# Borderlands 3 Hotfix Modding Library is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# Borderlands 3 Hotfix Modding Library is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Borderlands 3 Hotfix Modding Library.  If not, see
# <https://www.gnu.org/licenses/>.

import os
import sys

class Mod(object):
    """
    Helper class for writing hotfix-injection mods for BL3
    """

    # Hotfix target types
    (PATCH, LEVEL, EARLYLEVEL, CHAR, PACKAGE, POST) = range(6)

    # We have no examples of SparkPostLoadedEntry or SparkStreamedPackageEntry, and
    # I haven't been successful in trying to get them to work (I suspect that
    # modifying vehicle handling might require SparkStreamedPackageEntry), so they're
    # a bit pointless in here.  Still, putting them in for those times when I feel
    # like doing some more trial-and-error to get 'em to work.
    TYPE = {
            PATCH: 'SparkPatchEntry',
            LEVEL: 'SparkLevelPatchEntry',
            EARLYLEVEL: 'SparkEarlyLevelPatchEntry',
            CHAR: 'SparkCharacterLoadedEntry',
            # No idea what the right syntax is for these two...
            PACKAGE: 'SparkStreamedPackageEntry',
            POST: 'SparkPostLoadedEntry',
        }

    # "Known" licenses
    (CC_40,
            CC_BY_ND_40,
            CC_BY_SA_40,
            CC_NC_40,
            CC_BY_NC_ND_40,
            CC_BY_NC_SA_40,
            CC0,
            PUBLICDOMAIN) = range(8)

    # Reporting constants to the user
    LIC_TO_LABEL = {
            CC_40: 'CC_40',
            CC_BY_ND_40: 'CC_BY_ND_40',
            CC_BY_SA_40: 'CC_BY_SA_40',
            CC_NC_40: 'CC_NC_40',
            CC_BY_NC_ND_40: 'CC_BY_NC_ND_40',
            CC_BY_NC_SA_40: 'CC_BY_NC_SA_40',
            CC0: 'CC0',
            PUBLICDOMAIN: 'PUBLICDOMAIN',
            }

    # Known license info
    LIC_INFO = {
            CC_40: ('Creative Commons Attribution 4.0 International (CC BY 4.0)',
                'https://creativecommons.org/licenses/by/4.0/'),
            CC_BY_ND_40: ('Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)',
                'https://creativecommons.org/licenses/by-nd/4.0/'),
            CC_BY_SA_40: ('Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)',
                'https://creativecommons.org/licenses/by-sa/4.0/'),
            CC_NC_40: ('Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)',
                'https://creativecommons.org/licenses/by-nc/4.0/'),
            CC_BY_NC_ND_40: ('Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)',
                'https://creativecommons.org/licenses/by-nc-nd/4.0/'),
            CC_BY_NC_SA_40: ('Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)',
                'https://creativecommons.org/licenses/by-nc-sa/4.0/'),
            # These two are essentially just aliases for each other
            CC0: ('Creative Commons CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                'https://creativecommons.org/publicdomain/zero/1.0/'),
            PUBLICDOMAIN: ('Public Domain (Creative Commons CC0 1.0 Universal (CC0 1.0))',
                'https://creativecommons.org/publicdomain/zero/1.0/'),
            }

    def __init__(self, filename, title, author, description, version=None, lic=None):
        """
        Initializes ourselves and starts writing the mod
        """
        self.filename = filename
        self.title = title
        self.author = author
        self.description = description
        self.version = version
        self.lic = lic
        self.last_was_newline = True

        self.source = os.path.basename(sys.argv[0])

        self.df = open(self.filename, 'w')
        if not self.df:
            raise Exception('Unable to write to {}'.format(self.filename))

        print('###', file=self.df)
        if self.version is None:
            print('### {}'.format(self.title), file=self.df)
        else:
            print('### {} v{}'.format(self.title, self.version), file=self.df)
        print('### by {}'.format(self.author), file=self.df)
        print('###', file=self.df)
        for desc in self.description:
            if desc == '':
                print('###', file=self.df)
            else:
                print('### {}'.format(desc), file=self.df)
        if len(self.description) > 0:
            print('###', file=self.df)

        # Process license information, if it's been specified (complaint to the user
        # if it hasn't!)
        if self.lic is None:
            print('')
            print('WARNING: You should specify a license with the `lic=` argument to Mod()')
            print('')
            print('Available pre-configured licenses:')
            print('')
            max_strlen = str(max([len(l) for l in Mod.LIC_TO_LABEL.values()]) + 4)
            format_str = ' {:' + max_strlen + 's} {} {}'
            for lic_key, lic_label in Mod.LIC_TO_LABEL.items():
                lic_title, lic_url = Mod.LIC_INFO[lic_key]
                print(format_str.format('Mod.{}'.format(lic_label), '-', lic_title))
                print(format_str.format('', ' ', lic_url))
                print('')
            print('')
            print('You can alternatively specify text for `lic=` to use any other license.')
            print('Apocalyptech recommends `Mod.CC_BY_SA_40` but you do you!')
            print('')
        else:
            if self.lic in Mod.LIC_INFO:
                lic_name, lic_url = Mod.LIC_INFO[self.lic]
                print('### Licensed under {}'.format(lic_name), file=self.df)
                print('### {}'.format(lic_url), file=self.df)
            else:
                print('### License: {}'.format(self.lic), file=self.df)
            print('###', file=self.df)

        # Now continue on.
        print('### Generated by {}'.format(self.source), file=self.df)
        print('###', file=self.df)
        print('', file=self.df)

    @staticmethod
    def get_full(object_name, data_type=None):
        """
        Gets the "full" object name from one whose full reference just repeats the
        last component.
        """
        expanded_obj = '{}.{}'.format(object_name, object_name.split('/')[-1])
        if data_type:
            return '{}\'"{}"\''.format(
                    data_type,
                    expanded_obj,
                    )
        else:
            return expanded_obj

    @staticmethod
    def get_full_cond(object_name, data_type=None):
        """
        Gets the "full" object name if there's not already a . in the name
        """
        if object_name == 'None':
            return object_name

        if '.' in object_name:
            expanded_obj = object_name
        else:
            expanded_obj = Mod.get_full(object_name)

        if data_type:
            return '{}\'"{}"\''.format(
                    data_type,
                    expanded_obj,
                    )
        else:
            return expanded_obj

    def newline(self):
        """
        Writes a newline to the mod fil
        """
        print('', file=self.df)
        self.last_was_newline = True

    def comment(self, comment_str, weight=1):
        """
        Writes a comment string out to the mod file
        """
        stripped = comment_str.strip()
        if len(stripped) > 0:
            print('{} {}'.format('#'*weight, stripped), file=self.df)
        else:
            print('{}'.format('#'*weight), file=self.df)
        self.last_was_newline = False

    def header_lines(self, lines):
        """
        Outputs a "header" type thing, with three hashes
        """
        self.comment('', weight=3)
        for line in lines:
            self.comment(line, weight=3)
        self.comment('', weight=3)
        self.newline()

    def header(self, line):
        """
        Outputs a "header" type thing, with three hashes
        """
        self.header_lines([line])

    def _process_value(self, value):
        """
        Processes the new value given to a hotfix so that it's valid in the exported
        JSON
        """
        return ''.join([l.strip() for l in str(value).splitlines()])

    def reg_hotfix(self, hf_type, package, obj_name, attr_name, new_val, prev_val='', notify=False):
        """
        Writes a regular hotfix to the mod file
        """
        if notify:
            notification_flag=1
        else:
            notification_flag=0
        print('{hf_type},(1,1,{notification_flag},{package}),{obj_name},{attr_name},{prev_val_len},{prev_val},{new_val}'.format(
            hf_type=Mod.TYPE[hf_type],
            notification_flag=notification_flag,
            package=package,
            obj_name=Mod.get_full_cond(obj_name),
            attr_name=attr_name,
            prev_val_len=len(prev_val),
            prev_val=prev_val,
            new_val=self._process_value(new_val),
            ), file=self.df)
        self.last_was_newline = False

    def table_hotfix(self, hf_type, package, obj_name, row_name, attr_name, new_val, prev_val='', notify=False):
        """
        Writes a regular hotfix to the mod file
        """
        if notify:
            notification_flag=1
        else:
            notification_flag=0
        print('{hf_type},(1,2,{notification_flag},{package}),{obj_name},{row_name},{attr_name},{prev_val_len},{prev_val},{new_val}'.format(
            hf_type=Mod.TYPE[hf_type],
            notification_flag=notification_flag,
            package=package,
            obj_name=Mod.get_full_cond(obj_name),
            row_name=row_name,
            attr_name=attr_name,
            prev_val_len=len(prev_val),
            prev_val=prev_val,
            new_val=self._process_value(new_val),
            ), file=self.df)
        self.last_was_newline = False

    def close(self):
        """
        Closes us out
        """
        if not self.last_was_newline:
            self.newline()
        self.df.close()

class DataTableValue(object):
    """
    Class to make dealing with datatable values (inside BVC tuples) easier
    """

    def __init__(self, table=None, row='', value=''):
        if table:
            self.table = table
        else:
            self.table = 'None'
        self.row = row
        self.value = value

    def __str__(self):
        return '(DataTable={},RowName="{}",ValueName="{}")'.format(
                Mod.get_full_cond(self.table, 'DataTable'),
                self.row,
                self.value,
                )

class BVC(object):
    """
    Class to make dealing with BVC tuples/structures/whatever a bit easier.  By
    default, When turned into a string, it'll only include "interesting" data.
    So if you've just got a tuple with BVC=1,BVSC=1, you'll get an empty string
    instead.  Use `full=True` to get all components regardless (if, for instance,
    you're overwriting an existing tuple and want to be sure to reset all
    attributes).

    Very arguably this should exist in bl3data instead of bl3hotfixmod...
    """

    def __init__(self, bvc=1, dtv=None, bva=None, ai=None, bvs=1, full=False):
        self.full = full
        self.bvc = bvc
        if dtv:
            self.dtv = dtv
        else:
            self.dtv = DataTableValue()
        if bva:
            self.bva = bva
        else:
            self.bva = 'None'
        if ai:
            self.ai = ai
        else:
            self.ai = 'None'
        self.bvs = bvs

    @staticmethod
    def from_data_struct(data):
        """
        Given a serialized data struct, return a BVC object
        """

        # BVC
        if 'BaseValueConstant' in data:
            bvc = data['BaseValueConstant']
        else:
            bvc = 1

        # DataTable
        if 'DataTableValue' in data and 'export' not in data['DataTableValue']['DataTable']:
            dtv = DataTableValue(table=data['DataTableValue']['DataTable'][1],
                    row=data['DataTableValue']['RowName'],
                    value=data['DataTableValue']['ValueName'])
        else:
            dtv = None

        # BVA
        if 'BaseValueAttribute' in data and 'export' not in data['BaseValueAttribute']:
            bva = data['BaseValueAttribute'][1]
        else:
            bva = None

        # AI
        # TODO: haven't actually looked for examples of this.  I assume it's right.
        if 'AttributeInitializer' in data and 'export' not in data['AttributeInitializer']:
            ai = data['AttributeInitializer'][1]
        else:
            ai = None

        # BVS
        if 'BaseValueScale' in data:
            bvs = data['BaseValueScale']
        else:
            bvs = 1

        return BVC(bvc=bvc,
                dtv=dtv,
                bva=bva,
                ai=ai,
                bvs=bvs)

    def _get_parts(self):
        parts = []
        #if self.full or self.bvc != 1:
        parts.append('BaseValueConstant={}'.format(round(self.bvc, 6)))
        if self.full or self.dtv.table != 'None':
            parts.append('DataTableValue={}'.format(self.dtv))
        # TODO: Are these always the object types for BVA/AI?
        if self.full or self.bva != 'None':
            parts.append('BaseValueAttribute={}'.format(Mod.get_full_cond(self.bva, 'GbxAttributeData')))
        if self.full or self.ai != 'None':
            parts.append('AttributeInitializer={}'.format(Mod.get_full_cond(self.ai, 'BlueprintGeneratedClass')))
        if self.full or self.bvs != 1:
            parts.append('BaseValueScale={}'.format(round(self.bvs, 6)))
        return parts

    def has_data(self):
        return len(self._get_parts()) > 0

    def __str__(self):
        parts = self._get_parts()
        if len(parts) == 0:
            return ''
        else:
            return '({})'.format(','.join(parts))

class BVCF(BVC):
    """
    A BVC which always has `full=True` specified.  Just a little convenience class.

    Very arguably this should exist in bl3data instead of bl3hotfixmod...
    """

    def __init__(self, **kwargs):
        super().__init__(full=True, **kwargs)

class Pool(object):
    """
    Class to make dealing with pools a bit easier
    """

    def __init__(self, pool_name, probability=1, num=1):
        self.pool_name = pool_name
        if probability:
            if type(probability) == BVC or type(probability) == BVCF:
                self.probability = probability
            else:
                self.probability = BVC(bvc=probability)
        if num:
            if type(probability) == BVC or type(probability) == BVCF:
                self.num = num
            else:
                self.num = BVC(bvc=num)

    def __str__(self):
        parts = []
        parts.append('ItemPool={}'.format(Mod.get_full_cond(self.pool_name, 'ItemPool')))
        if self.probability and self.probability.has_data():
            parts.append('PoolProbability={}'.format(self.probability))
        if self.num and self.num.has_data():
            parts.append('NumberOfTimesToSelectFromThisPool={}'.format(self.num))
        return '({})'.format(','.join(parts))

class Part(object):
    """
    Class to hold info about a single Part for an item/weapon.  Just the object name
    and its weight, basically a glorified dict.

    Very arguably this should exist in bl3data instead of bl3hotfixmod...
    """

    def __init__(self, part_name, weight=1):
        self.part_name = part_name
        if type(weight) == BVC or type(weight) == BVCF:
            self.weight = weight
        else:
            self.weight = BVC(bvc=weight)

    def __str__(self):
        return '(PartData={},Weight={})'.format(
                Mod.get_full_cond(self.part_name),
                self.weight,
                )

class PartCategory(object):
    """
    Class for dealing with a collection of parts used in items/weapons.  Technically
    this is part of the PartSet object, but it'll also get used to set the attributes
    on the Balance.

    Very arguably this should exist in bl3data instead of bl3hotfixmod...
    """

    def __init__(self, num_min=1, num_max=1,
            index=0,
            partlist=None,
            part_type_enum=None,
            select_multiple=False, use_weight_with_mult=False,
            enabled=True):
        self.num_min = num_min
        self.num_max = num_max
        self.index = index
        self.part_type_enum = part_type_enum
        self.select_multiple = select_multiple
        if num_min > 1 or num_max > 1 or num_min != num_max:
            self.select_multiple = True
        self.use_weight_with_mult = use_weight_with_mult
        self.enabled = enabled
        if partlist:
            self.partlist = partlist
        else:
            self.partlist = []

    def __add__(self, other):
        """
        Convenience for when we construct Balance objects
        """
        new = PartCategory(
                num_min=self.num_min,
                num_max=self.num_max,
                index=self.index,
                part_type_enum=self.part_type_enum,
                partlist=list(self.partlist),
                select_multiple=self.select_multiple,
                use_weight_with_mult=self.use_weight_with_mult,
                enabled=self.enabled,
                )
        if type(other) == PartCategory:
            for part in other.partlist:
                new.add_part_obj(part)
        elif type(other) == int and other == 0:
            pass
        else:
            raise TypeError('PartCategory objects can only be added to other PartCategory objects')
        return new

    def __radd__(self, other):
        return self.__add__(other)

    def add_part_obj(self, new_part):
        """
        Adds an already-instantiated Part object
        """
        self.partlist.append(new_part)

    def add_part_name(self, new_part_name, weight=1):
        """
        Adds a new part by object name (and optionally weight)
        """
        self.add_part_obj(Part(new_part_name, weight))

    def str_partlist(self):
        """
        Returns just a string representation of our partlist
        """
        return ','.join([str(l) for l in self.partlist])

    def __len__(self):
        """
        Returns the number of parts we have
        """
        return len(self.partlist)

    def __str__(self):
        """
        Returns a string representation as a complete stanza inside a
        PartSet object
        """
        if not self.part_type_enum:
            raise Exception('PartSet representation requires part_type_enum')

        return """(
            PartTypeEnum={part_type_enum},
            PartType={index},
            bCanSelectMultipleParts={select_multiple},
            bUseWeightWithMultiplePartSelection={use_weight_with_mult},
            MultiplePartSelectionRange=(
                Min={num_min},
                Max={num_max}
            ),
            bEnabled={enabled},
            Parts=({parts})
        )""".format(
                part_type_enum=Mod.get_full_cond(self.part_type_enum),
                index=self.index,
                select_multiple=str(self.select_multiple),
                use_weight_with_mult=str(self.use_weight_with_mult),
                num_min=self.num_min,
                num_max=self.num_max,
                enabled=str(self.enabled),
                parts=self.str_partlist(),
                )

class Balance(object):
    """
    Class for dealing with both Balances and PartSets -- the class will generate
    hotfixes to deal with the pair.  Technically the PartSet object does NOT
    need to have an enumerated parts list -- it seems to be completely ignored
    by the game.  We'll go ahead and generate those by default though, anyway,
    just so it matches the parts that are listed in the Balance.

    Very arguably this should exist in bl3data instead of bl3hotfixmod...
    """

    def __init__(self, bal_name, partset_name, part_type_enum=None, raw_bal_data=None, raw_ps_data=None):
        """
        `part_type_enum` is a PartTypeEnum object name which will be used if partlists are added via
            `add_category_smart` (unused otherwise)
        `raw_bal_data` is the raw serialized Balance export (pretty much only useful with `from_data()`)
        `raw_ps_data` is the raw serialized PartSet export (pretty much only useful with `from_data()`)
        """
        self.bal_name = bal_name
        self.partset_name = partset_name
        self.part_type_enum = part_type_enum
        self.categories = []
        self.raw_bal_data = raw_bal_data
        self.raw_ps_data = raw_ps_data

    @staticmethod
    def from_data(data, bal_name):
        """
        Loads in all our data from a BL3Data instance, given a balance name.  Returns
        a fully-populated Balance object.
        """

        # Load in Balance
        bal_obj = data.get_data(bal_name)
        if len(bal_obj) != 1:
            raise Exception('Unknown export count ({}) for: {}'.format(len(bal_obj), bal_name))
        last_bit = bal_name.split('/')[-1]
        bal_data = bal_obj[0]

        # Load in part list from balance (grouping it as it would be done in a PartSet.
        partlists = []
        for toc in bal_data['RuntimePartList']['PartTypeTOC']:
            partlist = []
            for part_idx in range(toc['StartIndex'], toc['StartIndex']+toc['NumParts']):
                partdata = bal_data['RuntimePartList']['AllParts'][part_idx]['PartData']
                weight = BVC.from_data_struct(bal_data['RuntimePartList']['AllParts'][part_idx]['Weight'])
                if 'export' in partdata:
                    partlist.append(('None', weight))
                else:
                    partlist.append((partdata[1], weight))
            partlists.append(partlist)

        # Load our PartSet
        partset_name = bal_data['PartSetData'][1]
        partset_obj = data.get_data(partset_name)
        if len(partset_obj) != 1:
            raise Exception('Unknown export count ({}) for: {}'.format(len(partset_obj), partset_name))
        partset_data = partset_obj[0]

        # Sanity check
        if len(partlists) != len(partset_data['ActorPartLists']):
            raise Exception('Balance partlist count ({}) does not match PartSet partlist count ({}) - {} vs {}'.format(
                len(partlists),
                len(partset_data['ActorPartLists']),
                bal_name,
                partset_name,
                ))

        # Check to see if we have consensus about the PartTypeEnum
        part_type_enum = None
        have_mismatch = False
        for apl_idx, apl in enumerate(partset_data['ActorPartLists']):
            if 'export' not in apl['PartTypeEnum']:
                if part_type_enum:
                    if apl['PartTypeEnum'][1] != part_type_enum:
                        print('WARNING: PartTypeEnum mismatch detected in APL[{}] - {}'.format(
                            apl_idx,
                            partset_name,
                            ))
                        have_mismatch = True
                        break
                else:
                    part_type_enum = apl['PartTypeEnum'][1]
        if have_mismatch:
            part_type_enum = None
            #print('WARNING: No PartTypeEnum consensus for {}'.format(partset_name))

        # No reason not to create a Balance object now
        bal = Balance(bal_name, partset_name, part_type_enum,
                raw_bal_data=bal_data,
                raw_ps_data=partset_data,
                )

        # Loop through our partlists and populate our objects
        for (partlist, apl) in zip(partlists, partset_data['ActorPartLists']):
            partcat = PartCategory(
                    num_min=apl['MultiplePartSelectionRange']['Min'],
                    num_max=apl['MultiplePartSelectionRange']['Max'],
                    index=apl['PartType'],
                    part_type_enum=apl['PartTypeEnum'][1],
                    select_multiple=apl['bCanSelectMultipleParts'],
                    use_weight_with_mult=apl['bUseWeightWithMultiplePartSelection'],
                    enabled=apl['bEnabled'])
            for part, weight in partlist:
                partcat.add_part_name(part, weight=weight)
            bal.add_category(partcat)

        # That... should be all?
        return bal

    def add_category(self, category):
        """
        Adds a new PartCategory to ourselves
        """
        self.categories.append(category)

    def add_category_smart(self, category):
        """
        Adds a new PartCategory to ourselves, managing the PartCategory index
        by how many categories already exist, and automatically populating the
        part_type_enum based on what we already know about it.
        """
        if not self.part_type_enum:
            raise Exception('part_type_enum must be defined for add_category_smart()')
        category.index = len(self.categories)
        category.part_type_enum = self.part_type_enum
        self.categories.append(category)

    def set_balance_to(self, new_balance_name, data):
        """
        Updates our balance name to be `new_balance_name`, and updates the PartSet name
        appropriately using the BL3Data object `data` as well.  Used if you want to copy
        an existing balance over to another one.  Probably not a lot of general-purpose
        use, but what's a little API bloat, right?
        """
        self.bal_name = new_balance_name
        obj = data.get_data(self.bal_name)[0]
        self.partset_name = obj['PartSetData'][1]

    def hotfix_partset_full(self, mod, hf_type=Mod.PATCH, hf_package=''):
        """
        Generates hotfixes to completely set the PartSet portion.
        """
        mod.reg_hotfix(hf_type, hf_package,
                self.partset_name,
                'ActorPartLists',
                '({})'.format(','.join([str(c) for c in self.categories])))

    def hotfix_balance_full(self, mod, hf_type=Mod.PATCH, hf_package=''):
        """
        Generates hotfixes to completely set the Balance portion.
        """

        # Generate the TOC
        cur_idx = 0
        toc = []
        for cat in self.categories:
            toc.append((cur_idx, len(cat)))
            cur_idx += len(cat)
        mod.reg_hotfix(hf_type, hf_package,
                self.bal_name,
                'RuntimePartList.PartTypeTOC',
                '({})'.format(
                    ','.join([
                        '(StartIndex={},NumParts={})'.format(t[0], t[1]) for t in toc
                        ])
                    ))

        # Now the AllParts list
        all_parts = sum(self.categories)
        mod.reg_hotfix(hf_type, hf_package,
                self.bal_name,
                'RuntimePartList.AllParts',
                '({})'.format(','.join([str(p) for p in all_parts.partlist])))

    def hotfix_full(self, mod, hf_type=Mod.PATCH, hf_package=''):
        """
        Generates hotfixes to completely set the object
        """
        self.hotfix_partset_full(mod, hf_type, hf_package)
        self.hotfix_balance_full(mod, hf_type, hf_package)

LVL_TO_ENG = {
        'Archive_P': "Dustbound Archives",
        'AtlasHQ_P': "Atlas HQ",
        'Bar_P': "Lodge",
        'Beach_P': "Tazendeer Ruins",
        'BloodyHarvest_P': "Heck Hole",
        'COVSlaughter_P': "Slaughter Shaft",
        'Camp_P': "Negul Neshai",
        'Cartels_P': "Villa Ultraviolet",
        'CasinoIntro_P': "Grand Opening",
        'CityBoss_P': "Forgotten Basilica",
        'CityVault_P': "Neon Arterial",
        'City_P': "Meridian Metroplex",
        'Convoy_P': "Sandblast Scar",
        'Core_P': "Jack's Secret",
        'CreatureSlaughter_P': "Cistern of Slaughter",
        'Crypt_P': "Pyre of Stars",
        'DesertBoss_P': "Great Vault",
        'Desert_P': "Devil's Razor",
        'Desertvault_P': "Cathedral of the Twin Gods",
        'Desolate_P': "Desolation's Edge",
        'FinalBoss_P': "Destroyer's Rift",
        'Impound_P': "Impound Deluxe",
        'Lake_P': "Skittermaw Basin",
        'Mansion_P': "Jakobs Estate",
        'MarshFields_P': "Ambermire",
        'Mine_P': "Konrad's Hold",
        'Monastery_P': "Athenas",
        'MotorcadeFestival_P': "Carnivora",
        'MotorcadeInterior_P': "Guts of Carnivora",
        'Motorcade_P': "Splinterlands",
        'OrbitalPlatform_P': "Skywell-27",
        'Outskirts_P': "Meridian Outskirts",
        'Prison_P': "Anvil",
        'Prologue_P': "Droughts",
        'ProvingGrounds_Trial1_P': "Gradient of Dawn (Survival)",
        'ProvingGrounds_Trial4_P': "Skydrowned Pulpit (Fervor)",
        'ProvingGrounds_Trial5_P': "Ghostlight Beacon (Cunning)",
        'ProvingGrounds_Trial6_P': "Hall Obsidian (Supremacy)",
        'ProvingGrounds_Trial7_P': "Precipice Anchor (Discipline)",
        'ProvingGrounds_Trial8_P': "Wayward Tether (Instinct)",
        'Raid_P': "Midnight's Cairn (Maliwan Takedown)",
        'Recruitment_P': "Covenant Pass",
        'Sacrifice_P': "Ascension Bluff",
        'Sanctuary3_P': "Sanctuary",
        'Strip_P': "Spendopticon",
        'TechSlaughter_P': "Slaughterstar 3000",
        'TowerLair_P': "VIP Tower",
        'Towers_P': "Lectra City",
        'Trashtown_P': "Compactor",
        'Venue_P': "Heart's Desire",
        'Village_P': "Cursehaven",
        'Watership_P': "Voracious Canopy",
        'WetlandsBoss_P': "Floating Tomb",
        'WetlandsVault_P': "Blackbarrel Cellars",
        'Wetlands_P': "Floodmoor Basin",
        'Woods_P': "Cankerwood",
        }

# Also create a lowercase version
LVL_TO_ENG_LOWER = {}
for k, v in list(LVL_TO_ENG.items()):
    LVL_TO_ENG_LOWER[k.lower()] = v

