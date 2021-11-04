#Faça um programa que leia o ano de nascimento de um jovem e informe, 
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


anoNascimento = int (input('Digite o ano do seu Nascimento: '))

idadeAlistado = 2021 - anoNascimento


if idadeAlistado == 18:
  print('Aliste-se IMEDIATAMENTE!')

elif idadeAlistado > 18:
  print(' Seu alistamento foi em {} !VocÊ passou da data de alistamento em {} Anos)'.format(anoNascimento + 18 , idadeAlistado -18))

elif idadeAlistado < 18:
  print('Você tem {} anos e seu alistamento será em {} '.format(idadeAlistado , anoNascimento +18 ))


