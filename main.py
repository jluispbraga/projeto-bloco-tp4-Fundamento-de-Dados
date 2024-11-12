import sqlite3
import os

from create_tables import *
from consultas import consulta_1, consulta_2, consulta_3, consulta_4, consulta_5

diretorio = 'src'
os.makedirs(diretorio, exist_ok=True)
connection = sqlite3.connect(os.path.join(diretorio, 'empresa.db'))

# Buildar o banco de dados e criar os csv 
run(connection)

def executar_consulta(target, conn):
    if target == 1:
        consulta_1.media_salarios_atuais(conn)
    elif target == 2:
        consulta_2.identificar_recursos(conn)
    elif target == 3:
        consulta_3.custo_total_projetos(conn)
    elif target == 4:
        consulta_4.listar_projetos(conn)
    elif target == 5:
        consulta_5.projeto_maior_dependetnes(conn)
    else: 
        print('Consulta inexistente, favor digitar um número válido')
        
# Listagem das consultas
def options():
    print('1 - Trazer a média dos salários (atual) dos funcionários responsáveis por projetos concluídos, agrupados por departamento.')
    print('2 - Identificar os três recursos materiais mais usados nos projetos, listando a descrição do recurso e a quantidade total usada.')
    print('3 - Calcular o custo total dos projetos por departamento, considerando apenas os projetos "Concluídos"')
    print('4 - Listar todos os projetos com seus respectivos nomes, custo, data de início, data de conclusão e o nome do funcionário responsável, que estejam Em "Execução".')
    print('5 - Identificar o projeto com o maior número de dependentes envolvidos, considerando que os dependentes são associados aos funcionários que estão gerenciando os projetos.')
    return int(input('Digite o número da consulta: '))


print('Conectado com banco de dados!')
print('Bem-vindo ao programa!')

while True:
    consulta = int(options())

    # Verifica se a consulta é válida antes de tentar executá-la
    if consulta in [1, 2, 3, 4, 5]:
        print('Executando consulta...')
        executar_consulta(consulta, connection.cursor())
    else:
        print('Entrada inválida! Por favor, digite um número válido.')

    continuar = input('Deseja realizar outra consulta? (sim/não) ').strip().lower()
    if continuar in ['n', 'nao', 'não']:
        print('Saindo do sistema...')
        break