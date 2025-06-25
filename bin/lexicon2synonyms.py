#!/usr/bin/env python

# lexicon2synonyms.py - given a carrel, output synonyms of the carrel's lexicon

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# July 11, 2024 - first real cut


# configure
LIBRARY = 'localLibrary'

# require
from nltk.corpus import wordnet
from pathlib     import Path
from rdr         import configuration, ETC, DATABASE, LEXICON
from sys         import argv, exit, stderr

# get input
if len( argv ) != 2 : exit( 'Usage: ' + argv[ 0 ] + " <carrel>" )
carrel = argv[ 1 ]

# initialize
library = Path( configuration( LIBRARY ) )
with open( library/carrel/ETC/LEXICON ) as handle : lexicon = handle.read().splitlines()

# process each item in the lexicon; create a list of synonyms
synonyms = []
for word in lexicon :

	# a word is synonymous with itself; kinda like math
	synonyms.append( word )
		
	# process each synset
	for synset in wordnet.synsets( word ) :
	
		# do the work
		for lemma in synset.lemmas() : synonyms.append( lemma.name() )
			
# normalize and output; very very pythonic
synonyms = sorted( list( set( synonyms ) ) )
synonyms = [ synonym.replace( '_', ' ' ) for synonym in synonyms ]
[ print( synonym ) for synonym in synonyms ]

# done
exit()