import random
import pygame
# made by Cole Kleinebekel and Jazmyn Revels

DEBUGGING = True
global PhaseTwo
PhaseTwo = False

pygame.init()

#game window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ship Battles by Cole Kleinebekel and Jazmyn Revels')

start_img = pygame.image.load('C:\\Users\\SERN_INTERN\\Downloads\\start_btn.png')
rotate_img = pygame.image.load('C:\\Users\\SERN_INTERN\\Downloads\\rotate.png')
rotate_img = pygame.transform.scale(rotate_img, (int(200), int(200)))

#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

#blueprint that make buttons
class Button():
  def __init__(self, x, y, img, scale):
    width = img.get_width()
    height = img.get_height()
    self.img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
    self.rect = self.img.get_rect()
    self.rect.topleft = (x,y)
    self.clicked = False
  
  def draw(self):
    if not PhaseTwo:
      action = False
      #getting mouse possition
      pos = pygame.mouse.get_pos()
      
      if self.rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
          self.clicked = True
          action = True
          
      if pygame.mouse.get_pressed()[0] == 0:
        self.clicked = False
      
      screen.blit(self.img, (self.rect.x, self.rect.y))
      return action
  
class ColliderBox():
    def __init__(self, x, y, rect):
        self.row = x
        self.col = y
        self.rect = rect
    
