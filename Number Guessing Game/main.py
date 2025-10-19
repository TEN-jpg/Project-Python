import random

while True:  # <-- master game loop
    print("...................................")
    print("Welcome! to Number Guessing Game 🎲")
    print("...................................")

    print("👶 Easy -> Number range 1 to 50 --> Attempts = 30")
    print("🤓 Medium -> Number range 1 to 100 --> Attempts = 20")
    print("🗿 Hard -> Number range 1 to 200 --> Attempts = 10")
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    if difficulty == "easy":
        max_number = 50
        max_score = 50
        penalty = 5
        max_attempts = 30
    elif difficulty == "medium":
        max_number = 100
        max_score = 100
        penalty = 20
        max_attempts = 20
    elif difficulty == "hard":
        max_number = 200
        max_score = 200
        penalty = 20
        max_attempts = 10
    else:
        print("Invalid Difficulty 😑 Switching to Medium difficulty")
        max_number = 100
        max_score = 100
        penalty = 10
        max_attempts = 20

    number_to_guess = random.randint(1, max_number)
    attempts = 0

    while True:  # game round loop
        user_guess = int(input("ENTER YOUR GUESS = "))
        attempts += 1

        if user_guess < 1 or user_guess > max_number:
            print("Number out of range *_*")
        elif user_guess == number_to_guess:
            print(".............................................................")
            print(f"Congrats!🎉 You guessed the correct number in {attempts} tries ")
            score = max(max_score - (attempts - 1) * penalty, 0)
            print(".............................")
            print(f"Your score is {score} points")
            print(".............................")
            break
        elif user_guess < number_to_guess:
            print("-Try to guess Higher")
        elif user_guess > number_to_guess:
            print("-Try to guess Lower")

        if attempts % 3 == 0:
            if number_to_guess % 2 == 0:
                print("-->Hint: The number is Even")
            else:
                print("-->Hint: The number is Odd")

        if attempts >= max_attempts:
            print("..............................................")
            print(f"Game Over 😭 The number was {number_to_guess}")
            break

    play_again = input("Do you want to play again (Y/N): ").upper()
    if play_again == "Y":
        print("Great! Try to increase difficulty and guess in less tries now")
    elif play_again == "N":
        print("Thanks for playing! 👋")
        break
