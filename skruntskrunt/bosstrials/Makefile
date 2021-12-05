SEED=19
test:	extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/Maps/ProvingGrounds/Trial1/ProvingGrounds_Trial1_Dynamic.json

trial1.json: extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/Maps/ProvingGrounds/Trial1/ProvingGrounds_Trial1_Dynamic.json --output trial1.json

trial4.json: extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/Maps/ProvingGrounds/Trial4/ProvingGrounds_Trial4_Dynamic.json --output trial4.json

trial5.json: extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/Maps/ProvingGrounds/Trial5/ProvingGrounds_Trial5_Dynamic.json --output trial5.json

trial6.json: extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/Maps/ProvingGrounds/Trial6/ProvingGrounds_Trial6_Dynamic.json --output trial6.json

trial7.json: extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/Maps/ProvingGrounds/Trial7/ProvingGrounds_Trial7_Dynamic.json --output trial7.json

trial8.json: extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/Maps/ProvingGrounds/Trial8/ProvingGrounds_Trial8_Dynamic.json --output trial8.json

bosstrials.1.debug.bl3hotfix: trial1.json bosstrials.py spawnoptions.1.debug.json
	python3 bosstrials.py --in trial1.json --output bosstrials.1.debug.bl3hotfix --spawnoptions  spawnoptions.1.debug.json --trial 1 --seed $(SEED)

bosstrials.7.debug.bl3hotfix: trial7.json bosstrials.py spawnoptions.7.debug.json
	python3 bosstrials.py --in trial7.json --output bosstrials.7.debug.bl3hotfix --spawnoptions  spawnoptions.7.debug.json --trial 7 --seed $(SEED)

bosstrials.6.debug.bl3hotfix: trial6.json bosstrials.py spawnoptions.6.debug.json
	python3 bosstrials.py --in trial6.json --output bosstrials.6.debug.bl3hotfix --spawnoptions  spawnoptions.6.debug.json --trial 6 --seed $(SEED)

bosstrials.1.bl3hotfix: trial1.json bosstrials.py spawnoptions.1.json
	python3 bosstrials.py --in trial1.json --output bosstrials.1.bl3hotfix --spawnoptions  spawnoptions.1.json --trial 1 --seed $(SEED)

bosstrials.4.bl3hotfix: trial4.json bosstrials.py spawnoptions.4.json
	python3 bosstrials.py --in trial4.json --output bosstrials.4.bl3hotfix --spawnoptions  spawnoptions.4.json --trial 4 --seed $(SEED)
bosstrials.5.bl3hotfix: trial5.json bosstrials.py spawnoptions.5.json
	python3 bosstrials.py --in trial5.json --output bosstrials.5.bl3hotfix --spawnoptions  spawnoptions.5.json --trial 5 --seed $(SEED)
bosstrials.6.bl3hotfix: trial6.json bosstrials.py spawnoptions.6.json
	python3 bosstrials.py --in trial6.json --output bosstrials.6.bl3hotfix --spawnoptions  spawnoptions.6.json --trial 6 --seed $(SEED)
bosstrials.7.bl3hotfix: trial7.json bosstrials.py spawnoptions.7.json
	python3 bosstrials.py --in trial7.json --output bosstrials.7.bl3hotfix --spawnoptions  spawnoptions.7.json --trial 7 --seed $(SEED)
bosstrials.8.bl3hotfix: trial8.json bosstrials.py spawnoptions.8.json
	python3 bosstrials.py --in trial8.json --output bosstrials.8.bl3hotfix --spawnoptions  spawnoptions.8.json --trial 8 --seed $(SEED)

bosstrials.survival.bl3hotfix: trial1.json bosstrials.py
	python3 bosstrials.py --in trial1.json --output bosstrials.1.bl3hotfix --trial 1 --seed $(SEED)

default: bosstrials.1.bl3hotfix bosstrials.4.bl3hotfix bosstrials.5.bl3hotfix bosstrials.6.bl3hotfix bosstrials.7.bl3hotfix bosstrials.8.bl3hotfix
clean:
	rm -f bosstrials.1.bl3hotfix bosstrials.4.bl3hotfix bosstrials.5.bl3hotfix bosstrials.6.bl3hotfix bosstrials.7.bl3hotfix bosstrials.8.bl3hotfix


spawnoptions.1.json: extractspawnoptions.py trial1.json
	python3 extractspawnoptions.py --input trial1.json --output spawnoptions.1.json
spawnoptions.4.json: extractspawnoptions.py trial4.json
	python3 extractspawnoptions.py --input trial4.json --output spawnoptions.4.json
spawnoptions.5.json: extractspawnoptions.py trial5.json
	python3 extractspawnoptions.py --input trial5.json --output spawnoptions.5.json
