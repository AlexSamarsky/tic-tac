import re

win_states = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [1, 4, 8],
    [2, 4, 6],
]

def get_start():
    arr = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print('\n\nНовая игра, давайте начнем!')
    print_board(arr)
    return arr, 'X'

def check_win(arr):
    for win_arr in win_states:
        if len(set(win_arr).intersection(set(arr))) == 3:
            return True
    return False


def check_winner(arr):
    x_arr = []
    o_arr = []
    turn = 0
    for i in range(0, 9):
        if arr[i].upper() == 'X':
            x_arr.append(i)
            turn += 1
        elif arr[i].upper() == 'O':
            o_arr.append(i)
            turn += 1
    if turn == 9:
        return -1
    elif check_win(x_arr):
        return 'X'
    elif check_win(o_arr):
        return 'O'
    else:
        return None


def print_board(arr):
    print ('  0 1 2')
    for i in range(0, 9):
        row = i // 3
        col = i % 3
        if col == 0:
            str = f'{row}'
        str += f' {arr[i]}'
        if col == 2:
            print (str)

def make_turn(arr, coords, whos_turn):
    match = re.search('[012] [012]', coords)
    if not match:
        print ('\n\nОшибка ввода координат!!!')
        return arr, whos_turn, None
    else:
        col_row = coords.split()
        arr_number = int(col_row[0]) * 3 + int(col_row[1])
        winner = None
        if arr[arr_number] == ' ':
            arr[arr_number] = whos_turn
            whos_turn = 'X' if whos_turn == 'O' else 'O'
            winner = check_winner(arr)
        else:
            print (f'Координата {coords} занята!')
        return arr, whos_turn, winner
        

def will_begin_new_game():
    if winner == -1:
        new_game = input(f'Игра закончилась вничью, начать новую? Y для продолжения: ')
    else:
        new_game = input(f'Поздравляем, есть победитель {winner}. Игра закончена, начать новую? Y для продолжения: ')
    match = re.search('\w', new_game)
    if match:
        if new_game.upper() == 'Y':
            return True
        elif new_game.upper() == 'N':
            print('Игра завершена! Спасибо за участие')
            return False
        else:
            print('Введен непонятный символ, игра будет завершена! Спасибо за участие')
            return False
    else:
        print('Введен непонятный символ, игра будет завершена! Спасибо за участие')
        return True


if __name__ == '__main__':
    arr, whos_turn = get_start()
    while True:
        coords = input(f'Ход "{whos_turn}", введите координаты в формате (строка) (колонка), (например: 1 0) : ')
        arr, whos_turn, winner = make_turn(arr, coords, whos_turn)
        print_board(arr)
        if winner:
            if will_begin_new_game():
                arr, whos_turn = get_start()
            else:
                break
