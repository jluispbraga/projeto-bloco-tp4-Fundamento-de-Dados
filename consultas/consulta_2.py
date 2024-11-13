import json, os

def identificar_recursos(cursor):
    cursor.execute('''
        SELECT recurso_utilizado, SUM(quantidade_utilizada) AS quantidade_total
        FROM RecursosProjeto
        WHERE tipo_recurso = 'Material'
        GROUP BY recurso_utilizado
        ORDER BY quantidade_total DESC
        LIMIT 3
    ''')

    resultados = cursor.fetchall()
    dados_json = [
        {"recurso": recurso, "quantidade_total": quantidade_total}
        for recurso, quantidade_total in resultados
    ]

    json_resultado = json.dumps(dados_json, indent=4, ensure_ascii=False)

    for recurso, quantidade_total in resultados:
        print(f"Recurso: {recurso}, Quantidade Total Usada: {quantidade_total}")

    caminho_arquivo = os.path.join('json_files', 'quantidade_total_recursos.json')
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(json_resultado)
    