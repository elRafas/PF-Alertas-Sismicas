from fastapi import FastAPI

app = FastAPI()

@app.get("/peliculas_mes/{mes}")
def peliculas_mes(mes: str):
    return {'mes': mes}
    
