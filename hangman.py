import tkinter as tk
import random

class HangmanGame:
    def __init__(self):
        # Initialize game variables
        self.chosen_word = self.choose_word()
        self.guessed_letters = []
        self.tries = 6

        # Create the main window for the game
        self.window = tk.Tk()
        self.window.title('Hangman Game')
        self.window.geometry('400x350')

        # Display the word to guess
        self.word_label = tk.Label(self.window, text=self.display_word(self.chosen_word, self.guessed_letters), font=('Arial', 20), padx=10, pady=10)
        self.word_label.pack()

        # Entry field for user input
        self.entry = tk.Entry(self.window, font=('Arial', 16))
        self.entry.pack(pady=10)
        self.entry.focus()

        # Button for submitting guesses
        self.submit_button = tk.Button(self.window, text='Guess', command=self.get_guess, bg='sky blue', fg='white', font=('Arial', 12))
        self.submit_button.pack(pady=5)

        # Label for displaying information to the user
        self.info_label = tk.Label(self.window, text='', font=('Arial', 12), fg='red')
        self.info_label.pack(pady=5)

        # Label to show remaining tries
        self.tries_label = tk.Label(self.window, text=f'Tries left: {self.tries}', font=('Arial', 12))
        self.tries_label.pack(pady=5)

        # Button for trying again (initially hidden)
        self.try_again_button = tk.Button(self.window, text='Try Again', command=self.try_again, bg='orange', fg='white', font=('Arial', 12))
        self.try_again_button.pack(pady=5)
        self.try_again_button.pack_forget()

        # Bind the Enter key to call get_guess() when pressed in the entry field
        self.entry.bind('<Return>', lambda event: self.get_guess())

    def choose_word(self):
        words = ['apple', 'banana', 'orange', 'grape', 'watermelon']
        return random.choice(words).lower()

    def display_word(self, word, guessed_letters):
        display = ''
        for letter in word:
            if letter in guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display.strip()

    def try_again(self):
        # Reset game variables and GUI elements for a new game
        self.chosen_word = self.choose_word()
        self.guessed_letters = []
        self.tries = 6

        self.word_label.config(text=self.display_word(self.chosen_word, self.guessed_letters))
        self.info_label.config(text='')
        self.tries_label.config(text=f'Tries left: {self.tries}')
        self.try_again_button.pack_forget()  # Hide the "Try Again" button

    def get_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.info_label.config(text='Please enter a single letter.', fg='red')
        elif guess in self.guessed_letters:
            self.info_label.config(text='You already guessed that letter.', fg='red')
        else:
            self.guessed_letters.append(guess)
            display = self.display_word(self.chosen_word, self.guessed_letters)
            self.word_label.config(text=display)

            if guess not in self.chosen_word:
                self.tries -= 1
                self.tries_label.config(text=f'Tries left: {self.tries}')

                if self.tries == 0:
                    self.info_label.config(text=f'Sorry, you ran out of tries. The word was: {self.chosen_word}', fg='red')
                    self.try_again_button.pack()  # Show the "Try Again" button

            if '_' not in display:
                self.info_label.config(text=f'Congratulations! You guessed the word: {self.chosen_word}', fg='green')
                self.try_again_button.pack()  # Show the "Try Again" button

    def play(self):
        self.window.mainloop()

hangman = HangmanGame()
hangman.play()
