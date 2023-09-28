import random

#creates list of words
word_list = ['peach', 'pineapple', 'apple', 'banana', 'strawberry']

#chooses random word
word = random.choice(word_list)

#user input: guess
guess = input('Enter a letter: ')

def check_input_valid():
    '''
    This function checks that the input is alphabetical and that it only contains one letter.
    
    Args:
        input: str
            String containing the user input. Should be a single letter.
    '''
    if guess.isalpha() == True and len(guess) == 1:
        return True
    else:
        return False