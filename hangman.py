import random
words = ["apple", "banana", "grape", "orange", "mango"]
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman Funny Game")
print("You have 6 incorrect guesses allowed.")

while True:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())
    print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
    if "_" not in display_word:
        print("Congratulations! You guessed the word correctly!")
        break
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess not in secret_word:
        wrong_guesses += 1
        print("Wrong guess!")
    if wrong_guesses == max_wrong_guesses:
        print("Game Over!")
        print("The word was:", secret_word)
        break