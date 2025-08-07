print(" Welcome to the Number Guessing Game")
print("Think of a number between 1 and 100. I will try to guess it in 7 tries.")

low = 1
high = 100
found = False

for attempt in range(1, 8):  
    guess = (low + high) // 2
    print(f"\nAttempt {attempt}: Is your number {guess}?")

    feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

    if feedback == 'c':
        print(f" I guessed your number {guess} in {attempt} tries")
        found = True
        break
    elif feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    else:
        print("Invalid input. Please enter 'h', 'l', or 'c'.")

if not found:
    print(" I couldn't guess your number in 7 tries.")
