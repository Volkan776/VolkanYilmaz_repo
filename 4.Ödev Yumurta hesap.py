yumurta = int(input("Bu sabah kaç yumurta topladınız? "))
kutu_12 = yumurta // 12
kalan = yumurta % 12
kutu_6 = kalan // 6
kahvaltilik = kalan % 6
print("Bugün ihtiyacınız olan:")
print("12'li kutu:", kutu_12)
print("6'lı kutu:", kutu_6)
print("Kahvaltılık yumurta:", kahvaltilik)
