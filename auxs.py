import datetime

moment = datetime.datetime.now().strftime("%A %d %B %y %I:%M")
moment = str(datetime.datetime.now().strptime(moment, "%A %d %B %y %I:%M")).replace(':', '-')
nome_arquivo = f"teste_aplicacao {moment}.txt"


def escrever_log(texto):
    arquivo = open(nome_arquivo, "a")
    arquivo.write(texto)