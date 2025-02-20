#peça ao usuario para inserir um numero que deseja a tabuada e em seguida exiba a tabuada do numero
numero = int(input('Isira um numero'))
i = 1
for i in range(11):
    x = numero*i
    print('{} x {} = {}'.format(numero, i, x))