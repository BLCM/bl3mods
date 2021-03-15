.PHONY: bk clean

mod: 3000_simple.bl3hotfix

clean: 
	rm -f 3000_simple.bl3hotfix

3000_simple.bl3hotfix: boss.py simple_gen_3000_hyperion_slaughter.py
	python3 simple_gen_3000_hyperion_slaughter.py

bk:
	cp 3000_simple.bl3hotfix "3000_simple.bl3hotfix.$(shell date --iso=seconds)"

%.crash: %
	mv $< $@
