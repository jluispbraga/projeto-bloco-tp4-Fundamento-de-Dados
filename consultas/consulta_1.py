def media_salarios_atuais(cursor):
# Consulta SQL
    cursor.execute('''
        SELECT d.nome AS departamento,
            AVG(h.salario) AS media_salarios
        FROM Funcionarios f
        JOIN ProjetosDesenvolvidos p ON f.id = p.responsavel_id
        JOIN HistoricoSalarios h ON f.id = h.funcionario_id
        JOIN Departamentos d ON f.departamento_id = d.id
        WHERE 
            p.status = 'Concluído' 
            AND h.ano = strftime('%Y', 'now')
        GROUP BY d.id;
    ''')

    # Recuperando os resultados
    resultados = cursor.fetchall()
    for departamento, media_salario in resultados:
        print(f"Departamento: {departamento}, Média dos Salários: {media_salario}")