def printBoardPhase1():
  PhaseTwo = True
  print("-=-=-==-=-=-=-==-=-=-=-=-=-")
  arr = [["O" for i in range(10)] for i in range(10)]
  
  for i in range(len(gridCs)):
    for j in range(len(boxes)):
      if boxes[j].colliderect(gridCs[i]):
        if i < 10:
          arr[i][0] = "■"
        else:
          arr[i % 10][i // 10] = "■"
  
  for i in range(len(arr)):
    print(arr[i])
    print()
  return arr

def printBoard(arr):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    for r in range(len(arr)):
        print(arr[r])
        print()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
  

start_button = Button(651,430, start_img, 0.5)
active_box = None
boxes = []

Carrier = pygame.Rect(50-20, 50, 37, 185) # 5 long 37x5 = 185
Battleship = pygame.Rect(100-20, 50, 37, 148) # 4 long 37x4 = 148
Cruiser = pygame.Rect(150-20, 50, 37, 111) # 3 long 37x3 = 111
Submarine = pygame.Rect(200-20, 50, 37, 111) # 3 long 37x3 = 111
Destroyer = pygame.Rect(250-20, 50, 37, 74) # 2 long 37x2 = 74
boxes.append(Carrier)
boxes.append(Battleship)
boxes.append(Cruiser)
boxes.append(Submarine)
boxes.append(Destroyer)

GRID_WIDTH, GRID_HEIGHT = 20, 20
CELL_SIZE = 37
gridCs = []
def draw_grid():
    for x in range(300, CELL_SIZE*11 + 300, CELL_SIZE):
      pygame.draw.line(screen, pygame.Color("gray"), (x, 50), (x, 420))
    for y in range(50, CELL_SIZE*11 + 50, CELL_SIZE):
      pygame.draw.line(screen, pygame.Color("gray"), (300, y), (670, y))
      
def draw_grid_Mine():
    for x in range(10, CELL_SIZE*11 + 10, CELL_SIZE):
      pygame.draw.line(screen, pygame.Color("gray"), (x, 50), (x, CELL_SIZE*11 + 13))
    for y in range(50, CELL_SIZE*11 + 50, CELL_SIZE):
      pygame.draw.line(screen, pygame.Color("gray"), (10, y), (CELL_SIZE*10 +10, y))

def draw_grid_Opponet():
    for x in range(500, CELL_SIZE*11 + 500, CELL_SIZE):
      pygame.draw.line(screen, pygame.Color("gray"), (x, 50), (x, CELL_SIZE*11 + 13))
    for y in range(50, CELL_SIZE*11 + 50, CELL_SIZE):
      pygame.draw.line(screen, pygame.Color("gray"), (500, y), (CELL_SIZE*10 + 500, y))
      
EnemyColider = []
EnemyArr = [["O" for i in range(10)] for i in range(10)]
for row in range(500, CELL_SIZE*10 + 500, CELL_SIZE):
    for col in range(50, CELL_SIZE*10 + 50, CELL_SIZE):
        EnemyShip = pygame.Rect(row+1, col+1, 35, 35)
        EnemyColider.append(EnemyShip)
        
def find_closest_indexX(arr, target):
    closest_index = None
    min_diff = float('inf')  # Initialize minimum difference to infinity

    for i, num in enumerate(arr):
        diff = abs(num.x - target)
        if diff < min_diff:
            min_diff = diff
            closest_index = i
    return closest_index
  
def find_closest_indexY(arr, target):
  closest_index = None
  min_diff = float('inf')  # Initialize minimum difference to infinity

  for i, num in enumerate(arr):
      diff = abs(num.y - target)
      if diff < min_diff:
          min_diff = diff
          closest_index = i
  return closest_index

def fillEnemyArr(eArr):
    #making the 5 long guy first
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if dir == 0:
        row = random.randrange(0,5)
        col = random.randrange(0,10)
        for i in range(5):
            EnemyArr[row+i][col] = "■"
    else:
        row = random.randrange(0,10)
        col = random.randrange(0,5)
        for i in range(5):
            EnemyArr[row][col+i] = "■"

    tempFill(EnemyArr,4)

    tempFill(EnemyArr,3)
 
    tempFill(EnemyArr,3)
    
    tempFill(EnemyArr,2)
    
    
def tempFill(arr,size):
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if dir == 0:
        while True:
            row = random.randrange(0,10-size)
            col = random.randrange(0,10)
            for i in range(size):
                if EnemyArr[row+i][col] == "■":
                    continue
            break
        for i in range(size):
            if EnemyArr[row+i][col] == "■":
                EnemyArr[row+i][col] = "■"
            else:
                EnemyArr[row+i][col] = "■"
    else:
        while True:
            row = random.randrange(0,10)
            col = random.randrange(0,10-size)
            for i in range(size):
                if EnemyArr[row][col+i] == "■":
                    continue
            break
        for i in range(size):
            if EnemyArr[row][col+i] == "■":
                EnemyArr[row][col+i] = "■"
            else:
                EnemyArr[row][col+i] = "■"

fillEnemyArr(EnemyArr)

for x in range(300, 636, 37):
  for y in range(50, 400, 37):
    GC = pygame.Rect(x, y, 1, 1)
    gridCs.append(GC)

MyBoardCollisions = []

for x in range(10, 37*10+10, 37):
  for y in range(50, 37*10+50, 37):
    BoardCollison = pygame.Rect(x, y, 1, 1)
    MyBoardCollisions.append(BoardCollison)
    
run = True
while run:
  if not PhaseTwo:
    #print(PhaseTwo)
    screen.fill((33,66,99))
    draw_grid()
    # # the funny cover up
    # box1 = pygame.Rect(300, 426, 401, 201)
    # pygame.draw.rect(screen, "turquoise1", box1)
    # box2 = pygame.Rect(676, 50, 300, 600)
    # pygame.draw.rect(screen, "turquoise1", box2)
  
    rotateor = pygame.Rect(0, 400, 250, 200)
    pygame.draw.rect(screen, (6,26,84), rotateor)
    screen.blit(rotate_img, (rotateor.x, rotateor.y))
  
    for box in gridCs:
      pygame.draw.rect(screen, "black", box)
    for box in boxes:
      pygame.draw.rect(screen, "pink", box)
  
  if start_button.draw():
    if DEBUGGING: print("I worked")
    arr = printBoardPhase1()
    PhaseTwo = True
    screen.fill((33,66,99))
    for box in EnemyColider:
      pygame.draw.rect(screen, (33,66,99), box)
    
  boxTCs = []
  #important code that finds the index of the box that i am currently hoving over with my mouse and saves it
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      
    if not PhaseTwo :
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: # if left mouse button gets pressed down
          for num, box in enumerate(boxes): # loop though all boxes 
            if box.collidepoint(event.pos): # find the box that is coliding with the mouse
              active_box = num # save it in active_box

      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
          if active_box != None:
              if DEBUGGING: print(str(boxes[active_box].x) + "," + str(boxes[active_box].y))
              if boxes[active_box].x > 150:
                if active_box == 1:
                  off = 0
                else:
                  off = 1
                closex = find_closest_indexX(gridCs, boxes[active_box].x)
                boxes[active_box].x = gridCs[closex].x
                if DEBUGGING: print(closex // 5)
                closey = find_closest_indexY(gridCs, boxes[active_box].y)
                boxes[active_box].y = gridCs[closey].y
                if DEBUGGING: print(closey)
                if boxes[active_box].x + boxes[active_box].width > 710:
                  #if the place he user tryed to put the box is invalid then I move the box back to spawn
                  boxes[active_box].x = 50 
                  boxes[active_box].y = 50  
                  print("Invalid")
                elif boxes[active_box].y + boxes[active_box].height > 450:
                  #if the place he user tryed to put the box is invalid then I move the box back to spawn
                  boxes[active_box].x = 50
                  boxes[active_box].y = 50
                  print("Invalid")
                elif boxes[active_box].colliderect(boxes[off]):
                  #if the place he user tryed to put the box is invalid then I move the box back to spawn
                  boxes[active_box].x = 50
                  boxes[active_box].y = 50
                  print("Invalid")
              elif boxes[active_box].colliderect(rotateor):
                if DEBUGGING: print("rotateing")
                holder = boxes[active_box].width
                boxes[active_box].width = boxes[active_box].height
                boxes[active_box].height = holder
              active_box = None

      if event.type == pygame.MOUSEMOTION:
        if active_box != None:
          boxes[active_box].move_ip(event.rel)
    elif PhaseTwo:
        boardP = pygame.Rect(800, 500, 250, 200)
        pygame.draw.rect(screen, (6,26,84), boardP)
        
        myboardP = pygame.Rect(0, 500, 100, 200)
        pygame.draw.rect(screen, (6,26,84), myboardP)
        
        draw_grid_Mine()
        draw_grid_Opponet()
        for box in MyBoardCollisions:
            pygame.draw.rect(screen, "black", box)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # if left mouse button gets pressed down
                for num, box in enumerate(EnemyColider): # loop though all boxes 
                    if box.collidepoint(event.pos): # find the box that is coliding with the mouse
                        active_box = num # save it in active_box
                        if EnemyArr[num%10][num // 10] == "■":
                            EnemyArr[num%10][num // 10] = "X"
                            box = pygame.draw.rect(screen, "dark red", box)
                        elif EnemyArr[num%10][num // 10] == "O": 
                            EnemyArr[num%10][num // 10] = "X"
                            box = pygame.draw.rect(screen, "Black", box)
                        counter = 0
                        for r in range(len(EnemyArr)):
                            for c in range(len(EnemyArr)):
                                if EnemyArr[r][c] == "■":
                                    counter += 1
                        if counter == 0:
                            screen.fill("Green")
                        while True:
                            rowGuess = random.randrange(0,10)
                            colGuess = random.randrange(0,10)
                            if arr[rowGuess][colGuess] == "X":
                                continue
                            break
                        if arr[rowGuess][colGuess] == "O":
                            arr[rowGuess][colGuess] = "X"
                            pygame.draw.rect(screen, "black", fml)
                        elif arr[rowGuess][colGuess] == "■":
                            arr[rowGuess][colGuess] = "H"
                            pygame.draw.rect(screen, "dark red", fml)
        
        for r in range(len(EnemyArr)):
            for c in range(len(EnemyArr)):
                fml = pygame.Rect(MyBoardCollisions[r*10 + c].x, MyBoardCollisions[r*10 + c].y, 37, 37)
                            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if boardP.collidepoint(event.pos):
                    print("Enemys Board")
                    printBoard(EnemyArr)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if myboardP.collidepoint(event.pos):
                    print("Enemys Board")
                    printBoard(arr)
                
                
        for r in range(len(arr)):
            for c in range(len(arr)):
                if arr[c][r] == "■":
                    myShip = pygame.Rect(MyBoardCollisions[r*10 + c].x, MyBoardCollisions[r*10 + c].y, 37, 37)
                    pygame.draw.rect(screen, "pink", myShip)
                elif arr[c][r] == "X":
                    myShip = pygame.Rect(MyBoardCollisions[r*10 + c].x, MyBoardCollisions[r*10 + c].y, 37, 37)
                    pygame.draw.rect(screen, "black", myShip)
                elif arr[c][r] == "H":
                    myShip = pygame.Rect(MyBoardCollisions[r*10 + c].x, MyBoardCollisions[r*10 + c].y, 37, 37)
                    pygame.draw.rect(screen, "dark red", myShip)
        counter = 0
        for r in range(len(arr)):
            for c in range(len(arr)):
                if arr[c][r] == "■":
                    counter += 1
        if counter == 0: 
            screen.fill("dark red")
  pygame.display.update()

pygame.quit()
