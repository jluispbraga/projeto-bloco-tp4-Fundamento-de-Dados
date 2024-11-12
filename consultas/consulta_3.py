def custo_total_projetos(cursor):
    cursor.execute('''
    SELECT d.nome AS departamento, SUM(p.custo) AS custo_total
    FROM ProjetosDesenvolvidos p
    JOIN Funcionarios f ON p.responsavel_id = f.id
    JOIN Departamentos d ON f.departamento_id = d.id
    WHERE p.status = 'Concluído'
    GROUP BY d.id;
    ''')

    resultados = cursor.fetchall()
    for departamento, custo_total in resultados:
        print(f"Departamento: {departamento}, Custo Total: {custo_total}")
