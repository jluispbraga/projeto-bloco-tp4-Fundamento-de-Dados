import json, os

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
    dados_json = [
        {"departamento": departamento, "custo_total": custo_total}
        for departamento, custo_total in resultados
    ]

    json_resultado = json.dumps(dados_json, indent=4, ensure_ascii=False)

    for departamento, custo_total in resultados:
        print(f"Departamento: {departamento}, Custo Total: {custo_total}")

    caminho_arquivo = os.path.join('json_files', 'departamento_custo_total.json')
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(json_resultado)
