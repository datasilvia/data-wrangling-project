from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Paso 1: Configurar Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
driver = webdriver.Chrome(options=options)

# Paso 2: Obtener el contenido de la página web
url = "https://xenera.com/esp/tarifas/luz/unica"
driver.get(url)

# Esperar a que el contenido dinámico se cargue
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.grid.grid-cols-2.gap-x-10.xl\\:pb-10"))
)

# Obtener el HTML de la página
html = driver.page_source
driver.quit()

# Paso 3: Analizar el HTML
soup = BeautifulSoup(html, 'html.parser')

# Paso 4: Extraer la información específica
# Ajustar los selectores CSS según la estructura HTML actual de la página
energia_element = soup.select_one("ul.space-y-2 li")
potencia_element = soup.select_one("div.border-t-primary-light ul li")
coste_gestion_element = soup.select_one("div.border-t-primary-light p.font-bold")

# Verificar que los elementos existen antes de acceder a su texto
energia = energia_element.text.strip() if energia_element else "No encontrado"
potencia = potencia_element.text.strip() if potencia_element else "No encontrado"
coste_gestion = coste_gestion_element.text.strip() if coste_gestion_element else "No encontrado"

# Paso 5: Crear un DataFrame de pandas y guardar los resultados en un CSV
data = {
    "Energía": [energia],
    "Potencia": [potencia],
    "Coste de gestión": [coste_gestion]
}

df = pd.DataFrame(data)
df.to_csv("resultados_tarifas_xenera.csv", index=False)

df

print("Datos guardados en resultados_tarifas_xenera.csv")
