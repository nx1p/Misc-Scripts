from random import randint
import os

def LoadQuotes():
	return open('storage/quotes.txt').read().splitlines()

Quotes = LoadQuotes()
NumberOfQuotes = len(Quotes)
RandomQuoteNumber = randint(0, NumberOfQuotes)

print Quotes[RandomQuoteNumber]