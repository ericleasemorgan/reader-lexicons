#!/usr/bin/env bash

# initialize-with-nouns.sh - given a study carrel and depth, output a list of interesting words

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributred under a GNU Public License

# May 18, 2025 - Graduation Day; "I've graduated!"
# May 21, 2025 - redirected output to the lexicon file


# configure
ETC='etc'
LEXICON='lexicon.txt'

# get input
if [[ -z $1 || -z $2 ]]; then
	echo "Usage: $0 <carrel> <depth>" >&2
	exit
fi
CARREL=$1
DEPTH=$2

# initialize
LEXICON=$(rdr get)/$CARREL/$ETC/$LEXICON

# nouns
NOUNS=$(rdr pos $CARREL -c -s words -l N | head -n $DEPTH | cut -f1)

# output and done
RESULTS=$( echo "$NOUNS" | sort | sed "s/$/;/" | tr '\n' ' ' )
echo "Nouns: $RESULTS" >&2
echo -e "$NOUNS" | sort | uniq > $LEXICON
exit
