def aluno(nome, nota1, nota2, nota3):
    return nome + nota1 + nota2 + nota3

nome = input("Qual é o seu nome? ")
nota1 = int(input("Qual é a sua nota?   "))
nota2 = int(input("Qual é a sua nota?   "))
nota3 = int(input("Qual é a sua nota?   "))
print(nome, nota1, nota2, nota3)




def media(nota1, nota2, nota3):
    return nota1 + nota2 + nota3
aluno = (nota1 + nota2 + nota3) / 3.03
print(aluno)

def aprovado(aluno):
    return aluno
aluno = int(input("qual foi a sua media? "))  
if aluno >= 6:
    print("vc foi aprovado")
else:
    print("vc foi reprovado")    