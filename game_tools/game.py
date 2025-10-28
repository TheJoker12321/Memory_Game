from game_tools.board import *
import logging


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
def data():
    data_game = {
        "board": create_board(),
        "game_board": shuffle(create_game_board()),
        "Face up cards": 0,
        "mistakes": 0
    }
    return data_game

def range_x(x: int, size: int = 10) -> bool:
    return 0 < x < size

def range_y(y: int, size: int = 10) -> bool:
    return 0 < y < size

def choose_range():
       x = int(input("choose row between 1 - 10: ")) - 1
       y = int(input("choose column between 1 - 10: ")) - 1
       while not range_x(x) or not range_y(y):
           print("try again: ")
           x = int(input("choose row between 1 - 10: ")) - 1
           y = int(input("choose column between 1 - 10: ")) - 1
       return x , y

def game_over(board: list[list[str]]) -> bool:
    count = 0
    for i in board:
        if "X" in i:
            count += 1
    if count == 0:
        return True
    return False

def init_game(data_game):
    print_board(data_game["board"])
    while not game_over(data_game["board"]):
        choose1 = choose_range()
        print("choose one more card: ")
        choose2 = choose_range()
        if data_game["game_board"][choose1[0]][choose1[1]] == data_game["game_board"][choose2[0]][choose2[1]]:
            data_game["board"][choose1[0]][choose1[1]] = data_game["game_board"][choose1[0]][choose1[1]]
            data_game["board"][choose2[0]][choose2[1]] = data_game["game_board"][choose2[0]][choose2[1]]
            print_board(data_game["board"])
            logging.info(f"you found the card: {data_game["board"][choose2[0]][choose2[1]]}")
            data_game["Face up cards"] += 1
        else:
            data_game["board"][choose1[0]][choose1[1]] = data_game["game_board"][choose1[0]][choose1[1]]
            data_game["board"][choose2[0]][choose2[1]] = data_game["game_board"][choose2[0]][choose2[1]]
            print_board(data_game["board"])
            data_game["board"][choose1[0]][choose1[1]] = "X"
            data_game["board"][choose2[0]][choose2[1]] = "X"
            data_game["mistakes"] += 1
            print("these cards are not the same...")
            logging.info("you wrong")
            print_board(data_game["board"])

    print(f"you finished the game_tools.  your mistakes are: {data_game["mistakes"]}")
    logging.info("finished the game_tools!")






