#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KRİTİK ÇAY MOLASI HESAPLAYICI
Bu program, herhangi bir görevin bilimsel olarak kaç çay molası gerektirdiğini hesaplar.
Çay içilmezse evrenin dengesi bozulur. Ciddi bir iştir.
"""

import time
import random
import sys

def hesapla_molalar(zorluk: int) -> int:
    """Zorluk seviyesine göre çay molası sayısını hesaplar."""
    if zorluk < 1:
        zorluk = 1
    # Abartılı formül: zorluk * rastgele * pi yaklaşımı + şans faktörü
    baz = zorluk * random.randint(2, 7)
    ek = int(3.14159 * random.random() * 2)
    return max(1, baz + ek)

def demle_cay(molasi_no: int):
    """Çay demleme simülasyonu. Gerçekçi süreler abartılmıştır."""
    print(f"\n☕ ÇAY MOLASI #{molasi_no} BAŞLADI ☕")
    sebepler = [
        "Çünkü kod yazarken beynin çay ister.",
        "Çünkü trafik sıkışık gibi düşünceler sıkışmış.",
        "Çünkü bürokrasi çay olmadan ilerlemez.",
        "Çünkü hayat zaten yeterince ciddi, çay şaka yapar.",
        "Çünkü bu molası atlamak evrensel bir suçtur."
    ]
    print(random.choice(sebepler))
    for saniye in range(3, 0, -1):
        print(f"  Demleniyor... {saniye} (gerçekte anlık)")
        time.sleep(0.3)  # Abartılı yavaş ama çok da değil
    print("  Çay hazır! İçildi varsayılıyor. Güç +1.")

def main():
    print("=" * 50)
    print("   KRİTİK ÇAY MOLASI HESAPLAYICI v1.0")
    print("   'Görev çay kadar önemlidir.' - Bilinmeyen Kayyum")
    print("=" * 50)
    
    try:
        zorluk = int(input("Görev zorluk seviyesi (1-10): "))
    except:
        zorluk = 5
        print("Geçersiz giriş. Varsayılan 5 alındı. Çay içilmedi henüz.")
    
    molalar = hesapla_molalar(zorluk)
    print(f"\n📊 Bilimsel hesap sonucu: Bu görev için TAM {molalar} çay molası ŞARTTIR!")
    print("Aksi takdirde program kendini kapatabilir (veya kapanmayabilir).\n")
    
    for i in range(1, molalar + 1):
        demle_cay(i)
        if i < molalar:
            print("  Bir sonraki molasıya geçiliyor...")
            time.sleep(0.5)
    
    print("\n" + "=" * 50)
    print("🎉 GÖREV TAMAMLANDI! Çay molaları sayesinde hayatta kaldınız.")
    print("Not: Bu program çay içmeden çalışmaz. (Aslında çalışır ama ruhu olmaz.)")
    # Gizli damga: ZW4gaXlpIGNvenVtIGhlciB6YW1hbiBjYXkgbW9sYXNpZGlyIHNpeWFzZXQgZGVnaWw=
    # Çözülürse anlarsın. Ama çay içmeden çözme.

if __name__ == "__main__":
    main()
