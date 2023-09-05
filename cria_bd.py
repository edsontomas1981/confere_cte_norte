import sqlite3

# Função para criar o banco de dados e a tabela
def criar_banco_de_dados_e_tabela():
    try:
        conn = sqlite3.connect('banco_de_dados.db')
        cursor = conn.cursor()

        # Cria a tabela (substitua 'sua_tabela' pelo nome desejado)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sua_tabela (
                ci_num INTEGER PRIMARY KEY AUTOINCREMENT,
                destinatario TEXT,
                manifesto_numero TEXT,
                motorista TEXT,
                valor_frete REAL,
                percurso TEXT,
                data TEXT,
                observacao TEXT
            )
        ''')

        conn.commit()
        conn.close()
        print("Banco de dados e tabela criados com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados e a tabela: {e}")

# Chame a função para criar o banco de dados e a tabela
criar_banco_de_dados_e_tabela()
