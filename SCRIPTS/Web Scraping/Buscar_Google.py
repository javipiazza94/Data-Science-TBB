from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializamos el driver
driver = webdriver.Firefox()

# Cargar una página web de ejemplo
driver.get('https://www.google.com')
time.sleep(5)
cookies = driver.find_element(By.CSS_SELECTOR, 'button#L2AGLb')
cookies.click()
time.sleep(5)

# Realizar acciones en la página (por ejemplo, buscar en Google)
search_box = driver.find_element(By.XPATH, "//textarea[@class = 'gLFyf']")  # Buscar por css
search_box.send_keys('Selenium with Python')
search_box.submit()

# Esperar unos segundos para que puedas ver la acción (opcional)
time.sleep(30)

# Cerrar el navegador
driver.quit()
