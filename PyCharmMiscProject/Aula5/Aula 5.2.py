def verificar_velocidades(velocidades, limite):
     for v in velocidades:
        if v > limite:
            print(v, "km/h acima do limite!")
        else:
            print(v, "km/h dentro do limite!")



velocidades_carros =[123456798765765,1499,6786,0,1000]

limite_usuario =int(input("Qual é o limite de velocidades? "))

verificar_velocidades(velocidades_carros, limite_usuario)








