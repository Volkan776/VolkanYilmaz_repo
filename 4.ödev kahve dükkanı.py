kahve_fiyatlari = {
    "Espresso": 15,
    "Americano": 18,
    "Latte": 20,
}

fincan_fiyatlari = {
    "Orta": 0,
    "Büyük": 3,
    "XL": 5
}

siparis_turu_fiyat = 0

print("Kahve Siparişi Sistemi")

kahve_turu = input("Hangi kahve türünü istersiniz? (Espresso, Americano, Latte,): ")

while True:
    if kahve_turu == "Espresso" or kahve_turu == "Americano" or kahve_turu == "Latte":
        break
    else:
        print("Geçersiz kahve türü. Lütfen belirtilen seçeneklerden birini girin.")
        kahve_turu = input("Hangi kahve türünü istersiniz? (Espresso, Americano, Latte,): ")

fincan_boyutu = input("Hangi boyutta kahve istersiniz? (Orta, Büyük, XL): ")

while True:
    if fincan_boyutu == "Orta" or fincan_boyutu == "Büyük" or fincan_boyutu == "XL":
        break
    else:
        print("Geçersiz fincan boyutu. Lütfen Orta, Büyük veya XL seçin.")
        fincan_boyutu = input("Hangi boyutta kahve istersiniz? (Orta, Büyük, XL): ")

siparis_turu = input("İçeride mi yoksa dışarıda mı? (İçeride/Dışarıda): ")

if siparis_turu.lower() == "dışarıda":
    siparis_turu_fiyat = 2

kahve_fiyati = kahve_fiyatlari[kahve_turu] + fincan_fiyatlari[fincan_boyutu] + siparis_turu_fiyat

print("Sipariş Özeti:")
print("Kahve Türü: " + kahve_turu)
print("Fincan Boyutu: " + fincan_boyutu)
print("Sipariş Türü: " + siparis_turu)
print("Toplam Fiyat: " + str(kahve_fiyati) + " TL")
