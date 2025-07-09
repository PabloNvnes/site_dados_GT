from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensagem": "API ativa!"}

@app.get("/pergunta")
def fazer_pergunta():
    return {
        "pergunta": "Quanto é 2 + 2?",
        "id": "pergunta1"  # ID da pergunta (para expandir no futuro)
    }

@app.post("/responder")
def responder_pergunta(resposta: str = Form(...), id: str = Form(...)):
    if id == "pergunta1":
        if resposta.strip() in ["4", "quatro", "Quatro"]:
            return {"correto": True, "mensagem": "Resposta correta!"}
        else:
            return {"correto": False, "mensagem": "Resposta errada. Tente novamente."}
    return {"erro": "Pergunta não reconhecida"}
