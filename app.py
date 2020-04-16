import random

sets = ("hearts", "clubs", "diamonds", "spades")

randomNo52 = random.randint(0,13)
randomNo52 = randomNo52 +1
if randomNo52 == 11:
    randomNo52 = "Jack"
if randomNo52 == 12:
    randomNo52 = "Queen"
if randomNo52 == 13:
    randomNo52 = "King"
if randomNo52 == 1:
    randomNo52 = "Ace"
if randomNo52 <= 10 and randomNo52 > 1:
    randomNo52 = str(randomNo52)

randomSet = random.choice(sets)

print ("your card is the " + randomNo52 + " "+ "of " + randomSet)
