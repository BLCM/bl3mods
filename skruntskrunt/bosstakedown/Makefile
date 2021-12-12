SEED=42
MALIWANLEVEL=Raid_P
MALIWANPATH=/Game/PatchDLC/Raid1/Maps/Raid/Raid_Combat.Raid_Combat
DATA=spawnoptions.takedown.json spawnoptions.maliwan.json takedown.json maliwantakedown.json

takedown.json: extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.json --output takedown.json

maliwantakedown.json: extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/PatchDLC/Raid1/Maps/Raid/Raid_Combat.json --output maliwantakedown.json


default: bosstakedown.42.bl3hotfix bossmaliwantakedown.42.bl3hotfix $(DATA)

clean:
	rm -f bosstakedown.42.bl3hotfix bossmaliwantakedown.42.bl3hotfix

cleandata:
	rm -f $(DATA)
data: $(DATA)


spawnoptions.takedown.json: extractspawnoptions.py takedown.json
	python3 extractspawnoptions.py --input takedown.json --output spawnoptions.takedown.json

spawnoptions.maliwan.json: extractspawnoptions.py maliwantakedown.json
	python3 extractspawnoptions.py     --input maliwantakedown.json --output spawnoptions.maliwan.json


bosstakedown.%.bl3hotfix: takedown.json bosstakedown.py spawnoptions.takedown.json
	python3 bosstakedown.py --in takedown.json --output bosstakedown.$*.bl3hotfix --spawnoptions  spawnoptions.takedown.json --seed $* --spawnout bosstakedown.$*.spawnoptions.json

bossmaliwantakedown.%.bl3hotfix: maliwantakedown.json bosstakedown.py spawnoptions.maliwan.json
	python3 bosstakedown.py --in maliwantakedown.json --output bossmaliwantakedown.$*.bl3hotfix --spawnoptions  spawnoptions.maliwan.json --seed $* --spawnout bossmaliwantakedown.$*.spawnoptions.json --path ${MALIWANPATH} --level ${MALIWANLEVEL}

bossmaliwantakedown.skrunt1.bl3hotfix: maliwantakedown.json bosstakedown.py skrunt/bossmaliwantakedown.skrunt1.spawnoptions.json
	python3 bosstakedown.py --overridespawn --in maliwantakedown.json --output bossmaliwantakedown.skrunt1.bl3hotfix --spawnoptions skrunt/bossmaliwantakedown.skrunt1.spawnoptions.json --seed ${SEED} --spawnout bossmaliwantakedown.skrunt1.spawnoptions.json --path ${MALIWANPATH} --level ${MALIWANLEVEL} --dontmodifyspawnpoints --dontmodifyspawnoptions

bosstakedown.skrunt1.bl3hotfix: takedown.json bosstakedown.py skrunt/bosstakedown.skrunt1.spawnoptions.json
	python3 bosstakedown.py --overridespawn --in takedown.json --output bosstakedown.skrunt1.bl3hotfix --spawnoptions skrunt/bosstakedown.skrunt1.spawnoptions.json --seed ${SEED} --spawnout bosstakedown.skrunt1.spawnoptions.json  --multiply 3 --title 'Boss Guardian Takedown: Modders Cut'

bosstakedown.skrunt2.bl3hotfix: takedown.json bosstakedown.py skrunt/bosstakedown.skrunt2.spawnoptions.json
	python3 bosstakedown.py --overridespawn --in takedown.json --output bosstakedown.skrunt2.bl3hotfix --spawnoptions skrunt/bosstakedown.skrunt2.spawnoptions.json --seed ${SEED} --spawnout bosstakedown.skrunt2.spawnoptions.json  --multiply 3 --title 'Boss Guardian Takedown: DLC3 Invasion'



skrunt1: bossmaliwantakedown.skrunt1.bl3hotfix bosstakedown.skrunt1.bl3hotfix
skrunt: bossmaliwantakedown.skrunt1.bl3hotfix bosstakedown.skrunt1.bl3hotfix bosstakedown.skrunt2.bl3hotfix
cleanskrunt:
	rm -f bossmaliwantakedown.skrunt1.bl3hotfix bosstakedown.skrunt1.bl3hotfix bosstakedown.skrunt2.bl3hotfix
