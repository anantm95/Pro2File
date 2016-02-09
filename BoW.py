import nltk

positiveWords = {}

positiveWords['good'] = 1
positiveWords['not bad'] = 1
positiveWords['very good'] = 1.5
positiveWords['great'] = 1.5
positiveWords['awesome'] = 2.0
positiveWords['amazing'] = 2.0
positiveWords['worth'] = 2.5
positiveWords['unbeatable'] = 3.5
positiveWords['high-class'] = 2.8

negativeWords = {}

negativeWords['bad'] = 1
negativeWords['very bad'] = 1.5
negativeWords['not so good'] = 1
negativeWords['not good'] = 1
negativeWords['worst'] = 2.0
negativeWords['worse'] = 2.0
negativeWords['not worth'] = 2.5
negativeWords['low-class'] = 2.8

review = "This is a very good product. These speakers have an amazing base but not so good treble. \
Also, the speakers are made of high-class wood and hence an unbeatable sound. Worth buying."

total_score = 0

lower_review = review.lower()

tokens = nltk.word_tokenize(lower_review)
tagged_tokens = nltk.pos_tag(tokens)

#print tagged_tokens

chunk_grammar = "NP: {<JJ>+<NN>}"
chunk_parser = nltk.RegexpParser(chunk_grammar)
chunk_tree = chunk_parser.parse(tagged_tokens)

np_list = []

for subtree in chunk_tree.subtrees():
	if (subtree.label() == 'NP'):
		np_list.append(subtree.leaves())

#print np_list;

for phrase in np_list:
	feature_score = 0
	for (word, tag) in phrase:
		if (tag == 'JJ'):
			if (word in positiveWords):
				feature_score += positiveWords[word]
			elif (word in negativeWords):
				feature_score -= negativeWords[word]

		if (tag == 'NN'):
			print word, " ", feature_score
	

adjectives = []

for (word,tag) in tagged_tokens:
	if(tag == 'JJ'):
		adjectives.append(word)

for adj in adjectives:
    if (adj in positiveWords):
	    total_score += positiveWords[adj]

    elif (adj in negativeWords):
        total_score -= negativeWords[adj]

print "Total Score: ", total_score
