import argparse
import wget
import os
import colorama

p = argparse.ArgumentParser()

a = open("list.txt", "r")
b = a.read()

lop = b.split("\n")

p.add_argument("-i", "--install", help="install a package")

prsd = p.parse_args()

def get(url, file, text):
    print(colorama.Fore.CYAN + text)
    wget.download(url)
    os.system(f"{file}")
    os.remove(f"{file}")
    colorama.init()

if prsd.install in lop:
    text = "downloading"
    if prsd.install == lop[0]:
        text = text + " vlc"
        url = "https://get.videolan.org/vlc/3.0.21/win32/vlc-3.0.21-win32.exe"
        file = "vlc-3.0.21-win32.exe"
        get(url, file, text)
    if prsd.install == lop[1]:
        text = text + " sharex"
        url = "https://github.com/ShareX/ShareX/releases/download/v16.1.0/ShareX-16.1.0-setup.exe"
        file = "ShareX-16.1.0-setup.exe"
        get(url, file, text)
    if prsd.install == lop[2]:
        text = text + " obs"
        url = "https://cdn-fastly.obsproject.com/downloads/OBS-Studio-31.0.0-Windows-Installer.exe"
        file = "OBS-Studio-31.0.0-Windows-Installer.exe"
        get(url, file, text)
    if prsd.install == lop[3]:
        text = text + " rufus"
        url = "https://github.com/pbatard/rufus/releases/download/v4.6/rufus-4.6.exe"
        file = "rufus-4.6.exe"
        get(url, file, text)
    if prsd.install == lop[4]:
        text = text + " kdec"
        url = "https://download.kde.org/stable/release-service/24.02.0/windows/kdeconnect-kde-release_24.02-3692-windows-cl-msvc2022-x86_64.exe"
        file = "kdeconnect-kde-release_24.02-3692-windows-cl-msvc2022-x86_64.exe"
        get(url, file, text)