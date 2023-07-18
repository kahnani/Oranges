import random
#Made by Cole Kleinebekel and Jazmyn Revels, rember to have a good day ans stay kind!
#valadating the arr size input
while True:
    cole = False
    arrSize = input('Choose How big you want the array to be: ')
    try: 
        int(arrSize)
    except:
        print("Please provide a int")
        cole = True
        continue
    if cole != True:
        if int(arrSize) < 3: #checking for out of bounds on row
            print('Number has to be greater then 0... ben')
            continue
    break
    
arr = [["O" for i in range(int(arrSize))] for i in range(int(arrSize))]
myarr = [["O" for i in range(int(arrSize))] for i in range(int(arrSize))]
# for r in range(int(arrSize)):
#     for c in range(int(arrSize)):
#         arr[r][c] = "O"

while True:
    cole = False
    chooserR = input('Choose Your Ships Starting Row: ')
    try:
        int(chooserR)
    except:
        print("Please provide a int")
        cole = True
        continue
    if cole != True:
        if int(chooserR) < 0 or int(chooserR) >= int(arrSize): #checking for out of bounds on row
            print('Number has to be greater then 0 and less then ', + arrSize + '... ben')
            continue
    break

while True:
    cole = False
    chooserC = input('Choose Your Ships Starting Col: ')
    try:
        int(chooserC)
    except:
        print("Please provide a int")
        cole = True
        continue
    if cole != True:
        if int(chooserC) < 0 or int(chooserC) >= int(arrSize): #checking for out of bounds on row
            print('Number has to be greater then 0 and less then ', + arrSize + '... ben')
            continue
    break
myarr[int(chooserR)][int(chooserC)] = "H"


#method that will print the bord
def printBoard():
    print("Board Of The Enemy")
    for r in range(len(arr)):
        print(arr[r])
        print()
        
def printMyBoard():
    print("Your Board")
    for r in range(len(myarr)):
        print(myarr[r])
        print()

#blueprint currently holding all the parts of the ships
class ship():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

#init values
x = 0
row = random.randrange(0,int(arrSize))
col = random.randrange(0,int(arrSize))
print(str(col) + " , " + str(row))
allMoves = []
allShip = []

ship1 = ship(row,col,"Lefter")
allShip.append(ship1)

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

    #idk man
    hold = Trow
    Trow = Tcol
    Tcol = hold

    #checking if the (Row, Col) you picked has a ship in it or if you have already shot there, if not on both you shoot
    holder = False
    allMoves.append(int(Trow))
    allMoves.append(int(Tcol))
    if arr[int(Trow)][int(Tcol)] == "X":
        print("you have already gone there")
        x-=1 # subtract 1 from the round number
    else:
        remover = 0
        for i in range(len(allShip)):
            if int(allShip[i].x) == int(Trow) and int(allShip[i].y) == int(Tcol):
                print("You Hit Something at ", Tcol + " X, and at " + Trow + " Y")
                arr[int(Trow)][int(Tcol)] = "X"
                print("Ship Was Destoryed, You Win")
                quit()

        if not holder:
            print("Miss!")
            arr[int(Trow)][int(Tcol)] = "X"
    attackR = random.randrange(0,int(arrSize))
    attackC = random.randrange(0,int(arrSize))
    while myarr[attackR][attackC] == "X":
        attackR = random.randrange(0,int(arrSize))
        attackC = random.randrange(0,int(arrSize))
    if myarr[attackR][attackC] == "H":
        myarr[attackR][attackC] = 'X'
        printMyBoard()
        print('You died sad and alone')
        quit()
    else:
        myarr[attackR][attackC] = 'X'
        printMyBoard()
        
    #if round is 5 or greater than 5 then the game is over and you lost.. loser
    if x >= 5:
        print("They Killed You And Your Family")
        quit()