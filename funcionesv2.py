print("**** FUNCIONES VERSION 2 **** ")
print("miguel dominguez")
celulares=["iphone 13","samsung a23", "chafa"]
albumes=("lyke mike","x 100pre","ESTRELLA")
animales = {
  "pantera negra": "oso malayo",
  "serpiente": "mariposa",
  "perro": 5
}
tipodeportes = {"Futbol", "Box", "Padel"}
# zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)

def vertuplas(album):
    for cancion in album:
        print(cancion)

def verdiccionarios(mas):
    for animal in mas:
        print(animal)

def versets(tipo):
    for deportes in tipo:
        print(deportes)

# llama a funciones
print("\n ****imprime celulares****")
verlista(celulares)

print("\n ****imprime albumes****")
vertuplas(albumes)

print("\n ****imprime animales****")
verdiccionarios(animales)

print("\n ****imprime deportes****")
versets(tipodeportes)