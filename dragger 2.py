import pygame
# made by Cole Kleinebekel and Jazmyn Revels

pygame.init()

#game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ship Battles by Cole Kleinebekel and Jazmyn Revels')

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

for x in range(337, 710, 75):
  for y in range(87, 450, 75):
    GC = pygame.Rect(x, y, 5, 5)
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
  
  boxTCs = []
  
  for box in gridCs:
    pygame.draw.rect(screen, "red", box)
      
  #update and draw items
  for box in boxes:
    pygame.draw.rect(screen, "purple", box)
    if box.width > box.height:
      boxTC = pygame.Rect(box.x + box.width/2+box.width/4 , box.y + box.height/2, 5, 5)
      pygame.draw.rect(screen, "red", boxTC)
      boxTCs.append(boxTC)
      boxTC = pygame.Rect(box.x + box.width/2-box.width/4 , box.y + box.height/2, 5, 5)
      pygame.draw.rect(screen, "red", boxTC)
      boxTCs.append(boxTC)
    else:
      boxTC = pygame.Rect(box.x + box.width/2, box.y + box.height/2 + box.height/4, 5, 5)
      pygame.draw.rect(screen, "red", boxTC)
      boxTCs.append(boxTC)
      boxTC = pygame.Rect(box.x + box.width/2, box.y + box.height/2 - box.height/4, 5, 5)
      pygame.draw.rect(screen, "red", boxTC)
      boxTCs.append(boxTC)
        


  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        for num, box in enumerate(boxes):
          if box.collidepoint(event.pos):
            active_box = num

    if event.type == pygame.MOUSEBUTTONUP:
      if event.button == 1:
        if active_box != None:
            print(str(boxes[active_box].x) + "," + str(boxes[active_box].y))
            if boxes[active_box].width >= boxes[active_box].height:
              winner = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
              winners = []
              for gc in range(len(gridCs)-1):
                x = 0
                for bc in range(len(boxTCs)):
                  x = x + abs(boxTCs[bc].x - gridCs[gc].x)
                  x = x + abs(boxTCs[bc].y - gridCs[gc].y)
                  x = x + abs(boxTCs[bc].x - gridCs[gc+1].x)
                  x = x + abs(boxTCs[bc].y - gridCs[gc+1].y)
                if x < winner:
                  winner = x
                  winners = []
                  winners.append(gridCs[gc])
                  winners.append(gridCs[gc+1])
              if winners[0].x + winners[0].y <= winners[1].x + winners[1].y:
                print(str(winners[0].x) + "," + str(winners[0].y) + "<---- update pos to")
                boxes[active_box].x = winners[0].x - 37
                boxes[active_box].y = winners[0].y - 37
              else:
                boxes[active_box].x = winners[1].x - 37
                boxes[active_box].y = winners[1].y - 37
                print(str(winners[1].x) + "," + str(winners[1].y) + "<---- update pos to")
            else:
              print("try the other one")
            active_box = None

    if event.type == pygame.MOUSEMOTION:
      if active_box != None:
        boxes[active_box].move_ip(event.rel)

    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()