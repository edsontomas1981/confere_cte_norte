import tkinter as tk
from tkinter import ttk
from main_comunicacao_interna import ci_janela
from main import relat_carregamentos

# Função para criar uma nova janela filha
def form_mdi_ci():
    janela_secundaria = tk.Toplevel(root)
    janela_secundaria.title("Comunicação Interna")
    ci_janela(janela_secundaria)  # Passe a janela secundária como argumento para a função ci_janela

def form_mdi_estatistica_carregamento():
    janela_secundaria = tk.Toplevel(root)
    janela_secundaria.title("Estatística de Carregamento")
    relat_carregamentos(janela_secundaria)  # Passe a janela secundária como argumento para a função relat_carregamentos

# Função para sair do aplicativo
def sair():
    root.quit()

# Configuração da janela principal
root = tk.Tk()
root.title("Interface MDI")

# Obtém as dimensões da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Define o tamanho da janela principal para ocupar toda a tela
root.geometry(f"{largura_tela}x{altura_tela}")

# Barra de menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Menu "Arquivo"
menu_arquivo = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Comunicação Interna", command=form_mdi_ci)
menu_arquivo.add_command(label="Estatística de Carregamento", command=form_mdi_estatistica_carregamento)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=sair)

root.mainloop()
