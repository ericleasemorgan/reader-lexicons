#!/usr/bin/env bash

# edit.sh - given a carrel, open lexicon.txt for editing

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# June 24, 2025 - first cut


# configure
ETC='etc'
LEXICON='lexicon.txt'

if [[ -z $1 ]]; then
	echo "Usage: $0 <carrel>" >&2
	exit
fi
CARREL=$1

LEXICON="$(rdr get)/$CARREL/$ETC/$LEXICON"

$EDITOR $LEXICON
