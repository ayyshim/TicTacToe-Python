'''
Name : TicTacToe CLG (Command Line Game)
Type : CLI
Author : Ashim Upadhaya <upadhayaashim@gmail.com>
Timestamp : Tuesday, November 5, 2019 - 09:21:AM (Kathmandu/Asia)
Description : Python implementation of simple yet famous TicTacToe game.
'''

def gameStart():
    global game
    game = [[0,0,0] for x in range(3)]
    print("You are playing TicTacToe")
    start = input("Enter [s] to start and [any] to quit: ")
    return (start == "s")

def showGameBoard(game, startUp=False):
    if not startUp:
        print("\nThis is the game so far :\n ")
    else:
        print("\nHere is your brand new TicTacToe Board\n")

    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)
    print("")

def checkBoard(game, player, h, v):
    try:
        if game[h][v] is 0:
            game[h][v] = player
            player = 2 if player is 1 else 1
        else:
            print("Place is already occupied. Can not overwrite.\n")
        return game,player
    except IndexError as e:
        print("You can not go beyond 0 1 or 2. [{}]\n".format(e))
        return game, player

def win(current_game):
    won = False
    game_over = False
    
    # Horizontal
    for row in game:
        if row.count(row[0]) is len(row) and row[0] != 0:
            won = True
            break

    # Verticle
    for col in range(len(game[0])):
        colPoint = []
        for row in game:
            colPoint.append(row[col])
        if colPoint.count(colPoint[0]) is len(colPoint) and colPoint[0] != 0:
            won = True
            break

    # Diagonal (\)
    digPoint = []

    for point in range(len(game[0])):
        digPoint.append(game[point][point])
    
    if digPoint.count(digPoint[0]) is len(digPoint) and digPoint[0] !=0:
        won = True

    # Diagonal (/)
    digPoint = []
    for row, col in enumerate(reversed(range(len(game)))):
        digPoint.append(game[row][col])

    if digPoint.count(digPoint[0]) is len(digPoint) and digPoint[0] != 0:
        won = True
    
    # Game Over
    if sum(spaces.count(0) for spaces in current_game) == 0:
        game_over = True

    return won, game_over

def credits():
    print("")
    print("====> TicTacToe CLG (Command Line Game) <====")
    print("====>       Developed by Ashim.         <====")
    print("")

if __name__ == "__main__":
    while True:
        playerReady = gameStart()
        if not playerReady:
            credits()
            break
        
        showGameBoard(game, startUp=True)
        player = 1

        while True:
            print("=====Player {} turn=====".format(player))
            h,v = input("Enter your spot (Horizontal, Verticle) : ").split(",")
            h = int(h)
            v = int(v)
            game, nextPlayer = checkBoard(game, player, h, v)
            showGameBoard(game)
            won, game_over = win(game)

            if won:
                print("^^^^^^^^^^^^^^^^^^^^^^")
                print("======================")
                print("|   Player {} win.   |".format(player))
                print("======================")
                print("")
                break

            if game_over:
                print("^^^^^^^^^^^^^^^^^^^^^^")
                print("======================")
                print("| No more space left |")
                print("|     Game Over      |")
                print("======================")
                print("")
                break

            player = nextPlayer 