# Игра

# Рисуем поле

pole = [[" "] * 3 for i in range (3)]
def pole_():
    print()
    print ("       1   2   3  ")
    for i, i_ in enumerate (pole):
        print("     -------------")
        pole_ris = f"  {i+1}  | {' | '.join (i_)} | "
        print(pole_ris)
    print("     -------------")

# Комбинация победителя

def pobeda_():
    pob_kod = (((0, 0), (0, 1), (0, 2)),
               ((1, 0), (1, 1), (1, 2)),
               ((2, 0), (2, 1), (2, 2)),
               ((0, 2), (1, 1), (2, 0)),
               ((0, 0), (1, 1), (2, 2)),
               ((0, 0), (1, 0), (2, 0)),
               ((0, 1), (1, 1), (2, 1)),
               ((0, 2), (1, 2), (2, 2)))
    for kod_ in pob_kod:
        znak_ = []
        for i in kod_:
            znak_.append(pole[i[0]][i[1]])
        if znak_ == ["X", "X", "X"]:
            print("--------------------------------------------------------")
            print("В ы и г р а л   и г р о к   с о   з н а к о м   <X>  !!!")
            return True

        if znak_ == ["O", "O", "O"]:
            print("--------------------------------------------------------")
            print("В ы и г р а л   и г р о к   с о   з н а к о м   <O>  !!!")
            return True
    return False
pobeda_()

# ВВод игроком

def vvod_():
    while True:
        vopros = "     Неверно, координаты цифрами c 1 до 3 "
        koordinat_ = input("                               координаты: ").split()

        pobeda_()
        if len(koordinat_) != 2:
            print(vopros)
            continue
        x, y = koordinat_

        if not (x.isdigit()) or not (y.isdigit()):
            print(vopros)
            continue

        if 1 > int (x) or int (x) > 3 or int (y) < 1 or int (y) > 3:
            print(vopros)
            continue

        if pole[int(x)-1][int(y)-1] != " ":
            print("                     данная клетка занята")
            continue

        return x, y

# Очередность хода, ничья

number_ = 0
while True:
    number_ += 1
    pole_()

    if number_ % 2 == 1:
        print()
        print("  Очередь хода игрока со знаком X,введите")
    else:
        print ()
        print ("  Очередь хода игрока со знаком O,введите")

    x, y = vvod_()


    if number_ % 2 == 1:
        pole[int(x)-1][int(y)-1] = "X"
    else:
        pole[int(x)-1][int(y)-1] = "O"

    if pobeda_():
        pole_()
        break
    if number_ == 9:
        print ("      В этой партии победитель не выявлен.")
        break



