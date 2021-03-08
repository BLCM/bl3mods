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
import gzip


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

    def __init__(self, filename, title, author, description,
                 v=None, lic=None, cats=None,
                 ss=None, videos=None, urls=None, nexus=None):
        """
        Initializes ourselves and starts writing the mod
        """
        self.filename = filename
        self.title = title
        self.author = author
        self.description = description
        self.version = v
        self.lic = lic
        self.categories = cats
        self.ss = ss
        self.videos = videos
        self.urls = urls
        self.nexus = nexus
        self.last_was_newline = True

        self.source = os.path.basename(sys.argv[0])

        if self.filename.endswith('.gz'):
            self.df = gzip.open(self.filename, 'wt')
        else:
            self.df = open(self.filename, 'w')
        if not self.df:
            raise Exception('Unable to write to {}'.format(self.filename))

        print('###', file=self.df)
        print('### Name: {}'.format(self.title), file=self.df)
        if self.version is not None:
            print('### Version: {}'.format(self.version), file=self.df)
        print('### Author: {}'.format(self.author), file=self.df)
        if self.categories:
            if type(self.categories) == list:
                print('### Categories: {}'.format(
                    ', '.join(self.categories)), file=self.df)
            else:
                print('### Categories: {}'.format(
                    self.categories), file=self.df)
        print('###', file=self.df)

        # Process license information, if it's been specified (complaint to the user
        # if it hasn't!)
        if self.lic is None:
            print('')
            print(
                'WARNING: You should specify a license with the `lic=` argument to Mod()')
            print('')
            print('Available pre-configured licenses:')
            print('')
            max_strlen = str(
                max([len(l) for l in Mod.LIC_TO_LABEL.values()]) + 4)
            format_str = ' {:' + max_strlen + 's} {} {}'
            for lic_key, lic_label in Mod.LIC_TO_LABEL.items():
                lic_title, lic_url = Mod.LIC_INFO[lic_key]
                print(format_str.format('Mod.{}'.format(lic_label), '-', lic_title))
                print(format_str.format('', ' ', lic_url))
                print('')
            print('')
            print(
                'You can alternatively specify text for `lic=` to use any other license.')
            print('Apocalyptech recommends `Mod.CC_BY_SA_40` but you do you!')
            print('')
        else:
            if self.lic in Mod.LIC_INFO:
                lic_name, lic_url = Mod.LIC_INFO[self.lic]
                print('### License: {}'.format(lic_name), file=self.df)
                print('### License URL: {}'.format(lic_url), file=self.df)
            else:
                print('### License: {}'.format(self.lic), file=self.df)
            print('###', file=self.df)

        # Media links
        if ss or videos or urls or nexus:
            if ss:
                if type(ss) != list:
                    ss = [ss]
                for shot in ss:
                    print('### Screenshot: {}'.format(shot), file=self.df)
            if videos:
                if type(videos) != list:
                    videos = [videos]
                for video in videos:
                    print('### Video: {}'.format(video), file=self.df)
            if urls:
                if type(urls) != list:
                    urls = [urls]
                for url in urls:
                    print('### URL: {}'.format(url), file=self.df)
            if nexus:
                print('### Nexus: {}'.format(nexus), file=self.df)
            print('###', file=self.df)

        # Now continue on (basically just the description from here on out)
        print('', file=self.df)
        print('###', file=self.df)
        for desc in self.description:
            if desc == '':
                print('###', file=self.df)
            else:
                print('### {}'.format(desc), file=self.df)
        if len(self.description) > 0:
            print('###', file=self.df)
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
            notification_flag = 1
        else:
            notification_flag = 0
        print('{hf_type},(1,1,{notification_flag},{package}),{obj_name},{attr_name},{prev_val_len},{prev_val},{new_val}'.format( hf_type=Mod.TYPE[hf_type], notification_flag=notification_flag, package=package, obj_name=Mod.get_full_cond(obj_name), attr_name=attr_name, prev_val_len=len(prev_val), prev_val=prev_val, new_val=self._process_value(new_val),), file=self.df)
        self.last_was_newline = False

    def table_hotfix(self, hf_type, package, obj_name, row_name, attr_name, new_val, prev_val='', notify=False):
        """
        Writes a regular hotfix to the mod file
        """
        if notify:
            notification_flag = 1
        else:
            notification_flag = 0
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

    def mesh_hotfix(self, map_path, mesh_path,
                    location=(0, 0, 0),
                    rotation=(0, 0, 0),
                    scale=(1, 1, 1),
                    transparent=False,
                    early=False,
                    notify=False):
        """
        Writes out a SpawnMesh-altering hotfix to the mod file
        """

        # Early-level hotfix?
        if early:
            hf_type = Mod.TYPE[Mod.EARLYLEVEL]
        else:
            hf_type = Mod.TYPE[Mod.LEVEL]

        # Notify flag
        if notify:
            notification_flag = 1
        else:
            notification_flag = 0

        # Map path
        map_first, map_last = map_path.rsplit('/', 1)

        # Mesh path
        mesh_first, mesh_last = mesh_path.rsplit('/', 1)

        # Coordinates/transforms
        coord_parts = []
        for coords in [location, rotation, scale]:
            coord_parts.append(','.join([
                '{:.6f}'.format(n) for n in coords
            ]))
        coord_field = '|'.join(coord_parts)

        # Transparent-or-visible
        if transparent:
            transparent_flag = 1
        else:
            transparent_flag = 0

        print('{hf_type},(1,6,{notification_flag},{map_last}),{map_first},{mesh_first},{mesh_last},{coord_len},"{coord_field}",{transparent_flag}'.format(
            hf_type=hf_type,
            notification_flag=notification_flag,
            map_first=map_first,
            map_last=map_last,
            mesh_first=mesh_first,
            mesh_last=mesh_last,
            coord_len=len(coord_field),
            coord_field=coord_field,
            transparent_flag=transparent_flag,
        ), file=self.df)

    def close(self):
        """
        Closes us out
        """
        if not self.last_was_newline:
            self.newline()
        self.df.close()
        print('Wrote mod to {}'.format(self.filename))


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
            parts.append('BaseValueAttribute={}'.format(
                Mod.get_full_cond(self.bva, 'GbxAttributeData')))
        if self.full or self.ai != 'None':
            parts.append('AttributeInitializer={}'.format(
                Mod.get_full_cond(self.ai, 'BlueprintGeneratedClass')))
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


