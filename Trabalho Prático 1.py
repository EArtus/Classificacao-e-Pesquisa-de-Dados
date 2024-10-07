from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.kabum.com.br/gamer/playstation/jogos-playstation/playstation-4'
driver.get(url)

time.sleep(10)  

prices = []
price_elements = driver.find_elements(By.CSS_SELECTOR, 'span.priceCard')
print(f"Encontrados {len(price_elements)} valores")
for price_element in price_elements:
    price_text = price_element.get_attribute('innerText').replace('R$', '').replace(',', '.').replace('\xa0', '').strip()
    #print(f"Extracted text: {price_text}")  
    if price_text.replace('.', '', 1).isdigit():
        prices.append(float(price_text))

bubble_sort(prices)

print("Preços ordenados:")
for price in prices:
    print(f'R$ {price:.2f}')

driver.quit()
