#!/usr/bin/env python

# lexicon2variants.py - given a carrel, output variants of it's lexicon words

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# June 28, 2024 - first investigations
# July 11, 2024 - made more generic; works with just about any carrel


# configure
LIBRARY = 'localLibrary'
LEMMAS  = "select lemma, count(lemma) as c from pos where lower(token) is '##TOKEN##' group by lemma order by c desc;"
TOKENS  = "select token, count(token) as c from pos where lower(lemma) is '##LEMMA##' group by token order by c desc;"

# require
from sqlite3 import connect, Row
from pathlib import Path
from rdr     import configuration, ETC, DATABASE, LEXICON
from sys     import argv, exit, stderr

# get input
if len( argv ) != 2 : exit( 'Usage: ' + argv[ 0 ] + " <carrel>" )
carrel = argv[ 1 ]

# initialize
library            = Path( configuration( LIBRARY ) )
connection         = connect( library/carrel/ETC/DATABASE )
cursor             = connection.cursor()
cursor.row_factory = Row
with open( library/carrel/ETC/LEXICON ) as handle: lexicon = sorted( handle.read().splitlines() )

# process each word in the given lexicon; create a list of variants
variants = []
length   = str( len( lexicon ) )
for index, word in enumerate( lexicon ) :

	# debug
	stderr.write( 'Processing word #' + str( index + 1 ) + ' of ' + length + ' (' + word + ')              \r' )
	
	# update; a word is similar to itself
	variants.append ( word )
	
	# get and process each lemma
	cursor.execute( LEMMAS.replace( '##TOKEN##', word ) )
	lemmas = cursor.fetchall()
	for lemma in lemmas :
		
		# re-initialize and update
		lemma = lemma[ 'lemma' ]
		variants.append( lemma )
		
		# get and process each word associated with the given lemma
		cursor.execute( TOKENS.replace( '##LEMMA##', lemma ) )
		tokens = cursor.fetchall()
		for token in tokens : variants.append( token[ 'token' ] )

# normalize, output, and done
variants = sorted( list( set( variants ) ) )
print()
[ print( variant ) for variant in variants ]
exit()


