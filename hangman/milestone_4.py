import random

word_list = ['peach', 'pineapple', 'apple', 'banana', 'strawberry']

class Hangman:
    '''
    This class is used to play a game of hangman.
    
    Attributes
    ----------
    word_list : list
        the list of words that might be chosen by the hangman
    word : str
        the chosen hangman word
    word_guessed : list
        list of letters correctly guessed
    num_letters : int
        number of unique letters left to guess
    num_lives : int
        number of lives the player has (default is 5)
    list_of_guesses : list
        list of letters the player has guessed

    Methods
    -------
    check_guess(guess):
        Checks if the letter guessed is in the word.
        If not, the player loses a life. 
        If it is, the letter is appended to word_guessed.
    ask_for_input():
        Gathers user guess. 
        Iterates until valid guess is chosen.
        Appends to list_of_guesses.
    '''
    def __init__(self, word_list, num_lives = 5):
        '''
        See help(Hangman) for accurate signature
        '''
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = len(set(self.word) - {letter for letter in self.word_guessed if letter.isalpha})
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This function is used to check if a guess is valid.

        Parameters
        ----------
        guess : str
            The user input.

        Returns
        -------
        None
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for letter in self.word:
                if guess == letter:
                    index = self.word.index(guess)
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            print(f'Sorry, {guess} is not in the word.')
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')
            
    def ask_for_input(self):
        '''
        This function is used to gather the user input.
        It then assesses if the input is valid.
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        while True:
            guess = input('Enter a letter: ')
            if guess.isalpha() == False or len(guess) != 1:
               print('Invalid letter. Please, enter a single alphabetical character.') 
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

hangman1 = Hangman(word_list)
hangman1.ask_for_input()