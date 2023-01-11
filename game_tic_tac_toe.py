from tic_tac_toe_utils import *
from solver import *

def play_turn(cur_node, remaining_moves, is_auto, is_max):
    if is_auto:
        res = minimax_search(
            cur_node,
            min(remaining_moves, 9),
            is_max,
            False,
            isTerminalNode,
            getNodeValue,
            getSuccessors
        )
        cur_node = res.node
        remaining_moves-=1
        return (cur_node, remaining_moves)
    else:
        print("Input Row: ", end="")
        row = int(input())
        print("Input Col: ", end="")
        col = int(input())
        cur_node = make_move(cur_node, row, col, is_max)
        remaining_moves-=1
        return (cur_node, remaining_moves)

def play_tic_tac_toe(initial_node):
    print_node(initial_node, 3)
    print("INPUT GAMEMODE: \n(0=player_vs_player, 1=player_vs_computer, 2=computer_vs_player, 3=computer_vs_computer): ")
    gamemode_n = int(input())
    p1_auto = (gamemode_n//2)%2
    p2_auto = gamemode_n%2

    cur_node = initial_node
    remaining_moves = initial_node.depth

    while remaining_moves > 0:
        print("Player 1 turn: ", "Computer" if p1_auto else "Human")
        (cur_node, remaining_moves) = play_turn(cur_node, remaining_moves, p1_auto, True)

        print_node(cur_node, 3)
        if has_winner(cur_node) != 0:
            print("Player 1 wins")
            return
        
        if remaining_moves == 0:
            break
        
        print("Player 2 turn: ", "Computer" if p2_auto else "Human")
        (cur_node, remaining_moves) = play_turn(cur_node, remaining_moves, p2_auto, False)

        print_node(cur_node, 3)
        if has_winner(cur_node) != 0:
            print("Player 2 wins")
            return

    print("DRAW")

print("Input initial node")
initial_node = getInitialNode(3)
# for i in range(3):
#     for j in range(3):
#         initial_node.board[i][j] = int(input())

initial_node = Node([[],[],[]], 7, None, None)
initial_node.board[0] = [1, 0, 0]
initial_node.board[1] = [0, -1, 0]
initial_node.board[2] = [0, 0, 0]
play_tic_tac_toe(
    initial_node)