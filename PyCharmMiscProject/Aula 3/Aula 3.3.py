import os

# Vr o que há numa pasta
pasta = input("Escreva o caminho de uma pasta:")

# Verificar se a pasta existe
if os.path.exists(pasta):
    ficheiros = os.listdir(pasta)
    print("\aAqui estão os ficheiros e pastas que encontrei:")
    for f in ficheiros:
        print("-", f)

else:
    print("Essa pasta não existe! Verifique o caminho e tente novamente")
