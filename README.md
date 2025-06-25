Reader Lexicons
===============

This folder/directory contains a set of Bash shell and Python scripts used to create and enhance lexicons -- lists of desireable words rooted in Distant Reader study carrels. As such, these lexicons are kinda, sorta the complements to or the inverses of stop words. They are intended to model desirable ideas and concepts, and they are intended to be used to query, filter, and describe sentences and documents in narrative corpora. The scripts exploit the [Distant Reader Toolbox](https://reader-toolbox.readthedocs.io), but the concepts behind the Helpers are appropos to any corpus and the investigation of it.

Many of the scripts in the `bin` dirctory are used to create lexicons. They are listed below in an order of least complexity to greatest complexity. Remember, in order for these scripts to work, one needs to install the [Distant Reader Toolbox](https://reader-toolbox.readthedocs.io) and have at least one study carrel in their local library:

* `./bin/initialize-with-unigrams.sh` - given the name of a study carrel and an integer (N), output a list of the N most frequent words, sans stop words

* `./bin/initialize-with-keywords.sh` - given the name of a study carrel and an integer (N), output a list of the N most frequent keywords, sans stop words

* `./bin/initialize-with-nouns.sh` - given the name of a study carrel and an integer (N), output a list of the N most frequent nouns

* `./bin/initialize-with-file.sh` - given the name of a study carrel and the name of a file, copy the given file to the carrel's lexicon; useful when one has specific ideas to explore and those ideas are not explicitly hightlighed as unigrams, nouns, or keywords; example files can be found in the etc directory

* `./bin/initialize-with-all.sh` - given the name of a study carrel and an integer (N), output a list of the N most frequent unigrams, nouns, keywords, the keywords' semantically related words
    
Some of the scripts in the bin directory are used to modify and enhance existing lexicons:

* `./bin/lexicon2variants.py` - given the name of a study carrel, output all variations of the given lexicon words found in the carrel; for example, if a lexicon word is "library", then the output ought to include "libraries", "libraians", "librarianship", etc.

* `./bin/lexicon2variants.sh` - a front-end to lexicon2variants.py

* `./bin/lexicon2related.py` - given the name of a study carrel, output lexicon words and their semantically similar words; rooted in the concept of word embedding, this script identifies words often used in the "same breath" as the given word; for example, if the given word is "love", then a semantically related word might be "relationship"

* `./bin/lexicon2related.sh` - a front-end to lexicon2related.py

* `./bin/lexicon2synonyms.py` - given the name of a study carrel, use WordNet to identify and output synonyms of lexicon words; this script will most likely output words not necessarily found in a study carrel

The balance of the scripts in the bin directory output network graph files used to evaluate and visualize characteristics of a lexicon. These scripts are both cool and kewl; these scripts can be used to illustrate features, shapes, and relationships between items in a lexicon. After you run these scripts and import them into something like [Gephi](https://gephi.org), you will be able to describe your lexicon in nuanced ways. For example, you will be able to identify both strengths and weaknesses of a lexicon:

* `./bin/lexicon2vectors.py` - given the name of a study carrel and an integer (N), output an edges file with three columns: 1) source, 2) target, and 3) weight; the value of source is a lexicon word, target is a semantically related word, and weight is the semantic distance between source and target

* `./bin/lexicon2hypernyms2gml.py` - given a study carrel, output a graph markup language file hightlighting nouns in the lexicon and their hypernyms ("broader terms"); uses WordNet to do the good work, and for example, using this script brings to light concepts such as "mythical characters" when lexicon words include "ulysses", "achilles", and "hector"

Why should you care? Because the process of coming up sets of words connoting and alluding to concepts is difficult. If I were to ask you to list twelve colors, I assert the procesds would be a bit challenging. On the other hand, if I were to give you a list of words and then ask you to identify the colors, then the process would be easy. The Helpers faciliate this process. One is expected to automatically generate a lexicon, and then curate it by hand. Moreover, once a lexicon is manifested as a file, it a almost trivial to use the lexicon as input to queries, thus eliminating a whole lot of typing. Again, ease of use.

These scripts work very well for me. They make it easy for me to compare and contrast study carrel -- data set -- contents. They make it easy for me to extract sentences and documents represented by my sets of curated words. They make my work more scalable.

Fun with data science, data science with words.

---
Eric Lease Morgan &lt;eric_morgan@infomotions.com&gt;  
June 25, 2025