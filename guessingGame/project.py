import tkinter as tk
from tkinter import messagebox
import time
import random
import csv

# Save word bank data into CSV file
word_bank = {
    "Easy": {
        "Animals": [
            {"word": "cat", "definition": "A small domesticated carnivorous mammal."},
            {"word": "dog", "definition": "A domesticated carnivorous mammal."},
            {"word": "bird", "definition": "A warm-blooded egg-laying vertebrate with feathers and wings."},
            {"word": "fish", "definition": "A limbless cold-blooded vertebrate animal that lives in water."},
            {"word": "mouse", "definition": "A small rodent typically having a pointed snout."}
        ],
        "Places": [
            {"word": "park", "definition": "A large public green area for recreation."},
            {"word": "mall", "definition": "A large indoor shopping center."},
            {"word": "home", "definition": "The place where one lives."},
            {"word": "lake", "definition": "A large body of water surrounded by land."},
            {"word": "farm", "definition": "An area of land used for growing crops or raising animals."}
        ],
        "Fruits": [
            {"word": "apple", "definition": "A round fruit with red or green skin and a whitish interior."},
            {"word": "pear", "definition": "A sweet, juicy fruit with a rounded base and tapering top."},
            {"word": "kiwi", "definition": "A small, brown, fuzzy fruit with green flesh and black seeds."},
            {"word": "grape", "definition": "A small round fruit, typically green or purple, used to make wine."},
            {"word": "plum", "definition": "A round, smooth-skinned fruit with a pit inside."}
        ],
        "Random": [
            {"word": "ball", "definition": "A spherical object used in various sports."},
            {"word": "book", "definition": "A set of written, printed, or blank pages fastened together."},
            {"word": "pen", "definition": "A writing instrument that uses ink."},
            {"word": "milk", "definition": "A white liquid produced by the mammary glands of female mammals."},
            {"word": "tree", "definition": "A perennial plant with an elongated stem or trunk supporting branches."}
        ]
    },
    "Intermediate": {
        "Animals": [
            {"word": "horse", "definition": "A large domesticated mammal with hooves used for riding and work."},
            {"word": "rabbit", "definition": "A small burrowing mammal with long ears and a short tail."},
            {"word": "panda", "definition": "A large bear-like mammal with distinctive black and white coloring."},
            {"word": "zebra", "definition": "A wild horse with black and white stripes native to Africa."},
            {"word": "koala", "definition": "An Australian tree-dwelling marsupial with gray fur."}
        ],
        "Places": [
            {"word": "river", "definition": "A large natural stream of water flowing to the sea or another body of water."},
            {"word": "beach", "definition": "A sandy shore by the sea."},
            {"word": "forest", "definition": "A large area covered chiefly with trees."},
            {"word": "school", "definition": "A place where students go to learn."},
            {"word": "hotel", "definition": "A building providing lodging, meals, and other services for travelers."}
        ],
        "Fruits": [
            {"word": "mango", "definition": "A tropical stone fruit with a smooth skin and sweet flesh."},
            {"word": "papaya", "definition": "A tropical fruit with a sweet, orange-colored flesh."},
            {"word": "orange", "definition": "A round citrus fruit with a tough skin and sweet-tart flavor."},
            {"word": "banana", "definition": "A long yellow tropical fruit with a soft, sweet flesh."},
            {"word": "peach", "definition": "A round fruit with a fuzzy skin and a large pit inside."}
        ],
        "Random": [
            {"word": "bread", "definition": "A baked food made from flour and water, usually leavened."},
            {"word": "table", "definition": "A piece of furniture with a flat surface for eating, writing, etc."},
            {"word": "piano", "definition": "A large musical instrument with black and white keys."},
            {"word": "cloud", "definition": "A visible mass of condensed water vapor floating in the sky."},
            {"word": "grapes", "definition": "Small round fruits, typically purple or green, used for making wine or eating."}
        ]
    },
    "Hard": {
        "Animals": [
            {"word": "eagle", "definition": "A large bird of prey with a powerful beak and keen eyesight."},
            {"word": "falcon", "definition": "A bird of prey known for its speed and sharp talons."},
            {"word": "otter", "definition": "A carnivorous mammal known for its playful behavior and swimming abilities."},
            {"word": "badger", "definition": "A small mammal with a distinctive white stripe on its face."},
            {"word": "wolf", "definition": "A large carnivorous mammal of the dog family, typically living in packs."}
        ],
        "Places": [
            {"word": "island", "definition": "A piece of land surrounded by water."},
            {"word": "canyon", "definition": "A deep ravine between cliffs, typically carved by a river."},
            {"word": "village", "definition": "A small settlement, typically found in rural areas."},
            {"word": "mountain", "definition": "A large natural elevation of the earth's surface."},
            {"word": "palace", "definition": "A large and impressive residence of a monarch or ruler."}
        ],
        "Fruits": [
            {"word": "pineapple", "definition": "A large tropical fruit with spiky leaves and sweet flesh."},
            {"word": "blueberry", "definition": "A small, round, dark blue fruit with a sweet flavor."},
            {"word": "avocado", "definition": "A green fruit with a creamy texture, often used in salads."},
            {"word": "fig", "definition": "A pear-shaped fruit with a sweet, reddish or purple skin."},
            {"word": "coconut", "definition": "A large, brown fruit with a fibrous outer shell and a white edible interior."}
        ],
        "Random": [
            {"word": "castle", "definition": "A large fortified building or complex, often a residence of royalty."},
            {"word": "rocket", "definition": "A vehicle that uses controlled explosions to propel itself into space."},
            {"word": "ladder", "definition": "A structure with steps used to climb up or down."},
            {"word": "engine", "definition": "A machine designed to convert energy into mechanical power."},
            {"word": "puzzle", "definition": "A game or problem designed to test ingenuity or knowledge."}
        ]
    },
    "Difficult": {
        "Animals": [
            {"word": "platypus", "definition": "A mammal that lays eggs and has the bill of a duck."},
            {"word": "kangaroo", "definition": "A large marsupial from Australia known for its powerful hind legs."},
            {"word": "chameleon", "definition": "A lizard known for its ability to change color to blend in with its environment."},
            {"word": "cheetah", "definition": "A large cat known for its speed, capable of running faster than any other land animal."},
            {"word": "walrus", "definition": "A large marine mammal with tusks and whiskers."}
        ],
        "Places": [
            {"word": "galaxy", "definition": "A large system of stars, gas, and dust held together by gravity."},
            {"word": "desert", "definition": "A barren, dry landscape with little or no vegetation."},
            {"word": "volcano", "definition": "A mountain or hill with a crater through which molten lava, ash, and gases are expelled."},
            {"word": "tundra", "definition": "A cold, treeless biome found in polar regions."},
            {"word": "universe", "definition": "All of space and everything in it, including stars, planets, and galaxies."}
        ],
        "Fruits": [
            {"word": "dragonfruit", "definition": "A tropical fruit with a bright pink or yellow skin and white or red flesh."},
            {"word": "lychee", "definition": "A small, round fruit with a bumpy red rind and sweet, translucent flesh."},
            {"word": "pomegranate", "definition": "A fruit with a tough skin and many juicy seeds inside."},
            {"word": "durian", "definition": "A large, spiky fruit known for its strong odor and creamy, sweet flesh."},
            {"word": "jackfruit", "definition": "A large tropical fruit with green or yellow flesh that is sweet and aromatic."}
        ],
        "Random": [
            {"word": "quartz", "definition": "A hard, crystalline mineral composed of silicon and oxygen."},
            {"word": "vacuum", "definition": "A space with no matter, or a cleaning device that uses suction."},
            {"word": "plasma", "definition": "A state of matter where gases are ionized and electrically conductive."},
            {"word": "mystery", "definition": "Something that is difficult or impossible to understand or explain."},
            {"word": "rhythm", "definition": "A repeated pattern of sounds or movements."}
        ]
    }
}

