from turtle import clear
from hangman_art import logo, stages 
from hangman_words import word_list
import random


print (logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished :
    guess = input("Guess a letter: ").lower()
 #Use the clear() function imported from turtle to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    #Check if user is wrong.
    if guess not in chosen_word:
        
        print(f"You guessed {guess}, that`s not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    #Check if user has got all letters.
    if "_" not in display:
        game_is_finished = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])