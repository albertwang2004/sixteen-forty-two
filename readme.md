# 16.42 
### v0.1

This is a trainer for guessing the missing card in a deck of cards. The game is implemented in Python and can be played by running the `game.py` file with

```python game.py```

## Rules

16.42 is a game to be played with a group of any number of people, but preferably between 1 and 14. Your goal is to minimize the time it takes to guess the card correctly, accounting for the number of people present.

At the beginning of the game, a standard deck of cards is shuffled, and the bottom card is removed. Your job is to view all of the other cards one at a time, and guess what this bottom card is.

You may only use whatever you can do with your body, including but not limited to counting on your fingers, memorizing values, and communicating with your team. That means no writing down digits, using calculators, etc.

## Installation

You will need the `pygame` module, which can be simply installed by running

```pip install pygame```

## Changelog

### v0.1

Added simple visual interface

### Initial v0.0
All but one of the 52 cards will be dealt in sequence, printed to console output.

Before running the game, make sure you have the `keyboard` module installed. You can install it using the following command:

```pip install keyboard```