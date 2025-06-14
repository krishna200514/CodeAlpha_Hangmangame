import random

def hangman():
    words = ["apple", "python", "robot", "train", "water"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have 6 chances. Good luck!")

    while attempts > 0 and "_" in guessed:
        print("\nWord: " + " ".join(guessed))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

    if "_" not in guessed:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

# Run the game
hangman()
