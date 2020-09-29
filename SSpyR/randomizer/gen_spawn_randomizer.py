from bl3hotfixmod import Mod
from bl3data import BL3Data
import os, random

# Utils: spawnoptions.txt and bpchars.txt
# Maybe make spawn points higher to prevent falling throug the earth
# Some enemy spawns may not be under and /Enemies directory (see Dandelion's CrewChallenges/Kill/ directory)

mod=Mod('spawn_randomizer.bl3hotfix',
'Spawn Randomizer',
'SSpyR',
[
   'Mod that randomizes enemies spawns to varying success'
],
lic=Mod.CC_BY_SA_40,
cats='spawns'
)

data=BL3Data()

dir=os.path.dirname(__file__)

bpchars=open(os.path.join(dir, 'bpchars.txt')).readlines()
spawnoptions=open(os.path.join(dir, 'spawnoptions.txt')).readlines()

for spwop in spawnoptions:
    auxchar=bpchars.copy()
    allexports=data.get_data(spwop)
    try:
        optdata=data.get_exports(spwop, 'SpawnOptionData')[0]
        for idx, option in enumerate(optdata['Options']):
            export_idx=option['Factory']['export']
            randchar=random.choice(auxchar)
            bpchar=randchar
            index=auxchar.index(bpchar)
            del auxchar[index]
            cond=bpchar.split('/')
            cond='.'+cond[len(cond)-1]+'_C'
            bpchar=bpchar+cond

            factory = allexports[export_idx-1]
            location=None
            try:
                location=factory['SpawnExtent']
            except KeyError:
                print('No Spawn Extent')

            mod.reg_hotfix(Mod.EARLYLEVEL, 'MatchAll',
            str.rstrip(spwop),
            'Options.Options[{}].Factory.Object..AIActorClass'.format(idx),
            Mod.get_full_cond(bpchar, 'BlueprintGeneratedClass')
            )
            mod.newline()
            #if location != None:
            #    location['z']=900
            #    heightnum=location['z']

            #    mod.reg_hotfix(Mod.EARLYLEVEL, 'MatchAll',
            #    str.rstrip(spwop),
            #    'Options.Options[{}].Factory.Object..SpawnExtent'.format(idx),
            #    location
            #    )
            #    mod.newline()
            
    except IndexError:
        print('No Exports of Type SpawnOptionData')