# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
Figuring out who won the game was the hardest because it's easy to miss one.

2. Explain how you would add a computer player to the game.

Have a method to suggest a move, and then have a wrapper that asks the user and then asks the computer.


3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

There's a way to always win or at least tie in tic-tac-toe, so just do that. I think you just need to have a method to figure out which spots block the other player.