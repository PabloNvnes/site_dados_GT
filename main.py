from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Libera CORS para testes locais
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensagem": "API ativa!"}

@app.post("/avaliar")
def avaliar(codigo: str = Form(...)):
    try:
        # Código de teste simples
        exec_globals = {}
        exec(codigo, exec_globals)
        if 'soma' in exec_globals and exec_globals['soma'](2, 3) == 5:
            return {"resultado": "passou"}
        else:
            return {"resultado": "falhou"}
    except Exception as e:
        return {"erro": str(e)}
