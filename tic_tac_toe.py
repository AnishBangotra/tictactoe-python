#-------------------Global Variables------------------------
#Game Board
board=['-','-','-',
      '-','-','-',
      '-','-','-']
#assigning a bool value to run it true as default in while loop and false it when check_if_game_over is true
game_is_going=True
#current player let's start with X
current_player='X'
#winner taking as none until check_if_game_over comes true
winner = None

#lets start defining a function play_game in which all the functions run
def play_game():
#it doesn't matter for display_board()that it defines under the function in which it is calling, we usually calls when we need the output
  display_board()
  print('Welcome to TIC/TAC/TOE game,  Its X Turn')
#while the game is going
  while game_is_going:
#handel turn of the first arbitary player
    handel_turns(current_player)
#check for win and tie
    check_if_game_over()
#flip player after a turn
    flip_player()

#conditions for winner when check_if_game_over gets true it reads this and exit the loop bcz game_is_going get false
  if winner =='X' or winner =='0':
    print(winner +' Won!')
  elif winner == None:
    print("Tie.")

#display function
def display_board():
  print(board[0]+'|'+ board[1]+'|'+board[2]+'     1 | 2 | 3')
  print(board[3]+'|'+ board[4]+'|'+board[5]+'     4 | 5 | 6')
  print(board[6]+'|'+ board[7]+'|'+board[8]+'     7 | 8 | 9')

 #handling turns for X and 0
def handel_turns(player):
    print('Its '+player+"'s turn'")
    position=input('Enter the position in betwen 1/9...')
    while position not in ['1','2','3','4','5','6','7','8','9']:
      position=input('Invalid input, try values in between 1/9')
    position=int(position)-1
  #how to assign it on board
  #we do as index for board
    board[position] = player
    display_board()
  #again display_board() the result of assigning X


def check_if_game_over():
  # check_win'
  #but here we want to update winner but winner is gloabl outside and if we want to use it inside function we must declare it as a global

  check_win()
  check_tie()
  return


def check_win():
  global winner
  #storing check_rows function
  rows_winner=check_rows()

  columns_winner=check_columns()

  diagonals_winner=check_diagonals()


  if rows_winner:
   winner=rows_winner

  elif columns_winner:
   winner=columns_winner

  elif diagonals_winner:
   winner=diagonals_winner
  else:
    winner=None


#check win in rows
def check_rows():
  global game_is_going
  r1=board[0]==board[1]==board[2]!='-'
  r2=board[3]==board[4]==board[5]!='-'
  r3=board[6]==board[7]==board[8]!='-'

  if r1 or r2 or r3:
    game_is_going = False
  if r1:
    return board[0]
  elif r2:
    return board[3]
  elif r3:
    return board[6]
  else:
    return None
#check win in columns
def check_columns():
  global game_is_going
  c1=board[0]==board[3]==board[6]!='-'
  c2=board[1]==board[4]==board[7]!='-'
  c3=board[2]==board[5]==board[8]!='-'

  if c1 or c2 or c3:
    game_is_going = False
  if c1:
    return board[0]
  elif c2:
    return board[1]
  elif c3:
    return board[2]
  else:
    return None
#chech win in diagonals
def check_diagonals():
  global game_is_going
  d1=board[0]==board[4]==board[8]!='-'
  d2=board[2]==board[4]==board[6]!='-'

  if d1 or d2:
    game_is_going = False
  if d1:
    return board[0]
  elif d2:
    return board[2]
  else:
    return None

#check for tie
def check_tie():
  global game_is_going
  if '-' not in board:
   game_is_going = False
   return True
  #eles there's no tie return False
  else:
   return False

 #flipping current player
def flip_player():
  global current_player
  if current_player=='X':
    current_player = '0'
  elif current_player=='0':
    current_player = 'X'



play_game()
#end the function when game is over by calling play_game()
