"""
Você é um desenvolvedor de sistemas trabalhando em um projeto colaborativo com sua equipe.
Para garantir que todas as tarefas do projeto sejam concluídas dentro do prazo, você decide criar um pequeno programa para controlar o status das tarefas.
O programa deve permitir que você insira o nome de cada tarefa e indique se ela está concluída ou não.
No final, o programa deve apresentar um resumo com o total de tarefas, quantas estão concluídas e quantas ainda estão pendentes.
Desenvolva um programa em Python que:
1.	Solicite ao usuário o número de tarefas a serem inseridas.
2.	Para cada tarefa, solicite o nome da tarefa e se ela está concluída (aceitando "sim", "s", "não" ou "n").
3.	Conte e exiba o número de tarefas concluídas e não concluídas.
"""

n_tarefas = int(input('Insira o numero de tarefas a serem inseridas: '))
tarefas_concluidas = 0
tarefas_nao_concluidas = 0

for i in range(n_tarefas):
    nome_tarefa = input('Insira o nome da tarefa: ')
    status_tarefa = input('Concluida? ')
    if status_tarefa == 'sim' or 's':
        tarefas_concluidas = + 1
    elif status_tarefa == 'não' or 'n':
        tarefas_nao_concluidas = + 1

print('Nº de tarefas concluídas: ', tarefas_concluidas)
print('Nº de tarefas não concluídas: ', tarefas_nao_concluidas)
