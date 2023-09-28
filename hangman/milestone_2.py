import random

#creates list of words
word_list = ['peach', 'pineapple', 'apple', 'banana', 'strawberry']
print(word_list)

#chooses random word
word = random.choice(word_list)
print(word)

#user input: guess
guess = input('Enter a letter: ')

#checks if guess is valid
if guess.isalpha() == True and len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! that is not a valid input.')