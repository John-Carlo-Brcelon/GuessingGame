import pytest
import os
import time
import random
from tkinter import Tk, Label, Entry
from io import StringIO
from project import WordGuessingGame  # Assuming your game code is in word_guessing_game.py

@pytest.fixture
def setup_game():
    root = Tk()
    game = WordGuessingGame(root)
    yield game
    root.quit()

def test_generate_template(setup_game):
    game = setup_game
    word = "banana"
    template = game.generate_template(word)
    revealed_chars = [c for c in template if c != "_"]
    assert len(revealed_chars) >= 2  # At least 1/3 of the word should be revealed
    assert all(c in word for c in revealed_chars)  # All revealed chars must be in the word

def test_check_guess_correct(setup_game):
    game = setup_game
    game.current_word = "apple"
    game.attempts = 3
    guess = "apple"
    
    # Check if correct guess increments score
    game.check_guess()
    assert game.score == 1  # Score should increase by 1
    assert game.attempts == 3  # Attempts should remain unchanged

def test_check_guess_wrong(setup_game):
    game = setup_game
    game.current_word = "apple"
    game.attempts = 3
    guess = "orange"
    
    # Check if wrong guess reduces attempts
    game.check_guess()
    assert game.attempts == 2  # Attempts should decrease by 1

def test_save_word_bank_to_csv():
    game = setup_game
    game.save_word_bank_to_csv()
    
    for level in ["Easy", "Intermediate", "Hard", "Difficult"]:
        for category in ["Animals", "Places", "Fruits", "Random"]:
            filename = f"{level}_{category}.csv"
            assert os.path.exists(filename)
            
            with open(filename, "r") as file:
                lines = file.readlines()
                assert len(lines) > 1  # There should be more than just the header line

def test_game_over_score(setup_game):
    game = setup_game
    game.score = 10
    
    # Simulate game over scenario
    game.show_score()
    
    # Check if the score is displayed correctly
    assert "Your score: 10" in game.root.winfo_children()[0].cget("text")

def test_timer_update(setup_game):
    game = setup_game
    game.start_time = time.time()
    game.time_limit = 10
    game.update_timer()
    
    # Check if timer updates without error (it's harder to assert exact time because of sleep)
    time.sleep(1)
    elapsed_time = time.time() - game.start_time
    assert elapsed_time >= 1  # At least 1 second should have passed

@pytest.mark.parametrize("word, expected_template_length", [
    ("banana", 6), 
    ("apple", 5),
    ("orange", 6)
])
def test_generate_template_length(setup_game, word, expected_template_length):
    game = setup_game
    template = game.generate_template(word)
    assert len(template) == expected_template_length  # Template length should match word length
