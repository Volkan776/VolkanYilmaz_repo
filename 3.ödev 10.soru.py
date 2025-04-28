liste = [1, 2, -3, 4, 5, -6, 7, 8, 9, -10, 21, -24, 46, -89, 68, -90, -100]
negatifler = []
for sayi in liste:
    if sayi < 0:
        negatifler.append(sayi)
print(negatifler)
