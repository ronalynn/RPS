import random

# Print welcome and rules
def play_rps():
    print("Welcome to Rock, Paper, Scissors!")
    print("The rules are as follows:")
    print("Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\n")

    choices = ['Rock', 'Paper', 'Scissors']
    player_point_counter = 0
    computer_point_counter = 0

    # Prompt user for number of rounds, repeating until a valid input is received
    while True:
        num_rounds = int(input("How many rounds would you like to play? (Max: 10): "))
        if num_rounds > 0 and num_rounds <= 10:
            print(f"We're playing {num_rounds} rounds! Good Luck ;)\n")
            break
        else:
            print("You have entered an invalid number of rounds!\n")

    # Main game loop
    for round in range(1, num_rounds + 1):
        print(f"\nRound: {round}\n")
        
        while True:
            print("These are your choices:")
            print("\tRock\n\tPaper\n\tScissors")
            player_choice = input("Enter your choice: ").strip().capitalize()  # Convert input to title case
            
            if player_choice in choices:
                break
            else:
                print('You have entered an invalid choice!')
        
        # Computer choice
        computer_choice = random.choice(choices)
        print(f'I choose: {computer_choice}')

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
                (player_choice == 'scissors' and computer_choice == 'paper') or \
                (player_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            player_point_counter += 1
        else:
            print("Computer wins this round!")
            computer_point_counter += 1

    # Display final results
    print("\nFINAL SCORE:")
    print(f"You: {player_point_counter}  Computer: {computer_point_counter}")
    if player_point_counter > computer_point_counter:
        print("You won! Congratulations!")
    elif computer_point_counter > player_point_counter:
        print("I WON!!!!!!")
    else:
        print("We both won!")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        print()
        play_rps()
    else:
        print("\nThank you for playing!")

# Start the game
play_rps()


