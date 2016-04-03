import nltk
import urllib2
from FrequencySummarizer import *
from BoW import *
from bs4 import BeautifulSoup


review1 = "This is a very good product. These speakers have an amazing bases but very bad treble. \
Also, the speakers are made of high-class wood and hence an extraordinary sound. Worth buying. This product is \
well-made, and has a good durability. I received the product in not so good packaging which was the only \
issue. The speakers are worth for it's price. Go for it without thinking."

review2 = "OnePlus 2 has a lot to its name - a great fingerprint scanner, a wonderful camera (12MP + 5MP), a powerful Snapdragon processor, and a vibrant display, \ most important of all - the experience that the device provides is just amazing. The handset feels premium - and the interface is as smooth as it gets. \
There is nothing wrong at all - anywhere - in this beast of a device. But if you are really critical - the only CONS, that I can find is the new port for charging \ and the speakers. It has a new standard charging-port - so it'll take some time but you'll get used to it. The speakers are a little on \
the weaker side, but it's definitely not a deal breaker. \
For an in-depth review, check this link - http://bit.ly/OnePlus2Discount-n-Review \
On the whole - JUST GET THIS MOBILE! It's just amazing! :)"

review3 = "Conversations with God Book 1 is the single most extraordinary book I have ever \
read!!!It totally changed my life. I would recommend it to anyone who is seeking emotional\
 and spiritual growth, freedom and empowerment. This book did wonders for my relationship with \
 God, myself and everyone around me. I approach living differently, I enjoy life more.  I have \
 had a copy of this book since it was first published (1997)? and I still turn to it again and \
 again for spiritual enlightenment, upliftment and remembering. I love this book and I love \
 Neale Walsch for his courage in writing it."


fs = FrequencySummarizer()
review_short_list = fs.summarize(review1, 3)
review_short = " ".join(review_short_list)

#print review_short

total_score = 0

lower_review = review_short.lower()

tokens = nltk.word_tokenize(lower_review)
tagged_tokens = nltk.pos_tag(tokens)

#print tagged_tokens

max_positive = max_positive_words()
min_positive = min_positive_words()
max_negative = max_negative_words()
min_negative = min_negative_words()

chunk_grammar_type1 = "NP: {<RB|RBR|RBS>?<JJ>+<NN|NNS>}"
chunk_parser_type1 = nltk.RegexpParser(chunk_grammar_type1)
chunk_tree_type1 = chunk_parser_type1.parse(tagged_tokens)

np_list = []

for subtree in chunk_tree_type1.subtrees():
	if (subtree.label() == 'NP'):
		np_list.append(subtree.leaves())

print np_list;
print negativeWords['bad']
print "\nExtracted Features:\n"

for phrase in np_list:
	feature_score = 0
	intensify = 0
	for (word, tag) in phrase:
		#print phrase
		
		if(tag == 'RB' or tag == 'RBR' or tag == 'RBS'):
			intensify = 1

		if (tag == 'JJ'):

			if (word in positiveWords and word in negativeWords):
				if (positiveWords[word] > negativeWords[word]):
					feature_score += (positiveWords[word] - min_positive)/(max_positive - min_positive)
					if (intensify == 1):
						feature_score *= 1.2
				else:
					feature_score -= (negativeWords[word] - min_negative)/(max_negative - min_negative)
					if (intensify == 1):
						feature_score = feature_score * 1.2

			elif (word in positiveWords):
				#print positiveWords[word]
				feature_score += (positiveWords[word] - min_positive)/(max_positive - min_positive)
				if (intensify == 1):
					feature_score *= 1.2

			elif (word in negativeWords):
				feature_score -= (negativeWords[word] - min_negative)/(max_negative - min_negative)
				if (intensify == 1):
					feature_score *= 1.2

		if (tag == 'NN' or tag == 'NNS'):
			print word, " ", feature_score


chunk_grammar_type2 = "NP: {<RB|RBR|RBS>?<JJ>+<NN|NNS>}"
chunk_parser_type2 = nltk.RegexpParser(chunk_grammar_type2)
chunk_tree_type2 = chunk_parser_type2.parse(tagged_tokens)	

adjectives = []

for (word,tag) in tagged_tokens:
	if(tag == 'JJ'):
		adjectives.append(word)

#print adjectives


for adj in adjectives:
    if (adj in positiveWords):
    	#print positiveWords[adj]
    	total_score += (positiveWords[adj] - min_positive)/(max_positive - min_positive)

    elif (adj in negativeWords):
        total_score -= (negativeWords[adj] - min_negative)/(max_negative - min_negative)

avg_total_score = total_score/len(adjectives)

print "\nTotal Score: ", avg_total_score, "\n"