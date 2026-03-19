from pathlib import Path
import json

def locate_path():
    path = Path("user_info.json")
    if path.exists():
        load_data(path)
    else:
        store_data(path)

def get_name():
    name = input("Ingrese su nombre: ")
    return name

def get_favorite_number():
    favorite_number = input("¿Cuál es tu número favorito? ")
    return favorite_number

def get_age():
    age = input("¿Cuál es tu edad? ")
    return age

def store_data(path):
    datos = {
        "Nombre": get_name(),
        "Número favorito": get_favorite_number(),
        "Age:": get_age()
    }
    path.write_text(json.dumps(datos))

def load_data(path):
    contents = path.read_text()
    datos = json.loads(contents)
    saludar_usuario(datos)

def saludar_usuario(datos):
    print(f"Bienvenido, ¿eres {datos['Nombre']}?")
    op = input("Si/no: ")
    if op.lower() == "si":
        show_data(datos)
    else:
        store_data(Path("user_info.json"))

def show_data(datos):
    print(f"Tu número favorito es {datos['Número favorito']} y tu edad es {datos['Age:']}.")


locate_path()