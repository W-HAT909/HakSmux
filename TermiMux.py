import os
import sys
import time
from os import system
from time import sleep
from rich.panel import Panel
from rich import print as rprint

# Kolom Layar
cols = 56
colsColors = 64

# Warna
Merah = "\033[1;31m"
Kuning = "\033[1;33m"
Hijau = "\033[1;32m"
Biru = "\033[1;34m"
Putih = "\033[1;37m"

# Teks Menengah
def cprint(text):
    print(text.center(cols))

# Teks Menengah Hijau
def cprintH(text):
    text = f"{Hijau}{text}"
    print(text.center(cols + len(Hijau)))

# Teks Menengah Biru
def cprintB(text):
    text = f"{Biru}{text}"
    print(text.center(cols + len(Biru)))

# Teks Menengah Berwarna
def ccprint(text):
    print(text.center(colsColors))

# Animasi Mengetik
def ketik(o):
    for s in o + "\n":
        sys.stdout.write(s)
        sys.stdout.flush()
        sleep(0.015)

# Efek Mengetik Menengah
def cketik(o):
    spasi = ' ' * ((cols - len(o)) // 2)
    for s in spasi + o + "\n":
        sys.stdout.write(s)
        sys.stdout.flush()
        sleep(0.020)

# Efek Kursor Menghilang
def kursor_off():
    print("\033[?25l", end="")

# Efek Kursor Terlihat
def kursor_on():
    print("\033[?25h", end="")

# Animasi Loading Ditengah
def cload():
    panjang = 30
    for i in range(101):
        isi_bar = int(panjang * i // 100)
        bar = "$" * isi_bar + "-" * (panjang - isi_bar)
        loading = f"{bar} {i}%"
        loading_center = loading.center(cols)
        print(f"\r{loading_center}", end="")
        sleep(0.015)

# Animasi Loading Verifikasi Ditengah
def cvload():
    panjang = 30
    for i in range(101):
        isi_bar = int(panjang * i // 100)
        bar = "$" * isi_bar + "-" * (panjang - isi_bar)
        loading = f"[{bar}] {i}%"
        loading_center = loading.center(cols)
        print(f"\r{loading_center}", end="")
        sleep(0.015)
    sleep(0.03)
    verif = "[Terminal Linux running √]".center(cols)
    cprint(f"\r{Hijau}{verif}")
    sleep(1)

# Animasi Loading Verifikasi Ketengah Kursor Hilang
def vload():
    kursor_off()
    try:
        cvload()
    finally:
        kursor_on()

# Tampilan Sedang Memproses Verifikasi
def sverif():
    system("clear")
    os.system("jp2a --width=56 --colors HackBlue.jpeg")
    text = "Wait For Your Verification"
    rprint(Panel(text, title="[bold yellow]VERIF[/bold yellow]", style="bold white", border_style="blue"))
    ketik(f"{Putih}                Terminal Linux Is Found")
    print(f"{Kuning}")
    vload()

# Tampilan Login
def slogin():
    system("clear")
    os.system("jp2a --width=56 --colors alone.jpeg")
    text = "Welcome To Terminal, Show First Who Are You?"
    rprint(Panel(text, title="[bold yellow]FETCH[/bold yellow]", style="bold white", border_style="blue"))

##################Login-Terminal-Linux##################

# Login
def login():
    slogin()
    ketik(f"{Kuning}                     Terminal Lost")
    print()
    while True:
          try:
              interm = input(f"{Biru}Anonim Name: {Putih}")
              if interm == "Haket":
                 sverif()
                 tampilan()
                 break
              else:
                 slogin()
                 cprintB("Sorry Terminal Not Found")
                 print()
          except KeyboardInterrupt:
              slogin()
              ccprint(Merah + "Don't try this")
              print()

# Tampilan Terminal
def tampilan():
    system("clear")
    os.system("jp2a --width=56 --height=30 --colors Anonymous.jpeg")
    tertext = "Hello, Welcome To Terminal, Keep Strong Man!"
    rprint(Panel(tertext, title="[bold blue]HAKET[/bold blue]", style="bold yellow", border_style="white"))
    cprintH("[USE YOUR SKILLS FOR UPHOLD JUSTICE]")
    print()
    print()

###############Terminal-Root-Linux-Screen###############

# Eksekusi
login()
