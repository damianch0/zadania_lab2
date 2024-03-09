a = int(input("Podaj liczbe: "))

if a > 1:
    for i in range(2, a // 2):
        if a % i == 0:
            print("Nie jest liczba pierwsza")
            break
    else:
        print("Jest liczba pierwsza")
else:
    print("Nie jest liczba pierwsza")