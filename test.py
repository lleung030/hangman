from hangman import Hangman
import unittest

class HangmanGame(unittest.TestCase):
    
    def test_True(self):
        hangman = Hangman('man')
        # hangman.select_word()
        self.assertTrue('Peter', hangman.guessed)
        
    def test_assertNotIn(self):
        hangman = Hangman('man')
        # hangman.select_word()
        self.assertNotIn('Lucas', hangman.guessed)
        
    # def test_assertFalse(self):
    #     hangman = Hangman('man')
    #     # hangman.select_word()
    #     self.assertFalse('Lucas', hangman.guessed)
    
    def test_raise(self):
        hangman = Hangman('man')
        # hangman.select_word()
        self.assertRaises(Exception, hangman.select_word, 'Peter', hangman.guessed)
        
     
unittest.main()