import csv
import os
import pandas as pd

'''
    Dados que serão usados
    Dados pegos do TP3
'''
funcionarios = [
    {'id': 1, 'nome': 'João Silva', 'cargo_id': 1, 'departamento_id': 1},
    {'id': 2, 'nome': 'Ana Santos', 'cargo_id': 2, 'departamento_id': 1},
    {'id': 3, 'nome': 'Pedro Costa', 'cargo_id': 3, 'departamento_id': 2},
    {'id': 4, 'nome': 'Lucas Pereira', 'cargo_id': 2, 'departamento_id': 3},
    {'id': 5, 'nome': 'Mariana Souza', 'cargo_id': 4, 'departamento_id': 4},
    {'id': 6, 'nome': 'Fernanda Lima', 'cargo_id': 1, 'departamento_id': 2},
    {'id': 7, 'nome': 'Carlos Dias', 'cargo_id': 5, 'departamento_id': 3},
    {'id': 8, 'nome': 'Juliana Andrade', 'cargo_id': 3, 'departamento_id': 5},
    {'id': 9, 'nome': 'Fábio Castro', 'cargo_id': 4, 'departamento_id': 4},
    {'id': 10, 'nome': 'Beatriz Alves', 'cargo_id': 5, 'departamento_id': 5},
    {'id': 11, 'nome': 'Rafael Alves', 'cargo_id': 2, 'departamento_id': 2},
    {'id': 12, 'nome': 'Camila Rocha', 'cargo_id': 1, 'departamento_id': 5},
    {'id': 13, 'nome': 'Eduardo Mello', 'cargo_id': 2, 'departamento_id': 1},
    {'id': 14, 'nome': 'Patrícia Moreira', 'cargo_id': 1, 'departamento_id': 3},
    {'id': 15, 'nome': 'Tiago Lopes', 'cargo_id': 3, 'departamento_id': 4},
    {'id': 16, 'nome': 'Roberta Martins', 'cargo_id': 4, 'departamento_id': 1},
    {'id': 17, 'nome': 'Fernando Nunes', 'cargo_id': 5, 'departamento_id': 2},
    {'id': 18, 'nome': 'Larissa Barros', 'cargo_id': 1, 'departamento_id': 4},
    {'id': 19, 'nome': 'Vinícius Azevedo', 'cargo_id': 2, 'departamento_id': 5},
    {'id': 20, 'nome': 'Aline Fernandes', 'cargo_id': 3, 'departamento_id': 3},
]

cargos = [
    {'id': 1, 'nome': 'Estagiário'},
    {'id': 2, 'nome': 'Analista'},
    {'id': 3, 'nome': 'Gerente'},
    {'id': 4, 'nome': 'Diretor'},
    {'id': 5, 'nome': 'Técnico'},
]

departamentos = [
    {'id': 1, 'nome': 'Recursos Humanos'},
    {'id': 2, 'nome': 'Tecnologia'},
    {'id': 3, 'nome': 'Financeiro'},
    {'id': 4, 'nome': 'Marketing'},
    {'id': 5, 'nome': 'Vendas'},
]

historico_salarios = [
    {'id': 1, 'funcionario_id': 1, 'mes': 1, 'ano': 2024, 'salario': 1500},
    {'id': 2, 'funcionario_id': 2, 'mes': 6, 'ano': 2024, 'salario': 5000},
    {'id': 3, 'funcionario_id': 3, 'mes': 3, 'ano': 2024, 'salario': 7000},
    {'id': 4, 'funcionario_id': 4, 'mes': 7, 'ano': 2024, 'salario': 6000},
    {'id': 5, 'funcionario_id': 5, 'mes': 12, 'ano': 2024, 'salario': 9000},
    {'id': 6, 'funcionario_id': 11, 'mes': 2, 'ano': 2024, 'salario': 5200},
    {'id': 7, 'funcionario_id': 12, 'mes': 4, 'ano': 2024, 'salario': 1300},
    {'id': 8, 'funcionario_id': 13, 'mes': 5, 'ano': 2024, 'salario': 5100},
    {'id': 9, 'funcionario_id': 14, 'mes': 3, 'ano': 2024, 'salario': 1400},
    {'id': 10, 'funcionario_id': 15, 'mes': 6, 'ano': 2024, 'salario': 7500},
    {'id': 11, 'funcionario_id': 16, 'mes': 8, 'ano': 2024, 'salario': 9200},
    {'id': 12, 'funcionario_id': 17, 'mes': 2, 'ano': 2024, 'salario': 4500},
    {'id': 13, 'funcionario_id': 18, 'mes': 3, 'ano': 2024, 'salario': 1550},
    {'id': 14, 'funcionario_id': 19, 'mes': 1, 'ano': 2024, 'salario': 5300},
    {'id': 15, 'funcionario_id': 20, 'mes': 11, 'ano': 2024, 'salario': 7200},
    {'id': 16, 'funcionario_id': 4, 'mes': 8, 'ano': 2024, 'salario': 6200},
    {'id': 17, 'funcionario_id': 4, 'mes': 9, 'ano': 2024, 'salario': 6300},
    {'id': 18, 'funcionario_id': 4, 'mes': 10, 'ano': 2024, 'salario': 6400},
    {'id': 19, 'funcionario_id': 2, 'mes': 8, 'ano': 2024, 'salario': 5100},
    {'id': 20, 'funcionario_id': 2, 'mes': 9, 'ano': 2024, 'salario': 5200},
    {'id': 21, 'funcionario_id': 2, 'mes': 10, 'ano': 2024, 'salario': 5300},
]

