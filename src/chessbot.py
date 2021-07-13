#####################################
#
#  Visual object recognition based
#        chess bot interface
#
#                 by
#
#          Code Monkey King
#
#####################################

# packages
import cv2
import numpy as np
import pyautogui as pg
import chess

# constants (modify if needed)
BOARD_SIZE = 400
CELL_SIZE = int(BOARD_SIZE / 8)
BOARD_TOP_COORD = 141
BOARD_LEFT_COORD = 5
CONFIDENCE = 0.8
PIECES_PATH = './piece_recognition/pieces/'

# map piece names to FEN chars
piece_names = {
    'black_king': 'k',
    'black_queen': 'q',
    'black_rook': 'r',
    'black_bishop': 'b',
    'black_knight': 'n',
    'black_pawn': 'p',
    'white_knight': 'N',
    'white_pawn': 'P',
    'white_king': 'K',
    'white_queen': 'Q',
    'white_rook': 'R',
    'white_bishop': 'B'
}

# locate piece on image
def locate_piece(screenshot, piece_location):
    # loop over pieces
    for index in range(len(piece_location)):
        piece = piece_location[index]
        
        # draw rectangle around recognized piece
        cv2.rectangle(
            screenshot,
            (piece.left, piece.top),
            (piece.left + piece.width, piece.top + piece.height),
            (0, 0, 255),
            2
        )
    
    # display image
    cv2.imshow('Screenshot', screenshot)
    cv2.waitKey(0)

# convert board image to FEN string
def recognize_position():
    # piece locations
    piece_locations = {
        'black_king': [],
        'black_queen': [],
        'black_rook': [],
        'black_bishop': [],
        'black_knight': [],
        'black_pawn': [],
        'white_knight': [],
        'white_pawn': [],
        'white_king': [],
        'white_queen': [],
        'white_rook': [],
        'white_bishop': []
    }

    # take a board snapshot
    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)
    
    # # loop over piece names
    for piece in piece_names.keys():
        # store piece locations
        for location in pg.locateAllOnScreen(PIECES_PATH + piece + '.png', confidence=CONFIDENCE):
            # false detection flag
            noise = False
            
            # loop over matched pieces
            for position in piece_locations[piece]:
                # noice detection
                if abs(position.left - location.left) < 8 and abs(position.top - location.top) < 8:
                    noise = True
                    break
            
            # skip noice detections
            if noise: continue
            
            # detect piece
            piece_locations[piece].append(location)
            
    # return piece locations 
    return screenshot, piece_locations


################################    
#
#          Main driver
#
################################

screenshot, piece_locations = recognize_position()

for piece in piece_names.keys():
    locate_piece(screenshot, piece_locations[piece])
















