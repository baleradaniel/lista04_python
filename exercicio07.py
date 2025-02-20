# peça ao usuario para inserir o seu nome e um numero. se o numero for menor que 10 exiba o nome dele esse numero de vezes, caso contrario, exiba a mensagem "numero muito alto" tres vezes.

nome = input('Insira o seu nome: ')
numero = int(input('Insira um numero: '))

if numero < 10:
    for i in range(numero):
        print(nome)
else: 
    print('Numero muito alto')