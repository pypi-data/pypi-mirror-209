import os
import pyany
import subprocess

def restart():
    comment = "Pyany user restart\nPyany - Перезагрузка юзером\nОсталось 5 сек. до перезагрузки..."
    os.system(f"shutdown /r /t 5 /c \"{comment}\"")

def installall():
    print("Installing all necessary Python libraries for work...")
    subprocess.check_call(["pip", "install", "pyrogram", "tgcrypto", "sys", "os"])
    print("Successfully installed all the libraries that are necessary for work.")

def allinstall():
    installall()

def draw_pen():
    pen = [
        "             ⬛️⬛️🟥🟥⬛️⬛️",
        "             ⬛️🟥🟥🟥🟥⬛️",
        "             ⬛️🟥🟥🟥🟥⬛️",
        "             ⬛️🟫🟫🟫🟫⬛️",
        "             ⬛️🟫🟫🟫🟫⬛️",
        "             ⬛️🟫🟫🟫🟫⬛️",
        "             ⬛️🟫🟫🟫🟫⬛️",
        "             ⬛️🟫🟫🟫🟫⬛️",
        "🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫",
        "🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫"
    ]
    for line in pen:
        print(line)



