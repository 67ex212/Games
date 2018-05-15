import random

global Deck
Deck   = [] #list of tuples of suits and values
Suits  = ['C','D','H','S']
Values = ['A','K','Q','J',10,9,8,7,6,5,4,3,2]


for x in Suits:
	for y in Values:
		Deck.append((y,x))

random.shuffle(Deck)
print(Deck)

def draw(location,count):
	for x in count:
		Deck.popleft()
		