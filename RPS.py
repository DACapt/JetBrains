import random

def get_game_logic(options):
  choices = {}
  for option in options:
    win_list, lose_list = get_win_lose(options, option)
    choices[option] = {'win': win_list, 'lose':lose_list}
  return choices 


def get_win_lose(options, option):

  option_index = options.index(option)
  win_lose = options[option_index + 1:] + options[:option_index]
  lose_list = win_lose[:len(win_lose) // 2]
  win_list = win_lose[len(win_lose) // 2:]

  return [win_list, lose_list]

# Write your code here
choices = {'rock':{'win': 'scissors', 'lose': 'paper', 'draw': 'rock'},
            'paper': {'win': 'rock', 'lose': 'scissors', 'draw': 'paper'},
            'scissors': {'win': 'paper', 'lose': 'rock', 'draw': 'scissors'}}
possible_choices = ['rock', 'paper', 'scissors', '!exit', '!rating']
computer_choices = ['rock', 'paper', 'scissors']

ratings = {}
with open('rating.txt', 'r') as file:
    for line in file:
        name, rating = line.split()
        ratings[name] = int(rating)

user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

if user_name not in ratings:
    ratings[user_name] = 0

more_choices = input()

if more_choices:
    more_choices = list(more_choices.split(','))
    choices = get_game_logic(more_choices)
    computer_choices = more_choices
    possible_choices = more_choices
    
print("Okay, let's start")
while True:
    
    user_choice = input()
    if user_choice not in possible_choices and user_choice not in ['!exit','!rating']:
        print("invalid input")
        continue
        
    computer_choice = random.choice(computer_choices)

    if user_choice == '!exit':
        print("Bye!")
        break
    elif user_choice == '!rating':
        print(f"Your rating: {ratings[user_name]}")
    elif computer_choice in choices[user_choice]['win']:
        print(f"Well done. The computer chose {computer_choice} and failed")
        ratings[user_name] += 100
    elif computer_choice in choices[user_choice]['lose']:
        print(f"Sorry, but the computer chose {computer_choice}")
    elif computer_choice == user_choice:
        ratings[user_name] += 50
        print(f"There is a draw ({computer_choice})")
    else:
        print("reached end if")
