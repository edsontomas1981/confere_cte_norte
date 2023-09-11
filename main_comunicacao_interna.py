import tkinter as tk
from tkinter import ttk
from comunicacao_interna import imprimir_ci
import webbrowser
import sqlite3
from tkcalendar import Calendar
from ttkthemes import ThemedStyle
from datetime import datetime
import locale
import re

def ci_janela(root):
    def salvar_formulario():
        conn = sqlite3.connect('bd_norte.db')
        cursor = conn.cursor()
        
        isca_1 = isca_1_entry.get()
        isca_2 = isca_2_entry.get()    
        destinatario = destinatario_entry.get()
        manifesto_numero = manifesto_numero_entry.get()
        motorista = motorista_entry.get()
        valor_frete = float(valor_frete_entry.get())
        percurso = percurso_entry.get()
        data = data_entry.get()
        observacao = observacao_text.get("1.0", "end-1c")

        # Verificar se o registro já existe com base em algum critério, como o manifesto_numero
        cursor.execute("SELECT * FROM comunicacao_interna WHERE manifesto_numero=?", (manifesto_numero,))
        existing_record = cursor.fetchone()

        if existing_record:
                cursor.execute("UPDATE comunicacao_interna SET destinatario=?, motorista=?, valor_frete=?, percurso=?, data=?, observacao=?, isca_1=?, isca_2=? WHERE manifesto_numero=?",
                (destinatario, motorista, valor_frete, percurso, data, observacao, isca_1, isca_2, manifesto_numero))
        else:   
            # Inserir um novo registro
            cursor.execute("INSERT INTO comunicacao_interna (destinatario, manifesto_numero, motorista, valor_frete, percurso, data, observacao,isca_1,isca_2) VALUES (?, ?, ?, ?, ?, ?, ?,?,?)",
                        (destinatario, manifesto_numero, motorista, valor_frete, percurso, data, observacao,isca_1,isca_2))

        conn.commit()
        conn.close()

        preencher_treeview()

        preencher_campos_por_manifesto(manifesto_numero)


    def preencher_campos_por_manifesto(numero_manifesto):
        conn = sqlite3.connect('bd_norte.db')
        cursor = conn.cursor()

        # Execute uma consulta para recuperar os registros com base no número do manifesto
        cursor.execute("SELECT * FROM comunicacao_interna WHERE manifesto_numero=?", (numero_manifesto,))
        registro = cursor.fetchone()

        if registro:

            ci_num_label.config(text=f"CI Nº : {registro[0]}")

            # Preencha os campos do formulário com os valores obtidos do banco de dados
            isca_1_entry.delete(0, tk.END)
            isca_1_entry.insert(0, registro[8])  # Preencha o campo "1º Isca"
            
            isca_2_entry.delete(0, tk.END)
            isca_2_entry.insert(0, registro[9])  # Preencha o campo "2º Isca"
            
            manifesto_numero_entry.delete(0, tk.END)
            manifesto_numero_entry.insert(0, registro[2])  # Preencha o campo "Nº Manifesto"
            
            destinatario_entry.delete(0, tk.END)
            destinatario_entry.insert(0, registro[1])  # Preencha o campo "Destinatário"
            
            motorista_entry.delete(0, tk.END)
            motorista_entry.insert(0, registro[3])  # Preencha o campo "Motorista"
            
            valor_frete_entry.delete(0, tk.END)
            valor_frete_entry.insert(0, registro[4])  # Preencha o campo "Valor do Frete"
            
            percurso_entry.delete(0, tk.END)
            percurso_entry.insert(0, registro[5])  # Preencha o campo "Percurso"
            
            data_entry.delete(0, tk.END)
            data_entry.insert(0, registro[6])  # Preencha o campo "Data"
            
            observacao_text.delete("1.0", tk.END)
            observacao_text.insert("1.0", registro[7])  # Preencha o campo "Observação"

        conn.close()



    # Função para pegar a data selecionada e ocultar o calendário
    def pegar_data(event):
        selected_date = cal.get_date()
        data_obj = datetime.strptime(selected_date, "%Y-%m-%d")  # Converter a data para um objeto datetime
        formatted_date = data_obj.strftime("%d/%m/%Y")  # Formatar a data como dd/mm/yyyy
        data_entry.delete(0, tk.END)  # Limpar o campo de entrada anterior
        data_entry.insert(0, formatted_date)  # Inserir a data formatada no campo de entrada
        cal.place_forget()  # Ocultar o calendário após a data ser selecionada

    def fechar_janela():
        root.quit()
        root.destroy()

    def excluir_registro():
        # Obtenha o número do manifesto inserido pelo usuário
        numero_manifesto = manifesto_numero_entry.get()

        # Conecte-se ao banco de dados
        conn = sqlite3.connect('bd_norte.db')
        cursor = conn.cursor()

        # Exclua todos os registros com base no número do manifesto
        cursor.execute("DELETE FROM comunicacao_interna WHERE manifesto_numero=?", (numero_manifesto,))
        conn.commit()

        # Feche a conexão com o banco de dados
        conn.close()

        # Atualize o Treeview para refletir as exclusões
        preencher_treeview()  

        limpar_campos()      

        # Limpe o campo de entrada
        manifesto_numero_entry.delete(0, tk.END)

    def imprimir_formulario():
        ci_num = re.search(r'\d+', ci_num_label.cget("text"))
        ci_num = ci_num.group(0)
        isca_1 = isca_1_entry.get()
        isca_2 = isca_2_entry.get()
        destinatario = destinatario_entry.get()
        manifesto_numero = manifesto_numero_entry.get()
        motorista = motorista_entry.get()
        valor_frete = valor_frete_entry.get()
        percurso = percurso_entry.get()
        data = data_entry.get()
        observacao = observacao_text.get("1.0", "end-1c")

        pdf_filename = f"ciManif{manifesto_numero}.pdf"

        dados_imprimir = {"ci_num":ci_num,
                        "isca_1":isca_1,
                        "isca_2":isca_2,
                        "destinatario":destinatario,
                        "manifesto_numero":manifesto_numero,
                        "motorista":motorista,
                        "valor_frete":valor_frete,
                        "percurso":percurso,
                        "data":data,
                        "observacao":observacao,
                        "pdf_filename":pdf_filename
                        }

        # Chame a função com os novos campos
        imprimir_ci(dados_imprimir)

        # Após gerar o PDF, abrir automaticamente para impressão
        try:
            webbrowser.open(pdf_filename)
        except Exception as e:
            print(f"Erro ao abrir o PDF: {e}")

    # Função para preencher o Treeview com os registros do banco de dados
    def preencher_treeview():
        conn = sqlite3.connect('bd_norte.db')
        cursor = conn.cursor()

        # Execute uma consulta para recuperar todos os registros
        cursor.execute("SELECT * FROM comunicacao_interna")
        registros = cursor.fetchall()

        # Limpe o Treeview antes de preenchê-lo novamente
        for row in tree.get_children():
            tree.delete(row)

        # Preencha o Treeview com os registros
        for registro in registros:
            tree.insert('', 'end', values=registro)

        conn.close()

    def preencher_campos_selecionados(event):
        selected_item = tree.selection()[0]  # Obtém o item selecionado
        values = tree.item(selected_item, 'values')  # Obtém os valores do item selecionado
        ci_num_label.config(text=f"CI Nº : {values[0]}")
        manifesto_numero_entry.delete(0, tk.END)
        manifesto_numero_entry.insert(0, values[2])  # Preencha o campo "Nº Manifesto"
        destinatario_entry.delete(0, tk.END)
        destinatario_entry.insert(0, values[1])  # Preencha o campo "Destinatário"
        motorista_entry.delete(0, tk.END)
        motorista_entry.insert(0, values[3])  # Preencha o campo "Motorista"
        valor_frete_entry.delete(0, tk.END)
        valor_frete_entry.insert(0, values[4])  # Preencha o campo "Valor do Frete"
        percurso_entry.delete(0, tk.END)
        percurso_entry.insert(0, values[5])  # Preencha o campo "Percurso"
        data_entry.delete(0, tk.END)
        data_entry.insert(0, values[6])  # Preencha o campo "Data"
        observacao_text.delete("1.0", tk.END)
        observacao_text.insert("1.0", values[7])  # Preencha o campo "Observação"
        isca_1_entry.delete(0, tk.END)
        isca_1_entry.insert(0, values[8])  # Preencha o campo "ISCA 1"
        isca_2_entry.delete(0, tk.END)  
        isca_2_entry.insert(0, values[9])  # Preencha o campo "ISCA 2"

    # Função para mostrar o calendário quando o foco estiver no campo de data
    def mostrar_calendario(event):
        x, y, _, _ = data_entry.bbox("insert")  # Obtém as coordenadas do cursor no campo de data
        x += 550  # Calcula a posição x absoluta ajustada para a esquerda
        y += 310 # Calcula a posição y absoluta ajustada para cima
        cal.place(x=x, y=y, anchor="sw")  # Posiciona o calendário à esquerda e acima do campo de data

    # Função para formatar o valor do frete como moeda brasileira
    def formatar_valor_frete(valor):
        try:
            # Converter o valor para um número de ponto flutuante
            valor = float(valor)
            # Formatar o valor como moeda brasileira
            valor_formatado = locale.currency(valor, grouping=True, symbol=None)
            return valor_formatado
        except ValueError:
            return valor  # Retorna o valor original se não for um número válido


    # Função para aplicar a máscara quando o campo perder o foco
    def aplicar_mascara(event):
        valor_frete = valor_frete_var.get()
        valor_formatado = formatar_valor_frete(valor_frete)
        valor_frete_var.set(valor_formatado)

    # Função para validar a entrada e permitir apenas números e um ponto decimal
    def validar_entrada(event):
        # Obtém o texto atual no campo
        texto = valor_frete_entry.get()

        # Verifica cada caractere no texto
        novo_texto = ''
        for char in texto:
            # Se o caractere for um dígito ou um ponto decimal, adiciona ao novo texto
            if char.isdigit() or char == '.':
                novo_texto += char

        # Define o novo texto no campo
        valor_frete_entry.delete(0, tk.END)
        valor_frete_entry.insert(0, novo_texto)

    def limpar_campos():
        # Limpar os campos de entrada
        ci_num_label.config(text=f"CI Nº : ")
        isca_1_entry.delete(0, tk.END)
        isca_2_entry.delete(0, tk.END)
        manifesto_numero_entry.delete(0, tk.END)
        destinatario_entry.delete(0, tk.END)
        motorista_entry.delete(0, tk.END)
        valor_frete_entry.delete(0, tk.END)
        percurso_entry.delete(0, tk.END)
        data_entry.delete(0, tk.END)

        # Limpar o campo de texto
        observacao_text.delete("1.0", tk.END)

    # Crie uma janela principal
    # root = tk.Tk()
    # Crie um estilo personalizado para a janela
    style = ThemedStyle(root)
    style.set_theme("clearlooks")
    root.title("Formulário de Impressão")

    # Crie um frame para o formulário com rótulos acima dos campos
    formulario_frame = ttk.LabelFrame(root, text="Informações do Documento")
    formulario_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configure a janela para tela cheia
    # root.geometry(f"{largura_tela}x{altura_tela}")
    root.geometry("960x600")


    # Crie um botão para imprimir
    imprimir_button = ttk.Button(formulario_frame, text=" Imprimir ", command=imprimir_formulario, width=15)
    imprimir_button.grid(row=5, column=4, padx=10, pady=5, sticky="e")

    # Crie um botão para salvar
    salvar_button = ttk.Button(formulario_frame, text=" Salvar ", command=salvar_formulario, width=15)
    salvar_button.grid(row=3, column=4, padx=10, pady=5, sticky="w")

    # Crie um botão de exclusão
    excluir_button = ttk.Button(formulario_frame, text=" Excluir ", command=excluir_registro, width=15)
    excluir_button.grid(row=4, column=4, columnspan=2, padx=10, pady=5, sticky="w")

    # Crie um botão para chamar a função de limpar campos
    limpar_button = ttk.Button(formulario_frame, text=" Limpar ", command=limpar_campos, width=15)
    limpar_button.grid(row=6, column=4, padx=10, pady=5, sticky="w")



    ci_num_label = ttk.Label(formulario_frame, text="CI Nº : ")
    ci_num_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    # Crie uma variável de controle para o campo "Valor do Frete"
    isca_1_label = ttk.Label(formulario_frame, text="1º Isca:")
    isca_1_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    isca_1_entry = ttk.Entry(formulario_frame)
    isca_1_entry.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    # Crie uma variável de controle para o campo "Valor do Frete"
    isca_2_label = ttk.Label(formulario_frame, text="2º Isca:")
    isca_2_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    isca_2_entry = ttk.Entry(formulario_frame)
    isca_2_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")


    manifesto_numero_label = ttk.Label(formulario_frame, text="Nº Manifesto:")
    manifesto_numero_label.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    manifesto_numero_entry = ttk.Entry(formulario_frame)
    manifesto_numero_entry.grid(row=3, column=2, padx=10, pady=5, sticky="w")

    # Crie uma variável de controle para o campo "Valor do Frete"
    valor_frete_var = tk.StringVar()

    valor_frete_label = ttk.Label(formulario_frame, text="Valor do Frete:")
    valor_frete_label.grid(row=2, column=3, padx=10, pady=5, sticky="w")
    valor_frete_var = tk.DoubleVar()  # Usando DoubleVar para armazenar o valor como número de ponto flutuante
    valor_frete_entry = ttk.Entry(formulario_frame, textvariable=valor_frete_var)
    valor_frete_entry.grid(row=3, column=3, padx=10, pady=5, sticky="w")

    valor_frete_entry.bind("<KeyRelease>", validar_entrada)

    # Associe a função aplicar_mascara ao evento de perda de foco no campo "Valor do Frete"
    valor_frete_entry.bind("<FocusOut>",aplicar_mascara)

    destinatario_label = ttk.Label(formulario_frame, text="Destinatário:")
    destinatario_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    destinatario_entry = ttk.Entry(formulario_frame)
    destinatario_entry.grid(row=5, column=0, padx=10, pady=5, sticky="w")

    motorista_label = ttk.Label(formulario_frame, text="Motorista:")
    motorista_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    motorista_entry = ttk.Entry(formulario_frame)
    motorista_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    percurso_label = ttk.Label(formulario_frame, text="Percurso:")
    percurso_label.grid(row=4, column=2, padx=10, pady=5, sticky="w")
    percurso_entry = ttk.Entry(formulario_frame)
    percurso_entry.grid(row=5, column=2, padx=10, pady=5, sticky="w")

    # Label para "Data:"
    data_label = ttk.Label(formulario_frame, text="Data:")
    data_label.grid(row=4, column=3, padx=10, pady=5, sticky="w")

    # Campo de entrada para a data
    data_entry = ttk.Entry(formulario_frame)
    data_entry.grid(row=5, column=3, padx=10, pady=5, sticky="w")

    # Crie o calendário
    cal = Calendar(formulario_frame, selectmode="day", date_pattern="yyyy-mm-dd")
    # cal.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

    # Crie um campo de texto para observação que ocupa três colunas
    observacao_label = ttk.Label(formulario_frame, text="Observação:")
    observacao_label.grid(row=14, column=0, padx=10, pady=5, sticky="w")
    observacao_text = tk.Text(formulario_frame, height=5, width=40)
    observacao_text.grid(row=15, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

    # Crie um Treeview para listar os registros
    tree = ttk.Treeview(root, columns=("ci_num", "destinatario", "manifesto_numero", "motorista", "valor_frete", 
                                    "percurso", "data", "observacao","isca_1","isca_2"), show="headings", height=7)
    tree.heading("ci_num", text="CI Nº")
    tree.column("ci_num", width=80)
    tree.heading("destinatario", text="Destinatário")
    tree.column("destinatario", width=90)
    tree.heading("manifesto_numero", text="Manifesto")
    tree.column("manifesto_numero", width=80)
    tree.heading("motorista", text="Motorista")
    tree.column("motorista", width=100)
    tree.heading("valor_frete", text="Frete")
    tree.column("valor_frete", width=80)
    tree.heading("percurso", text="Percurso")
    tree.column("percurso", width=80)
    tree.heading("data", text="Data")
    tree.column("data", width=80)
    tree.heading("observacao", text="Observação")
    tree.column("observacao", width=80)
    tree.heading("isca_1", text="1º Isca")
    tree.column("isca_1", width=80)
    tree.heading("isca_2", text="2º Isca")
    tree.column("isca_2", width=80)
    tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Associe a função preencher_campos_selecionados ao evento de seleção no Treeview
    tree.bind("<Double-1>", preencher_campos_selecionados)

    # Associe a função mostrar_calendario ao evento de foco no campo de data
    data_entry.bind("<FocusIn>", mostrar_calendario)

    # Associe a função pegar_data para atualizar o campo de data quando uma data for selecionada no calendário
    cal.bind("<<CalendarSelected>>", pegar_data)

    # Barra de rolagem vertical para o Treeview
    vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Grid para os componentes
    formulario_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    vsb.grid(row=1, column=1, sticky="ns")

    # Preenche inicialmente o Treeview com os registros do banco de dados
    preencher_treeview()

    # Inicie a interface
    root.mainloop()