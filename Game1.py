# import random
# import time
#
# name=input("What is your name?")
# gameWords=['python','java','PHP','javascript','computer','geeks','keyboard','laptop','headphones','hardware','software']
# answer=input('do you want to guess a word?')
# print('Good luck!', name)
# while answer == 'yes':
#     word= random.choice(gameWords)
#     guesses =''
#     turns=6
#     while turns>0:
#         for char in word:
#             if char in guesses:
#                 print(char, end=' ')
#             else:
#                 print('_', end=' ')
#         print('')
#         guess= input("give me a letter:")
#         guesses += guess
#     if guess not in word:
#         turns -= 1
#     if turns == 0:
#         print('GAME OVER!')
#         answer=input('do you want to play again?')
# print('Come back soon!')
# time.sleep(3)

# import random
#
# tries = 0
#
# print("Welcome to the word game!")
# name=input("What is your name?")
# print('Good luck!', name)
#
# WORDS = ('python','java','PHP','javascript','computer','geeks','keyboard','laptop','headphones','hardware','software')
#
# word = random.choice(WORDS)
#
# correct = word
# length = len(word)
# length = str(length)
#
# guess = input("The word is " + length + " letters long. Guess a letter!: ")
#
# while tries < 5:
#     for guess in word:
#         if guess not in word:
#             print ("Sorry, try again.")
#         else:
#             print ("Good job! Guess another!")
#
#     tries = tries + 1
#
#     if tries == 5:
#         final = input ("Try to guess the word!: ")
#
#         if final == correct:
#             print ("Amazing! My word was ", word, "!")
#
#         else:
#             print ("Sorry. My word was ", word, ". Better luck next time!")
#
# input("\n\nPress enter to exit")
import random

name = input("What is your name? ")


print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)


print("Guess the characters")

guesses = ''

turns = 12


while turns > 0:


    failed = 0


    for char in word:


        if char in guesses:
            print(char)

        else:
            print("_",end=' ')


            failed += 1


    if failed == 0:

        print("You Win")


        print("The word is: ", word)
        break


    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1

        print("Wrong")

        print("You have", + turns, 'more guesses')


        if turns == 0:
            print("You Lose")
