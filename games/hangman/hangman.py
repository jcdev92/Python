import random
from hangman_arts import stages, logo
from hangman_words import word_list
import os

# words = ["autana", "roraima", "corolla", "arepa", "veneco", "vinotinto"]

selected_word = random.choice(word_list)

blanks = []
matched = ""
formated = ""
lives = 6
clear = lambda: os.system("clear")
hangman = ""


for blank in selected_word:
    blanks.append(" _ ")

print(logo)
print("please welcome to the hangman game, enter a letter until you match the secret word or lose all your lives")

while matched != selected_word and lives > 0:
    letter = input("please enter a letter:\n").lower()
    clear()
    if selected_word.find(letter) >= 0:
        for i in range(0, len(selected_word)):
            if selected_word[i] == letter:
                blanks[i] = letter
        print(f"HIT! the letter: '{letter}' is in the secret word!")
        formated = ' '.join(blanks)
        matched = "".join(blanks)
    else:
        lives -= 1
        hangman = stages[lives]
        print(f"\nwrong! you guessed the letter: '{letter}', and that's not in the secret word, you loose a life")

    if hangman:    
        print(hangman)
    

    print(f"\n{formated}\n")

if lives == 0:
    print("game over, you are dead")
elif matched == selected_word:
    print(f"\nThe WORD is {selected_word}")
    print("\nCongrats!! You Win!")
    