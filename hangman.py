import time
import random 



def hangman():
    with open('wordlist.txt', 'r') as f:
        strings_list = f.read().splitlines()

    random_string = random.choice(strings_list)
    def underscores(string):

        under = ''
        for letter in string:
            under+= '_'
        print(under)
    underscores(random_string)
    

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


