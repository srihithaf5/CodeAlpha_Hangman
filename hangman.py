import random

def hangman():
    # Predefined list of 5 words
    words = ["python", "intern", "project", "hangman", "codealpha"]
    word = random.choice(words)  # Randomly select a word
    guessed_word = ["_"] * len(word)  # Hide word with underscores
    guessed_letters = []  # Keep track of guessed letters
    attempts = 6  # Maximum incorrect guesses allowed

    print("🎮 Welcome to Hangman Game!")
    print("Guess the word: ", " ".join(guessed_word))

    # Game loop
    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        # Validation
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Good job! '{guess}' is in the word.")
            # Reveal the guessed letter
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Word: ", " ".join(guessed_word))
        print("Guessed Letters: ", ", ".join(guessed_letters))

    # Game Over
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The correct word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()

