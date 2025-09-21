from PIL import Image
import os

# --- Constantes de Configuração ---
REDUCTION_FACTOR = 0.5
SOURCE_PATH = 'fotos'
COMPRESSED_PATH = "compressed_images"
ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png')

# Garante que o diretório de destino exista de forma segura.
os.makedirs(COMPRESSED_PATH, exist_ok=True)

# Filtra os arquivos de imagem de forma mais robusta (case-insensitive e múltiplas extensões).
files = [f for f in os.listdir(SOURCE_PATH) if f.lower().endswith(ALLOWED_EXTENSIONS)]

size_before = 0
size_after = 0

for file in files:
    file_path = os.path.join(SOURCE_PATH, file)
    new_path = os.path.join(COMPRESSED_PATH, file)

    size_before += os.stat(file_path).st_size
    img = Image.open(file_path)

    new_w = int(REDUCTION_FACTOR * img.size[0])
    new_h = int(REDUCTION_FACTOR * img.size[1])

    # Image.ANTIALIAS está obsoleto. Use Image.Resampling.LANCZOS para alta qualidade.
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # O parâmetro 'optimize' é um booleano, não o módulo importado.
    img.save(new_path, 'JPEG', optimize=True, quality=90)
    file_stats = os.stat(new_path)
    size_after += file_stats.st_size

print("Compressão concluída!")
print(f"Tamanho original: {size_before / 1_000_000:.2f} MB")
print(f"Tamanho comprimido: {size_after / 1_000_000:.2f} MB")