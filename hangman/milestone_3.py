import random

#creates list of words
word_list = ['peach', 'pineapple', 'apple', 'banana', 'strawberry']

#chooses random word
word = random.choice(word_list)

def check_guess(guess):
    '''
    This function converts the letter to lower case, then checks if the letter guessed is in the hangman word.
    
    Args:
        guess: str
            String containing the letter guessed.
    Returns:
        None
    '''
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word.')

def ask_for_input():
    '''
    This function allows the user to enter their input, then checks if the input is a single letter. It then checks if the letter is in the word.
    
    Args:
        None
    Returns:
        None
    '''
    while True:
        guess = input('Enter a letter: ')
        if guess.isalpha() == True and len(guess) == 1:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()