import os


def factorial(num):
    if type(num) != int:
        raise TypeError
    if num < 0:
        raise ValueError
    if num < 2:
        return 1
    return num * factorial(num - 1)


def add(num_a, num_b):
    if type(num_a) != int or type(num_b) != int:
        raise TypeError
    return num_a + num_b


def sub(num_a, num_b):
    if type(num_a) != int or type(num_b) != int:
        raise TypeError
    return num_a - num_b


def root(num, index):
    if type(num) != int or type(index) != int:
        raise TypeError
    if num < 0 and index % 2 == 0:
        raise ValueError
    return num ** (1 / index)


menu = {
    1: 'Dodawanie',
    2: 'Odejmowanie',
    3: 'Pierwiastek',
    4: 'Silnia',
    5: 'Wyjscie'
}


def show_menu():
    for key in menu.keys():
        print(key, ': ', menu[key])


if __name__ == '__main__':
    while True:
        show_menu()
        selected_action = ''
        try:
            selected_action = int(input('Wybierz dzialanie: '))
        except ValueError:
            print('Wybierz od 1 do 5...')
        if selected_action == 1:
            a = int(input("Pierwsza liczba: "))
            b = int(input("Druga liczba: "))
            print("Wynik: ", add(a, b))
            print("__________")
            # os.system('read -s -n 1 -p "Nacisnij dowolny klawisz"')
        elif selected_action == 2:
            a = int(input("Pierwsza liczba: "))
            b = int(input("Druga liczba: "))
            print("Wynik: ", sub(a, b))
            print("__________")
            # os.system('read -s -n 1 -p "Nacisnij dowolny klawisz"')
        elif selected_action == 3:
            a = int(input("Liczba: "))
            b = int(input("Stopien pierwiastka: "))
            print("Wynik: ", root(a, b))
            print("__________")
            # os.system('read -s -n 1 -p "Nacisnij dowolny klawisz"')
        elif selected_action == 4:
            a = int(input("Liczba: "))
            print("Wynik: ", factorial(a))
            print("__________")
            # os.system('read -s -n 1 -p "Nacisnij dowolny klawisz"')
        elif selected_action == 5:
            print('Wyjscie')
            exit()
        else:
            print('Wybierz od 1 do 5...')
