import random

rock = 'r'
scissors = 's'
paper = 'p'
emojis = { rock: '🪨', paper: '📃', scissors: '✂️',} 
choices = ('r', 'p', 's') # read-only list 
# choices = ['r', 'p', 's']
def play_game():
  while True:
    user_choice = get_user_choice()

    opponent_choice = random.choice(choices)

    display_choices(user_choice, opponent_choice)

    determine_winner(user_choice, opponent_choice)

    should_continue = input('Continue? (y/n): ').lower()

    if should_continue == 'n':
      break

def get_user_choice():
  name = input("Hello! What's your name? ")
  print(f'Welcome, {name}!' )
  while True:
    user_choice = input('rock, paper, or scissors? (r/p/s): ').lower()
    if user_choice in choices: # check if in list
      return user_choice      
    else:
      print('Invalid choice!')
      
def display_choices(user_choice, opponent_choice):
  print(f'You chose {emojis[user_choice]}')
  print(f'Opponent chose {emojis[opponent_choice]}')


def determine_winner(user_choice, opponent_choice):
  if user_choice == opponent_choice:
    print('Tie!')
  elif (
    (user_choice == rock and opponent_choice == scissors) or 
    (user_choice == scissors and opponent_choice == paper) or 
    (user_choice == paper and opponent_choice == rock)):
    print('You win!')
  else:
    print('You lose!')  



play_game()