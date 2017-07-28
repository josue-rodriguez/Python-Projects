import time
import random


def magic_eight():
    question = input("What do you desire to know? Careful what you wish for. ")
    print(question)
    print("...Peering into the future. Please hold.")
    time.sleep(5)
    num = random.randint(1, 20)
    if num == 1:
        print('Signs point to yes')
    elif num == 2:
        print('Better not to tell you now.')
    elif num == 3:
        print('It is certain.')
    elif num == 4:
        print('It is decidedly so.')
    elif num == 5:
        print('Without a doubt.')
    elif num == 6:
        print('Yes, definitely.')
    elif num == 7:
        print('You may rely on it')
    elif num == 8:
        print('As I see it, yes')
    elif num == 9:
        print('Most likely.')
    elif num == 10:
        print('Outlook good.')
    elif num == 11:
        print('Yes')
    elif num == 12:
        print('Reply hazy, try again')
    elif num == 13:
        print('Ask again later.')
    elif num == 14:
        print('Cannot predict now.')
    elif num == 15:
        print('Concentrate, and try again.')
    elif num == 16:
        print("Don't count on it.")
    elif num == 17:
        print('My sources say no.')
    elif num == 18:
        print('Outlook not so good.')
    elif num == 19:
        print('Very doubtful.')
    else:
        print('No.')

    quit = input('Ask another question, or enter q to quit: )
    quit.lower()
    if quit == 'q' or quit == 'quit':
        print('Come again soon.')
    else:
        magic_eight()

magic_eight()
