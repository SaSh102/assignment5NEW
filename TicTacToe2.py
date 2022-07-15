import time
from colorama import Fore


def show_game_board():
    for i in range(3):
        for j in range(3):
            print(Fore.RED + game[i][j], end=' ')
        print()

def check():
    if game[0][0] == Fore.GREEN +"X" and game[0][1] == Fore.GREEN +"X" and game[0][2] == Fore.GREEN +"X":
        print (Fore.GREEN +'player 1 wins')
        exit()
    if game[0][0] == Fore.YELLOW + "O" and game[0][1] == Fore.YELLOW + "O" and game[0][2] == Fore.YELLOW + "O":
        print (Fore.YELLOW +'player 2 wins')
        exit()
    if game[1][0] == Fore.GREEN +"X" and game[1][1] == Fore.GREEN +"X" and game[1][2] == Fore.GREEN +"X":
        print (Fore.GREEN +'player 1 wins')
        exit()
    if game[1][0] == Fore.YELLOW + "O" and game[1][1] == Fore.YELLOW + "O" and game[1][2] == Fore.YELLOW + "O":
        print (Fore.YELLOW +'player 2 wins')
        exit()
    if game[2][0] == Fore.GREEN +"X" and game[2][1] == Fore.GREEN +"X" and game[2][2] == Fore.GREEN +"X":
        print (Fore.GREEN +'player 1 wins')
        exit()
    if game[2][0] == Fore.YELLOW + "O" and game[2][1] == Fore.YELLOW + "O" and game[2][2] == Fore.YELLOW + "O":
        print (Fore.YELLOW +'player 2 wins')
        exit()
    if game[0][0] == Fore.GREEN +"X" and game[1][0] == Fore.GREEN +"X" and game[2][0] == Fore.GREEN +"X":
        print (Fore.GREEN +'player 1 wins')
        exit()
    if game[0][0] == Fore.YELLOW + "O" and game[1][0] == Fore.YELLOW + "O" and game[2][0] == Fore.YELLOW + "O":
        print (Fore.YELLOW +'player 2 wins')
        exit()
    if game[0][1] == Fore.GREEN +"X" and game[1][1] == Fore.GREEN +"X" and game[2][1] == Fore.GREEN +"X":
        print (Fore.GREEN +'player 1 wins')
        exit()
    if game[0][1] == Fore.YELLOW + "O" and game[1][1] == Fore.YELLOW + "O" and game[2][1] == Fore.YELLOW + "O":
        print (Fore.YELLOW +'player 2 wins')
        exit()
    if game[0][2] == Fore.GREEN +"X" and game[1][2] == Fore.GREEN +"X" and game[2][2] == Fore.GREEN +"X":
        print (Fore.GREEN +'player 1 wins')
        exit()
    if game[0][2] == Fore.YELLOW + "O" and game[1][2] == Fore.YELLOW + "O" and game[2][2] == Fore.YELLOW + "O":
        print (Fore.YELLOW +'player 2 wins')
        exit()
    if game[0][0] == Fore.GREEN +"X" and game[1][1] == Fore.GREEN +"X" and game[2][2] == Fore.GREEN +"X":
        print (Fore.GREEN +'player 1 wins')
        exit()
    if game[0][0] == Fore.YELLOW + "O" and game[1][1] == Fore.YELLOW + "O" and game[2][2] == Fore.YELLOW + "O":
        print (Fore.YELLOW +'player 2 wins')
        exit()
    if game[2][0] == Fore.GREEN +"X" and game[1][1] == Fore.GREEN +"X" and game[0][2] == Fore.GREEN +"X":
        print (Fore.GREEN +'player 1 wins')
        exit()
    if game[2][0] == Fore.YELLOW + "O" and game[1][1] == Fore.YELLOW + "O" and game[0][2] == Fore.YELLOW + "O":
        print (Fore.YELLOW +'player 2 wins')
        exit()
    

start= time.time()

game = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]
show_game_board()

while True:
    
    print(Fore.WHITE +'player 1')
    
    while True:
        row = int(input(Fore.WHITE +'satr ra vared kon: '))
        col = int(input(Fore.WHITE +'sotoon ra vared kon: '))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col]== '-':
                game[row][col] = Fore.GREEN + 'X'
                break
            else:
                print(Fore.WHITE +'cell is not empty!')
        else:
            print(Fore.WHITE +'index out of range, try again!')
    show_game_board()
    check()
    
    print(Fore.WHITE +'player 2')

    while True:
        row = int(input(Fore.WHITE +'satr ra vared kon: '))
        col = int(input(Fore.WHITE +'sotoon ra vared kon: '))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col]== '-':
                game[row][col] = Fore.YELLOW + 'O'
                break
            else:
                print(Fore.WHITE +'cell is not empty!')
        else:
            print(Fore.WHITE +'index out of range, try again!')
    show_game_board()
    check()

else:
    print(Fore.WHITE +'The game ended without a winner!')
print("run time: " + str(time.time()-start))



