from random import randint

#CREATE BOARD
board = []


for x in range(5):
  board.append(["O"] * 5) #add stuff to the end of the list 


def print_board(board):
    
  for row in board:
      
    print(" ".join(row)) #join all elements from the iterable, create string and return output to user


print("Welcome to Battleship!")

print_board(board)


def random_row(board):
  return randint(0, len(board) - 1) #len command returns the length of the object


def random_col(board):
    
  return randint(0, len(board[0]) - 1)


ship_row = random_row(board)

ship_col = random_col(board)

# print(ship_row)
# print(ship_col)


for turn in range(9):
    
  print("Turn", turn + 1)
  
  guess_row = int(input("Guess Row:"))
  guess_col = int(input("Guess Col:"))


  if guess_row == ship_row and guess_col == ship_col:
      
    print("Argg! YOU SANK MY SHIP!")
    
    break

  else:
      
    if guess_row != int or guess_col != int:
     
        print("fbjfju")
      
    
    elif():
        
        guess_row not in range(5) or \
        guess_col not in range(5)
        print("ARE YOU AIMING FOR LAND!?")

      
      
      
    elif board[guess_row][guess_col] == "X":
        
      print("Select a location that you have not already chosen.")
      
      
    else:
        
      print("YOU MISSED! Give it another shot. ")
      board[guess_row][guess_col] = "X"
      
      
    if (turn == 8):
        
      print("Too many attempts. GAME OVER LOSER!")
      
      
    print_board(board)
