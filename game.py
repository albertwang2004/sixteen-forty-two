import random
import sys, getpass
import keyboard


def raw_input2(value="",end=""):
    sys.stdout.write(value)
    data = getpass.getpass("")
    sys.stdout.write(data)
    sys.stdout.write(end)
    return data

cards = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
suits = ['♠', '♣', '♦', '♥']

# make a deck and shuffle it
deck = []
for card in cards[1:]:
    for suit in suits:
        deck.append(card + suit)
random.shuffle(deck)

# remove the last card
answer = deck.pop()

# display each number while erasing the last one, hitting enter to deal next card
for card in deck:
    print(card)
    keyboard.wait('space')
    print("\033[F\033[K", end="") # erase last line

print("Guess the card! (space to see answer)")
keyboard.wait('space')
print(answer)