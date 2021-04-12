#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

# Script to update our main translation template, and then update
# each translation's copy of it

echo "Updating master translation template..."
pygettext.py -d base -o locales/base.pot gen_red_text_explainer.py
echo

for pofile in locales/*/LC_MESSAGES/base.po
do
    echo "Merging changes to ${pofile}"
    echo "================================================="
    msgmerge -U --backup=none --no-wrap "${pofile}" locales/base.pot
    echo
done

echo "Done!"
echo

