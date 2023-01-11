from collections import namedtuple
import math

Node = namedtuple("Node", "board depth last_row last_col")

def getInitialNode(n):
    return Node(
        [[0 for j in range(n)] for i in range(n)],
        n*n,
        None, None
    )

def isTerminalNode(node: Node):
    return node.depth == 0 or has_winner(node) != 0


def has_winner(node: Node):
    n = len(node.board)

    # Rows
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum += node.board[i][j]
        if sum == n:
            return 10
        if sum == -n:
            return -10
    
    # Cols 
    for j in range(0, n):
        sum = 0
        for i in range(0, n):
            sum += node.board[i][j]
        if sum == n:
            return 10
        if sum == -n:
            return -10
    
    # Diag 1
    sum = 0
    for k in range(0, n):
        sum += node.board[k][k]
    if sum == n:
        return 10
    if sum == -n:
        return -10
    # Diag 2
    sum = 0
    for k in range(0, n):
        sum += node.board[n - 1 - k][k]
    if sum == n:
        return 10
    if sum == -n:
        return -10
    
    return 0


def getNodeValue(node: Node, initial_depth, isMax):
    # Node value is 0 if game resulted in draw
    if has_winner(node) == 0:
        return 0

    n = len(node.board)
    # Utility function to compute value of row/column/diagonal
    # Based on number of Xs and Os on current row/column/diagonal
    # Only Rows, columns or diagonals where only a single player has played have nonzero value
    def selectStreakValue(countA, countB):
        if countA == 4 and countB == 0:
            return 10000
        if countB == 4 and countA == 0:
            return -10000
        if countA == 3 and countB == 0:
            return 10000
        if countB == 3 and countA == 0:
            return -10000
        if countA == 2 and countB == 0:
            return 100
        if countB == 2 and countA == 0:
            return -100
        if countA == 1 and countB == 0:
            return 1
        if countB == 1 and countA == 0:
            return -1
        return 0
    
    # Count number of Xs and Os on each Row/ Column/ Diagonal
    # Sum all of the 
    val = 0
    for i in range(n):
        count_A = 0
        count_B = 0
        # Rows
        for j in range(n):
            if node.board[i][j] == 1:
                count_A+=1
            elif node.board[i][j] == -1:
                count_B+=1
        val += selectStreakValue(count_A, count_B)
        count_A = 0
        count_B = 0
        # Columns
        for j in range(n):
            if node.board[j][i] == 1:
                count_A+=1
            elif node.board[j][i] == -1:
                count_B+=1
        val += selectStreakValue(count_A, count_B)

    # Diag 1
    count_A = 0
    count_B = 0
    for k in range(n):
        if node.board[k][k] == 1:
            count_A+=1
        elif node.board[k][k] == -1:
            count_B+=1
    val += selectStreakValue(count_A, count_B)

    # Diag 2
    count_A = 0
    count_B = 0
    for k in range(n):
        if node.board[n-1-k][k] == 1:
            count_A+=1
        elif node.board[n-1-k][k] == -1:
            count_B+=1
    val += selectStreakValue(count_A, count_B)
    
    # Number of empty squares left
    # Leaf nodes that have more empty squares left are closer to root node
    num_empty = sum([1 if node.board[i][j] == 0 else 0 for i in range(n) for j in range(n)])

    # Value of quick losses should be much lower for losing player
    # Value of quick wins should be much higher for winning player
    sign = -1 if isMax else 1
    # Sign is reversed because eval function is called for leaf nodes where:
    # - max played last move; eval is called when min should be playing
    #   or
    # - min played last move; eval is called when max should be playing

    return val + sign*num_empty*pow(10, n-1)

# print(getNodeValue(Node(
#     [[0, 0, 1],
#     [0, -1, 1],
#     [0, 0, 1]],
#     0,
#     None,
#     None
# )))

def make_move(node:Node, I:int, J:int, isMax:bool) -> Node:
    n = len(node.board)
    val = 1 if isMax else -1
    return Node(
        [[node.board[i][j] if i!=I or J!=j else val for j in range(n)] for i in range(n)],
        node.depth-1,
        I, J
    )

def getSuccessors(node: Node, isMax:bool):
    n = len(node.board)
    return [make_move(node, i, j, isMax) for i in range(n) for j in range(n) if node.board[i][j] == 0]


def print_node(node:Node, d):
    n = len(node.board)
    print("REMAINING MOVES",node.depth)
    # print("VAL", getNodeValue(node, 0, 0))
    print("PLACED ON:", node.last_row, node.last_col)
    for i in range(n):
        for k in range(d):
            print(" ", end="")
        for j in range(n):
            if node.board[i][j] == 0:
                print("-", end="")
            elif node.board[i][j] == 1:
                print("X", end="")
            else:
                print("O", end="")
        print("")
    print("")