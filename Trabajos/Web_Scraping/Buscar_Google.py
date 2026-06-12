from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializamos el driver
driver = webdriver.Firefox()

# Cargar una página web de ejemplo
driver.get('https://www.google.com')
time.sleep(5)

# Aceptar cookies
try:
    cookies_button = driver.find_element(By.ID, 'L2AGLb')  # Utilizando ID en lugar de CSS_SELECTOR
    driver.execute_script("arguments[0].scrollIntoView();", cookies_button)
    cookies_button.click()
except Exception as e:
    print(f"Error al hacer clic en cookies: {e}")

# Realizar acciones en la página (por ejemplo, buscar en Google)
search_box = driver.find_element(By.XPATH, "//textarea[@class = 'gLFyf']")
search_box.send_keys('Selenium with Python')
search_box.submit()

# Esperar unos segundos para que puedas ver la acción (opcional)
time.sleep(30)

# Cerrar el navegador
driver.quit()
