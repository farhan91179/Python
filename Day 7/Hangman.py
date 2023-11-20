import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

#Testing
# print(f'Pssst, the solution is {chosen_word}')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"No!! the word was {chosen_word}, You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(f"Yes!! the word was {chosen_word}, You Win.")

    from hangman_art import stages
    print(stages[lives])