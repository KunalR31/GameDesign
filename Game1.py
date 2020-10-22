import random
import time

name=input("What is your name?")
gameWords=['python','java','PHP','javascript','computer','geeks','keyboard','laptop','headphones','hardware','software']
answer=input('do you want to guess a word?')
print('Good luck!', name)
while answer == 'yes':
    word= random.choice(gameWords)
    guesses =''
    turns=6
    while turns>0:
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print('')
        guess= input("give me a letter:")
        guesses += guess
    if guess not in word:
        turns -= 1
    if turns == 0:
        print('GAME OVER!')
        answer=input('do you want to play again?')
print('Come back soon!')
time.sleep(3)
