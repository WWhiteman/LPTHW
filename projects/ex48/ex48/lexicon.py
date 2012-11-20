def scan(stuff):
	words = stuff.split(' ')
	answer = []
	for word in words:
		directions = ["north", "south", "east", "west", "down", "up",
					   "left", "right", "back"]
		verbs = ["go", "stop", "kill", "eat"]
		stop_verbs = ["the", "in", "of", "from", "at", "it"]
		nouns = ["door", "bear", "princess", "cabinet"]

		if isint(word) == None:
			if word in directions:
				kind = "direction"
				answer.append((kind, word))
			elif word in verbs:
				kind = "verb"
				answer.append((kind, word))
			elif word in stop_verbs:
				kind = "stop"
				answer.append((kind, word))
			elif word in nouns:
				kind = "noun"
				answer.append((kind, word))
			else:
				kind = "error"
				answer.append((kind, word))
		else:
			kind = "number"
			answer.append((kind, int(word)))

	return(answer)

def isint(isnumber):
	try:
		return int(isnumber)
	except ValueError:
		return None



