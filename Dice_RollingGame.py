import random

player_score = 0
computer_score = 0

print("🎲 DICE BATTLE 🎲")
print("First to 5 points wins!")

while player_score < 5 and computer_score < 5:
    input("\nPress Enter to roll...")

    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print(f"\nYou rolled: {player_roll}")
    print(f"Computer rolled: {computer_roll}")

    if player_roll > computer_roll:
        print("🏆 You win this round!")
        player_score += 1
    elif computer_roll > player_roll:
        print("💻 Computer wins this round!")
        computer_score += 1
    else:
        print("🤝 It's a tie!")

    print(f"\nScore")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")
print()
print("====================")

if player_score == 5:
    print("🎉 CONGRATULATIONS! You won the game!")
else:
    print("😢 The computer won. Better luck next time!")

print("====================")