import random

board = []
ships = [{"name": "carrier", "size": 5, "position":[], "marker": "C"},
         {"name": "battleship", "size": 4, "position":[], "marker": "B"},
         {"name": "cruiser", "size": 4, "position":[], "marker": "Z"},
         {"name": "submarine", "size": 3, "position":[], "marker": "S"},
         {"name": "destroyer", "size": 2, "position":[], "marker": "D"}]

def generateBoard():
    for i in range(9):
        board.append([0]*11)


def printBoard():
    i=0
    while i < len(board):
        j=0
        print(str(9-i)+" ",end="")
        while j < len(board[i]):
            if (not j==0) and j%10==0:
                print(str(board[i][j])+" \n")
            else:
                print(str(board[i][j])+" ",end="")
            j+=1
        i+=1

    print("  "+"A B C D E F G H I J K")

def placeShips():
    # test = [{"name": "carrier", "size": 5, "position":[],"marker": "C"},
    #         {"name": "destroyer", "size": 2, "position":[], "marker": "D"}]
    for i in ships:
        valid = False
        while valid==False:
            x = random.randint(0,10)
            y = random.randint(0,8)
            if board[y][x]==0:
                valid = True
                board[y][x]=i["marker"]
                # print(i["marker"]+":",x,y)
                isValid(i,x,y)
            else:
                continue
    printBoard()


def isValid(ship,x,y):
    valid = False
    pos_direct = [1,2,3,4]
    while valid == False:
        direct = random.choice(pos_direct)

        if direct==1:
            if y-(ship["size"]-1) < 0:
                pos_direct.remove(direct)
                continue
            else:
                for i in range(1,ship["size"]): 
                    if not board[y-i][x]==0:
                        pos_direct.remove(direct)
                        continue
                
                i=(ship["size"]-1)
                while i > 0:
                    board[y-i][x]=ship["marker"]
                    i-=1
                valid = True
        elif direct==2:
            if x+(ship["size"]-1) > 10:
                pos_direct.remove(direct)
                continue
            else:
                for i in range(1,ship["size"]): 
                    if not board[y][x+i]==0:
                        pos_direct.remove(direct)
                        continue

                i=(ship["size"]-1)
                while i > 0:
                    board[y][x+i]=ship["marker"]
                    i-=1
                valid = True
        elif direct==3:
            if y+(ship["size"]-1) > 8:
                pos_direct.remove(direct)
                continue
            else:
                for i in range(1,ship["size"]): 
                    if not board[y+i][x]==0:
                        pos_direct.remove(direct)
                        continue

                i=(ship["size"]-1)
                while i > 0:
                    board[y+i][x]=ship["marker"]
                    i-=1
                valid = True
        else:
            if x-(ship["size"]-1) < 0:
                pos_direct.remove(direct)
                continue
            else:
                for i in range(1,ship["size"]): 
                    if not board[y][x-i]==0:
                        pos_direct.remove(direct)
                        continue

                i=(ship["size"]-1)
                while i > 0:
                    board[y][x-i]=ship["marker"]
                    i-=1
                valid = True


generateBoard()
placeShips()