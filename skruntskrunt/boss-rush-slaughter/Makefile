.PHONY: bk clean bpcharmod
MOD=boss_rush_3000.bl3hotfix
GEN=gen_boss_rush_3000.py
SEED=42
mod: $(MOD)

clean: 
	rm -f 3000_simple.bl3hotfix gen_bpchars.json boss_rush_3000-42.bl3hotfix gen_bpchars.42.json

$(MOD): boss.py $(GEN)
	python3 $(GEN)

bk:
	cp boss_rush_3000.bl3hotfix "boss_rush_3000.bl3hotfix.$(shell date --iso=seconds)"

gen_bpchars.json: bpchar-gen.py boss.py
	python3 bpchar-gen.py --seed $(SEED)

bpcharmod: gen_bpchars.json $(GEN)
	python3 $(GEN) --json gen_bpchars.json --seed $(SEED) | fgrep Deploying | sort | uniq -c

# Seed 42
boss_rush_3000-42.bl3hotfix:
	python3 bpchar-gen.py --json gen_bpchars.42.json --seed 42
	python3 $(GEN) --json gen_bpchars.42.json --seed 42 --output boss_rush_3000-42.bl3hotfix

# Pure random 
boss_rush_3000-rand.bl3hotfix:
	python3 bpchar-gen.py --json gen_bpchars.rand.json 
	python3 $(GEN) --json gen_bpchars.rand.json --output boss_rush_3000-rand.bl3hotfix

# Seed any number
boss_rush_3000.%.bl3hotfix:
	python3 bpchar-gen.py --json gen_bpchars.$*.json --seed $*
	python3 $(GEN) --json gen_bpchars.$*.json --seed $* --output boss_rush_3000.$*.bl3hotfix

%.crash: %
	mv $< $@
