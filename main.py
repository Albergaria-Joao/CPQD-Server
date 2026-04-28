from datetime import datetime
from typing import Literal, List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(title="Backend Portaria - Protótipo")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LeituraEntrada(BaseModel):
    placa: str = Field(..., examples=["ABC1D23"])
    empresa: str = Field(..., examples=["CPQD"])
    status: Literal["liberado", "nao_liberado"]


class LeituraSaida(BaseModel):
    placa: str
    empresa: str
    status: Literal["liberado", "nao_liberado"]
    horario: str


leitura_atual: LeituraSaida | None = None
historico: List[LeituraSaida] = []
websockets_ativos: List[WebSocket] = []


@app.get("/")
def home():
    return {"mensagem": "Backend rodando"}


@app.post("/api/leitura", response_model=LeituraSaida)
async def receber_leitura(dados: LeituraEntrada):
    global leitura_atual

    nova_leitura = LeituraSaida(
        placa=dados.placa.upper().strip(),
        empresa=dados.empresa.strip(),
        status=dados.status,
        horario=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    )

    leitura_atual = nova_leitura

    historico.insert(0, nova_leitura)

    if len(historico) > 10:
        historico.pop()

    await enviar_para_frontend(nova_leitura)

    return nova_leitura


@app.get("/api/leitura-atual", response_model=LeituraSaida | None)
def obter_leitura_atual():
    return leitura_atual


@app.get("/api/historico", response_model=List[LeituraSaida])
def obter_historico():
    return historico


@app.websocket("/ws/leitura")
async def websocket_leitura(websocket: WebSocket):
    await websocket.accept()
    websockets_ativos.append(websocket)

    try:
        if leitura_atual:
            await websocket.send_json(leitura_atual.model_dump())

        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        if websocket in websockets_ativos:
            websockets_ativos.remove(websocket)


async def enviar_para_frontend(leitura: LeituraSaida):
    desconectados = []

    for websocket in websockets_ativos:
        try:
            await websocket.send_json(leitura.model_dump())
        except Exception:
            desconectados.append(websocket)

    for websocket in desconectados:
        if websocket in websockets_ativos:
            websockets_ativos.remove(websocket)