#hi all
#rnbqkbnr/pppppp1p/8/6p1/5P2/8/PPPPP1PP/RNBQKBNR w KQkq - 0 2
from random import randint
import chess
import datetime

scores = {'p':1, 'n':3, 'b':3, 'r':5, 'q':9}

# board = chess.Board()
def max(board):
    hyp_board = board.copy()
    legal_moves_w = (hyp_board.legal_moves)

    best_score = float('-inf')
    best_move = None
    #get all legal moves you could make with white/black
    for move1 in legal_moves_w:
        score = 0
        #for each move, check if it's a capture, if it is, add the value to your score
        if hyp_board.is_capture(move1):
            piece = hyp_board.piece_at(chess.parse_square((str(move1))[2:4]))
            value = scores[str(piece).lower()]
            score += value
            print('capture', value)
            
            if score > best_score:
              # new best move !!
              print('taken', -1*value)
              print("score", score)
              best_score = score
              best_move = move1
        
            # hyp_board.push(move1)
        # for move2 in ....
        #     score = positive or zero score for white move  + negative or zero score for black move j
        #     if score > best_score
        #     # new best move !!
        #     best_score = score
        #     best_move = i
        
        #next step: make sure white takes lowest score val move
    print("SCORE**************************", score)
    if best_move == None:
      print('no capture moves')
      best_move = list(legal_moves_w)[randint(0, len(list(legal_moves_w))-1)]
    return best_move
    

def min(board):
  return


def minimax()

def computerChooseMove(board):

    hyp_board = board.copy()
    legal_moves_w = (hyp_board.legal_moves)
    

    best_score = float('-inf')
    best_move = None
    #get all legal moves you could make with white/black
    for move1 in legal_moves_w:
        score = 0
        #for each move, check if it's a capture, if it is, add the value to your score
        if hyp_board.is_capture(move1):
            piece = hyp_board.piece_at(chess.parse_square((str(move1))[2:4]))
            value = scores[str(piece).lower()]
            score += value
            print('capture', value)
            hyp_board.push(move1)
            legal_moves_b = hyp_board.legal_moves
            for move2 in legal_moves_b:
                if hyp_board.is_capture(move2):
                    piece = hyp_board.piece_at(chess.parse_square((str(move2))[2:4]))
                    value = scores[str(piece).lower()]
                    score -= value

                if score > best_score:
                  # new best move !!
                  print('taken', -1*value)
                  print("score", score)
                  best_score = score
                  best_move = move1
            hyp_board.pop()
            

            # hyp_board.push(move1)
        # for move2 in ....
        #     score = positive or zero score for white move  + negative or zero score for black move j
        #     if score > best_score
        #     # new best move !!
        #     best_score = score
        #     best_move = i
        
        #next step: make sure white takes lowest score val move
    print("SCORE**************************", score)
    if best_move == None:
      print('no capture moves')
      best_move = list(legal_moves_w)[randint(0, len(list(legal_moves_w))-1)]
      return best_move
    else:
      return best_move
      
            
    #find moves white can do
      # legal_moves = list(board.legal_moves)
      
      # capture_moves = []
      # for move in legal_moves:
      #     if board.is_capture(move):
      #         capture_moves.append(move)
      
      # if not capture_moves: #if list is empty
      #     random_move = legal_moves[randint(0, len(legal_moves)-1)]
      # else:
      #     random_move = capture_moves[randint(0, len(capture_moves)-1)]
      # return random_move


  #If one or more moves are available which capture an enemy piece, 
  # your program should always choose one of the capture moves.  Otherwise, program should 
  # randomly choose a move from among all of the available valid moves. 
  

def computerWhite(board):
  #do the first move, f2f4
  # first_move = chess.Move.from_uci("f2f4")

  while board.outcome() is None:

    first_move = computerChooseMove(board)
    print("computer move (white): ", first_move)
    board.push(first_move)
    print(board.fen())
    print(board)
    # if board.is_checkmate():
    #   print("Checkmate!")
    if board.outcome() is not None:
      break


    #Black makes move
    black_first_move = chess.Move.from_uci(input('Black: '))
    while black_first_move not in board.legal_moves:
      black_first_move = chess.Move.from_uci(input('Move not legal. Pls enter new move: '))
    board.push(black_first_move)
    print("New FEN Position: " + board.fen())
    print(board)

  
  return board

  

  # computerChooseMove(board.fen(), board)

def computerBlack(board):
  while (board.outcome()) is None:

    #white makes first move
    white_first_move = chess.Move.from_uci(input('White: '))
    while white_first_move not in board.legal_moves:
      white_first_move = chess.Move.from_uci(input('Move not legal. Pls enter new move: '))
    board.push(white_first_move)
    print("New FEN Position: " + board.fen())
    print(board)
    # if board.is_checkmate():
    #   print("Checkmate!")
    if board.outcome():
      break

    first_move = computerChooseMove(board)
    print("computer move (black): ", first_move)
    board.push(first_move)
    print(board.fen())
    print(board)

  return board


def botsPlay(board):
  #do the first move, f2f4
  # first_move = chess.Move.from_uci("f2f4")

  while not board.outcome():

    first_move = computerChooseMove(board)
    print("computer move (white): ", first_move)
    board.push(first_move)
    print(board.fen())
    print(board)
    # if board.is_checkmate():
    #   print("Checkmate!")
    if board.outcome():
      break


    #Black makes move
    black_first_move = computerChooseMove(board)
    while black_first_move not in board.legal_moves:
      black_first_move = chess.Move.from_uci(input('Move not legal. Pls enter new move: '))
    board.push(black_first_move)
    print("New FEN Position: " + board.fen())
    print(board)
  
  

  return

def main():
  print('=====================================================\nCS 290 Chess Bot Version 0.1\n=====================================================')
  #date and time
  x = datetime.datetime.now()
  print('Time: ', x)
  computer_player = input('Computer Player (w=white/b=black): ')
  starting_FEN = input('Starting FEN position? (enter for standard starting position): ')
  if starting_FEN == '':
    board = chess.Board()
  else:
    board = chess.Board(starting_FEN)
  print(board)
  print(board.fen())
  if computer_player == 'w':
    computerWhite(board)
  elif computer_player == 'b':
    computerBlack(board)
  elif computer_player == 'bots':
    botsPlay(board)

  if board.is_checkmate():
    print("Checkmate!")
  if board.is_stalemate():
    print("It's a tie!")
  elif board.is_insufficient_material():
    print("Neither side has sufficient enough material to win!")
  
  #in a loop:
  #white move, new fen, black moves, new fen.
  #maybe after ea move, should check if anyone has won or sth? and before ea computer turn, the computer needs a list of moves (board.legal_moves)

if __name__ == "__main__":
  main()