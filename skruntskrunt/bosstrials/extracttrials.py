import json
import sys
import random
import argparse

version = '0.1.0'
INPUT='jwp.json'
TRIALDFL=1
OUTPUT=f'trial{TRIALDFL}.json'
def parse_args():
    parser = argparse.ArgumentParser(description=f'Trial Fact Extactor Generator v{version}')
    parser.add_argument('--input', type=str, help='jwp json file')
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

def main(args):
    jwp = json.load(open(args.input))
    oakmissionspawners = [x for x in jwp if x.get(EXPORT_TYPE,None) == OAKMISSIONSPAWNER]
    spawn_points = [x[NAME] for x in jwp if 'SpawnPointComponent' in x]
    # spawn_points = [oms[NAME] for oms in oakmissionspawners]
    all_facts = {
        "spawnoptions":None,
        "spawnpoints" :spawn_points,
    }
    facts = []
    # resolve spawner components
    # print("Resolve Spawner Components")
    for oms in oakmissionspawners:
        # print(oms[SPAWNERCOMPONENT])
        oms[SPAWNERCOMPONENT] = find_jwp_by_id(jwp,oms[SPAWNERCOMPONENT][EXPORT])[0]
        if oms[SPAWNERCOMPONENT] == []:
            print("Empty Component?")
    # resolve spawner style
    # print("Resolve Spawner Style")
    for oms in oakmissionspawners:
        if SPAWNERSTYLE in oms[SPAWNERCOMPONENT]:
            st = oms[SPAWNERCOMPONENT][SPAWNERSTYLE]
            oms[SPAWNERCOMPONENT][SPAWNERSTYLE] = find_jwp_by_id(jwp,st[EXPORT])[0]
    # resolve spawner style fo waves
    for oms in oakmissionspawners:
        st = oms[SPAWNERCOMPONENT].get(SPAWNERSTYLE,{})
        if WAVES in st:
            waves = st[WAVES]
            for wave in waves:
                export_id = wave[SPAWNERSTYLE][EXPORT]
                # print(f'export_id: {export_id}')
                wave[SPAWNERSTYLE] = find_jwp_by_id(jwp,export_id)[0]
        else:
            print(f"Doesn't have waves? {oms[NAME]}")
    # output it
    sos = set()
    for oms in oakmissionspawners:
        st = oms[SPAWNERCOMPONENT][SPAWNERSTYLE]
        for wave_i,wave in enumerate(st.get(WAVES,[])):
            # print(f'wave_i: {wave_i} {oms[NAME]}')
            # print(i,wave)
            # print(wave[SPAWNERSTYLE])
            so = wave[SPAWNERSTYLE][SPAWNOPTIONS][1]
            sos.add(so)
            fact = {SPAWNOPTIONS:None, NUMACTORS:None}
            fact_key = f'{oms[NAME]}.{SPAWNERCOMPONENT}.{SPAWNERSTYLE}.{WAVES}.{WAVES}[{wave_i}].{SPAWNERSTYLE}.{SPAWNOPTIONS}'
            fact_val = f'{so}'
            fact["wave"] = f'{wave_i}'
            # print(f'{fact_key},{fact_val}')
            fact[SPAWNOPTIONS] = {fact_key: fact_val}
            num_actors = deep_get(wave,[SPAWNERSTYLE,NUMACTORS,ATTRINIT,BASEVALUECONSTANT],-1)
            fact_key = f'{oms[NAME]}.{SPAWNERCOMPONENT}.{SPAWNERSTYLE}.{WAVES}.{WAVES}[{wave_i}].{SPAWNERSTYLE}.{NUMACTORS}.{ATTRINIT}'
            fact_val = f'{num_actors}'
            fact[NUMACTORS] = {fact_key: fact_val}
            facts.append(fact)
    print(json.dumps(facts,indent=1))
    all_facts["spawnoptions"] = facts
    all_facts["spawnpoints"] = spawn_points
    all_facts["spawnoption_list"] = sorted(list(sos))
    with open(args.output,'w') as fd:
        json.dump(all_facts,fd,indent=1)
    
if __name__ == "__main__":
    args = parse_args()
    main(args)
