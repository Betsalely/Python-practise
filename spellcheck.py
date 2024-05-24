# import difflib

# #this gets all the words form wordlisty.txt when its called
# def read_wordlist(filename):
#     with open(filename, 'r') as file:
#         words = [line.strip() for line in file]
#     return words

# #gets 3 words
# def suggest_corrections(word, dictionary):
#     matches = difflib.get_close_matches(word, dictionary, n=5)
#     matches.sort(key=lambda x: (x != 'thy', difflib.SequenceMatcher(None, word, x).ratio()), reverse=True)
    
#     return matches


# def main():
#     #this calls that first function which gets the words
#     dictionary = read_wordlist("wordlist.txt")
#     print("Dictionary created successfully.")

#     while True:
#         word = input("Enter a sentence (or 'quit' to exit): ")
        
#         if word.lower() == "quit":
#             print("Goodbye!")
#             break

       
#         if word.lower() in dictionary:
#             print("No spelling errors found.")
#         else:
#             corrections = suggest_corrections(word, dictionary)
#             if corrections:
#                 print("Did you mean one of these words?")
#                 for i, suggestion in enumerate(corrections, start=1):
#                     print(f"{i}. {suggestion}")
#             else:
#                 print("No suggestions found.")


# main()






# import difflib

# #this gets all the words form wordlisty.txt when its called
# def read_wordlist(filename):
#     with open(filename, 'r') as file:
#         words = [line.strip() for line in file]
#     return words

# #gets 3 words
# def suggest_corrections(word, dictionary):
#     matches = difflib.get_close_matches(word, dictionary, n=5)
#     matches.sort(key=lambda x: (x != 'dug', x != 'thy',x != 'mousy', x != 'blur', x!= 'tyre', difflib.SequenceMatcher(None, word, x).ratio()), reverse=True)
#     return matches

# def main():
#     dictionary = read_wordlist("wordlist.txt")
#     print("Dictionary created successfully.")
#     corrections_num = 0
#     while True:
#         sentence = input("Enter a sentence (or 'quit' to exit): ")
#         sentence = sentence.lower()
#         if sentence == "quit":
#             print("Goodbye!")
#             break

#         words = sentence.split()  
#         corrected_sentence = [] 
#         for word in words:
#             if word.lower() in dictionary:
#                 corrected_sentence.append(word)  
#             else:
#                 corrections = suggest_corrections(word, dictionary)
#                 if corrections:
#                     corrected_sentence.append(corrections[corrections_num])  
                    
#                 else:
#                     corrected_sentence.append(word)  
        
#         print("Corrected sentence:", " ".join(corrected_sentence))
#         def trier():
#             redo = input('is this the sentence you were looking for? answer yes or no: ')
#             if redo.lower() == 'no':
             
#                 corrections_num+=1
#                 print('Just put in your original sentence but now add the words tje previous guess got correct')
#             elif redo.lower() == 'yes':
#                 print('sweet you now have a fully spellchecked sentence')
#             else:
#                 print('incorrect answer, please write yes or no')
#                 trier()
#         trier()


# main()

import difflib
sentence = ''
def read_wordlist(filename):
    with open(filename, 'r') as file:
        words = [line.strip() for line in file]
    return words

def suggest_corrections(word, dictionary, start_index=0, num_suggestions=7):
    matches = difflib.get_close_matches(word, dictionary, n=start_index + num_suggestions)
    matches.sort(key=lambda x: difflib.SequenceMatcher(None, word, x).ratio(), reverse=True)
    return matches[start_index:start_index + num_suggestions]

def get_user_input():
    while True:
        sentence = input("Enter a sentence (or 'quit' to exit): ").lower()
        if sentence == "quit":
            print("Goodbye!")
            exit()
        elif sentence.strip():
            return sentence
        else:
            print("Please enter a valid sentence.")

def correct_sentence(sentence, dictionary):
    corrected_sentence = []
    for word in sentence.split():
        if word in dictionary:
            corrected_sentence.append(word)
        else:
            corrections = suggest_corrections(word, dictionary)
            if corrections:
                corrected_sentence.append(choose_correction(word, corrections))
            else:
                corrected_sentence.append(word)
    return " ".join(corrected_sentence)

def choose_correction(word, corrections):
    print(f"Suggestions for '{word}':")
    for i, correction in enumerate(corrections, start=1):
        print(f"{i}. {correction}")
    print("8. Next five suggestions")
    while True:
        print(sentence)
        choice = input("Choose a correction (1-6), or enter '0' to skip: ")
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice <= 8:
                return corrections[choice - 1] if choice > 0 else word
        print("Invalid choice. Please enter a number between 1 and 8, or '0' to skip.")

def main():
    dictionary = read_wordlist("wordlist.txt")
    print("Dictionary created successfully.")
    
    while True:
        sentence = get_user_input()
        corrected_sentence = correct_sentence(sentence, dictionary)
        print("Corrected sentence:", corrected_sentence)
        if sentence != corrected_sentence:
            print("Would you like to retry?")
            if input("Enter 'yes' to retry or anything else to exit: ").lower() != 'yes':
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()

