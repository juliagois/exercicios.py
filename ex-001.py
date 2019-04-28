from random import randint
computador = randint(0, 50)
jogador = int(input("Advinhe o número!"))
if jogador == computador:
    print(" Você acertou!")
else:    
 if jogador < computador:
    print("É um número maior")
 elif jogador > computador:
    print("É um número menor")

