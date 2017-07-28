import random
import itertools

roundNum = 1
gamescore = 100

while roundNum <= 5:

    """creating the deck"""
    deck = []
    for i in range(4):
        deck.append(['h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'hJ', 'hQ', 'hK', 'hA'])

    for i in range(0, len(deck[1])):
        deck[1][i] = deck[1][i].replace('h', 's')
        deck[2][i] = deck[2][i].replace('h', 'c')
        deck[3][i] = deck[3][i].replace('h', 'd')

    deck = list(itertools.chain.from_iterable(deck))

    """1st things 1st (i'm the realest)"""
    print('Round ' + str(roundNum))
    round_value = 0

    """ 1st card """
    card1 = random.choice(deck)
    if card1[1] in ['J', 'Q', 'K']:
        round_value += 10
    elif card1[1] == 'A':
        round_value += 1
    else:
        round_value += int(card1[1])
    print('You drew {}'.format(card1))
    deck.remove(card1)

    """2nd card"""
    card2 = random.choice(deck)
    if card2[1] in ['J', 'Q', 'K']:
        round_value += 10
    elif card2[1] == 'A':
        round_value += 1
    else:
        round_value += int(card2[1])
    print('You drew {}'.format(card2))
    deck.remove(card2)

    """ All other cards """
    while True:
        draw = input('\nDraw another card? (y/n): ')
        print()
        if draw[0].lower() == 'y':
            card3 = random.choice(deck)
            if card3[1] in ['J', 'Q', 'K']:
                round_value += 10
            elif card3[1] == 'A':
                round_value += 1
            else:
                round_value += int(card3[1])
            print('You drew {}'.format(card3))
            deck.remove(card3)
        else:
            break
        if round_value > 21:
            print('You busted!')
            print(gamescore)
            break

    """getting round totals"""
    if round_value > 21:
        diff = 21
    else:
        diff = 21 - round_value

    gamescore -= diff

    print('Your score is: {}'.format(gamescore))
    print()
    roundNum += 1

print('you received a {}%'.format(gamescore))
