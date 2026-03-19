from pathlib import Path

name = ""
names = []

while name != "n":
    name = input("Ingrese su nombre (n/para salir):")
    if name != "n":
        names.append(name)
        
path = Path("guest_book.txt")
path.write_text("\n".join(names))