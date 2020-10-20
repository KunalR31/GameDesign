import random
import time

name=input("What is your name?")
print('Good luck!', name)
gameWords=['python','java','PHP','javascript','computer','geeks','keyboard','laptop','headphones','hardware','software']
answer=input('do you want to guess a word?')
while answer == 'yes':
    word= random.choice(gameWords)
    guesses =''
    turns=6
    while turns>0:
        for char in word:
            if char in guesses:
                print(char)
            else:
                print('_', end=' ')
        print('')
    if guess in gameWords:
        print('good job')
        guess= input("give me a letter:")
        guesses += guess
    print(word)
    answer=input('do you want to play again?')
time.sleep(3)
