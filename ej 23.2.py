def hacer_album(artista, titulo, cant_canciones=None):
    album = {"nombre": artista, "titulo": titulo}
    if cant_canciones:
        album["canciones"] = cant_canciones
        
    return album
a = ""
while a != "n":
    titulo = input("titulo del album: ")
    artista = input("artista: ")
    album = hacer_album(titulo,artista)
    print(album)
    a = input("¿desea continuar? (n/para salir)")

