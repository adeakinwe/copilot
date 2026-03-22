import unittest
from unittest.mock import patch
import sys
import os

# Add the current directory to the path so we can import rockpaperscissors
sys.path.insert(0, os.path.dirname(__file__))

from rockpaperscissors import get_user_choice, get_computer_choice, determine_winner

class TestRockPaperScissors(unittest.TestCase):

    def test_get_computer_choice(self):
        """Test that get_computer_choice returns a valid choice."""
        choices = ['rock', 'paper', 'scissors']
        # Test multiple times due to randomness
        for _ in range(100):
            result = get_computer_choice()
            self.assertIn(result, choices)

    def test_determine_winner_tie(self):
        """Test tie scenarios."""
        self.assertEqual(determine_winner('rock', 'rock'), "It's a tie!")
        self.assertEqual(determine_winner('paper', 'paper'), "It's a tie!")
        self.assertEqual(determine_winner('scissors', 'scissors'), "It's a tie!")

    def test_determine_winner_user_wins(self):
        """Test user win scenarios."""
        self.assertEqual(determine_winner('rock', 'scissors'), "You win!")
        self.assertEqual(determine_winner('paper', 'rock'), "You win!")
        self.assertEqual(determine_winner('scissors', 'paper'), "You win!")

    def test_determine_winner_computer_wins(self):
        """Test computer win scenarios."""
        self.assertEqual(determine_winner('rock', 'paper'), "Computer wins!")
        self.assertEqual(determine_winner('paper', 'scissors'), "Computer wins!")
        self.assertEqual(determine_winner('scissors', 'rock'), "Computer wins!")

    @patch('builtins.input', side_effect=['rock'])
    def test_get_user_choice_valid_first_try(self, mock_input):
        """Test get_user_choice with valid input on first try."""
        result = get_user_choice()
        self.assertEqual(result, 'rock')
        mock_input.assert_called_once_with("Enter your choice (rock, paper, scissors): ")

    @patch('builtins.input', side_effect=['invalid', 'paper'])
    def test_get_user_choice_invalid_then_valid(self, mock_input):
        """Test get_user_choice with invalid input first, then valid."""
        result = get_user_choice()
        self.assertEqual(result, 'paper')
        self.assertEqual(mock_input.call_count, 2)

if __name__ == '__main__':
    unittest.main()