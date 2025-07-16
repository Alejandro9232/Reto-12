#importa request para conectarse a interner, json para los diccionarios y random para generar ids aleatorios
import requests
import json
import random

def consultar_api(nombre, url):
    print(f"Conectando a la API: {nombre}")
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            for clave, valor in data.items():
                print(f"{clave} : {valor}")
        else:
            print(f"Error al conectar con {nombre} - Código: {respuesta.status_code}")
    except Exception as e:
        print(f"Error: {e}")
        
def consultar_api_pokemon(nombre, url):
    print(f"Conectando a la API: {nombre}")
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()

            # Muestra los datos  del pokemon
            print("Nombre:", data["name"].capitalize())
            print("ID:", data["id"])
            print("Altura:", data["height"])
            print("Peso:", data["weight"])

            tipos = [tipo["type"]["name"] for tipo in data["types"]]
            print("Tipo(s):", ", ".join(tipos))

        else:
            print(f"Error al conectar con {nombre} - Código: {respuesta.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# URLs de las APIs
api1 = ("API del gato", "https://catfact.ninja/fact")
api2 = ("API del chiste", "https://official-joke-api.appspot.com/random_joke")
random_id = random.randint(1, 1010)
api3 = ("API de Pokemon", f"https://pokeapi.co/api/v2/pokemon/{random_id}/")

# Consulta las APIs
consultar_api(*api1)
consultar_api(*api2)
consultar_api_pokemon(*api3)