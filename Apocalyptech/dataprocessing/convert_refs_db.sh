#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

read -sp 'Enter bl3refs pass: ' FULLPASS
read -sp 'Enter bl3refs_ro pass: ' PASS
echo
echo "Dumping SQL first..."
echo
rm bl3refs.zip
mysqldump -u bl3refs -p${FULLPASS} -h mcp bl3refs > bl3refs.sql
zip bl3refs.zip bl3refs.sql
rm bl3refs.sql
echo
echo "Now doing SQLite dump/conversion..."
echo
rm bl3refs.sqlite3*
/usr/local/dv/virtualenv/mysql2sqlite/bin/mysql2sqlite -f bl3refs.sqlite3 -d bl3refs -u bl3refs_ro -h mcp -V -p ${PASS} && zip bl3refs.sqlite3.zip bl3refs.sqlite3 && ls -lh bl3refs.sqlite3*
ls -lh bl3refs.zip
