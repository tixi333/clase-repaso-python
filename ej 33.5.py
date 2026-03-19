from pathlib import Path


try:
    path_c = Path("gatos.txt")
    path_d = Path("perros.txt")
    contents_c = path_c.read_text()
    contents_d = path_d.read_text()
    print("Nombres de gatos:")
    print(contents_c)
    print("Nombres de perros:")
    print(contents_d)

except FileNotFoundError:
    print("No se encontraron los archivos.")

