SEED=42
test:	extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/Maps/ProvingGrounds/Trial1/ProvingGrounds_Trial1_Dynamic.json

trial1.json: extracttrials.py
	python3 extracttrials.py --input ~/projects/bl3data/extracted_new/Game/Maps/ProvingGrounds/Trial1/ProvingGrounds_Trial1_Dynamic.json --output trial1.json

bosstrials.1.bl3hotfix: trial1.json bosstrials.py
	python3 bosstrials.py --in trial1.json --output bosstrials.1.bl3hotfix --trial 1 --seed 42

default: bosstrials.1.bl3hotfix trial1.json
