lista = [1, "napis", 2.3, "inny napis", "napis"]
dict = {}

for x in lista:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

print(dict)

for x in list(dict.keys()):
    if not (isinstance(x, float) or isinstance(x, int)):
        print(x)
        del dict[x]

print(dict)
