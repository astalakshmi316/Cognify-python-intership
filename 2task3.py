def computer_guessing_game():
    print("Welcome to the Reverse Guessing Game!")
    print("Think of a number between 1 and 100 in your mind, and I will try to guess it!")
    input("Press Enter when you are ready...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        
        guess = (low + high) // 2
        attempts += 1
        
        print(f"\nIs your number {guess}?")
        feedback = input("Type 'h' if it's too high, 'l' if it's too low, or 'c' if it's correct: ").lower()

        if feedback == 'c':
            print(f"🎉 Awesome! I guessed your number in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1  
        elif feedback == 'l':
            low = guess + 1   
        else:
            print("Invalid input! Please type 'h', 'l', or 'c'.")
            attempts -= 1  


computer_guessing_game()
