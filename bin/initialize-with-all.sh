#!/usr/bin/env bash

# initialize-with-all.sh - given a study carrel and depth, output a list of interesting words

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
SIZE=$2

# keywords
echo 'Keywords' >&2
KEYWORDS=$(rdr wrd $CARREL -c | head -n $SIZE | cut -f1)

# semantics
WORDS=$( echo $KEYWORDS | tr '\n' ' ' )
for WORD in $WORDS; do
	echo "Semantics ($WORD)" >&2
	SEMANTICS=$(echo -e "$SEMANTICS\n$WORD")
	SEMANTICS=$(echo -e "$SEMANTICS\n$(rdr semantics $CARREL -q $WORD -s $SIZE | cut -f1)" )
done

# nouns
echo 'Nouns' >&2
NOUNS=$(rdr pos $CARREL -c -s words -l N | head -n $SIZE | cut -f1)

# unigrams
echo 'Unigrams' >&2
UNIGRAMS=$(rdr ngrams $CARREL -c | head -n $SIZE | cut -f1)

LEXICON=$(rdr get)/$CARREL/$ETC/$LEXICON

# output and done
echo -e "$SEMANTICS\n$KEYWORDS\n$NOUNS\n$UNIGRAMS" | sort | uniq > $LEXICON
exit
