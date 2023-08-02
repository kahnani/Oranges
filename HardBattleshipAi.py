# Battleship AI by Cole kleinebekel

CarrierBias = 0.5 #5 Long Ship
battleshipBias = 0.1 #4 Long Ship
destroyerBias = 0.1 #3 Long Ship
patrolBias = 0.1 #2 Long Ship

arr = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0, -1, 0.0, 0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],]

# Method that prints the array
def printArr():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    for row in range(len(arr)):
        print(str(round(arr[row][0], 2)) + " | " + str(round(arr[row][1], 2)) + " | " + str(round(arr[row][2], 2)) + " | " + str(round(arr[row][3], 2)) + " | " + str(round(arr[row][4], 2)) + " | " + str(round(arr[row][5], 2)) + " | " + str(round(arr[row][6], 2)) + " | " + str(round(arr[row][7], 2)) + " | " + str(round(arr[row][8], 2)) + " | " + str(round(arr[row][9], 2)))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
'''
@Param row = the row where the "ship" will be placed
@Param col = the col where the "ship" will be placed
@Param size = how big the "ship" is
@Method Function = This method will try to fit a "ship" into a square based off its size,
if it is able it it will add the weight value of the ship based off size into those squares in the array
'''
def tryFit(row, col, size):
    HorizontalFit = True
    VerticalFit = True
    
    #assign the weight based off the ships size
    if size == 5:
        weight = CarrierBias
    elif size == 4:
        weight = battleshipBias
    elif size == 3:
        weight = destroyerBias
    elif size == 2:
        weight = patrolBias
    else:
        print("Fix me im borken")
            
    #Checking if you can fit it horazontally
    try:
        for i in range(size):
            if arr[row+i][col] < 0:
                VerticalFit = False
    except:
        VerticalFit = False
    
    #checking to see if you can fit it vertically
    try:
        for i in range(size):
            if arr[row][col+i] < 0:
                HorizontalFit = False
    except:
        HorizontalFit = False
        
    if VerticalFit:
        for i in range(size):
            arr[row+i][col] = arr[row+i][col] + weight
    
    # add to the array if it can fit
    if HorizontalFit:
            for i in range(size):
                arr[row][col+i] = arr[row][col+i] + weight
                print(i)

#free falling code where i actually call the methodz
for row in range(len(arr)):
    for col in range(len(arr[0])):
        tryFit(row,col,5)
        tryFit(row,col,4)
        tryFit(row,col,3)
        tryFit(row,col,2)
printArr()