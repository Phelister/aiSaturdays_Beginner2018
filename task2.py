import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

randomPhrase

reversePhrase= randomPhrase[::-1]

print(randomPhrase) #prints the random chosen phrase so that one can compare to the reversed phrase

print(reversePhrase) #prints the reversed phrase

