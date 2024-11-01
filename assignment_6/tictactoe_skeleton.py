from operator import indexOf


def createZeroMatrix(r,c):
    output = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        output.append(row)
    return output

def printTTT(game):
    for i in range(3):
        print(f'{game[i][0]}|{game[i][1]}|{game[i][2]}')
        if i !=2:
            print( '-----')
piece = ['X','O']

def checkValidMove(game,inp):
    for i in game:
        if inp in i:
            return True
    return False

def checkWin(game):
    for i in range(0,len(game)):
        if game[i][0] == game[i][1] == game[i][2] != " ":
            return game[i][0]
        if game[0][i] == game[1][i] == game[2][i] != " ":
            return game[0][i]

        if game[0][0] == game[1][1] == game[2][2] != " " \
        or game[0][2] == game[1][1] == game[2][0] != " ":
            return game[1][1]

        if " " not in game[0] and " " not in game[1] and " " not in game[2]:
            return False
    return False

def tttGamePlay():
    game = createZeroMatrix(3,3)
    for i in range(3):
        for j in range(3):
            game[i][j] = i*3+j+1
    player = 0
    printTTT(game)
    print('')
    for i in range(9): # Anyhow play 9 times
        res = False
        while not res:
            pos = int(input(f'Player {piece[player]} move:')) - 1
            res = checkValidMove(game,pos + 1)
            if res == False:
                print('Invalid move!')
        game[pos//3][pos%3] = piece[player]
        printTTT(game)
        winner = checkWin(game)
        if winner != False:
            print(f'Player {winner} won!')
            return winner
        else:
            print('')
        player = 1 - player

game1 = [[1,2,3],[4,5,6],[7,8,9]]
game2 = [['X',2,3],['X',5,6],['X',8,9]]
game3 = [['O',2,3],[4,'O',6],[7,'O',9]]
game4 = [['X',2,'X'],[4,'O',6],['X','O','X']]
game5 = [['X','X','O'],['X','O','X'],['O','X','X']]


print(tttGamePlay())