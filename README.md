# ConnectFour-AI-Based-Game

Connect Four is a deterministic board game. We create a strategic AI model for this game. We used minimax algorithm and heuristic function to improve our strategie.

                                  **Minimax Search Tree**

![alt text](https://github.com/newsteps8/ConnectFour-AI-Based-Game/blob/main/minimaxtree.png)



heuristic 1, heuristic 2, and heuristic 3 Explanation
--------------------------------------
**evaluation heuristic 1(AI1):** For AI (maximizing player), we thought it an advantage to have a lot of
sequential double and triple groups of their pieces. That's why 10 points were added to the score for
each group of doubles. 1000 points were added to the score for each group of three. For the
minimizing player, 10 points were subtracted from the score for each group of doubles and 1000
points were subtracted from the score for each group of three.


**evaluation heuristic 2(AI2):** As a result of our research, we learned that it is an advantage to start the
game from the columns in the middle in the Connect Four game and to collect the player's pieces
there during the game to win the game. For this reason, we have given different values to the
squares on the board depending on whether it is in the middle or in the corner. For AI, we tried the
approach of adding extra points to score according to the position of the pieces and subtracting the
opponent's points from score. Again, as with other heuristics, we thought it was an advantage to
have a large number of consecutive pairs and three tracks for AI (maximizing player). Thus, 10 points
were added to the score for each group doubles. 1000 points were added to the score for each
group of three. For the minimizing player, 10 points were subtracted from the score for each group
of doubles, and 1000 points were subtracted from the score for all three groups. Additionally,
100000 points have been added to the score for cases where AI pieces are consecutive quads. When
the same situation was found in the opponent player, 100000 points were subtracted from the
score.


**evaluation heuristic 3(AI3):** For AI (maximizing player), we thought it an advantage to have a lot of
sequential double and triple groups of their pieces. That's why 10 points were added to the score for
each group of doubles. 1000 points were added to the score for each group of three. For the
minimizing player, 10 points were subtracted from the score for each group of doubles and 1000
points were subtracted from the score for each group of three. In addition, 100000 points were 
added to the score for cases where AI's pieces were in consecutive quadruples. When the same
situation was found in the opposing player, 100000 points were subtracted from the score.

Finally, A2 has the best heuristic method. Won the games against AI1 and AI3. He eventually played
AI2 with the human player. And AI2 won most games against us.

