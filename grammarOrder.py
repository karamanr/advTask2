import random
personWords = ["Baxter", "Shila", "Igor"]
actionWords = ["recognise", "eat", "sees", "pick"]
positionWords = ["left", "right", "forwards", "backwards"]
pronounWords = ["I", "you", "him", "we", "her"]
thingWords = ["screwdriver", "diamond", "person", "boat", "ball", "dog", "apple"]
valueWords = ["cheap", "expensive", "priceless"]
def buildSentence():
	"""Function to build a random sentence from the different word arrays. Will return an array of length 3 or 4"""
	sentenceThree = []
	sentenceFour = []
	for i in range(3): #build sentence of length 3
		x = random.randint(0,5)
		if x == 0:
			sentenceThree.append(personWords[random.randint(0, len(personWords)-1)])
		elif x == 1:
			sentenceThree.append(actionWords[random.randint(0, len(actionWords)-1)])
		elif x == 2:
			sentenceThree.append(positionWords[random.randint(0, len(positionWords)-1)])
		elif x == 3:
			sentenceThree.append(pronounWords[random.randint(0, len(pronounWords)-1)])
		elif x == 4:
			sentenceThree.append(thingWords[random.randint(0, len(thingWords)-1)])
		else:
			sentenceThree.append(valueWords[random.randint(0, len(valueWords)-1)])
	for i in range(4): #build sentence of length 4
		x = random.randint(0,5)
		if x == 0:
			sentenceFour.append(personWords[random.randint(0, len(personWords)-1)])
		elif x == 1:
			sentenceFour.append(actionWords[random.randint(0, len(actionWords)-1)])
		elif x == 2:
			sentenceFour.append(positionWords[random.randint(0, len(positionWords)-1)])
		elif x == 3:
			sentenceFour.append(pronounWords[random.randint(0, len(pronounWords)-1)])
		elif x == 4:
			sentenceFour.append(thingWords[random.randint(0, len(thingWords)-1)])
		else:
			sentenceFour.append(valueWords[random.randint(0, len(valueWords)-1)])
	if random.randint(0,1) == 0:
		return " ".join(sentenceThree)
	else:
		return " ".join(sentenceFour)
def grammarCheck(sentence):
	"""Takes an input of a sentence, returns true if sentence satisfies grammar rules and false if not"""
	print(sentence)
	sentence=sentence.split()
	if len(sentence) == 3:
		if sentence[0] in personWords and sentence[1] in actionWords and sentence[2] in thingWords:
			print("Sentence is grammatically correct: person, action, thing")
			return True
		elif sentence[0] in personWords and sentence[1] in actionWords and sentence[2] in positionWords:
			print("Sentence is grammatically correct: person, action, position")
			return True
		elif sentence[0] in pronounWords and sentence[1] in actionWords and sentence[2] in thingWords:
			print("Sentence is grammatically correct: pronoun, action, thing")
			return True
		elif sentence[0] in pronounWords and sentence[1] in actionWords and sentence[2] in positionWords:
			print("Sentence is grammatically correct: pronoun, action, position")
			return True
		else:
			print("Sentence is grammatically incorrect!")
			print("Word order: person, action, thing is not fulfilled")
			print("Word order: person, action, position is not fulfilled")
			print("Word order: pronoun, action, thing is not fulfilled")
			print("Word order: pronoun, action, position is not fulfilled")			
			return False			
	elif len(sentence) == 4:
		if sentence[0] in personWords and sentence[1] in actionWords and sentence[2] in valueWords and sentence[3] in thingWords:
			print("Sentence is grammatically correct: person, action, value, thing")
			return True
		else:
			print("Sentence is grammatically incorrect!")
			print("Word order: person, action, value, thing is not fulfilled") 
			return False
	else:
		print("Sentence is invalid")
		return False
if __name__ == '__main__':
	#Example usage
	#Random sentence generation
	grammarCheck(buildSentence())
	#Example sentences
	grammarCheck("Baxter sees boat")
	grammarCheck("I pick diamond")
	grammarCheck("Baxter Baxter")
	grammarCheck("boat goes backwards")
	grammarCheck("we eat apple")
	grammarCheck("Shila recognise cheap ball")
	grammarCheck("eat ball")
	grammarCheck("right right left")