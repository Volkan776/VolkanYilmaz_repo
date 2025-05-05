dondurma_fiyatlari = {
    1: 10,
    2: 12,
    3: 14,
    4: 16
}

servis_fiyatlari = {
    "Külah": 0,
    "Kupa": 2
}

ekstra_fiyatlar = {
    "Mısır Gevreği": 3,
    "Çikolata": 4,
    "Çilek Sosu": 5
}

print("Dondurma Siparişi Sistemi")

servis_secimi = input("Dondurma Külahta mı yoksa Kupada mı olsun? (Kupa/Külah): ")

while True:
    if servis_secimi == "Kupa" or servis_secimi == "Külah":
        break
    else:
        print("Geçersiz seçenek. Lütfen Kupa veya Külah girin.")
        servis_secimi = input("Dondurma Külahta mı yoksa Kupada mı olsun? (Kupa/Külah): ")

top_sayisi = int(input("Kaç top dondurma istersiniz? (1-4): "))

while top_sayisi < 1 or top_sayisi > 4:
    print("Geçersiz sayı. Lütfen 1 ile 4 arasında bir sayı girin.")
    top_sayisi = int(input("Kaç top dondurma istersiniz? (1-4): "))

ekstra_secim = input("Mısır gevreği eklemek ister misiniz? (Evet/Hayır): ")

if ekstra_secim == "Evet":
    ekstra_fiyat = ekstra_fiyatlar["Mısır Gevreği"]
else:
    ekstra_fiyat = 0

ekstra_secim = input("Çikolata serpmek ister misiniz? (Evet/Hayır): ")

if ekstra_secim == "Evet":
    ekstra_fiyat += ekstra_fiyatlar["Çikolata"]

ekstra_secim = input("Çilek sosu eklemek ister misiniz? (Evet/Hayır): ")

if ekstra_secim == "Evet":
    ekstra_fiyat += ekstra_fiyatlar["Çilek Sosu"]

toplam_fiyat = dondurma_fiyatlari[top_sayisi] + servis_fiyatlari[servis_secimi] + ekstra_fiyat

print("Sipariş Özeti:")
print("Servis Türü: " + servis_secimi)
print("Top Dondurma Sayısı: " + str(top_sayisi))
print("Toplam Fiyat: " + str(toplam_fiyat) + " TL")