class ItemPoolListEntry(object):
    """
    Class to make dealing with ItemPoolList entries a bit easier
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
        parts.append('ItemPool={}'.format(
            Mod.get_full_cond(self.pool_name, 'ItemPool')))
        if self.probability and self.probability.has_data():
            parts.append('PoolProbability={}'.format(self.probability))
        if self.num and self.num.has_data():
            parts.append(
                'NumberOfTimesToSelectFromThisPool={}'.format(self.num))
        return '({})'.format(','.join(parts))


class ItemPoolEntry(object):
    """
    Some abstraction for items inside an ItemPool
    """

    def __init__(self, pool_name=None, balance_name=None, weight=None):
        """
        `weight` should be a BVC/BVCF object
        """
        self.pool_name = pool_name
        self.balance_name = balance_name
        self.weight = weight

    def __str__(self):
        """
        Outputs a string which can be used in a hotfix to represent this entry
        """
        parts = []
        if self.pool_name:
            parts.append('ItemPoolData={}'.format(
                Mod.get_full_cond(self.pool_name, 'ItemPoolData')))
        if self.balance_name:
            parts.append('InventoryBalanceData={}'.format(
                Mod.get_full_cond(self.balance_name)))
            parts.append('ResolvedInventoryBalanceData={}'.format(
                Mod.get_full_cond(self.balance_name, 'InventoryBalanceData')))
        if self.weight:
            parts.append('Weight={}'.format(self.weight))
        return '({})'.format(','.join(parts))


class ItemPool(object):
    """
    Some abstraction to easily build up ItemPools.
    """

    def __init__(self, pool_name):
        self.pool_name = pool_name
        self.balanceditems = []

    def add_pool(self, pool_name, weight=None):
        """
        Adds the specified `pool_name` to our ItemPool, optionally with the specified
        `weight`, which should be a BVC/BVCF object.  Weight will default to 1 if not
        specified.
        """
        if not weight:
            weight = BVC()
        self.balanceditems.append(ItemPoolEntry(
            pool_name=pool_name, weight=weight))

    def add_balance(self, balance_name, weight=None):
        """
        Adds the specified `balance_name` to our ItemPool, optionally with the specified
        `weight`, which should be a BVC/BVCF object.  Weight will default to 1 if not
        specified.
        """
        if not weight:
            weight = BVC()
        self.balanceditems.append(ItemPoolEntry(
            balance_name=balance_name, weight=weight))

    @staticmethod
    def from_data(data, pool_name):
        """
        Returns a new ItemPool object by loading `pool_name` from the BL3Data object `data`
        """

        pool = ItemPool(pool_name)
        pool_data = data.get_data(pool_name)[0]
        for bal in pool_data['BalancedItems']:
            if 'export' in bal['ItemPoolData']:
                bal_name = bal['ResolvedInventoryBalanceData'][1]
                pool.add_balance(bal_name, BVC.from_data_struct(bal['Weight']))
            else:
                pool_name = bal['ItemPoolData'][1]
                pool.add_pool(pool_name, BVC.from_data_struct(bal['Weight']))

        return pool

    def __str__(self):
        """
        Format our BalancedItems as a hotfix
        """
        return '({})'.format(','.join([str(i) for i in self.balanceditems]))


class Part(object):
    """
    Class to hold info about a single Part for an item/weapon.  Just the object name
    and its weight, basically a glorified dict.

    Very arguably this should exist in bl3data instead of bl3hotfixmod...
    """

    def __init__(self, part_name, weight=1):
        self.part_name = part_name
        self.short_name = part_name.split('/')[-1]
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
            raise TypeError(
                'PartCategory objects can only be added to other PartCategory objects')
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

    def clear(self):
        """
        Clears this category entirely
        """
        self.partlist = []

    def enable(self):
        """
        Enables the category
        """
        self.enabled = True

    def disable(self):
        """
        Disables the category
        """
        self.enabled = False

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

        # If we ever want to include the partlist again, we'd want to add in
        # `self.str_partlist()` to the `Parts=()` section in here.  The attribute
        # seems to be entirely ignored by the game engine, though, so we can
        # safely omit it.
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
            Parts=()
        )""".format(
            part_type_enum=Mod.get_full_cond(self.part_type_enum),
            index=self.index,
            select_multiple=str(self.select_multiple),
            use_weight_with_mult=str(self.use_weight_with_mult),
            num_min=self.num_min,
            num_max=self.num_max,
            enabled=str(self.enabled),
        )


