# Hangman game in Python;;;

import random

words = ("ronaldo", "messi", "neymar", "mbappe", "yamal","lewondoski","modric","marcelo","saka")

# Dictionary of hangman stages
hangman_art = {
    0: (
        "    ",
        "    ",
        "    ",
    ),
    1: (
        " o  ",
        "    ",
        "    ",
    ),
    2: (
        " o  ",
        " |  ",
        "    ",
    ),
    3: (
        " o  ",
        "/|  ",
        "    ",
    ),
    4: (
        " o  ",
        "/|\\ ",
        "    ",
    ),
    5: (
        " o  ",
        "/|\\ ",
        "/   ",
    ),
    6: (
        " o  ",
        "/|\\ ",
        "/ \\ ",
    ),
}


def display_man(wrong_guesses):
    print("----------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("----------------")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        # Correct guess
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        # Win condition
        if "_" not in hint:
            display_hint(hint)
            print("🎉 You win!")
            is_running = False

        # Lose condition
        elif wrong_guesses == 6:
            display_man(wrong_guesses)
            print("💀 You lose!")
            print("The word was:", answer)
            is_running = False


if __name__ == "__main__":
    main()