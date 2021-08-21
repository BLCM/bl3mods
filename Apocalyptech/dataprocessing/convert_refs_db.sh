#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

read -sp 'Enter bl3refs_ro pass: ' PASS
rm bl3refs.sqlite3*
/usr/local/dv/virtualenv/mysql2sqlite/bin/mysql2sqlite -f bl3refs.sqlite3 -d bl3refs -u bl3refs_ro -h mcp -V -p ${PASS} && zip bl3refs.sqlite3.zip bl3refs.sqlite3 && ls -lh bl3refs.sqlite3*

