default: murdertime

doublemurdertime.bl3hotfix: murdertime.py doublemurdertime.csv
	python3 murdertime.py --csv doublemurdertime.csv --output doublemurdertime.bl3hotfix

fastmurdertime.bl3hotfix: murdertime.py fastmurdertime.csv
	python3 murdertime.py --csv fastmurdertime.csv --output fastmurdertime.bl3hotfix

growmurdertime.bl3hotfix: murdertime.py growmurdertime.csv
	python3 murdertime.py --csv growmurdertime.csv --output growmurdertime.bl3hotfix

murdertime: growmurdertime.bl3hotfix fastmurdertime.bl3hotfix doublemurdertime.bl3hotfix

