# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random

SITE_LINK = "https://rastreadordecarga-front.vercel.app/admin"
SITE_RASTREIO = "https://rastreadordecarga-front.vercel.app/carga"
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# gera um valor aleatorio para selecionar cidade
cidades = {2: 'Macapá', 3: 'Belém', 4: 'São Luis', 5: 'Fortaleza', 6: 'Natal', 7: 'Recife', 8: 'Maceió', 9: 'Aracáju', 10: 'Salvador', 11: 'Vitória', 12: 'Rio de Janeiro', 13: 'Santos'}
cidade_origem = random.randint(2, 13)
cidade_destino = random.randint(2, 13)

cidade_att = random.randint(2, 13)
op_att = random.randint(3, 6)

# ano = [2023,2024]
# dia = str(random.randint(1, 30))
# mes = str(random.randint(1, 12))
# ano = str(random.choice(ano))
# data = dia+mes+ano
