import random
from hangman_arts import stages, logo
from hangman_words import word_list

# words = ["autana", "roraima", "corolla", "arepa", "veneco", "vinotinto"]

selected_word = random.choice(word_list)

blanks = []
matched = ""
lives = 6

for blank in selected_word:
    blanks.append(" - ")

print(logo)
print("please welcome to the hangman game, enter a letter until you match the secret word or lose all your lives")
while matched != selected_word and lives > 0:
    print(f"\n   {matched}  \n")
    letter = input("please enter a letter:\n").lower()
    if selected_word.find(letter) >= 0:
        for i in range(0, len(selected_word)):
            if selected_word[i] == letter:
                blanks[i] = letter
    else:
        lives -= 1
        hangman = stages[lives]
        print(f"\nwrong! you gussed the letter: {letter}, and that's not in the secret word, you loose a life")
        print(hangman)

    matched = "".join(blanks)

if lives == 0:
    print("game over, you are dead")
elif matched == selected_word:
    print(f"\n{matched}")
    print("\nCongrats!! You Win!")
    