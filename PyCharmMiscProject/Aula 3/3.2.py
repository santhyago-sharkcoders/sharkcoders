# Dicionário

notas ={
    "Pedro":17,
    "Henrique":18,
    "João":7,
    "Maria":20,
}
nome = input("Digite o nome do aluno:")
if nome in notas:
    nota = notas[nome]
    print(nome, "tem nota", nota)
    if nota >= 10:
        print("Parabéns! Passou.")
    else:
        print("infelismente não passou.")
else:
    print("Aluno não esncontrado.")