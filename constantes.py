from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random

SITE_LINK = "https://rastreadordecarga-front.vercel.app/admin"
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# gera um valor aleatorio para selecionar cidade
cidade_origem = random.randint(2, 13)
cidade_destino = random.randint(2, 13)

cidade_att = random.randint(2, 13)
op_att = random.randint(3, 6)


# ano = [2023,2024]
# dia = str(random.randint(1, 30))
# mes = str(random.randint(1, 12))
# ano = str(random.choice(ano))
# data = dia+mes+ano
