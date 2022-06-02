#Python Script for rock paper scissors game
import random # Import required python module
print("\nThe Rock-Paper-Scissors Game!!!\n\n")
game_name = input('Enter a game name:  ').title()
print(f'\nHello {game_name}...\n Let\'s Play!' )
game_rules = """
Rock wins against scissors;
Paper wins against rock; and 
Scissors wins against paper.\n

Options : 
'R' - For Rock
'P' - For Paper
'S' - For Scissors\n
"""
count =  0
while count == 0:
    print(game_rules)
    print('Pick any of the options....R or P or S')
    options = ['R', 'P', 'S']
    choice_option = input("Input an Option: ").upper()
    computer = random.choice(options)
    if computer == 'R' and choice_option == 'S':
        print(f'{game_name}({choice_option}):Computer({computer})')
        print('Computer Wins!')
        count +=1
    elif computer == 'S' and choice_option == 'R':
        print(f'{game_name}({choice_option}):Computer({computer})')
        print(f'{game_name} Wins!')
        count +=1
    elif computer == 'P' and choice_option == 'R':
        print(f'{game_name}({choice_option}):Computer({computer})')
        print(f'Computer Wins!')
        count +=1
    elif computer == 'R' and choice_option == 'P':
        print(f'{game_name}({choice_option}):Computer({computer})')
        print(f'{game_name} Wins!')
        count +=1
    elif computer == 'S' and choice_option == 'P':
        print(f'{game_name}({choice_option}):Computer({computer})')
        print(f'Computer Wins!')
        count +=1
    elif computer == 'P' and choice_option == 'S':
        print(f'{game_name}({choice_option}):Computer({computer})')
        print(f'{game_name} Wins!')
        count +=1
    elif computer == choice_option:
        print('It\'s a tie....Play Again!')
    else:
        print('Please enter a valid option...')

print('\nGame Ends!')