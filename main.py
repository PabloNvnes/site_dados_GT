# Arquivo: main.py
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# A linha abaixo é CRUCIAL para permitir que seu site (frontend) 
# consiga fazer requisições para sua API (backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (para simplificar)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc)
    allow_headers=["*"],
)

# Endpoint que ENVIA a pergunta para o frontend
@app.get("/pergunta")
def fazer_pergunta():
    return {
        "id_pergunta": "desafio_soma_simples",
        "enunciado": "Quanto é 2 + 2?"
    }

# Endpoint que RECEBE a resposta do frontend e a corrige
@app.post("/responder")
def receber_resposta(id_pergunta: str = Form(...), resposta_usuario: str = Form(...)):
    gabarito = {
        "desafio_soma_simples": "4"
    }

    if id_pergunta in gabarito:
        if resposta_usuario.strip() == gabarito[id_pergunta]:
            return {"correto": True, "feedback": "Parabéns, resposta correta!"}
        else:
            return {"correto": False, "feedback": "Resposta errada. Tente novamente."}
    
    return {"correto": False, "feedback": "Erro: Desafio não encontrado."}