dependentes = [
    {'id': 1, 'funcionario_id': 1, 'nome': 'Maria Silva', 'idade': 5, 'genero': 'Feminino'},
    {'id': 2, 'funcionario_id': 1, 'nome': 'Lucas Silva', 'idade': 3, 'genero': 'Masculino'},
    {'id': 3, 'funcionario_id': 2, 'nome': 'Pedro Santos', 'idade': 7, 'genero': 'Masculino'},
    {'id': 4, 'funcionario_id': 4, 'nome': 'Ana Santos', 'idade': 4, 'genero': 'Feminino'},
    {'id': 5, 'funcionario_id': 4, 'nome': 'Carla Costa', 'idade': 6, 'genero': 'Feminino'},
    {'id': 6, 'funcionario_id': 11, 'nome': 'Fernanda Alves', 'idade': 3, 'genero': 'Feminino'},
    {'id': 7, 'funcionario_id': 11, 'nome': 'Julia Alves', 'idade': 5, 'genero': 'Feminino'},
    {'id': 8, 'funcionario_id': 12, 'nome': 'Gabriel Rocha', 'idade': 2, 'genero': 'Masculino'},
    {'id': 9, 'funcionario_id': 13, 'nome': 'Sofia Mello', 'idade': 6, 'genero': 'Feminino'},
    {'id': 10, 'funcionario_id': 13, 'nome': 'Laura Mello', 'idade': 4, 'genero': 'Feminino'},
    {'id': 11, 'funcionario_id': 14, 'nome': 'Paulo Moreira', 'idade': 8, 'genero': 'Masculino'},
    {'id': 12, 'funcionario_id': 15, 'nome': 'Alice Lopes', 'idade': 5, 'genero': 'Feminino'},
    {'id': 13, 'funcionario_id': 17, 'nome': 'Caio Nunes', 'idade': 6, 'genero': 'Masculino'},
    {'id': 14, 'funcionario_id': 18, 'nome': 'Marina Barros', 'idade': 2, 'genero': 'Feminino'},
    {'id': 15, 'funcionario_id': 19, 'nome': 'Lucas Azevedo', 'idade': 3, 'genero': 'Masculino'},
]

