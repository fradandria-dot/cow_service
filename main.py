from fastapi import FastAPI, Query, Body, Header, HTTPException
from datetime import datetime
from simulador import simular_datos_vacas
from config import config

app = FastAPI()
API_TOKEN = "secreto123"

def verificar_token(token: str):
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Token inválido")

@app.get("/simular_vacas")
def generar_vacas(
    fecha_inicio: str = Query("2025-07-30T08:00:00"),
    vacas: int = Query(25),
    intervalos: int = Query(18),
    guardar: bool = Query(False),
    token: str = Header(...)
):
    verificar_token(token)
    inicio = datetime.fromisoformat(fecha_inicio)
    datos = simular_datos_vacas(inicio, vacas, intervalos)

    if guardar:
        with open("cow_samples.txt", "w", encoding="utf-8") as f:
            f.write("cow_id\ttimestamp\tlat\tlon\ttemperature\tfrequency\tsent\n")
            for d in datos:
                f.write(f"{d['cow_id']}\t{d['timestamp']}\t{d['lat']}\t{d['lon']}\t{d['temperature']}\t{d['frequency']}\t{d['sent']}\n")

    return {"datos_simulados": datos}

@app.post("/configuracion")
def actualizar_configuracion(nueva_config: dict = Body(...), token: str = Header(...)):
    verificar_token(token)
    config.update(nueva_config)
    return {"config_actualizada": config}

@app.get("/configuracion")
def obtener_configuracion(token: str = Header(...)):
    verificar_token(token)
    return {"config_actual": config}
