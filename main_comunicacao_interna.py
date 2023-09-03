import tkinter as tk
from tkinter import ttk
from comunicacao_interna import imprimir_ci
import webbrowser

def salvar_formulario():
    # Adicione aqui a lógica para salvar os dados do formulário
    pass

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


# Defina o tamanho da janela principal como um tamanho de modal
root.geometry("570x410")  # Altere as dimensões conforme necessário

# Inicie a interface
root.mainloop()