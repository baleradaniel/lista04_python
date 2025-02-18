# faça um programa que solicite ao usuario para digitar o seu nome e um numero qualquer, e em seguida, exiba seu nome varias vezes de acordo com o numero que ele digitou.

nome = input('insira o nome: ')
qtde = int(input('quantidade de repetição: '))
for i in range(qtde):
    print(nome)
