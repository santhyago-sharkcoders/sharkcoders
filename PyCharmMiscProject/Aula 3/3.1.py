 # Dicionários

frutas = {
    "maçã":"vermelha",
    "banana":"amarela",
    "uva": "roxa"
 }

print(frutas["banana"])   # Vai mostrar "amarela"

print(frutas.keys())  # Mostra tods as chaves: ([ ´maçã ´, ´banana´, ´uva
print(frutas.values()) # Mostra todos os valores: ([´vermelha´, ´amarela´
print(frutas.items())  # Mostra pares chave-valor

for fruta in frutas:
    print(fruta)

#----------------------------------------------------------------------------------

pessoa = {
    "nome": "Ana",
    "idade": 12,
    "cidade": "Lisboa"}

print (pessoa["nome"])
print (pessoa["idade"])
print(pessoa["cidade"])

# Cada fruta tem várias cores possíveis
frutas= {
    "maçã":["vermelha", "verde"],
    "banana": ["amarela","verde"],
    "uva": ["roxa", "verde"]
 }

print(frutas["maçã"])
print(frutas["banana"][0])


#-----------------------------------------------------------------------------------

