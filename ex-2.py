idade = int(input("Qual é a sua idade?"))
salario = int(input("Qual é o seu salario?"))
emprestimo = int(input("Qual é o valor do emprestimo?"))

if idade >= 22 and idade <= 55: 
  if salario <= 1000:
   print("emprestimo aceito")
  elif emprestimo <= 15 * salario:
else:
    print("emprestimo negado") 
