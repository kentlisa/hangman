from milestone_2 import *

while True:
    if check_input_valid() == True:
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')


def letter_in_word():
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(F'Sorry, {guess} is not in the word.')

letter_in_word()