# Function to save the word bank to CSV
def save_word_bank_to_csv():
    for level, categories in word_bank.items():
        for category, words in categories.items():
            filename = f"{level}_{category}.csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["word", "definition"])
                for word_info in words:
                    writer.writerow([word_info['word'], word_info['definition']])

# Save the word bank to CSV
save_word_bank_to_csv()

class WordGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")
        self.root.geometry("900x700")
        self.root.configure(bg="#6A89CC")
        self.total_score = 0
        self.current_word = ""
        self.current_category = ""
        self.template = ""
        self.level = ""
        self.categories = []
        self.words_by_category = {}
        self.category_index = 0
        self.word_index = 0
        self.attempts = 5
        self.start_time = 0
        self.score = 0
        self.time_expired = False

        # Splash screen
        self.splash_screen()

    def splash_screen(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg="#6A89CC")
        frame.pack(expand=True)

        tk.Label(frame, text="Word Guessing Game", font=("Helvetica", 36, 'bold'), bg="#6A89CC", fg="white").pack(pady=20)

        self.root.after(2000, self.main_menu)

    def main_menu(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg="#6A89CC")
        frame.pack(expand=True)

        tk.Label(frame, text="Word Guessing Game", font=("Helvetica", 24, 'bold'), bg="#6A89CC", fg="white").pack(pady=30)

        tk.Button(
            frame, text="Start", command=self.choose_level,
            bg="#3B83BD", fg="white", font=("Helvetica", 14), width=20, height=2
        ).pack(pady=10)

        tk.Button(
            frame, text="Exit", command=self.root.quit,
            bg="#3B83BD", fg="white", font=("Helvetica", 14), width=20, height=2
        ).pack(pady=10)

    def choose_level(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg="#6A89CC")
        frame.pack(expand=True)

        tk.Label(
            frame, text="Choose a difficulty level:", font=("Helvetica", 18, 'bold'), bg="#6A89CC", fg="white"
        ).pack(pady=20)

        for level in ["Easy", "Intermediate", "Hard", "Difficult"]:
            tk.Button(
                frame, text=level, command=lambda l=level: self.start_level(l),
                bg="#3B83BD", fg="white", font=("Helvetica", 14), width=20, height=2
            ).pack(pady=10)

        tk.Button(
            frame, text="Back", command=self.main_menu,
            bg="#3B83BD", fg="white", font=("Helvetica", 14), width=20, height=2
        ).pack(pady=10)

    def start_level(self, level_name):
        self.clear_frame()
        self.level = level_name

        # Gather words and categories
        categories = word_bank[level_name]
        self.categories = list(categories.keys())
        self.words_by_category = {category: random.sample(words, len(words)) for category, words in categories.items()}
        self.category_index = 0
        self.word_index = 0

        self.score = 0
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
        if self.category_index >= len(self.categories):
            self.show_score()
            return

        current_category = self.categories[self.category_index]
        words = self.words_by_category[current_category]

        if self.word_index >= len(words):
            self.word_index = 0
            self.category_index += 1
            self.next_word()
            return

        self.current_word = words[self.word_index]['word']
        self.current_category = current_category
        self.template = self.generate_template(self.current_word)
        self.attempts = 5
        self.start_time = time.time()
        self.word_index += 1
        self.time_expired = False

        self.show_word()

    def show_word(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg="#6A89CC")
        frame.pack(expand=True)

        # Display level, category, and word information
        tk.Label(frame, text=f"Level: {self.level}", font=("Helvetica", 16), bg="#6A89CC", fg="white").pack(pady=10)
        tk.Label(frame, text=f"Category: {self.current_category}", font=("Helvetica", 16), bg="#6A89CC", fg="white").pack(pady=10)
        tk.Label(frame, text=f"Word {self.word_index}/{len(self.words_by_category[self.current_category])} in Category", font=("Helvetica", 16), bg="#6A89CC", fg="white").pack(pady=10)

        # Display the definition
        definition = self.words_by_category[self.current_category][self.word_index-1]["definition"]
        tk.Label(frame, text=f"Definition: {definition}", font=("Helvetica", 16), bg="#6A89CC", fg="white").pack(pady=10)

        # Create a separate frame for the word template
        word_frame = tk.Frame(frame, bg="#6A89CC")
        word_frame.pack(pady=20)

        # Display each letter or underscore in a separate label
        for char in self.template:
            tk.Label(word_frame, text=char, font=("Helvetica", 24), bg="#6A89CC", fg="white", width=2).pack(side=tk.LEFT, padx=2)

        # Timer and input fields
        self.timer_label = tk.Label(frame, text=f"Time remaining: {self.time_limit} seconds", font=("Helvetica", 16), bg="#6A89CC", fg="white")
        self.timer_label.pack(pady=10)

        self.guess_entry = tk.Entry(frame, font=("Helvetica", 18), width=30, justify="center")
        self.guess_entry.pack(pady=20)
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        tk.Button(frame, text="Submit", command=self.check_guess, bg="#3B83BD", fg="white", font=("Helvetica", 14), width=20, height=2).pack(pady=10)

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

         # Check if the guess contains only alphabetic characters
        if not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please use only alphabet letters.")
            self.guess_entry.delete(0, tk.END)  # Clear the input field
            return

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
        revealed = random.sample(range(len(word)), max(1, len(word) // 3))
        return "".join([word[i] if i in revealed else "_" for i in range(len(word))])

    def show_score(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg="#6A89CC")
        frame.pack(expand=True)

        tk.Label(frame, text="Game Over", font=("Helvetica", 36, 'bold'), bg="#6A89CC", fg="white").pack(pady=20)
        tk.Label(frame, text=f"Your score: {self.score}", font=("Helvetica", 24), bg="#6A89CC", fg="white").pack(pady=20)

    

        tk.Button(frame, text="Back to Main Menu", command=self.main_menu, bg="#3B83BD", fg="white", font=("Helvetica", 14), width=20, height=2).pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = WordGuessingGame(root)
    root.mainloop()

