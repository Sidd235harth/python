VALID_PIECES = {
    'pawn': 8,
    'knight': 2,
    'bishop': 2,
    'rook': 2,
    'queen': 1,
    'king': 1
}

VALID_COLORS = {'w', 'b'}
VALID_COLUMNS = 'abcdefgh'
VALID_ROWS = '12345678'

def is_valid_position(pos):
    return len(pos) == 2 and pos[0] in VALID_ROWS and pos[1] in VALID_COLUMNS

def validate_chess_board(chess_dict):
    piece_count = {'w': {}, 'b': {}}
    king_count = {'w': 0, 'b': 0}

    for position, piece in chess_dict.items():
        if not is_valid_position(position):
            print(f"Invalid position: {position}")
            return False

        if len(piece) < 2 or piece[0] not in VALID_COLORS:
            print(f"Invalid piece identifier: {piece}")
            return False

        color = piece[0]
        name = piece[1:]

        if name not in VALID_PIECES:
            print(f"Invalid piece name: {name}")
            return False

        if name == 'king':
            king_count[color] += 1

        piece_count[color][name] = piece_count[color].get(name, 0) + 1
        if piece_count[color][name] > VALID_PIECES[name]:
            print(f"Too many {color + name}s on the board.")
            return False

    if king_count['w'] != 1 or king_count['b'] != 1:
        print("Each side must have exactly one king.")
        return False

    print("Chess board is valid.")
    return True

# Example usage
if __name__ == "__main__":
    chess_board = {
        '1a': 'wrook',
        '1b': 'wknight',
        '1c': 'wbishop',
        '1d': 'wqueen',
        '1e': 'wking',
        '1f': 'wbishop',
        '1g': 'wknight',
        '1h': 'wrook',
        '2a': 'wpawn',
        '2b': 'wpawn',
        '2c': 'wpawn',
        '2d': 'wpawn',
        '2e': 'wpawn',
        '2f': 'wpawn',
        '2g': 'wpawn',
        '2h': 'wpawn',
        '8a': 'brook',
        '8b': 'bknight',
        '8c': 'bbishop',
        '8d': 'bqueen',
        '8e': 'bking',
        '8f': 'bbishop',
        '8g': 'bknight',
        '8h': 'brook',
        '7a': 'bpawn',
        '7b': 'bpawn',
        '7c': 'bpawn',
        '7d': 'bpawn',
        '7e': 'bpawn',
        '7f': 'bpawn',
        '7g': 'bpawn',
        '7h': 'bpawn'
    }

    validate_chess_board(chess_board)
