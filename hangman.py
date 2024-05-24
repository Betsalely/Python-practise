import time
import random 

recent = ''
stringLength = 0
letters = []
lives = 8

def hangman():
    with open('wordlist.txt', 'r') as f:
        strings_list = f.read().splitlines()

    random_string = random.choice(strings_list)

    letters = [char for char in random_string.lower()]
    under = underscores(random_string)
    letterinput(random_string, under)
    
    
def underscores(string):
    under = ''
    for letter in string:
        under += '___ '
    print(under)
    stringLength = len(under) // 4  # Use integer division to get the number of letters
    return under

def updateUnderscores(letter, word, under):
    global recent  # Declare recent as a global variable
    updated_under = ''
    for i, char in enumerate(word):
        if char == letter:
            updated_under += char + ' '
        else:
            updated_under += under[i*2:i*2+1] + ' '  # Keep the underscore or whitespace
    print(updated_under)
    recent = updated_under
    return updated_under

def letterinput(word, under):
    global recent 
    global lives 
    while '_' in under and lives > 0: 
        guess = input('What letter would you like to guess? \n')
        if guess == '':
            print('thats an empty string')
            print('lives left: '+str(lives))
            under = updateUnderscores(guess, word, under)
        elif guess in word:
            print('lives left: '+str(lives))
            under = updateUnderscores(guess, word, under)
        else:
            print("Incorrect guess! Try again.")
            lives -= 1
            print('lives left: '+str(lives))
            print(recent)


    print("Congratulations! You finished the game!")
    print('\n \n')
    play_again = input('play again? y/n: ')
    if play_again == 'y':
        recent = ''
        stringLength = 0
        letters = []
        lives = 8
        hangman()
    


hangman()







# name = input('What is your name? \n')
# print('Welcome, ' + name + ', to Hangman by Yair')
# time.sleep(1)

# answer = input('Are you ready to start? (yes/no) \n')

# if answer.lower() == 'yes':
#         print('Sweet! Here comes your word.')
#         time.sleep(0.5)
#         hangman()
# else:
#         print('Too bad. We\'re doing it anyway.')
#         time.sleep(0.5)
#         hangman()


