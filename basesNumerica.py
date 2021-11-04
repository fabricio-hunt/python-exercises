#Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

import math

print('=*'*30)
print('CONVERSOR DE BASES NUMÉRICAS')
print('=*'*30)
print()

num = int (input('Digite um numero inteiro qualquer: '))
print('''Escola uma das Opções para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para EXADECIMAL''')

opcao = int (input('Sua Opção: '))


if opcao == 1:
    print('O valor em binário é {} '.format(bin(num)[2:]))
elif opcao == 2:
    print('O valor em octal é {}'.format(oct(num)[2:]))
elif opcao == 3:
    print('O valor em hexadecimal é {}'.format(hex(num)[2:]))
else:
    print('O valor é inválido!!')
















