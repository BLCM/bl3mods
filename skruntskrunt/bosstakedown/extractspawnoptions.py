import json
import sys
import random
import argparse
import subprocess

version = '0.1.0'
INPUT='jwp.json'
OUTPUT=f'spawnoptions.json'
def parse_args():
    parser = argparse.ArgumentParser(description=f'SpawnOption Fact Extactor Generator v{version}')
    parser.add_argument('--input', type=str, help='trial.json')
    parser.add_argument('--output', type=str, default=OUTPUT, help='factfile')
    return parser.parse_args()

NAME="_jwp_object_name"
EXPORT_ID="_jwp_export_idx"
EXPORT="export"

def find_jwp_by_id(jwp, export_id):
    # print(export_id)
    return [x for x in jwp if int(x.get(EXPORT_ID,-1)) == export_id]

OAKMISSIONSPAWNER="OakMissionSpawner"
EXPORT_TYPE="export_type"
SPAWNERCOMPONENT="SpawnerComponent"
SPAWNERSTYLE="SpawnerStyle"
SPAWNOPTIONS="SpawnOptions"
SPAWNOPTIONDATA="SpawnOptionData"
WAVES="Waves"
NUMACTORS="NumActorsParam"
ATTRINIT="AttributeInitializationData"
BASEVALUECONSTANT="BaseValueConstant"

def deep_get(h, keys, dfl=-1):
    if keys[0] in h:
        if len(keys) > 1:
            return deep_get(h[keys[0]], keys[1:], dfl=dfl)
        else:
            return h[keys[0]]
    else:
        return dfl


def open_jwp(so):
    command = f'bash jwp-json.sh {so}'
    print(command)
    result = subprocess.check_output(command, shell=True)
    # print(result)
    return json.loads(result)
    
def main(args):
    trial = json.load(open(args.input))
    sos   = trial["spawnoption_list"]
    seen = {}
    entries = []
    work = sos + []
    while len(work) > 0:
        so = work.pop(0)
        if so in seen:
            continue
        seen[so] = True
        # for so in sos:
        print(so)
        jso = open_jwp(so)
        sod = [x for x in jso if x.get(EXPORT_TYPE,None) == SPAWNOPTIONDATA][0]
        for option in sod["Options"]:
            idx = option["_jwp_arr_idx"]
            factory = option["Factory"]["_jwp_export_dst_name"]
            factoryid = option["Factory"][EXPORT]
            actor = find_jwp_by_id(jso, factoryid)[0]
            if "AIActorClass" in actor:
                asset = actor["AIActorClass"]["asset_path_name"]
                entries.append( (so, factory, idx, asset) )
            elif "Options" in actor:
                # this is a spawnfactory container instead?
                # these are external SpawnOptions we can't do much about :(
                # TODO DEAL WITH THIS
                print(f"Options {so} {factory} {idx}", actor)
                work.append(actor["Options"][1])
            else:
                # this is a spawnfactory container instead?
                # these are external SpawnOptions we can't do much about :(
                # TODO DEAL WITH THIS
                print(f"Missing AIAactorCLass {so} {factory} {idx}", actor)

    with open(args.output,'w') as fd:
        json.dump(entries,fd,indent=1)
    
if __name__ == "__main__":
    args = parse_args()
    main(args)
