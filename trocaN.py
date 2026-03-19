from pathlib import Path

# caminho da pasta raiz do dataset
BASE_DIR = Path(r"C:\Users\jvalb\Downloads\YOLO-CEAF\YOLO-CEAF\Placa")  # TROQUE AQUI

splits = ["train", "valid", "test"]
arquivos_alterados = 0
linhas_alteradas = 0

for split in splits:
    labels_dir = BASE_DIR / split / "labels"

    if not labels_dir.exists():
        print(f"[IGNORADO] pasta não encontrada: {labels_dir}")
        continue

    txt_files = list(labels_dir.glob("*.txt"))
    print(f"\n--- {split.upper()} ---")

    for txt_file in txt_files:
        with open(txt_file, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        novas_linhas = []
        alterou_arquivo = False

        for linha in linhas:
            partes = linha.strip().split()

            if len(partes) >= 5 and partes[0] == "0":
                partes[0] = "1"
                linha = " ".join(partes) + "\n"
                linhas_alteradas += 1
                alterou_arquivo = True
            else:
                linha = linha if linha.endswith("\n") else linha + "\n"

            novas_linhas.append(linha)

        if alterou_arquivo:
            with open(txt_file, "w", encoding="utf-8") as f:
                f.writelines(novas_linhas)

            arquivos_alterados += 1
            print(f"[ALTERADO] {txt_file.name}")

print("\nConcluído.")
print(f"Arquivos alterados: {arquivos_alterados}")
print(f"Linhas alteradas: {linhas_alteradas}")