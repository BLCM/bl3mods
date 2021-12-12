#!/bin/bash
JWP=/home/hindle1/.local/bin/john-wick-parse
pushd ~/projects/bl3data/extracted_new/ > /dev/null && \
${JWP} serialize .$1 2> /dev/null > /dev/null && \
cat .$1.json
