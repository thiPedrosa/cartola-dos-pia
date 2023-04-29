import requests
import urllib.request
from PIL import Image
import time

url = 'https://api.cartolafc.globo.com/atletas/mercado'

response = requests.get(url)
data = response.json()

clubes = data['clubes']

for clube in clubes:
    infos_clube = clubes[f'{clube}']
    nome_time = infos_clube['nome_fantasia']
    link_escudo = infos_clube['escudos']['30x30']
    urllib.request.urlretrieve(link_escudo, f'C:\\Users\\Usuario\\Documents\\C4rT0La\\cartola-dos-pia\\pasta_do_ber\\escudos\\{nome_time}.png')




