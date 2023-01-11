
from collections import namedtuple


Node = namedtuple("Node", "board_hor board_ver square_onwer depth is_last_hor lastI lastJ")

def getInitialNode(n:int, m:int):
    return Node(
        [[0 for j in range(n-1)] for i in range(n)],
        [[0 for j in range(n)] for i in range(n-1)],
        [[0 for j in range(n)] for i in range(n)],
        2*(n-1)*n,
        None,
        None,
        None
    )

def isTerminalNode(node: Node) -> bool:
    return node.depth == 0

def getNodeValue(node:Node) -> int:
    n = len(node.square_onwer)
    return sum([sum([node.square_onwer[i][j] for j in range(n)]) for i in range(n)])*100

def make_move(node: Node, isHor:bool, row:int, col:int, isMax:bool) -> Node:
    return None
