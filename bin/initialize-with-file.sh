#!/usr/bin/env bash

# initialize-lexicon.sh - given a carrel and a file, create a lexicon

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 21, 2025 - first investigations


# configure
ETC='etc'
LEXICON='lexicon.txt'

# get input
if [[ -z $1 || -z $2 ]]; then
	echo "Usage: $0 <carrel> <file>" >&2
	exit
fi
CARREL=$1
SOURCE=$2

# do the work and done; simple
cp $SOURCE "$(rdr get)/$CARREL/$ETC/$LEXICON"
exit