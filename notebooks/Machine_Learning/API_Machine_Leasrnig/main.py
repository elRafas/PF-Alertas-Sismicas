from fastapi import FastAPI
import uvicorn

uvicorn.run(app, host="0.0.0.0", port=8000)
app = FastAPI()

@app.get("/peliculas_mes/{mes}")
def peliculas_mes(mes: str):
    
    
    return {'mes':mes  }
    
