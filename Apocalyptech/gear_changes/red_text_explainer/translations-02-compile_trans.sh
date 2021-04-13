#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

# Script to compile translations.  We could have this take an
# arg and just do one, but we may as well just do all of 'em.

for transdir in locales/??
do
    echo "Processing ${transdir}"
    echo "====================="

    msgfmt "${transdir}/LC_MESSAGES/base.po" -o "${transdir}/LC_MESSAGES/base.mo"
done

echo
echo "Done!"
echo

