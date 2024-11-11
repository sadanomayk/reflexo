import os
from tkinter import filedialog, Tk
from PIL import Image
import pillow_heif

# Função para selecionar arquivos HEIC
def select_files():
    root = Tk()
    root.withdraw()  # Não mostra a janela principal do Tkinter
    # Permite selecionar vários arquivos
    files = filedialog.askopenfilenames(title="Selecione as imagens HEIC", filetypes=[("HEIC files", "*.heic")])
    return files

# Função para converter HEIC para JPG
def convert_heic_to_jpg(files, output_folder):
    for file in files:
        try:
            # Abrir o arquivo HEIC
            img = Image.open(file)
            # Criar o nome do arquivo de saída
            output_file = os.path.join(output_folder, os.path.basename(file).replace('.heic', '.jpg'))
            # Salvar a imagem como JPG
            img.save(output_file, 'JPEG')
            print(f"Imagem convertida: {output_file}")
        except Exception as e:
            print(f"Erro ao converter {file}: {e}")

# Função principal
def main():
    # Selecionar os arquivos HEIC
    heic_files = select_files()

    if not heic_files:
        print("Nenhum arquivo selecionado.")
        return

    # Selecionar a pasta de saída
    output_folder = filedialog.askdirectory(title="Selecione a pasta para salvar os JPGs")

    if not output_folder:
        print("Nenhuma pasta de saída selecionada.")
        return

    # Converter os arquivos HEIC para JPG
    convert_heic_to_jpg(heic_files, output_folder)

if __name__ == "__main__":
    main()
