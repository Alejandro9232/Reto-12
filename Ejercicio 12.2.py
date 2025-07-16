# Diccionarios de paises con sus capitales
paises1 = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago de chile",
    "Colombia": "Bogota",
    "Peru": "Lima",
    "Mexico": "Ciudad de Mexico",
    "España": "Madrid",
    "Alemania": "Berlin",
    "Italia": "Roma",
    "Portugal": "Lisboa",
    "India": "Nueva Delhi",
    "Japon": "Tokio",
    "China": "Pekin",
    "Canada": "Ottawa",
    "Australia": "Canberra"
}

paises2 = {
    "Argentina": "La Plata",      
    "Brasil": "Rio de Janeiro", 
    "Corea del Sur": "Seul",
    "Rusia": "Moscu",
    "Egipto": "El Cairo",
    "Nigeria": "Abuya",
    "Francia": "Paris",
    "Reino Unido": "Londres",
    "Turquia": "Ankara",
    "Sudafrica": "Pretoria"
}

# Función que sirve para combinar los dos diccionarios
def combinar_diccionarios(dic1, dic2):
    resultado = dic2.copy() 
    resultado.update(dic1)     
    return resultado

diccionario_mezclado = combinar_diccionarios(paises1, paises2)

# Se imprimen los diccionarios mezclados ordenados alfabeticamente
print("Diccionario combinado (preferencia al primero):\n")
for pais in sorted(diccionario_mezclado):
    print(f"{pais} → {diccionario_mezclado[pais]}")