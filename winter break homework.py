# # zamtris davaleba
import random
#
def get_user_choice():
    print("Enter your choice (rock, paper, or scissors):")
    user_choice = input().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please choose rock, paper, or scissors.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()





# def get_user_choice(player_number):
#     print(f"Player {player_number}, enter your choice (rock, paper, or scissors):")
#     user_choice = input().lower()
#     while user_choice not in ["rock", "paper", "scissors"]:
#         print("Invalid choice, please choose rock, paper, or scissors.")
#         user_choice = input().lower()
#     return user_choice
#
# def determine_winner(player1_choice, player2_choice):
#     if player1_choice == player2_choice:
#         return "It's a tie!"
#     elif (player1_choice == "rock" and player2_choice == "scissors") or \
#          (player1_choice == "paper" and player2_choice == "rock") or \
#          (player1_choice == "scissors" and player2_choice == "paper"):
#         return "Player 1 wins!"
#     else:
#         return "Player 2 wins!"
#
# def play_game():
#     player1_choice = get_user_choice(1)
#     player2_choice = get_user_choice(2)
#     print(f"Player 1 chose: {player1_choice}")
#     print(f"Player 2 chose: {player2_choice}")
#     result = determine_winner(player1_choice, player2_choice)
#     print(result)
#
# if __name__ == "__main__":
#     play_game()
