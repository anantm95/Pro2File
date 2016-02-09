positiveWords = {}

positiveWords['ok'] = 0.5
positiveWords['okay'] = 0.5
positiveWords['good'] = 1
positiveWords['well-made'] = 1
positiveWords['not bad'] = 1
positiveWords['very good'] = 1.5
positiveWords['great'] = 1.5
positiveWords['awesome'] = 2.0
positiveWords['amazing'] = 2.0
positiveWords['worth'] = 2.5
positiveWords['high-class'] = 2.8
positiveWords['excellent'] = 3.0
positiveWords['go for it'] = 3.2
positiveWords['extraordinary'] = 3.2
positiveWords['unbeatable'] = 3.5

negativeWords = {}

negativeWords['bad'] = 1
negativeWords['not ok'] = 0.5
negativeWords['not okay'] = 0.5
negativeWords['very bad'] = 1.5
negativeWords['not so good'] = 1
negativeWords['not good'] = 1
negativeWords['worst'] = 2.0
negativeWords['worse'] = 2.0
negativeWords['not worth'] = 2.5
negativeWords['low-class'] = 2.8
negativeWords["don't buy"] = 3.0


def sum_positive_words():
	sum = 0
	for word in positiveWords:
		sum += positiveWords[word]

	return sum

def sum_negative_words():
	sum = 0
	for word in negativeWords:
		sum += negativeWords[word]

	return sum