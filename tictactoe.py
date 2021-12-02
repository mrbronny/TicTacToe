def print_board(board):
  for row in board:
      for character in row:
        print(character, end = " ")
      print()

def check_board4win(board):
  p1 = board[0][0] + board[0][1] + board[0][2]
  p2 = board[1][0] + board[1][1] + board[1][2]
  p3 = board[2][0] + board[2][1] + board[2][2]
  p4 = board[0][0] + board[1][0] + board[2][0]
  p5 = board[0][1] + board[1][1] + board[2][1]
  p6 = board[0][2] + board[1][2] + board[2][2]
  p7 = board[0][0] + board[1][1] + board[2][2]
  p8 = board[0][2] + board[1][1] + board[2][0]
  plyst = [p1, p2, p3, p4, p5, p6, p7, p8]
  for p in plyst:
    winner = check_row4win(p)
    if winner:
      return winner
  return None

def check_row4win(possibility):
  xs = 0
  os = 0
  for symbol in possibility:
    if symbol == "X":
      xs += 1
    elif symbol == "O":
      os += 1
    if xs == 3:
      return "X"
    elif os == 3:
      return "O"
  return None

def validate_input(user_input, board):
  if len(user_input) != 2:
    return False
  for character in user_input:
    if not is_integer(character):
      return False
  row = int(user_input[0])-1
  column = int(user_input[1])-1
  if row > 2 or row < 0 or column > 2 or column < 0:
    return False
  if board[row][column] != "_":
    return False
  return True

def is_integer(n):
  try:
    float(n)
    return True
  except:
    return False

def play():
  turn = "X"
  counter = 0
  game_board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
  while True:
    print_board(game_board)
    winner = check_board4win(game_board)
    if winner:
      print(f"\n{winner} WINS!")
      break
    if counter == 9:
      print("CAT'S GAME!")
      break
    user_input = input(f"\n{turn}'s turn\nType rc:\n")
    while True:
      if validate_input(user_input, game_board):
        break
      user_input = input(f"Invalid input, {turn}. Try again\n")
    if turn == "X":
      row = int(user_input[0])-1
      column = int(user_input[1])-1
      game_board[row][column] = "X"
      turn = "O"
    elif turn == "O":
      row = int(user_input[0])-1
      column = int(user_input[1])-1
      game_board[row][column] = "O"
      turn = "X"
    counter += 1