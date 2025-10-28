import random
def create_board(size: int = 10) -> list[list[str]]:
    board = [["X" for _ in range(size)] for _ in range(size)]
    return board

def print_board(board: list[list[str]]) -> None:
    for i in board:
        print(i)

def create_game_board(size: int = 10) -> list[list[str]]:
    cards = [str(i) for i in range(1, 51)]
    game_board = []
    lst_temp = []
    for j in range(2):
        for i in cards:
            lst_temp.append(i)
            if len(lst_temp) == 10:
                game_board.append(lst_temp)
                lst_temp = []
    return game_board

def shuffle(game_board: list[list[str]]) -> list[list[str]]:
    for i in range(10000):
        idx1 = random.randint(0, 9)
        idx2 = random.randint(0, 9)
        idx3 = random.randint(0, 9)
        idx4 = random.randint(0, 9)
        while idx1 == idx3 and idx2 == idx4:
            idx1 = random.randint(0, 9)
            idx2 = random.randint(0, 9)
            idx3 = random.randint(0, 9)
            idx4 = random.randint(0, 9)
        game_board[idx1][idx2], game_board[idx3][idx4] = game_board[idx3][idx4], game_board[idx1][idx2]
    return game_board


