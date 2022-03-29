#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

read -sp 'Enter wlrefs pass: ' FULLPASS
read -sp 'Enter wlrefs_ro pass: ' PASS
echo
echo "Dumping SQL first..."
echo
rm wlrefs.zip
mysqldump -u wlrefs -p${FULLPASS} -h mcp wlrefs > wlrefs.sql
zip wlrefs.zip wlrefs.sql
rm wlrefs.sql
echo
echo "Now doing SQLite dump/conversion..."
echo
rm wlrefs.sqlite3*
/usr/local/dv/virtualenv/mysql2sqlite/bin/mysql2sqlite -f wlrefs.sqlite3 -d wlrefs -u wlrefs_ro -h mcp -V -p ${PASS} && zip wlrefs.sqlite3.zip wlrefs.sqlite3 && ls -lh wlrefs.sqlite3*
ls -lh wlrefs.zip
