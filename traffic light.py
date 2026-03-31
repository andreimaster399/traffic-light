print('Привет, я светофор')
input('Чтобы запустить светофор нажми ENTER')

from time import sleep as ts
import os
while True:
    for a in range(10, 0, -1):
        print('Красный цвет 🔴')
        print(a)
        ts(1)
        def clear_terminal():
            os.system('cls' if os.name == 'nt' else 'clear')
        if __name__ == "__main__":
            clear_terminal()
    for b in range(5, 0, -1):
        print('Желтый цвет 🟡')
        print(b)
        ts(1)
        def clear_terminal():
            os.system('cls' if os.name == 'nt' else 'clear')
        if __name__ == "__main__":
            clear_terminal()
    for c in range(10, 0, -1):
        print('Зелёный цвет 🟢')
        print(c)
        ts(1)
        def clear_terminal():
            os.system('cls' if os.name == 'nt' else 'clear')
        if __name__ == "__main__":
            clear_terminal()

