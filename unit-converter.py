def conversion_options():
    print()
    print("*** Konwerter jednostek ***")
    print()
    print("1. Zamień centymetry na metry")
    print("2. Zamień centymetry na cale")
    print("3. Zamień metry na centymetry")
    print("4. Zamień metry na cale")
    print("5. Zamień cale na metry")
    print("6. Zamień cale na centymetry")
    print("0. Wyjdź z programu")
    print()

choice = -10000

while choice != 0:
    conversion_options()
    value = int(input("Podaj wartość do konwersji: "))
    choice = int(input("Wybierz numer operacji, którą chcesz wykonać: "))
    if choice == 0:
        break

    if choice == 1:
        result = value / 100
        print("{:.2f} cm to {:.2f} m".format(value, result))

    elif choice == 2:
        result = value / 2.54
        print("{:.2f} cm to {:.2f} cali".format(value, result))

    elif choice == 3:
        result = value * 100
        print("{:.2f} m to {:.2f} cm".format(value, result))

    elif choice == 4:
        result = value / 0.0254
        print("{:.2f} m to {:.2f} cali".format(value, result))

    elif choice == 5:
        result = value * 0.0254
        print("{:.2f} cali to {:.2f} m".format(value, result))

    elif choice == 6:
        result = value * 2.54
        print("{:.2f} cali to {:.2f} cm".format(value, result))
    else: 
        print("Nie ma takiego numeru. Spróbuj jeszcze raz.")
    




