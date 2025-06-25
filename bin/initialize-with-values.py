#!/usr/bin/env python

# initialize-with-values.py - find human values in a corpus and output the result to a files

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# February 22, 2024 - first cut; a long time coming
# June     23, 2025 - migrating to reader-sentences


# configure
MODEL           = './etc/models/human-values'
LIBRARY         = 'localLibrary'
SENTENCES       = 'sentences.db'
SELECTSENTENCES = "SELECT sentence FROM sentences"

# require
from spacy   import load
from rdr     import TXT, configuration, ETC, LEXICON
from sys     import argv, exit, stderr
from sqlite3 import connect

# migrate the results of sql queries into a generator; smart!?
def select2generator( connection, sql ) :

	# query the given connection
	results = connection.execute( sql ).fetchall()
	
	# yield each result; ought to be very memory efficient
	for result in connection.execute( sql ).fetchall(): yield( result[ 0 ] )

# get input
if len( argv ) != 2 : exit( 'Usage: ' + argv[ 0 ] + " <carrel>" )
carrel = argv[ 1 ]

# initialize
library = configuration( LIBRARY )
nlp     = load( MODEL )
	
# get all sentences; might not be scalable
sentences = select2generator( connect( library/carrel/ETC/SENTENCES ), SELECTSENTENCES )

# process each sentence; create a list of probable human values
values = []
for sentence in sentences :
	
	# try to model the sentence
	try : doc = nlp( sentence )
	except ValueError : 
		stderr.write( "Empty sentence error. Call Eric.\n" )
		continue
		
	# output
	for entity in doc.ents : values.append( entity.text.lower() )

# normalize and open the output
values = sorted( list( set( values ) ) )
with open( library/carrel/ETC/LEXICON, 'w' ) as handle :
	
	# output
	for value in values : handle.write( value + '\n' )
        
# done
exit()
