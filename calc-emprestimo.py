# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('=*'*45)
print('SISTEMA DE EMPRÉSTIMO')
print('=*'*45)

valorCasa = float (input('Digite o valor da sua casa? '))
salarioComprador = float (input('Digite seu salário: '))
prestacao = int (input('Em quantos anos você pretende pagar a casa? '))

prestacaoNova = valorCasa / (prestacao * 12) 

novoSalario = salarioComprador *30/100


if prestacaoNova < novoSalario:
  print('PARABÉNS você pode fazer o emprestimo! a  prestação será de {:.2f}'.format(prestacaoNova))
else:
  print('INFELIZMENTE vocÊ não pode fazer o empréstimo prestação é {:.2f}'.format(prestacaoNova))


