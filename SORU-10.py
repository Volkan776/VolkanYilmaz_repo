CUMLE = input("KELİME GİR: ")
sesli_harfler = "aeıioöuü"
sesli_sayisi = 0
for harf in CUMLE:
      if harf.lower() in sesli_harfler:
        sesli_sayisi += 1
        print(sesli_sayisi)




