SEED=42
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

dist:	bosstrials.4.41.bl3hotfix bosstrials.4.42.bl3hotfix bosstrials.4.1.bl3hotfix bosstrials.5.42.bl3hotfix bosstrials.5.1.bl3hotfix bosstrials.8.42.bl3hotfix 
