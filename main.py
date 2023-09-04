import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from verifica_inconsistencias_cte import verifica_cte
from main_confere_ctes import gera_dict

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    pasta_entry.delete(0, tk.END)
    pasta_entry.insert(0, pasta)

def processar_dados():
    pasta = pasta_entry.get()
    filial = filial_combobox.get()
    valor_minimo = float(valor_minimo_entry.get())
    valor_maximo = float(valor_maximo_entry.get())
    
    ctes,ctes_1 = gera_dict(pasta)
        
    # Lógica de processamento dos dados com base nas configurações escolhidas.
    dados = verifica_cte(ctes)
    # Limpar dados anteriores na Treeview
    for row in tree.get_children():
        tree.delete(row)
    
    # Adicionar os dados à Treeview com cores alternadas
    for i, (cte, descricao, valor) in enumerate(dados, start=1):
        if i % 2 == 0:
            tree.insert("", "end", values=(cte, descricao, valor), tags=("even",))
        else:
            tree.insert("", "end", values=(cte, descricao, valor), tags=("odd",))

# Configuração da janela principal
root = tk.Tk()
root.title("Configurações de Frete")

# Frame para organizar os widgets
frame = ttk.Frame(root, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Label e Entry para a pasta
pasta_label = ttk.Label(frame, text="Pasta:")
pasta_label.grid(column=0, row=0, sticky=tk.W)

pasta_entry = ttk.Entry(frame, width=40)
pasta_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

selecionar_pasta_button = ttk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta)
selecionar_pasta_button.grid(column=2, row=0, sticky=tk.W)

# ComboBox para a filial
filial_label = ttk.Label(frame, text="Filial:")
filial_label.grid(column=0, row=1, sticky=tk.W)

filial_combobox = ttk.Combobox(frame, values=["Filial 1", "Filial 2", "Filial 3"])
filial_combobox.grid(column=1, row=1, sticky=(tk.W, tk.E))
filial_combobox.set("Filial 1")

# Label e Entry para valor mínimo e máximo
valor_minimo_label = ttk.Label(frame, text="Valor Mínimo por Kg:")
valor_minimo_label.grid(column=0, row=2, sticky=tk.W)

valor_minimo_entry = ttk.Entry(frame, width=10)
valor_minimo_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))
valor_minimo_entry.insert(0, "0.00")

valor_maximo_label = ttk.Label(frame, text="Valor Máximo por Kg:")
valor_maximo_label.grid(column=0, row=3, sticky=tk.W)

valor_maximo_entry = ttk.Entry(frame, width=10)
valor_maximo_entry.grid(column=1, row=3, sticky=(tk.W, tk.E))
valor_maximo_entry.insert(0, "10.00")

# Botão para enviar as configurações e processar os dados
enviar_button = ttk.Button(frame, text="Enviar Configurações", command=processar_dados)
enviar_button.grid(column=1, row=4, sticky=tk.W)

# Treeview para exibir os dados processados com barra de rolagem
tree = ttk.Treeview(frame, columns=("Item", "Descrição", "Valor"), show="headings")
tree.grid(column=0, row=5, columnspan=3, sticky=(tk.W, tk.E))
tree.heading("#1", text="Cte")
tree.heading("#2", text="Descrição")
tree.heading("#3", text="Valor")

# Tags para cores alternadas
tree.tag_configure("even", background="lightgray")
tree.tag_configure("odd", background="white")

# Barra de rolagem vertical
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar.grid(column=3, row=5, sticky=(tk.N, tk.S))
tree.configure(yscrollcommand=scrollbar.set)

# Configuração do redimensionamento
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame.columnconfigure(1, weight=1)

root.mainloop()
