def listar_projetos(cursor):
    cursor.execute('''
        SELECT p.nome, p.custo, p.dt_inicio, p.dt_conclusao, f.nome AS nome_responsavel
        FROM ProjetosDesenvolvidos p
        JOIN Funcionarios f ON p.responsavel_id = f.id
        WHERE p.status = 'Em Execução'
    ''')

    resultados = cursor.fetchall()
    for nome, custo, dt_inicio, dt_conclusao, nome_responsavel in resultados:
        print(f"Projeto: {nome}, Custo: {custo}, Data Início: {dt_inicio}, Data Conclusão: {dt_conclusao}, Responsável: {nome_responsavel}")
