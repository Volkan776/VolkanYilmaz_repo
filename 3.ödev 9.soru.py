sayilar = [1 ,12, 7, 3, 5,9,8,21,64,74,52]
buyukler=[]
for i in range(len(sayilar)):
  if i > 0:
    if sayilar[i] > sayilar[i-1]:
      buyukler.append(sayilar[i])
      print(buyukler)
      
