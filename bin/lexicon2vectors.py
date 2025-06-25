#!/usr/bin/env python


# configure
#LEXICON = '/shared/reader-patron-library/ericleasemorgan/philosophers-works/etc/lexicon.txt'
#TOPN    = 128
HEADER  = [ 'source', 'target', 'weight' ]
LIBRARY = 'localLibrary'

# require
import rdr
import sys

# get input and make it operating sytem independent
if len( sys.argv ) !=3 : sys.exit( 'Usage: ' + sys.argv[ 0 ] + " <carrel> <topn>" )
carrel = sys.argv[ 1 ]
topn   = int( sys.argv[ 2 ] )

# initialize
library = rdr.configuration( LIBRARY )
lexicon = library/carrel/( rdr.ETC )/( rdr.LEXICON )
with open( lexicon ) as handle: lexicon = handle.read().splitlines()

# sanity check
rdr.checkForSemanticIndex( carrel, rdr.configuration( LIBRARY ) )

# start the output
print( '\t'.join( HEADER ) )

# process each word in the lexicon
for word in lexicon :

	# do the work and process each result
	try : results = rdr.word2vec( carrel, type='similarity', query=word, topn=topn ).splitlines()
	except AttributeError : continue
	
	for result in results :

		# parse and output
		( similarity, score ) = result.split( '\t' )
		print( '\t'.join( [ word, similarity, str( score ) ] ) )

# done
exit()
