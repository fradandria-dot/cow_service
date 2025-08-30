import requests

# Configuración del cliente
URL = "http://localhost:8000/simular_vacas"
TOKEN = "secreto123"

# Parámetros de la petición
params = {
    "fecha_inicio": "2025-07-30T08:00:00",
    "vacas": 1,
    "intervalos": 1,
    "guardar": False
}

# Headers con el token
headers = {
    "token": TOKEN
}

# Realizar la petición
try:
    response = requests.get(URL, params=params, headers=headers)
    response.raise_for_status()
    datos = response.json()

    print("✅ Datos simulados recibidos:")
    for d in datos["datos_simulados"]:
        print(f"{d['cow_id']} | {d['timestamp']} | {d['lat']} | {d['lon']} | {d['temperature']}°C | {d['frequency']}Hz")

except requests.exceptions.RequestException as e:
    print("❌ Error al conectar con el servicio:", e)
