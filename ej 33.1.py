from pathlib import Path

nombre = input("Ingrese su nombre: ")

path = Path("guest.txt")

path.write_text(nombre)