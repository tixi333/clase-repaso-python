persona1 = {
    "nombre":"naty",
    "apellido":"baikauskas",
    "edad":"16",
    "ciudad":""
}

persona2 = {
    "nombre":"zoe",
    "apellido":"ayuso",
    "edad":"16",
    "ciudad":""
}

persona4 = {
    "nombre":"x",
    "apellido":"y",
    "edad":"64",
    "ciudad":"z"
}

gente = [persona1,persona2,persona4]

for p in gente:
    for e in p:
        print(f"{e}: {p[e]}")
