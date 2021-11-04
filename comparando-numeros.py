#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem


print('=-'*30)
print('ANALISADOR DE NÚMEROS')
print('=-'*30)
print()


num1 = int (input('Escreva o primeiro número: '))
num2 = int (input('Escreva o segundo número: '))




if num1 > num2:
    print('O primeiro número é maior foi o {}'.format(num1))

elif num2 > num1:
    print('O segundo número é maior foi o {}'.format(num2))
else:
    print('Os números  são iguais')