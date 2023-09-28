#battleship HW assighnment Eli

# random used for G.L selecting target and placing ships
import random
ranint = random.randint(0,10)
print (ranint)

#this is the board
rows = 10
cols = 10
lst = [["~"]*cols]*rows
board = [["~" for i in range(cols)]for j in range(rows)]
print ("   0    1    2    3    4    5    6    7    8    9")
for i in range (0,10):
    print (i, lst[i])

#P1 ship placement
#odd boats 6 total three 3 boats two 5 boats one 7 boat
xinput = int(input("give me x "))
yinput = int(input("give me y "))
axis = input("L/R or U/D")
print ("you picked "+ axis)

#G.L 3 boats
def gamelogicboatplacement():
    randir = random.randint(0, 1)
    xinput = random.randint(1, 10)
    yinput = random.randint(1, 10)

    if randir ==1:
        if board[xinput][yinput] == "~" and board[xinput + 1][yinput] == "~" and board[xinput-1][yinput] == "~":
            board[xinput][yinput] = "B"
            board[xinput + 1][yinput] = "B"
            board[xinput - 1][yinput] = "B"
    else:
        if board[xinput][yinput] == "~" and board[xinput][yinput + 1] == "~" and board[xinput][yinput - 1] == "~":
            board[xinput][yinput] = "B"
            board[xinput + 1][yinput] = "B"
            board[xinput - 1][yinput] = "B"
gamelogicboatplacement()

#P1 ship placement fine tuning
def threeboat ():
    if axis == "U" or  axis == "D" or axis == "U/D" or axis == "u" or axis == "d" or axis == "u/d":
        board[xinput][yinput] = "B"
        board[xinput + 1][yinput] = "B"
        board[xinput - 1][yinput] = "B"
    else:
        board[xinput][yinput] = "B"
        board[xinput + 1][yinput] = "B"
        board[xinput - 1][yinput] = "B"
threeboat()

for i in range(0,10):
    print (i, board[i])

#P1 hit registration and shooting
def P1target():
    targetx = int(input("pick X coordinate to fire at"))
    targety = int(input("pick Y coordinate to fire at"))
    if board[targetx][targety] == "B":
        print ("You hit my battleship!")
        board[targetx][targety] = "X"
    elif board[targetx][targety] == "X" or board[targetx][targety] == "O":
        print ("You already shot here! You loose a turn")
    else:
        board [targetx][targety] = "O"
    for i in range(0, 10):
        print (i, lst[i])
P1target()
threeboat()