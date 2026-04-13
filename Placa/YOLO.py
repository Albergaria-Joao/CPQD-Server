from ultralytics import YOLO


def main():
    # modelo pequeno e leve para começar
    model = YOLO("yolo26n.pt")

    # treino
    model.train(
        data=r"C:\Users\jvalb\Documents\GitHub\CPQD-YOLO\Placa\data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        project="runs_placa",
        name="placas_v1"
    )

    # validação no conjunto de validação
    model = YOLO(r"runs_placa\placas_v1\weights\best.pt")
    model.val()

    # validação no conjunto de teste
    model.val(data=r"C:\Users\jvalb\Documents\GitHub\CPQD-YOLO\Placa\data.yaml", split="test")

    # predição salvando imagens de saída
    model.predict(
        source=r"C:\Users\jvalb\Documents\GitHub\CPQD-YOLO\Placa\test\images",
        conf=0.25,
        save=True
    )


if __name__ == "__main__":
    main()