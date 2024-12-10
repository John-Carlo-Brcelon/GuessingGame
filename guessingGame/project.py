import tkinter as tk
from tkinter import messagebox
import random
import time

# Word bank for each difficulty level
word_bank = {
    "Easy": ["cat", "dog", "fish", "bird", "car", "bus", "apple", "ball", "milk", "tree"],
    "Intermediate": ["horse", "table", "piano", "plant", "chair", "grapes", "flower", "bread", "ocean", "river"],
    "Hard": ["jacket", "rocket", "castle", "forest", "puzzle", "helmet", "island", "tunnel", "ladder", "engine"],
    "Difficult": ["complex", "journey", "rhythm", "python", "galaxy", "diamond", "quartz", "mystery", "plasma", "vacuum"]
}

class WordGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")
        self.root.geometry("900x700")
        self.root.configure(bg="blue")
        self.total_score = 0
        self.current_word = ""
        self.template = ""
        self.level = ""
        self.words = []
        self.attempts = 5
        self.start_time = 0
        self.score = 0
        self.word_index = 0
        self.time_expired = False

        # Splash screen
        self.splash_screen()

    def splash_screen(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg="blue")
        frame.pack(expand=True)

        tk.Label(frame, text="Word Guessing Game", font=("Helvetica", 36), bg="blue", fg="white").pack(pady=20)

        self.root.after(2000, self.main_menu)

    def main_menu(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg="blue")
        frame.pack(expand=True)

        tk.Label(frame, text="Word Guessing Game", font=("Helvetica", 24), bg="blue", fg="white").pack(pady=30)

        tk.Button(
            frame, text="Start", command=self.choose_level,
            bg="#00008B", fg="white", font=("Helvetica", 14), width=20, height=2
        ).pack(pady=10)

        tk.Button(
            frame, text="Exit", command=self.root.quit,
            bg="#00008B", fg="white", font=("Helvetica", 14), width=20, height=2
        ).pack(pady=10)

    def choose_level(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg="blue")
        frame.pack(expand=True)

        tk.Label(
            frame, text="Choose a difficulty level:", font=("Helvetica", 18), bg="blue", fg="white"
        ).pack(pady=20)

        for level in ["Easy", "Intermediate", "Hard", "Difficult"]:
            tk.Button(
                frame, text=level, command=lambda l=level: self.start_level(l),
                bg="#00008B", fg="white", font=("Helvetica", 14), width=20, height=2
            ).pack(pady=10)

        tk.Button(
            frame, text="Back", command=self.main_menu,
            bg="#00008B", fg="white", font=("Helvetica", 14), width=20, height=2
        ).pack(pady=10)

    def start_level(self, level_name):
        self.clear_frame()
        self.level = level_name
        self.words = word_bank[level_name][:]  # Make a copy of the word list
        self.score = 0
        self.word_index = 0
        self.time_expired = False
        
        # Set time limit based on difficulty level
        if level_name == "Easy":
            self.time_limit = 25
        elif level_name == "Intermediate":
            self.time_limit = 20
        elif level_name == "Hard":
            self.time_limit = 15
        elif level_name == "Difficult":
            self.time_limit = 10
        
        self.next_word()

    def next_word(self):
        if self.word_index >= 10:
            self.show_score()
            return

        self.current_word = random.choice(self.words)
        self.words.remove(self.current_word)
        self.template = self.generate_template(self.current_word)
        self.attempts = 5
        self.start_time = time.time()
        self.word_index += 1
        self.time_expired = False

        self.show_word()

    def show_word(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg="blue")
        frame.pack(expand=True)

        tk.Label(frame, text=f"Level: {self.level}", font=("Helvetica", 16), bg="blue", fg="white").pack(pady=10)
        tk.Label(frame, text=f"Word {self.word_index}/10", font=("Helvetica", 16), bg="blue", fg="white").pack(pady=10)
        tk.Label(frame, text=self.template, font=("Helvetica", 24), bg="blue", fg="white").pack(pady=20)

        self.timer_label = tk.Label(frame, text=f"Time remaining: {self.time_limit} seconds", font=("Helvetica", 16), bg="blue", fg="white")
        self.timer_label.pack(pady=10)

        self.guess_entry = tk.Entry(frame, font=("Helvetica", 18), width=30, justify="center")
        self.guess_entry.pack(pady=20)
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        tk.Button(
            frame, text="Submit", command=self.check_guess,
            bg="#00008B", fg="white", font=("Helvetica", 14), width=20, height=2
        ).pack(pady=10)

        self.update_timer()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, self.time_limit - int(elapsed_time))
        self.timer_label.config(text=f"Time remaining: {remaining_time} seconds")

        if remaining_time > 0 and self.attempts > 0 and not self.time_expired:
            self.root.after(1000, self.update_timer)
        elif remaining_time <= 0 and not self.time_expired:
            self.time_expired = True
            messagebox.showinfo("Time's up!", f"Time's up! The correct word was '{self.current_word}'.")
            self.next_word()

    def check_guess(self):
        guess = self.guess_entry.get().strip().lower()
        if not guess:
            return

        self.guess_entry.delete(0, tk.END)

        if guess == self.current_word:
            messagebox.showinfo("Correct!", f"Your guess is correct! The word was '{self.current_word}'.")
            self.score += 1
            self.next_word()
        else:
            self.attempts -= 1
            if self.attempts > 0:
                messagebox.showwarning("Wrong!", f"Wrong guess! You have {self.attempts} attempts remaining.")
            else:
                messagebox.showinfo("Out of Attempts", f"You ran out of attempts! The correct word was '{self.current_word}'.")
                self.next_word()

    def generate_template(self, word):
        revealed = random.sample(range(len(word)), max(1, len(word) // 2))
        return ''.join([word[i] if i in revealed else '_' for i in range(len(word))])

    def show_score(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg="blue")
        frame.pack(expand=True)

        tk.Label(frame, text=f"Score: {self.score}/10", font=("Helvetica", 20), bg="blue", fg="white").pack(pady=30)
        tk.Button(
            frame, text="Back to Main Menu", command=self.main_menu,
            bg="#00008B", fg="white", font=("Helvetica", 14), width=20, height=2
        ).pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = WordGuessingGame(root)
    root.mainloop()
