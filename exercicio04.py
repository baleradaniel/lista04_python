# escreva um programa para solicitar um numero e em seguida o nome. exiba o nome (uma letra de cada vez em cada linha) e repita isso para o numero de vezes que ele digitou.

numero = int(input('Insira um numero: '))
nome = input('Insira o seu nome: ')
i = len(nome)
for i in range(numero):
    for i in nome:
        print(i)