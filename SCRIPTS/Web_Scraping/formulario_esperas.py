from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Inicializar el driver de Firefox
driver = webdriver.Firefox()

try:
    # Abrir la página del formulario
    driver.get('http://127.0.0.1:5500/ALUMNOS/SCRIPTS/Web_Scraping/formulario.html')

    # Esperar a que aparezca el formulario
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'nombre')))

    # Rellenar el formulario
    driver.find_element(By.NAME, 'nombre').send_keys('TuNombre')
    time.sleep(2)  # Esperar 2 segundos
    driver.find_element(By.NAME, 'apellido').send_keys('TuApellido')
    time.sleep(2)
    driver.find_element(By.NAME, 'email').send_keys('tu@email.com')
    time.sleep(2)
    fecha_nacimiento_input = driver.find_element(By.ID, "fecha_nacimiento")
    fecha_nacimiento_input.send_keys("1990-01-01")
    time.sleep(2)
    domicilio_input = driver.find_element(By.ID, "domicilio")
    domicilio_input.send_keys("123 Main Street")
    time.sleep(2)

    # Seleccionar la cantidad de entradas
    cantidad_entradas = driver.find_element(By.NAME, 'cantidad')
    cantidad_entradas.clear()
    cantidad_entradas.send_keys('2')
    time.sleep(2)

    # Seleccionar el método de pago
    metodo_pago_dropdown = Select(driver.find_element(By.NAME, 'metodo_pago'))
    time.sleep(2)
    metodo_pago_dropdown.select_by_value('paypal')
    time.sleep(2)

    # Seleccionar asientos
    driver.find_element(By.NAME, 'asientos[]').click()  # Marcar el primer asiento
    time.sleep(2)

    # Enviar el formulario
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    # Esperar un momento para ver los resultados
    WebDriverWait(driver, 10).until(EC.title_contains('Confirmation'))  # Esperar a que aparezca "Confirmation" en el título


finally:
    # Cerrar el navegador al finalizar
    driver.quit()
