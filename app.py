import random

sets = ("Hearts", "Clubs", "Diamonds", "Spades")
cards = ("king", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "Ace")

randomSet = random.choice(sets)
randomCard = random.choice(cards)

print ("your card is the " + randomCard + " "+ "of " + randomSet)


