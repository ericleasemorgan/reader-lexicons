#!/usr/bin/env python

# lexicon2related.py - given a carrel, output its lexicon's semantically related words

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# July 11, 2024 - first investigations
# July 12, 2024 - added support for threshold values of int or float; kinda cool


# configure
LIBRARY = 'localLibrary'
TOPN    = 2

# require
from pathlib import Path
from rdr     import configuration, ETC, DATABASE, LEXICON, word2vec
from sys     import argv, exit, stderr

# get input
if len( argv ) != 3 : exit( 'Usage: ' + argv[ 0 ] + " <carrel> <threshold>" )
carrel    = argv[ 1 ]
threshold = argv[ 2 ]

# initialize
library = Path( configuration( LIBRARY ) )
with open( library/carrel/ETC/LEXICON ) as handle : lexicon = sorted( handle.read().splitlines() )

# process each item in the lexicon; create a list of related words
related = []
for word in lexicon :

	# normalize, just in case
	word = word.strip()

	# a word is related to itself
	related.append( word )
	
	# sanity check; only process single words
	if len( word.split() ) > 1 : continue
	
	# get a set of related words
	relations = word2vec( carrel, query=word, topn=TOPN )
	
	# try to parse the result; trap for bogus rdr error
	try : relations = relations.splitlines()
	except AttributeError : continue
	
	# branch accordingly; check for digit
	if threshold.isdigit() : 
	
		# process each relation
		for index, relation in enumerate( relations ) :
		
			# parse and update
			word, score = relation.split( '\t' )
			related.append( word )
			
			# break, conditionally
			if index >= int( threshold ) : break
			
	# otherwise
	else :
	
		# more sanity checking
		if threshold.replace( '.', '', 1 ).isdigit() == False : exit( 'Error: Invalid value for threshold.' )
		
		# process each relation
		for relation in relations :
		
			# parse, and conditionally update
			word, score = relation.split( '\t' )
			if float( score ) >= float( threshold ) : related.append( word )
			else : break
	
# normalize, output, and done
related = sorted( list( set( related ) ) )
[ print( word ) for word in related ]
exit()
