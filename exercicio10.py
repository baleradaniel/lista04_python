"""
Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
	Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
	Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
"""

qtde_convidados = int(input('Quantos convidados desea convidar para a festa? '))
convidados = []
if qtde_convidados < 10:
    for i in range(qtde_convidados):
        nome = input('Insira o nome do {}º convidado: '.format(i + 1))
        convidados.append(nome)
        print('{} está convidado para a festa.'.format(nome))
else:
    print('Muitas pessoas')