spawnoptions.6.json: extractspawnoptions.py trial6.json
	python3 extractspawnoptions.py --input trial6.json --output spawnoptions.6.json
spawnoptions.7.json: extractspawnoptions.py trial7.json
	python3 extractspawnoptions.py --input trial7.json --output spawnoptions.7.json
spawnoptions.8.json: extractspawnoptions.py trial8.json
	python3 extractspawnoptions.py --input trial8.json --output spawnoptions.8.json

# these are working seeds as of 0.1.0
bosstrials.4.41.bl3hotfix: trial4.json bosstrials.py spawnoptions.4.json
	python3 bosstrials.py --in trial4.json --output bosstrials.4.41.bl3hotfix --spawnoptions  spawnoptions.4.json --trial 4 --seed 41
bosstrials.4.42.bl3hotfix: trial4.json bosstrials.py spawnoptions.4.json
	python3 bosstrials.py --in trial4.json --output bosstrials.4.42.bl3hotfix --spawnoptions  spawnoptions.4.json --trial 4 --seed 42
bosstrials.4.1.bl3hotfix: trial4.json bosstrials.py spawnoptions.4.json
	python3 bosstrials.py --in trial4.json --output bosstrials.4.1.bl3hotfix --spawnoptions  spawnoptions.4.json --trial 4 --seed 1
bosstrials.5.42.bl3hotfix: trial5.json bosstrials.py spawnoptions.5.json
	python3 bosstrials.py --in trial5.json --output bosstrials.5.42.bl3hotfix --spawnoptions  spawnoptions.5.json --trial 5 --seed 42
bosstrials.5.1.bl3hotfix: trial5.json bosstrials.py spawnoptions.5.json
	python3 bosstrials.py --in trial5.json --output bosstrials.5.1.bl3hotfix --spawnoptions  spawnoptions.5.json --trial 5 --seed 1
bosstrials.8.42.bl3hotfix: trial8.json bosstrials.py spawnoptions.8.json
	python3 bosstrials.py --in trial8.json --output bosstrials.8.42.bl3hotfix --spawnoptions  spawnoptions.8.json --trial 8 --seed 42

MIX1 =	bosstrials.1.16.bl3hotfix \
	bosstrials.4.13.bl3hotfix \
	bosstrials.5.16.bl3hotfix \
	bosstrials.6.18.bl3hotfix \
	bosstrials.7.19.bl3hotfix \
	bosstrials.8.15.bl3hotfix

# 5 - 24 doesn't work
# 1 - 21 doesn't work
#     27 doesn't work
#     89 doesn't work
#     90 doesn't work
#     91 
# 8 - 26 too hard
# 7 - 25 annointed alpha
# 8 - 21 annointed alpha
# 4 - 22 is annointed alpha
MIX2 =	bosstrials.1.91.bl3hotfix \
	bosstrials.4.22.bl3hotfix \
	bosstrials.5.25.bl3hotfix \
	bosstrials.6.24.bl3hotfix \
	bosstrials.7.67.bl3hotfix \
	bosstrials.8.58.bl3hotfix

# 1 - 220 wrong (221 works)
# 4 - 393 kinda too much
# Fervor too hard
MIX3 =	bosstrials.1.221.bl3hotfix \
	bosstrials.4.394.bl3hotfix \
	bosstrials.5.415.bl3hotfix \
	bosstrials.6.664.bl3hotfix \
	bosstrials.7.850.bl3hotfix \
	bosstrials.8.913.bl3hotfix

SKRUNT1=bosstrials.skrunt1.1.bl3hotfix \
	bosstrials.skrunt1.4.bl3hotfix \
	bosstrials.skrunt1.5.bl3hotfix \
	bosstrials.skrunt1.6.bl3hotfix \
	bosstrials.skrunt1.7.bl3hotfix \
	bosstrials.skrunt1.8.bl3hotfix

# 749 doesn't work for 1
MIX4 =	bosstrials.1.750.bl3hotfix \
	bosstrials.4.734.bl3hotfix \
	bosstrials.5.649.bl3hotfix \
	bosstrials.6.913.bl3hotfix \
	bosstrials.7.453.bl3hotfix \
	bosstrials.8.489.bl3hotfix

bosstrials.skrunt1.%.bl3hotfix: bosstrials.py skrunt1/bosstrials.*.spawnoptions.json
	python3 bosstrials.py --in trial$*.json --output bosstrials.skrunt1.$*.bl3hotfix --spawnoptions skrunt1/bosstrials.$*.spawnoptions.json --trial $* --seed 42 --overridespawn 


# This is the currated mix
bosstrials.bl3hotfix: bosstrials.bl3hotfix.header $(MIX1)
	cat $^ > $@

