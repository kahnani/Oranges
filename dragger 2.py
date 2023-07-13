import pygame
import random

pygame.init()

#game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ships That Happen To Battle')

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
        
run = True
while run:

  screen.fill("turquoise1")
  draw_grid()
  box1 = pygame.Rect(300, 426, 401, 201)
  pygame.draw.rect(screen, "turquoise1", box1)
  box2 = pygame.Rect(676, 50, 300, 600)
  pygame.draw.rect(screen, "turquoise1", box2)
  boxTCs = []
  #update and draw items
  for box in boxes:
    pygame.draw.rect(screen, "purple", box)
    for i in range(2):
        boxTC = pygame.Rect(box.x + box.width/2 , box.y + box.height/2, 5, 5)
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
            active_box = None

    if event.type == pygame.MOUSEMOTION:
      if active_box != None:
        boxes[active_box].move_ip(event.rel)

    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()