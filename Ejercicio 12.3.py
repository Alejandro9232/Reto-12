import json

#Esta es la carpeta donde se guardo el archivo json
ruta = "/storage/emulated/0/Documents/personas.json"

#Aca es donde se abre y se carga el archivo json
with open(ruta, "r", encoding="utf-8") as archivo:
    personas = json.load(archivo)

#Buscar por deporte
deporte = input("Ingresa el deporte que deseas buscar: ")

print(f"Personas que practican {deporte}:")
for persona in personas.values():
    if deporte in persona["deportes"]:
        print(f"{persona['nombres']} {persona['apellidos']}")

#Busca por rango de edad
edad_min = int(input("Edad minima: "))
edad_max = int(input("Edad maxima: "))

print(f"Personas entre {edad_min} y {edad_max} años:")
for persona in personas.values():
    if edad_min <= persona["edad"] <= edad_max:
        print(f"{persona['nombres']} {persona['apellidos']}")