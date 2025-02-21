# Simple Python Solitaire Game

## Game Setup

You start with a list of cards, which are all placed in pile 0 to start. The game creates several piles based on the number of cards.

## Game Objective

The goal is to move all cards out of Pile 0, distributing them across the other piles while following specific movement rules.
You win if Pile 0 is empty and only one other pile has all the cards in a valid order.

## Game Rules

1. Moving within pile 0
     * If you move from Pile 0 to Pile 0, the top card moves to the bottom of Pile 0.
2. Moving from Pile 0 to another Pile
     * You can move the top card of Pile 0 to another pile if:
       * The target pile is empty.
       * OR, the top card from Pile 0 is exactly one less than the bottom card of the target pile.
3. Moving from One Pile to Another
     * You can move an entire pile's contents to another pile only if:
       * The top card of the source pile is exactly one less than the bottom card of the target pile.
         If allowed, all cards from the source pile move together.
4. Random Card Addition (pick_random function)
     * Occasionally, a random card (1-10) may be added to the top of Pile 0.

## How to Play

1. The game starts, and you see the piles displayed.
2. Each round, you choose two piles:
    * Move from pile no.: (Enter the pile number you want to move a card from)
    * Move to pile no.: (Enter the pile number where you want to move it)
3. The move happens if it's legal (following the rules above).
4. The game ends when either:
     * You move all cards, and only one pile (excluding Pile 0) has cards (You win).
     * You run out of moves (You lose).

