listy = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
b = 0
set_table = [0, 1, 2, 3, 4, 5, 6, 7, 8]
winning_combinations = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]
while b < 9:

    print(f'Player1, now you have choice in these numbers on table: {set_table}')
    for i, n in enumerate(listy):
        if (i + 1) % 3 == 0:
            print(f'{n}')
        else:
            print(f'{n}|', end='')
    get_number1 = int(input('Please, choose number, where you want to draw: '))
    if get_number1 in set_table:
        pass
    else:
        raise ValueError('Not a number in range 1, 9')
    if get_number1 not in set_table:
        raise ValueError('Has been gotten')
    else:
        pass

    listy[get_number1] = 'X'
    set_table.remove(get_number1)

    for (x, y, z) in winning_combinations:
        if listy[x] == 'X' and listy[y] == 'X' and listy[z] == 'X':
            b = 9
        else:
            pass

    if b == 9 and set_table == []:
        print('draw')

        for i, n in enumerate(listy):
            if (i + 1) % 3 == 0:
                print(f'{n}')
            else:
                print(f'{n}|', end='')

        break

    elif b == 9:
        print('Player 1 won')

        for i, n in enumerate(listy):
            if (i + 1) % 3 == 0:
                print(f'{n}')
            else:
                print(f'{n}|', end='')

        break

    b += 1

    print(f'Player2, now you have choice in these numbers on table: {set_table}')
    for i, n in enumerate(listy):
        if (i + 1) % 3 == 0:
            print(f'{n}')
        else:
            print(f'{n}|', end='')
    get_number2 = int(input('Please, choose number, where you want to draw: '))
    if get_number2 in set_table:
        pass
    else:
        raise ValueError('Not a number in range 1, 9')

    if get_number2 not in set_table:
        raise ValueError('Has been gotten')

    else:
        pass

    listy[get_number2] = 'O'
    set_table.remove(get_number2)

    for (x, y, z) in winning_combinations:
        if listy[x] == 'O' and listy[y] == 'O' and listy[z] == 'O':
            b = 9
        else:
            pass

    if b == 9 and set_table == []:
        print('draw')

        for i, n in enumerate(listy):
            if (i + 1) % 3 == 0:
                print(f'{n}')
            else:
                print(f'{n}|', end='')

        break
    elif b == 9:
        print('Player 2 won')

        for i, n in enumerate(listy):
            if (i + 1) % 3 == 0:
                print(f'{n}')
            else:
                print(f'{n}|', end='')

        break

    b += 1