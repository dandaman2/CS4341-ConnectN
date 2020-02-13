# CS4341-Project 1

Connect-N AlphaBeta Minimax search
Blake Dobay, Dan Duff, Andrew Levy

Introduction:
-The goal of this project is to create an AI agent for the game connect N. Connect N is a more generalized version of the game connect 4 where each player places a tile in a column; stacking on the earlier pieces. A player wins when they stack 4 pieces in vertical or diagonal configurations. The AI uses alpha beta pruning and is limited to fifteen seconds per turn. 

Alpha-Beta Pruning:
Alpha–beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. This particular bot seeks to maximize it's score through iterative maximizing and minimizing of player score, predicting up to 4 moves ahead of any one given board state. In evaluating these states, may can be "pruned" preemptively; a process which short-circuits evaluations of states which cannot possibly result in a value better than the current minimum or maximum. An example of this would be the evaluation of a board state which consists of an opponent win state (a scenario which doesn't need to be eavlauted any further, as the main player will lose no matter what the rest of the board contains). 

Agent Heuristics:
Our Connect-N A.I. utilizes heuristics which add weights to board evaluations, as well as multipliers for those evaluations. 
The weight heursistc takes the number of consecutive tokens used by the agent, and uses that number as a reference for which predetermined weight value should be used. The weight table is listed below.

`self.weights = [0, 10, 50, 5000, 1000000, 1000000000]`

For example, if a particular board configuration has 3 consecutive player tokens, that board state would we evaluated at 5000. With this heuristic implemented, the value of board states scale almost exponentially, leading to 3-in-a-rows being valued much higher than 5 instances of 2-in-a-row. This ensures that the agent will always value longer sequences more than mulitple instances of shorter sequences. 
If the N input of the game is larger than the size of the weight array, then additional values will be added to the list of weights (with new values being multiplied by 1000 for each additional weight added). All of these values were determined via crude trial-and-error testing. 

In addition to weight values affecting board state evaluations, an additional overall multiplier called *defensiveness* effects all board states. This multiplier increases the opponent's score on a board state, ultimately causing the A.I. to select moves which deterement opponents moreso than themselves.

`self.defensiveness = .65`

Similar to the list of weights, the *defensiveness* number was obtained through numerous trial-and-error testing. 
As a result, the overall score of a board state is determined by the following code segment:

`score_diff = (1-self.defensiveness)*player_scores[0] - self.defensiveness*player_scores[1]`

This takes the difference of the two player's scores on the baord state, factoring in weights and defense heuristics. 
This differential value is then retruned to the calling min/max function as a terminal node value. 
