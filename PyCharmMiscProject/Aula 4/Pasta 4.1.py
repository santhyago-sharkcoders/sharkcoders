#Criar uma subpasta
import os

pasta_principal =input("Escreva o caminho da pasta onde quer criar algo: ")
#exemplo: "C:/Users/Ana/Downloads"
nova_pasta = input("Escreva o neme da nova pasta: ")
#exemplo: fotos

caminho_novo = os.path.join(pasta_principal,nova_pasta)
#resultado exemplo: C:/User/Ana/Downloads/fotos

if not os.path.exists(caminho_novo):
    os.mkdir(caminho_novo)
    print("Pasta criado com sucesso!")
else:
    print("Essa pasta já existe!")


#----------------------------------------------------------------------------------
