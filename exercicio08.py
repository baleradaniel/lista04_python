# defina uma variavel chamada 'total' como zero. Peça ao usuario para inserir 5 numeros e, apos cada entrada pergunte se ele deseja que este numero seja incluido (S ou s, N ou n).
# se ele desejar, adicione o numero ao total. se ele nao quiser incluilo, nao adicione ao total. depois de inserir os 5 numeros exiba o total.

total = 0

for i in range(5):
    numero = int(input('Insira o {}º numero: '.format(i+1)))
    confirmacao = input('Deseja incluir esse numero? ')
    if confirmacao == 's' and 'S':
        total = total + numero
    else:
        i = i - 1
print('{} é o total dos numeros incluidos.'.format(total))

