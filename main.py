from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from constantes import *
from auxs import *

def checar_dash(id_tabela, cod_rastreio):
    time.sleep(2)
    navegador.get(SITE_LINK)
    navegador.find_element('xpath', '//*[@id="__next"]/div/button').click()
    navegador.find_element('xpath', '//*[@id="__next"]/div/button').click()
    time.sleep(2)
    try:
        navegador.find_element('xpath', '/html/body/div/div/div[1]/ul/li[2]/button').click()
    except(Exception):
        print(f'erro ao tentar clicar no dashboard \n{Exception}')

    cargas = navegador.find_elements(By.ID, id_tabela)

    if cod_rastreio in cargas[0].text:
        return True

    else: return False


# cadastra nova carga
def nova_carga():
    escrever_log("Executando cadastro de nova carga")
    navegador.get(SITE_LINK)
    navegador.find_element('xpath', f'//*[@id="formCriarcarga"]/select[1]/option[{cidade_origem}]').click()
    navegador.find_element('xpath', f'//*[@id="formCriarcarga"]/select[2]/option[{cidade_destino}] ').click()
    navegador.find_element('xpath', '//*[@id="formCriarcarga"]/input ').send_keys('15062023')
    navegador.find_element('xpath', '//*[@id="formCriarcarga"]/button').click()

    # Pega o cod rastreio do pop-up.
    alert = lambda x: WebDriverWait(x, 5).until(EC.alert_is_present())
    time.sleep(1)
    cod_rastreio = alert(navegador).text
    escrever_log(f"\nCarga Criada.\nCódigo de Rastreio:{cod_rastreio}\n")
    alert(navegador).accept()

    #checar se a nova carga aparece no dashboard em cargas não roteadas
    resultado = checar_dash("tabelaSemRastreio", cod_rastreio)
    if resultado:
        escrever_log("\n-----------RESULTADO-----------:\nTeste Bem-Sucedido. Carga Cadastrada com Sucesso\n\n")
    else:
        escrever_log("\n-----------RESULTADO-----------:\n. Teste Falhou. A Função de adicionar carga não está funcionando corretamente\n")

    atualizar_carga(cod_rastreio)


# teste AtualizarCarga (ação Reivindicar)
def atualizar_carga(cod_rastreio):
    escrever_log(f"\nExecutando Atualização da carga: {cod_rastreio}\n")
    navegador.get(SITE_LINK)
    navegador.find_element('xpath', '//*[@id="__next"]/div/button').click()
    navegador.find_element('xpath', '//*[@id="__next"]/div/button').click()
    time.sleep(2)
    try:
        navegador.find_element('xpath', '/html/body/div/div/div[1]/ul/li[3]/button').click()
    except(Exception):
        print(f'erro ao clicar em atualizar carga {Exception}')

    navegador.find_element('xpath', '//*[@id="formAtualizarCarga"]/input').send_keys(cod_rastreio)
    navegador.find_element('xpath', f'//*[@id="formAtualizarCarga"]/select[1]/option[2]').click()
    navegador.find_element('xpath', f'//*[@id="formAtualizarCarga"]/select[2]/option[4]').click()
    navegador.find_element('xpath', '//*[@id="formAtualizarCarga"]/button').click()

    # checar se a carga mudou para Cargas Reivindicadas
    resultado = checar_dash("tabelaEntregada", cod_rastreio)

    if resultado:
        escrever_log("\n-----------RESULTADO-----------:\nTeste Bem-Sucedido. Carga Atualizada com Sucesso\n")
    else:
        escrever_log("\n-----------RESULTADO-----------:\nTeste Falhou. A Função de Atualizar Carga não está funcionando corretamente")

    consultar_carga(cod_rastreio)

def consultar_carga(cod_rastreio):
    escrever_log(f"\n\nExecutando CONSULTA da carga: {cod_rastreio}\n")

    navegador.get(f'{SITE_RASTREIO}/{cod_rastreio}')
    time.sleep(1)
    informacoes_carga = navegador.find_elements('xpath', '//*[@id="__next"]/div/div/div')
    informacoes_existentes = [cod_rastreio, '15/06/2023', cidades[cidade_origem], cidades[cidade_destino],'carga registrada', 'Reivindicar' ]
    resultado = False
    print(f'info da carga\n{informacoes_carga[0].text}')
    #verificar se todas as informações cadastradas estão na pagina
    for i in informacoes_existentes:
        if str(i) in informacoes_carga[0].text:
            resultado = True
    if resultado:
        escrever_log("\n-----------RESULTADO-----------:\nTeste Bem-Sucedido. Informações da Carga estão coerentes")
    else:
        escrever_log("\n-----------RESULTADO-----------:\nTeste Falhou. A Consulta da carga não está funcionando  corretamente")


if __name__ == '__main__':
        nova_carga()


