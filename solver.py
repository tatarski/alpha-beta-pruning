
import math
import os
from tic_tac_toe_utils import *
c = 0
SearchRes = namedtuple("SearchRes", "node value sol_depth")
def minimax_search(
    initial_node: Node, initial_depth: int, isMaxFirst:bool, doPruning: bool,
    isTerminalNode, getNodeValue, getSuccessors) -> SearchRes:
    def minimax(node: Node, depth:int, alpha, beta, isMax:bool) -> SearchRes:
        global c
        c+=1
        # Return current node heuristic value when:
        #  depth is reached 
        #  or node is terminal(no more turns can be played)
        if depth == 0 or isTerminalNode(node):
            return SearchRes(node, getNodeValue(node, initial_depth, isMax), depth)

        if isMax:
            max_res = SearchRes(None, -math.inf, 0)
            succ = getSuccessors(node, isMax)
            for child in succ:
                res = minimax(child, depth-1, alpha, beta, not isMax)
                if res.value > max_res.value:
                    max_res = SearchRes(child, res.value, res.sol_depth)
                if doPruning:
                    alpha = max(res.value, alpha)
                    if alpha >= beta:
                        break

            return max_res 

        if not isMax:
            min_res = SearchRes(None, math.inf, 0)
            succ = getSuccessors(node, isMax)
            for child in succ:
                res = minimax(child, depth-1, alpha, beta, not isMax)
                if res.value < min_res.value:
                    min_res = SearchRes(child, res.value, res.sol_depth)

                if doPruning:
                    beta = min(res.value, beta)
                    if alpha >= beta:
                        break

            return min_res 

        return SearchRes(None, 0, 0)

    return minimax(
        initial_node,
        initial_depth,
        -math.inf,
        math.inf,
        isMaxFirst
    )