class Balance(object):
    """
    Class for dealing with both Balances and PartSets -- the class will generate
    hotfixes to deal with the pair.  Technically the PartSet object does NOT
    need to have an enumerated parts list -- it seems to be completely ignored
    by the game.  We'll go ahead and generate those by default though, anyway,
    just so it matches the parts that are listed in the Balance.

    This class *does* pull in information about the anointments for the balance
    (in the `generics` attribute) but does NOT actually write out any data relating
    to generics.  The attribute will be a list of tuples, the first element of
    which is the path to the object where the anointment is coming from, and the
    second of which is a list of `(part_name, weight)` tuples.

    Very arguably this should exist in bl3data instead of bl3hotfixmod...
    """

    # PartSet mode mappings
    (PS_MODE_COMPLETE, PS_MODE_ADDITIVE, PS_MODE_SELECTIVE) = range(3)
    PS_MODE_MAPPING = {
        'EActorPartReplacementMode::Complete': PS_MODE_COMPLETE,
        # Additive is the default and will likely never actually show up in dumps
        'EActorPartReplacementMode::Additive': PS_MODE_ADDITIVE,
        'EActorPartReplacementMode::Selective': PS_MODE_SELECTIVE,
    }
    PS_MODE_DEFAULT = PS_MODE_ADDITIVE

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
        self.generics = []
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
        if not bal_obj:
            raise Exception('Could not find datafile for {}'.format(bal_name))
        if len(bal_obj) != 1:
            raise Exception('Unknown export count ({}) for: {}'.format(
                len(bal_obj), bal_name))
        last_bit = bal_name.split('/')[-1]
        bal_data = bal_obj[0]

        # Now.  *Previously* we would read parts in right from the Balance itself, but it turns out
        # that we can't always trust the "cached" RuntimePartList in the Balance object.
        # Specifically the DLC3 patch introduced some new parts for COMs which aren't present in
        # the on-disk Balance data, and while investigating that, it turns out we're being lied to
        # about a couple Artifact parts from the balance as well.  So, we *do*, in the end, have
        # to build the part lists from all the various PartSet objects which are used by the
        # game at runtime to generate RuntimePartList.  Again, this does nearly always match the
        # on-disk data for that attr, but not always, so let's Do The Right Thing here.

        # Get a list of PartSets that we need to process
        partset_names = []
        cur_bal_data = bal_data
        while True:
            partset_names.append(cur_bal_data['PartSetData'][1])
            if 'BaseSelectionData' in cur_bal_data and type(cur_bal_data['BaseSelectionData']) == list:
                base_sel_name = cur_bal_data['BaseSelectionData'][1]
                cur_bal_data = data.get_data(base_sel_name)
                if not cur_bal_data:
                    raise Exception(
                        'Could not find datafile for {}'.format(base_sel_name))
                cur_bal_data = cur_bal_data[0]
            else:
                break

        # Loop through the partset objects (note that we need to do the above list in reverse)
        # to grab parts by category, overwriting/appending where instructed to by the
        # PartSet object.
        generics = [(bal_name, [])]
        partlists = []
        partset_name = None
        partset_obj = None
        for partset_name in reversed(partset_names):
            partset_data = data.get_data(partset_name)
            if not partset_data:
                raise Exception(
                    'Could not find datafile for {}'.format(partset_name))
            partset_data = partset_data[0]

            # Figure out the mode of the PartSet APLs
            if 'ActorPartReplacementMode' in partset_data:
                partset_mode = Balance.PS_MODE_MAPPING[partset_data['ActorPartReplacementMode']]
            else:
                partset_mode = Balance.PS_MODE_DEFAULT

            # Grab our "generic" parts (anointments, basically).  Some of the code here is duplicated
            # below when processing part categories, alas.
            if 'GenericParts' in partset_data and partset_data['GenericParts']:
                category = partset_data['GenericParts']
                if partset_mode == Balance.PS_MODE_COMPLETE:
                    # First up: Complete
                    if 'bEnabled' in category and category['bEnabled']:
                        if 'Parts' in category:
                            for part in category['Parts']:
                                partdata = part['PartData']
                                weight = BVC.from_data_struct(part['Weight'])
                                if type(part['PartData']) == list:
                                    generics[0][1].append(
                                        (partdata[1], weight))
                                else:
                                    generics[0][1].append(('None', weight))

                elif partset_mode == Balance.PS_MODE_ADDITIVE:
                    # Next: Additive
                    if 'bEnabled' in category and category['bEnabled']:
                        if 'Parts' in category:
                            for part in category['Parts']:
                                partdata = part['PartData']
                                weight = BVC.from_data_struct(part['Weight'])
                                if type(part['PartData']) == list:
                                    generics[0][1].append(
                                        (partdata[1], weight))
                                else:
                                    generics[0][1].append(('None', weight))

                elif partset_mode == Balance.PS_MODE_SELECTIVE:
                    # Finally: Selective
                    if 'bEnabled' in category and category['bEnabled']:
                        generics = [(bal_name, [])]
                        if 'Parts' in category:
                            for part in category['Parts']:
                                partdata = part['PartData']
                                weight = BVC.from_data_struct(part['Weight'])
                                if type(part['PartData']) == list:
                                    generics[0][1].append(
                                        (partdata[1], weight))
                                else:
                                    generics[0][1].append(('None', weight))

                else:
                    # Not sure how we'd ever get here...
                    raise Exception(
                        'Unknown generics partset mode: {}'.format(partset_mode))

            # Loop through the APLs
            for idx, category in enumerate(partset_data['ActorPartLists']):

                # Make sure our partlists list is big enough
                if len(partlists) < (idx+1):
                    partlists.append([])

                # Behavior for each APL depends on what the mode is
                if partset_mode == Balance.PS_MODE_COMPLETE:
                    # First up: Complete
                    partlists[idx] = []
                    if category['bEnabled']:
                        for part in category['Parts']:
                            partdata = part['PartData']
                            weight = BVC.from_data_struct(part['Weight'])
                            if type(part['PartData']) == list:
                                partlists[idx].append((partdata[1], weight))
                            else:
                                partlists[idx].append(('None', weight))

                elif partset_mode == Balance.PS_MODE_ADDITIVE:
                    # Next: Additive
                    if category['bEnabled']:
                        for part in category['Parts']:
                            partdata = part['PartData']
                            weight = BVC.from_data_struct(part['Weight'])
                            if type(part['PartData']) == list:
                                partlists[idx].append((partdata[1], weight))
                            else:
                                partlists[idx].append(('None', weight))

                elif partset_mode == Balance.PS_MODE_SELECTIVE:
                    # Finally: Selective
                    if category['bEnabled']:
                        partlists[idx] = []
                        for part in category['Parts']:
                            partdata = part['PartData']
                            weight = BVC.from_data_struct(part['Weight'])
                            if type(part['PartData']) == list:
                                partlists[idx].append((partdata[1], weight))
                            else:
                                partlists[idx].append(('None', weight))

                else:
                    # Not sure how we'd ever get here...
                    raise Exception(
                        'Unknown partset mode: {}'.format(partset_mode))

        # Doublecheck we have a partset (don't know how we'd get here)
        if partset_name is None or partset_data is None:
            raise Exception('No Partset found')

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

        # If we have a BL3Data object to work with, find any extra anointments we'd be pulling in
        generics.extend(data.get_extra_anoints(bal_name))

        # No reason not to create a Balance object now
        bal = Balance(bal_name, partset_name, part_type_enum,
                      raw_bal_data=bal_data,
                      raw_ps_data=partset_data,
                      )

        # Populate the `generics` PartCategory inside the new Balance object
        bal.generics = generics

        # Loop through our partlists and populate our objects
        for idx, (partlist, apl) in enumerate(zip(partlists, partset_data['ActorPartLists'])):

            # Hardcoded fix - SparkPatchEntry210 was brought into the main game binary, and
            # alters the part range inside an APL for PartSet_Shield_Ward.  Will have to
            # just handle it stupidly like this, for now.
            if partset_name == '/Game/Gear/Shields/_Design/_Uniques/Ward/Balance/PartSet_Shield_Ward' and idx == 3:
                apl['MultiplePartSelectionRange']['Min'] = 1

            partcat = PartCategory(
                num_min=apl['MultiplePartSelectionRange']['Min'],
                num_max=apl['MultiplePartSelectionRange']['Max'],
                index=apl['PartType'],
                part_type_enum=apl['PartTypeEnum'][1],
                select_multiple=apl['bCanSelectMultipleParts'],
                use_weight_with_mult=apl['bUseWeightWithMultiplePartSelection'],
                enabled=apl['bEnabled'])
            for part, weight in partlist:
                # Weird data mangling here.  A couple of artifacts seem to reference
                # Artifact_Part_Stats_FireDamage and Artifact_Part_Stats_CryoDamage in
                # their JWP serializations, but both should have a `_2` suffix (all
                # the other artifacts already do that).  There is no valid object
                # *without* that `_2` suffix, so we're gonna cheat and alter the name
                # if we need to.
                if part == '/Game/Gear/Artifacts/_Design/PartSets/SecondaryStats/Elemental/Artifact_Part_Stats_FireDamage':
                    part = '/Game/Gear/Artifacts/_Design/PartSets/SecondaryStats/Elemental/Artifact_Part_Stats_FireDamage_2'
                elif part == '/Game/Gear/Artifacts/_Design/PartSets/SecondaryStats/Elemental/Artifact_Part_Stats_CryoDamage':
                    part = '/Game/Gear/Artifacts/_Design/PartSets/SecondaryStats/Elemental/Artifact_Part_Stats_CryoDamage_2'
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
            raise Exception(
                'part_type_enum must be defined for add_category_smart()')
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
    'Anger_P': "Castle Crimson",
    'Archive_P': "Dustbound Archives",
    'AtlasHQ_P': "Atlas HQ",
    'Bar_P': "Lodge",
    'Beach_P': "Tazendeer Ruins",
    'BloodyHarvest_P': "Heck Hole",
    'Camp_P': "Negul Neshai",
    'Cartels_P': "Villa Ultraviolet",
    'CasinoIntro_P': "Grand Opening",
    'Chase_P': "Sapphire's Run",
    'City_P': "Meridian Metroplex",
    'CityBoss_P': "Forgotten Basilica",
    'CityVault_P': "Neon Arterial",
    'Convoy_P': "Sandblast Scar",
    'Core_P': "Jack's Secret",
    'COVSlaughter_P': "Slaughter Shaft",
    'CraterBoss_P': "Crater's Edge",
    'CreatureSlaughter_P': "Cistern of Slaughter",
    'Crypt_P': "Pyre of Stars",
    'Desert_P': "Devil's Razor",
    'DesertBoss_P': "Great Vault",
    'Desertvault_P': "Cathedral of the Twin Gods",
    'Desolate_P': "Desolation's Edge",
    'Eldorado_P': "Vaulthalla",
    'Experiment_P': "Benediction of Pain",
    'Facility_P': "Bloodsun Canyon",
    'FinalBoss_P': "Destroyer's Rift",
    'Forest_P': "Obsidian Forest",
    'Frontier_P': "The Blastplains",
    'FrostSite_P': "Stormblind Complex",
    'GuardianTakedown_P': "Minos Prime / The Shattered Tribunal",
    'Impound_P': "Impound Deluxe",
    'Lake_P': "Skittermaw Basin",
    'Lodge_P': "Ashfall Peaks",
    'Mansion_P': "Jakobs Estate",
    'MarshFields_P': "Ambermire",
    'Mine_P': "Konrad's Hold",
    'Monastery_P': "Athenas",
    'Motorcade_P': "Splinterlands",
    'MotorcadeFestival_P': "Carnivora",
    'MotorcadeInterior_P': "Guts of Carnivora",
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
    'Sanctum_P': "The Psychoscape",
    'Strip_P': "Spendopticon",
    'TechSlaughter_P': "Slaughterstar 3000",
    'TowerLair_P': "VIP Tower",
    'Towers_P': "Lectra City",
    'Town_P': "Vestige",
    'Trashtown_P': "Compactor",
    'Venue_P': "Heart's Desire",
    'Village_P': "Cursehaven",
    'Watership_P': "Voracious Canopy",
    'Wetlands_P': "Floodmoor Basin",
    'WetlandsBoss_P': "Floating Tomb",
    'WetlandsVault_P': "Blackbarrel Cellars",
    'Woods_P': "Cankerwood",
}

# Also create a lowercase version
LVL_TO_ENG_LOWER = {}
for k, v in list(LVL_TO_ENG.items()):
    LVL_TO_ENG_LOWER[k.lower()] = v