import random
#all colors of magic the gathering decks
decks = ['red', 'black', 'white', 'blue', 'green']

d1 = random.choice(decks)
decks.remove(d1)
d2 = random.choice(decks)
print('Oscar uses ' + d1)
print('Dad uses ' + d2)
print("Enjoy your game")