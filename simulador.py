import random
from datetime import datetime, timedelta
from config import config

def simular_datos_vacas(inicio: datetime, vacas: int = 25, intervalos: int = 18):
    datos = []
    for cow in range(1, vacas + 1):
        lat = round(41.3800 + cow * 0.00005, 6)
        lon = round(1.2000 + cow * 0.00006, 6)
        for i in range(intervalos):
            time = inicio + timedelta(minutes=i * config["intervalo_minutos"])
            temp = round(random.uniform(config["valor_min"], config["valor_max"]), 1)
            freq = random.randint(config["frecuencia_min"], config["frecuencia_max"])
            datos.append({
                "cow_id": f"{cow:03}",
                "timestamp": time.strftime(config["formato_fecha"]),
                "lat": lat,
                "lon": lon,
                "temperature": temp,
                "frequency": freq,
                "sent": 1
            })
    return datos
