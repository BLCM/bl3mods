#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Borderlands 3 Data Processing Scripts
# Copyright (C) 2022 CJ Kucera
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import sys
import json
import html
import argparse
import textwrap
import subprocess

# Default external commands we call
cmd_serialize = '/home/pez/bin/ueserialize'

def main():

    global cmd_serialize

    # Arguments
    parser = argparse.ArgumentParser(
            description='Get dialogue lines given a dialogscript and guid',
            )

    parser.add_argument('-s', '--serialize',
            type=str,
            default=cmd_serialize,
            help='Command to use for object serialization',
            )

    parser.add_argument('filename',
            nargs=1,
            type=str,
            help='DialogScript filename',
            )

    parser.add_argument('guids',
            nargs='+',
            type=str,
            help='GUID',
            )

    args = parser.parse_args()
    cmd_serialize = args.serialize
    filename = args.filename[0]

    # Grab the filename to process
    if filename.endswith('.'):
        filename = filename[:-1]
    if '.' in filename:
        filename_base, ext = filename.rsplit('.', 1)
        if ext not in {'json', 'uasset', 'uexp'}:
            raise RuntimeError('Unknown filename: {}'.format(filename))
        filename = filename_base

    # Serialize it (might be already serialized, but don't bother checking)
    subprocess.run([cmd_serialize, 'serialize', filename])

    # Make sure it worked
    json_path = '{}.json'.format(filename)
    if not os.path.exists(json_path):
        raise RuntimeError('Could not find {}'.format(json_path))

    # Collect GUIDs into a set
    guid_set = set(args.guids)

    # Get results
    results = {}
    with open(json_path) as df:
        data = json.load(df)
        for export in data:
            if export['export_type'] == 'DialogTimeSlotData':
                if export['Guid'] in guid_set:
                    guid = export['Guid']
                    results[guid] = []
                    for line_idx, line in enumerate(export['Lines']):
                        linedata = data[line['export']-1]
                        for perf_idx, perf in enumerate(linedata['Performances']):
                            perfdata = data[perf['export']-1]
                            text = perfdata['Text']['string']
                            results[guid].append(f'{guid} | {line_idx} | {perf_idx} | {text}')

    # Report on results
    for guid in args.guids:
        if guid in results:
            for line in results[guid]:
                print(line)
            print('')
        else:
            print(f'{guid} - Not found!')
            print('')

if __name__ == '__main__':
    main()
