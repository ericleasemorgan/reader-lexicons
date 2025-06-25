#!/usr/bin/env bash

# initialize-with-semantics.sh - given a study carrel, a word, and a depth, output a list of semantically simlar words

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributred under a GNU Public License

# May  18, 2025 - Graduation Day; "I've graduated!"
# May  21, 2025 - redirected output to the lexicon file
# June 25, 2025 - on the train to French lesson is Philadelphia


# configure
ETC='etc'
LEXICON='lexicon.txt'

# get input
if [[ -z $1 || -z $2  || -z $3 ]]; then
	echo "Usage: $0 <carrel> <word> <depth>" >&2
	exit
fi
CARREL=$1
WORD=$2
DEPTH=$3

# initialize
LEXICON=$(rdr get)/$CARREL/$ETC/$LEXICON

# nouns
WORDS="$WORD\n"$(rdr semantics $CARREL -q $WORD -s $DEPTH | cut -f1)

# output and done
#RESULTS=$( echo "$NOUNS" | sort | sed "s/$/;/" | tr '\n' ' ' )
#echo "Nouns: $RESULTS" >&2
echo -e "$WORDS" | uniq > $LEXICON
exit
