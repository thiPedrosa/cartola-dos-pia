from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://dicasdarodada.com/valorizacao-app/')

minimo_para_valorizar = []

time.sleep(5)

for i in range(1,703):
    nome = driver.find_element(By.XPATH, f'//*[@id="footable_180061"]/tbody/tr[{i}]/td[1]').text
    min_val = driver.find_element(By.XPATH, f'//*[@id="footable_180061"]/tbody/tr[{i}]/td[4]').text
    infos = {
        'nome':nome,
        'min_val':min_val
    }
    minimo_para_valorizar.append(infos)

min_val = pd.DataFrame(minimo_para_valorizar)

min_val.to_excel('minimo_para_valorizar.xlsx', index=False)