# Dados novos para o contexto do TP4
projetos_desenvolvidos = [
    {
        "id": 1,
        "nome": "Desenvolvimento de Sistema de Gestão",
        "descricao": "Sistema para gerenciar operações internas da empresa.",
        "dt_inicio": "2024-01-10",
        "dt_conclusao": "2024-04-15",
        "responsavel_id": 1,
        "custo": 15000.0,
        "observacoes": "Projeto prioritário para o primeiro semestre.",
        "status": "Concluído"
    },
    {
        "id": 2,
        "nome": "Implementação de CRM",
        "descricao": "Sistema de gestão de relacionamento com o cliente.",
        "dt_inicio": "2024-05-01",
        "dt_conclusao": "2024-09-20",
        "responsavel_id": 3,
        "custo": 22000.0,
        "observacoes": "Necessidade de integração com o sistema legado.",
        "status": "Em Execução"
    },
    {
        "id": 3,
        "nome": "Desenvolvimento de Aplicativo Móvel",
        "descricao": "Aplicativo móvel para clientes acessarem seus dados.",
        "dt_inicio": "2024-06-15",
        "dt_conclusao": None,
        "responsavel_id": 5,
        "custo": 18000.0,
        "observacoes": "Em fase inicial, definição de requisitos.",
        "status": "Em Planejamento"
    },
    {
        "id": 4,
        "nome": "Reestruturação do Site Institucional",
        "descricao": "Redesign do site corporativo da empresa.",
        "dt_inicio": "2024-03-10",
        "dt_conclusao": "2024-06-05",
        "responsavel_id": 2,
        "custo": 8000.0,
        "observacoes": "Redesign completo com SEO otimizado.",
        "status": "Concluído"
    },
    {
        "id": 5,
        "nome": "Migração para Nuvem",
        "descricao": "Migração de servidores e banco de dados para a nuvem.",
        "dt_inicio": "2024-02-01",
        "dt_conclusao": "2024-12-15",
        "responsavel_id": 7,
        "custo": 50000.0,
        "observacoes": "Expectativa de reduzir custos de infraestrutura.",
        "status": "Em Execução"
    },
    {
        "id": 6,
        "nome": "Treinamento de Equipe",
        "descricao": "Programa de capacitação para os colaboradores.",
        "dt_inicio": "2024-04-20",
        "dt_conclusao": "2024-07-25",
        "responsavel_id": 4,
        "custo": 12000.0,
        "observacoes": "Treinamento em novas ferramentas de gestão.",
        "status": "Concluído"
    },
    {
        "id": 7,
        "nome": "Projeto de Sustentabilidade",
        "descricao": "Implementação de práticas de sustentabilidade.",
        "dt_inicio": "2024-08-01",
        "dt_conclusao": None,
        "responsavel_id": 10,
        "custo": 25000.0,
        "observacoes": "Atividade contínua sem prazo definido.",
        "status": "Em Planejamento"
    }
]

recursos_projetos = [
    {
        "id": 1,
        "projeto_id": 1,
        "recurso_utilizado": "Orçamento inicial",
        "tipo_recurso": "Financeiro",
        "quantidade_utilizada": 15000,
        "dt_utilizacao": "2024-01-10"
    },
    {
        "id": 2,
        "projeto_id": 2,
        "recurso_utilizado": "Consultoria de CRM",
        "tipo_recurso": "Humano",
        "quantidade_utilizada": 3,
        "dt_utilizacao": "2024-05-10"
    },
    {
        "id": 3,
        "projeto_id": 3,
        "recurso_utilizado": "Servidores de Teste",
        "tipo_recurso": "Material",
        "quantidade_utilizada": 5,
        "dt_utilizacao": "2024-06-20"
    },
    {
        "id": 4,
        "projeto_id": 4,
        "recurso_utilizado": "Equipe de Desenvolvimento Web",
        "tipo_recurso": "Humano",
        "quantidade_utilizada": 4,
        "dt_utilizacao": "2024-03-15"
    },
    {
        "id": 5,
        "projeto_id": 5,
        "recurso_utilizado": "Serviços em Nuvem",
        "tipo_recurso": "Financeiro",
        "quantidade_utilizada": 20000,
        "dt_utilizacao": "2024-02-15"
    },
    {
        "id": 6,
        "projeto_id": 6,
        "recurso_utilizado": "Materiais de Treinamento",
        "tipo_recurso": "Material",
        "quantidade_utilizada": 50,
        "dt_utilizacao": "2024-04-25"
    },
    {
        "id": 7,
        "projeto_id": 7,
        "recurso_utilizado": "Equipe de Sustentabilidade",
        "tipo_recurso": "Humano",
        "quantidade_utilizada": 5,
        "dt_utilizacao": "2024-08-05"
    },
    {
        "id": 8,
        "projeto_id": 1,
        "recurso_utilizado": "Equipamentos de TI",
        "tipo_recurso": "Material",
        "quantidade_utilizada": 10,
        "dt_utilizacao": "2024-02-01"
    }
]
'''
    Fim dos dados usados
'''

