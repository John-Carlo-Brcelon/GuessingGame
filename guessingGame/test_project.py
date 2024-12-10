import pytest
from unittest import mock
from guessingGame.project import WordGuessingGame  # Assuming the game code is in project.py

# Mock the tkinter root to avoid GUI interactions
@pytest.fixture
def mock_root():
    mock_root = mock.MagicMock()
    mock_root.title = mock.MagicMock()
    mock_root.geometry = mock.MagicMock()
    mock_root.configure = mock.MagicMock()
    return mock_root

# Test the `generate_template` method to ensure it correctly generates word templates
def test_generate_template(mock_root):
    game = WordGuessingGame(mock_root)

    # Test with a word that has multiple letters
    template = game.generate_template("apple")
    assert template == "_p__e"  # Example template output, will vary depending on the word

    # Test with a word that has one letter
    template = game.generate_template("a")
    assert template == "a"

    # Test with an empty word (edge case)
    template = game.generate_template("")
    assert template == ""

    # Test with a long word
    template = game.generate_template("computer")
    assert template != "computer"  # Ensure the template is not the same as the word

# Test the game's next_word method to ensure it handles word selection and template generation correctly
def test_next_word(mock_root):
    game = WordGuessingGame(mock_root)
    game.words = ["apple", "banana", "cherry"]

    game.next_word()  # Simulate moving to the next word

    assert game.current_word in game.words  # Check that the current word is in the word bank
    assert game.template != game.current_word  # Check that a template is generated
    assert game.attempts == 5  # Check that attempts are reset to 5
    assert game.word_index == 1  # Check that word_index increments correctly

# Test the `check_guess` method to ensure it correctly handles correct and incorrect guesses
def test_check_guess(mock_root):
    game = WordGuessingGame(mock_root)
    game.current_word = "apple"
    game.attempts = 3

    # Correct guess
    game.guess_entry = mock.MagicMock()
    game.guess_entry.get.return_value = "apple"
    game.check_guess()
    assert game.score == 1  # Score should increase by 1

    # Incorrect guess
    game.guess_entry.get.return_value = "banana"
    game.check_guess()
    assert game.attempts == 2  # Attempts should decrease by 1
