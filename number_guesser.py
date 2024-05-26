import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingApp:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing App")

        self.label = tk.Label(master, text="Welcome to the Number Guessing App!")
        self.label.pack()

        self.pick_number_label = tk.Label(master, text="Pick a number between 1 and 99.")
        self.pick_number_label.pack()

        self.play_button = tk.Button(master, text="Play", command=self.start_guessing_game)
        self.play_button.pack()

    def start_guessing_game(self):
        self.play_button.config(state="disabled")
        messagebox.showinfo("Rules", "Here are the rules:\n"
                                      "1. I get 10 guesses to get your number.\n"
                                      "2. You can't lie at any point.\n"
                                      "3. If I got it correct you lose.")

        self.upper_limit = 99
        self.lower_limit = 1

        for _ in range(10):
            number = random.randint(self.lower_limit, self.upper_limit)
            guess = messagebox.askquestion("Guess", f"Is your number {number}?")

            if guess == 'yes':
                result = messagebox.askquestion("Win", "I knew it! I win! Play again?")
                if result == 'yes':
                    self.start_guessing_game()
                else:
                    break
            elif guess == 'no':
                response = messagebox.askquestion("Response", "Was I too high?")
                if response == 'yes':
                    self.upper_limit = number - 1
                else:
                    self.lower_limit = number + 1
            else:
                messagebox.showerror("Error", "Invalid input. Please enter 'L' for lower, 'H' for higher, or 'Win' if I'm correct.")
        else:
            messagebox.showinfo("Lost", "I couldn't guess your number within 8 tries. You win!")
            result = messagebox.askquestion("Play again", "Do you want to play again?")
            if result == 'yes':
                self.start_guessing_game()

def main():
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
