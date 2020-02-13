# CS4341-Project 1

Connect-N AlphaBeta Minimax search
Blake Dobay, Dan Duff, Andrew Levy

Introduction:
-The goal of this project is to create an AI agent for the game connect N. Connect N is a more generalized version of the game connect 4 where each player places a tile in a column; stacking on the earlier pieces. A player wins when they stack 4 pieces in vertical or diagonal configurations. The AI uses alpha beta pruning and is limited to fifteen seconds per turn. 

Agent Heuristics:
Our Connect-N A.I. utilizes heuristics which add weights to board evaluations, as well as multipliers for those evaluations. 
The weight heursistc takes the number of consecutive tokens used by the agent, and uses that number as a reference for which predetermined weight value should be used. The weight table is listed below.

``self.weights = [0, 10, 50, 5000, 1000000, 1000000000]``
For example, if a particular 
	
	The last heuristic in the AI is based around the number of consecutive tokens in a row. This heuristic puts more weight when there are more pieces in a row. This allows to AI to play towards higher number of pieces. This is done using a for loop and a counter. The for loop goes through each of the spaces on the board and checks if the current piece is the same as any of the other adjacent pieces. If it is then it increases the in a row counter. 
