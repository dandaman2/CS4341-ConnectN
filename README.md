# CS4341-Project 1

Connect-N AlphaBeta Minimax search
Blake Dobay, Dan Duff, Andrew Levy

## Introduction:
-The goal of this project is to create an AI agent for the game connect N. Connect N is a more generalized version of the game connect 4 where each player places a tile in a column; stacking on the earlier pieces. A player wins when they stack 4 pieces in vertical or diagonal configurations. The AI uses alpha beta pruning and is limited to fifteen seconds per turn. 

## Alpha-Beta Pruning:
-Alpha–beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. This particular bot seeks to maximize it's score through iterative maximizing and minimizing of player score, predicting up to 4 moves ahead of any one given board state. In evaluating these states, may can be "pruned" preemptively; a process which short-circuits evaluations of states which cannot possibly result in a value better than the current minimum or maximum. An example of this would be the evaluation of a board state which consists of an opponent win state (a scenario which doesn't need to be eavlauted any further, as the main player will lose no matter what the rest of the board contains). 

## Minimize and Maximize Functions:
The board evaluation function is nested within the ``maximize`` and ``minimize`` functions of the min-max alpha-beta algorithm provided by the lecture. Initially, the agent seeks to maximize the score of a particular board state (as determined by the evaluation function), and then anticipate a minimization of the next board state - representing the opponent's move. This process continues to an input depth (determined in class instantiation, but is usually 4) or until a win/loss state is detected. Once these criteria are met, the board state is evaluated in one of three ways:

+ If the given state has the player winning: return ```math.inf``` if maximizing, ```-math.inf``` if minimizing
+ If the given state has the player losing: return ```-math.inf``` if maximizing, ```math.inf``` if minimizing 
+ If the depth has been reached, evaluate the board by summing the board's state of all 1-N "in-a-row" secquences of the player and the opponent's tokens. They are valued more highly depending on the heuristic weights, and are altered by defensiveness, however ultimately the score that is returned is the difference between the opponent's and the player's token sequence evaluation. 



## Testing Agents:
The different agents were tested by running several different games of a basic game of Connect 4 with each combination of agents playing against each other. This way it could be tested if all of the agents actually worked properly and could win a game without performing an illegal move (such as placing a token in an illegal column) or breaking the program. Once all of the agents were tested for simple functionality, the number of rows, columns, and tokens in a row were changed and then tested. Since the game needs to be connect N with any possible number as N, it was important to make sure that the agents could work with any number of tokens to win. After a dynamic board was tested, the alpha-beta agent was tested. In order to ensure that this agent was as efficient as possible, it had to be tested many times to try to find the best possible AI to win games of connect N. This was tested by using trial-and-error methods, which resulted in exponeitally-increasing values. These larger values resulted in more logical decision-making; priotizing longer sequences of consecutive tokens over multiple instances of smaller sequences. 

Another important finding from the testing of this agent was that sometimes the agent would be looking too far ahead and would make a move for the future when it could just win immediately. A big change that was made to solve this problem was by adding a method that checks if the AI is one token away from a win and then make that move if it existed.
	
Finally, defensiveness was also tested via trial-and-error, however it seemed necessary to implement so as to have the A.I. consider the opponent's moves more heavily. This would prevent the A.I. from being too overconfident, and force it to select moves which determent the opponent's score moreso than increase it's own; essentially prioritizing surivial over aggressiveness. 


## Agent Heuristics:
-Our Connect-N A.I. utilizes heuristics which add weights to board evaluations, as well as multipliers for those evaluations. 
The weight heursistc takes the number of consecutive tokens used by the agent, and uses that number as a reference for which predetermined weight value should be used. The weight table is listed below.

```self.weights = [0, 10, 50, 5000, 1000000, 1000000000]```

For example, if a particular board configuration has 3 consecutive player tokens, that board state would we evaluated at 5000. With this heuristic implemented, the value of board states scale almost exponentially, leading to 3-in-a-rows being valued much higher than 5 instances of 2-in-a-row. This ensures that the agent will always value longer sequences more than mulitple instances of shorter sequences. 

If the N input of the game is larger than the size of the weight array, then additional values will be added to the list of weights (with new values being multiplied by 1000 for each additional weight added). All of these values were determined via crude trial-and-error testing. 

In addition to weight values affecting board state evaluations, an additional overall multiplier called *defensiveness* effects all board states. This multiplier increases the opponent's score on a board state, ultimately causing the A.I. to select moves which lower opponents moreso than themselves.

```self.defensiveness = .65```

Similar to the list of weights, the *defensiveness* number was obtained through numerous trial-and-error testing. 
As a result, the overall score of a board state is determined by the following code segment:

```score_diff = (1-self.defensiveness)*player_scores[0] - self.defensiveness*player_scores[1]```

This takes the difference of the two player's scores on the baord state, factoring in weights and defense heuristics. 
This differential value is then retruned to the calling min/max function as a terminal node value. 


## Improvements to the Agent
If we had more time to work on the agent, we would likely have more time to fine-tune the heuristic score weights and defensiveness multiplier. This could potentially be done via a genetic algorithm, wherein different varieties of defensiveness and score weights could be tested and modified to become more advantageous throughout mulitple tournaments. The heuristic values would likely be the genes in such an algorithm, and a crossover would take the two most-effective (highest win rate) agents, and produce a hybrid combination consisting of some of both parent's genotypes. 
