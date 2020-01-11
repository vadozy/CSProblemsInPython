from minimax import find_best_move
from connectfour import C4Board
from board import Move, Board
from time import sleep
from typing import Tuple

board: Board = C4Board()


def computer_play(board: Board, search_depth: int = 5) -> Tuple[bool, Board]:
    end_of_game: bool = False

    computer_move: Move = find_best_move(board, search_depth)
    print(f"Computer move is {computer_move}")
    board = board.move(computer_move)
    print(board)
    if board.is_win:
        print(f"{board.turn.opposite} wins!")
        end_of_game = True
    elif board.is_draw:
        print("Draw!")
        end_of_game = True
    return end_of_game, board


if __name__ == "__main__":
    # main game loop
    end_of_game: bool = False
    while True:
        end_of_game, board = computer_play(board, 4)
        if end_of_game:
            break
        end_of_game, board = computer_play(board, 4)
        if end_of_game:
            break
        # sleep(2)
