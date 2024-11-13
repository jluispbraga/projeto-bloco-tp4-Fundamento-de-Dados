import json, os

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

    resultados = cursor.fetchall()
    dados_json = [
        {"departamento": departamento, "media_salarios": media_salario}
        for departamento, media_salario in resultados
    ]
    
    json_resultado = json.dumps(dados_json, indent=4, ensure_ascii=False)

    for departamento, media_salario in resultados:
        print(f"Departamento: {departamento}, Média dos Salários: {media_salario}")

    caminho_arquivo = os.path.join('json_files', 'departamento_media_salarial.json')
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(json_resultado)