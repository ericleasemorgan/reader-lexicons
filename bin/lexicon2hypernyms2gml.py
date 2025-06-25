#!/usr/bin/env python

# lexicon2hypernyms2gml.py - given a lexicon, output a network graph (GML file) of nouns and their hypernyms

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public license

# May      16, 2022 - first documentation; while in the Culver Public Library
# November  1, 2023 - worked on outputting as graph
# May      18, 2025 - added command-line input; Graduation Day!


# configure
MINIMUM   = 0 
STOPWORDS = [ 'entity' ]
LEXICON   = 'lexicon.txt'
LIBRARY   = 'localLibrary'

# require
from nltk.corpus import wordnet as wn
from networkx    import DiGraph, write_gml
from sys         import argv, exit, stdout
from rdr         import configuration, ETC

# get input
if len( argv ) != 2 : exit( 'Usage: ' + argv[ 0 ] + " <carrel>" )
carrel = argv[ 1 ]

# initialize
lexicon = configuration( LIBRARY )/carrel/ETC/LEXICON
with open( lexicon ) as handle : lexicon = handle.read().splitlines()

# process each item in the lexicon; create lists of nodes and edges
nodes  = []
edges  = []
for i in range( len( lexicon ) ) :

	# get the given word and do a sanity check; make sure the word is a noun
	synsets01 = wn.synsets( lexicon[ i ], pos=wn.NOUN )
	if len( synsets01 ) == 0 : continue

	# process every other word in the lexicon; here, could probably exploit itertools
	for j in range( i+1, len( lexicon ) ) :

		# get the next word and do a sanity check; again, make sure the word is a noun
		synsets02 = wn.synsets( lexicon[ j ], pos=wn.NOUN )
		if len( synsets02 ) == 0 : continue
		
		# re-initialize
		distance = MINIMUM
		pair     = ()

		# process each synset of the given word; identify the most similar pair
		for synset01 in synsets01 :

			# check for exact given word; but langauge is ambiguous
			word01 = synset01.name().split( '.' )[ 0 ]
			if word01 != lexicon[ i ] : continue
			
			# process each synset in the other given word
			for synset02 in synsets02 :
	
				# check for exact given word
				word02 = synset02.name().split( '.' )[ 0 ]
				if word02 != lexicon[ j ] : continue
				
				# compute similarity and compare
				similarity = synset01.path_similarity( synset02 ) 
				if similarity > distance :
		
					# update
					distance = similarity
					pair     = ( synset01, synset02 )

		# only evaluate if there is a pair
		if len( pair ) == 0 : continue
		
		# re-initialize
		synset01 = pair[ 0 ]
		synset02 = pair[ 1 ]
				
		# get the names of the given pairs; these will become nodes
		source = synset01.name().split( '.' )[ 0 ]
		target = synset02.name().split( '.' )[ 0 ]

		# get and check for a hypernym
		hypernym  = synset01.lowest_common_hypernyms( synset02 )
		if len( hypernym ) > 0 :
		
			# get the first one
			hypernym = hypernym[ 0 ]
			hypernym = hypernym.name().split( '.' )[ 0 ]
			if hypernym in STOPWORDS : continue
			
			# update the lists of nodes and edges
			nodes.append( ( source,   { 'types' : 'keyword' } ) )
			nodes.append( ( target,   { 'types' : 'keyword' } ) )
			nodes.append( ( hypernym, { 'types' : 'hypernym' } ) )
			edges.append( ( source, hypernym, { 'weight' : distance } ) )
			edges.append( ( target, hypernym, { 'weight' : distance } ) )
			
# build and output the graph
graph = DiGraph()
graph.add_nodes_from( nodes )
graph.add_edges_from( edges )
write_gml( graph, stdout.buffer )

# done
exit()

	
	