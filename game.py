import tkinter as tk
import random as rnd

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Game: Guess the number")
        
        self.secret_number = rnd.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(master, text="Guess the number from 1 to 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Check", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            if guess < 1 or guess > 100:
                self.result_label.config(text="Enter a number from 1 to 100.")
            elif guess < self.secret_number:
                self.result_label.config(text="Too low! Try again!.")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} tries!")
                self.reset_game()
                
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def reset_game(self):
        self.secret_number = rnd.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
