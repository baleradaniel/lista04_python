# peça um numero abaixo de 50 e em seguida faça uma contagem regressiva de 50 até esse numero, certificando-se de mostrar que eles inseriram na saida.

numero = int(input('Insira um numero: '))
i = 50 - numero
for numero in range(i):
    print(50 - numero)