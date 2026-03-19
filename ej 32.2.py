from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()
print(contents)

contents = path.read_text().splitlines()
for e in contents:
    print(e)