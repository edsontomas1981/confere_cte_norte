import tkinter as tk
from tkinter import ttk
from comunicacao_interna import imprimir_ci
import webbrowser
import sqlite3

def salvar_formulario():
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    
    ci_num = ci_num_entry.get()
    destinatario = destinatario_entry.get()
    manifesto_numero = manifesto_numero_entry.get()
    motorista = motorista_entry.get()
    valor_frete = float(valor_frete_entry.get())
    percurso = percurso_entry.get()
    data = data_entry.get()
    observacao = observacao_text.get("1.0", "end-1c")

    # Inserir os dados na tabela do banco de dados
    cursor.execute("INSERT INTO sua_tabela (destinatario, manifesto_numero, motorista, valor_frete, percurso, data, observacao) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (destinatario, manifesto_numero, motorista, valor_frete, percurso, data, observacao))
    
    conn.commit()
    conn.close()

def excluir_formulario():
    # Adicione aqui a lógica para excluir os dados do formulário
    pass

def imprimir_formulario():
    ci_num = ci_num_entry.get()
    destinatario = destinatario_entry.get()
    manifesto_numero = manifesto_numero_entry.get()
    motorista = motorista_entry.get()
    valor_frete = valor_frete_entry.get()
    percurso = percurso_entry.get()
    data = data_entry.get()
    observacao = observacao_text.get("1.0", "end-1c")

    # Chame a função com os novos campos
    imprimir_ci(ci_num, destinatario, manifesto_numero, motorista, valor_frete, percurso, data, observacao)

    # Após gerar o PDF, abrir automaticamente para impressão
    pdf_filename = "documento.pdf"
    try:
        webbrowser.open(pdf_filename)
    except Exception as e:
        print(f"Erro ao abrir o PDF: {e}")

# Função para preencher o Treeview com os registros do banco de dados
def preencher_treeview():
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()

    # Execute uma consulta para recuperar todos os registros
    cursor.execute("SELECT * FROM sua_tabela")
    registros = cursor.fetchall()

    # Limpe o Treeview antes de preenchê-lo novamente
    for row in tree.get_children():
        tree.delete(row)

    # Preencha o Treeview com os registros
    for registro in registros:
        tree.insert('', 'end', values=registro)

    conn.close()

# Crie uma janela principal
root = tk.Tk()
root.title("Formulário de Impressão")

# Crie um frame para o formulário com rótulos acima dos campos
formulario_frame = ttk.LabelFrame(root, text="Informações do Documento")
formulario_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

ci_num_label = ttk.Label(formulario_frame, text="Número da CI:")
ci_num_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
ci_num_entry = ttk.Entry(formulario_frame)
ci_num_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

manifesto_numero_label = ttk.Label(formulario_frame, text="Nº Manifesto:")
manifesto_numero_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
manifesto_numero_entry = ttk.Entry(formulario_frame)
manifesto_numero_entry.grid(row=3, column=0, padx=10, pady=5, sticky="w")

destinatario_label = ttk.Label(formulario_frame, text="Destinatário:")
destinatario_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
destinatario_entry = ttk.Entry(formulario_frame)
destinatario_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

motorista_label = ttk.Label(formulario_frame, text="Motorista:")
motorista_label.grid(row=2, column=2, padx=10, pady=5, sticky="w")
motorista_entry = ttk.Entry(formulario_frame)
motorista_entry.grid(row=3, column=2, padx=10, pady=5, sticky="w")

valor_frete_label = ttk.Label(formulario_frame, text="Valor do Frete:")
valor_frete_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
valor_frete_entry = ttk.Entry(formulario_frame)
valor_frete_entry.grid(row=5, column=0, padx=10, pady=5, sticky="w")

percurso_label = ttk.Label(formulario_frame, text="Percurso:")
percurso_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
percurso_entry = ttk.Entry(formulario_frame)
percurso_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

data_label = ttk.Label(formulario_frame, text="Data:")
data_label.grid(row=4, column=2, padx=10, pady=5, sticky="w")
data_entry = ttk.Entry(formulario_frame)
data_entry.grid(row=5, column=2, padx=10, pady=5, sticky="w")

# Crie um campo de texto para observação que ocupa três colunas
observacao_label = ttk.Label(formulario_frame, text="Observação:")
observacao_label.grid(row=14, column=0, padx=10, pady=5, sticky="w")
observacao_text = tk.Text(formulario_frame, height=5, width=40)
observacao_text.grid(row=15, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")


# Crie um botão para imprimir
imprimir_button = ttk.Button(formulario_frame, text="Imprimir", command=imprimir_formulario)
imprimir_button.grid(row=23, column=0, padx=10, pady=5, sticky="e")

# Crie um botão para salvar
salvar_button = ttk.Button(formulario_frame, text="Salvar", command=salvar_formulario)
salvar_button.grid(row=23, column=1, padx=10, pady=5, sticky="w")



# Crie um Treeview para listar os registros
tree = ttk.Treeview(root, columns=("ci_num", "destinatario", "manifesto_numero", "motorista", "valor_frete", "percurso", "data", "observacao"), show="headings")
tree.heading("ci_num", text="Número da CI")
tree.column("ci_num", width=80)
tree.heading("destinatario", text="Destinatário")
tree.column("destinatario", width=80)
tree.heading("manifesto_numero", text="Nº Manifesto")
tree.heading("motorista", text="Motorista")
tree.heading("valor_frete", text="Valor do Frete")
tree.heading("percurso", text="Percurso")
tree.heading("data", text="Data")
tree.heading("observacao", text="Observação")
tree.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

# Adicione uma barra de rolagem vertical ao Treeview
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.grid(row=1, column=1, padx=0, pady=10, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

# Crie um botão para atualizar a lista de registros no Treeview
atualizar_button = ttk.Button(root, text="Atualizar Registros", command=preencher_treeview)
atualizar_button.grid(row=2, column=0, padx=10, pady=5, sticky="e")

# Preencha inicialmente o Treeview com os registros do banco de dados
preencher_treeview()

# Defina o tamanho da janela principal como um tamanho de modal
root.geometry("800x600")  # Altere as dimensões conforme necessário

# Inicie a interface
root.mainloop()