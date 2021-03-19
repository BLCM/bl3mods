.PHONY: bk clean bpcharmod

mod: 3000_simple.bl3hotfix

clean: 
	rm -f 3000_simple.bl3hotfix gen_bpchars.json

3000_simple.bl3hotfix: boss.py simple_gen_3000_hyperion_slaughter.py
	python3 simple_gen_3000_hyperion_slaughter.py

bk:
	cp 3000_simple.bl3hotfix "3000_simple.bl3hotfix.$(shell date --iso=seconds)"

gen_bpchars.json: bpchar-gen.py
	python3 bpchar-gen.py
	
bpcharmod: gen_bpchars.json
	python3 simple_gen_3000_hyperion_slaughter.py --json gen_bpchars.json | fgrep Deploying | sort | uniq -c


%.crash: %
	mv $< $@
