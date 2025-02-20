import shutil
import os
import PIL.Image
from colorama import init, Fore, Style, Back

seleccion = 0
path = input("Introduzca la ruta del archivo: ")

while True:
    print("\n")
    print(f"[{Style.BRIGHT}{Fore.GREEN}1{Fore.RESET}]: {Fore.CYAN}PNG a JPG{Fore.RESET}\n")
    print(f"[{Fore.GREEN}2{Fore.RESET}]: {Fore.CYAN}JPG a PNG{Fore.RESET}\n")
    print(f"[{Fore.GREEN}3{Fore.RESET}]: {Fore.CYAN}JPEG a JPG{Fore.RESET}\n")
    print(f"[{Fore.GREEN}4{Fore.RESET}]: {Fore.CYAN}JPG a JPEG{Fore.RESET}\n")
    print(f"[{Fore.GREEN}5{Fore.RESET}]: {Fore.RED}Salir{Style.RESET_ALL}")
    print("\n")

    seleccion = int(input("Convertir a? "))

    if seleccion == 1:
        image = PIL.Image.open(path)
        rgb_image = image.convert('RGB')
        pathC = path.replace('.png', '.jpg')
        rgb_image.save(pathC, quality=100)
        os.remove(path)
        print("Success")
        print("\n")
    elif seleccion == 2:
        image = PIL.Image.open(path)
        rgb_image = image.convert('RGB')
        pathC = path.replace('.jpg', '.png')
        rgb_image.save(pathC, quality=100)
        os.remove(path)
        print("Success")
        print("\n")
    elif seleccion == 3:
        image = PIL.Image.open(path)
        rgb_image = image.convert('RGB')
        pathC = path.replace('.jpeg', '.jpg')
        rgb_image.save(pathC, quality=100)
        os.remove(path)
        print("Success")
        print("\n")
    elif seleccion == 4:
        image = PIL.Image.open(path)
        rgb_image = image.convert('RGB')
        pathC = path.replace('.jpg', '.jpeg')
        rgb_image.save(pathC, quality=100)
        os.remove(path)
        print("Success")
        print("\n")
    elif seleccion == 5:
        break