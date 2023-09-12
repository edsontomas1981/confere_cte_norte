from selenium import webdriver
import time

# Inicializa o WebDriver do Chrome
browser = webdriver.Chrome()

# Abre o site alvo
browser.get("https://www.uol.com.br/")

# Aguarda um período de tempo para que a página carregue completamente
# time.sleep(10)

# Localiza os elementos de entrada de texto (nome de usuário e senha) e o botão de login
username = browser.find_element_by_id("lmfcl4xk")
# password = browser.find_element_by_id("senha")
# login_button = browser.find_element_by_xpath("//*[@type='submit']")

# Preenche os campos de nome de usuário e senha
# username.send_keys("edson@nor")
# password.send_keys("analu1710")

# Clica no botão de login
# login_button.click()
print(username)
# Aguarda um tempo para que a página de login seja processada (pode ser necessário ajustar esse valor)
# time.sleep(5)

# Verifica se o login foi bem-sucedido (você pode adicionar sua própria lógica aqui)
if "Página inicial" in browser.title:
    print("Login bem-sucedido!")
else:
    print("Falha no login.")

# Fecha o navegador
browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def fazer_login(usuario, senha):
#     # Configurar o caminho para o executável do ChromeDriver
#     chromedriver_path = '/home/edson/Downloads/conferencia_ctes/chrome/chromedriver'

#     # Configurar as opções do Chrome (opcional)
#     chrome_options = webdriver.ChromeOptions()
#     # Você pode configurar opções adicionais, como headless mode, aqui.

#     # Inicialize o driver do Chrome com o caminho correto e as opções
#     driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

#     # Abra a página de login do site
#     driver.get('https://lonngren.app/')

#     try:
#         # Encontre os campos de entrada de usuário e senha e insira as informações
#         usuario_input = driver.find_element_by_id('usuario')
#         usuario_input.send_keys(usuario)

#         senha_input = driver.find_element_by_id('senha')
#         senha_input.send_keys(senha)

#         # Envie o formulário de login
#         senha_input.submit()

#         # Aguarde até que a página de login seja processada
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, 'td2'))
#         )

#         # O login foi bem-sucedido
#         print("Login bem-sucedido!")

#     except Exception as e:
#         # Algo deu errado
#         print("Erro durante o login:", str(e))

#     finally:
#         # Feche o navegador
#         driver.quit()

# # Substitua 'edson@nor' e 'analu1710' pelas informações reais de login
# fazer_login('edson@nor', 'analu1710')
