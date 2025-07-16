# Diccionario con sus paises y sus capitales
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogota",
    "Peru": "Lima",
    "Ecuador": "Quito",
    "Venezuela": "Caracas",
    "Uruguay": "Montevideo",
    "Paraguay": "Asuncion",
    "Bolivia": "La Paz",
    "Mexico": "Ciudad de Mexico",
    "Estados Unidos": "Washington D.C.",
    "Canada": "Ottawa",
    "España": "Madrid",
    "Francia": "Paris",
    "Alemania": "Berlin",
    "Italia": "Roma",
    "Reino Unido": "Londres",
    "Portugal": "Lisboa",
    "Rusia": "Moscu",
    "China": "Pekin",
    "Japon": "Tokio",
    "Corea del Sur": "Seul",
    "India": "Nueva Delhi",
    "Australia": "Canberra",
    "Egipto": "El Cairo",
    "Sudafrica": "Pretoria",
    "Nigeria": "Abuya",
    "Turquia": "Ankara",
    "Irlanda": "Dublin"
}

# Imprime los paises en orden alfabetico
print("Paises ordenados alfabeticamente: ")
for pais in sorted(paises):
    print(f"{pais} → {paises[pais]}")