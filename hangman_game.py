import random

# ASCII stages for the hangman
HANGMAN_STAGES = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

# 6 Levels with engaging words and 3 progressive hints each
GAME_LEVELS = [
    {
        "word": "galaxy",
        "hints": [
            "Hint 1: It contains billions of stars, gas, and dust.",
            "Hint 2: Our solar system is located inside the Milky Way one.",
            "Hint 3: Bound together by gravity on a massive cosmic scale."
        ]
    },
    {
        "word": "crystal",
        "hints": [
            "Hint 1: A solid material with a highly ordered structure.",
            "Hint 2: Often found as sparkling quartz or cut into gemstones.",
            "Hint 3: Known for clear, geometric faces and beautiful shine."
        ]
    },
    {
        "word": "whisper",
        "hints": [
            "Hint 1: Speaking in a very soft, low breath.",
            "Hint 2: Done without vibrating your vocal cords fully.",
            "Hint 3: Used when you want to keep a secret in a quiet room."
        ]
    },
    {
        "word": "phoenix",
        "hints": [
            "Hint 1: A majestic mythological creature.",
            "Hint 2: Deeply associated with fire, flame, and brilliant colors.",
            "Hint 3: Famously rises brand new from its own ashes."
        ]
    },
    {
        "word": "journey",
        "hints": [
            "Hint 1: The act of traveling from one destination to another.",
            "Hint 2: Often spans a long distance or an adventurous quest.",
            "Hint 3: People often say 'life is a ___' rather than a destination."
        ]
    },
    {
        "word": "eclipse",
        "hints": [
            "Hint 1: A fascinating astronomical alignment event.",
            "Hint 2: Involves celestial bodies passing in front of one another.",
            "Hint 3: Can be solar or lunar, temporarily blocking light."
        ]
    }
]

def play_hangman():
    print("=" * 50)
    print("      WELCOME TO THE ULTIMATE HANGMAN ADVENTURE!     ")
    print("=" * 50)
    
    current_level = 0
    max_levels = len(GAME_LEVELS)

    while current_level < max_levels:
        level_data = GAME_LEVELS[current_level]
        secret_word = level_data["word"]
        hints = level_data["hints"]
        
        guessed_letters = []
        incorrect_guesses = 0
        max_incorrect = 6

        print(f"\n✨ --- LEVEL {current_level + 1} of {max_levels} --- ✨")
        print(f"You have {max_incorrect} incorrect attempts allowed.")

        # Main game loop for the current level
        while incorrect_guesses <= max_incorrect:
            # Display current stage drawing
            print(HANGMAN_STAGES[incorrect_guesses])

            # Progressive hints based on incorrect guesses
            print(f"💡 {hints[0]}")
            if incorrect_guesses >= 2:
                print(f"💡 {hints[1]}")
            if incorrect_guesses >= 4:
                print(f"💡 {hints[2]}")

            # Display current word progress
            display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
            print("\nWord: " + " ".join(display_word))
            
            # Check if user has guessed all letters
            if "_" not in display_word:
                print(f"\n🎉 Awesome! You cleared Level {current_level + 1}!")
                print(f"The word was: {secret_word}")
                break

            # Check if attempts ran out
            if incorrect_guesses == max_incorrect:
                break

            # Take player input
            guess = input("\nEnter a letter: ").strip().lower()

            # Input validation
            if len(guess) != 1 or not guess.isalpha():
                print("⚠️ Please enter a single valid alphabet letter.\n")
                continue

            if guess in guessed_letters:
                print(f"⚠️ You've already guessed '{guess}'. Try another letter.\n")
                continue

            # Add guess to history
            guessed_letters.append(guess)

            # Check guess outcome
            if guess in secret_word:
                print(f"✅ Good job! '{guess}' is in the word.")
            else:
                incorrect_guesses += 1
                remaining = max_incorrect - incorrect_guesses
                print(f"❌ Oops! '{guess}' is not in the word.")
                print(f"Remaining attempts: {remaining}")

            print("-" * 40)

        # If the loop exits because attempts ran out
        if incorrect_guesses == max_incorrect:
            print(f"\n💥 Game Over! You ran out of guesses on Level {current_level + 1}.")
            print(f"The correct word was: {secret_word}")

        # Ask if player wants to proceed to the next round/level
        if current_level < max_levels - 1:
            choice = input("\nDo you want to play the next round? (yes/no): ").strip().lower()
            if choice not in ["yes", "y"]:
                print("\nThanks for playing! See you next time.")
                break
        else:
            print("\n🏆 Congratulations! You have successfully completed all 6 levels!")
            
        current_level += 1

if __name__ == "__main__":
    play_hangman()