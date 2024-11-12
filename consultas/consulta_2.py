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
    for recurso, quantidade_total in resultados:
        print(f"Recurso: {recurso}, Quantidade Total Usada: {quantidade_total}")
