
# 1. ОПРЕДЕЛЯЕМ ВСЕ НЕОБХОДИМЫЕ ФУНКЦИИ ДЛЯ ЭТОЙ ИГРЫ

# Приветствие
def greet():
    print("--------------------")
    print("  Приветствуем Вас  ")
    print("      в игре        ")
    print("  крестики-нолики   ")
    print("--------------------")
    print("  Формат ввода: x y ")
    print("  x - номер строки  ")
    print("  y - номер столбца ")

# # Показываем поле на экране (1-й вариант)
# def show():
#     print(f"  0 1 2")
#     for i in range(3):
#         row_info = " ".join(field[i])
#         print(f"{i}  {row_info}")
# show()

# Показываем поле на экране (2-й вариант)
def show():
    print()
    print("   | 0 | 1 | 2 |")
    print(" --+---+---+---+")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print(" --+---+---+---+")
    print()

# Ввод координат и их проверка
def ask():
    while True:
        coords = input("Ваш ход: ").split()

        if len(coords) != 2:
            print("Введите две координаты!")
            continue

        x, y = coords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Введенные координаты вне диапазона от 0 до 2-х!")
            continue

        if field[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y

# # Проверка выигрышных комбинаций (1-й вариант)
# def check_win():
#     win_coord = [((0, 0),(0, 1),(0, 2)), ((1, 0),(1, 1),(1, 2)), ((2, 0),(2, 1),(2, 2)),
#                  ((0, 0),(1, 0),(2, 0)), ((0, 1),(1, 1),(2, 1)), ((0, 2),(1, 2),(2, 2)),
#                  ((0, 0),(1, 1),(2, 2)), ((0, 2),(1, 1),(2, 0))]
#     for coord in win_coord:
#         symbols = []
#         for c in coord:
#             symbols.append(field[c[0]][c[1]])
#         if symbols == ["x", "x", "x"]:
#             print("Выиграли крестики(X)!")
#             return True
#         if symbols == ["0", "0", "0"]:
#             print("Выиграли нолики(0)!")
#             return True
#     return False

# # Проверка выигрышных комбинаций (2-й вариант)
# def check_win():
#     win_coord = [((0, 0),(0, 1),(0, 2)), ((1, 0),(1, 1),(1, 2)), ((2, 0),(2, 1),(2, 2)),
#                  ((0, 0),(1, 0),(2, 0)), ((0, 1),(1, 1),(2, 1)), ((0, 2),(1, 2),(2, 2)),
#                  ((0, 0),(1, 1),(2, 2)), ((0, 2),(1, 1),(2, 0))]
#     for coord in win_coord:
#         a = coord[0]
#         b = coord[1]
#         c = coord[2]
#
#         if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != " ":
#             print(f"Выиграл {field[a[0]][a[1]]}!")
#             return True
#     return False

# Проверка выигрышных комбинаций (3-й вариант без списка всех возможных комбинаций)
def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["x", "x", "x"]:
            print("Выиграли крестики(X)!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграли нолики(0)!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["x", "x", "x"]:
            print("Выиграли крестики(X)!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграли нолики(0)!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ["x", "x", "x"]:
        print("Выиграли крестики(X)!")
        return True
    if symbols == ["0", "0", "0"]:
        print("Выиграли нолики(0)!")
        return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
    if symbols == ["x", "x", "x"]:
        print("Выиграли крестики(X)!")
        return True
    if symbols == ["0", "0", "0"]:
        print("Выиграли нолики(0)!")
        return True

    return False


# 2. СОЗДАЕМ ИГРОВОЙ ЦИКЛ, ИСПОЛЬЗУЯ ВСЕ ФУНКЦИИ:

greet()         # Запускаем эту функцию, чтобы видеть приветствие на экране

# Создаем поле
field = [[" "]*3 for i in range(3)]

# Определяем, кто будет ходить: "X" или "0"
num = 0         # num - это просто один ход и неважно чей
while True:
    num += 1

    show()      # Запускаем эту функцию, чтобы видеть поле на экране

    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print("Ничья")
        break       # Чтобы завершить цикл