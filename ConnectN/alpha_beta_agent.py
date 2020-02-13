import math
import agent

###########################
# Alpha-Beta Search Agent #
###########################

class AlphaBetaAgent(agent.Agent):
    """Agent that uses alpha-beta search"""

    # Class constructor.
    #
    # PARAM [string] name:      the name of this player
    # PARAM [int]    max_depth: the maximum search depth
    def __init__(self, name, max_depth):
        super().__init__(name)
        # Max search depth
        self.max_depth = max_depth
        self.weights = [0, 10, 50, 5000, 1000000, 1000000000]  # the weight table to process board state evaluations
        self.defensiveness = .65  # a heuristic modifier that makes the bot prefer defensive play over offensive play

    # Pick a column.
    #
    # PARAM [board.Board] brd: the current board state
    # RETURN [int]: the column where the token must be added
    #
    # NOTE: make sure the column is legal, or you'll lose the game.
    def go(self, brd):
        """Search for the best move (choice of column for the token)"""
        # Your code here
        # print("[[-----------------GO-----------------------]]")
        depth = -self.max_depth  # start with negative depth. Once depth is 0, then return board states as terminal node
        alpha = -math.inf
        beta = math.inf

        weight_len = len(self.weights)
        if brd.n > weight_len-1:  # add additional weight heuristics for larger n
            for i in range(weight_len, brd.n+1):
                self.weights.append(1000*max(self.weights))

        # print(self.weights)
        # check to see if AI can win next move
        one_away_res = self.__one_away(brd)
        if one_away_res[0]:
            return one_away_res[1]  # if it can win in one particular action, return that action
        # AI seeks to maximize. Start with -inf and inf bounds initially
        utility, action = self.__maximize(brd, depth, alpha, beta)
        if action < 0 or action > brd.h:
            print('outta action bounds---------------')
            return abs(action % brd.h)
        return action

    # returns a boolean and an action (tuple) if the AI can win next turn
    def __one_away(self, board_state):
        for state, action in self.get_successors(board_state):
            if state.get_outcome() == board_state.player:
                return True, action
        return False, -1

    # Returns the max value, and its associated action with pruning (from lecture)
    def __maximize(self, board_state, depth, alpha, beta):
        win_state = board_state.get_outcome()
        if win_state == board_state.player:
            return math.inf, -1
        elif win_state != 0:  # opponent wins
            return -math.inf, -1
        if len(board_state.free_cols()) == 0:
            return 0, -1
        if depth >= 0:  # depth reached, return value as terminal node
            next_player = board_state.player
            utility = self.__evaluate_score(board_state, next_player)
            return utility, -1
        else:
            val = (-math.inf, -1)  # best value
            for state, action in self.get_successors(board_state):
                new_val = self.__minimize(state, depth+1, alpha, beta)
                #print("New Val is", new_val)
                if new_val >= val[0]:
                    val = new_val, action

                if val[0] >= beta:
                    return val

                alpha = max(alpha, val[0])

        return val

    # Returns the min value, and its associated action with pruning (from lecture)
    def __minimize(self, board_state, depth, alpha, beta):
        win_state = board_state.get_outcome()
        if win_state == board_state.player:
            return -math.inf
        elif win_state != 0:  # opponent wins
            return math.inf
        if len(board_state.free_cols()) == 0:
            return 0
        if depth >= 0:  # depth reached, return value as terminal node
            next_player = board_state.player
            utility = self.__evaluate_score(board_state, next_player)
            return utility
        else:
            val = math.inf  # worst value
            for state, action in self.get_successors(board_state):
                new_val, action = self.__maximize(state, depth + 1, alpha, beta)
                val = min(new_val, val)

                if val <= alpha:
                    return val

                beta = min(beta, val)

        return val

    # the utility function which evaluates the overall gain/loss from a particular board state
    def __evaluate_score(self, board_state, player):
        player_scores = [0, 0]  # initialize with 0, 0 scores for the two players
        for dx, dy in [(1, 0), (1, 1), (0, 1), (1, -1)]:  # iterate through all directions
            for i in range(board_state.h):
                for j in range(board_state.w):  # check all board spots
                    cur_token = board_state.board[i][j]
                    num_inarow = 1 if cur_token == player else 0 #!=0
                    next_i = i
                    next_j = j
                    for step in range(board_state.n):  # counter for how many of a given token are in a row
                        next_i += dx
                        next_j += dy
                        # out of bounds check
                        if next_i >= board_state.h or next_i < 0 or next_j >= board_state.w or next_j < 0:
                            num_inarow = 0
                            break
                        next_token = board_state.board[next_i][next_j]
                        if cur_token == 0 and next_token > 0:
                            # reset num_inarow if new non-empty spot found
                            cur_token = next_token
                            num_inarow = 1
                        elif cur_token != next_token:
                            if next_token == 0:  # if next cell is empty, advance check to next position
                                continue
                            # Different player tokens in a row, num_inarow has thus ended prematurely
                            num_inarow = 0
                            break
                        else:
                            if cur_token > 0:
                                num_inarow += 1
                    # add to score based on number of consecutive tokens and weight heuristic
                    player_scores[cur_token-1] += self.weights[num_inarow]
        # score is difference in board state value (with defensiveness included)
        score_diff = (1-self.defensiveness)*player_scores[0] - self.defensiveness*player_scores[1]
        return score_diff if player == 1 else -1*score_diff

    def get_successors(self, brd):
        """Returns the reachable boards from the given board brd. The return value is a tuple (new board state, column number where last token was added)."""
        # Get possible actions
        freecols = brd.free_cols()
        # Are there legal actions left?
        if not freecols:
            return []
        # Make a list of the new boards along with the corresponding actions
        succ = []
        for col in freecols:
            # Clone the original board
            nb = brd.copy()
            # Add a token to the new board
            # (This internally changes nb.player, check the method definition!)
            nb.add_token(col)
            # Add board to list of successors
            succ.append((nb,col))
        return succ


THE_AGENT = AlphaBetaAgent("Group08", 4)
