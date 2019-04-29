idade = int(input("Qual é a sua idade? "))
salario = float(input("Qual é o seu salario? R$ "))
emprestimo = int(input("Qual é o valor do emprestimo? R$ "))


if idade >= 22 and idade <= 55: 
  print("emprestimo aceito")
elif salario >= 1000:
  print("segunda passo aceito")
elif emprestimo <= 15 * salario:
  print("emprestimo aceito")
aceito = input(" aceita ou não aceita o emprestimo? ")       
else:
  print("emprestimo negado")

   

  