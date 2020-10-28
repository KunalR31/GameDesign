import random
import time

name=input('What Is Your Name?')
numbers={'uno':'one','dos':'two','tres':'three','quatro':'four','cinco':'five','seis':'six','siete':'seven','ocho':'eight','nueve':'nine','diez':'ten'}
verbs={'hablar':'to speak', 'escribir':'to write', 'hacer':'to do', 'leer':'to read', 'beber':'to drink', 'cocinar':'to cook', 'trabajar':'to work'}

def game():
    score = 0
    rounds = 5
    print('')
    print('Good luck',name,end='!')
    def words():
        print('\nHere Are Your Words')
        for key, value in set.items():
            print('|',key,end=' ')
        print(' ')
    for key, value in set.items():
        word = value
        correct = key
        words()
        print('What do you think the word',word,end=' is in Spanish?')
        answer=input('\nAnswer: ')
        if answer == correct:
            print('\nCorrect\n')
            score += 1
            rounds -= 1
        else:
            print('\nIncorrect\n')
            rounds -= 1
        if rounds == 0:
            print('Your score was',score,'out of 5')
            if score >= 3:
                print('Congratulations', name, 'you won')
            else:
                print('You lost')
            start=input('Would you like to play (yes/no)')
            if start == "yes":
                score = 0
                print('')
                menu()
    time.sleep(5)
def menu():
    print('***********************************')
    print('*   Spanish Word Guessing Game    *')
    print('*                                 *')
    print('*    What mode do you to play     *')
    print('*         1. Numbers              *')
    print('*          2.Verbs                *')
    print('*         How to play:            *')
    print('*You have 5 turns to guess 3 words*')
    print('***********************************')


start=input('Would you like to play (yes/no)')
if start == "yes":
    score = 0
    print('')
    menu()
    set=input('Which mode do you want to play (1/2)?')
    if set == '1':
        set=numbers
        game()
    elif set == '2':
        set = verbs
        game()
