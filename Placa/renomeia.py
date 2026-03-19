from pathlib import Path

# pasta raiz do dataset
BASE_DIR = Path(r"C:\Users\vcapu\OneDrive\Área de Trabalho\Placa")  # TROQUE AQUI
PREFIXO = "placa"

# extensões aceitas para imagem
EXTENSOES_IMG = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

splits = ["train", "valid", "test"]
contador = 1

for split in splits:
    images_dir = BASE_DIR / split / "images"
    labels_dir = BASE_DIR / split / "labels"

    if not images_dir.exists() or not labels_dir.exists():
        print(f"[IGNORADO] {split} não existe completo.")
        continue

    imagens = sorted([p for p in images_dir.iterdir() if p.suffix.lower() in EXTENSOES_IMG])

    print(f"\n--- {split.upper()} ---")
    for img_path in imagens:
        label_path = labels_dir / f"{img_path.stem}.txt"

        if not label_path.exists():
            print(f"[SEM LABEL] {img_path.name}")
            continue

        novo_nome = f"{PREFIXO}_{contador:06d}"
        nova_img = images_dir / f"{novo_nome}{img_path.suffix.lower()}"
        novo_label = labels_dir / f"{novo_nome}.txt"

        # renomeia
        img_path.rename(nova_img)
        label_path.rename(novo_label)

        print(f"{img_path.name} -> {nova_img.name}")
        contador += 1

print("\nRenomeação concluída.")