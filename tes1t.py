def empty_sudoku_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    return board

def print_sudoku_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Boş bir Sudoku tahtası oluştur
empty_board = empty_sudoku_board()

# Oluşturulan boş tahtayı yazdır
print("Empty Sudoku Board:")
print_sudoku_board(empty_board)
