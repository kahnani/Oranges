import random
#Made by Cole Kleinebekel and Jazmyn Revels, rember to have a good day ans stay kind!
DEBUGG = False
arr = [["O","O","O","O","O"],
       ["O","O","O","O","O"],
       ["O","O","O","O","O"],
       ["O","O","O","O","O"],
       ["O","O","O","O","O"]]

#method that will print the bord
def printBoard():
    for r in range(len(arr)):
        print(arr[r])
        print()
#blueprint currently holding all the parts of the ships
class ship():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

#init values
x = 0
row = 0
col = 0
#random.randrange(0,3)
direct = random.randrange(0,4) # 0 = vertical, 1 = horizontal, 2 = sideways--top left to bottom right, 3 = sideways bottom left to top right
length = random.randrange(2,5)
#okay so i have to edit the starting pos according to the direction, i will randomly roll the starting point,
# what is vertical will always be going down , sideways always left to right etc.
if direct == 0:
    wRow = random.randrange(0,6-length) # starting y of my guy
    wCol = random.randrange(0,5) #starting x of my guy
elif direct == 1:
    wRow = random.randrange(0,5) #starting x of my guy
    wCol = random.randrange(0,6-length) #starting x of my guy
elif direct == 2:
    wRow = random.randrange(0,6-length) #starting x of my guy
    wCol = random.randrange(0,6-length) # starting y of my guy
elif direct == 3:
    wRow = random.randrange(0,6-length) #starting x of my guy
    wCol = random.randrange(length,5) # starting y of my guy
allShip = []
print(str(direct) + " 0 = vertical, 1 = horizontal, 2 = sideways--top left to bottom right, 3 = sideways bottom left to top right")
for i in range(length):
    if direct == 0:
        ship1 = ship(wRow+i,wCol,"Lefter")
    elif direct == 1:
        ship1 = ship(wRow,wCol+i,"Lefter")
    elif direct == 2:
        ship1 = ship(wRow+i,wCol+i,"Lefter")
    elif direct == 3:
        ship1 = ship(wRow+i,wCol-i,"Lefter")
    allShip.append(ship1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
for i in range(len(allShip)):
    print(str(allShip[i].y) + " , " + str(allShip[i].x))
    arr[allShip[i].x][allShip[i].y] = "■"
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#main game loop
while True:
    x += 1
    print("Round =", x)
    printBoard()

    #valadating the row input
    while True:
        cole = False
        Trow = input('Choose Row: ')
        try:
            int(Trow)
        except:
            print("Please provide a int")
            cole = True
            continue
        if cole != True:
            if int(Trow) < 0 or int(Trow) > 4: #checking for out of bounds on row
                print('Please enter a number in the bounds.')
                continue
        break

    #valadating the col input
    while True:
        cole = False
        Tcol = input('Choose Col: ')
        try:
            int(Tcol)
        except:
            print("Please provide a int")
            cole = True
            continue
        if cole != True:
            if int(Tcol) < 0 or int(Tcol) > 4: #checking for out of bounds on row
                print('Please enter a number in the bounds.')
                continue
        break

    hold = Trow
    Trow = Tcol
    Tcol = hold

    #checking if the (Row, Col) you picked has a ship in it or if you have already shot there, if not on both you shoot
    holder = False
    if arr[int(Trow)][int(Tcol)] == "X":
        print("you have already gone there")
        x-=1 # subtract 1 from the round number
    else:
        remover = 0
        for i in range(len(allShip)):
            if int(allShip[i].x) == int(Trow) and int(allShip[i].y) == int(Tcol):
                print("You Hit Something at ", Tcol + " X, and at " + Trow + " Y")
                arr[int(Trow)][int(Tcol)] = "X"
                holder = True
                length -= 1
                if length <= 0:
                    print("Ship Was Destoryed, You Win")
                    quit()

        if not holder:
            print("Miss!")
            arr[int(Trow)][int(Tcol)] = "X"