bosstrials.vol2.bl3hotfix: bosstrials.vol2.bl3hotfix.header $(MIX2)
	cat $^ > $@

bosstrials.vol3.bl3hotfix: bosstrials.vol3.bl3hotfix.header $(MIX3)
	cat $^ > $@

bosstrials.vol4.bl3hotfix: bosstrials.vol4.bl3hotfix.header $(MIX4)
	cat $^ > $@

bosstrials.skrunt1.bl3hotfix: bosstrials.skrunt1.bl3hotfix.header $(SKRUNT1)
	cat $^ > $@


bosstrials.1.%.bl3hotfix: trial1.json bosstrials.py spawnoptions.1.json
	python3 bosstrials.py --in trial1.json --output bosstrials.1.$*.bl3hotfix --spawnoptions  spawnoptions.1.json --trial 1 --seed $* --spawnout bosstrials.1.$*.spawnoptions.json
bosstrials.4.%.bl3hotfix: trial4.json bosstrials.py spawnoptions.4.json
	python3 bosstrials.py --in trial4.json --output bosstrials.4.$*.bl3hotfix --spawnoptions  spawnoptions.4.json --trial 4 --seed $* --spawnout bosstrials.4.$*.spawnoptions.json
bosstrials.5.%.bl3hotfix: trial5.json bosstrials.py spawnoptions.5.json
	python3 bosstrials.py --in trial5.json --output bosstrials.5.$*.bl3hotfix --spawnoptions  spawnoptions.5.json --trial 5 --seed $* --spawnout bosstrials.5.$*.spawnoptions.json
bosstrials.6.%.bl3hotfix: trial6.json bosstrials.py spawnoptions.6.json
	python3 bosstrials.py --in trial6.json --output bosstrials.6.$*.bl3hotfix --spawnoptions  spawnoptions.6.json --trial 6 --seed $* --spawnout bosstrials.6.$*.spawnoptions.json
bosstrials.7.%.bl3hotfix: trial7.json bosstrials.py spawnoptions.7.json
	python3 bosstrials.py --in trial7.json --output bosstrials.7.$*.bl3hotfix --spawnoptions  spawnoptions.7.json --trial 7 --seed $* --spawnout bosstrials.7.$*.spawnoptions.json
bosstrials.8.%.bl3hotfix: trial8.json bosstrials.py spawnoptions.8.json
	python3 bosstrials.py --in trial8.json --output bosstrials.8.$*.bl3hotfix --spawnoptions  spawnoptions.8.json --trial 8 --seed $* --spawnout bosstrials.8.$*.spawnoptions.json

bosstrials-override.1.bl3hotfix: trial1.json bosstrials.py spawnoptions.1.json spawnoptions.1.override.json
	python3 bosstrials.py --in trial1.json --output bosstrials-override.1.bl3hotfix --spawnoptions  spawnoptions.1.override.json --trial 1 --overridespawn --seed 42 --spawnout bosstrials-override.1.spawnoptions.json



# bosstrials.4.42.bl3hotfix: trial4.json bosstrials.py spawnoptions.4.json
# 	python3 bosstrials.py --in trial4.json --output bosstrials.4.42.bl3hotfix --spawnoptions  spawnoptions.4.json --trial 4 --seed 42
# bosstrials.4.1.bl3hotfix: trial4.json bosstrials.py spawnoptions.4.json
# 	python3 bosstrials.py --in trial4.json --output bosstrials.4.1.bl3hotfix --spawnoptions  spawnoptions.4.json --trial 4 --seed 1
# bosstrials.5.42.bl3hotfix: trial5.json bosstrials.py spawnoptions.5.json
# 	python3 bosstrials.py --in trial5.json --output bosstrials.5.42.bl3hotfix --spawnoptions  spawnoptions.5.json --trial 5 --seed 42
# bosstrials.5.1.bl3hotfix: trial5.json bosstrials.py spawnoptions.5.json
# 	python3 bosstrials.py --in trial5.json --output bosstrials.5.1.bl3hotfix --spawnoptions  spawnoptions.5.json --trial 5 --seed 1
# bosstrials.8.42.bl3hotfix: trial8.json bosstrials.py spawnoptions.8.json
# 	python3 bosstrials.py --in trial8.json --output bosstrials.8.42.bl3hotfix --spawnoptions  spawnoptions.8.json --trial 8 --seed 42



dist:	bosstrials.4.41.bl3hotfix bosstrials.4.42.bl3hotfix bosstrials.4.1.bl3hotfix bosstrials.5.42.bl3hotfix bosstrials.5.1.bl3hotfix bosstrials.8.42.bl3hotfix bosstrials.bl3hotfix

