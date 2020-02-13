# CS4341-Project 1

Connect-N AlphaBeta Minimax search
Blake Dobay, Dan Duff, Andrew Levy

Introduction:
	The goal of this project is to create an AI agent for the game connect N. Connect N is a more generalized version of the game connect 4 where each player places a tile in a column; stacking on the earlier pieces. A player wins when they stack 4 pieces in vertical or diagonal configurations. The AI uses alpha beta pruning and is limited to fifteen seconds per turn. 

Agent Heuristics:
	Our groups A.I. agent has multiple heuristics that assist it. One of the simplest heuristics is to check whether or not the AI is one turn away from winning. This heuristic ensures that the AI wins when it can instead of playing extra moves that does not win it the game. To do this the program loops through each of the next board states and if any of them result in an AI win then it returns the move. The code for this heuristic is shown below. 



	






Another heuristic that was added to the AI is named defensiveness. Defensiveness is a weight that leads the AI to play more defensive mover instead of being more aggressive. This weight can be adjusted before it is used in evaluating a move (as shown in the code below).

As seen in the code above the defensiveness weight is multiplied by the score of the move.

	The last heuristic in the AI is based around the number of consecutive tokens in a row. This heuristic puts more weight when there are more pieces in a row. This allows to AI to play towards higher number of pieces. This is done using a for loop and a counter. The for loop goes through each of the spaces on the board and checks if the current piece is the same as any of the other adjacent pieces. If it is then it increases the in a row counter. 