# Funcao para crias as tabelas
def create_tables(conn):
    cursor = conn.cursor()

    '''
        Inicio da criação das tabelas
    '''
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cargo_id INTEGER,
        departamento_id INTEGER,
        FOREIGN KEY(cargo_id) REFERENCES Cargos(id),
        FOREIGN KEY(departamento_id) REFERENCES Departamentos(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cargos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departamentos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS HistoricoSalarios (
        id INTEGER PRIMARY KEY,
        funcionario_id INTEGER,
        mes INTEGER,
        ano INTEGER,
        salario REAL,
        FOREIGN KEY(funcionario_id) REFERENCES Funcionarios(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Dependentes (
        id INTEGER PRIMARY KEY,
        funcionario_id INTEGER,
        nome TEXT NOT NULL,
        idade INTEGER,
        genero TEXT NOT NULL,
        FOREIGN KEY(funcionario_id) REFERENCES Funcionarios(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ProjetosDesenvolvidos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        descricao TEXT NOT NULL,
        dt_inicio DATE NOT NULL,
        dt_conclusao DATE,
        responsavel_id INTEGER UNIQUE NOT NULL,
        custo FLOAT,
        observacoes TEXT, 
        status TEXT CHECK (status IN ('Em Planejamento', 'Em Execução', 'Concluído', 'Cancelado')),
        FOREIGN KEY(responsavel_id) REFERENCES Funcionarios(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS RecursosProjeto (
        id INTEGER PRIMARY KEY,
        projeto_id INTEGER,
        recurso_utilizado TEXT,
        tipo_recurso TEXT CHECK (tipo_recurso IN ('Financeiro', 'Material', 'Humano')),
        quantidade_utilizada INTEGER,
        dt_utilizacao DATE,
        FOREIGN KEY(projeto_id) REFERENCES ProjetosDesenvolvidos(id)
    )
    ''')

    conn.commit()

    '''
        Fim da criação das tabela
    '''

# Função para criar o csv
def create_csv(nome_arquivo, dados, campos):
    '''
    :param nome_arquivo:
    :param dados:
    :param campos:
    :return: criar um csv com os dados do arquivo
    '''
    os.makedirs('src', exist_ok=True)
    caminho_arquivo = os.path.join('src', nome_arquivo)
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(dados)


# Função para criar o csv um por um
def run_create_datas():
    tables_and_data = [
        ('funcionarios.csv', funcionarios, ['id', 'nome', 'cargo_id', 'departamento_id']),
        ('cargos.csv', cargos, ['id', 'nome']),
        ('departamentos.csv', departamentos, ['id', 'nome']),
        ('historico_salarios.csv', historico_salarios, ['id', 'funcionario_id', 'mes', 'ano', 'salario']),
        ('dependentes.csv', dependentes, ['id', 'funcionario_id', 'nome', 'idade', 'genero']),
        ('projetos_desenvolvidos.csv', projetos_desenvolvidos, ['id', 'nome', 'descricao', 'dt_inicio', 'dt_conclusao', 'responsavel_id', 'custo', 'observacoes', 'status']),
        ('recursos_projetos.csv', recursos_projetos, ['id', 'projeto_id', 'recurso_utilizado', 'tipo_recurso', 'quantidade_utilizada', 'dt_utilizacao'])
    ]
    
    # Cria cada arquivo CSV com tratamento de erros
    for file_name, data, columns in tables_and_data:
        create_csv(file_name, data, columns)

# Função para importar para o banco de dados
def import_csv_to_bd(nome_tabela, caminho_csv, conn):
    '''
    :param nome_tabela:
    :param caminho_csv:
    :return: converter o csv para sql e preencher o banco de dados
    '''
    caminho_arquivo = os.path.join('src', caminho_csv)
    df = pd.read_csv(caminho_arquivo, sep=',', encoding='utf-8')
    df.to_sql(nome_tabela, conn, if_exists='replace', index=False)


# Função para criar tabelas-criacao do banco de dados
def run_create_tables(conn):
    tables_and_files = [
        ('Funcionarios', 'funcionarios.csv'),
        ('Cargos', 'cargos.csv'),
        ('Departamentos', 'departamentos.csv'),
        ('HistoricoSalarios', 'historico_salarios.csv'),
        ('Dependentes', 'dependentes.csv'),
        ('ProjetosDesenvolvidos', 'projetos_desenvolvidos.csv'),
        ('RecursosProjeto', 'recursos_projetos.csv')
    ]
    
    # Importa cada tabela e arquivo CSV
    for table_name, csv_file in tables_and_files:
        import_csv_to_bd(table_name, csv_file, conn)


def run(conn):
    create_tables(conn)
    run_create_datas()
    run_create_tables(conn)