from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import uvicorn

app = FastAPI()

DATABASE_URL = "mysql+pymysql://cco_cpqd:123456@localhost:3306/cpqd_servidor_teste"
engine = create_engine(DATABASE_URL)

class UpdateData(BaseModel):
    id_registro: int
    coluna: str
    novo_valor: str

@app.post("/update-sheet")
async def update_from_sheet(data: UpdateData):
    print(f"Recebido: {data}")
    

    colunas_permitidas = ["id", "placa", "modelo", "cor", "empresa"] # Evita SQL injection
    if data.coluna not in colunas_permitidas:
        raise HTTPException(status_code=400, detail="Coluna inválida")

    try:
        with engine.connect() as conn:
            print("Conexao feita")
            
            if data.coluna == "id":
                query = text(f"INSERT INTO liberacao (id) VALUES (:id)")
                params = {"id": data.id_registro}
            else:
                query = text(f"UPDATE liberacao SET {data.coluna} = :valor WHERE id = :id")
                params = {"valor": data.novo_valor, "id": data.id_registro}
            
            result = conn.execute(query, params)
            conn.commit()
            print(f"Sucesso - linhas afetadas: {result.rowcount}")
            
            return {"status": "success", "rows": result.rowcount}
            
    except Exception as e:
        print(f"ERRO DE CONEXÃO: {e}")
        raise HTTPException(status_code=500, detail=f"Erro no banco: {str(e)}")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
