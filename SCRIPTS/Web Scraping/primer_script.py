import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# Utiliza barras invertidas dobles o una barra invertida cruda
path = r'C:\Users\Javi P. Piazza\OneDrive\Documents\DOCUMENTOS\INFORMATICA\DATA SCIENCE\GIT\ALUMNOS\SCRIPTS\Web Scraping\chromedriver.exe'

# Crea un objeto Options
options = Options()

# Crea un objeto Service
service = ChromeService(executable_path=path)

# Inicializa el driver de Chrome con el objeto Options y Service
driver = webdriver.Chrome(service=service, options=options)

driver.get('http://www.google.com/')

time.sleep(100) # Espera para que el usuario pueda ver algo!

search_box = driver.find_elements_by_class_name('RNNXgb')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(100) # Espera para que el usuario pueda ver algo!

driver.quit()
