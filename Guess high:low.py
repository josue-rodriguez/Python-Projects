# random number game:
import random

def intro():
    print("Hi, welcome to the guessing game.\n")
    print("The goal of the game is to correctly guess a number chosen at random between 1 and 100 in the least amount of guesses.\n")
    print("After each guess you will get a hint as to whether your guess was greater or less than the chosen number.\n")
    
def guessing_game():
    intro()
    
    game = random.randint(1, 100)
    count = 1
    
    while True:
        try: 
            guess = int(input("Plese enter a guess: "))
            break
        except ValueError:
            print("I'm sorry, that is not a valid number. Please try again.\n")
            count += 1
    
    if guess == game and count == 1:
        print("Congratulations! You guessed right on the first try, you lucky bastard.")
        
    elif guess == game and count > 1:
         print("You finally got it right! It only took you %s tries" % (str(count)))
         
    else:
        while guess != game:
            if guess < game:
                choices = ['Guess higher, asshole.', 'Aim higher. In life.', 'Just a bit higher.']
                choices = str(random.choice(choices))
                print("{0}\n".format(choices))
            else:
                choices = ['Guess lower, asshole.', 'You aimed low. In life.', 'Just a bit lower.']
                choices = str(random.choice(choices))
                print("{0}\n".format(choices))
            
            while True:
                try: 
                    guess = int(input("Plese enter a guess: "))
                    break
                except ValueError:
                    print("I'm sorry, that is not a valid number. Please try again.\n")
            count += 1

        print("You finally got it right! It only took you %s tries" % (str(count)))

guessing_game()
    