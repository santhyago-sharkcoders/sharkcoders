import os  # serve para falar com o sistema operativo (pastas, ficheiros).
import shutil  # serve para copiar ou mover ficheiros

print("=== Organizador de Ficheiros ===")

# 1. Perguntar a pasta onde estão os ficheiros
pasta = input("Digite o caminho da pasta que deseja organizar: ")

# while True:
#    pasta = input("Digite o caminho da pasta que deseja organizar: ")
#    if os.path.exists(pasta):
#        break
#    else:
#        print("Pasta não existe. Tente novamente!")

# 2. Definir categorias
categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Áudio": [".mp3", ".wav"],
    "Vídeos": [".mp4", ".avi", ".mov"],
    "Outros": []
}
# 3. Criar subpastas se não existirem
for categoria in categorias:
    caminho_subpasta = os.path.join(pasta, categoria)
    # C:\Users\Ana\Downloads -> C:\Users\Ana\Downloads\Imagens
    if not os.path.exists(caminho_subpasta):
        os.mkdir(caminho_subpasta)

# 4. Ler ficheiros da pasta
for ficheiro in os.listdir(pasta):  # listdir é uma lista dos ficheiros da pasta
    caminho_ficheiro = os.path.join(pasta, ficheiro)
    # C:\Users\Ana\Downloads -> C:\Users\Ana\Downloads\foto.jpg
    if os.path.isfile(caminho_ficheiro):
        nome, extensao = os.path.splitext(ficheiro)
        # foto.jpg -> nome = "foto", extensão = ".jpg".

        # Verificar categoria do ficheiro
        movido = False
        for categoria, extensoes in categorias.items():
            if extensao.lower() in extensoes:
                shutil.move(caminho_ficheiro, os.path.join(pasta, categoria, ficheiro))
                movido = True
                break
        # Se não estiver em nenhuma categoria, vai para "Outros"
        if not movido:
            shutil.move(caminho_ficheiro, os.path.join(pasta, "Outros", ficheiro))

print("Organização concluída!")