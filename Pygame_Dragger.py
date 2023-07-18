import pygame
# made by Cole Kleinebekel and Jazmyn Revels

DEBUGGING = False

pygame.init()

#game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ship Battles by Cole Kleinebekel and Jazmyn Revels')

start_img = pygame.image.load('C:\\Users\\molet\\Downloads\\start_btn.png')

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
  
def printBoard():
  print("-=-=-==-=-=-=-==-=-=-=-=-=-")
  arr=[["O","O","O","O","O"],
       ["O","O","O","O","O"],
       ["O","O","O","O","O"],
       ["O","O","O","O","O"],
       ["O","O","O","O","O"]]
  
  for i in range(len(gridCs)):
    for j in range(len(boxes)):
      if boxes[j].colliderect(gridCs[i]):
        if i < 5:
          arr[i][0] = "X"
        elif i < 10:
          arr[i - 5][1] = "X"
        elif i < 15:
          arr[i - 10][2] = "X"
        elif i < 20:
          arr[i - 15][3] = "X"
        elif i < 25:
          arr[i - 20][4] = "X"
          
  for i in range(len(arr)):
    print(arr[i])
    print()
  

start_button = Button(651,430, start_img, 0.5)
active_box = None
boxes = []

boxT = pygame.Rect(50, 50, 75, 150)
boxL = pygame.Rect(50, 250, 150, 75)
boxes.append(boxT)
boxes.append(boxL)

GRID_WIDTH, GRID_HEIGHT = 10, 10
CELL_SIZE = 75
gridCs = []
def draw_grid():
    for x in range(300, CELL_SIZE*6 + 300, CELL_SIZE):
      pygame.draw.line(screen, pygame.Color("black"), (x, 50), (x, SCREEN_HEIGHT))
    for y in range(50, CELL_SIZE*6 + 50, CELL_SIZE):
      pygame.draw.line(screen, pygame.Color("black"), (300, y), (SCREEN_WIDTH, y))

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
  
for x in range(300, 635, 75):
  for y in range(50, 375, 75):
    GC = pygame.Rect(x, y, 1, 1)
    gridCs.append(GC)
    
run = True
while run:

  screen.fill("turquoise1")
  draw_grid()
  
  # the funny cover up
  box1 = pygame.Rect(300, 426, 401, 201)
  pygame.draw.rect(screen, "turquoise1", box1)
  box2 = pygame.Rect(676, 50, 300, 600)
  pygame.draw.rect(screen, "turquoise1", box2)
  
  rotateor = pygame.Rect(0, 400, 250, 200)
  pygame.draw.rect(screen, "turquoise3", rotateor)
  
  if start_button.draw():
    if DEBUGGING: print("I worked")
    printBoard()
    
  boxTCs = []
  
  for box in gridCs:
    pygame.draw.rect(screen, "black", box)
  for box in boxes:
    pygame.draw.rect(screen, "purple", box)

#important code that finds the index of the box that i am currently hoving over with my mouse and saves it
  for event in pygame.event.get():
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

    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()