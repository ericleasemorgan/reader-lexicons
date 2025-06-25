#!/usr/bin/env bash

# lexicon2related.sh - a front-end to lexicon2related.py


# configure
LEXICON2RELATED='./bin/lexicon2related.py'
ETC='etc'
LEXICON='lexicon.txt'

# get input
if [[ -z $1 ]]; then
	echo "Usage: $0 <carrel> <threshold>" >&2
	exit
fi
CARREL=$1
THRESHOLD=$2

# initialize, submit the work, and done
LEXICON=$(rdr get)/$CARREL/$ETC/$LEXICON
$LEXICON2RELATED $CARREL $THRESHOLD | sponge $LEXICON
exit
