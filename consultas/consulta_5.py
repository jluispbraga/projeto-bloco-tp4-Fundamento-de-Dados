def projeto_maior_dependetnes(cursor):
    cursor.execute('''
        SELECT p.nome, COUNT(d.id) AS num_dependentes
        FROM ProjetosDesenvolvidos p
        JOIN Funcionarios f ON p.responsavel_id = f.id
        LEFT JOIN Dependentes d ON f.id = d.funcionario_id
        GROUP BY p.id
        ORDER BY num_dependentes DESC
        LIMIT 1
    ''')

    resultados = cursor.fetchall()
    for nome, num_dependentes in resultados:
        if resultados is None:
            print('Nenhum projeto com dependentes encontrado')
            return
        print(f"Projeto: {nome}, Número de Dependentes: {num_dependentes}")
