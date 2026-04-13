import cv2
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import os
import sys

app = FastAPI(title="CCO Video Streamer")

# Em produção, a URL deve vir do ambiente (ex: arquivo .env)
# Para o teste, vamos permitir o input manual se estiver vazio.
RTSP_URL = os.getenv("URL_NVR", "")

def capturar_frames():
    """Conecta ao NVR e gera os frames em formato JPEG (MJPEG)"""
    cap = cv2.VideoCapture(RTSP_URL)
    
    if not cap.isOpened():
        print(f"[ERRO] Falha ao conectar na URL: {RTSP_URL}")
        # Retorna uma imagem preta ou encerra em caso de falha severa
        return

    print("[INFO] Conexão com NVR estabelecida. Transmitindo frames...")
    while True:
        sucesso, frame = cap.read()
        if not sucesso:
            print("[AVISO] Perda de frame ou desconexão da câmera.")
            break
            
        # --- FUTURO: É aqui que você fará a chamada para o YOLO e o OCR ---
        # frame = aplicar_inferencia_yolo(frame)
        
        # Codifica o frame do OpenCV para JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        # Yield no formato multipart para o streaming contínuo no navegador
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.get("/video-feed")
def video_feed():
    """Rota que será consumida pelo sistema Web da Portaria"""
    return StreamingResponse(capturar_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    print("=== Inicializando Módulo CCO ===")
    
    # Lógica de fallback para o seu teste inicial
    if not RTSP_URL:
        RTSP_URL = input("Digite a string de conexão RTSP do NVR: ").strip()
        if not RTSP_URL:
            print("[ERRO] URL não fornecida. Encerrando.")
            sys.exit(1)

    print("\n[INFO] Servidor iniciando...")
    print("[INFO] Rota da Portaria: http://localhost:8000/video-feed")
    print("[INFO] Para encerrar, pressione CTRL+C")
    
    # O uvicorn.run programático é obrigatório para o PyInstaller funcionar depois
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")
