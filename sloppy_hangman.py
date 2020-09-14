import random
import string
# Write your code here
print("H A N G M A N\n")

while True: 
    play_input = input('Type "play" to play the game, "exit" to quit: ')
    if play_input != 'play':
        break
    winning_words = ["python", "java", "kotlin", "javascript"]
    winning_word = random.choice(winning_words)

    remaining_lives = 8

    winning_word_list = list(winning_word)
    guess_letters_list = list('-' * len(winning_word))
    winning_letters = set(winning_word)
    guess_letters = set(guess_letters_list)

    while remaining_lives != 0:
        print("\n")
        print(''.join(guess_letters_list))
        if guess_letters_list == winning_word_list:
            print("""You guessed the word!
            You survived!""")
            break
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should input a single letter")
            continue
        elif not guess.islower():
            print("It is not an ASCII lowercase letter")
            continue
        else:
            if guess in guess_letters:
                print("You already typed this letter")
            elif guess in winning_letters:
                for _ in range(winning_word_list.count(guess)):
                    guess_letters_list[winning_word_list.index(guess)] = guess
                    winning_word_list[winning_word_list.index(guess)] = '-'
                    guess_letters.add(guess)
            else:
                guess_letters.add(guess)
                print("No such letter in the word")
                remaining_lives -= 1
    else:
        print("You are hanged!")
