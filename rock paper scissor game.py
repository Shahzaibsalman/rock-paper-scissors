import random

print("Welcome to Rock Paper Scissors")

choices = ["rock", "paper", "scissor"]
print("Enter 0 for rock, 1 for paper, 2 for scissor")

person_choice = int(input("Enter your choice: "))

# input validation
if person_choice < 0 or person_choice > 2:
    print("Invalid choice. You lose.")
else:
    user = choices[person_choice]
    computer = random.choice(choices)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("Draw match")
    elif (
        (user == "rock" and computer == "scissor") or
        (user == "paper" and computer == "rock") or
        (user == "scissor" and computer == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")





