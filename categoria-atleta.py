#A Confederação Nacional de Natação precisa de um programa que 
#leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

print('=*'*30)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('=*'*30)


anoNascimento = int (input('Digite o ano do seu nascimento: '))

idadeAtleta =  2021 - anoNascimento


if idadeAtleta <= 9:
  print('MIRIM')

elif idadeAtleta >= 9 and idadeAtleta < 19:
  print('INFANTIL')

elif idadeAtleta >= 19 and idadeAtleta < 25:
  print('JÚNIOR')

elif idadeAtleta == 25:
  print('SÊNIOR')

elif idadeAtleta > 25:
  print('MASTER')

