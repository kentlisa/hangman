import random

#creates list of words
word_list = ['peach', 'pineapple', 'apple', 'banana', 'strawberry']
print(word_list)

#chooses random word
word = random.choice(word_list)
print(word)

#user input: guess
guess = input('Enter a letter: ')

def check_input_valid(input):
    '''
    This function checks if the input is alphabetical and that it only contains one letter.
    
    Args:
        input: str
            String containing the user input. Should be a single letter.
    '''
    if input.isalpha() == True and len(input) == 1:
        print('Good guess!')
    else:
        print('Oops! that is not a valid input.')

