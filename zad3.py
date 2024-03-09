text = input("Podaj tekst")

for t in range(len(text)):
    if text[t] != text[len(text) - 1 - t]:
        print("Tekst nie jest palindromem")
        break
else:
    print("podany tekst jest palindromem ")
