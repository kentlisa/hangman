while True:
    guess = input('Enter a letter: ')
    if guess.isalpha() == True and len(guess) == 1:
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')