import nltk
import urllib2
from FrequencySummarizer import *
from BoW import *
from bs4 import BeautifulSoup


review = "This is a very good product. These speakers have an amazing base but not so good treble. \
Also, the speakers are made of high-class wood and hence an unbeatable sound. Worth buying. This product is \
well-made, and has a good durability. I received the product in not so good packaging which was the only \
issue. The speakers are worth for it's price. Go for it without thinking."


review2 = "This product is well-made, and it does an EXCELLENT job keeping leaves out of the gutter. \
Unfortunately, while it also blocks pine needles, the needles on our New England pine trees are fine \
enough that they manage to get stuck upright in the mesh, and after a while enough of them accumulate so \
they have to be removed by hand. What's particularly bad is the needles can't be brushed off, but have to \
be pulled out of the mesh. While this reduces the need to climb an extension ladder to once a year, it doesn't \
eliminate the need, so in our application the product is OK. Zoom in on the attached picture to see a \
plucked section and a section bristling with pine needles. I am also a bit concerned that any water \
from melting snow tends to freeze up and block the mesh - particularly on the side of the house \
that does not face the sun - so there is a nagging question in the back of my mind if these might \
contribute to ice dam formation."

fs = FrequencySummarizer()
review_short_list = fs.summarize(review, 3)
review_short = " ".join(review_short_list)

#print review_short

total_score = 0

lower_review = review_short.lower()

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
print "\nExtracted Features:\n"

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

print "\nTotal Score: ", total_score, "\n"

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

