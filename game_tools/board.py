import random
def create_board(size) -> list[list[str]]:
    board = [["X" for _ in range(size)] for _ in range(size)]
    return board

def print_board(board: list[list[str]]) -> None:
    for i in board:
        print(i)


def shuffle(size) -> list[str]:
    cards = [str(i) for i in range(((size ** 2) // 2) + 1)]
    for i in range(10000):
        idx1 = random.randint(0, len(cards) - 1)
        idx2 = random.randint(0, len(cards) - 1)
        while idx1 == idx2:
            idx1 = random.randint(0, len(cards) - 1)
            idx2 = random.randint(0, len(cards) - 1)
        cards[idx1], cards[idx2] = cards[idx2], cards[idx1]
    return cards


def create_game_board(cards_shuffled, size) -> list[list[str]]:
    game_board = []
    lst_temp = []
    for j in range(2):
        for i in cards_shuffled:
            lst_temp.append(i)
            if len(lst_temp) == size:
                game_board.append(lst_temp)
                lst_temp = []
    return game_board




