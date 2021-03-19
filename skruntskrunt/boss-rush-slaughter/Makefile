.PHONY: bk clean bpcharmod
MOD=boss_rush_3000.bl3hotfix
GEN=gen_boss_rush_3000.py
mod: $(MOD)

clean: 
	rm -f 3000_simple.bl3hotfix gen_bpchars.json

$(MOD): boss.py $(GEN)
	python3 $(GEN)

bk:
	cp boss_rush_3000.bl3hotfix "boss_rush_3000.bl3hotfix.$(shell date --iso=seconds)"

gen_bpchars.json: bpchar-gen.py boss.py
	python3 bpchar-gen.py
	
bpcharmod: gen_bpchars.json $(GEN)
	python3 $(GEN) --json gen_bpchars.json | fgrep Deploying | sort | uniq -c

%.crash: %
	mv $< $@
