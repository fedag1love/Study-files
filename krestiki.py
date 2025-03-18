n = [['-', '-', '-'],['-', '-', '-'], ['-', '-', '-']]
def field(board): #Функция создания двумерного игрового поля
    print('  0 1 2')
    for i, row in enumerate(board):
        print(f'{i} {' '.join(row)}')

def game_end(board): #Проверка условий на победу
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

    for row in board:
        if '-' in row:
            return None

    return "Ничья"

def turnx(): #Функция хода для игрока 1
    while True:
        x, y = [int(x) for x in input('Введите строку и столбец куда хотите поставить Х (формат х у, от 0 до 2) : ').split()]
        if n[x][y] == '-':
            n[x][y] = 'X'
            field(n)
            break
        else:
            print("Клетка уже занята, попробуйте еще раз.")


def turn0(): #Функция хода для игрока 2
    while True:
        x, y = [int(x) for x in input('Введите строку и столбец куда хотите поставить Х (формат х у, от 0 до 2) : ').split()]
        if n[x][y] == '-':
            n[x][y] = '0'
            field(n)
            break
        else:
            print("Клетка уже занята, попробуйте еще раз.")


def game():
    while True:
        turnx()
        result = game_end(n)
        if result is not None:
            if result == "Ничья":
                print("Ничья!")
            else:
                print(f"Игрок {result} выиграл!")
            break

        turn0()
        result = game_end(n)
        if result is not None:
            if result == "Ничья":
                print("Ничья!")
            else:
                print(f"Игрок {result} выиграл!")
            break
game()