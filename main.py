CUMLE = input("BİŞİ YAZIN: ")
sayi = int(input("SAYI GİR: "))
harf = input("CÜMLEDİ Kİ BİR HARFİ DEĞİŞTİR: ")
yeni_CUMLE = CUMLE[:sayi] + harf + CUMLE[sayi+1:]
print(yeni_CUMLE)
