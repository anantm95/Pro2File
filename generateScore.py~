import nltk
import urllib2
from FrequencySummarizer import *
from BoW import *
from bs4 import BeautifulSoup


review = "This is a very good product. These speakers have an amazing base but very bad treble. \
Also, the speakers are made of high-class wood and hence an unbeatable sound. Worth buying. This product is \
well-made, and has a good durability. I received the product in not so good packaging which was the only \
issue. The speakers are worth for it's price. Go for it without thinking."


fs = FrequencySummarizer()
review_short_list = fs.summarize(review, 3)
review_short = " ".join(review_short_list)

print review_short

total_score = 0

lower_review = review_short.lower()

tokens = nltk.word_tokenize(lower_review)
tagged_tokens = nltk.pos_tag(tokens)

print tagged_tokens

chunk_grammar = "NP: {<JJ>+<NN>}"
chunk_parser = nltk.RegexpParser(chunk_grammar)
chunk_tree = chunk_parser.parse(tagged_tokens)

np_list = []

for subtree in chunk_tree.subtrees():
	if (subtree.label() == 'NP'):
		np_list.append(subtree.leaves())

max_positive = max_positive_words()
min_positive = min_positive_words()
max_negative = max_negative_words()
min_negative = min_negative_words()

#print np_list;
print "\nExtracted Features:\n"

for phrase in np_list:
	feature_score = 0
	for (word, tag) in phrase:
		#print phrase
		if (tag == 'JJ'):
			if (word in positiveWords):
				feature_score += (positiveWords[word] - min_positive)/(max_positive - min_positive)
			elif (word in negativeWords):
				feature_score -= (negativeWords[word] - min_negative)/(max_negative - min_negative)

		if (tag == 'NN'):
			print word, " ", feature_score
	

adjectives = []

for (word,tag) in tagged_tokens:
	if(tag == 'JJ'):
		adjectives.append(word)

print adjectives


for adj in adjectives:
    if (adj in positiveWords):
	    total_score += (positiveWords[adj] - min_positive)/(max_positive - min_positive)

    elif (adj in negativeWords):
        total_score -= (negativeWords[adj] - min_negative)/(max_negative - min_negative)

avg_total_score = total_score/len(adjectives)

print "\nTotal Score: ", avg_total_score, "\n"

'''feed_xml = urllib2.urlopen('http://feeds.bbci.co.uk/news/rss.xml').read()
feed = BeautifulSoup(feed_xml.decode('utf8'), "lxml")
to_summarize = map(lambda p: p.text, feed.find_all('guid'))

fs = FrequencySummarizer()
for article_url in to_summarize[:5]:
    title, text = get_only_text(article_url)
    print '----------------------------------'
    print title
    for s in fs.summarize(text, 2):
    	print '*',s'''

