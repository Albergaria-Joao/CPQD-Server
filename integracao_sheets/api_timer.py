from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import uvicorn
from typing import List

app = FastAPI()

DATABASE_URL = "mysql+pymysql://cco_cpqd:123456@localhost:3306/cpqd_servidor_teste"
engine = create_engine(DATABASE_URL)

class RowData(BaseModel):
    placa: str
    modelo: str
    cor: str
    empresa: str


@app.post("/sync-sheet")
async def update_from_sheet(data: List[RowData]):
    print(f"Recebido: {data}")

    select_query = text("SELECT placa FROM liberacao")
    delete_query = text("DELETE FROM liberacao WHERE placa IN :lista")

    
    upsert_query = text("""
        INSERT INTO liberacao (placa, modelo, cor, empresa) 
        VALUES (:placa, :modelo, :cor, :empresa)
        ON DUPLICATE KEY UPDATE 
            modelo = VALUES(modelo), 
            cor = VALUES(cor), 
            empresa = VALUES(empresa)
    """)    

    try:
        with engine.connect() as conn:
            print("Conexao feita")
            params = [row.dict() for row in data]
            
            placas_sheets = [row['placa'] for row in params]

            placas_db = conn.execute(select_query).fetchall()
            placas_db = [row[0] for row in placas_db]

            placas_delete = list(set(placas_db) - set(placas_sheets))

            if placas_delete:
                conn.execute(delete_query, {"lista": tuple(placas_delete)}) # SQL espera (x, y, z), que é justamente o formato da tupla
 
            conn.execute(upsert_query, params) 
            conn.commit()
            print(f"Sucesso - linhas afetadas: {len(params)}")

            
            return {"status": "success", "rows": f"{len(data)} veículos processados."}
            
    except Exception as e:
        print(f"ERRO DE CONEXÃO: {e}")
        raise HTTPException(status_code=500, detail=f"Erro no banco: {str(e)}")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
