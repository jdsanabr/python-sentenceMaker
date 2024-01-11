import random

'''
This program will write sentences composed of nouns and verbs.
The theme of the sentences is related to Super Smash Bros Ultimate tournament commentary.

Though this is a simple program, the primary purpose of this is for me to become familiar with Python syntax.
'''


# List: contains selection of noun words
nouns = ["Player 2", "ledge"]

# List: contains selection of verb words
verbs = ["three stocks", "spikes", "edge guards", "grabs"]


# Need a random noun for my sentence:
nounInt = random.randint(0, 1)

# Need a random verb for my sentence:
if nounInt == 0:
    verbInt = random.randint(0, 3)
else:
    verbInt = 2


# This string contains the sentence to be printed.
mySentence = "Player 1 " + verbs[verbInt] + " " + nouns[nounInt] + "!"

print(mySentence)
