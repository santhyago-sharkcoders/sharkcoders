
#Mover um ficheiro
import shutil

origem = input ("Escreva o caminho completo do ficheiro que quer mover")
destino = input("Escreva o destino: ")
shutil.move(origem,destino)
print("Ficheiro movido com sucesso!")