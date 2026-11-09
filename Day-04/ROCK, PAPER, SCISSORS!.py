rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

choices = [rock, paper, scissors]

player_matches = 0
computer_matches = 0

print("WELCOME TO ROCK, PAPER, SCISSORS!")
print("THREE MATCHES! FIRST TO TWO ROUNDS WINS EACH MATCH!")

for match in range(1, 4):

    player_score = 0
    computer_score = 0

    print(f"\n========== MATCH {match} ==========")

    while player_score < 2 and computer_score < 2:

        player = input("\n0 = ROCK, 1 = PAPER, 2 = SCISSORS: ")

        if player not in ("0", "1", "2"):
            print("INVALID CHOICE! TRY AGAIN!")
            continue

        player = int(player)
        computer = random.randint(0, 2)

        print("\nYOU CHOSE:")
        print(choices[player])

        print("\nCOMPUTER CHOSE:")
        print(choices[computer])

        if player == computer:
            print("IT'S A TIE! GO AGAIN!")

        elif (player == 0 and computer == 2) or \
             (player == 1 and computer == 0) or \
             (player == 2 and computer == 1):
            print("YOU WIN THIS ROUND!")
            player_score += 1

        else:
            print("COMPUTER WINS THIS ROUND!")
            computer_score += 1

        print(f"SCORE: YOU {player_score} | COMPUTER {computer_score}")

    if player_score == 2:
        print("\nYOU WON THE MATCH!")
        player_matches += 1
    else:
        print("\nCOMPUTER WON THE MATCH!")
        computer_matches += 1

    if match < 3:
        input("\nBULLSHIT! REMATCH! PRESS ENTER!")

print("\n========== FINAL RESULTS ==========")
print(f"YOU: {player_matches} MATCHES")
print(f"COMPUTER: {computer_matches} MATCHES")

if player_matches > computer_matches:
    print("YOU ARE THE ROCK, PAPER, SCISSORS CHAMPION!")
else:
    print("THE COMPUTER IS THE CHAMPION! BETTER LUCK NEXT TIME!")

input("\nPRESS ENTER TO CLOSE THE GAME...")
