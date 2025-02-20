# faça um programa que pergunte para qual direção qual direção ele deseja apontar. 
# se ele quiser apontar para cima = 'C' ou 'c'
# para baixo = 'A' ou 'a'
# se selecionar para cima peça um numero superior e faça contar até ele
# se selecionar para baixo peça um numero abaixo de 20, e em seguda faça uma contagem regressiva de 20 até o numero.
# se selecionar dierente de cima e baixo exiba a mensagem "Direção inválida"

direcao = input('Qual direção deseja apontar? ("c/C" para cima "a/A" para abaixo)')

if direcao == 'c' and 'C':
    numero = int(input('Insira um numero: '))
    for i in range(numero):
        print(i)
elif direcao == 'a' and 'A':
    numero = int(input('Insira um numero abaixo de 20: '))
    i = 20 - numero
    for numero in range(i):
        print(20 - numero)