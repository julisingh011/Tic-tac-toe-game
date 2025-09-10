def show_scoreboard(scoreboard):
    print("\t----------------------------------------------------")
    print("\t   The SCORECARD for TIC TAC TOE Python game        ")
    print("\t----------------------------------------------------")
    for k, v in scoreboard.items():
        print("\t   ", k, "\t   ", v)
    print("\t----------------------------------------------------")


def showgrid(value):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(value[0], value[1], value[2]))
    print('\t_____|_____|_________')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(value[3], value[4], value[5]))
    print('\t_____|_____|_________')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(value[6], value[7], value[8]))
    print("\t     |     |")


def draw_validate(player_position):
    if len(player_position["X"]) + len(player_position["O"]) == 9:
        return True
    return False


def win_validate(player_position, symbol):
    win_combs = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                 [1, 4, 7], [2, 5, 8], [3, 6, 9],
                 [1, 5, 9], [3, 5, 7]]
    for cmb in win_combs:
        if all([j in player_position[symbol] for j in cmb]):
            return True
    return False


def game_single(symbol):
    value = [" " for _ in range(9)]
    player_position = {'X': [], 'O': []}

    while True:
        showgrid(value)
        print(f" {symbol} choose position to occupy (1-9):")
        try:
            chc = int(input())
        except ValueError:
            print("Invalid input. Enter a number (1-9).")
            continue

        if chc < 1 or chc > 9:
            print("Invalid position. Try again.")
            continue

        if value[chc - 1] != ' ':
            print("Position already occupied. Try another one.")
            continue

        value[chc - 1] = symbol
        player_position[symbol].append(chc)

        if win_validate(player_position, symbol):
            return symbol
        if draw_validate(player_position):
            return "D"

        symbol = "O" if symbol == "X" else "X"


def main():
    player_one = input("Enter name of first player: ")
    player_two = input("Enter name of second player: ")
    scoreboard = {player_one: 0, player_two: 0}
    player_current = player_one

    while True:
        print("Enter P to play game")
        print("Enter S to show scoreboard")
        print("Enter E to exit")
        chc = input().upper()

        if chc == "E":
            break
        elif chc == "S":
            show_scoreboard(scoreboard)
        elif chc == "P":
            print(f"{player_current}, choose your symbol (X or O): ")
            res = input().upper()

            if res not in ["X", "O"]:
                print("Invalid choice. Try again.")
                continue

            player_choice = {"X": "", "O": ""}
            player_choice[res] = player_current
            player_choice["O" if res == "X" else "X"] = (
                player_two if player_current == player_one else player_one
            )

            winner = game_single(res)

            if winner == "D":
                print("Game was close. It is a draw!")
                show_scoreboard(scoreboard)
            else:
                scoreboard[player_choice[winner]] += 1
                print(f"Hurray! {player_choice[winner]} won the game 🎉")
                show_scoreboard(scoreboard)

            player_current = (
                player_two if player_current == player_one else player_one
            )


main()
