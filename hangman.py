import random 

class Hangman():
    def __init__(self,name):
        self.name = name
        self.word_list = ['Peter', 'James', 'John', 'Andrew', 'Bartholomew', 'Jude', 'Matthew', 'Philip', 'Simon', 'Thomas', 'Paul']
        self.used = []
        self.guessed = []
        
        
    def select_word(self):
        tries = 7
        word = (random.choice(self.word_list))
        word_enumerate = list(enumerate(word))
        word_empty = "_ " * len(word)
        print (word_empty)
        
        done = False
        
        while not done:
            print('')
            print('')
            guess = input('Guess a letter: ').lower()
            if guess not in self.used:
                self.used.append(guess.lower())
#                 self.guessed.append(guess.lower())
#                 print(f"Letters used in word bank: {self.guessed}")
                
            
                
                for letter in word:
                    if letter.lower() in self.used:
                        print(letter, end = ' ')
                        
                    
                    elif letter.lower() not in self.used:
                        print('_', end = ' ')
                
                if guess not in word:
                    self.guessed.append(guess.lower())
                    tries = 7 - len(self.guessed)
                    
                    #check
                    if tries == 0:
                        print('')
                        print(f'Sorry! You lost! Your word was {word}')
                        break
                    #check
                    
                print(f"Letters used in word bank: {self.guessed}")
                print(f'You have {tries} tries left.')
                
            
            else:
                print(f'"{guess}" is already used. Try again.')
                #already in word bank 
                

                    
    
        
#         done = True 
#         for letter in word:
#             if letter.lower() not in guess:
#                 done = False
        

hangman = Hangman('hangman')
hangman.select_word()