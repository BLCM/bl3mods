#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import json
import glob
import appdirs
import MySQLdb
import subprocess
import configparser

class BL3Data(object):
    """
    Class to assist in programmatically inspecting Borderlands 3 data as much as
    possible.  The first time this class is instantiated, it'll create a config
    file and then error out.  To use the class, populate at least the "filesystem"
    section of the config file (the path will be provided on the console).

    The "filesystem" section contains two config values:

        1) data_dir - This is a directory containing data extracted from the BL3
           .pak files using UnrealPak.  It should also be processed so that the
           pathnames on the filesystem match the object names exactly.

        2) ueserialize_path - This is the path to a 'ueserialize' binary from the
           JohnWickParse project, used to serialize borderlands .uasset/.umap files
           to a JSON object.  This is what's used to process the extracted data into
           a format we can work with, on an on-demand basis.
           https://github.com/SirWaddles/JohnWickParse

    The "database" section contains the values "host", "db", "user", and "passwd".
    These define the connection parameters to a MySQL database populated with BL3
    reference data, which can be found at: http://apocalyptech.com/games/bl3-refs/
    This is only required if you want to use the `get_refs_to()` or `get_refs_from()`
    methods of this class, and BL3Data will not attempt any database connections
    until either of those methods are called.
    """

    # Data serialization version requirements
    data_version = 1

    # Hardcoded BVA values
    bva_values = {
            }

    def __init__(self):
        """
        Initialize a BL3Data object.  Will create a sample config file if one
        is not already found.  Will require that the "filesystem" section be
        properly filled in, or we'll raise an exception.
        """

        config_dir = appdirs.user_config_dir('bl3data')

        # Create the config dir if it doesn't exist
        if not os.path.exists(config_dir):
            os.makedirs(config_dir, exist_ok=True)

        # Create a sample INI file it if doesn't exist
        self.config_file = os.path.join(config_dir, 'bl3data.ini')
        if not os.path.exists(self.config_file):
            config = configparser.ConfigParser()
            config['filesystem'] = {
                    'data_dir': 'CHANGEME',
                    'ueserialize_path': 'CHANGEME',
                    }
            config['mysql'] = {
                    'host': 'CHANGEME',
                    'db': 'CHANGEME',
                    'user': 'CHANGEME',
                    'passwd': 'CHANGEME',
                    }
            with open(self.config_file, 'w') as odf:
                config.write(odf)
            print('Created sample config file {}'.format(self.config_file))

        # Read in the config file and at least make sure we have filesystem
        # data available
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)
        self._enforce_config_section('filesystem')

        # Convenience var
        self.data_dir = self.config['filesystem']['data_dir']

        # Now the rest of the vars we'll use
        self.cache = {}
        self.db = None
        self.curs = None

    def _enforce_config_section(self, section_name):
        """
        Raises an exception if the configuration section `section_name` hasn't
        been changed from its "CHANGEME" defaults.
        """
        if any([v == 'CHANGEME' for v in self.config[section_name].values()]):
            raise Exception('Populate the "{}" section in {} to continue'.format(
                section_name,
                self.config_file,
                ))

    def _connect_db(self):
        """
        Attempts to connect to the refs database, if we haven't already done so.
        """
        if self.db is None:
            self._enforce_config_section('mysql')
            self.db = MySQLdb.connect(
                    user=self.config['mysql']['user'],
                    passwd=self.config['mysql']['passwd'],
                    host=self.config['mysql']['host'],
                    db=self.config['mysql']['db'],
                    )
            self.curs = self.db.cursor()

    def get_data(self, obj_name):
        """
        Returns a JSON-serialized version of the object `obj_name`, if possible.
        May return None, either due to the object not existing, or if JohnWickParse
        can't actually produce a serialization for the object.  Results will be
        cached, so requesting the same object more than once will not result in
        re-parsing JSON content.
        """
        if obj_name not in self.cache:

            base_path = '{}{}'.format(self.data_dir, obj_name)
            json_file = '{}.json'.format(base_path)
            if not os.path.exists(json_file):
                # PyPy3 is still on 3.6, which doesn't have capture_output
                #subprocess.run([self.config['filesystem']['ueserialize_path'], base_path], encoding='utf-8', capture_output=True)
                subprocess.run([self.config['filesystem']['ueserialize_path'], base_path], encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if os.path.exists(json_file):
                with open(json_file) as df:
                    self.cache[obj_name] = json.load(df)
                if len(self.cache[obj_name]) > 0:
                    if '_apoc_data_ver' not in self.cache[obj_name][0] or self.cache[obj_name][0]['_apoc_data_ver'] < BL3Data.data_version:
                        # Regenerate if we have an old serialization
                        subprocess.run([self.config['filesystem']['ueserialize_path'], base_path], encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        with open(json_file) as df:
                            self.cache[obj_name] = json.load(df)
            else:
                self.cache[obj_name] = None

        return self.cache[obj_name]

    def find(self, base, prefix):
        """
        Given a base object path `base`, recursively search through to find any
        objects with the prefix `prefix`.  Will match case-insensitively.  Will
        yield the object names as they're found.
        """
        prefix_lower = prefix.lower()
        base_dir = '{}{}'.format(self.data_dir, base)
        results = []
        for (dirpath, dirnames, filenames) in os.walk(base_dir):
            obj_base = dirpath[len(self.data_dir):]
            for filename in filenames:
                if filename.lower().startswith(prefix_lower) and filename.endswith('.uasset'):
                    yield os.path.join(obj_base, filename[:-7])

    def find_data(self, base, prefix):
        """
        Given a base object path `base`, recursively search through to find any
        objects with the prefix `prefix`.  Will match case-insensitively.  Will
        yield the JSON-serialized data of the objects (or None, if no serialization
        is possible) as they're found.
        """
        for obj_name in self.find(base, prefix):
            yield (obj_name, self.get_data(obj_name))

    def glob(self, glob_pattern):
        """
        Find classes which match the given `glob_pattern` and yield the
        object names which were found.
        https://en.wikipedia.org/wiki/Glob_(programming)
        """
        for filename in glob.glob('{}{}'.format(self.data_dir, glob_pattern)):
            if filename.endswith('.uasset'):
                yield filename[len(self.data_dir):-7]

    def glob_data(self, glob_pattern):
        """
        Find classes which match the given `glob_pattern` and yield the
        serialized object data for each (or None if unavailable).
        https://en.wikipedia.org/wiki/Glob_(programming)
        """
        for obj_name in self.glob(glob_pattern):
            yield (obj_name, self.get_data(obj_name))

    def get_export_idx(self, obj_name, export_idx):
        """
        Given an object `obj_name`, return the specified export at `export_idx`, or
        None.
        """
        if export_idx == 0:
            return None
        data = self.get_data(obj_name)
        if export_idx > len(data):
            return None
        else:
            return data[export_idx-1]

    def get_exports(self, obj_name, export_type):
        """
        Given an object `obj_name`, return a list of serialized exports which match
        the type `export_type`.
        """
        exports = []
        data = self.get_data(obj_name)
        if data:
            for export in data:
                if export['export_type'] == export_type:
                    exports.append(export)
        return exports

    def get_refs_to(self, obj_name):
        """
        Find all object names which reference the given `obj_name`, and return
        a list of those objects.  Requires a database connection to the refs
        database.
        """
        self._connect_db()
        self.curs.execute("""select o2.name
                from bl3object o, bl3refs r, bl3object o2
                where
                    o.name=%s
                    and o.id=r.to_obj
                    and o2.id=r.from_obj
                """, (obj_name,))
        return [row[0] for row in self.curs.fetchall()]

    def get_refs_from(self, obj_name):
        """
        Find all object names which `obj_name` references, and return
        a list of those objects.  Requires a database connection to the refs
        database.
        """
        self._connect_db()
        self.curs.execute("""select o2.name
                from bl3object o, bl3refs r, bl3object o2
                where
                    o.name=%s
                    and o.id=r.from_obj
                    and o2.id=r.to_obj
                """, (obj_name,))
        return [row[0] for row in self.curs.fetchall()]

    def datatable_lookup(self, table_name, row_name, col_name):
        """
        Given a `table_name`, `row_name`, and `col_name`, return the specified cell.
        """
        data = self.get_exports(table_name, 'DataTable')[0]
        return data[row_name][col_name]

    def process_bvc_struct(self, data):
        """
        Given a serialized BVC/BVSC/etc structure, return a value.
        """

        # BVC
        if 'BaseValueConstant' in data:
            bvc = data['BaseValueConstant']
        else:
            bvc = 1

        # DT
        if 'DataTableValue' in data and 'export' not in data['DataTableValue']['DataTable']:
            raise Exception('datatable: {}'.format(data['DataTableValue']['DataTable']))

        # BVA
        if 'BaseValueAttribute' in data and 'export' not in data['BaseValueAttribute']:
            attr_name = data['BaseValueAttribute'][1]
            if attr_name in self.bva_values:
                bvc = self.bva_values[attr_name]
            else:
                # Try to read the attr
                base = self.get_exports(attr_name, 'GbxAttributeData')
                if len(base) != 1:
                    raise Exception('bva: {}'.format(attr_name))
                if 'ValueResolver' not in base[0]:
                    raise Exception('bva: {}'.format(attr_name))
                lookup_export = base[0]['ValueResolver']['export']
                lookup = self.get_export_idx(attr_name, lookup_export)
                lookup_type = lookup['export_type']
                if lookup_type == 'ConstantAttributeValueResolver':
                    bvc = lookup['Value']['BaseValueConstant']
                    #print('{} -> {}'.format(attr_name, bvc))
                elif lookup_type == 'DataTableAttributeValueResolver':
                    table_name = lookup['DataTableRow']['DataTable'][1]
                    row = lookup['DataTableRow']['RowName']
                    col = lookup['Property']['ParsedPath']['PropertyName']
                    bvc = self.datatable_lookup(table_name, row, col)
                    #print('{} -> {}'.format(attr_name, bvc))
                else:
                    raise Exception('Unknown bva type {} for {}'.format(lookup_type, attr_name))

        # AI
        if 'AttributeInitializer' in data and 'export' not in data['AttributeInitializer']:
            raise Exception('ai: {}'.format(data['BaseValueAttribute']))

        # BVS
        if 'BaseValueScale' in data:
            return bvc * data['BaseValueScale']
        else:
            return bvc

