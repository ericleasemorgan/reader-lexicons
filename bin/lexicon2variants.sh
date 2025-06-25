#!/usr/bin/env bash

# lexicon2variants.sh - a front-end to lexicon2variants.py


# configure
LEXICON2VARIANTS='./bin/lexicon2variants.py'
ETC='etc'
LEXICON='lexicon.txt'

# get input
if [[ -z $1 ]]; then
	echo "Usage: $0 <carrel>" >&2
	exit
fi
CARREL=$1

# initialize, submit the work, and done
LEXICON=$(rdr get)/$CARREL/$ETC/$LEXICON
$LEXICON2VARIANTS $CARREL | sponge $LEXICON
exit
