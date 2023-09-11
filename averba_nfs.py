from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Substitua '/caminho/para/o/executavel/do/chrome' pelo caminho real
# para o executável do Chrome em seu sistema
chrome_path = '/home/edson/Downloads/cromium/'

# Configurar o WebDriver do Chrome com o caminho especificado
driver = webdriver.Chrome(executable_path=chrome_path)

# URL do site
url = 'https://lonngren.app/'

# Abrir o site no navegador
driver.get(url)

# Localizar e preencher campos de login
username_field = driver.find_element_by_id('usuario')
password_field = driver.find_element_by_id('senha')

# Certifique-se de que os IDs correspondem aos campos reais no site
username_field.send_keys('seu_email')
password_field.send_keys('sua_senha')

# Enviar o formulário de login
password_field.send_keys(Keys.RETURN)

# Aguardar alguns segundos para garantir que a página seja carregada completamente
time.sleep(5)

# Verificar se o login foi bem-sucedido (use verificações específicas para o seu site)
if 'Página de boas-vindas' in driver.page_source:
    print('Login bem-sucedido!')
else:
    print('Login falhou!')

# Fechar o navegador
driver.quit()
