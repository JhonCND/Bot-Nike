from typing import Text
import requests
from bs4 import BeautifulSoup

     #url do site
url = "https://www.nike.com.br/masculino?p=1&Fabricante=&Filtros=Tipo+de+Produto%3ACal%E7ados&cor=&tamanho=&precode=&precoate=&ofertas=sim&ordenacao=5&limit=24&ordemFiltro=Tipo+de+Produto&site_id="
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
     #coletador de sapatos
placas = soup.find_all('div',class_='box-resultados vitrine-vertical grid-produtos grid-produtos--4-col')
placa = placas[0]
     #nome do sapato\\esse get tira o link
marca = placa.find('a',class_='produto__nome').get_text()
link = placa.find('a',class_='produto__nome').attrs['href']

imge = placa.find('div',class_='nao-redireciona produto__cor js-alterna-cor ativo').attrs['data-img']
teste = imge.find(" ", 0,)
img = imge[:teste]

preco = placa.find('span',class_='produto__preco_por ws-nr').get_text()
cores = placa.find('a',class_='produto__cores').get_text().strip()
estilo = placa.find('a',class_='produto__descricaocurta').get_text().strip()
porcetagem = placa.find('span',class_='produto__percentdesconto percental_desconto ws-nr').get_text().replace(" ", "")
