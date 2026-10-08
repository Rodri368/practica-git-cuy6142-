import requests

nombre = input("Ingrese el nombre del Pokémon: ").strip().lower()
if not nombre:
    raise SystemExit("Debe ingresar un nombre")

url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
respuesta = requests.get(url, timeout=10)
print(f"Código HTTP: {respuesta.status_code}")

if respuesta.status_code == 404:
    raise SystemExit(f"No existe el Pokémon '{nombre}'")
respuesta.raise_for_status()

datos = respuesta.json()
print(f"Nombre: {datos['name'].title()}")
print(f"Peso: {datos['weight']} hectogramos")
print("Tipos:")
for tipo in datos["types"]:
    print(f" - {tipo['type']['name']}")
print("Habilidades:")
for habilidad in datos["abilities"]:
    print(f" - {habilidad['ability']['name']}")
