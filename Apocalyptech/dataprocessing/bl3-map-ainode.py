#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Borderlands 3 Data Processing Scripts
# Copyright (C) 2023 CJ Kucera
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
import argparse
import textwrap
import subprocess
try:
    import pandas
    import plotly.express
    have_plotly = True
except ModuleNotFoundError:
    print('NOTICE: pandas/plotly not found -- will only generate graphviz component')
    have_plotly = False


# I suspect this probably doesn't cope well with circular paths, though I'm
# guessing the game wouldn't, either.  So hopefully we don't run into those.

# The plotly stuff was just grafted rudely on top of the existing graphviz
# stuff and isn't done "right."  It's also pretty dependent on finding nodes
# in the "right" order, for the lines to be drawn properly.  We just take it
# for granted that we're reading them in chronological order.  This *should*
# be the case for the "main" ones taken from the Default__ object, but could
# very well be wrong if there's other orphans out there.  (For my initial use
# case, all the orphans were just single nodes, so I don't know how common
# that would be.)


class GVStyle:

    def __init__(self, shape, fillcolor, color='black', styles=None, margin=None):
        self.shape = shape
        self.fillcolor = fillcolor
        self.color = color
        if styles is None:
            styles = []
        self.style = ','.join(['filled', *styles])
        self.margin = margin

        parts = [
                f'shape={self.shape}',
                f'color={self.color}',
                f'fillcolor={self.fillcolor}',
                f'style={self.style}',
                ]
        if self.margin is not None:
            parts.append(f'margin="{self.margin}"')
        self.attrs = ' '.join(parts)


class GVNode:

    def __init__(self, index, style, lines, prefix='n'):
        self.index = index
        self.prefix = prefix
        self.identifier = f'{self.prefix}{self.index}'
        self.style = style
        self.lines = lines
        # stupid hardcoding here; whatever.
        if prefix != 'l':
            self.lines.append(f'<i>(export {self.index})</i>')
        self.label = '<br/>'.join(lines)

    def output(self):
        return f'{self.identifier} [label=<{self.label}> {self.style.attrs}];'


class AINodeComponent:

    # graphviz styles to use
    gvs_loc_node = GVStyle('cds', 'cyan', margin='0.15,0.15')

    def __init__(self, parent, export_ref):
        global plotly_data
        global cur_color
        global cur_idx

        self.parent = parent
        self.catalog = self.parent.catalog
        self.export_ref = export_ref
        self.export_idx = export_ref['export']
        self.export = self.catalog.data[self.export_idx-1]
        lines = []
        if 'ArrivalThreshold' in self.export:
            self.arrival_threshhold = self.export['ArrivalThreshold']
            lines.append(f'Arrival Threshhold: {self.arrival_threshhold}')
        else:
            self.arrival_threshhold = None
        self.x = self.export['RelativeLocation']['x']
        self.y = self.export['RelativeLocation']['y']
        self.z = self.export['RelativeLocation']['z']
        plotly_data['x'].append(self.x)
        plotly_data['y'].append(self.y)
        plotly_data['z'].append(self.z)
        plotly_data['color'].append(cur_color)
        plotly_data['text'].append(cur_idx)
        hover_text = [
                f'Order: {cur_idx}',
                f'AINode Name: {self.parent.name}',
                f'AINode Export: {self.parent.export_idx}',
                f'Component Export: {self.export_idx}',
                ]
        plotly_data['hover_name'].append('<br>'.join(hover_text))
        cur_idx += 1
        lines.append(f'({self.x}, {self.y}, {self.z})')
        if 'RelativeRotation' in self.export:
            self.pitch = self.export['RelativeRotation']['pitch']
            self.yaw = self.export['RelativeRotation']['yaw']
            self.roll = self.export['RelativeRotation']['roll']
            lines.append(f'rot: ({self.pitch}, {self.yaw}, {self.roll})')
        else:
            self.pitch = 0
            self.yaw = 0
            self.roll = 0
        self.links = []
        if 'LinksTo' in self.export:
            for link_to in self.export['LinksTo']:
                if 'Actor' not in link_to:
                    raise RuntimeError(f'No "Actor" attr in LinkTo, export {self.export_idx}')
                self.links.append(self.catalog.load_node(link_to['Actor']))

        self.gvnode = GVNode(self.export_idx, AINodeComponent.gvs_loc_node, lines)
        self.gvlinks = []
        for link in self.links:
            self.gvlinks.append((self.gvnode, link.gvnodes[0]))


class AINode:

    # graphviz styles to use
    gvs_top_label = GVStyle('house', 'aquamarine')
    gvs_top_node = GVStyle('box', 'burlywood1')

    def __init__(self, catalog, export_ref, top_label=None):

        self.catalog = catalog
        self.export_ref = export_ref
        self.top_label = top_label
        self.export_idx = export_ref['export']
        self.export = self.catalog.data[self.export_idx-1]
        self.name = self.export['_jwp_object_name']
        self.component = AINodeComponent(self, self.export['AINodeComponent'])

        self.gvnodes = []
        self.gvlinks = []
        self.gvnodes.append(GVNode(self.export_idx, AINode.gvs_top_node, [self.name]))
        if self.top_label:
            self.gvnodes.insert(0, GVNode(self.export_idx, AINode.gvs_top_label, [self.top_label], prefix='l'))
            self.gvlinks.append((self.gvnodes[0], self.gvnodes[1]))
        self.gvlinks.append((self.gvnodes[-1], self.component.gvnode))
        self.gvnodes.append(self.component.gvnode)
        self.gvlinks.extend(self.component.gvlinks)


