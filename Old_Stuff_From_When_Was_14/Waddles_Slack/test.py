import random

def fic():
    fics = open('urls.txt').read().splitlines()
    num = random.randint(0, (len(fics)-1))
    return ('Here ya go a random TAU fic on Ao3: '+fics[num]+' :D')



print fic()
