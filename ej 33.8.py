from pathlib import Path
import json

def locate_path():
    path = Path("favorite_number.json")
    if path.exists():
        load_favorite_number(path)
    else:
        store_favorite_number(path)

def load_favorite_number(path):
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"Tu número favorito es {favorite_number}.")

def store_favorite_number(path):
    favorite_number = input("¿Cuál es tu número favorito? ")
    path.write_text(json.dumps(favorite_number))

locate_path()
    