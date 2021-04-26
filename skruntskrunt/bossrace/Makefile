MOD=bossrace.bl3hotfix
EXE=ixoraspawners.py
SEED ?= 42
DISTFILES=$(MOD) bossrace.rand.bl3hotfix \
	seeds/bossrace.1.bl3hotfix.txt \
	seeds/bossrace.2.bl3hotfix.txt \
	seeds/bossrace.3.bl3hotfix.txt \
	seeds/bossrace.4.bl3hotfix.txt \
	seeds/bossrace.5.bl3hotfix.txt \
	seeds/bossrace.6.bl3hotfix.txt \
	seeds/bossrace.7.bl3hotfix.txt \
	seeds/bossrace.8.bl3hotfix.txt \
	seeds/bossrace.9.bl3hotfix.txt \
	seeds/bossrace.10.bl3hotfix.txt \
	seeds/bossrace.11.bl3hotfix.txt \
	seeds/bossrace.12.bl3hotfix.txt \
	seeds/bossrace.13.bl3hotfix.txt \
	seeds/bossrace.14.bl3hotfix.txt \
	seeds/bossrace.15.bl3hotfix.txt \
	seeds/bossrace.16.bl3hotfix.txt \
	seeds/bossrace.17.bl3hotfix.txt \
	seeds/bossrace.18.bl3hotfix.txt \
	seeds/bossrace.19.bl3hotfix.txt \
	seeds/bossrace.20.bl3hotfix.txt \
	seeds/bossrace.21.bl3hotfix.txt \
	seeds/bossrace.22.bl3hotfix.txt \
	seeds/bossrace.23.bl3hotfix.txt \
	seeds/bossrace.24.bl3hotfix.txt \
	seeds/bossrace.25.bl3hotfix.txt \
	seeds/bossrace.26.bl3hotfix.txt \
	seeds/bossrace.27.bl3hotfix.txt \
	seeds/bossrace.28.bl3hotfix.txt \
	seeds/bossrace.29.bl3hotfix.txt \
	seeds/bossrace.30.bl3hotfix.txt \
	seeds/bossrace.31.bl3hotfix.txt \
	seeds/bossrace.32.bl3hotfix.txt \
	seeds/bossrace.33.bl3hotfix.txt \
	seeds/bossrace.34.bl3hotfix.txt \
	seeds/bossrace.35.bl3hotfix.txt \
	seeds/bossrace.36.bl3hotfix.txt \
	seeds/bossrace.37.bl3hotfix.txt \
	seeds/bossrace.38.bl3hotfix.txt \
	seeds/bossrace.39.bl3hotfix.txt \
	seeds/bossrace.40.bl3hotfix.txt \
	seeds/bossrace.41.bl3hotfix.txt \
	seeds/bossrace.42.bl3hotfix.txt \
# 	seeds/bossrace.43.bl3hotfix.txt \
# 	seeds/bossrace.44.bl3hotfix.txt \
# 	seeds/bossrace.45.bl3hotfix.txt \
# 	seeds/bossrace.46.bl3hotfix.txt \
# 	seeds/bossrace.47.bl3hotfix.txt \
# 	seeds/bossrace.48.bl3hotfix.txt \
# 	seeds/bossrace.49.bl3hotfix.txt \
# 	seeds/bossrace.50.bl3hotfix.txt \
# 	seeds/bossrace.51.bl3hotfix.txt \
# 	seeds/bossrace.52.bl3hotfix.txt \
# 	seeds/bossrace.53.bl3hotfix.txt \
# 	seeds/bossrace.54.bl3hotfix.txt \
# 	seeds/bossrace.55.bl3hotfix.txt \
# 	seeds/bossrace.56.bl3hotfix.txt \
# 	seeds/bossrace.57.bl3hotfix.txt \
# 	seeds/bossrace.58.bl3hotfix.txt \
# 	seeds/bossrace.59.bl3hotfix.txt \
# 	seeds/bossrace.60.bl3hotfix.txt \
# 	seeds/bossrace.61.bl3hotfix.txt \
# 	seeds/bossrace.62.bl3hotfix.txt \
# 	seeds/bossrace.63.bl3hotfix.txt \
# 	seeds/bossrace.64.bl3hotfix.txt \
# 	seeds/bossrace.65.bl3hotfix.txt \
# 	seeds/bossrace.66.bl3hotfix.txt \
# 	seeds/bossrace.67.bl3hotfix.txt \
# 	seeds/bossrace.68.bl3hotfix.txt \
# 	seeds/bossrace.69.bl3hotfix.txt \
# 	seeds/bossrace.70.bl3hotfix.txt \
# 	seeds/bossrace.71.bl3hotfix.txt \
# 	seeds/bossrace.72.bl3hotfix.txt \
# 	seeds/bossrace.73.bl3hotfix.txt \
# 	seeds/bossrace.74.bl3hotfix.txt \
# 	seeds/bossrace.75.bl3hotfix.txt \
# 	seeds/bossrace.76.bl3hotfix.txt \
# 	seeds/bossrace.77.bl3hotfix.txt \
# 	seeds/bossrace.78.bl3hotfix.txt \
# 	seeds/bossrace.79.bl3hotfix.txt \
# 	seeds/bossrace.80.bl3hotfix.txt \
# 	seeds/bossrace.81.bl3hotfix.txt \
# 	seeds/bossrace.82.bl3hotfix.txt \
# 	seeds/bossrace.83.bl3hotfix.txt \
# 	seeds/bossrace.84.bl3hotfix.txt \
# 	seeds/bossrace.85.bl3hotfix.txt \
# 	seeds/bossrace.86.bl3hotfix.txt \
# 	seeds/bossrace.87.bl3hotfix.txt \
# 	seeds/bossrace.88.bl3hotfix.txt \
# 	seeds/bossrace.89.bl3hotfix.txt \
# 	seeds/bossrace.90.bl3hotfix.txt \
# 	seeds/bossrace.91.bl3hotfix.txt \
# 	seeds/bossrace.92.bl3hotfix.txt \
# 	seeds/bossrace.93.bl3hotfix.txt \
# 	seeds/bossrace.94.bl3hotfix.txt \
# 	seeds/bossrace.95.bl3hotfix.txt \
# 	seeds/bossrace.96.bl3hotfix.txt \
# 	seeds/bossrace.97.bl3hotfix.txt \
# 	seeds/bossrace.98.bl3hotfix.txt \
# 	seeds/bossrace.99.bl3hotfix.txt \
# 	seeds/bossrace.100.bl3hotfix.txt 

seeds:
	mkdir seeds

default: mod

mod: $(MOD)

$(MOD): $(EXE)
	python3 $(EXE) --seed $(SEED)
clean:
	rm -f bossrace.bl3hotfix
	rm -f $(DISTFILES)

bossrace.rand.bl3hotfix: $(EXE)
	python3 $(EXE) --output bossrace.rand.bl3hotfix

bossrace.%.bl3hotfix: $(EXE)
	python3 $(EXE) --seed $* --output bossrace.$*.bl3hotfix

bossrace.%.bl3hotfix.txt: bossrace.%.bl3hotfix
	mv $< $@

seeds/bossrace.%.bl3hotfix.txt: bossrace.%.bl3hotfix.txt
	mv $< $@

dist: seeds $(DISTFILES) 

gen:
	rm -f $(MOD)
	make $(MOD)