class Catalog:

    def __init__(self, data):
        self.data = data
        self.nodes = {}

    def load_node(self, export_ref, top_label=None):
        export_idx = export_ref['export']
        if export_idx not in self.nodes:
            ainode = AINode(self, export_ref, top_label)
            self.nodes[export_idx] = ainode
        return self.nodes[export_idx]

    def load_node_export(self, export):
        # This is stupid, whatever.
        export_idx = export['_jwp_export_idx']
        export_ref = {
                'export': export_idx,
                }
        return self.load_node(export_ref)

    def __iter__(self):
        return iter(self.nodes.values())


parser = argparse.ArgumentParser(
        description='Generate graphviz+plotly graphs describing BL3/WL map-based AINode paths',
        )

parser.add_argument('-r', '--render',
        default='svg',
        choices={'svg', 'png', 'jpg', 'gif'},
        help='Render type',
        )

parser.add_argument('-s', '--serialize',
        type=str,
        default='/home/pez/bin/ueserialize',
        help='Command to use to serialize data',
        )

parser.add_argument('-d', '--dot',
        type=str,
        default='/usr/bin/dot',
        help='Path to Grpahviz dot executable',
        )

parser.add_argument('-v', '--view',
        type=str,
        default='/usr/bin/feh',
        help='Path to viewer application',
        )

parser.add_argument('filename',
        nargs=1,
        help='Filename to serialize and render',
        )

args = parser.parse_args()
args.filename = args.filename[0]

# Grab the filename to process
filename = args.filename
if filename.endswith('.'):
    filename = filename[:-1]
if '.' in filename:
    filename_base, ext = filename.rsplit('.', 1)
    if ext not in {'json', 'uasset', 'uexp', 'umap'}:
        raise Exception('Unknown filename: {}'.format(filename))
    filename = filename_base

# Serialize it (might be already serialized, but don't bother checking)
subprocess.run([args.serialize, 'serialize', filename])

# Make sure it worked
json_path = '{}.json'.format(filename)
if not os.path.exists(json_path):
    raise Exception('Could not find {}'.format(json_path))

# Open the JSON and parse it
plotly_data = {
        'x': [],
        'y': [],
        'z': [],
        'color': [],
        'text': [],
        'hover_name': [],
        }
cur_color = None
with open(json_path) as df:
    data = json.load(df)
    catalog = Catalog(data)

    found_main_export = False
    top_nodes = []
    for export in data:
        export_type = export['export_type']
        if export_type.endswith('_C') and export['_jwp_object_name'] == f'Default__{export_type}':
            # Load any main node paths directly referenced by the map
            found_main_export = True
            for k, v in export.items():
                if type(v) == dict and '_jwp_export_dst_type' in v and v['_jwp_export_dst_type'] == 'AINode':
                    cur_idx = 0
                    cur_color = k
                    catalog.load_node(v, k)
        elif export_type == 'AINode':
            # Load any "orphan" node paths which aren't directly referenced by the map
            cur_idx = 0
            cur_color = export['_jwp_object_name']
            catalog.load_node_export(export)

    if not found_main_export:
        print('ERROR: Did not find main export in object')
        sys.exit(1)

# Now generate a DOT graph
dot_path = '{}_ainodes.dot'.format(filename)
with open(dot_path, 'wt') as odf:
    if '/' in filename:
        obj_name = filename.split('/')[-1]
    else:
        obj_name = filename
    print('digraph {} {{'.format(obj_name), file=odf)
    print('', file=odf)

    print('// Main Graph Label', file=odf)
    print('labelloc = "t";', file=odf)
    print('fontsize = 16;', file=odf)
    print('label = <{}>'.format(obj_name), file=odf)
    print('', file=odf)

    print('// Exports', file=odf)
    for node in catalog:
        for gvnode in node.gvnodes:
            print(gvnode.output(), file=odf)
    print('', file=odf)

    print('// Attributes and Links', file=odf)
    for node in catalog:
        for from_node, to_node in node.gvlinks:
            print(f'{from_node.identifier} -> {to_node.identifier};', file=odf)
    print('', file=odf)

    print('}', file=odf)
print('Wrote dotfile to {}!'.format(dot_path))

# Now generate graphviz
final_path = '{}_ainodes.{}'.format(filename, args.render)
subprocess.run([args.dot, '-T{}'.format(args.render), dot_path, '-o', final_path])

# Now generate plotly
if have_plotly:
    html_path = f'{filename}_ainodes.html'
    fig = plotly.express.line_3d(
            plotly_data,
            x='x',
            y='y',
            z='z',
            color='color',
            text='text',
            hover_name='hover_name',
            markers=True,
            title=filename,
            )
    fig.update_traces(marker=dict(
        size=5,
        line=dict(
            color='black',
            width=1,
            ),
        ))
    fig.update_layout(
            scene=dict(
                xaxis=dict(
                    autorange='reversed',
                    ),
                aspectmode='data',
                ),
            )
    fig.write_html(html_path,
            include_plotlyjs='cdn',
            )
    if os.path.exists(html_path):
        print(f'Wrote to {html_path}')
    else:
        print(f'ERROR: {html_path} was not written')
else:
    print('Skipped plotly generation because either pandas or plotly was not found')

# ... and display it, if it worked
if os.path.exists(final_path):
    print('Wrote to {}'.format(final_path))
    subprocess.run([args.view, final_path])
else:
    print('ERROR: {} was not written'.format(final_path))

