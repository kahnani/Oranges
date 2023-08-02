import random
import pygame

# made by Cole Kleinebekel and Jazmyn Revels

DEBUGGING = True
global PhaseTwo
PhaseTwo = False
findingDir = False
DirFound = None
Hunting = False
prey = []
difficulty = 1

pygame.init()

#game window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BGCOLOR = (33,66,99)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Supercalifragilisticexpialidocious by Cole Kleinebekel and Jazmyn Revels')

########################### EDIT FILE PATH ########################
start_img = pygame.image.load('C:\\Users\\molet\\Downloads\\start_btn.png') # <-----------
rotate_img = pygame.image.load('C:\\Users\\molet\\Downloads\\rotate.png') # <-------------
###################################################################

font_size = 36
font = pygame.font.Font(None, font_size)

def print_text(text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))


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
          arr[i][0] = boxesNames[j]
        else:
          arr[i % 10][i // 10] = boxesNames[j]
  
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

boxesNames = []

boxesNames.append("Carrier")
boxesNames.append("Battleship")
boxesNames.append("Cruiser")
boxesNames.append("Submarine")
boxesNames.append("Destroyer")

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

def Func(row, col, size, dir):
    if dir == 0:
        try:
            for i in range(size):
                if EnemyArr[row+i][col] != "O":
                    return False
        except:
            return False
    else:
        try:
            for i in range(size):
                if EnemyArr[row][col+i] != "O":
                    return False
        except:
            return False
    return True

def add(row, col, size, dir, name):
    if dir == 0:
        for i in range(size):
            EnemyArr[row+i][col] = name
    else:
        for i in range(size):
                EnemyArr[row][col+i] = name
                
def aiHelper(rowGuess, colGuess):
  if arr[rowGuess][colGuess] == "O":
      arr[rowGuess][colGuess] = "X"
      pygame.draw.rect(screen, "black", fml)
      return "CPU: Miss!"
  elif arr[rowGuess][colGuess] != "H" and arr[rowGuess][colGuess] != "X":
      returnholder = arr[rowGuess][colGuess]
      arr[rowGuess][colGuess] = "H"
      pygame.draw.rect(screen, "dark red", fml)
      return "CPU: Hit your " + returnholder    
    
def easyAI():
    while True:
        rowGuess = random.randrange(0,10)
        colGuess = random.randrange(0,10)
        if arr[rowGuess][colGuess] != "X" and arr[rowGuess][colGuess] != "H":
          break
    return aiHelper(rowGuess, colGuess,)

def mediumAI():
  for r in range(len(arr)):
    for c in range(len(arr[0])):
      if arr[r][c] == "H":
        returnHolder = scanAroundShip(r,c)
        if returnHolder[0]:
          return aiHelper(returnHolder[1], returnHolder[2])
  while True:
      notSurounded = False
      rowGuess = random.randrange(0,10)
      colGuess = random.randrange(0,10)
      if rowGuess < 9 and colGuess < 9 and rowGuess > 0 and colGuess > 0:
        if (arr[rowGuess +1][colGuess] != "X") or (arr[rowGuess ][colGuess+1] != "X") or (arr[rowGuess -1][colGuess] != "X") or (arr[rowGuess ][colGuess-1] != "X"):
            notSurounded = True
      else:
        if rowGuess == 9 and colGuess == 9:
          if (arr[rowGuess -1][colGuess] != "X") or (arr[rowGuess ][colGuess-1] != "X"):
            notSurounded = True
            
        elif rowGuess == 0 and colGuess == 0:
          if (arr[rowGuess +1][colGuess] != "X") or (arr[rowGuess ][colGuess+1] != "X"):
            notSurounded = True
            
        elif rowGuess == 0 and colGuess == 9:
          if (arr[rowGuess +1][colGuess] != "X") or (arr[rowGuess][colGuess-1] != "X"):
            notSurounded = True
        
        elif rowGuess == 9 and colGuess == 0:
          if (arr[rowGuess -1][colGuess] != "X") or (arr[rowGuess][colGuess+1] != "X"):
            notSurounded = True
            
        elif rowGuess == 0:
          if (arr[rowGuess +1][colGuess] != "X") or (arr[rowGuess ][colGuess+1] != "X") or (arr[rowGuess ][colGuess-1] != "X"):
            notSurounded = True
            
        elif colGuess == 0:
          if (arr[rowGuess +1][colGuess] != "X") or (arr[rowGuess ][colGuess+1] != "X") or (arr[rowGuess -1][colGuess] != "X"):
            notSurounded = True
            
        elif colGuess == 9:
          if (arr[rowGuess -1][colGuess] != "X") or (arr[rowGuess ][colGuess-1] != "X") or (arr[rowGuess +1][colGuess] != "X"):
            notSurounded = True
            
        elif rowGuess == 9:
          if (arr[rowGuess -1][colGuess] != "X") or (arr[rowGuess ][colGuess+1] != "X") or (arr[rowGuess ][colGuess+1] != "X"):
            notSurounded = True
      if arr[rowGuess][colGuess] != "X" and arr[rowGuess][colGuess] != "H" and notSurounded:
        break
  return aiHelper(rowGuess, colGuess)

def hardAIHelper1(rowGuess, colGuess):
  if DEBUGGING: print("AI HELPER 1, RUNNING NOW")
  tempDir = 0
  if arr[rowGuess][colGuess] == "O":
      arr[rowGuess][colGuess] = "X"
      pygame.draw.rect(screen, "black", fml)
      return "CPU: Miss!"
  elif arr[rowGuess][colGuess] != "H" and arr[rowGuess][colGuess] != "X":
      hit = True
      firstRowHit = rowGuess
      firstColHit = colGuess
      returnholder = arr[rowGuess][colGuess]
      arr[rowGuess][colGuess] = "H"
      pygame.draw.rect(screen, "dark red", fml)
      return "CPU: Hit your " + returnholder
  
  
def hardAIHelper2(rowGuess, colGuess):
  if DEBUGGING: print("AI HELPER 2, RUNNING NOW")
  hadTurn = False
  if DirFound == None:
    if tempDir == 0: # 0 == up, 1 == right, 2 == down, 3 == left
      if firstRowHit != 9 and not hadTurn:
        rowGuess = firstRowHit + 1
        colGuess = firstColHit
        hadTurn = True
        if arr[rowGuess][colGuess] == "O":
          arr[rowGuess][colGuess] = "X"
          pygame.draw.rect(screen, "black", fml)
          return "CPU: Miss!"
        elif arr[rowGuess][colGuess] != "H" and arr[rowGuess][colGuess] != "X":
          DirFound = tempDir
          returnholder = arr[rowGuess][colGuess]
          arr[rowGuess][colGuess] = "H"
          pygame.draw.rect(screen, "dark red", fml)
          return "CPU: Hit your " + returnholder
          tempDir += 1
      else:
        tempDir += 1
        
    if tempDir == 1 and not hadTurn:
      if firstColHit != 9 and not hadTurn:
        rowGuess = firstRowHit 
        colGuess = firstColHit + 1
        hadTurn = True
        if arr[rowGuess][colGuess] == "O":
          arr[rowGuess][colGuess] = "X"
          pygame.draw.rect(screen, "black", fml)
          return "CPU: Miss!"
        elif arr[rowGuess][colGuess] != "H" and arr[rowGuess][colGuess] != "X":
          DirFound = tempDir
          returnholder = arr[rowGuess][colGuess]
          arr[rowGuess][colGuess] = "H"
          pygame.draw.rect(screen, "dark red", fml)
          return "CPU: Hit your " + returnholder
          tempDir += 1
      else:
        tempDir += 1
        
    if tempDir == 2 and not hadTurn:
      if firstRowHit != 0 and not hadTurn:
        rowGuess = firstRowHit - 1
        colGuess = firstColHit
        hadTurn = True
        if arr[rowGuess][colGuess] == "O":
          arr[rowGuess][colGuess] = "X"
          pygame.draw.rect(screen, "black", fml)
          return "CPU: Miss!"
        elif arr[rowGuess][colGuess] != "H" and arr[rowGuess][colGuess] != "X":
          DirFound = tempDir
          returnholder = arr[rowGuess][colGuess]
          arr[rowGuess][colGuess] = "H"
          pygame.draw.rect(screen, "dark red", fml)
          return "CPU: Hit your " + returnholder
          tempDir += 1
      else:
        tempDir += 1
    
    if tempDir == 3 and not hadTurn:
      if firstRowHit != 0 and not hadTurn:
        rowGuess = firstRowHit - 1
        colGuess = firstColHit
        hadTurn = True
        if arr[rowGuess][colGuess] == "O":
          arr[rowGuess][colGuess] = "X"
          pygame.draw.rect(screen, "black", fml)
          return "CPU: Miss!"
        elif arr[rowGuess][colGuess] != "H" and arr[rowGuess][colGuess] != "X":
          DirFound = 3
          returnholder = arr[rowGuess][colGuess]
          arr[rowGuess][colGuess] = "H"
          pygame.draw.rect(screen, "dark red", fml)
          return "CPU: Hit your " + returnholder
          tempDir += 1
      else:
        tempDir += 1
    pass

hitShip = None
DirFound = None
tempDir = None
firstRowHit = None
firstColHit = None
hit = False
          
def hardAI():
  if hit:
    hardAIHelper2()
  while True:
      notSurounded = False
      rowGuess = random.randrange(0,10)
      colGuess = random.randrange(0,10)
      if rowGuess < 9 and colGuess < 9 and rowGuess > 0 and colGuess > 0:
        if (arr[rowGuess +1][colGuess] != "X") or (arr[rowGuess ][colGuess+1] != "X") or (arr[rowGuess -1][colGuess] != "X") or (arr[rowGuess ][colGuess-1] != "X"):
            notSurounded = True
      else:
        if rowGuess == 9 and colGuess == 9:
          if (arr[rowGuess -1][colGuess] != "X") or (arr[rowGuess ][colGuess-1] != "X"):
            notSurounded = True
            
        elif rowGuess == 0 and colGuess == 0:
          if (arr[rowGuess +1][colGuess] != "X") or (arr[rowGuess ][colGuess+1] != "X"):
            notSurounded = True
            
        elif rowGuess == 0 and colGuess == 9:
          if (arr[rowGuess +1][colGuess] != "X") or (arr[rowGuess][colGuess-1] != "X"):
            notSurounded = True
        
        elif rowGuess == 9 and colGuess == 0:
          if (arr[rowGuess -1][colGuess] != "X") or (arr[rowGuess][colGuess+1] != "X"):
            notSurounded = True
            
        elif rowGuess == 0:
          if (arr[rowGuess +1][colGuess] != "X") or (arr[rowGuess ][colGuess+1] != "X") or (arr[rowGuess ][colGuess-1] != "X"):
            notSurounded = True
            
        elif colGuess == 0:
          if (arr[rowGuess +1][colGuess] != "X") or (arr[rowGuess ][colGuess+1] != "X") or (arr[rowGuess -1][colGuess] != "X"):
            notSurounded = True
            
        elif colGuess == 9:
          if (arr[rowGuess -1][colGuess] != "X") or (arr[rowGuess ][colGuess-1] != "X") or (arr[rowGuess +1][colGuess] != "X"):
            notSurounded = True
            
        elif rowGuess == 9:
          if (arr[rowGuess -1][colGuess] != "X") or (arr[rowGuess ][colGuess+1] != "X") or (arr[rowGuess ][colGuess+1] != "X"):
            notSurounded = True
      if arr[rowGuess][colGuess] != "X" and arr[rowGuess][colGuess] != "H" and notSurounded:
        break
  return hardAIHelper1(rowGuess, colGuess)

def scanAroundShip(row,col):
  for i in range(4):
    if i == 0:
      try:
        if arr[row+1][col] != "H" and arr[row+1][col] != "X":
          return True, row+1,col
      except:
        pass
    elif i == 1:
      try:
        if arr[row-1][col] != "H" and arr[row-1][col] != "X":
          return True, row-1, col
      except:
        pass
    elif i == 2:
      try:
        if arr[row][col+1] != "H" and arr[row][col+1] != "X":
          return True, row, col+1
      except:
        pass
    elif i == 3:
      try:
        if arr[row][col-1] != "H" and arr[row][col-1] != "X":
          return True, row, col-1
      except:
        pass
      return False, 0, 0
                  
while True:
    row = random.randrange(0,10)
    col = random.randrange(0,10)
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if Func(row, col, 5, dir):
        add(row, col, 5, dir, "Carrier")
        break
while True:
    row = random.randrange(0,10)
    col = random.randrange(0,10)
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if Func(row, col, 4, dir):
        add(row, col, 4, dir, "Battleship")
        break
while True:
    row = random.randrange(0,10)
    col = random.randrange(0,10)
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if Func(row, col, 3, dir):
        add(row, col, 3, dir, "Cruiser")
        break
while True:
    row = random.randrange(0,10)
    col = random.randrange(0,10)
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if Func(row, col, 3, dir):
        add(row, col, 3, dir, "Submarine")
        break
while True:
    row = random.randrange(0,10)
    col = random.randrange(0,10)
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if Func(row, col, 2, dir):
        add(row, col, 2, dir, "Destroyer")
        break


for x in range(300, 636, 37):
  for y in range(50, 400, 37):
    GC = pygame.Rect(x, y, 5, 5)
    gridCs.append(GC)

MyBoardCollisions = []

for x in range(10, 37*10+10, 37):
  for y in range(50, 37*10+50, 37):
    BoardCollison = pygame.Rect(x, y, 1, 1)
    MyBoardCollisions.append(BoardCollison)
    
playerOutput = font.render("Player:", True, (255, 255, 255))
CpuOutput = font.render("Cpu:", True, (255, 255, 255))
    
run = True
while run:
  if not PhaseTwo:
    #print(PhaseTwo)
    screen.fill((33,66,99))
    
    draw_grid()
  
    rotateor = pygame.Rect(0, 400, 250, 200)
    pygame.draw.rect(screen, (6,26,84), rotateor)
    screen.blit(rotate_img, (rotateor.x+20, rotateor.y))
  
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
              
              if boxes[active_box].x <= 0:
                  boxes[active_box].x = 50 
                  boxes[active_box].y = 50  
                  print("Invalid")
             
              if boxes[active_box].y <= 0:
                  boxes[active_box].x = 50 
                  boxes[active_box].y = 50  
                  print("Invalid")
              
              
              if boxes[active_box].x > 150:
                  
                closex = find_closest_indexX(gridCs, boxes[active_box].x)
                boxes[active_box].x = gridCs[closex].x
                
                if DEBUGGING: print(closex // 5)
                
                closey = find_closest_indexY(gridCs, boxes[active_box].y)
                boxes[active_box].y = gridCs[closey].y
                if DEBUGGING: print(closey)
                
                if boxes[active_box].x + boxes[active_box].width > 675:
                  #if the place he user tryed to put the box is invalid then I move the box back to spawn
                  boxes[active_box].x = 50 
                  boxes[active_box].y = 50  
                  print("Invalid")
                  
                elif boxes[active_box].y + boxes[active_box].height > 450:
                  #if the place he user tryed to put the box is invalid then I move the box back to spawn
                  boxes[active_box].x = 50
                  boxes[active_box].y = 50
                  print("Invalid")
                  
                for i in range(len(boxes)):
                  if i != active_box:
                    if boxes[active_box].colliderect(boxes[i]):
                      #if the place he user tryed to put the box is invalid then I move the box back to spawn
                      boxes[active_box].x = 50
                      boxes[active_box].y = 50
                      print("Invalid")
                      
              if boxes[active_box].colliderect(rotateor):
                if DEBUGGING: print("rotateing")
                holder = boxes[active_box].width
                boxes[active_box].width = boxes[active_box].height
                boxes[active_box].height = holder
              active_box = None

      if event.type == pygame.MOUSEMOTION:
        if active_box != None:
          boxes[active_box].move_ip(event.rel)
          
    elif PhaseTwo:
        boardP = pygame.Rect(250, 433, 400, 100)
        pygame.draw.rect(screen, BGCOLOR, boardP)
        
        screen.blit(playerOutput, (300, 450))
        screen.blit(CpuOutput, (300, 500))
        
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
                        ConsecutiveHitCounter = 0
                        
                        ######### PLAYER ATTACK TURN ###########
                        
                        if EnemyArr[num%10][num // 10] != "O" and EnemyArr[num%10][num // 10] != "X":
                            print("HIT!")
                            playerOutput = font.render("Player: HIT!", True, (255, 255, 255))
                            tempHold = EnemyArr[num%10][num // 10]
                            EnemyArr[num%10][num // 10] = "X"
                            box = pygame.draw.rect(screen, "dark red", box)
                            count = 0
                            
                            for row in EnemyArr:
                                for i in row:
                                    if i == tempHold:
                                        count += 1
                                        
                            if count == 0:
                                print("You Destoryed The " + tempHold)
                                playerOutput = font.render("Player: Sunk the " + tempHold, True, (255, 255, 255))

                        elif EnemyArr[num%10][num // 10] == "O":
                            playerOutput = font.render("Player: Miss!", True, (255, 255, 255))
                            EnemyArr[num%10][num // 10] = "X"
                            box = pygame.draw.rect(screen, "Black", box)
                            
                        counter = 0
                        for r in range(len(EnemyArr)):
                            for c in range(len(EnemyArr)):
                                if EnemyArr[r][c] != "O" and EnemyArr[r][c] != "X":
                                  counter += 1 # nested within 12
                                    
                        if counter == 0:
                          screen.fill("Green")
                        
                        ############ CPU ATTACK TURN ##########
                        
                        if difficulty == 0:
                          CpuOutput = font.render(easyAI() , True, (255, 255, 255))
                          
                        elif difficulty == 1:
                          CpuOutput = font.render(mediumAI() , True, (255, 255, 255))
                            
                        elif difficulty == 2:
                          CpuOutput = font.render(hardAI() , True, (255, 255, 255))
                          
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
                if arr[c][r] == "X":
                    myShip = pygame.Rect(MyBoardCollisions[r*10 + c].x+1, MyBoardCollisions[r*10 + c].y+1, 36, 36)
                    pygame.draw.rect(screen, "black", myShip)
                elif arr[c][r] == "H":
                    myShip = pygame.Rect(MyBoardCollisions[r*10 + c].x+1, MyBoardCollisions[r*10 + c].y+1, 36, 36)
                    pygame.draw.rect(screen, "dark red", myShip)
                elif arr[c][r] == "O":
                    myShip = pygame.Rect(MyBoardCollisions[r*10 + c].x+1, MyBoardCollisions[r*10 + c].y+1, 36, 36)
                    pygame.draw.rect(screen, BGCOLOR, myShip)
                else: 
                    myShip = pygame.Rect(MyBoardCollisions[r*10 + c].x+1, MyBoardCollisions[r*10 + c].y+1, 36, 36)
                    pygame.draw.rect(screen, "pink", myShip)
                    
        counter = 0
        for r in range(len(arr)):
            for c in range(len(arr)):
                if arr[c][r] != "X" and arr[c][r] != "H" and arr[c][r] != "O":
                    counter += 1
                    
        if counter == 0: 
            screen.fill("dark red")
                
            
  pygame.display.update()

pygame.quit()