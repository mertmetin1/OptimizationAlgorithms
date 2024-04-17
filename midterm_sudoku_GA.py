import colorama
from colorama import Fore, Style
import os
import time

# Colorama'yı başlat
colorama.init()

def clear_console():
    # Konsolu temizle
    os.system('cls' if os.name == 'nt' else 'clear')

def is_valid_move(board, row, col, num):
    # Verilen sayının belirli bir hücreye atanıp atanamayacağını kontrol eder
    # Aynı satırda, sütunda ve 3x3'lük blokta aynı sayıdan başka olmamasını kontrol eder
    # Geçerliyse True, değilse False döner
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True

def find_empty_cell(board):
    # Boş bir hücre bulur ve konumunu (satır, sütun) olarak döndürür
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Tüm hücreler dolu, çözüm tamamlandı
    current_row, current_col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, current_row, current_col, num):
            board[current_row][current_col] = num  # Belirli bir sayıyı ata
            clear_console()  # Konsolu temizle
            print_board(board, current_row, current_col)  # Board'u yazdır
            print(f"Checking row {current_row}, column {current_col} for number {num}")
            print()
            #time.sleep(0.01)  # İşlemi yavaşlat
            if solve_sudoku(board):  # Rekürsif olarak sonraki boş hücreleri çözmek için çağır
                return True
            board[current_row][current_col] = 0  # Geri adım
    return False  # Bu durumda, geçerli bir çözüm yok

def print_board(board, current_row=None, current_col=None):
    # Board'u karakterlerle yazdır
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                print('.', end=' ')  # Boş hücreleri '.' ile göster
            elif i == current_row and j == current_col:
                print(Fore.RED + str(board[i][j]), end=' ')  # Kontrol edilen hücreyi kırmızı renkte yazdır
            elif i == current_row or j == current_col:
                print(Fore.BLUE + str(board[i][j]), end=' ')  # Kontrol edilen satır veya sütundaki sayıları mavi renkte yazdır
            else:
                print(board[i][j], end=' ')  # Diğer sayıları direk yazdır
            if (j + 1) % 3 == 0 and j != 8:
                print('|', end=' ')
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)

# Sudoku bulmacasını temsil eden bir başlangıç durumu
initial_state = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def empty_sudoku_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    return board
# Boş bir Sudoku tahtası oluştur
empty_board = empty_sudoku_board()
# Sudoku çözümü
if solve_sudoku(initial_state):
    print(Fore.GREEN + "Sudoku Bulmacasının Çözümü:" + Style.RESET_ALL)
    print_board(initial_state)  # Çözümü yazdır
else:
    print(Fore.RED + "Çözüm bulunamadı." + Style.RESET_ALL)
