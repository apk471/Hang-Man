import random
import hangman_words
import hangman_art

print(hangman_art.logo)


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
stages.reverse()

selected_word = random.choice(hangman_words.word_list)
tempWord = selected_word
selected_list = list(selected_word)

qussed_word = []
for i in range(len(selected_word)):
    qussed_word.append("_")
print(qussed_word)


try:

    tries = 0
    while tries <= 7:
        user_guess = input("Enter a letter in lowercase: ")
        user_guess = user_guess.lower()

        if len(user_guess) > 1:
            print("Please enter a single character and not more than 1 character ........")
            continue
        if user_guess in qussed_word:
            print("You already have gussed this word please select some other alphabet ...... ")
            continue

        right_choice = 0
        for i in range(len(selected_word)):
            char = selected_word[i]
            if char == user_guess:
                position = selected_word.find(user_guess)
                qussed_word[position] = char
                selected_word = selected_word[:position] + "_" + selected_word[position + 1:]
                print(qussed_word)
                right_choice += 1

        if right_choice > 0:
            right_choice -= selected_word.count(user_guess)
            print(right_choice)
        else:
            print(stages[tries])
            tries += 1
        
        if "_" not in qussed_word:
            print("You won")
            print("Thank you for playing this game ......")
            break
except:
    print("You lost")
    print(f"The final word was {tempWord}")
    print("Thank you for playing this game ....... ")








