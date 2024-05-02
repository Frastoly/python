import sqlite3

def metin_benzerligi(cümle1, cümle2): 
  # Cümleleri küçük harfe çevir ve kelime listelerine ayır
  kelimeler_cümle1 = set(cümle1.lower().split())
  kelimeler_cümle2 = set(cümle2.lower().split())

  # Ortak kelime sayısını hesapla
  ortak_kelime_sayisi = len(kelimeler_cümle1.intersection(kelimeler_cümle2))

  # İki cümlenin toplam kelime sayısının ortalamasını al
  ortalama_kelime_sayisi = (len(kelimeler_cümle1) + len(kelimeler_cümle2)) / 2

  # Benzerlik skorunu hesapla
  benzerlik_skoru = ortak_kelime_sayisi / ortalama_kelime_sayisi

  # Benzerlik durumunu belirle
  benzerlik_durumu = "Benzemez"
  if benzerlik_skoru > 0.5:
    benzerlik_durumu = "Benzer"

  return benzerlik_skoru, benzerlik_durumu

# Kullanıcıdan cümleleri al
cümle1 = input("İlk cümleyi girin: ")
cümle2 = input("İkinci cümleyi girin: ")

# Cümleler arasındaki benzerlik skorunu ve durumunu hesapla
benzerlik_skoru, benzerlik_durumu = metin_benzerligi(cümle1, cümle2)

# Sonucu ekrana yazdır
print("Cümleler arasındaki benzerlik skoru:", benzerlik_skoru)
print("Benzerlik durumu:", benzerlik_durumu)
