import cv2

# Troque a string aqui com as tentativas acima

# INTELBRAS
# rtsp://[USUARIO]:[SENHA]@[IP_DO_NVR]:554/cam/realmonitor?channel=[CANAL]&subtype=0

# HIKVISION
# rtsp://[USUARIO]:[SENHA]@[IP_DO_NVR]:554/Streaming/Channels/101 
#   (onde 101 significa Canal 1, Stream Principal).

url = "rtsp://admin:1234567890@192.168.0.3:554/live/ch00_0"

print(f"Tentando conectar: {url}")
cap = cv2.VideoCapture(url)

if cap.isOpened():
    print("[SUCESSO] Autenticado! Lendo frames...")
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Teste NVR', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
else:
    print("[FALHA] 401 Unauthorized ou erro de conexão.")

cap.release()
cv2.destroyAllWindows()